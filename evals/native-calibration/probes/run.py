"""Run fresh three-way controls; never repair or overwrite a preserved attempt."""
import hashlib
import json
import re
import subprocess
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
BASE = ROOT / "evals/results/native-calibration"
EX = ROOT / "code-examples/platforms"
MODES = ("positive", "alternative", "mutant")
METHODS = {
    "Field": ("testLiveEdit", "obsolete field reply accepted"),
    "Sheet": ("testSurvivingOrigin", "eligible origin survives close"),
    "Responder": ("testAttachedRefusal", "attached ineligible origin must yield to fallback"),
}


def digest(data):
    return hashlib.sha256(data).hexdigest()


def cmd(*args):
    return subprocess.check_output(args, text=True).strip()


def replace(text, old, new):
    if text.count(old) != 1:
        raise ValueError(f"Source no longer matches: {old}")
    return text.replace(old, new)


def subject(platform, family, mode):
    if family == "Sheet":
        path = "SheetAlternative.swift" if mode == "alternative" else "SheetSubject.swift"
        s = (HERE / path).read_text()
        if mode == "mutant":
            s = replace(s, 'available.contains(pending.origin) ? pending.origin : "fallback"',
                        'visible.flatMap { available.contains($0) ? $0 : nil } ?? "fallback"')
    elif family == "Field":
        s = (EX / f"{platform.lower()}-closure-v1/Sources/AsyncOwnership.swift").read_text()
        guard = "guard self.snapshot == input else { self.cancel(); return }"
        if mode == "alternative":
            # Validate each captured field through its native control rather than rebuilding a snapshot.
            s = replace(s, guard, 'if input.contains(where: { self.fields[$0.key]?.text ?? "" != $0.value }) { self.cancel(); return }')
        elif mode == "mutant":
            s = replace(s, guard, "")
    else:
        s = (EX / "macos-lifecycle-v1/Sources/DesktopLifecycle.swift").read_text()
        if mode == "alternative":
            s = replace(s, "eligible(primary) ? primary : eligible(fallback) ? fallback : nil",
                        "[primary, fallback].compactMap { $0 }.first { eligible($0) }")
        elif mode == "mutant":
            s = replace(s, " && target.acceptsFirstResponder", "")
    return s


def run():
    BASE.mkdir(exist_ok=True)
    batch = Path(tempfile.mkdtemp(prefix="qualification-", dir=BASE))
    devices = json.loads(cmd("xcrun", "simctl", "list", "devices", "booted", "-j"))["devices"]
    for platform, sdk, families in [
        ("macOS", "macosx", ["Responder"]), ("iOS", "iphonesimulator", ["Field", "Sheet"]),
        ("tvOS", "appletvsimulator", ["Field"])
    ]:
        dest = "platform=macOS,arch=arm64"
        runtime = cmd("sw_vers", "-productVersion")
        if platform != "macOS":
            runtime = "26.5"
            device, = [d for d in devices[f"com.apple.CoreSimulator.SimRuntime.{platform}-26-5"]
                       if d["name"] == f"SwiftAccessibility-OS26-Unit-{platform}"]
            dest = "id=" + device["udid"]
        for mode in MODES:
            w = batch / platform / mode
            src, tests = w / "Sources/Probe", w / "Tests/ProbeTests"
            src.mkdir(parents=True)
            tests.mkdir(parents=True)
            for family in families:
                (src / (family+".swift")).write_text(subject(platform, family, mode))
                (tests / (family+".swift")).write_bytes((HERE / (family+".swift")).read_bytes())
            (w/"Package.swift").write_text('// swift-tools-version: 5.9\nimport PackageDescription\nlet package = Package(name:"Probe", platforms:[.macOS("26.0"),.iOS("26.0"),.tvOS("26.0")], products:[.library(name:"Probe",targets:["Probe"])], targets:[.target(name:"Probe"),.testTarget(name:"ProbeTests", dependencies:["Probe"])])\n')
            args = ["xcodebuild", "test", "-scheme", "Probe", "-destination", dest,
                    "-derivedDataPath", str(w/"dd"), "-resultBundlePath", str(w/"result.xcresult"),
                    "-parallel-testing-enabled", "NO", "-collect-test-diagnostics", "never", "CODE_SIGNING_ALLOWED=NO"]
            row = dict(platform=platform, variant=mode, runtime=runtime, deployment="26.0",
                       sdk=cmd("xcrun","--sdk",sdk,"--show-sdk-version"), xcode=cmd("xcodebuild","-version"),
                       command=args, inputs={str(p.relative_to(w)):digest(p.read_bytes()) for p in w.rglob("*.swift")})
            (w/"intent.json").write_text(json.dumps(row,indent=2))
            with (w/"native.log").open("xb") as log:
                result = subprocess.run(args,cwd=w,stdout=log,stderr=subprocess.STDOUT,timeout=240)
            data = (w/"native.log").read_bytes()
            lines = data.decode(errors="replace").splitlines()
            row.update(exit=result.returncode,logSHA256=digest(data),tests={})
            for f in families:
                name, marker = METHODS[f]
                status = [m[1] for line in lines if (m:=re.search(r"Test Case '.* "+name+r"\]' (passed|failed)",line))]
                errors = [line.split(": error: ",1)[1] for line in lines if ": error: " in line and " "+name+"]" in line]
                row["tests"][name] = dict(status=status, diagnostics=errors)
            (w/"receipt.json").write_text(json.dumps(row,indent=2))
            expected = "failed" if mode=="mutant" else "passed"
            ok = result.returncode==(65 if mode=="mutant" else 0) and all(
                row["tests"][m]["status"]==[expected] and (mode!="mutant" or any(
                    marker in e for e in row["tests"][m]["diagnostics"])) for m,marker in map(METHODS.get,families))
            print(w.relative_to(ROOT), ok, flush=True)
            if not ok:
                raise SystemExit("Unexpected result; first receipt preserved")
    print(batch.name)


if __name__ == "__main__":
    run()

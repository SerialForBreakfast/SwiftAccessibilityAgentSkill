"""Apply preserved submitted proofs to qualified fixture subjects, not to repaired answers."""
import hashlib
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
CAL = HERE.parent
ROOT = CAL.parents[1]
PRIVATE = ROOT / "evals/results"
sys.path.insert(0, str(CAL))
from probes.verify import verified

ORIGINAL = PRIVATE / "persistent-replay/tmp6xijam9k"
BINDINGS = {
    "P-4099aaf89ec377cf": ("tvOS", "Field", "testLiveEdit"),
    "P-db6ab4c551e67aca": ("iOS", "Field", "testLiveEdit"),
    "P-be25d510c5ffe50f": ("macOS", "Responder", "testAttachedRefusal"),
    "P-90629dd9d60ff906": ("iOS", "Sheet", "testSurvivingOrigin"),
}


def sha(data):
    return hashlib.sha256(data).hexdigest()


def save(path, value):
    with path.open("x") as f:
        json.dump(value, f, indent=2)
        f.write("\n")


def run():
    controls = {(p["platform"],p["method"]):p for p in verified()}
    index = json.loads((CAL/"probes/evidence.json").read_bytes())
    out = Path(tempfile.mkdtemp(prefix="submitted-",dir=PRIVATE/"native-calibration"))
    print(out.name, flush=True)
    rows = []
    for case, (platform, family, method) in BINDINGS.items():
        for arm in ("unaided","skill"):
            cell = ORIGINAL/(case+"."+arm)
            meta = json.loads((cell/"input.json").read_bytes())
            proof = sorted(cell.glob("Proof*.swift"))
            for p in proof:
                assert sha(p.read_bytes()) == meta["inputs"][p.name]
            row = dict(id=case, arm=arm, platform=platform, probe=method,
                       answerSHA256=meta["inputs"]["answer.txt"],
                       proofHashes=[sha(p.read_bytes()) for p in proof],
                       returnedProofFences=meta["returnedProofFences"], attempts={})
            rows.append(row)
            if not proof:
                assert not meta["returnedProofFences"]
                row["outcome"]="no-executable-proof"
                continue
            if family=="Sheet":
                api = "FocusTargetCoordinator" if arm=="unaided" else "PresentationCoordinator"
                assert api in proof[0].read_text()
                row.update(outcome="interface-gap", requiredType=api, fixtureType="Sheet")
                continue
            control = controls[platform,method]
            env = control["anchor"]
            assert subprocess.check_output(["xcodebuild","-version"],text=True).strip()==env["xcode"]
            sdk = {"iOS":"iphonesimulator","tvOS":"appletvsimulator","macOS":"macosx"}[platform]
            assert subprocess.check_output(["xcrun","--sdk",sdk,"--show-sdk-version"],text=True).strip()==env["sdk"]
            if platform=="macOS":
                assert subprocess.check_output(["sw_vers","-productVersion"],text=True).strip()==env["runtime"]
            else:
                devices=json.loads(subprocess.check_output(["xcrun","simctl","list","devices","booted","-j"]))["devices"]
                assert env["destination"][3:] in [d["udid"] for d in devices["com.apple.CoreSimulator.SimRuntime."+platform+"-"+env["runtime"].replace(".","-")]]
            row["anchor"]=env
            for mode in ("positive","alternative","mutant"):
                w = out/(case+"."+arm)/mode
                src, tests = w/"Sources"/meta["module"], w/"Tests/Checks"
                src.mkdir(parents=True); tests.mkdir(parents=True)
                data=(PRIVATE/"native-calibration"/index["batch"]/platform/mode/"Sources/Probe"/(family+".swift")).read_bytes()
                assert sha(data)==control["runs"][mode]["subjectSHA256"]
                (src/"Subject.swift").write_bytes(data)
                for p in proof:
                    (tests/p.name).write_bytes(p.read_bytes())
                module=meta["module"]
                (w/"Package.swift").write_text(f'// swift-tools-version: 5.9\nimport PackageDescription\nlet package=Package(name:"Replay",platforms:[.macOS("26.0"),.iOS("26.0"),.tvOS("26.0")],products:[.library(name:"Replay",targets:["{module}"])],targets:[.target(name:"{module}"),.testTarget(name:"Checks",dependencies:["{module}"])])\n')
                args=["xcodebuild","test","-scheme","Replay","-destination",env["destination"],"-derivedDataPath",str(w/"dd"),"-resultBundlePath",str(w/"result.xcresult"),"-parallel-testing-enabled","NO","-collect-test-diagnostics","never","CODE_SIGNING_ALLOWED=NO"]
                save(w/"intent.json",dict(command=args, environment=env,inputs={str(p.relative_to(w)):sha(p.read_bytes()) for p in w.rglob("*.swift")}))
                with (w/"native.log").open("xb") as log:
                    rc=subprocess.run(args,cwd=w,stdout=log,stderr=subprocess.STDOUT,timeout=240).returncode
                log=(w/"native.log").read_bytes()
                methods=re.findall(r"Test Case '([^'\n]+)' (passed|failed)",log.decode(errors="replace"))
                expected=set(re.findall(r'func (test\w+)\s*\(', '\n'.join(p.read_text() for p in proof)))
                ran=[k.split()[-1].rstrip("]") for k,_ in methods]
                status="pass" if rc==0 and set(ran)==expected and len(ran)==len(expected)>0 and all(s=="passed" for _,s in methods) else "needs-review"
                receipt=dict(exit=rc,methods=methods,status=status,logSHA256=sha(log),subjectSHA256=sha(data))
                save(w/"receipt.json",receipt)
                row["attempts"][mode]=receipt
                print(case,arm,mode,status,flush=True)
                if not methods and not any(m in log for m in (b"/Tests/Checks/",b"/Sources/")):
                    raise RuntimeError("infrastructure failure; receipts preserved")
            row["outcome"]="missed-qualified-mutant" if all(r["status"]=="pass" for r in row["attempts"].values()) else "needs-review"
    save(out/"summary.json",dict(batch=out.name, rows=rows))


if __name__=="__main__":
    run()

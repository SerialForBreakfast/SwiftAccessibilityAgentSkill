"""Run maintained fixtures; arbitrary submissions require a disposable offline macOS VM."""
import argparse
from collections import Counter
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import platform
import subprocess
import sys
import tempfile
sys.dont_write_bytecode = True
from tasks import TASKS

ROOT = Path(__file__).resolve().parents[3]
SDK = {"ios": ("iphonesimulator","ios26.0-simulator"), "tvos": ("appletvsimulator","tvos26.0-simulator"), "macos": ("macosx","macosx26.0")}
digest = lambda b: hashlib.sha256(b).hexdigest()


def read(*args):
    return subprocess.check_output(args, text=True, timeout=40).strip()


def devices():
    data = json.loads(read("xcrun","simctl","list","devices","booted","-j"))["devices"]
    result = {}
    for p, runtime in [("ios","iOS"),("tvos","tvOS")]:
        options = data.get("com.apple.CoreSimulator.SimRuntime."+runtime+"-26-5", [])
        device = next((x for x in options if x["name"] == "SwiftAccessibility-OS26-Unit-"+runtime), None)
        if not device and options:
            device = options[0]
        if device:
            result[p] = device["udid"]
    return result


def oracle(task):
    receiver = """
@MainActor final class Receiver: NSObject {
    var events: [String] = []
    @objc func open(_ sender: Any?) { events.append("open") }
    @objc func save(_ sender: Any?) { events.append("save") }
}
""" if task.id == "ordinary-buttons" else ""
    return f"import {task.framework}\nimport Darwin\n{receiver}\n@main struct Oracle {{\n@MainActor static func check() -> Bool {{\n{task.test}\n}}\nstatic func main() {{ if check() {{ print(\"PASS:{task.id}\") }} else {{ print(\"FAIL:{task.id}\"); exit(42) }} }}\n}}\n"


def run(task, kind, source, runroot, cache, env, anchors, sdkpaths):
    folder = runroot / task.id / kind
    folder.mkdir(parents=True)
    submission, hidden, exe = (folder / f for f in ("Submission.swift","Oracle.swift","unit"))
    submission.write_bytes(source)
    hidden.write_text(oracle(task))
    row = dict(task=task.id, variant=kind, platform=task.platform, framework=task.framework,
               submissionSHA256=digest(source), oracleSHA256=digest(hidden.read_bytes()), artifacts=str(folder.relative_to(ROOT)))
    sdk, suffix = SDK[task.platform]
    cmd = ["xcrun","--sdk",sdk,"swiftc","-parse-as-library","-module-cache-path",str(cache),"-sdk",sdkpaths[sdk],
           "-target",platform.machine()+"-apple-"+suffix,str(submission),str(hidden),"-o",str(exe)]
    try:
        build = subprocess.run(cmd, capture_output=True, env={**env, "SDKROOT": sdkpaths[sdk]}, timeout=150)
        (folder/"compile.log").write_bytes(build.stdout+build.stderr)
        row["compiled"] = build.returncode == 0
        if not row["compiled"]:
            # Do not classify missing SDK, broken compiler or oracle errors as a subject defect.
            diagnostics = build.stderr.decode(errors="replace")
            row["status"] = "compile-failure" if str(submission)+":" in diagnostics and str(hidden)+":" not in diagnostics else "infrastructure-error"
        else:
            cmd = [str(exe)] if task.platform == "macos" else ["xcrun","simctl","spawn",anchors[task.platform],str(exe)]
            observed = subprocess.run(cmd, capture_output=True, env=env, timeout=40)
            (folder/"unit.log").write_bytes(observed.stdout+observed.stderr)
            lines = observed.stdout.decode(errors="replace").splitlines()
            row["status"] = ("pass" if observed.returncode == 0 and lines == ["PASS:"+task.id] else
                             "contract-failure" if observed.returncode == 42 and lines == ["FAIL:"+task.id] else "infrastructure-error")
    except (subprocess.TimeoutExpired, OSError) as error:
        row.update(status="infrastructure-error", reason=str(error))
    (folder/"outcome.json").write_text(json.dumps(row,indent=2)+"\n")
    return row


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--export", metavar="TASK")
    parser.add_argument("--task", choices=[t.id for t in TASKS])
    parser.add_argument("--submission", type=Path)
    args = parser.parse_args()
    if args.export:
        task = next(t for t in TASKS if t.id == args.export)
        # One control is already correct; don't force every subject to invent a fix.
        starter = task.reference if task.id == "switch-preservation" else '    fatalError("Implement this contract")'
        print(task.question+"\n\nReturn only Submission.swift, preserving this interface. Keep correct code as-is.\n\n"+task.solution(starter))
        return
    if args.submission:
        # Fixture qualification on a developer machine never executes a supplied file.
        if not args.task or os.getenv("RC1_ISOLATED_WORKER") != "1" or read("sysctl","-n","kern.hv_vmm_present") != "1":
            parser.error("external submissions require --task and the isolated disposable VM worker (see README)")
        if args.submission.stat().st_size > 64000:
            parser.error("submission exceeds 64 KB")
    base = ROOT/"evals/results/rc1-grader"
    base.mkdir(parents=True,exist_ok=True)
    runroot = Path(tempfile.mkdtemp(prefix="attempt-",dir=base))
    cache = base/"modules"; cache.mkdir(exist_ok=True)
    tmp = runroot/"tmp"; tmp.mkdir()
    env = {"PATH":"/usr/bin:/bin:/usr/sbin:/sbin", "HOME":os.environ["HOME"], "TMPDIR":str(tmp)}
    rows = []
    report = dict(startUTC=datetime.now(timezone.utc).isoformat(), rows=rows, scope="offline code contracts only")
    path = runroot/"scorecard.json"
    try:
        selected = [t for t in TASKS if not args.task or t.id == args.task]
        anchors = devices() if any(t.platform != "macos" for t in selected) else {}
        sdkpaths = {s:read("xcrun","--sdk",s,"--show-sdk-path") for s,_ in SDK.values()}
        report.update(xcode=read("xcodebuild","-version"),swift=read("xcrun","swiftc","--version"),host=platform.mac_ver()[0],
                      deployment="26.0", simulatorRuntime="26.5", devices=anchors,
                      sdkVersions={s:read("xcrun","--sdk",s,"--show-sdk-version") for s in sdkpaths})
        for t in selected:
            if t.platform != "macos" and t.platform not in anchors:
                raise RuntimeError("Boot an existing "+t.platform+" 26.5 unit simulator first")
            variants = [("submission",args.submission.read_bytes())] if args.submission else [
                (k,t.solution(getattr(t,k)).encode()) for k in ("reference","alternative","mutant")]
            for k, source in variants:
                r = run(t,k,source,runroot,cache,env,anchors,sdkpaths)
                rows.append(r)
                print(f"{t.id}: {k}: {r['status']}",flush=True)
                if r["status"] == "infrastructure-error":
                    raise RuntimeError("Native execution stopped; inspect "+r["artifacts"])
    except (RuntimeError, OSError, subprocess.SubprocessError) as error:
        report["infrastructureError"] = str(error)
    finally:
        report["totals"] = dict(Counter(r["status"] for r in rows))
        report["accepted"] = not report.get("infrastructureError") and bool(rows) and all(
            r["status"] == ("contract-failure" if r["variant"]=="mutant" else "pass") for r in rows)
        path.write_text(json.dumps(report,indent=2)+"\n")
        print(path,report["totals"],report.get("infrastructureError",""),flush=True)
    return 0 if report["accepted"] else 1


if __name__ == "__main__":
    sys.exit(main())

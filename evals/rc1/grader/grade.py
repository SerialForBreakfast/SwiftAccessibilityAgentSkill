"""Run maintained fixtures, or controller-reviewed submissions through the reviewed local lane."""
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
# Reviewed local lane. The owner approved it on 2026-11-07 and declined a VM or a separate user.
# A submission runs on this host only if (1) the controller read it and recorded its hash
# with decision "run" in the RC1_REVIEWED_LOCAL record, and (2) it passes this screen.
# The screen supports the human read. It is not a sandbox.
FORBIDDEN = ("Process", "NSTask", "FileManager", "FileHandle", "URLSession", "URL(", "Socket", "dlopen", "dlsym",
             "@_silgen_name", "@_cdecl", "posix_spawn", "system(", "popen", "fork(", "execv", "getenv", "setenv",
             "exit(", "abort(", "print(", "fwrite", "fputs", "write(", "Unsafe", "unsafeBitCast", "#if", "@main",
             "CommandLine", "Darwin", "Glibc", "Foundation")


def screen(task, source):
    text = source.decode("utf-8")
    imports = {l.split()[1] for l in text.splitlines() if l.strip().startswith("import ") and len(l.split()) > 1}
    return [t for t in FORBIDDEN if t in text] + [f"import {i}" for i in sorted(imports - {task.framework})]


def reviewed(task, source):
    path = os.getenv("RC1_REVIEWED_LOCAL")
    if not path:
        return "set RC1_REVIEWED_LOCAL to the controller review record"
    entry = json.loads(Path(path).read_bytes()).get(digest(source))
    if not entry or entry.get("task") != task.id or entry.get("decision") != "run":
        return "submission hash is not approved for this task in the review record"
    problems = screen(task, source)
    return "refused by screen: " + ", ".join(problems) if problems else None


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
    parser.add_argument("--result", type=Path, help="write the scorecard JSON here once (structured result)")
    args = parser.parse_args()
    if args.export:
        task = next(t for t in TASKS if t.id == args.export)
        # One control is already correct; don't force every subject to invent a fix.
        starter = task.reference if task.id == "switch-preservation" else '    fatalError("Implement this contract")'
        print(task.question+"\n\nReturn only Submission.swift, preserving this interface. Keep correct code as-is.\n\n"+task.solution(starter))
        return
    submitted = None
    if args.submission:
        if not args.task:
            parser.error("a submission requires --task")
        # Read once. The same immutable bytes are approved, stored, compiled and hashed.
        submitted = args.submission.read_bytes()
        if len(submitted) > 64000:
            parser.error("submission exceeds 64 KB")
        refusal = reviewed(next(t for t in TASKS if t.id == args.task), submitted)
        if refusal:
            parser.error(refusal)
    base = Path(os.getenv("RC1_RESULTS_BASE") or ROOT/"evals/results/rc1-grader")
    if not inside_results(base) or (args.result and not inside_results(args.result)):
        parser.error("results must stay under evals/results/")
    if args.result and args.result.exists():
        parser.error("result already recorded; results are written once: " + str(args.result))
    selected = [t for t in TASKS if not args.task or t.id == args.task]
    variants = (lambda t: [("submission", submitted)]) if submitted is not None else (
        lambda t: [(k, t.solution(getattr(t, k)).encode()) for k in ("reference", "alternative", "mutant")])
    expect = lambda r: "contract-failure" if r["variant"] == "mutant" else "pass"
    report = execute(selected, variants, base, expect)
    if args.result:
        write_once(args.result, report)
    return 0 if report["accepted"] else 1


def inside_results(path):
    return Path(path).resolve().is_relative_to((ROOT/"evals/results").resolve())


def write_once(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "x") as f:
        f.write(json.dumps(data, indent=2)+"\n")


def grader_fingerprint():
    here = Path(__file__).resolve().parent
    return {name: digest((here/name).read_bytes()) for name in ("grade.py", "tasks.py")}


def execute(selected, variants, base, expect):
    """Grade each task's variants once; stop at the first infrastructure error. Returns the scorecard."""
    base.mkdir(parents=True,exist_ok=True)
    runroot = Path(tempfile.mkdtemp(prefix="attempt-",dir=base))
    cache = base/"modules"; cache.mkdir(exist_ok=True)
    tmp = runroot/"tmp"; tmp.mkdir()
    env = {"PATH":"/usr/bin:/bin:/usr/sbin:/sbin", "HOME":os.environ["HOME"], "TMPDIR":str(tmp)}
    rows = []
    report = dict(startUTC=datetime.now(timezone.utc).isoformat(), rows=rows, scope="offline code contracts only",
                  grader=grader_fingerprint(), attempt=str(runroot.relative_to(ROOT)))
    path = runroot/"scorecard.json"
    try:
        anchors = devices() if any(t.platform != "macos" for t in selected) else {}
        sdkpaths = {s:read("xcrun","--sdk",s,"--show-sdk-path") for s,_ in SDK.values()}
        report.update(xcode=read("xcodebuild","-version"),swift=read("xcrun","swiftc","--version"),host=platform.mac_ver()[0],
                      deployment="26.0", simulatorRuntime="26.5", devices=anchors,
                      sdkVersions={s:read("xcrun","--sdk",s,"--show-sdk-version") for s in sdkpaths})
        for t in selected:
            if t.platform != "macos" and t.platform not in anchors:
                raise RuntimeError("Boot an existing "+t.platform+" 26.5 unit simulator first")
            for k, source in variants(t):
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
            r["status"] == expect(r) for r in rows)
        write_once(path, report)
        print(path,report["totals"],report.get("infrastructureError",""),flush=True)
    return report


if __name__ == "__main__":
    sys.exit(main())

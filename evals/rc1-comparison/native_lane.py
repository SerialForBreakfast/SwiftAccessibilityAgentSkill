"""Grade the reviewed v2 answers natively through the reviewed local lane (no model calls).

Inputs: evals/results/rc1-return-20261107/native-pending/<cell>-<task>.swift plus review.json
(the controller's read record). Each cell is run once through grade.py. Unit simulators that
this script boots are shut down afterwards. Writes native.json next to the inputs.
"""
import json
from pathlib import Path
import re
import subprocess
import sys

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "evals/results/rc1-return-20261107"
PENDING = BASE / "native-pending"
GRADE = ROOT / "evals/rc1/grader/grade.py"


def boot():
    started = []
    devices = json.loads(subprocess.check_output(["xcrun", "simctl", "list", "devices", "available", "-j"], timeout=30))["devices"]
    for platform in ("iOS", "tvOS"):
        candidates = devices.get("com.apple.CoreSimulator.SimRuntime." + platform + "-26-5", [])
        if any(d["state"] == "Booted" for d in candidates):
            continue
        unit = next(d for d in candidates if d["name"] == "SwiftAccessibility-OS26-Unit-" + platform)
        subprocess.run(["xcrun", "simctl", "boot", unit["udid"]], check=True, timeout=120)
        started.append(unit["udid"])
        subprocess.run(["xcrun", "simctl", "bootstatus", unit["udid"]], check=True, timeout=180)
    return started


def main():
    out = BASE / "native"
    out.mkdir(exist_ok=True)
    env = {"PATH": "/usr/bin:/bin:/usr/sbin:/sbin", "HOME": str(Path.home()),
           "RC1_REVIEWED_LOCAL": str(PENDING / "review.json"), "RC1_RESULTS_BASE": str(out)}
    rows, started = [], boot()
    try:
        for f in sorted(PENDING.glob("C*.swift")):
            cell, task = f.stem.split("-", 1)
            p = subprocess.run([sys.executable, "-B", str(GRADE), "--task", task, "--submission", str(f)],
                               capture_output=True, text=True, env=env, timeout=600)
            card = re.search(r"^(/.*?/scorecard\.json) ", p.stdout, re.M)  # repo path contains spaces
            report = json.loads(Path(card.group(1)).read_text()) if card else {}
            row = (report.get("rows") or [{}])[0]
            rows.append(dict(cell=cell, task=task, status=row.get("status", "not-run"),
                             compiled=row.get("compiled"), submissionSHA256=row.get("submissionSHA256"),
                             scorecard=str(Path(card.group(1)).relative_to(ROOT)) if card else None,
                             infrastructureError=report.get("infrastructureError"),
                             refusal=p.stderr.strip()[-300:] if p.returncode and not card else None))
            print(cell, task, rows[-1]["status"], flush=True)
    finally:
        for udid in reversed(started):
            subprocess.run(["xcrun", "simctl", "shutdown", udid], timeout=120)
        (BASE / "native.json").write_text(json.dumps(rows, indent=2) + "\n")


if __name__ == "__main__":
    main()

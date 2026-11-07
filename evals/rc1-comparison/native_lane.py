"""Reviewed local native lane for the rc.1 v2 answers. Offline: no model calls.

  adopt          one time: link each cell to the first native scorecard already recorded (write-once)
  run [--base B] grade only cells with no record; warm up with trusted fixtures first; stop on the
                 first infrastructure error; each cell record is written once
  --base         a fresh directory under evals/results/rc1-return-20261107/ (used by the rehearsal)

Answers come straight from the private v2 bundle through the strict extractor; the bytes must be
approved in native-pending/review.json. Cell records live in <base>/cells/<cell>.json.
"""
import argparse
from hashlib import sha256
import json
import os
from pathlib import Path
import subprocess
import sys
from zipfile import ZipFile

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[2]
RUN = ROOT / "evals/results/rc1-return-20261107"
BUNDLE = RUN / "bundles/rc1-release-native-chat-36-v2-return.zip"
REVIEW = RUN / "native-pending/review.json"
GRADE = ROOT / "evals/rc1/grader/grade.py"
sys.path.insert(0, str(ROOT / "evals/protocol"))
from answer_contract import extract

WARMUP = ("checkout-font", "row-traits")  # trusted fixtures: one iOS, one tvOS
digest = lambda b: sha256(b).hexdigest()


def write_once(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "x") as f:
        f.write(json.dumps(data, indent=2) + "\n")


def cells():
    z = ZipFile(BUNDLE)
    for row in json.loads(z.read("index.json")):
        answer = z.read(f"cells/{row['cell']}/answer.txt")
        x = extract(answer.decode("utf-8"))
        yield row, answer, x


def fingerprint(row, x):
    return dict(cell=row["cell"], task=row["task"], arm=row["arm"], lane=row["lane"],
                answerSHA256=None, extraction=x["status"], format=x.get("format"),
                submissionSHA256=digest(x["code"]) if x["code"] else None)


def scorecard_record(card_path):
    card = json.loads(card_path.read_bytes())
    r = card["rows"][0] if card["rows"] else {}
    return dict(status=r.get("status", "not-run"), compiled=r.get("compiled"),
                oracleSHA256=r.get("oracleSHA256"), gradedSHA256=r.get("submissionSHA256"),
                scorecard=str(card_path.relative_to(ROOT)), scorecardSHA256=digest(card_path.read_bytes()),
                infrastructureError=card.get("infrastructureError"), startUTC=card.get("startUTC"))


def adopt():
    """Link the first recorded scorecard to each cell. The legacy map is the second, complete lane run;
    C01 was first graded by the run that crashed while parsing (attempt-bglcchrd)."""
    legacy = {r["cell"]: r for r in json.loads((RUN / "native.json").read_bytes())}
    first = {"C01": RUN / "native/attempt-bglcchrd/scorecard.json"}
    for row, answer, x in cells():
        rec = fingerprint(row, x)
        rec["answerSHA256"] = digest(answer)
        primary = first.get(row["cell"], ROOT / legacy[row["cell"]]["scorecard"])
        rec.update(scorecard_record(primary))
        dupes = [ROOT / legacy[row["cell"]]["scorecard"]] if row["cell"] in first else []
        rec["laterGradings"] = [scorecard_record(p) for p in dupes]
        rec["graderNote"] = "graded by grade.py at 226b3a4 (reviewed local lane, before structured results)"
        assert rec["gradedSHA256"] == rec["submissionSHA256"], row["cell"]
        write_once(RUN / "native/cells" / f"{row['cell']}.json", rec)
    print("adopted 36 first results")


def grade(args, env, result):
    return subprocess.run([sys.executable, "-B", str(GRADE), *args, "--result", str(result)],
                          capture_output=True, text=True, env=env, timeout=900)


def warm(base, env):
    for attempt in range(1, 4):
        ok = True
        for task in WARMUP:
            out = base / "warmup" / f"{task}-{attempt}.json"
            grade(["--task", task], env, out)
            card = json.loads(out.read_bytes()) if out.exists() else {}
            ok &= bool(card.get("accepted"))
        if ok:
            return attempt
    raise SystemExit("warm-up fixtures did not pass after 3 tries; no answer graded")


def boot():
    started = []
    devices = json.loads(subprocess.check_output(["xcrun", "simctl", "list", "devices", "available", "-j"], timeout=30))["devices"]
    for platform in ("iOS", "tvOS"):
        options = devices.get("com.apple.CoreSimulator.SimRuntime." + platform + "-26-5", [])
        if any(d["state"] == "Booted" for d in options):
            continue
        unit = next(d for d in options if d["name"] == "SwiftAccessibility-OS26-Unit-" + platform)
        subprocess.run(["xcrun", "simctl", "boot", unit["udid"]], check=True, timeout=120)
        subprocess.run(["xcrun", "simctl", "bootstatus", unit["udid"]], check=True, timeout=180,
                       stdout=subprocess.DEVNULL)
        started.append(unit["udid"])
    return started


def run(base):
    assert base.resolve().is_relative_to(RUN.resolve())
    review = json.loads(REVIEW.read_bytes())
    todo = []
    for row, answer, x in cells():
        rec_path = base / "cells" / f"{row['cell']}.json"
        if rec_path.exists():
            old = json.loads(rec_path.read_bytes())
            if (old["task"], old["submissionSHA256"]) != (row["task"], fingerprint(row, x)["submissionSHA256"]):
                raise SystemExit(f"{row['cell']}: recorded fingerprint differs; refusing to regrade")
            continue
        todo.append((row, answer, x))
    if not todo:
        print("every cell already has a recorded result")
        return
    env = {"PATH": "/usr/bin:/bin:/usr/sbin:/sbin", "HOME": str(Path.home()),
           "RC1_REVIEWED_LOCAL": str(REVIEW), "RC1_RESULTS_BASE": str(base / "attempts")}
    started = boot()
    try:
        tries = warm(base, env)
        print(f"warm-up passed on try {tries}", flush=True)
        for row, answer, x in todo:
            rec = fingerprint(row, x)
            rec["answerSHA256"] = digest(answer)
            if x["status"] != "accepted":
                rec.update(status="not-gradable", reason=x["status"])
                write_once(base / "cells" / f"{row['cell']}.json", rec)
                continue
            if review.get(rec["submissionSHA256"], {}).get("decision") != "run":
                raise SystemExit(f"{row['cell']}: not approved in review record; stopping")
            submission = base / "submissions" / f"{row['cell']}.swift"
            if not submission.exists():
                submission.parent.mkdir(parents=True, exist_ok=True)
                submission.write_bytes(x["code"])
            result = base / "scorecards" / f"{row['cell']}.json"
            p = grade(["--task", row["task"], "--submission", str(submission)], env, result)
            if not result.exists():
                raise SystemExit(f"{row['cell']}: grader refused or crashed; stopping\n{p.stderr[-400:]}")
            rec.update(scorecard_record(result))
            rec["laterGradings"] = []
            if rec["status"] == "infrastructure-error":
                print(f"{row['cell']}: infrastructure error; stopping, cell left ungraded", flush=True)
                break  # no record: the cell stays ungraded and can be resumed
            write_once(base / "cells" / f"{row['cell']}.json", rec)
            print(row["cell"], row["task"], rec["status"], flush=True)
    finally:
        for udid in reversed(started):
            subprocess.run(["xcrun", "simctl", "shutdown", udid], timeout=120)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("mode", choices=["adopt", "run"])
    parser.add_argument("--base", type=Path, default=RUN / "native")
    args = parser.parse_args()
    adopt() if args.mode == "adopt" else run(args.base)

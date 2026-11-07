"""Build or verify the controller packet offline. Does not invoke a model."""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
RC = ROOT / "evals/rc1"
sys.path.insert(0, str(RC / "grader"))
from tasks import TASKS

BASE = "0.2.2"
CAND = "0.3.0-rc.1"
REPEAT = ["checkout-font", "ordinary-buttons", "stale-media-reply",
          "toggle-binding", "checkout-layout", "restoration-eligibility"]
EXPLICIT = ["toggle-binding", "ordinary-buttons", "restoration-eligibility"]
PREFIX = "Use the installed swift-accessibility-agent skill for this task.\n\n"
REV = "11b56fc0404251851176fd181a1450d46262e5dd"


def sha(data):
    return hashlib.sha256(data).hexdigest()


def build():
    subject = {}
    for t in TASKS:
        subject[t.id] = subprocess.check_output(
            [sys.executable, "-B", str(RC / "grader/grade.py"), "--export", t.id]
        ).decode("utf-8")
    by_id = {t.id: t for t in TASKS}
    assert len(by_id) == 12
    assert len({(by_id[i].platform, by_id[i].framework) for i in REPEAT}) == 6
    assert len({by_id[i].platform for i in EXPLICIT}) == 3
    jobs = []

    def add(task, arm, kind):
        prompt = (PREFIX if kind == "explicit" else "") + subject[task]
        jobs.append(dict(cell=f"C{len(jobs)+1:02}", task=task, arm=arm, lane=kind,
                         promptSHA256=sha(prompt.encode())))
    # Interleave platforms. Reverse arm order on alternating pairs.
    for j, t in enumerate(TASKS[p*4+i] for i in range(4) for p in range(3)):
        for arm in ((BASE, CAND) if j % 2 == 0 else (CAND, BASE)):
            add(t.id, arm, "automatic")
    for n, task in enumerate(REPEAT):
        add(task, BASE, "repeat-automatic")
        if n % 2 == 1:
            for arm in ((CAND, BASE) if n == 3 else (BASE, CAND)):
                add(EXPLICIT[n//2], arm, "explicit")
    assert len(jobs) == 36
    baseline = subprocess.check_output(["git", "ls-tree", "-r", "--name-only", REV,
                                        "--", "SKILL.md", "VERSION", "agents", "references"],
                                       cwd=ROOT).decode().splitlines()
    pins = {p: sha((ROOT / p).read_bytes()) for p in baseline}
    assert pins["SKILL.md"] == "2f4ce5ea5a6c8fa7c7cdd08eea620c606eedcc7ae389ac19a493d73078f7c3e3"
    controller = [RC / "RUBRIC.md", RC / "scorecard.json", *sorted((RC / "grader").glob("*.py")),
                  RC / "swift-accessibility-agent-0.3.0-rc.1.zip", HERE / "HANDOFF.md",
                  ROOT / "evals/BIGDOG-SINGLE-EXCHANGE.md", Path(__file__).resolve()]
    return dict(job="rc1-release-native-36-v1", sourceRevision=REV,
                model="claude-haiku-5-5", effort="low", maxFirstSessions=36,
                retries=0, incrementalSpend=0, releaseRuntime=pins,
                pins={str(p.relative_to(ROOT)): sha(p.read_bytes()) for p in controller},
                subjectExports=subject, explicitPrefix=PREFIX, cells=jobs)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    out = HERE / "packet.json"
    data = (json.dumps(build(), indent=2, ensure_ascii=False) + "\n").encode()
    if args.verify:
        if out.read_bytes() != data:
            sys.exit("Packet differs; do not execute")
    else:
        if out.exists() and out.read_bytes() != data:
            sys.exit("Existing seal differs; create a new revision instead")
        out.write_bytes(data)
    print("36 planned first sessions; packet SHA256:", sha(data))

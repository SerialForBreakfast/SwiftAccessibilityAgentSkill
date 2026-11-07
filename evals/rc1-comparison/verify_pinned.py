"""Verify the sealed rc.1 packet at the revision that sealed it, not at HEAD.

The packet pins grade.py and other controller files, so `prepare.py --verify` at HEAD correctly
refuses once the grader changes. Do not reseal. This script exports the sealing revision with
`git archive` into ignored evals/results/, runs that revision's own verifier there, checks HEAD's
packet.json is byte-identical, and reports the post-return grader separately.
"""
from hashlib import sha256
import io
import json
import os
from pathlib import Path
import subprocess
import sys
import tarfile

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[2]
SEALED_AT = "ba507210d5b09cace38ae8516d4954eb2f687b01"  # commit that added packet.json
PACKET = "evals/rc1-comparison/packet.json"
OUT = ROOT / "evals/results/rc1-return-20261107/pinned-ba50721"
git = lambda *a: subprocess.check_output(["git", *a], cwd=ROOT)


def main():
    if not OUT.exists():
        tar = git("archive", "--format=tar", SEALED_AT)
        OUT.mkdir(parents=True)
        with tarfile.open(fileobj=io.BytesIO(tar)) as t:
            t.extractall(OUT, filter="data")
    head = (ROOT / PACKET).read_bytes()
    assert (OUT / PACKET).read_bytes() == head, "HEAD packet.json differs from the sealed bytes"
    # The sealed preparer calls `git ls-tree` with paths relative to its own root; point git at the export.
    env = {**os.environ, "GIT_DIR": str(ROOT / ".git"), "GIT_WORK_TREE": str(OUT)}
    verdict = subprocess.run([sys.executable, "-B", str(OUT / "evals/rc1-comparison/prepare.py"), "--verify"],
                             capture_output=True, text=True, cwd=OUT, env=env)
    assert verdict.returncode == 0, verdict.stdout + verdict.stderr
    pins = json.loads(head)["pins"]
    sealed_grader = pins["evals/rc1/grader/grade.py"]
    current = sha256((ROOT / "evals/rc1/grader/grade.py").read_bytes()).hexdigest()
    rev = git("log", "-1", "--format=%H", "--", "evals/rc1/grader/grade.py").decode().strip()
    print(verdict.stdout.strip())
    print(json.dumps(dict(packetSHA256=sha256(head).hexdigest(), sealedAt=SEALED_AT,
                          sealedGraderSHA256=sealed_grader, postReturnGraderSHA256=current,
                          postReturnGraderLastCommit=rev, graderChanged=current != sealed_grader), indent=2))


if __name__ == "__main__":
    main()

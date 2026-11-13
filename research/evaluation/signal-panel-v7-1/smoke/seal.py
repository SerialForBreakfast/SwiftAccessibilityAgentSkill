"""Deterministic held packet for signal-v7-1-smoke1: signal-v7.1 only, one trial of all 56 questions.

The worker returns answers and traces only. Grading is local: the mutation grader first, then source review.
Questions are byte-identical to signal-v6 run 1 (seal 1b865cef…), so trial-1 answers pair with v6 trial 1.

  python3 -B research/evaluation/signal-panel-v7-1/smoke/seal.py [--check]
"""
from pathlib import Path
import hashlib, io, json, sys
from zipfile import ZipFile, ZipInfo, ZIP_DEFLATED

D = Path(__file__).resolve().parent
V = D.parent
ROOT = D.parents[3]
H = lambda b: hashlib.sha256(b).hexdigest()
V6_HELD = "1b865cefd58a01253e8f89928f7c527bf2b7bb97e11a41c5c6087b38c73be928"
ARM = "signal-v7.1"


def dump(obj):
    return (json.dumps(obj, indent=2) + "\n").encode()


def build():
    v6 = (V.parent / "signal-panel-v6/readiness/held.zip").read_bytes()
    assert H(v6) == V6_HELD, "v6 held packet changed"
    with ZipFile(io.BytesIO(v6)) as z:
        files = {n: z.read(n) for n in z.namelist() if n.startswith("subjects/")}
        v6_schedule = json.loads(z.read("schedule.json"))
    files["arms/signal-v7-1.zip"] = (V / "candidate.zip").read_bytes()
    for n in ["HANDOFF.md", "RETURN.md", "check_return.py"]:
        files[n if n == "HANDOFF.md" else "controller/" + n] = (D / n).read_bytes()
    files["controller/single-exchange.md"] = (ROOT / "evals/BIGDOG-SINGLE-EXCHANGE.md").read_text().split(
        "**Current Flash excerpt request:**")[0].encode()
    skill = H(files["arms/signal-v7-1.zip"])
    rows = sorted({(r["id"], r["subject"], r["questionSHA256"]) for r in v6_schedule if r["trial"] == 1})
    schedule = []
    for i, subject, qsha in rows:
        assert H(files[subject]) == qsha
        schedule.append(dict(id=i, arm=ARM, trial=1, subject=subject, questionSHA256=qsha, skillSHA256=skill))
    assert len(schedule) == 56
    files["schedule.json"] = dump(schedule)
    files["SHA256.json"] = dump({n: H(b) for n, b in sorted(files.items())})
    out = io.BytesIO()
    with ZipFile(out, "w") as z:
        for n, b in sorted(files.items()):
            z.writestr(ZipInfo(n, (2026, 1, 1, 0, 0, 0)), b, compress_type=ZIP_DEFLATED)
    return out.getvalue()


if __name__ == "__main__":
    b = build()
    p = D / "held.zip"
    if "--check" in sys.argv:
        assert p.read_bytes() == b, "held.zip differs from a rebuild"
    else:
        p.write_bytes(b)
    print("held.zip", H(b))

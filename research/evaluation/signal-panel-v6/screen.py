"""Fail if v6 card text newly shares an 8-word run with a panel question, rubric, criterion,
calibration note or preserved v4 answer. Text inherited unchanged from v5 is not counted.

  python3 -B research/evaluation/signal-panel-v6/screen.py
"""
import glob, json, re, sys, zipfile
from pathlib import Path

sys.dont_write_bytecode = True
D = Path(__file__).resolve().parent
ROOT = D.parents[2]
N = 8
words = lambda t: re.findall(r"[a-z0-9_.]+", t.lower())
grams = lambda t: {" ".join(w[i:i + N]) for w in [words(t)] for i in range(len(w) - N + 1)}


def main():
    held = zipfile.ZipFile(ROOT / "research/evaluation/signal-panel-v4/readiness/held.zip")
    src = {}
    for n in held.namelist():
        if n.startswith("subjects/") or (n.startswith("controller/repository/") and n.endswith(".md")):
            src[n] = held.read(n).decode()
    for c in json.loads(held.read("controller/criteria.json")):
        src["criterion " + c["id"]] = " ".join(str(c[k]) for k in ("originalCriterion", "contrast", "insufficientAlone"))
    src["calibration"] = (ROOT / "evals/qualification-56/source-calibration.tsv").read_text()
    ret_path = ROOT / "evals/results/signal-v4-review/signal-v4-return.zip"
    if ret_path.exists():
        ret = zipfile.ZipFile(ret_path)
        for c in json.loads(ret.read("return.json"))["cells"]:
            src["answer " + c["id"] + " " + c["arm"]] = ret.read(c["answer"]["path"]).decode()
    index = {}
    for k, t in src.items():
        for g in grams(t):
            index.setdefault(g, k)
    with zipfile.ZipFile(D.parent / "signal-panel-v5/candidate.zip") as v5:
        inherited = set().union(*(grams(v5.read(n).decode()) for n in v5.namelist()))
    hits = sorted((Path(p).name, index[g], g) for p in glob.glob(str(D / "cards/*.md"))
                  for g in grams(Path(p).read_text()) if g in index and g not in inherited)
    for h in hits:
        print("FAIL", *h)
    if hits:
        sys.exit(f"{len(hits)} shared runs")
    print(f"PASS: no new {N}-word run shared with {len(src)} controller or answer texts"
          + ("" if ret_path.exists() else " (answers skipped: private return absent)"))


if __name__ == "__main__":
    main()

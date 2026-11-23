"""Fail if v7.2 skill text shares an 8-word run with something it must not copy.

The protected corpus:
- the 56 panel questions and their criteria;
- the controller repository and calibration notes;
- the reference tests and evaluation notes under code-examples;
- the native controls and calibration tests;
- every preserved run-1 answer (when the private return is present).

Text inherited unchanged from v7.1 (already screened) is not counted. The v7 and v7.1 smoke answers and the source-regrade reasons are also protected. Comment-free Swift boilerplate shorter than 8 words cannot match.

  python3 -B research/evaluation/signal-panel-v7-2/screen.py
"""
import json, re, sys, zipfile
from pathlib import Path

sys.dont_write_bytecode = True
D = Path(__file__).resolve().parent
ROOT = D.parents[2]
N = 8
words = lambda t: re.findall(r"[a-z0-9_.]+", t.lower())
grams = lambda t: {" ".join(w[i:i + N]) for w in [words(t)] for i in range(len(w) - N + 1)}


def corpus():
    src = {}
    held = zipfile.ZipFile(ROOT / "research/evaluation/signal-panel-v6/readiness/held.zip")
    for n in held.namelist():
        if n.startswith("subjects/") or (n.startswith("controller/") and n.endswith((".md", ".json", ".swift"))):
            src[n] = held.read(n).decode(errors="replace")
    src["calibration"] = (ROOT / "evals/qualification-56/source-calibration.tsv").read_text()
    for pattern in ["code-examples/**/Tests/*.swift", "code-examples/**/evaluation/*.md", "code-examples/**/NegativeFixtures/*.swift",
                    "evals/native-calibration/**/*.swift", "evals/native-calibration/**/*.md", "evals/qualification-56/*controls*.py"]:
        for p in ROOT.glob(pattern):
            src[str(p.relative_to(ROOT))] = p.read_text(errors="replace")
    ret = ROOT.parent / "SharedStatusFile/joe-big-dog/request-1507-continuation-return.zip"
    answers = 0
    if ret.exists():
        z = zipfile.ZipFile(ret)
        for c in json.loads(z.read("return.json"))["cells"]:
            if c["state"] == "answered":
                src["answer " + c["id"] + " " + c["arm"] + " " + str(c["trial"])] = z.read(c["answer"]["path"]).decode(errors="replace")
                answers += 1
    for run in ("signal-v6-release-1507", "signal-v6-release-1507-continuation", "signal-v7-smoke1", "signal-v7-1-smoke1"):
        for p in sorted((ROOT / "evals/results" / run / "records").glob("*/answer.txt")):
            src[run + " " + p.parent.name] = p.read_text(errors="replace")
            answers += 1
    grades = ROOT / "evals/results/signal-v7-grading/grades.jsonl"
    if grades.exists():
        for line in grades.read_text().splitlines():
            r = json.loads(line)
            src["grade " + r["token"]] = r["reason"]
    return src, answers


def main():
    src, answers = corpus()
    index = {}
    for k, t in src.items():
        for g in grams(t):
            index.setdefault(g, k)
    with zipfile.ZipFile(D.parent / "signal-panel-v7-1/candidate.zip") as prior:
        inherited = set().union(*(grams(prior.read(n).decode()) for n in prior.namelist()))
    hits = sorted({(p.relative_to(D / "skill").as_posix(), index[g], g) for p in (D / "skill").rglob("*.md")
                   for g in grams(p.read_text()) if g in index and g not in inherited})
    for h in hits:
        print("FAIL", *h)
    if hits:
        sys.exit(f"{len(hits)} shared runs")
    print(f"PASS: no new {N}-word run shared with {len(src)} protected texts ({answers} preserved answers)")


if __name__ == "__main__":
    main()

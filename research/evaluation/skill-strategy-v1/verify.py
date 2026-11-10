"""Verify the strategy audit: shards against items.json and schema, no answer leakage, document in sync.

  python3 -B research/evaluation/skill-strategy-v1/verify.py
"""
import json
from pathlib import Path
import re
import sys
import zipfile

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
RETURN = ROOT / "evals/results/signal-v2-review-20261108/signal-panel-v2-return.zip"
GAPS = {"harmful-instruction", "content-gap", "not-opened", "question-defect", "oracle-defect", "verification-gap",
        "rework", "variance", "unmeasured", "sound-control"}
TEXT = ("diagnosis", "questionChange", "oracleChange", "skillChange", "routingChange")
words = lambda t: re.findall(r"[A-Za-z0-9_.]+", t.lower())


def main():
    sys.path.insert(0, str(HERE))
    from render import generated
    items = json.loads((HERE / "items.json").read_bytes())
    errors, recs = [], {}
    for tier in ("tier1", "tier2"):
        want = {i["id"] for i in items[tier]}
        got = json.loads((HERE / "shards" / f"{tier}.json").read_bytes())
        ids = [r["id"] for r in got]
        if len(ids) != len(set(ids)) or set(ids) != want:
            errors.append(f"{tier}: ids differ (missing {sorted(want - set(ids))[:3]}, extra {sorted(set(ids) - want)[:3]})")
        for r in got:
            bad = lambda m: errors.append(f"{r['id']}: {m}")
            if r.get("gapType") not in GAPS: bad(f"gapType {r.get('gapType')}")
            if r.get("v3Covers") not in ("yes", "partial", "no", "n/a"): bad("v3Covers")
            if r.get("priority") not in ("P0", "P1", "P2", "P3"): bad("priority")
            if r.get("confidence") not in ("high", "medium", "low"): bad("confidence")
            for f in TEXT:
                if not isinstance(r.get(f), str) or not r[f].strip(): bad(f"empty {f}")
            if r.get("questionChange", "none").strip().lower() != "none" and not (r.get("proposedWording") or "").strip():
                bad("question change without proposed wording")
            recs[r["id"]] = r
    # No 12-word run copied from any original model answer in the signal-v2 return.
    if RETURN.exists():
        z = zipfile.ZipFile(RETURN)
        grams = set()
        for n in z.namelist():
            if n.startswith("masked/") and n.endswith(".json"):
                aw = words(json.loads(z.read(n)).get("answer") or "")
                grams |= {" ".join(aw[k:k + 12]) for k in range(len(aw) - 11)}
        for i, r in recs.items():
            tw = words(" ".join(str(r.get(f) or "") for f in TEXT + ("proposedWording",)))
            if any(" ".join(tw[k:k + 12]) in grams for k in range(len(tw) - 11)):
                errors.append(f"{i}: 12-word overlap with a model answer")
    doc = (HERE / "SKILL-DEVELOPMENT-STRATEGY.md").read_text()
    for marker, body in generated(items, recs).items():
        seg = re.search(rf"<!-- {marker}:begin -->\n(.*?)<!-- {marker}:end -->", doc, re.S)
        if not seg or seg.group(1) != body:
            errors.append(f"document section {marker} is stale; run render.py")
    for m in re.finditer(r"\]\(([^)#]+?)(?:#[^)]*)?\)", doc):
        target = m.group(1)
        if not target.startswith("http") and not (HERE / target).resolve().exists():
            errors.append(f"broken link {target}")
    for e in errors[:40]:
        print("FAIL", e)
    if errors:
        sys.exit(f"{len(errors)} problems")
    print(f"PASS: {len(recs)} recommendations, answer-overlap {'checked' if RETURN.exists() else 'skipped'}, document in sync")


if __name__ == "__main__":
    main()

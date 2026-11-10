"""Verify the three suggestion shards against items.json, the schema and the private answers.

  python3 -B research/evaluation/prompt-improvements-v1/verify.py
Checks: 384 unique ids, one shard each, matching platform; valid enums; required wording; non-empty
evidence-grounded diagnosis for every fail/inconclusive item; no 12-word overlap with any private
first answer (when packets are present); the document's generated sections match the shards.
"""
from collections import Counter
import json
from pathlib import Path
import re
import sys

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
PACKETS = ROOT / "evals/results/prompt-improvements-v1/items"
PROBLEMS = {"no-headroom", "symptom-as-fact", "ambiguous-policy", "oracle-mismatch", "bundled-criteria", "weak-endpoint",
            "real-model-gap", "rework-only", "evidence-only", "grader-uncertain", "duplicate", "good-as-is"}
DISPOSITIONS = {"keep-control", "rewrite-neutral", "pair-variant", "specify-policy", "split-criteria", "repair-oracle",
                "raise-to-integration", "grade-components", "retire-duplicate", "reserve-transfer"}
NEEDS_WORDING = {"rewrite-neutral", "split-criteria", "specify-policy", "raise-to-integration"}
SKILLS = {f"S{i}" for i in range(1, 9)}
TEXT = ("diagnosis", "promptChange", "oracleChange", "skillWhy", "transfer")
SHARDS = {"iOS": "ios", "macOS": "macos", "tvOS": "tvos"}


def load():
    items = {i["id"]: i for i in json.loads((HERE / "items.json").read_bytes())["items"]}
    recs = {}
    for plat, name in SHARDS.items():
        for r in json.loads((HERE / "shards" / f"{name}.json").read_bytes()):
            assert r["id"] not in recs, f"duplicate {r['id']}"
            assert items[r["id"]]["platform"] == plat, f"{r['id']} in wrong shard {name}"
            recs[r["id"]] = r
    return items, recs


def words(t):
    return re.findall(r"[A-Za-z0-9_.]+", t.lower())


def main():
    items, recs = load()
    errors = []
    missing = set(items) - set(recs)
    if missing:
        errors.append(f"{len(missing)} items without a suggestion, e.g. {sorted(missing)[:3]}")
    for i, r in recs.items():
        bad = lambda m: errors.append(f"{i}: {m}")
        if r.get("problem") not in PROBLEMS: bad(f"problem {r.get('problem')}")
        if r.get("disposition") not in DISPOSITIONS: bad(f"disposition {r.get('disposition')}")
        if r.get("priority") not in ("P0", "P1", "P2", "P3"): bad("priority")
        if r.get("confidence") not in ("high", "medium", "low"): bad("confidence")
        if not isinstance(r.get("skill"), list) or set(r["skill"]) - SKILLS: bad(f"skill {r.get('skill')}")
        for f in TEXT:
            if not isinstance(r.get(f), str) or not r[f].strip(): bad(f"empty {f}")
        if r.get("disposition") in NEEDS_WORDING and not (r.get("proposedWording") or "").strip(): bad("needs proposedWording")
        if r.get("disposition") == "split-criteria" and "‖" not in (r.get("proposedWording") or ""): bad("split needs two questions")
        if items[i]["verdict"] != "pass" and len(r.get("diagnosis", "")) < 40: bad("thin diagnosis for a non-pass")
    # No answer leakage: no run of 12 consecutive answer words in any free-text field.
    leaks = 0
    if PACKETS.exists():
        for i, r in recs.items():
            ans = json.loads((PACKETS / f"{i}.json").read_bytes()).get("answer") or ""
            aw = words(ans)
            grams = {" ".join(aw[k:k + 12]) for k in range(len(aw) - 11)}
            text = " ".join(str(r.get(f) or "") for f in TEXT + ("proposedWording",))
            tw = words(text)
            if any(" ".join(tw[k:k + 12]) in grams for k in range(len(tw) - 11)):
                leaks += 1
                errors.append(f"{i}: 12-word overlap with the private answer")
    doc = HERE / "PROMPT-IMPROVEMENTS.md"
    if doc.exists():
        sys.path.insert(0, str(HERE))
        from render import generated
        text = doc.read_text()
        for marker, body in generated(items, recs).items():
            seg = re.search(rf"<!-- {marker}:begin -->\n(.*?)<!-- {marker}:end -->", text, re.S)
            if not seg or seg.group(1) != body:
                errors.append(f"document section {marker} differs from shards; run render.py")
    for e in errors[:40]:
        print("FAIL", e)
    if errors:
        print(f"{len(errors)} problems")
        sys.exit(1)
    c = Counter(r["disposition"] for r in recs.values())
    print(f"PASS: {len(recs)} suggestions; dispositions {dict(c)}; answer-overlap checks "
          f"{'run' if PACKETS.exists() else 'skipped (no private packets)'}")


if __name__ == "__main__":
    main()

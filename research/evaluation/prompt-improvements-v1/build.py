"""Join everything known about each of the 384 Gemini discovery prompts. Offline; no model calls.

  python3 -B research/evaluation/prompt-improvements-v1/build.py           write items.json + private packets
  python3 -B research/evaluation/prompt-improvements-v1/build.py --check   fail if items.json differs

Public output (items.json) carries no answer text. Private per-item packets for reviewers, including
the original first answer and the reviewer record, go to ignored evals/results/prompt-improvements-v1/.
Private returns are read with zipfile and never extracted wholesale or executed.
"""
import argparse
from collections import Counter, defaultdict
from hashlib import sha256
import json
from pathlib import Path
import re
import sys
from zipfile import ZipFile

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
GD = ROOT / "evals/gemini-discovery"
BUNDLES = ROOT / "evals/results/gemini-discovery-20261108/bundles"
PRIVATE = ROOT / "evals/results/prompt-improvements-v1/items"
CONT = "gemini-discovery-375-continuation-return.zip"
FACT = "flash-factorial-68-return.zip"
SUMS = {"gemini-discovery-384-unaided-r1-return.zip": "e46468d4cc391ab4",
        CONT: "717a64d77e30462a", FACT: "fc35e74ecd73088c"}

# A request that asserts a defect as fact (rather than asking whether one exists).
ASSERTS = re.compile(r"\b(can|could|may|might) (still )?(be|end up|operate|act|dispatch|read|apply|restore|announce|leave|"
                     r"select|show|lose|keep|stay|fire|call|post|hide|merge|drop|clip|truncate|shrink|expose)\b|"
                     r"\b(doesn't|does not|don't|isn't|is not|never|stale|wrong|incorrect|broken|fails?|lost|missing)\b", re.I)
ASKS_FIX = re.compile(r"\b(fix|repair|correct|patch|change|update)\b", re.I)
ALLOWS_NO_CHANGE = re.compile(r"(no change|leave .{0,20} (alone|as is|in place)|already (correct|works?)|if .{0,30} (works|is correct))", re.I)


def checked_zip(name):
    p = BUNDLES / name
    assert sha256(p.read_bytes()).hexdigest().startswith(SUMS[name]), name
    return ZipFile(p)


def audit_rows():
    rows = {}
    for line in (GD / "BLIND-AUDIT-CASES.md").read_text().splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) == 6 and re.fullmatch(r"Q\d\d", cells[0]):
            ow, op = [x.strip() for x in cells[3].split("/")]
            bw, bp = [x.strip() for x in cells[4].split("/")]
            rows[cells[1]] = dict(mask=cells[0], lane=cells[2], originalWhole=ow, originalPrimary=op,
                                  blindWhole=bw, blindPrimary=bp, finding=cells[5])
    return rows


def factorial():
    cases = json.loads((GD / "audit-revision-1/cases.json").read_bytes())
    # Per-question whole/primary for each arm, from the published RESULTS.md table.
    by = {}
    for line in (GD / "audit-revision-1/RESULTS.md").read_text().splitlines():
        cells = [x.strip() for x in line.strip().strip("|").split("|")]
        if len(cells) == 5 and cells[0] in cases:
            by[cells[0]] = {arm: dict(zip(("whole", "primary"), (v.strip() for v in cell.split("/"))))
                            for arm, cell in zip(("unaided", "review", "text", "both"), cells[1:])}
    assert len(by) == len(cases) == 17, (len(by), len(cases))
    out = defaultdict(list)
    for name, c in cases.items():
        out[c["parent"]].append(dict(child=name, opening=c["opening"], criterion=c["criterion"], arms=by.get(name, {})))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()
    controller = json.loads((GD / "controller.json").read_bytes())
    subjects = {s["id"]: s["prompt"] for s in map(json.loads, (GD / "subjects.jsonl").read_text().splitlines())}
    z = checked_zip(CONT)
    ledger = {r["id"]: r for r in json.loads(z.read("grade-ledger.json"))}
    explore = {e["case"]: e for e in json.loads(z.read("exploratory-findings.json"))}
    audits, fact = audit_rows(), factorial()
    assert len(controller) == len(subjects) == len(ledger) == 384
    # Defective/working fixture pairs share source fixture and check id across repair and preservation.
    pair_key = lambda c: (c["source"], c.get("check"))
    by_key = defaultdict(list)
    for c in controller:
        if c["lane"] in ("repair", "preservation") and c.get("check"):
            by_key[pair_key(c)].append(c)
    siblings = defaultdict(list)
    for c in controller:
        if c.get("decision"):
            siblings[c["decision"]].append(c["id"])
    names = set(z.namelist())
    if not a.check:
        PRIVATE.mkdir(parents=True, exist_ok=True)
    items = []
    for c in controller:
        q, g = subjects[c["id"]], ledger[c["id"]]
        partner = [p for p in by_key.get(pair_key(c), []) if p["id"] != c["id"] and p["lane"] != c["lane"]] if c["lane"] in ("repair", "preservation") else []
        pair = None
        if partner:
            p = partner[0]
            mine, theirs = (g, ledger[p["id"]])
            defective, working = (mine, theirs) if c["lane"] == "repair" else (theirs, mine)
            outcome = ("both-correct" if defective["verdict"] == working["verdict"] == "pass" else
                       "fixes-defect-breaks-working" if defective["verdict"] == "pass" and working["verdict"] == "fail" else
                       "misses-defect-keeps-working" if defective["verdict"] == "fail" and working["verdict"] == "pass" else
                       "both-fail" if defective["verdict"] == working["verdict"] == "fail" else "inconclusive")
            pair = dict(partner=p["id"], partnerLane=p["lane"], partnerVerdict=theirs["verdict"],
                        partnerPrimary=theirs["primary"], outcome=outcome)
        flags = dict(assertsDefect=bool(ASSERTS.search(q)), asksForFix=bool(ASKS_FIX.search(q)),
                     allowsNoChange=bool(ALLOWS_NO_CHANGE.search(q)), words=len(q.split()))
        item = dict(id=c["id"], lane=c["lane"], platform=c["platform"], framework=c["framework"],
                    decision=c.get("decision"), source=c["source"], check=c.get("check"), sourceFile=c.get("sourceFile"),
                    rubric=c.get("rubric"), criterion=c.get("criterion"), assertions=c.get("assertions", []),
                    questionSHA256=sha256(q.encode()).hexdigest(), opening=q.strip().split("\n")[0][:240],
                    verdict=g["verdict"], primary=g["primary"], critical=g["critical"], rationale=g.get("rationale", ""),
                    audit=audits.get(c["id"]), factorialChildren=fact.get(c["id"], []),
                    exploratory=bool(explore.get(c["id"])), pair=pair,
                    siblings=[s for s in siblings.get(c.get("decision"), []) if s != c["id"]], flags=flags)
        items.append(item)
        if not a.check:
            ev = g.get("evidence")
            review = json.loads(z.read(ev)) if ev and ev in names else None
            ans = next((n for n in (f"{c['id']}/answer.txt", f"original/{c['id']}/answer.txt") if n in names), None)
            packet = dict(item, question=q, controller=c, ledger=g, review=review,
                          exploratoryFinding=explore.get(c["id"]),
                          answer=z.read(ans).decode("utf-8", "replace") if ans else None)
            (PRIVATE / f"{c['id']}.json").write_text(json.dumps(packet, indent=2) + "\n")
    summary = dict(items=len(items), byLane=dict(Counter(i["lane"] for i in items)),
                   verdicts=dict(Counter(i["verdict"] for i in items)),
                   byPlatform=dict(Counter(i["platform"] for i in items)),
                   pairs=dict(Counter(i["pair"]["outcome"] for i in items if i["pair"] and i["lane"] == "repair")),
                   audited=sum(bool(i["audit"]) for i in items),
                   factorialParents=sum(bool(i["factorialChildren"]) for i in items),
                   assertsDefect=sum(i["flags"]["assertsDefect"] for i in items))
    text = json.dumps(dict(schema=1, summary=summary, items=items), indent=2) + "\n"
    out = HERE / "items.json"
    if a.check:
        ok = out.read_text() == text
        print("PASS: items.json matches sources" if ok else "FAIL: items.json differs")
        sys.exit(0 if ok else 1)
    out.write_text(text)
    print(json.dumps(summary, indent=1))


if __name__ == "__main__":
    main()

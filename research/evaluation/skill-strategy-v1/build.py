"""Join every gold prompt set into one tiered evidence table for the strategy audit.

  python3 -B research/evaluation/skill-strategy-v1/build.py          # write items.json and private packets
  python3 -B research/evaluation/skill-strategy-v1/build.py --check  # rebuild in memory and compare

Tier 1: the 56 signal-panel questions with signal-v2 paired grades and read traces.
Tier 2: the 6 OS26 gold prompts and the 24 gold-parity scenarios not already in Tier 1.
Tier 3: the remaining discovery prompts, rolled up by decision key.
Public items.json carries grades, transitions, card reads and pointers, never answer text.
Private packets (question and grader rationale) go to evals/results/skill-strategy-v1/.
"""
from collections import Counter, defaultdict
import hashlib
import io
import json
from pathlib import Path
import sys
import zipfile

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
PRIVATE = ROOT / "evals/results/skill-strategy-v1"
RETURN = ROOT / "evals/results/signal-v2-review-20261108/signal-panel-v2-return.zip"
RETURN_SHA = "9929eb1bddb1eb850bdc6ff026bb0469852e8ecab19ef7100689595788990368"
HELD = ROOT / "research/evaluation/signal-panel-v2/held.zip"
HELD_SHA = "51bf28327715ad63929a107b9c8b3e3c364669916e3f2c0107f61b6300b45acd"
COMPONENTS = ("primary", "preservation", "verification", "integration", "rework", "whole")

load = lambda p: json.loads((ROOT / p).read_bytes())
sha = lambda b: hashlib.sha256(b).hexdigest()


def transition(u, s):
    if u is None or s is None:
        return "unpaired"
    if u == s:
        return {"pass": "both-pass", "fail": "both-fail"}.get(u, f"both-{u}")
    if u == "fail" and s == "pass":
        return "gain"
    if u == "pass" and s == "fail":
        return "loss"
    return f"{u}->{s}"


def build():
    assert sha(RETURN.read_bytes()) == RETURN_SHA, "signal-v2 return changed"
    assert sha(HELD.read_bytes()) == HELD_SHA, "sealed packet changed"
    ret, held = zipfile.ZipFile(RETURN), zipfile.ZipFile(HELD)
    grades = {(g["id"], g["arm"]): g for g in json.loads(ret.read("grades.json"))}
    traces = json.loads(ret.read("traces.json"))
    transitions = {t["id"]: t for t in json.loads(ret.read("transitions.json"))}
    panel = load("research/evaluation/signal-panel-v1/panel.json")
    assert panel == json.loads(held.read("controller/panel.json")), "v1 and v2 panels differ"

    discovery = {i["id"]: i for i in load("research/evaluation/prompt-improvements-v1/items.json")["items"]}
    review = {}
    for name in ("ios", "macos", "tvos"):
        for r in load(f"research/evaluation/prompt-improvements-v1/shards/{name}.json"):
            review[r["id"]] = r
    by_source = defaultdict(list)
    for i in discovery.values():
        by_source[i["source"]].append(i["id"])

    def prior(gid):
        i, r = discovery.get(gid), review.get(gid)
        if not i:
            return None
        return {"lane": i["lane"], "decision": i["decision"], "verdict": i["verdict"], "primary": i["primary"],
                "disposition": r and r["disposition"], "problem": r and r["problem"], "priority": r and r["priority"],
                "skill": r and r["skill"]}

    def zb(name):
        ids = by_source.get(f"research/evaluation/zero-base-v1/subjects/{name}.txt", [])
        return ids[0] if ids else None

    gold_parity = load("research/evaluation/gold-parity-v1/audit-v1/audit.json")["cases"]
    inventory = {c["id"]: c for c in load("research/evaluation/gold-parity-v1/case-inventory.json")["cases"]}
    gp_parent = {c["id"]: zb(c["id"]) for c in gold_parity}
    os26 = load("evals/os26/prompts.json")["cases"]
    ready = {c["id"]: c for c in load("evals/os26/reports/2026-11-05-gold-closeout/readiness.json")["cases"]}
    extra_os26 = {zb(f"GP26-{n:02}"): f"GP26-{n:02}" for n in range(1, 13) if zb(f"GP26-{n:02}")}
    gp_by_parent = {v: k for k, v in gp_parent.items() if v}

    tier1, private = [], {}
    for p in sorted(panel, key=lambda x: x["id"]):
        u, s = grades.get((p["id"], "unaided")), grades.get((p["id"], "skill"))
        reads = traces.get(p["id"] + ".skill", {}).get("reads", [])
        cards = sorted({r["path"].split("swift-accessibility-agent/")[-1] for r in reads if r.get("path")})
        question = held.read(f"subjects/{p['id']}.txt").decode()
        tier1.append({
            "id": p["id"], "tier": 1, "parent": p["parent"], "family": p["family"], "axis": p["axis"],
            "platform": p["platform"], "framework": p["framework"], "counterpart": p["counterpart"],
            "criterion": p["criterion"], "source": p["source"], "historicalWhole": p["frozenWhole"],
            "blindAudit": p["blind"], "opening": " ".join(question.split("```")[0].replace("#", "").split())[:220],
            "unaided": {c: u[c] for c in COMPONENTS} | {"critical": u["critical"]} if u else None,
            "skill": {c: s[c] for c in COMPONENTS} | {"critical": s["critical"]} if s else None,
            "transitions": {c: transition(u and u[c], s and s[c]) for c in COMPONENTS},
            "cardsRead": cards, "skillOpened": bool(cards),
            "prior384": prior(p["parent"]),
            "alsoGoldParity": gp_by_parent.get(p["parent"]), "alsoOS26": extra_os26.get(p["parent"]),
        })
        private[p["id"]] = {"question": question, "panelEvidence": p["evidence"], "reviewProposal": p["reviewProposal"],
                            "unaidedRationale": u and u["rationale"], "skillRationale": s and s["rationale"]}
    panel_parents = {t["parent"] for t in tier1}

    tier2 = []
    for c in os26:
        gid = zb(c["id"])
        tier2.append({"id": c["id"], "tier": 2, "set": "os26", "parent": gid, "family": c["family"],
                      "platform": c["platform"], "framework": c["framework"], "control": c["control"],
                      "opening": c["prompt"].strip().split("\n")[2 if c["prompt"].startswith(("iOS", "iPadOS", "tvOS", "macOS")) else 0][:220],
                      "gates": [g["id"] for g in ready[c["id"]]["gates"]], "goldReady": ready[c["id"]]["status"],
                      "prior384": prior(gid) if gid else None, "inPanel": gid in panel_parents})
    for c in gold_parity:
        gid = gp_parent[c["id"]]
        if gid in panel_parents:
            continue
        inv = inventory[c["id"]]
        tier2.append({"id": c["id"], "tier": 2, "set": "gold-parity", "parent": gid, "family": c["family"],
                      "platform": inv["platform"], "framework": inv["framework"], "control": c["family"].startswith("control/"),
                      "criteria": [{"id": k["id"], "coverage": k["coverage"]} for k in c["criteria"]],
                      "coverage": dict(Counter(k["coverage"] for k in c["criteria"])),
                      "caseDecision": c.get("caseDecision"), "prior384": prior(gid) if gid else None})
        private[c["id"]] = {"criteria": [{"id": k["id"], "pass": k.get("pass"), "finding": k.get("finding"),
                                           "nextAction": k.get("nextAction")} for k in c["criteria"]]}

    covered = panel_parents | {t["parent"] for t in tier2 if t["parent"]}
    rollup = defaultdict(lambda: {"items": 0, "verdict": Counter(), "disposition": Counter(), "priority": Counter(),
                                  "skill": Counter(), "platforms": Counter()})
    for gid, i in discovery.items():
        if gid in covered:
            continue
        r, key = review[gid], i["decision"] or f"open:{i['lane']}"
        g = rollup[key]
        g["items"] += 1
        g["verdict"][i["verdict"]] += 1
        g["disposition"][r["disposition"]] += 1
        g["priority"][r["priority"]] += 1
        g["platforms"][i["platform"]] += 1
        for s in r["skill"]:
            g["skill"][s] += 1
    tier3 = [{"decision": k, "items": v["items"], **{f: dict(v[f]) for f in ("verdict", "disposition", "priority", "skill", "platforms")}}
             for k, v in sorted(rollup.items(), key=lambda kv: (-kv[1]["items"], kv[0]))]

    summary = {
        "tier1": len(tier1), "tier2": len(tier2), "tier3Items": sum(t["items"] for t in tier3), "tier3Decisions": len(tier3),
        "distinctItems": len(tier1) + len(tier2) + sum(t["items"] for t in tier3),
        "tier1Whole": dict(Counter(t["transitions"]["whole"] for t in tier1)),
        "tier1Opened": sum(t["skillOpened"] for t in tier1 if t["skill"]),
        "tier1SkillAnswers": sum(1 for t in tier1 if t["skill"]),
        "inputs": {"return": RETURN_SHA, "held": HELD_SHA},
    }
    return {"schema": 1, "summary": summary, "tier1": tier1, "tier2": tier2, "tier3": tier3}, private


def main():
    public, private = build()
    out = json.dumps(public, indent=1, sort_keys=True) + "\n"
    if "--check" in sys.argv:
        same = (HERE / "items.json").read_text() == out
        print("PASS" if same else "FAIL: items.json differs from a rebuild")
        sys.exit(0 if same else 1)
    (HERE / "items.json").write_text(out)
    PRIVATE.mkdir(parents=True, exist_ok=True)
    (PRIVATE / "packets.json").write_text(json.dumps(private, indent=1, sort_keys=True))
    print(json.dumps(public["summary"], indent=1))


if __name__ == "__main__":
    main()

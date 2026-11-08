"""Score a partial or complete adjudicated ledger; never calls a model."""
import argparse
from collections import Counter, defaultdict
from hashlib import sha256
import json
from pathlib import Path

HERE=Path(__file__).resolve().parent
ARMS=("unaided","challenger")
VERDICTS={"pass","fail","inconclusive","not-run"}
def digest(path):return sha256(path.read_bytes()).hexdigest()

def summarize(cases, grades, seal, seal_hash):
    by={c["id"]:c for c in cases}
    pairs=defaultdict(dict)
    for r in grades:
        i=r["id"];arm=r["arm"]
        if i not in by or arm not in ARMS or arm in pairs[i]:
            raise ValueError(f"Unknown or duplicate cell: {i}/{arm}")
        if (r["sealSHA256"]!=seal_hash or r["inputSHA256"]!=by[i]["inputSHA256"] or
            r["skillSHA256"]!=(None if arm=="unaided" else seal["challengerSHA256"])):
            raise ValueError(f"Unmatched packet, question or skill: {i}")
        if r["verdict"] not in VERDICTS or r["primary"] not in VERDICTS:
            raise ValueError("Invalid verdict")
        if type(r["critical"]) is not bool:raise ValueError("critical must be boolean")
        if r["verdict"]=="not-run" and r["primary"]!="not-run":raise ValueError("Unexpected primary grade")
        if r["verdict"]=="pass" and by[i].get("decision") and r["primary"]!="pass":
            raise ValueError("A whole-answer pass must satisfy the registered decision")
        if r["primary"]=="fail" and r["verdict"]!="fail":raise ValueError("Primary loss cannot be an overall pass")
        if r["critical"] and r["verdict"]!="fail":raise ValueError("Critical loss requires failure")
        if r["verdict"] in ("pass","fail") and not all(r.get(k) for k in ("answerSHA256","rationale","evidence","cohort")):
            raise ValueError("Missing grading or cohort evidence")
        if r["verdict"]!="not-run" and r["model"]!=seal["model"]:raise ValueError("Model mismatch")
        pairs[i][arm]=r
    counts=Counter(); groups=defaultdict(list); incidents=[]; regressions=[]; per=defaultdict(Counter)
    armTotals={arm:Counter() for arm in ARMS}
    outcomes={}
    for i,c in by.items():
        a,b=(pairs[i].get(arm,{}) for arm in ARMS)
        x,y=a.get("verdict"),b.get("verdict")
        for arm,v in zip(ARMS,(x,y)):
            armTotals[arm][v or "not-run"]+=1
        comparable=x in ("pass","fail") and y in ("pass","fail") and a["cohort"]==b["cohort"]
        outcome={("fail","pass"):"rescued",("pass","fail"):"regressed",("fail","fail"):"persistent",
                 ("pass","pass"):"preserved"}.get((x,y),"inconclusive") if comparable else "inconclusive"
        counts[outcome]+=1;per[c["platform"]+"/"+c["framework"]][outcome]+=1
        outcomes[i]=outcome
        if b.get("critical") and not a.get("critical"): incidents.append(i)
        if outcome=="regressed":regressions.append(i)
        if c.get("decision"):groups[c["decision"]].append((c["lane"],a.get("primary"),outcome,comparable))
    observed=[]; rescued=[]; partial=[]
    for k,rows in groups.items():
        failures=[o for lane,p,o,_ in rows if lane in ("repair","workflow") and p=="fail"]
        if not failures:continue
        observed.append(k)
        if all(o=="rescued" for o in failures) and all(done and o!="regressed" for _,_,o,done in rows):
            rescued.append(k)
        elif "rescued" in failures:partial.append(k)
    return dict(planned=len(cases),submittedRows=len(grades),armTotals=armTotals,pairOutcomes=dict(counts),platforms=dict(per),
                primaryDistinctFailures=sorted(observed),fullyRescuedDecisions=sorted(rescued),
                partiallyRescuedDecisions=sorted(partial),regressions=regressions,
                candidateCriticalFlagsNotSeenOnBaseline=incidents,caseOutcomes=outcomes)

if __name__=="__main__":
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("ledger",type=Path,help="JSON array of controller grade records")
    a=ap.parse_args()
    s=json.loads((HERE/"seal.json").read_bytes())
    if digest(HERE/"controller.json")!=s["controllerSHA256"]:raise SystemExit("Controller mismatch")
    print(json.dumps(summarize(json.loads((HERE/"controller.json").read_bytes()),json.loads(a.ledger.read_bytes()),
                               s,digest(HERE/"seal.json")),indent=2))

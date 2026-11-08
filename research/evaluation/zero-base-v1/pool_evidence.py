"""Reconcile private qualification attempts by submitted bytes, oracle and expected result."""
import argparse
import json
from pathlib import Path
import sys
from build import HERE, ROOT, digest
sys.path.insert(0,str(ROOT/"evals/pool"))
import pool


def reconcile():
    tasks = pool.load()
    out = {t.id:dict(matching=[], prior=[], status="no matching receipt") for t in tasks}
    for p in sorted((ROOT/"evals/results/pool").glob("attempt-*/scorecard.json")):
        report=json.loads(p.read_bytes())
        for t in tasks:
            rows=[v for v in report["rows"] if v["task"]==t.id]
            if not rows:
                continue
            desired={(k,digest(src),digest(t.oracle_source.encode())):want for k,src,want in t.variants}
            actual={(r["variant"],r["submissionSHA256"],r["oracleSHA256"]):r["status"] for r in rows}
            entry=dict(receipt=str(p.relative_to(ROOT)),sha256=digest(p.read_bytes()),utc=report["startUTC"],
                       environment={k:report.get(k) for k in ("host","xcode","sdkVersions","deployment","simulatorRuntime")})
            matches=actual.keys()==desired.keys() and len(rows)==len(desired)
            if matches:
                for r in rows:
                    d=ROOT/r["artifacts"]
                    assert digest((d/"Oracle.swift").read_bytes())==r["oracleSHA256"]
                    assert digest((d/"Submission.swift").read_bytes())==r["submissionSHA256"]
                entry["mismatches"]=[k[0] for k,v in desired.items() if actual[k]!=v]
                entry["accepted"]=not entry["mismatches"] and report["accepted"]
            out[t.id]["matching" if matches else "prior"].append(entry)
    for record in out.values():
        matches=record["matching"]
        if matches:
            record["status"]="qualified on recorded anchor" if all(e["accepted"] for e in matches) else "unresolved; exclude from grading"
    return (json.dumps(out,indent=2)+"\n").encode()


if __name__=="__main__":
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--check",action="store_true")
    data=reconcile()
    p=HERE/"pool-receipts.json"
    if ap.parse_args().check:
        assert p.read_bytes()==data
    else:
        p.write_bytes(data)
    for case,row in json.loads(data).items():
        print(case,row["status"])

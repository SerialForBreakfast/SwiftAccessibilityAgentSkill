"""Summarize captured results without rebuilding or rerunning any submission."""
import hashlib,json,sys
from pathlib import Path
dest=Path(sys.argv[1])
HISTORY=Path(__file__).resolve().parent.parent/"failure-driven/checkout-review-20261106"
observations=json.loads((dest/"typechecks.json").read_bytes())
def hash_(b):
    return hashlib.sha256(b).hexdigest()
result=json.loads((dest/"native/result.json").read_bytes())
historical=json.loads((HISTORY/"unit-results.json").read_bytes())
execution=result["execution"]
summary={"case":"GP26-03","firstPassUnchanged":True,"answerRepairs":0,"typechecks":observations,
         "environment":result["environment"],"unitExecution":execution,
         "matchesPriorTypecheckExits":all(x["exit"]==x["historicalExit"] for x in observations),
         "matchesPriorUnitTests":sorted(execution["executedTestIds"])==sorted(historical["execution"]["executedTestIds"])
         and sorted(execution["failedTestIds"])==sorted(historical["execution"]["failedTestIds"]),
         "nativeReceiptSHA256":hash_((dest/"native/result.json").read_bytes())}
(dest/"replay-summary.json").write_text(json.dumps(summary,indent=2)+"\n")

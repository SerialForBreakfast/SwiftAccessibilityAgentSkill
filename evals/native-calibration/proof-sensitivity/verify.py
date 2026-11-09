"""Validate the public board against immutable first-attempt native artifacts."""
import json
import re
from collections import Counter
from replay import HERE, ORIGINAL, PRIVATE, BINDINGS, sha
from probes.verify import verified
from grade import pinned, REPLAY, REPLAY_SHA


def require(ok, message):
    if not ok:
        raise ValueError(message)


def check(board):
    controls={(p["platform"],p["method"]):p for p in verified()}
    originals={(r["id"],r["arm"]):r for r in pinned(REPLAY,REPLAY_SHA)["rows"]}
    batch=PRIVATE/"native-calibration"/board["batch"]
    require(json.loads((batch/"summary.json").read_bytes())==board,"private/public mismatch")
    expected={(case,arm) for case in BINDINGS for arm in ("skill","unaided")}
    seen=set()
    for row in board["rows"]:
        case,arm=row["id"],row["arm"]
        require((case,arm) in expected-seen, "unexpected or duplicate cell")
        seen.add((case,arm))
        platform,family,method=BINDINGS[case]
        cell=ORIGINAL/(case+"."+arm)
        require(sha((cell/"answer.txt").read_bytes())==row["answerSHA256"],"original answer")
        meta=json.loads((cell/"input.json").read_bytes())
        original, = [a for a in originals[case,arm]["attempts"] if a["run"]==ORIGINAL.name]
        require(original["inputs"]==meta["inputs"],"unregistered staged inputs")
        for name,expected_hash in original["inputs"].items():
            require(sha((cell/name).read_bytes())==expected_hash,"original staged byte drift")
        proofs=sorted(cell.glob("Proof*.swift"))
        require([sha(p.read_bytes()) for p in proofs]==row["proofHashes"],"original proof")
        require(meta["returnedProofFences"]==row["returnedProofFences"],"original fences")
        control=controls[platform,method]
        if not proofs or family=="Sheet":
            require(row["outcome"]==("interface-gap" if proofs else "no-executable-proof")
                    and not row["attempts"],"gap misgraded")
            continue
        require(row["anchor"]==control["anchor"],"anchor mismatch")
        require(set(row["attempts"])==set(control["runs"]),"incomplete variants")
        for mode,receipt in row["attempts"].items():
            w=batch/(case+"."+arm)/mode
            require(json.loads((w/"receipt.json").read_bytes())==receipt,"receipt mismatch")
            for f,h in json.loads((w/"intent.json").read_bytes())["inputs"].items():
                require(sha((w/f).read_bytes())==h,"input drift")
            src=w/"Sources"/meta["module"]/"Subject.swift"
            require(sha(src.read_bytes())==receipt["subjectSHA256"]==control["runs"][mode]["subjectSHA256"],"control drift")
            for p in proofs:
                require((w/"Tests/Checks"/p.name).read_bytes()==p.read_bytes(),"proof changed")
            data=(w/"native.log").read_bytes()
            require(sha(data)==receipt["logSHA256"],"log drift")
            methods=re.findall(r"Test Case '([^'\n]+)' (passed|failed)",data.decode(errors="replace"))
            require([list(m) for m in methods]==receipt["methods"],"method outcomes")
            expected_methods=set(re.findall(r'func (test\w+)\s*\(', '\n'.join(p.read_text() for p in proofs)))
            passed=(receipt["exit"]==0 and len(methods)==len(expected_methods)>0 and
                    {k.split()[-1].rstrip("]") for k,s in methods if s=="passed"}==expected_methods)
            require((receipt["status"]=="pass")==passed,"false pass")
        allpass=all(r["status"]=="pass" for r in row["attempts"].values())
        require(row["outcome"]==("missed-qualified-mutant" if allpass else "needs-review"),"wrong classification")
    require(seen==expected,"missing cases")
    return Counter(r["outcome"] for r in board["rows"])


if __name__=="__main__":
    print(check(json.loads((HERE/"evidence.json").read_bytes())))

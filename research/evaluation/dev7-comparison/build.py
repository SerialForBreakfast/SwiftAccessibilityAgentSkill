"""Offline builder. Default operation compares bytes; --create exclusively creates new files."""
import argparse
import hashlib
import importlib.util
import json
import subprocess
import sys
from pathlib import Path

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
E = HERE.parent
ROOT = E.parents[1]
C = E / "failure-driven/candidates/0.3.0-dev.7"
AUD = E / "gold-parity-v1/audit-v1/audit.json"
MAC = E / "gold-parity-v1/mac-evidence-20261107"
V2 = E / "milestone-package-v2"
BASE = "37e70c5e2ba87fd58f79a091ba1cba437049620d"
spec = importlib.util.spec_from_file_location("candidate_router", C / "route.py")
router = importlib.util.module_from_spec(spec)
spec.loader.exec_module(router)


def load(p):
    return json.loads(p.read_bytes())


def sha(b):
    return hashlib.sha256(b).hexdigest()


def encode(o):
    return (json.dumps(o, indent=2, ensure_ascii=False) + "\n").encode()


def keyed(rows):
    result = {r["id"]: r for r in rows}
    assert len(result) == len(rows)
    return result


def check_protected():
    # New artifacts must never mask a changed or deleted historical input.
    paths = ["SKILL.md", "agents", "references", "skill", "VERSION", "evals/baselines",
             "evals/os26", "research/evaluation/milestone-package-v2",
             "research/evaluation/gemini-preflight-v1", "research/evaluation/gold-parity-v1",
             "research/evaluation/failure-driven/candidates/0.3.0-dev.5",
             "research/evaluation/failure-driven/candidates/0.3.0-dev.6"]
    subprocess.run(["git", "diff", "--quiet", BASE, "--", *paths], cwd=ROOT, check=True)
    assert not subprocess.check_output(["git", "ls-files", "--others", "--exclude-standard", "--", *paths], cwd=ROOT)


def build():
    check_protected()
    audit = load(AUD)
    mac = keyed(load(MAC / "index.json")["cases"])
    shared = keyed(load(MAC / "portable-reconciliation.json")["rows"])
    assert len(shared) == 73 and all(x["sourceHashMatches"] and x["matchingPositiveReceipt"] for x in shared.values())
    audit_cases = keyed(audit["cases"])
    guide = keyed(load(E / "gemini-preflight-v1/controller.json")["rows"])
    prior = load(E / "gemini-controlled-run-20261107/summary.json")
    previous = {r["case"]: r for r in prior["pair_rows"]}
    matrix, jobs, outputs = [], [], {}
    for case in load(V2 / "manifest.json")["cases"]:
        cid = case["id"]
        plan = next(p for p in case["plans"] if p["arm"] == "candidate-controlled")
        raw = (V2 / plan["path"]).read_bytes()
        assert sha(raw) == plan["sha256"]
        old = json.loads(raw)["messages"]
        assert [m["role"] for m in old] == ["system", "user"]
        user = json.loads(old[1]["content"])
        question = user["request"]
        a = audit_cases[cid]
        assert question == (ROOT / a["subject"]["path"]).read_text()
        question_change = None
        if case["topic"] == "lifecycle":
            question_change = "Specify the product fallback already graded by the controller."
            question = question.replace("Describe the ownership", "If the opener disappears, use the first remaining eligible item, or make no request if none remains. Describe the ownership")
            assert question != user["request"]
        refs = []
        if user["suppliedReferences"]:
            status, refs = router.select(case["platform"], case["framework"], case["topic"])
            assert status == "selected", (cid, status)
        entry = (C / "ENTRYPOINT.md").read_text().strip()
        session = old[0]["content"].split("\n\n", 1)[0]
        for arm, system, references in (("dev5", old[0]["content"], user["suppliedReferences"]),
                                        ("dev7", session + "\n\n" + entry, refs)):
            subject = {"request": question, "suppliedReferences": references}
            messages = [{"role": "system", "content": system},
                        {"role": "user", "content": json.dumps(subject, ensure_ascii=False, separators=(",", ":"))}]
            dest = f"subjects/{cid}/{arm}.json"
            body = encode({"messages": messages})
            outputs[dest] = body
            jobs.append(dict(case=cid, arm=arm, path=dest, sha256=sha(body),
                             requestSha256=sha(question.encode()), contextBytes=sum(len(r["content"].encode()) for r in references),
                             messageContentBytes=sum(len(m["content"].encode()) for m in messages), tokens=None))
        criteria = []
        mrows = keyed(mac[cid]["criteria"])
        for item, oldrule in zip(a["criteria"], guide[cid]["criteria"], strict=True):
            key = item["id"]
            assert oldrule["id"] == key
            links = [r["reference"] for r in mrows[key]["references"]]
            assert set(links) == set(item["contracts"]) and all(k in shared for k in links)
            for pin in item["sourcePins"]:
                assert sha((ROOT / pin["path"]).read_bytes()) == pin["sha256"]
            scope = item["finding"]
            change = None
            if case["topic"] == "lifecycle" and oldrule["index"] == 0:
                change = "Assess actual dismissal completion, not the Close request. A serialized presenter is valid if old callbacks cannot consume a new panel."
            if cid == "tvos-uikit-lifecycle" and oldrule["index"] == 1:
                change = "End mutating access before external dispatch; a returned decision applied by the caller is sufficient."
            if cid == "mixed-macos-owner" and oldrule["index"] == 1:
                change = "Do not infer hidden AppKit children from the parent element flag alone. Asking for wrapper and native role/children code without a patch is complete."
            if item["coverage"] == "genuine_gap":
                change = "Score proposed design and integration from the answer, not runtime success. Existing receipts do not exercise this checkout."
            criteria.append(dict(id=key, meets=oldrule["pass"], gap=oldrule["fail"], insufficient=oldrule["missing"],
                clarification=change, evidenceClass=item["coverage"], scope=scope, sources=item["sourcePins"],
                contracts=links, receiptHashes=[shared[k]["positiveReceiptHash"] for k in links],
                negatives=item["assertionNegativeWitnesses"], supplemental=[s for s in audit["supplementalReuse"] if s["criterion"] == key]))
        matrix.append(dict(case=cid, family=case["family"], framework=case["framework"], platform=case["platform"],
            originalQuestion=a["subject"], questionChange=question_change, historicalTransition=previous[cid]["reviewer_task_transition"],
            candidateGuidance=[r["path"] for r in refs] or ["ENTRYPOINT.md (reference-free control)"],
            status="ready for comparative scoring", reason="Design/answer review only. "+a["criteria"][0]["finding"],
            acceptedAlternatives=guide[cid]["acceptedAlternatives"], criteria=criteria))
    assert len(matrix)==24 and sum(len(c["criteria"]) for c in matrix)==78 and len(jobs)==48
    outputs["controller/scoring.json"] = encode(matrix)
    outputs["jobs.json"] = encode(jobs)
    sources = [AUD, MAC / "index.json", MAC / "portable-reconciliation.json", V2 / "manifest.json",
               E / "gemini-controlled-run-20261107/summary.json", E / "gemini-preflight-v1/controller.json",
               E / "independent-v2-review-20261107/review.json", E / "gemini-preflight-v1/RETROSPECTIVE-TRANSPORT.md",
               *sorted(p for p in C.rglob("*") if p.is_file() and "__pycache__" not in p.parts),
               *[HERE / f for f in ("build.py","checks.py","DISTINCTIONS.md","SCORING.md","BIGDOG.md","AUTHORING.md","REQUEST.md")]]
    outputs["seal.json"] = encode(dict(version="dev5-vs-dev7/1", historicalAnchor=BASE, executionAuthorized=False,
        approvedSessions=0, approvedSpend=0, proposedFirstAttempts=48, retries=0, eligibility="development, source-scored only",
        inputs={str(p.relative_to(ROOT)):sha(p.read_bytes()) for p in sources},
        files={k:sha(v) for k,v in outputs.items()}))
    return outputs


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--create", action="store_true")
    args = parser.parse_args()
    for name, data in build().items():
        dest = HERE / name
        if args.create and not dest.exists():
            dest.parent.mkdir(parents=True, exist_ok=True)
            with dest.open("xb") as stream:
                stream.write(data)
        elif dest.read_bytes() != data:
            sys.exit("Seal mismatch: " + name)
    print("Verified 24 pairs, 78 criteria and protected checkpoint; no provider execution.")

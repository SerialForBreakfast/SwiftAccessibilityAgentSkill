#!/usr/bin/env python3
"""Offline evidence indexing; authored semantic decisions are separate inputs.

No native/model execution, networking, temporary files or outside-project writes.
Run from any directory with --write to materialize, or --check to verify outputs.
"""
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[4]
HERE = Path(__file__).resolve().parent
CONTROLLER = "research/evaluation/gemini-preflight-v1/controller.json"
BINDINGS = "research/evaluation/assertion-bindings-v1/bindings.json"
RUBRICS = "research/evaluation/rubric-closure-v1/rubrics.json"
SEED = "research/evaluation/gold-parity-v1/case-inventory.json"
LEDGER = "research/evaluation/local-qualification-v1/evidence-ledger.json"
INPUTS = [CONTROLLER, BINDINGS, RUBRICS, SEED, LEDGER, "GoldPrompts.md",
          "research/evaluation/independent-v2-review-20261107/review.json",
          "research/evaluation/v2-controller-resolution-20261107/overlay-review.json",
          "research/evaluation/v2-controller-resolution-20261107/composite-controller.json",
          "research/evaluation/gemini-controlled-run-20261107/summary.json",
          "research/evaluation/swiftui-review-v1/results-index.json",
          "evals/reports/local-dev5-20261107/summary.json",
          "evals/os26/reports/2026-11-05-gold-closeout/model-input-plan.json",
          "evals/os26/reports/2026-11-05-gold-closeout/reviewed-evidence.json",
          "evals/os26/reports/2026-11-05-gold-closeout/readiness.json",
          "research/evaluation/failure-driven/PRD.md",
          "research/evaluation/gold-parity-v1/audit-v1/decisions.json",
          "research/evaluation/gold-parity-v1/audit-v1/audit.py",
          "research/evaluation/gold-parity-v1/audit-v1/test_audit.py"]


def path(name):
    p = (ROOT / name).resolve()
    if not p.is_relative_to(ROOT):
        raise ValueError("Evidence path outside project")
    return p


def digest(data):
    return hashlib.sha256(data).hexdigest()


def sha(name):
    return digest(path(name).read_bytes())


def read(name):
    return json.loads(path(name).read_text())


def pinned(name, expected):
    actual = sha(name)
    if actual != expected:
        raise ValueError("Hash mismatch: " + name)
    return {"path": name, "sha256": actual}


def result_hash(row):
    return row.get("originalResultHash", row.get("originalRecordHash"))


def receipt_rows(data):
    return data.get("attempts", data.get("rows", []))


def row_check(row):
    return row.get("checkId", row.get("check"))


def check_receipt(row, manifest, manifest_hash, index):
    """Check declared outcomes against exact selected tests, not test-name leads."""
    checks = {c["id"]: c for c in manifest["checks"]}
    check = checks.get(row_check(row))
    if not check:
        return None
    if row.get("manifestHash", index.get("manifestHash")) != manifest_hash:
        return None  # historical/other package evidence remains separate
    execution = row["execution"]
    actual = set(execution["executedTestIds"])
    expected = set(check["testIds"])
    failed = set(execution["failedTestIds"])
    intended = set(check.get("failureIds", []))
    issues = []
    if actual != expected:
        issues.append("selected-test-set-mismatch")
    if execution.get("build") != "passed" or execution.get("infrastructureError"):
        issues.append("build-or-infrastructure-error")
    if execution.get("signal") or execution.get("skippedTests"):
        issues.append("signal-or-skipped-tests")
    if row.get("status") != "passed" or row.get("observed") != check["expected"]:
        issues.append("unexpected-outcome")
    if check["lane"] == "unit" and not actual:
        issues.append("empty-unit-selection")
    if check["expected"] == "failure":
        if not intended or failed != intended or not failed <= actual:
            issues.append("wrong-or-missing-intended-assertion-failure")
        if not isinstance(execution.get("exitCode"), int) or execution["exitCode"] == 0:
            issues.append("missing-or-successful-negative-exit")
    elif failed or execution.get("exitCode") != 0:
        issues.append("failed-positive")
    return {"check": check["id"], "attempt": row.get("attempt"),
            "originalResultHash": result_hash(row), "expected": check["expected"],
            "observed": row["observed"], "lane": check["lane"],
            "executedTestIds": sorted(actual), "failedTestIds": sorted(failed),
            "environment": row["environment"], "issues": issues}


def contract_record(contract, packages):
    manifest_name = contract["manifest"]
    manifest_pin = pinned(manifest_name, contract["manifestSha256"])
    manifest = read(manifest_name)
    source_pins = [pinned(p["path"], p["sha256"]) for p in contract["sourcePins"]]
    file_pin = pinned(contract["file"], contract["fileSha256"])
    method = contract.get("method", contract)
    data = path(contract["file"]).read_bytes()
    snippet = data[method["startByte"]:method["endByte"]]
    if digest(snippet) != contract["methodSha256"]:
        raise ValueError("Method changed: " + contract["id"])
    receipt = contract["receipt"]
    index_name = receipt.get("index", receipt.get("path"))
    index_pin = pinned(index_name, receipt.get("indexSha256", receipt.get("sha256")))
    index = read(index_name)
    matching = [r for r in receipt_rows(index) if result_hash(r) == receipt["originalResultHash"]]
    if len(matching) != 1:
        raise ValueError("Receipt identity unresolved: " + contract["id"])
    row = matching[0]
    selected = check_receipt(row, manifest, manifest_pin["sha256"], index)
    if not selected or selected["issues"] or contract["testId"] not in selected["executedTestIds"]:
        raise ValueError("Invalid contract receipt: " + contract["id"])
    if selected["environment"] != receipt["environment"]:
        raise ValueError("Receipt environment mismatch: " + contract["id"])
    if manifest_name not in packages:
        records = [x for r in receipt_rows(index)
                   if (x := check_receipt(r, manifest, manifest_pin["sha256"], index))]
        packages[manifest_name] = {"manifest": manifest_pin, "sourcePins": source_pins,
            "receiptIndex": index_pin, "receipts": records,
            "limitations": manifest["limitations"],
            "rawOriginalAvailability": "Indexed original hashes; full private originals not established by this audit."}
    return {"id": contract["id"], "manifest": manifest_name, "testId": contract["testId"],
            "file": file_pin, "line": method["line"], "methodSha256": digest(snippet),
            "assertionSource": snippet.decode(), "receiptIndex": index_name,
            "receiptOriginalHash": receipt["originalResultHash"],
            "environment": selected["environment"],
            "limitation": "Existing fixture assertions only; not generated-answer validation or independent qualification."}


def reuse_record(candidate):
    """Verify additional existing evidence without rebinding the frozen controller."""
    name = candidate["manifest"]
    manifest = read(name)
    index_name = candidate["receiptIndex"]
    index = read(index_name)
    rows = [r for r in receipt_rows(index)
            if r.get("manifestHash", index.get("manifestHash")) == sha(name)
            and row_check(r) == candidate["check"]]
    assert len(rows) == 1, name
    receipt = check_receipt(rows[0], manifest, sha(name), index)
    assert receipt and not receipt["issues"], name
    assert set(candidate["testIds"]) <= set(receipt["executedTestIds"])
    sources = [pinned(str((Path(name).parent / f["path"]).as_posix()), f["sha256"])
               for f in manifest["files"]]
    test_pin = next(p for p in sources if p["path"] == candidate["testFile"])
    text = path(test_pin["path"]).read_text()
    methods = []
    for tid in candidate["testIds"]:
        method = tid.split("/")[1]
        match = re.search(r"^    func " + re.escape(method) + r"\(", text, re.M)
        assert match, tid
        following = re.search(r"^    func |^}", text[match.end():], re.M)
        assert following, tid
        snippet = text[match.start():match.end() + following.start()].rstrip()
        methods.append({"testId": tid, "line": text[:match.start()].count("\n") + 1,
                        "sha256": digest(snippet.encode()), "source": snippet})
    public = rows[0].get("publicResult")
    public_pin = pinned(public["path"], public["sha256"]) if public else None
    return {**candidate, "status": "existing-evidence-reuse-candidate-not-independent-rebinding",
            "manifestSha256": sha(name), "sourcePins": sources,
            "receiptIndexSha256": sha(index_name), "receipt": receipt,
            "publicResult": public_pin, "methods": methods}


def build():
    controller, seed = read(CONTROLLER), read(SEED)
    for pin in seed["inputs"]:
        pinned(pin["path"], pin["sha256"])
    decisions = read("research/evaluation/gold-parity-v1/audit-v1/decisions.json")
    contracts = read(BINDINGS)["contracts"]
    contracts.update({r["id"]: r for r in read(RUBRICS)["supplementalContracts"]})
    seed_by_id = {r["id"]: r for r in seed["cases"]}
    ledger = {r["id"]: r for r in read(LEDGER)["rows"]}
    expected_ids = {k["id"] for r in controller["rows"] for k in r["criteria"]}
    assert set(decisions["criteria"]) == expected_ids and len(expected_ids) == 78
    packages, selected_contracts, cases = {}, {}, []
    for row in controller["rows"]:
        pinned(row["subject"]["path"], row["subject"]["sha256"])
        case = {"id": row["id"], "family": seed_by_id[row["id"]]["family"],
                "subject": row["subject"], "criteria": [],
                "caseDecision": decisions["cases"][row["id"]],
                "historicalLedgerManifest": ledger[row["id"]].get("manifest", {}).get("path"),
                "qualification": "provisional-author-audit; independent acceptance pending"}
        for criterion in row["criteria"]:
            item = {"id": criterion["id"], "pass": criterion["pass"],
                    **decisions["criteria"][criterion["id"]]}
            assert item["coverage"] in {"direct_evidence", "partial_evidence", "review_only", "genuine_gap", "not_audited"}
            item["contracts"] = criterion["priorContractIds"] + criterion["supplementalContractIds"]
            for cid in item["contracts"]:
                if cid not in selected_contracts:
                    selected_contracts[cid] = contract_record(contracts[cid], packages)
            binding = criterion.get("sourceBinding")
            if binding:
                sources = binding["application_acceptance_sources"][:]
                if binding.get("separate_declaration_context"):
                    sources.append(binding["separate_declaration_context"])
                item["sourceInterpretation"] = "Current rebound application/policy/declaration separation; prior anchors historical."
            else:
                sources = row["sources"]
                item["sourceInterpretation"] = "Existing local source/policy anchors; not a live primary-source refresh."
            item["sourcePins"] = [pinned(s["path"], s["sha256"]) for s in sources]
            item["assertionNegativeWitnesses"] = [
                {"manifest": name, "check": r["check"], "receiptIndex": p["receiptIndex"]["path"],
                 "failedTestIds": r["failedTestIds"], "issues": r["issues"]}
                for name, p in packages.items() for r in p["receipts"]
                if r["expected"] == "failure" and
                any(selected_contracts[cid]["testId"] in r["failedTestIds"] and selected_contracts[cid]["manifest"] == name
                    for cid in item["contracts"])]
            item["calibration"] = "48 design fixtures reported by completed comparison; raw bytes unavailable here; criterion mapping unverified."
            item["independentAcceptance"] = False
            case["criteria"].append(item)
        case["negativeChecksOnSelectedAssertions"] = [
            {"manifest": name, "check": check}
            for name, check in sorted({(w["manifest"], w["check"])
                                      for k in case["criteria"] for w in k["assertionNegativeWitnesses"]})]
        cases.append(case)
    assert len(cases) == 24 and len({r["family"] for r in cases}) == 12
    counts = Counter(k["coverage"] for r in cases for k in r["criteria"])
    reuse = [reuse_record(c) for c in decisions["reuseCandidates"]]
    original_inputs = read("evals/os26/reports/2026-11-05-gold-closeout/model-input-plan.json")["cases"]
    original_evidence = {r["id"]: r for r in read("evals/os26/reports/2026-11-05-gold-closeout/reviewed-evidence.json")["cases"]}
    crosswalk = []
    for c in decisions["originalGoldCrosswalk"]:
        original = next(r for r in original_inputs if r["id"] == c["id"])
        question = original["input"]["content"]
        duplicates = [r["id"] for r in cases if path(r["subject"]["path"]).read_text().strip() == question.strip()]
        assert not duplicates
        crosswalk.append({**c, "originalQuestionSha256": digest(question.encode()),
                          "originalEvidenceRecordSha256": digest(json.dumps(original_evidence[c["id"]], sort_keys=True).encode()),
                          "originalEvidenceRecordHashBasis": "Derived index: UTF-8 json.dumps(case, sort_keys=True); not an original raw-file hash.",
                          "exactQuestionMatches": duplicates,
                          "qualificationTransfer": "None; shared concerns are not identical question/fixture contracts."})
    all_receipts = [r for p in packages.values() for r in p["receipts"]]
    bound_cases = [r for r in cases if any(k["contracts"] for k in r["criteria"])]
    negative_counts = Counter("zero" if not r["negativeChecksOnSelectedAssertions"] else
                              "one" if len(r["negativeChecksOnSelectedAssertions"]) == 1 else "twoOrMore"
                              for r in bound_cases)
    summary = {"cases": 24, "criteria": 78, "families": 12,
               "coverage": dict(sorted(counts.items())), "selectedAssertionMethods": len(selected_contracts),
               "linkedManifestPackages": len(packages),
               "receiptRowsChecked": len(all_receipts),
               "receiptRowsWithIssues": sum(bool(r["issues"]) for r in all_receipts),
               "supplementalReuseMethods": len({(r["manifest"], t) for r in reuse for t in r["testIds"]}),
               "casesWithBoundNativeAssertions": len(bound_cases),
               "negativeCheckCountsOnSelectedAssertions": dict(sorted(negative_counts.items())),
               "newGoldQualifications": 0, "modelCalls": 0, "nativeRuns": 0}
    return {"schema": "gold-parity-first-pass-audit-v1", "status": "executed-author-audit-not-independent-acceptance",
            "visibility": "controller-only", "authorization": "Owner: Ok start our tasks. Do a large tranche",
            "executionModel": "Current authoring chat only; exact serving revision and complete provider request unavailable. No subject/judge model run.",
            "scope": "GPAR-01 portable audit; GPAR-02 remains pending Mac packet.",
            "inputPins": [{"path": p, "sha256": sha(p)} for p in INPUTS],
            "summary": summary, "coverageDefinitions": decisions["coverageDefinitions"],
            "cases": cases, "contracts": list(selected_contracts.values()),
            "packages": list(packages.values()), "supplementalReuse": reuse, "crosswalk": crosswalk,
            "limits": decisions["limits"]}


def markdown(audit):
    lines = ["# Criterion evidence matrix", "", "Executed first-pass author audit; independent acceptance pending.", "",
             "Coverage describes the named existing evidence, not model success or gold readiness.", "",
             "| Case / criterion | Coverage | Finding | Next action |", "| --- | --- | --- | --- |"]
    for case in audit["cases"]:
        for c in case["criteria"]:
            cells = [c["id"], c["coverage"], c["finding"], c["nextAction"]]
            lines.append("| " + " | ".join(x.replace("|", "\\|").replace("\n", " ") for x in cells) + " |")
    lines.extend(["", "Exact assertion sources, source/receipt hashes, environment records and negative witnesses are in [audit.json](audit.json).", ""])
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--write", action="store_true")
    mode.add_argument("--check", action="store_true")
    args = parser.parse_args()
    result = build()
    outputs = {"audit.json": json.dumps(result, indent=2, ensure_ascii=False) + "\n",
               "MATRIX.md": markdown(result)}
    for name, content in outputs.items():
        if args.write:
            (HERE / name).write_text(content)
        elif (HERE / name).read_text() != content:
            raise ValueError("Derived output differs: " + name)
    print(json.dumps(result["summary"], indent=2))


if __name__ == "__main__":
    main()

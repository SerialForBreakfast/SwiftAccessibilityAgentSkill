"""Portable reconciliation of published evidence; no subject/native execution.

--write materializes additive reports here; --check compares them without writes.
Semantic review proposals live separately in review-spec.json. No grades are
reconstructed from case-level summaries or from unavailable original answers.
"""
import argparse
from collections import Counter
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import subprocess
import sys

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
AUDIT = "research/evaluation/gold-parity-v1/audit-v1/audit.json"
MAC = "research/evaluation/gold-parity-v1/mac-evidence-20261107/"
PACKAGE = "research/evaluation/dev7-comparison/"
RESULTS = "research/evaluation/dev7-flash-haiku-results-20261107/"
SPEC = "research/evaluation/portable-followup-20261107/review-spec.json"
INPUTS = [AUDIT, MAC + "index.json", MAC + "artifact-manifest.json",
          MAC + "portable-reconciliation.json", PACKAGE + "seal.json",
          PACKAGE + "controller/scoring.json", PACKAGE + "jobs.json",
          RESULTS + "summary.json", RESULTS + "README.md", SPEC,
          "research/evaluation/gold-parity-v1/audit-v1/audit.py",
          "research/evaluation/gemini-preflight-v1/RETROSPECTIVE-TRANSPORT.md",
          "research/evaluation/failure-driven/checkout-review-20261106/unit-results.json",
          "research/evaluation/failure-driven/checkout-review-20261106/ADJUDICATION.md",
          "evals/os26/reports/2026-11-05-gold-closeout/readiness.json",
          "research/evaluation/portable-followup-20261107/reconcile.py",
          "research/evaluation/portable-followup-20261107/test_reconcile.py"]


def path(name):
    p = (ROOT / name).resolve()
    if not p.is_relative_to(ROOT):
        raise ValueError("Outside-project evidence path")
    return p


def sha(name):
    return hashlib.sha256(path(name).read_bytes()).hexdigest()


def read(name):
    return json.loads(path(name).read_text())


def pin(name, expected):
    if sha(name) != expected:
        raise ValueError("Changed evidence: " + name)


def keyed(rows, key):
    result = {r[key]: r for r in rows}
    if len(result) != len(rows):
        raise ValueError("Duplicate identity: " + key)
    return result


def transition(left, right):
    allowed = {"meets", "material-gap", "not-assessable"}
    if left not in allowed or right not in allowed:
        raise ValueError("Unknown published grade")
    if "not-assessable" in (left, right):
        return "inconclusive"
    return {("meets", "meets"): "preserved success",
            ("material-gap", "material-gap"): "persistent gap",
            ("material-gap", "meets"): "gain",
            ("meets", "material-gap"): "regression"}[left, right]


def provider_accounting(provider, rows, declared, case_ids):
    selected = [r for r in rows if r["provider"] == provider]
    keyed(selected, "case")
    if not {r["case"] for r in selected} <= case_ids:
        raise ValueError("Unknown case in provider cohort")
    for row in selected:
        if transition(row["dev5"], row["dev7"]) != row["transition"]:
            raise ValueError("Incorrect pair transition")
    transitions = dict(Counter(r["transition"] for r in selected))
    if transitions != declared["paired_outcomes"]:
        raise ValueError("Provider transition accounting mismatch")
    for arm in ("dev5", "dev7"):
        if len(selected) != declared["arms"][arm]["completed"]:
            raise ValueError("Provider completion mismatch")
        if dict(Counter(r[arm] for r in selected)) != declared["arms"][arm]["source_grades"]:
            raise ValueError("Provider grade-count mismatch")
    used = len(selected) * 2
    closed = declared["execution"]["closed"]
    if declared["execution"]["completed"] != used or closed["used"] != used:
        raise ValueError("Reservation accounting mismatch")
    if used + closed["remaining_cancelled"] != 48:
        raise ValueError("Unclosed reservation scope")
    return {"pairs": len(selected), "answers": used, "unattemptedPairs": len(case_ids) - len(selected),
            "transitions": transitions, "completedArms": declared["arms"],
            "remainingReservationsCancelled": closed["remaining_cancelled"],
            "inferenceLimit": "One published source review per answer; no provider ranking or native outcome inferred."}


def normalized_environment(env):
    # Mac's display capture escapes newlines in these two text fields only.
    return {k: v.replace("\\n", "\n") if k in ("xcode", "compiler") and isinstance(v, str) else v
            for k, v in env.items()}


def mac_verification(audit):
    data = read(MAC + "index.json")
    for p in read(MAC + "artifact-manifest.json")["artifacts"]:
        pin(MAC + p["path"], p["sha256"])
    for p in data["inputs"]:
        pin(p["path"], p["sha256"])
    module_path = "research/evaluation/gold-parity-v1/audit-v1/audit.py"
    pin(module_path, next(p["sha256"] for p in audit["inputPins"] if p["path"] == module_path))
    spec = importlib.util.spec_from_file_location("existing_audit", path(module_path))
    old = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(old)
    checked, sources = [], set()
    for package in data["packages"]:
        pin(package["path"], package["manifestSha256"])
        manifest = read(package["path"])
        for source in package["sourcePins"]:
            pin(source["path"], source["expectedSha256"])
            sources.add(source["path"])
        for check in package["checks"]:
            assert not check["invalidMatchingReceipts"]
            receipts = check["validMatchingReceipts"]
            assert receipts, (package["path"], check["id"])
            for receipt in receipts:
                pin(receipt["index"], receipt["indexSha256"])
                index = read(receipt["index"])
                raw = [r for r in old.receipt_rows(index) if old.result_hash(r) == receipt["originalResultHash"]]
                assert len(raw) == 1
                verified = old.check_receipt(raw[0], manifest, package["manifestSha256"], index)
                assert verified and not verified["issues"]
                assert verified["check"] == check["id"]
                assert verified["executedTestIds"] == sorted(receipt["execution"]["executedTestIds"])
                assert verified["failedTestIds"] == sorted(receipt["execution"]["failedTestIds"])
                assert normalized_environment(verified["environment"]) == normalized_environment(receipt["environment"])
                checked.append({"manifest": package["path"], "check": check["id"],
                                "index": receipt["index"], "originalResultHash": receipt["originalResultHash"],
                                "lane": check["lane"], "expected": check["expected"]})
    by_case = keyed(data["cases"], "id")
    refs = {}
    for case in by_case.values():
        pin(case["subject"]["path"], case["subject"]["sha256"])
        for criterion in case["criteria"]:
            for ref in criterion["references"]:
                assert ref["positiveReceiptPresent"] and ref["testDeclarationLocated"]
                refs[ref["reference"]] = ref
    for contract in audit["contracts"]:
        ref = refs[contract["id"]]
        pin(contract["file"]["path"], contract["file"]["sha256"])
        assert any(s["path"] == contract["file"]["path"] and s["sha256"] == contract["file"]["sha256"]
                   for s in ref["testSources"])
        package_name, test_id = contract["id"].split("#")
        assert any(r["manifest"] == package_name and r["originalResultHash"] == contract["receiptOriginalHash"]
                   and r["check"] in ref["positiveCheckIds"] for r in checked)
    assert len(refs) == len(audit["contracts"]) == 73
    assert len(checked) == 104 and len(data["packages"]) == 17 and len(sources) == 146
    portable_packages = {p["manifest"]["path"] for p in audit["packages"]}
    extras = [p["path"] for p in data["packages"] if p["path"] not in portable_packages]
    assert set(extras) == {"code-examples/pilots/uikit-containers-v1/manifest.json", "code-examples/pilots/uikit-reuse-v1/manifest.json"}
    assert sum(r["manifest"] in portable_packages for r in checked) == 94
    accepted = data["workerAcceptance"]
    historical = subprocess.check_output(["git", "show", accepted["checkoutCommit"] + ":" + accepted["instructionPath"]], cwd=ROOT)
    assert hashlib.sha256(historical).hexdigest() == accepted["instructionSha256"]
    return {"status": "GPAR-02-public-source-and-receipt-reconciliation-executed",
            "workerReportedAcceptance": accepted["accepted"], "packages": 17, "sourceArtifactsVerified": 146,
            "receiptChecksVerified": 104, "sharedMethodsVerified": 73, "exactControllerReceiptChecks": 94,
            "additionalDiscoveryChecks": 10, "additionalDiscoveryPackages": extras,
            "receipts": checked, "rawPrivateArchivesAuthenticated": False,
            "environmentTransformation": "Normalize literal backslash-n to newline in xcode/compiler display strings only.",
            "limits": "Public hash/selection agreement only; no new semantic acceptance, SDK freshness, native execution or gold promotion."}, by_case


def build():
    audit, rubric, results, spec = read(AUDIT), read(PACKAGE + "controller/scoring.json"), read(RESULTS + "summary.json"), read(SPEC)
    cases = keyed(rubric, "case")
    audit_cases = keyed(audit["cases"], "id")
    assert set(cases) == set(audit_cases) and len(cases) == 24
    seal = read(PACKAGE + "seal.json")
    pin(PACKAGE + "seal.json", results["seal_sha256"])
    for name, expected in seal["inputs"].items():
        pin(name, expected)
    for name, expected in seal["files"].items():
        pin(PACKAGE + name, expected)
    mac, mac_cases = mac_verification(audit)
    all_criteria = {k["id"] for r in rubric for k in r["criteria"]}
    assert len(all_criteria) == 78
    for proposal in spec["proposals"]:
        assert set(proposal["criteria"]) <= all_criteria and proposal["status"] == "draft-not-applied"
    cohorts = {p: provider_accounting(p, results["pair_rows"], results["outcomes"][p], set(cases)) for p in results["models"]}
    assert cohorts["gemini"]["pairs"] == 24 and cohorts["claude"]["pairs"] == 7
    absent = set(cases) - {r["case"] for r in results["pair_rows"] if r["provider"] == "claude"}
    assert set(results["unattempted_haiku_subjects"]) == {f"subjects/{c}/{arm}.json" for c in absent for arm in ("dev5", "dev7")}
    report_text = path(RESULTS + "README.md").read_text()
    model_keys = {v: k for k, v in results["models"].items()}
    flags = []
    for i, line in enumerate(report_text.splitlines(), 1):
        m = re.fullmatch(r"- ([^,]+), (dev[57]), ([a-z0-9-]+) — (.+)", line)
        if m:
            model, arm, case, reason = m.groups()
            assert model in model_keys and case in cases
            flags.append({"provider": model_keys[model], "modelAlias": model, "arm": arm, "case": case,
                          "publishedReason": reason, "source": RESULTS + "README.md", "line": i,
                          "originalAnswerSpan": None, "evidenceLevel": "Published reviewer finding; original source span unavailable here."})
    assert len(flags) == 10
    for provider in cohorts:
        for arm in ("dev5", "dev7"):
            assert len({f["case"] for f in flags if f["provider"] == provider and f["arm"] == arm}) == results["outcomes"][provider]["arms"][arm]["critical_answers"]
    case_rows, criterion_rows = [], []
    for cid, row in cases.items():
        jobs = [j for j in read(PACKAGE + "jobs.json") if j["case"] == cid]
        assert len(jobs) == 2 and len({j["requestSha256"] for j in jobs}) == 1
        for j in jobs:
            body = read(PACKAGE + j["path"])
            assert hashlib.sha256(json.loads(body["messages"][1]["content"])["request"].encode()).hexdigest() == j["requestSha256"]
        outcomes = [r for r in results["pair_rows"] if r["case"] == cid]
        critical = [f for f in flags if f["case"] == cid]
        regressions = [r["provider"] for r in outcomes if r["transition"] == "regression"]
        priority = "P0" if regressions or any(f["arm"] == "dev7" for f in critical) else (
            "P1" if any(r["dev7"] != "meets" for r in outcomes) else "preservation-control")
        case_rows.append({"case": cid, "family": row["family"], "priority": priority,
                          "questionChangedFromHistoricalV2": bool(row["questionChange"]), "pairedQuestionSha256": jobs[0]["requestSha256"],
                          "publishedOutcomes": outcomes, "publishedCriticalFindings": critical,
                          "guidanceAlreadySupplied": row["candidateGuidance"],
                          "caseLevelRegressionProviders": regressions,
                          "criterionGradeAvailability": "Unavailable: published summary gives whole-task outcomes only; grades not reconstructed.",
                          "missingProviderCases": [p for p in results["models"] if not any(r["provider"] == p for r in outcomes)]})
        previous = keyed(audit_cases[cid]["criteria"], "id")
        mac_criteria = keyed(mac_cases[cid]["criteria"], "id")
        for k in row["criteria"]:
            assert k["evidenceClass"] == previous[k["id"]]["coverage"]
            assert set(k["contracts"]) == {r["reference"] for r in mac_criteria[k["id"]]["references"]}
            criterion_rows.append({"id": k["id"], "case": cid, "family": row["family"],
                "evidenceClass": k["evidenceClass"], "meets": k["meets"],
                "macReferencesVerified": len(k["contracts"]), "nativeEvidenceScope": k["scope"],
                "criterionVerdicts": None, "criterionVerdictStatus": "Original grading records not in published packet; whole-case results do not establish this grade.",
                "portableNextAction": previous[k["id"]]["nextAction"],
                "reviewProposals": [p["id"] for p in spec["proposals"] if k["id"] in p["criteria"]]})
    assert sum(r["questionChangedFromHistoricalV2"] for r in case_rows) == 3
    calibration = read("research/evaluation/failure-driven/checkout-review-20261106/unit-results.json")["execution"]
    assert calibration["failedTestIds"] == ["CheckoutAnswerTests/testR16PreservesButtonTypography"]
    assert "CheckoutAnswerTests/testR13PreservesButtonTypography" in calibration["executedTestIds"]
    return {"schema": "portable-followup-reconciliation-v1", "status": "executed-author-reconciliation; semantic proposals not independently accepted",
            "visibility": "controller-only", "inputPins": [{"path": p, "sha256": sha(p)} for p in INPUTS],
            "summary": {"cases": 24, "criteria": 78, "families": 12, "publishedPairs": 31, "publishedAnswers": 62,
                        "publishedCriticalFindings": 10, "currentCandidateCriticalFindings": sum(f["arm"] == "dev7" for f in flags),
                        "coverage": dict(Counter(k["evidenceClass"] for k in criterion_rows)),
                        "newGoldQualifications": 0, "newEvaluationCalls": 0, "newNativeRuns": 0},
            "macReconciliation": mac, "providerCohorts": cohorts, "cases": case_rows, "criteria": criterion_rows,
            "reviewProposals": spec["proposals"],
            "artifactRequests": [{"name": k, "expectedSha256": v, "availability": "Not in published result packet"} for k, v in results["grade_hashes"].items()],
            "calibrationReuse": spec["calibrationReuse"], "limits": spec["limits"]}


def markdown(data):
    lines = ["# Current case and criterion reconciliation", "", "Author reconciliation; no retrospective regrading.", "",
             "## Case outcomes", "", "| Case | Priority | Flash dev.5 → dev.7 | Haiku dev.5 → dev.7 |", "| --- | --- | --- | --- |"]
    for c in data["cases"]:
        fields = []
        for provider in ("gemini", "claude"):
            r = next((r for r in c["publishedOutcomes"] if r["provider"] == provider), None)
            fields.append(f'{r["dev5"]} → {r["dev7"]}' if r else "unattempted")
        lines.append("| " + " | ".join([c["case"], c["priority"], *fields]) + " |")
    lines.extend(["", "## All criteria", "", "Whole-task outcomes are available; individual verdicts remain unavailable, not inferred.", "",
                  "| Criterion | Evidence | Mac references | Draft review proposals |", "| --- | --- | ---: | --- |"])
    for c in data["criteria"]:
        lines.append(f'| {c["id"]} | {c["evidenceClass"]} | {c["macReferencesVerified"]} | {", ".join(c["reviewProposals"]) or "retain current contract"} |')
    return "\n".join(lines) + "\n"


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--write", action="store_true")
    mode.add_argument("--check", action="store_true")
    args = parser.parse_args()
    data = build()
    for name, content in {"reconciliation.json": json.dumps(data, indent=2, ensure_ascii=False) + "\n", "MATRIX.md": markdown(data)}.items():
        if args.write:
            (HERE / name).write_text(content)
        elif (HERE / name).read_text() != content:
            raise ValueError("Derived output differs: " + name)
    print(json.dumps({**data["summary"], "macPackages": data["macReconciliation"]["packages"],
                      "macReceiptChecks": data["macReconciliation"]["receiptChecksVerified"]}, indent=2))

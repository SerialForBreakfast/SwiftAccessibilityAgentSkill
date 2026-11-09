"""Controller-only native evidence overlay. Does not assign whole-answer grades."""
import argparse
import hashlib
import json
from collections import Counter
from pathlib import Path
from probes.verify import verified

HERE = Path(__file__).resolve().parent
V3 = HERE.parents[1] / "research/evaluation/signal-panel-v3"
REPLAY = V3 / "persistent-replay/evidence.json"
REPLAY_SHA = "7f7aafe2e999fa3914166988f3e9f52c7ed1b61b3781f79c4e3a5d0e02823c9f"
NATIVE = V3 / "evidence.json"
NATIVE_SHA = "6364fae50df4da5c53ebaee3de1088c564c49149367a25de31038177b3fd62e0"


def pinned(path, expected):
    data = path.read_bytes()
    if hashlib.sha256(data).hexdigest() != expected:
        raise ValueError(f"Changed calibration input: {path.name}")
    return json.loads(data)


def grade(contract, proof):
    behavior = {
        "unit-pass": "supported", "unit-failure": "contradicted",
        "subject-compile-failure": "does-not-build", "compile-only": "unmeasured",
        "no-bound-assertion": "unmeasured", "source-only": "unmeasured",
        "oracle-interface-gap": "unmeasured", "harness-error": "unmeasured",
    }[contract]
    execution = {
        "unit-pass": "passed", "unit-failure": "failed",
        "test-compile-failure": "does-not-build", "missing-proof-fixture": "missing-fixture",
        "source-only": "not-executed", "no-executable-proof-submitted": "not-executed",
        "offline-build-only": "not-executed", "blocked-by-identical-subject": "blocked",
        "harness-error": "not-executed",
    }[proof]
    # Agreement on a single implementation cannot establish sensitivity to a defect.
    adequacy = "unestablished"
    if execution == "passed" and behavior == "contradicted":
        adequacy = "missed-contract-failure"
    return dict(behavior=behavior, proofExecution=execution, proofAdequacy=adequacy)


def qualify(positive, alternative, mutant, diagnostic, expected):
    """Only for the same registered probe on all three subjects in one environment."""
    return (positive == ["passed"] and alternative == ["passed"] and mutant == ["failed"]
            and bool(expected) and any(expected in line for line in diagnostic))


def calibrate():
    ledger = pinned(REPLAY, REPLAY_SHA)
    rows = ledger["rows"]
    board = {(r["id"], r["arm"]): grade(**r["effective"]) for r in rows}
    if len(board) != len(rows) or len(rows) != 80:
        raise ValueError("Incomplete or duplicate calibration cohort")
    fixtures = json.loads((HERE / "fixtures.json").read_text())
    cases = {(r["id"], r["arm"]): r for r in rows}
    annotated = set()
    for case, arm, witness, signature in fixtures["missed"]:
        key = case, arm
        if key in annotated or board[key]["proofAdequacy"] != "missed-contract-failure":
            raise ValueError(key)
        receipts = [a["contract"] for a in cases[key]["attempts"] if "contract" in a]
        if not any(signature in d for d in receipts[-1]["diagnostics"]):
            raise ValueError(f"Wrong assertion for {key}")
        board[key]["witness"] = witness
        annotated.add(key)
    if annotated != {k for k,v in board.items() if v["proofAdequacy"]=="missed-contract-failure"}:
        raise ValueError("Missing false-green fixture")
    for case, arm, behavior, execution in fixtures["contrasts"]:
        v = board[case, arm]
        if (v["behavior"], v["proofExecution"], v["proofAdequacy"]) != (behavior, execution, "unestablished"):
            raise ValueError(f"Contrast misclassified: {case}.{arm}")

    native = pinned(NATIVE, NATIVE_SHA)
    controls = []
    for platform, method, marker in fixtures["qualifiedProbes"]:
        trio = {r["variant"]:r for r in native if r["platform"]==platform and r["accepted"]}
        # All three use identical test code, runtime and compiler. Only subjects vary.
        for field in ("runtime", "sdk", "deployment", "xcode"):
            if len({r[field] for r in trio.values()}) != 1:
                raise ValueError(field)
        if len({r["inputs"]["Tests/ContractsTests/ContractTests.swift"] for r in trio.values()}) != 1:
            raise ValueError("Probe changed between variants")
        mutant = trio["mutant"]
        log = (HERE.parent/"results/signal-v3-native"/mutant["attempt"]/"native.log").read_bytes()
        if hashlib.sha256(log).hexdigest() != mutant["logSHA256"]:
            raise ValueError("Changed mutant execution log")
        diagnostics = [line for line in log.decode().splitlines()
                       if ": error: -[" in line and f" {method}]" in line]
        if not qualify(*(trio[v]["tests"][method] for v in ("positive","alternative","mutant")),
                       diagnostics, marker):
            raise ValueError(f"Unqualified probe: {method}")
        controls.append(dict(platform=platform, method=method, diagnostic=marker,
                             receiptHashes={k:v["receiptSHA256"] for k,v in trio.items()}))
    controls.extend(dict(platform=p["platform"], method=p["method"], diagnostic=p["diagnostic"],
                         receiptHashes={mode:r["receiptSHA256"] for mode,r in p["runs"].items()})
                    for p in verified())
    return dict(rows=[dict(id=k[0],arm=k[1],**v) for k,v in sorted(board.items())],
                counts=dict(Counter(v["proofAdequacy"] for v in board.values())), controllerProbes=controls)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--ledger", type=Path, help="Project a separately verified replay ledger to stdout; no grade files are modified")
    args = parser.parse_args()
    if args.ledger:
        if args.check:
            parser.error("use --check for the pinned calibration, --ledger for a new replay")
        rows = json.loads(args.ledger.read_bytes())["rows"]
        results = [dict(id=r["id"], arm=r["arm"], **grade(**r["effective"])) for r in rows]
        if len({(r["id"], r["arm"]) for r in results}) != len(results):
            raise ValueError("Duplicate replay cell")
        print(json.dumps(results, indent=2))
        raise SystemExit(0)
    report = calibrate()
    data = json.dumps(report, indent=2) + "\n"
    path = HERE / "calibration.json"
    if args.check:
        if data != path.read_text():
            raise SystemExit("Calibration report out of date")
    else:
        path.write_text(data)
    print(report["counts"], len(report["controllerProbes"]), "platform/probe controls")

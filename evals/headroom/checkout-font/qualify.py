"""Qualify the two checkout-font contracts natively (fixtures only; no model calls).

Every reference and alternative must pass, and every mutant must fail with the contract marker.
If the private rc.1 return is present, the two observed failing implementations are also run
against the supplied-setting contract (they must fail; they were already reviewed and approved).
  python3 -B evals/headroom/checkout-font/qualify.py [--record]
--record writes scorecard.json beside this file (refused if it already exists).
"""
import argparse
from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(ROOT / "evals/rc1/grader"))
from contracts import CONTRACTS, EXTRA
import grade

PRIVATE = ROOT / "evals/results/rc1-return-20261107/native-pending"
OBSERVED = {"C01": "C01-checkout-font.swift", "C02": "C02-checkout-font.swift"}  # two distinct failing answers


def observed_as_supplied(task):
    """The observed answers use the same signature as font-supplied-setting; run their exact bytes."""
    out = []
    for cell, name in OBSERVED.items():
        p = PRIVATE / name
        if p.exists():
            out.append(("observed-" + cell, p.read_bytes(), "contract-failure"))
    return out


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--record", action="store_true")
    args = parser.parse_args()
    if args.record and (HERE / "scorecard.json").exists():
        sys.exit("scorecard.json already recorded; qualify again without --record to check")
    expected = {}

    def variants(t):
        vs = [(k, t.solution(getattr(t, k)).encode(), "contract-failure" if k == "mutant" else "pass")
              for k in ("reference", "alternative", "mutant")]
        vs += [(k, t.solution(body).encode(), want) for k, body, want in EXTRA[t.id]]
        if t.id == "font-supplied-setting":
            vs += observed_as_supplied(t)
        for k, _, want in vs:
            expected[t.id, k] = want
        return [(k, src) for k, src, _ in vs]

    started = []
    devices = json.loads(subprocess.check_output(["xcrun", "simctl", "list", "devices", "available", "-j"], timeout=30))["devices"]
    ios = devices.get("com.apple.CoreSimulator.SimRuntime.iOS-26-5", [])
    if not any(d["state"] == "Booted" for d in ios):
        unit = next(d for d in ios if d["name"] == "SwiftAccessibility-OS26-Unit-iOS")
        subprocess.run(["xcrun", "simctl", "boot", unit["udid"]], check=True, timeout=120)
        subprocess.run(["xcrun", "simctl", "bootstatus", unit["udid"]], check=True, timeout=180, stdout=subprocess.DEVNULL)
        started.append(unit["udid"])
    try:
        base = ROOT / "evals/results/headroom-checkout-font"
        # Warm the simulator with the trusted rc.1 fixture so a cold first launch can't time out a contract.
        warm = grade.execute([t for t in grade.TASKS if t.id == "checkout-font"],
                             lambda t: [("reference", t.solution(t.reference).encode())], base / "warmup",
                             lambda r: "pass")
        if not warm["accepted"]:
            warm = grade.execute([t for t in grade.TASKS if t.id == "checkout-font"],
                                 lambda t: [("reference", t.solution(t.reference).encode())], base / "warmup",
                                 lambda r: "pass")
        assert warm["accepted"], "warm-up fixture failed twice; nothing qualified"
        report = grade.execute(CONTRACTS, variants, base, lambda r: expected[r["task"], r["variant"]])
    finally:
        for udid in started:
            subprocess.run(["xcrun", "simctl", "shutdown", udid], timeout=120)
    report["contractsSHA256"] = sha256((HERE / "contracts.py").read_bytes()).hexdigest()
    report["expected"] = {f"{t}/{k}": v for (t, k), v in expected.items()}
    if args.record:
        grade.write_once(HERE / "scorecard.json", report)
    print("ACCEPTED" if report["accepted"] else "NOT ACCEPTED", report["totals"])
    return 0 if report["accepted"] else 1


if __name__ == "__main__":
    sys.exit(main())

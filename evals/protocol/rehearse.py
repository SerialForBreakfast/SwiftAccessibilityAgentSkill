"""Offline dress rehearsal of the delivery path, using the preserved rc.1 returns. No model calls.

Steps, in order; it stops at the first failure:
  1. sealed packet verifies at its sealing revision        (verify_pinned.py)
  2. reservation ledger enforces the owner's budget and policy; rc.1 replayed under strict and
     fix-and-continue policies (one partial return; two labeled cohorts within the budget)
  3. strict extractor accepts all 36 recorded answers unchanged
  4. fresh native reproduction of all 36 cells in a new folder matches the recorded first results
  5. linked verifier re-derives the summary and the RESULT.md table from private evidence
  6. RESULT.md leads with the decision; rc.1 distribution and fixtures still verify
Writes a JSON report under evals/results/rc1-return-20261107/rehearsal-<UTC>/.
"""
from datetime import datetime, timezone
import json
from pathlib import Path
import subprocess
import sys

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[2]
RUN = ROOT / "evals/results/rc1-return-20261107"
PY = [sys.executable, "-B"]


def step(name, cmd, report, timeout=900):
    p = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True, timeout=timeout)
    tail = (p.stdout + p.stderr).strip().splitlines()[-3:]
    report["steps"].append(dict(step=name, ok=p.returncode == 0, tail=tail))
    print(("PASS " if p.returncode == 0 else "FAIL ") + name + ": " + (tail[-1] if tail else ""), flush=True)
    if p.returncode:
        raise SystemExit(1)


def main():
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    out = RUN / f"rehearsal-{stamp}"
    report = dict(startUTC=stamp, steps=[])
    try:
        step("sealed packet at sealing revision", PY + ["evals/rc1-comparison/verify_pinned.py"], report)
        step("reservation ledger and rc.1 replay", PY + ["evals/protocol/test_ledger.py"], report)
        step("strict extractor on 36 answers", PY + ["evals/protocol/test_answer_contract.py"], report)
        step("native reproduction (fresh folder)", PY + ["evals/rc1-comparison/native_lane.py", "run",
                                                       "--base", str(out / "native")], report, timeout=3600)
        recorded = {p.stem: json.loads(p.read_bytes()) for p in (RUN / "native/cells").glob("*.json")}
        fresh = {p.stem: json.loads(p.read_bytes()) for p in (out / "native/cells").glob("*.json")}
        mismatch = sorted(c for c in recorded if (recorded[c]["status"], recorded[c]["submissionSHA256"])
                          != (fresh.get(c, {}).get("status"), fresh.get(c, {}).get("submissionSHA256")))
        statuses = sorted({(r["status"]) for r in fresh.values()})
        ok = len(fresh) == 36 and not mismatch
        report["steps"].append(dict(step="reproduction matches first results", ok=ok, mismatch=mismatch,
                                    totals={s: sum(r["status"] == s for r in fresh.values()) for s in statuses}))
        print(("PASS" if ok else "FAIL") + f" reproduction matches first results: {len(fresh)} cells, mismatches {mismatch}")
        if not ok:
            raise SystemExit(1)
        step("linked verifier (private evidence)", PY + ["evals/rc1-comparison/verify_return.py"], report)
        text = (ROOT / "evals/rc1-comparison/RESULT.md").read_text()
        first = next(l for l in text.splitlines()[1:] if l.startswith("## "))
        ok = first == "## Decision" and "summary:begin" in text
        report["steps"].append(dict(step="report leads with the decision", ok=ok))
        print(("PASS" if ok else "FAIL") + " report leads with the decision")
        if not ok:
            raise SystemExit(1)
        step("rc.1 distribution and fixtures", PY + ["evals/rc1/verify.py"], report)
        report["result"] = "rehearsal passed"
    finally:
        report.setdefault("result", "rehearsal failed")
        out.mkdir(parents=True, exist_ok=True)
        (out / "report.json").write_text(json.dumps(report, indent=2) + "\n")
        print(report["result"], "->", (out / "report.json").relative_to(ROOT))


if __name__ == "__main__":
    main()

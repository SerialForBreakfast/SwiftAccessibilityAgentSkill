"""Offline ledger tests, including replays of the actual rc.1 dispatch history under two policies.

Uses only public files: the sealed packet.json and the sanitized summary.json.
Scratch ledgers go under ignored evals/results/protocol-tests/.
"""
from hashlib import sha256
import json
from pathlib import Path
import shutil
import sys
import unittest

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
from ledger import Ledger, Refused

ROOT = Path(__file__).resolve().parents[2]
PACKET = ROOT / "evals/rc1-comparison/packet.json"
SUMMARY = ROOT / "evals/rc1-comparison/summary.json"
SCRATCH = ROOT / "evals/results/protocol-tests"
CONTINUE = {"onInterruption": "continue", "promptRevisions": "new-cohort"}


def authorization(policy=None, budget=None):
    packet = json.loads(PACKET.read_bytes())
    auth = dict(job=packet["job"], packetSHA256=sha256(PACKET.read_bytes()).hexdigest(),
                maxAttempts=budget or packet["maxFirstSessions"],
                cells={c["cell"]: c["promptSHA256"] for c in packet["cells"]})
    if policy:
        auth["policy"] = policy
    return auth


class Base(unittest.TestCase):
    policy, budget = None, None

    def setUp(self):
        self.dir = SCRATCH / self.id().split(".")[-1]
        shutil.rmtree(self.dir, ignore_errors=True)
        self.auth = authorization(self.policy, self.budget)
        self.ledger = Ledger(self.dir / "ledger.jsonl", self.auth)

    def ok(self, cell):
        return self.ledger.reserve(cell, self.auth["cells"][cell], self.auth["packetSHA256"])

    def replay(self, rewrite_reason=None):
        """Feed the real rc.1 history: sealed job, then the rewritten all-36 rerun."""
        s = json.loads(SUMMARY.read_bytes())
        launched = {"sealed": 0, "chat-rewrite": 0}
        for row in s["sealed"]:
            if row["state"] == "unattempted":
                continue
            self.ok(row["cell"])
            launched["sealed"] += 1
            stop = "harness-rejected" if row["state"] == "attempt-error" else None
            self.ledger.record(row["cell"], row["state"], stop_reason=stop)
        prompts = {r["cell"]: "rewritten:" + r["cell"] for r in s["diagnostic"]}
        try:
            self.ledger.revise("chat-rewrite", s["derivedPacketSHA256"], prompts, rewrite_reason)
        except Refused:
            pass
        for i, row in enumerate(s["diagnostic"]):
            try:
                self.ledger.reserve(row["cell"], prompts[row["cell"]], s["derivedPacketSHA256"], "chat-rewrite")
            except Refused:
                continue
            launched["chat-rewrite"] += 1
            stop = "quota-read-failed" if launched["chat-rewrite"] == 9 else None  # the observed v2 interruption
            self.ledger.record(row["cell"], "completed", "chat-rewrite", stop_reason=stop)
        return launched, self.ledger.summary()


class AlwaysEnforced(Base):
    policy = CONTINUE

    def test_retry_in_same_cohort_refused(self):
        self.ok("C01")
        with self.assertRaisesRegex(Refused, "no retries"):
            self.ok("C01")

    def test_unregistered_derived_packet_refused(self):
        with self.assertRaisesRegex(Refused, "not registered"):
            self.ledger.reserve("C01", "x", "f" * 64, "rewrite")

    def test_changed_prompt_needs_registration(self):
        with self.assertRaisesRegex(Refused, "prompt differs"):
            self.ledger.reserve("C01", "0" * 64, self.auth["packetSHA256"])

    def test_revision_needs_a_reason(self):
        with self.assertRaisesRegex(Refused, "invalid revision"):
            self.ledger.revise("r2", "f" * 64, {"C01": "x"}, "")

    def test_quota_exhaustion_always_ends(self):
        self.ok("C01")
        self.ledger.record("C01", "completed", stop_reason="quota-exhausted")
        with self.assertRaisesRegex(Refused, "job ended"):
            self.ok("C02")

    def test_budget_is_the_owners_number(self):
        for cell in self.auth["cells"]:
            self.ok(cell)
        self.ledger.revise("r2", "f" * 64, {"C01": "x"}, "fix delivery")
        with self.assertRaisesRegex(Refused, "budget reached"):
            self.ledger.reserve("C01", "x", "f" * 64, "r2")

    def test_other_authorization_cannot_reuse_ledger(self):
        with self.assertRaisesRegex(Refused, "different authorization"):
            Ledger(self.dir / "ledger.jsonl", dict(self.auth, job="another-job"))


class StrictPolicy(Base):
    """Default when an authorization states no policy (as the rc.1 packet did)."""

    def test_interruption_ends_the_job_even_after_restart(self):
        self.ok("C01")
        self.ledger.record("C01", "attempt-error", stop_reason="harness-rejected")
        reopened = Ledger(self.dir / "ledger.jsonl", self.auth)
        with self.assertRaisesRegex(Refused, "job ended"):
            reopened.reserve("C02", self.auth["cells"]["C02"], self.auth["packetSHA256"])

    def test_revision_refused(self):
        with self.assertRaisesRegex(Refused, "policy refuses"):
            self.ledger.revise("r2", "f" * 64, {"C01": "x"}, "fix delivery")

    def test_rc1_history_yields_one_partial_return(self):
        launched, s = self.replay(rewrite_reason="write refused in read-only session")
        self.assertEqual(launched, {"sealed": 10, "chat-rewrite": 0})
        self.assertEqual((s["state"], s["attempted"], s["ended"]), ("partial", 10, "harness-rejected"))
        self.assertEqual(s["cohorts"]["sealed"], dict(attempted=10, outcomes={"completed": 9, "attempt-error": 1},
                                                      unattempted=26))


class FixAndContinueWithinBudget(Base):
    """Owner allows a delivery fix and continuation, same 36-session budget."""
    policy = CONTINUE

    def test_rc1_history_two_labeled_cohorts_capped_by_budget(self):
        launched, s = self.replay(rewrite_reason="write refused in read-only session; chat answer contract")
        self.assertEqual(launched, {"sealed": 10, "chat-rewrite": 26})
        self.assertEqual(s["attempted"], 36)
        self.assertEqual(s["interruptions"], ["harness-rejected", "quota-read-failed"])
        self.assertEqual(s["cohorts"]["chat-rewrite"]["unattempted"], 10)
        self.assertEqual(s["refusals"]["budget reached"], 10)
        self.assertIsNone(s["ended"])


class FixAndContinueLargerBudget(Base):
    """With a 46-session budget, the observed history would have been fully authorized."""
    policy, budget = CONTINUE, 46

    def test_rc1_history_fits(self):
        launched, s = self.replay(rewrite_reason="write refused in read-only session; chat answer contract")
        self.assertEqual(launched, {"sealed": 10, "chat-rewrite": 36})
        self.assertEqual((s["attempted"], dict(s["refusals"])), (46, {}))


if __name__ == "__main__":
    unittest.main()

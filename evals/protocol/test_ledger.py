"""Offline ledger tests, including a replay of the actual rc.1 dispatch history.

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


def authorization():
    packet = json.loads(PACKET.read_bytes())
    return dict(job=packet["job"], packetSHA256=sha256(PACKET.read_bytes()).hexdigest(),
                maxAttempts=packet["maxFirstSessions"], cells={c["cell"]: c["promptSHA256"] for c in packet["cells"]})


class Base(unittest.TestCase):
    def setUp(self):
        self.dir = SCRATCH / self.id().split(".")[-1]
        shutil.rmtree(self.dir, ignore_errors=True)
        self.auth = authorization()
        self.ledger = Ledger(self.dir / "ledger.jsonl", self.auth)

    def ok(self, cell):
        return self.ledger.reserve(cell, self.auth["cells"][cell], self.auth["packetSHA256"])


class Rules(Base):
    def test_changed_prompt_refused(self):
        with self.assertRaisesRegex(Refused, "prompt differs"):
            self.ledger.reserve("C01", "0" * 64, self.auth["packetSHA256"])

    def test_derived_packet_refused(self):
        with self.assertRaisesRegex(Refused, "derived packet"):
            self.ledger.reserve("C01", self.auth["cells"]["C01"], "f" * 64)

    def test_retry_refused(self):
        self.ok("C01")
        with self.assertRaisesRegex(Refused, "no retries"):
            self.ok("C01")

    def test_thirty_seventh_refused(self):
        for cell in self.auth["cells"]:
            self.ok(cell)
        with self.assertRaisesRegex(Refused, "not authorized|attempt limit"):
            self.ledger.reserve("C37", "0" * 64, self.auth["packetSHA256"])
        self.assertEqual(self.ledger.summary()["state"], "complete")

    def test_continuation_after_quota_failure_refused(self):
        self.ok("C01")
        self.ledger.record("C01", "completed", stop_reason="quota-read-failed")
        with self.assertRaisesRegex(Refused, "job stopped"):
            self.ok("C02")

    def test_restart_cannot_reopen(self):
        self.ok("C01")
        self.ledger.record("C01", "attempt-error", stop_reason="harness-rejected")
        reopened = Ledger(self.dir / "ledger.jsonl", self.auth)  # a worker restart reads the same ledger
        with self.assertRaisesRegex(Refused, "job stopped"):
            reopened.reserve("C02", self.auth["cells"]["C02"], self.auth["packetSHA256"])

    def test_other_authorization_cannot_reuse_ledger(self):
        with self.assertRaisesRegex(Refused, "different authorization"):
            Ledger(self.dir / "ledger.jsonl", dict(self.auth, job="rc1-release-native-chat-36-v2"))


class Replay(Base):
    def test_rc1_history_yields_one_partial_return_and_no_later_launches(self):
        s = json.loads(SUMMARY.read_bytes())
        launches = 0
        # Sealed job: C01..C09 completed, then C10's Write was rejected by the harness.
        for row in s["sealed"]:
            if row["state"] == "unattempted":
                continue
            self.ok(row["cell"])
            launches += 1
            stop = "harness-rejected" if row["state"] == "attempt-error" else None
            self.ledger.record(row["cell"], row["state"], stop_reason=stop)
        # Second job: rewritten prompts under a derived packet, all 36 cells, then a "continuation".
        for row in s["diagnostic"]:
            self.assertFalse(row["promptMatchesSeal"])
            with self.assertRaises(Refused):
                self.ledger.reserve(row["cell"], "rewritten:" + row["cell"], s["derivedPacketSHA256"])
        summary = self.ledger.summary()
        self.assertEqual(launches, 10)
        self.assertEqual(summary, dict(job="rc1-release-native-36-v1", state="partial", attempted=10,
                                       outcomes={"completed": 9, "attempt-error": 1}, unattempted=26,
                                       refusals=36, stop="harness-rejected"))


if __name__ == "__main__":
    unittest.main()

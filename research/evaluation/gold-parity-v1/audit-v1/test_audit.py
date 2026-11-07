"""Synthetic evidence-parser checks; no native execution or fixture mutations."""
from copy import deepcopy
import unittest

from audit import check_receipt, pinned


class ReceiptSafetyTests(unittest.TestCase):
    def setUp(self):
        self.manifest = {"checks": [
            {"id": "positive", "lane": "unit", "expected": "success",
             "testIds": ["Suite/testCurrent"], "failureIds": []},
            {"id": "mutant", "lane": "unit", "expected": "failure",
             "testIds": ["Suite/testCurrent"], "failureIds": ["Suite/testCurrent"]}]}
        self.row = {"check": "positive", "manifestHash": "frozen", "status": "passed",
                    "observed": "success", "environment": {"runtimeVersion": "recorded"},
                    "execution": {"executedTestIds": ["Suite/testCurrent"], "failedTestIds": [],
                                  "exitCode": 0, "build": "passed", "infrastructureError": None,
                                  "signal": None, "skippedTests": 0}}

    def inspect(self, row=None):
        return check_receipt(row or self.row, self.manifest, "frozen", {})

    def negative(self):
        r = deepcopy(self.row)
        r.update(check="mutant", observed="failure")
        r["execution"].update(failedTestIds=["Suite/testCurrent"], exitCode=65)
        return r

    def test_positive_exact_selection(self):
        self.assertEqual(self.inspect()["issues"], [])

    def test_zero_tests_never_prove_positive(self):
        self.row["execution"]["executedTestIds"] = []
        self.assertIn("empty-unit-selection", self.inspect()["issues"])

    def test_wrong_test_selection(self):
        self.row["execution"]["executedTestIds"] = ["Suite/testUnrelated"]
        self.assertIn("selected-test-set-mismatch", self.inspect()["issues"])

    def test_skipped_positive_is_not_clean(self):
        self.row["execution"]["skippedTests"] = 1
        self.assertIn("signal-or-skipped-tests", self.inspect()["issues"])

    def test_other_manifest_not_reused(self):
        self.row["manifestHash"] = "old-or-different-source"
        self.assertIsNone(self.inspect())

    def test_positive_exit_failure_not_success(self):
        self.row["execution"]["exitCode"] = 65
        self.assertIn("failed-positive", self.inspect()["issues"])

    def test_intended_assertion_failure_is_valid_negative(self):
        self.assertEqual(self.inspect(self.negative())["issues"], [])

    def test_build_failure_not_mutation_kill(self):
        row = self.negative()
        row["execution"]["build"] = "failed"
        self.assertIn("build-or-infrastructure-error", self.inspect(row)["issues"])

    def test_infrastructure_failure_not_mutation_kill(self):
        row = self.negative()
        row["execution"]["infrastructureError"] = "simulator unavailable"
        self.assertIn("build-or-infrastructure-error", self.inspect(row)["issues"])

    def test_wrong_assertion_not_mutation_kill(self):
        row = self.negative()
        row["execution"]["failedTestIds"] = ["Suite/testUnrelated"]
        self.assertIn("wrong-or-missing-intended-assertion-failure", self.inspect(row)["issues"])

    def test_successful_exit_does_not_attest_negative(self):
        row = self.negative()
        row["execution"]["exitCode"] = 0
        self.assertIn("missing-or-successful-negative-exit", self.inspect(row)["issues"])

    def test_changed_source_pin_rejected(self):
        with self.assertRaisesRegex(ValueError, "Hash mismatch"):
            pinned("research/evaluation/gold-parity-v1/audit-v1/decisions.json", "wrong")


if __name__ == "__main__":
    unittest.main()

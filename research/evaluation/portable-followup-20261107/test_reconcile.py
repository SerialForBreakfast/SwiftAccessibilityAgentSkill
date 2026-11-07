"""Synthetic cohort-accounting checks; no providers, native code or file writes."""
from copy import deepcopy
import unittest
from reconcile import keyed, path, provider_accounting, transition


class CohortSafetyTests(unittest.TestCase):
    def setUp(self):
        self.rows = [{"provider": "p", "case": "a", "dev5": "material-gap", "dev7": "meets", "transition": "gain"}]
        self.declared = {"paired_outcomes": {"gain": 1}, "arms": {
            "dev5": {"completed": 1, "source_grades": {"material-gap": 1}},
            "dev7": {"completed": 1, "source_grades": {"meets": 1}}},
            "execution": {"completed": 2, "closed": {"used": 2, "remaining_cancelled": 46}}}

    def inspect(self):
        return provider_accounting("p", self.rows, self.declared, {"a", "b"})

    def test_partial_cohort_retains_missing_pairs(self):
        self.assertEqual(self.inspect()["unattemptedPairs"], 1)

    def test_other_provider_not_pooled(self):
        self.rows.append({"provider": "q", "case": "b", "dev5": "meets", "dev7": "material-gap", "transition": "regression"})
        self.assertEqual(self.inspect()["transitions"], {"gain": 1})

    def test_missing_side_is_not_regression(self):
        self.assertEqual(transition("meets", "not-assessable"), "inconclusive")

    def test_gap_and_unassessable_is_not_persistent_gap(self):
        self.assertEqual(transition("material-gap", "not-assessable"), "inconclusive")

    def test_unattempted_not_a_grade(self):
        with self.assertRaises(ValueError):
            transition("meets", "unattempted")

    def test_duplicate_case_rejected(self):
        self.rows.append(deepcopy(self.rows[0]))
        with self.assertRaisesRegex(ValueError, "Duplicate"):
            self.inspect()

    def test_unknown_case_rejected(self):
        self.rows[0]["case"] = "unknown"
        with self.assertRaisesRegex(ValueError, "Unknown case"):
            self.inspect()

    def test_transition_mismatch_rejected(self):
        self.rows[0]["transition"] = "regression"
        with self.assertRaisesRegex(ValueError, "transition"):
            self.inspect()

    def test_grade_count_mismatch_rejected(self):
        self.declared["arms"]["dev7"]["source_grades"] = {"material-gap": 1}
        with self.assertRaisesRegex(ValueError, "grade-count"):
            self.inspect()

    def test_answer_count_mismatch_rejected(self):
        self.declared["arms"]["dev7"]["completed"] = 2
        with self.assertRaisesRegex(ValueError, "completion"):
            self.inspect()

    def test_reservation_usage_mismatch_rejected(self):
        self.declared["execution"]["closed"]["used"] = 3
        with self.assertRaisesRegex(ValueError, "Reservation"):
            self.inspect()

    def test_closed_budget_does_not_reopen_missing_work(self):
        self.declared["execution"]["closed"]["remaining_cancelled"] = 45
        with self.assertRaisesRegex(ValueError, "Unclosed"):
            self.inspect()

    def test_duplicate_criterion_identity_rejected(self):
        with self.assertRaises(ValueError):
            keyed([{"id": "x"}, {"id": "x"}], "id")

    def test_outside_project_evidence_path_rejected(self):
        with self.assertRaisesRegex(ValueError, "Outside-project"):
            path("../outside-project")


if __name__ == "__main__":
    unittest.main()

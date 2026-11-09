import unittest
from grade import calibrate, grade, qualify


class NativeCalibrationTests(unittest.TestCase):
    def test_contradiction_overrides_passing_proof(self):
        self.assertEqual(grade("unit-failure","unit-pass")["proofAdequacy"],"missed-contract-failure")

    def test_passing_test_is_not_automatically_a_good_witness(self):
        for contract in ("unit-pass","compile-only","no-bound-assertion","harness-error"):
            with self.subTest(contract=contract):
                self.assertEqual(grade(contract,"unit-pass")["proofAdequacy"],"unestablished")

    def test_broken_proof_cannot_demote_the_implementation(self):
        for proof in ("missing-proof-fixture","test-compile-failure","unit-failure","offline-build-only"):
            self.assertEqual(grade("unit-pass",proof)["behavior"],"supported")

    def test_unknown_status_is_not_credit(self):
        with self.assertRaises(KeyError):
            grade("new-status","unit-pass")

    def test_calibration_probe_must_discriminate(self):
        good,bad=["passed"],["failed"]
        self.assertTrue(qualify(good,good,bad,["target refused"],"target refused"))
        for inputs in [(bad,good,bad,["target refused"]), (good,bad,bad,["target refused"]),
                       (good,good,good,[]), (good,good,bad,["unrelated failure"]),
                       (good,good,[],["compile error"])]:
            self.assertFalse(qualify(*inputs,"target refused"))

    def test_sealed_fixtures(self):
        report=calibrate()
        self.assertEqual(report["counts"],{"unestablished":72,"missed-contract-failure":8})
        controls = {(r["platform"],r["method"]) for r in report["controllerProbes"]}
        self.assertEqual(len(controls),9)
        self.assertTrue({("iOS","testLiveEdit"),("tvOS","testLiveEdit"),
                         ("macOS","testAttachedRefusal"),("iOS","testSurvivingOrigin")} <= controls)


if __name__=="__main__":unittest.main()

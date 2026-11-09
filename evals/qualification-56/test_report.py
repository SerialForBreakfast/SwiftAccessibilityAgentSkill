import unittest
from report import outcome

class QualificationTests(unittest.TestCase):
    def test_witness_belongs_to_this_method(self):
        method='testC1234Mutant'
        log="Test Case '-[A.Probe testC1234Mutant]' failed (0.01 seconds)."
        self.assertEqual(outcome(log,method),'failed')
        self.assertEqual(outcome(log+'\np.swift:4: error: -[A.Probe testElse] : XCTAssertTrue failed - witness',method),'failed')
        self.assertEqual(outcome(log+'\np.swift:4: error: -[A.Probe testC1234Mutant] : XCTAssertTrue failed - witness',method),'caught at witness')

    def test_no_credit_for_missing_or_retried_check(self):
        method='testC1234Alternative'
        line="Test Case '-[A.Probe testC1234Alternative]' passed (0.01 seconds)."
        self.assertEqual(outcome('** TEST SUCCEEDED **',method),'no unique verdict')
        self.assertEqual(outcome(line,method),'passed')
        self.assertEqual(outcome(line+'\n'+line,method),'no unique verdict')

if __name__=='__main__':unittest.main()

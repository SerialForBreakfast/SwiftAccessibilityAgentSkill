import unittest
from report import verdict

class EvidenceRules(unittest.TestCase):
    def test_only_intended_assertion_qualifies_mutant(self):
        event = [['Checks.Unit testCurrent','failed']]
        self.assertEqual(verdict({'events':event,'errors':['Unit testCurrent] wrong value']},
                                 'testCurrent','wrong value'),'assertion failure')
        for events, errors in (([],['compiler error']), (event,['fixture unavailable']),
                               ([['Checks.Unit testCurrent','skipped']],[]),
                               (event,['another test failed: wrong value'])):
            self.assertEqual(verdict({'events':events,'errors':errors},
                                     'testCurrent','wrong value'),'not established')

    def test_one_execution_per_method(self):
        event = [['Checks.Unit testCurrent','passed']]
        self.assertEqual(verdict({'events':event,'errors':[]},'testCurrent'),'pass')
        self.assertEqual(verdict({'events':event*2,'errors':[]},'testCurrent'),'not established')

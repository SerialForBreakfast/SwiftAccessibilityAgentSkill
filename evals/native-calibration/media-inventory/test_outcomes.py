import unittest
from qualify import outcome

def log(status,errors=()):
    method='-[InventoryTests.InventoryTests testLoadAndChooseEveryNativeOption]'
    return ('\n'.join(f'Input.swift:27: error: {method} : {error}' for error in errors)+f"\nTest Case '{method}' {status}").encode()

class Outcomes(unittest.TestCase):
    def test_compile_failure_is_not_a_rejected_mutant(self):
        self.assertFalse(outcome(b'error: could not build module','language',65)['accepted'])
    def test_fixture_failure_is_not_evidence(self):
        self.assertFalse(outcome(log('failed',['fixture must expose multiple native options','real caption write']),'local-only',65)['accepted'])
    def test_outcomes_match_variant(self):
        self.assertTrue(outcome(log('passed'),'opaque',0)['accepted'])
        self.assertFalse(outcome(log('passed'),'language',0)['accepted'])
        self.assertFalse(outcome(log('failed',['real caption write']),'audio-loss',65)['accepted'])
        self.assertTrue(outcome(log('failed',['preserve audio']),'audio-loss',65)['accepted'])

if __name__=='__main__':unittest.main()

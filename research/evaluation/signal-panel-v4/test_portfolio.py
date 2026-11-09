import io, json, unittest
from collections import Counter
from zipfile import ZipFile
from build import D, ROOT, board, candidate, digest
from scoring import proof_verdict

class Portfolio(unittest.TestCase):
    def test_panel_and_controls(self):
        rows=board()
        self.assertEqual(len({r['id'] for r in rows}),56)
        self.assertEqual(Counter(r['historicalTransition'] for r in rows),
                         dict(persistent=40,rescue=9,preserved=4,inconclusive=3))
        self.assertEqual(len({(r['platform'],r['framework']) for r in rows}),6)
        self.assertEqual(sum(len(r['originalReplay']) for r in rows),80)
        self.assertTrue(all((ROOT/r['source']).is_file() for r in rows))
        for r in rows:
            for outcome in r['qualifiedProofComparison'].values():
                if outcome=='missed-qualified-mutant':
                    self.assertEqual(proof_verdict(r['verificationScope'],needs_fix=True,native=outcome),'does-not-distinguish-defect')
        self.assertEqual(sum(v=='missed-qualified-mutant' for r in rows for v in r['qualifiedProofComparison'].values()),4)

    def test_separation(self):
        with ZipFile(io.BytesIO(candidate())) as z, ZipFile(D.parent/'signal-panel-v3/rescue-replay/candidate.zip') as parent:
            self.assertEqual(set(z.namelist()),set(parent.namelist()))
            for n in z.namelist():
                self.assertNotRegex(z.read(n),rb'\b[PG]-[a-f0-9]{10,}|missed-qualified-mutant|controller.json')
                if n.endswith(('facts.md','font.md','openai.yaml')) or '/examples/' in n:
                    self.assertEqual(z.read(n),parent.read(n))
            entry='swift-accessibility-agent/SKILL.md'
            self.assertLess(len(z.read(entry)),len(parent.read(entry)))
            self.assertEqual(z.read(entry).count(b'signal-v4'),2)
    def test_no_new_requirements(self):
        self.assertEqual(proof_verdict('only-if-fix-needed',needs_fix=False),'not-required')
        self.assertEqual(proof_verdict('only-if-fix-needed'),'undetermined')
        self.assertEqual(proof_verdict('no-added-proof-requirement'),'not-required')
    def test_calibration_boundaries(self):
        self.assertEqual(proof_verdict('focused-check',path=False,observation=True),'does-not-establish-requested-effect')
        self.assertEqual(proof_verdict('focused-check',native='interface-gap'),'undetermined')
        self.assertEqual(proof_verdict('describe-check',path=True,observation=True,native='no-executable-proof'),'source-supported-check')
        self.assertEqual(proof_verdict('supply-tests',path=True,observation=True,native='no-executable-proof'),'requested-unit-check-missing')
        with self.assertRaises(ValueError): proof_verdict('focused-check',native='unit-pass')

if __name__=='__main__': unittest.main()

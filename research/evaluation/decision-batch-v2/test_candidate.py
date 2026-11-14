import hashlib
import io
import json
from pathlib import Path
import posixpath
import re
import unittest
from zipfile import ZipFile
from build import build, D, P, table

def members(data):
    with ZipFile(io.BytesIO(data)) as z:
        return {n.removeprefix('swift-accessibility-agent/'):z.read(n) for n in z.namelist()}

class Candidate(unittest.TestCase):
    def test_previous_win_witnesses_remain_available(self):
        root = D.parents[2]
        slider = json.loads((P/'controls/receipt.json').read_bytes())['checks']['slider']
        self.assertTrue(slider['compiled'])
        control = (P/'controls/slider.md').read_bytes().split(b'```swift\n')[1].split(b'\n```')[0]
        self.assertEqual(hashlib.sha256(control).hexdigest(), slider['sourceSHA256'])
        history = json.loads((root/'evals/discovery-500/callback-batch/evidence.json').read_bytes())
        for method in ('testLiveEdit', 'testPanel'):
            for variant, expected in [('working','passed'),('alternative','passed'),('defect','failed')]:
                self.assertIn(['Checks.ContractTests '+method, expected], history['iOS-'+variant]['events'])
        runs = json.loads((D.parent/'platform-expansion-v1/results-index.json').read_bytes())['attempts']
        for name, observed in [('platform-tv-original-missing-titles-r1','failure'),
                               ('platform-tv-positive-r2','success')]:
            run, = [r for r in runs if r['attempt']==name]
            self.assertEqual((run['status'],run['observed']),('passed',observed))
            self.assertIn('testVisibleActionNames',json.dumps(run['execution']))

    def test_only_declared_behavior_changes(self):
        before=members((P/'candidate.zip').read_bytes())
        after=members(build())
        self.assertEqual(build(),(D/'candidate.zip').read_bytes())
        self.assertEqual(after.keys()-before.keys(),{'fixtures/control.mov','fixtures/positive.mov'})
        self.assertFalse(before.keys()-after.keys())
        self.assertEqual({k for k in before if before[k]!=after[k]},{
            'SKILL.md','references/actions.md','references/structure.md',
            'references/text.md','references/media.md'})
        self.assertEqual(after['SKILL.md'].replace(b'decision-batch-v2',b'decision-batch-v1'),before['SKILL.md'])
        for r in table(P/'decisions.tsv'):
            key='references/'+r['route']+'.md'
            if r['family'] not in {f['family'] for f in table(D/'fixes.tsv')}:
                self.assertIn(r['guidance'].encode(),after[key])
        for path in ('SKILL.md','references/media.md'):
            for link in re.findall(rb'\]\(([^)]+)\)',after[path]):
                self.assertIn(posixpath.normpath(posixpath.join(posixpath.dirname(path),link.decode())),after)
        self.assertNotRegex(b' '.join(v for n,v in after.items() if n.endswith('.md')),rb'Q-[0-9a-f]{16}')
        self.assertEqual(hashlib.sha256((D.parents[2]/'SKILL.md').read_bytes()).hexdigest(),'2f4ce5ea5a6c8fa7c7cdd08eea620c606eedcc7ae389ac19a493d73078f7c3e3')

    def test_regression_board_complete(self):
        read=json.loads((D/'regressions.json').read_bytes())
        self.assertEqual({k for r in table(D/'fixes.tsv') for k in r['cases'].split(',')},set(read))
        self.assertEqual(len(read),8)
        self.assertTrue(all(x['whole']==['pass','fail'] for x in read.values()))

if __name__=='__main__':unittest.main()

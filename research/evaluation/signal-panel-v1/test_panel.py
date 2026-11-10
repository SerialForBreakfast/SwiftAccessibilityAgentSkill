import json
from io import BytesIO
from zipfile import ZipFile
import unittest
from build import build,D,h
from score import score,AXES

class PanelTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.files=build()
        cls.panel=json.loads(cls.files['panel.json'])
    def test_seals_and_reproduction(self):
        for name,data in self.files.items():self.assertEqual((D/name).read_bytes(),data)
        with ZipFile(BytesIO(self.files['held.zip'])) as z:
            m=json.loads(z.read('seal.json'))
            self.assertEqual(set(z.namelist()),set(m)|{'seal.json'})
            for n,v in m.items():self.assertEqual(h(z.read(n)),v)
            self.assertEqual(sum(n.startswith('subjects/') for n in m),len(self.panel))
    def test_selection(self):
        p=self.panel
        self.assertEqual(len({r['id'] for r in p}),56)
        controls=[r for r in p if r['axis']=='sentinel']
        self.assertEqual(len({(r['framework'],r['platform']) for r in controls}),6)
        self.assertTrue(all(r['frozenWhole']=='pass' and r['counterpart'] for r in controls))
    def test_missing_is_not_a_rescue(self):
        result=score(self.panel,[])
        self.assertEqual(result['planned'],112)
        self.assertFalse(result['familiesWithRescueAndNoObservedLossOrUnknown'])
        self.assertEqual(sum(x['inconclusive'] for x in result['targetAxes'].values()),56)
    def test_quality_separate_from_evidence(self):
        r=next(r for r in self.panel if r['axis']=='verification'); base=dict(id=r['id'],critical=False,**dict.fromkeys(AXES,'pass'))
        g=[dict(base,arm='unaided',verification='fail',whole='fail'),dict(base,arm='skill',critical=True)]
        res=score(self.panel,g)
        self.assertEqual(res['targetAxes']['verification']['rescue'],1)
        self.assertEqual(res['candidateCriticalFlagsRequiringReview'],[r['id']])
        with self.assertRaises(ValueError):score(self.panel,g+g)
    def test_twins(self):
        r=next(x for x in self.panel if x['axis']=='sentinel')
        pair=[r,next(x for x in self.panel if x['parent']==r['counterpart'])]
        g=[dict(id=x['id'],arm='skill',critical=False,**dict.fromkeys(AXES,'pass')) for x in pair]
        self.assertEqual(score(self.panel,g)['twins']['skill:both correct'],1)
if __name__=='__main__':unittest.main()

import hashlib
import json
import unittest
import zipfile
from collections import Counter
from score import ROOT, compare


class PacketTests(unittest.TestCase):
    def test_subject_isolation(self):
        cases = json.loads((ROOT/'controller.json').read_bytes())
        with zipfile.ZipFile(ROOT/'subjects.zip') as z:
            schedule = json.loads(z.read('schedule.json'))
            self.assertEqual(len(schedule), 500)
            self.assertEqual({r['id'] for r in schedule}, {r['id'] for r in cases})
            self.assertEqual(set(z.namelist()), {'schedule.json', *(r['path'] for r in cases)})
            for r in cases:
                self.assertEqual(hashlib.sha256(z.read(r['path'])).hexdigest(),r['promptSHA256'])
                self.assertTrue(all(r[k] for k in ('required','accepted','reject','ancestors')))
        self.assertEqual(len({r['ancestors'][0]['id'] for r in cases if r['mode']=='decision'}),50)
        self.assertTrue(all(r['ancestors'][0]['priorWhole']=='fail' for r in cases if r['mode']=='decision'))
        self.assertEqual(Counter(r['lane'] for r in json.loads((ROOT/'qualification19.json').read_bytes())),
                         {'native':9,'source-only':8,'partial-native':1,'open':1})

    def test_pair_boundaries(self):
        catalog={k:{'promptSHA256':k} for k in 'abcd'}
        def row(i,arm,grade):
            return dict(id=i,arm=arm,promptSHA256=i,modelRevision='test',transport='test',
                        settingsSHA256='x',permissionsSHA256='y',rubricSHA256='z',
                        decision=grade,whole=grade,ordinary='pass')
        rows=[row('a','unaided','fail'),row('a','skill','pass'),row('b','unaided','pass'),
              row('b','skill','fail'),row('c','unaided','fail'),row('c','skill','pass')]
        rows[-1]['modelRevision']='other'
        got=compare(rows,catalog)
        self.assertEqual(got['matchedScores']['decision'], {'rescued':1,'regressed':1})
        self.assertEqual(got['statusCounts'], {'matched':2,'incompatible':1,'unpaired':1})
        with self.assertRaises(ValueError):
            compare(rows+rows[:1],catalog)


if __name__=='__main__':
    unittest.main()

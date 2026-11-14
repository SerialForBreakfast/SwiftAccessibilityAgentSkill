import io,json,unittest
from zipfile import ZipFile
import prepare,score

class Frozen(unittest.TestCase):
    def test_packet(self):
        for k,b in prepare.build().items():self.assertEqual(b,(prepare.D/k).read_bytes())
        with ZipFile(prepare.D/'held.zip') as z:
            m=json.loads(z.read('manifest.json'))
            self.assertEqual(set(z.namelist()),set(m['files'])|{'manifest.json'})
            self.assertTrue(all(prepare.h(z.read(k))==h for k,h in m['files'].items()))
            c=json.loads(z.read('controller/criteria.json'))
            with ZipFile(io.BytesIO(z.read('subjects.zip'))) as subjects:
                self.assertEqual(set(subjects.namelist()),{f'questions/{k}.md' for k in c})
                for k,v in c.items():
                    b=subjects.read(f'questions/{k}.md')
                    self.assertEqual(prepare.h(b),v['promptSHA256'])
                    for field in ('primary','ordinary','acceptedAlternative','reject'):
                        self.assertNotIn(v[field].encode(),b)
    def test_loss_even_when_diagnosis_improves(self):
        with ZipFile(prepare.D/'held.zip') as z:
            c=json.loads(z.read('controller/criteria.json'))
        q=next(iter(c))
        rows=[dict(question=q,arm=a,promptSHA256=c[q]['promptSHA256'],primary=p,ordinary=o,whole='fail',excerpt='synthetic passage',reason='synthetic reason')
              for a,p,o in zip(score.ARMS,['fail','pass'],['pass','fail'])]
        s=score.score(rows)
        self.assertEqual(s['primary']['counts'],{'gain':1,'inconclusive':23})
        self.assertEqual(s['ordinaryLosses'][0]['question'],q)
        self.assertEqual(s['whole']['counts'],{'both fail':1,'inconclusive':23})
        with self.assertRaises(ValueError):score.score(rows+rows)
        with self.assertRaises(ValueError):score.score([dict(rows[1],whole='pass')])

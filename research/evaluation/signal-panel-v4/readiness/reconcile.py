"""Check frozen masked proof judgments, link original answers, and unmask after review."""
import csv,json,sys
from zipfile import ZipFile
from mask import OUT,D,ROOT,H
review=(D/'masked-review.tsv').read_bytes()
assert H(review)=='de5398584c5ecb1ebb5c4cf2d077512afc025c30b14bcde85babf0b0cb0d31be'
rows=list(csv.DictReader(review.decode().splitlines(),delimiter='\t'))
key=json.loads((OUT/'key.json').read_bytes())
assert set(key)=={r['mask'] for r in rows} and len(rows)==10
native={(r['id'],r['arm']):r for r in json.loads((ROOT/'evals/native-calibration/proof-sensitivity/evidence.json').read_bytes())['rows']}
joined=[]
with ZipFile(ROOT/'evals/results/signal-v2-review-20261108/signal-panel-v2-return.zip') as z:
    for r in rows:
        k=key[r['mask']]
        data=(OUT/r['mask']/'answer.txt').read_bytes()
        assert H(data)==k['maskedSHA256'] and r['decisive substring'] in data.decode()
        assert H(z.read(f'records/{k["id"]}.{k["arm"]}/answer.txt'))==k['answerSHA256']
        n=native.get((k['id'],k['arm']),{}).get('outcome','not-compared')
        joined.append(dict(**k,**r,nativeComparison=n))
out=(json.dumps(joined,indent=2)+'\n').encode()
if '--check' in sys.argv:assert (D/'calibration.json').read_bytes()==out
else:(D/'calibration.json').write_bytes(out)
print('10 frozen masked judgments verified against original answer hashes.')

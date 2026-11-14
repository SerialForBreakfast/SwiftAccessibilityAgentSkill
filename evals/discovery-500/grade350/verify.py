"""Validate the offline judgments' membership and evidence spans; never calls a model."""
import csv
import hashlib
import json
import sys
from collections import Counter
from pathlib import Path
from zipfile import ZipFile

HERE = Path(__file__).resolve().parent
def verify(bundle):
    with (HERE/'grades.csv').open() as f:
        grades = list(csv.DictReader(f))
    with (HERE.parent/'audit-1562/index.csv').open() as f:
        originals = {r['id']: r for r in csv.DictReader(f) if r['triage'] == 'not-assessed'}
    assert len(grades) == len(originals) == len({r['id'] for r in grades}) == 350
    with ZipFile(bundle) as z:
        for g in grades:
            r = originals[g['id']]
            assert all(g[k] == r[k] for k in ('mode','platform','framework','answerSHA256','promptSHA256'))
            b = z.read('raw/'+g['id']+'/answer.txt')
            start, end = int(g['answerSpanStart']), int(g['answerSpanEnd'])
            assert 0 <= start < end <= len(b)
            for data, key in ((b,'answerSHA256'),(b[start:end],'spanSHA256')):
                assert hashlib.sha256(data).hexdigest() == g[key]
            assert g['primary'] == {'source-supported':'pass','material-answer-error':'fail','prompt-gap':'unresolved','grading-gap':'unresolved'}[g['disposition']]
            assert bool(g['family']) == (g['primary']=='fail')
    print(json.dumps({k:Counter(g[k] for g in grades) for k in ('disposition','family','mode')},indent=2))
if __name__=='__main__':
    verify(sys.argv[1])

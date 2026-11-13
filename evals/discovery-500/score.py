"""Compare masked local grades after unmasking. Does not execute any provider."""
import argparse
import hashlib
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUTCOME = {('fail','pass'):'rescued', ('pass','fail'):'regressed',
           ('pass','pass'):'preserved', ('fail','fail'):'persistent'}
MATCH = ('modelRevision','transport','settingsSHA256','permissionsSHA256','rubricSHA256')


def compare(rows, catalog):
    cells = {}
    for r in rows:
        key = (r['id'],r['arm'])
        if (key in cells or key[0] not in catalog or key[1] not in ('unaided','skill')
                or r['promptSHA256'] != catalog[key[0]]['promptSHA256']):
            raise ValueError(f'Duplicate or invalid input: {key}')
        if not all(r.get(k) for k in MATCH):
            raise ValueError(f'Missing comparison metadata: {key}')
        if not all(r[k] in ('pass','fail','unresolved') for k in ('decision','whole','ordinary')):
            raise ValueError(f'Invalid grade: {key}')
        cells[key] = r
    outcomes = {}
    for i in catalog:
        a, b = (cells.get((i,arm)) for arm in ('unaided','skill'))
        if not a or not b:
            outcomes[i] = {'status':'unpaired'}
        elif any(a[k] != b[k] for k in MATCH):
            outcomes[i] = {'status':'incompatible'}
        else:
            outcomes[i] = {'status':'matched', **{
                k: OUTCOME.get((a[k], b[k]), 'unresolved') for k in ('decision','whole','ordinary')}}
    return {'statusCounts':dict(Counter(o['status'] for o in outcomes.values())),
            'matchedScores':{k:dict(Counter(o[k] for o in outcomes.values() if o['status']=='matched'))
                             for k in ('decision','whole','ordinary')},
            'cases':outcomes}


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('grades', help='Private, unmasked JSONL grade rows')
    a = p.parse_args()
    raw = (ROOT/'controller.json').read_bytes()
    assert hashlib.sha256(raw).hexdigest() == json.loads((ROOT/'freeze.json').read_text())['sha256']['controller.json']
    print(json.dumps(compare([json.loads(s) for s in Path(a.grades).read_text().splitlines()],
                             {r['id']:r for r in json.loads(raw)}), indent=2))

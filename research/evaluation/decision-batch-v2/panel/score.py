"""Offline aggregation of adjudicated source grades. Does not assign grades."""
import json
import sys
from collections import Counter
from pathlib import Path
from zipfile import ZipFile

D=Path(__file__).resolve().parent
ARMS=('decision-batch-v1','decision-batch-v2')
AXES=('primary','ordinary','whole')
def transition(old,new):
    if 'unresolved' in (old,new):return 'inconclusive'
    return {('pass','pass'):'both pass',('fail','fail'):'both fail',
            ('fail','pass'):'gain',('pass','fail'):'regression'}[old,new]
def score(rows):
    with ZipFile(D/'held.zip') as z:
        criteria=json.loads(z.read('controller/criteria.json'))
        pairs=json.loads(z.read('controller/pairs.json'))
    grades={}
    for r in rows:
        k=(r['question'],r['arm'])
        if k in grades or k[0] not in criteria or k[1] not in ARMS:raise ValueError('invalid/duplicate cell')
        if r['promptSHA256']!=criteria[k[0]]['promptSHA256']:raise ValueError('input mismatch')
        for axis in AXES:
            if r[axis] not in ('pass','fail','unresolved'):raise ValueError('invalid grade')
        if r['whole']=='pass' and any(r[a]!='pass' for a in ('primary','ordinary')):raise ValueError('whole pass without supported decision and preservation')
        if not r['reason'].strip() or not r['excerpt'].strip():raise ValueError('grade without evidence')
        grades[k]=r
    result={}
    missing=lambda q,a,axis: grades.get((q,a),{}).get(axis,'unresolved')
    for axis in AXES:
        cells={q:transition(*(missing(q,a,axis) for a in ARMS)) for q in criteria}
        def both(ids,a):
            values=[missing(q,a,axis) for q in ids]
            return 'unresolved' if 'unresolved' in values else ('pass' if values==['pass','pass'] else 'fail')
        result[axis]=dict(counts=dict(Counter(cells.values())),byQuestion=cells,
            passes={a:sum(missing(q,a,axis)=='pass' for q in criteria) for a in ARMS},
            byDecisionPair={k:{a:both(ids,a) for a in ARMS} for k,ids in pairs.items()})
    result['ordinaryLosses']=[dict(question=q,ordinaryPath=criteria[q]['ordinary'],
        evidence={a:{k:grades[q,a][k] for k in ('excerpt','reason')} for a in ARMS})
        for q,v in result['ordinary']['byQuestion'].items() if v=='regression']
    result['returnedGrades']=len(grades)
    return result
if __name__=='__main__':print(json.dumps(score(json.loads(Path(sys.argv[1]).read_bytes())),indent=2))

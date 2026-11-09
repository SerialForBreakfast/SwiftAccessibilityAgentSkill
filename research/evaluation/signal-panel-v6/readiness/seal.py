"""Deterministic held packet for signal-v6-run1: unaided, signal-v2, signal-v6; three trials."""
from pathlib import Path
import json,sys,hashlib,io
from zipfile import ZipFile,ZipInfo,ZIP_DEFLATED
D=Path(__file__).resolve().parent
V=D.parent
ROOT=D.parents[3]
H=lambda b: hashlib.sha256(b).hexdigest()
ARMS=('unaided','signal-v2','signal-v6'); TRIALS=3
def dump(obj): return (json.dumps(obj,indent=2)+'\n').encode()
def build():
    packet=(V.parent/'signal-panel-v4/readiness/held.zip').read_bytes()
    assert H(packet)=='5e73c208ef105df6a93364a7925363178dd527b3b7d5c8e7cbd5ed1c9180f103'
    with ZipFile(io.BytesIO(packet)) as z:
        files={n:z.read(n) for n in z.namelist() if n.startswith(('subjects/','controller/repository/','arms/signal-v2'))}
        v4criteria=json.loads(z.read('controller/criteria.json'))
    files['arms/signal-v6.zip']=(V/'candidate.zip').read_bytes()
    for n in ['HANDOFF.md','GRADING.md','check_return.py','RETURN.md']:
        files[n if n=='HANDOFF.md' else 'controller/'+n]=(D/n).read_bytes()
    files['controller/single-exchange.md']=(ROOT/'evals/BIGDOG-SINGLE-EXCHANGE.md').read_text().split('**Current Flash excerpt request:**')[0].encode()
    files['controller/criteria.json']=dump(v4criteria)
    board=json.loads((V.parent/'signal-panel-v4/controller.json').read_bytes())
    schedule=[]
    for t in range(TRIALS):
        for idx,r in enumerate(sorted(board,key=lambda x:x['id'])):
            i=r['id']; subject='subjects/'+i+'.txt'
            assert H(files[subject])==r['questionSHA256']
            k=(idx+t)%3; order=ARMS[k:]+ARMS[:k]
            for arm in order:
                skill=None if arm=='unaided' else H(files['arms/'+arm+'.zip'])
                schedule.append(dict(id=i,arm=arm,trial=t+1,subject=subject,questionSHA256=r['questionSHA256'],skillSHA256=skill))
    assert len(schedule)==504 and len({(x['id'],x['arm'],x['trial']) for x in schedule})==504
    files['schedule.json']=dump(schedule)
    files['SHA256.json']=dump({n:H(b) for n,b in sorted(files.items())})
    out=io.BytesIO()
    with ZipFile(out,'w') as z:
        for n,b in sorted(files.items()): z.writestr(ZipInfo(n,(2026,1,1,0,0,0)),b,compress_type=ZIP_DEFLATED)
    return out.getvalue()
if __name__=='__main__':
    b=build(); p=D/'held.zip'
    if '--check' in sys.argv: assert p.read_bytes()==b
    else:p.write_bytes(b)
    print('held.zip',H(b))

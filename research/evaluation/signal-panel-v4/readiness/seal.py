"""Deterministic held packet; checks subject bytes and excludes historical grading outcomes."""
from pathlib import Path
import json,sys,hashlib,io
from zipfile import ZipFile,ZipInfo,ZIP_DEFLATED
D=Path(__file__).resolve().parent
V=D.parent
ROOT=D.parents[3]
H=lambda b: hashlib.sha256(b).hexdigest()
def dump(obj): return (json.dumps(obj,indent=2)+'\n').encode()
def build():
    packet=(V.parent/'signal-panel-v2/held.zip').read_bytes()
    assert H(packet)=='51bf28327715ad63929a107b9c8b3e3c364669916e3f2c0107f61b6300b45acd'
    with ZipFile(io.BytesIO(packet)) as z:
        files={n:z.read(n) for n in z.namelist() if n.startswith(('subjects/','controller/repository/'))}
        files['arms/signal-v2.zip']=z.read('candidate.zip')
    files['arms/signal-v4.zip']=(V/'candidate.zip').read_bytes()
    for n in ['HANDOFF.md','GRADING.md','check_return.py','RETURN.md']:
        files[n if n=='HANDOFF.md' else 'controller/'+n]=(D/n).read_bytes()
    files['controller/single-exchange.md']=(ROOT/'evals/BIGDOG-SINGLE-EXCHANGE.md').read_text().split('**Current Flash excerpt request:**')[0].encode()
    board=json.loads((V/'controller.json').read_bytes())
    schedule=[]; criteria=[]
    for idx,r in enumerate(sorted(board,key=lambda x:x['id'])):
        i=r['id']; subject='subjects/'+i+'.txt'
        assert H(files[subject])==r['questionSHA256']
        criteria.append({k:r[k] for k in ('id','platform','framework','family','verificationScope','originalCriterion','contrast','insufficientAlone','source','assertions')})
        assert 'controller/repository/'+r['source'] in files
        for arm in (('signal-v4','signal-v2') if idx%2 else ('signal-v2','signal-v4')):
            schedule.append(dict(id=i,arm=arm,subject=subject,questionSHA256=r['questionSHA256'],skillSHA256=H(files['arms/'+arm+'.zip'])))
    assert len(schedule)==112 and len({(x['id'],x['arm']) for x in schedule})==112
    files['controller/criteria.json']=dump(criteria)
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

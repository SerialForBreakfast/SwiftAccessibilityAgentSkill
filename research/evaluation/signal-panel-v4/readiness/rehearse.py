"""Synthetic transport fixtures only. Nothing here is model evidence."""
import copy,io,json
from zipfile import ZipFile
from seal import D,H,dump
from check_return import verify
p=D/'held.zip'; seal=H(p.read_bytes())
with ZipFile(p) as z:s=json.loads(z.read('schedule.json'))
def ref(path,b):
    blobs[path]=b;return dict(path=path,sha256=H(b))
def exercise(m,success=True):
    b=io.BytesIO()
    with ZipFile(b,'w') as z:
        for k,v in blobs.items():z.writestr(k,v)
        z.writestr('return.json',dump(m))
    try:r=verify(p,seal,b)
    except (KeyError,ValueError):
        if success:raise
        return
    assert success
    return r
blobs={}; shared=ref('fixture','synthetic fixture'.encode())
m=dict(job='signal-v4-head-to-head',packetSHA256=seal,report=shared,runLedger=shared,
       gradeFreeze=shared,maskMap=shared,status='complete',cells=[])
for n,r in enumerate(s):
    c={k:r[k] for k in ('id','arm','questionSHA256','skillSHA256')}
    c.update(state='answered',attempts=1,request=shared,receipt=shared,transport=shared,usage=shared,trace=shared,
             answer=ref(f'answers/{n}',b'synthetic answer'),mask=str(n),critical=False,graderInput=shared,graderOutput=shared,
             grade={a:dict(verdict='pass',reason='fixture',excerpt='synthetic') for a in ('primary','preservation','integration','verification','rework','whole')})
    m['cells'].append(c)
assert exercise(m)['whole']=={'preserved':56}
bad=copy.deepcopy(m);bad['cells'][0]['grade']['primary']['excerpt']='not present';exercise(bad,False)
bad=copy.deepcopy(m);bad['cells'].pop();exercise(bad,False)
bad=copy.deepcopy(m);bad['cells'][0]['answer']['sha256']='0'*64;exercise(bad,False)
bad=copy.deepcopy(m);bad['cells'][0]['attempts']=2;exercise(bad,False)
blocked=[dict(id=r['id'],arm=r['arm'],reason='fixture',attempts=0,state='unattempted') for r in s]
m.update(status='partial',stopReason='fixture',cells=m['cells'][:1]+blocked[1:]);assert exercise(m)['answered']==1
m.update(status='blocked',cells=blocked);assert exercise(m)['attempted']==0
print('Accepted complete, partial and blocked; rejected wrong excerpt, missing cell, changed bytes and retry.')

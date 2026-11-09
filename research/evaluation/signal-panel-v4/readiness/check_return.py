"""Usage: python3 check_return.py held.zip expected_packet_sha256 return.zip"""
import hashlib,json,sys
from collections import Counter
from pathlib import Path,PurePosixPath
from zipfile import ZipFile
H=lambda b:hashlib.sha256(b).hexdigest()
AXES=('primary','preservation','integration','verification','rework','whole')
def need(ok,msg):
    if not ok:raise ValueError(msg)
def inventory(z):
    names=z.namelist()
    need(len(names)==len(set(names)) and all(not PurePosixPath(n).is_absolute() and '..' not in PurePosixPath(n).parts for n in names),'unsafe or duplicate members')
def verify(packet,seal,result):
    need(H(Path(packet).read_bytes())==seal,'packet seal')
    with ZipFile(packet) as p, ZipFile(result) as z:
        inventory(p);inventory(z)
        hashes=json.loads(p.read('SHA256.json'))
        need(set(hashes)==set(p.namelist())-{'SHA256.json'} and all(H(p.read(k))==v for k,v in hashes.items()),'packet contents')
        schedule=json.loads(p.read('schedule.json'))
        expected={(r['id'],r['arm']):r for r in schedule}
        m=json.loads(z.read('return.json'))
        need(m['packetSHA256']==seal and m['job']=='signal-v4-head-to-head','wrong job')
        def artifact(ref):
            b=z.read(ref['path']);need(b and H(b)==ref['sha256'],'missing or changed artifact');return b
        for k in ('report','runLedger'):artifact(m[k])
        cells={};answered=0;attempted=0;mask=set(); answerpaths=set()
        for c in m['cells']:
            key=(c['id'],c['arm']);need(key in expected and key not in cells,'invalid or duplicate cell');cells[key]=c
            state=c['state'];need(state in {'answered','error','unattempted'},'state')
            if state=='unattempted':
                need(c['reason'] and c['attempts']==0,'unattempted');continue
            attempted+=1
            need(c['attempts']==1 and c['questionSHA256']==expected[key]['questionSHA256'] and c['skillSHA256']==expected[key]['skillSHA256'],'attempt binding')
            for k in ('request','receipt','transport','usage','trace'):artifact(c[k])
            if state=='error':artifact(c['error']);continue
            answered+=1
            raw=artifact(c['answer']).decode();need(c['answer']['path'] not in answerpaths,'reused answer path');answerpaths.add(c['answer']['path'])
            if c.get('grade') is None:
                need(m['status']=='partial' and c['reason'],'missing grade');continue
            need(c['mask'] and c['mask'] not in mask,'duplicate mask');mask.add(c['mask'])
            for k in ('graderInput','graderOutput'):artifact(c[k])
            need(isinstance(c['critical'],bool) and set(c['grade'])==set(AXES),'grading dimensions')
            for a,g in c['grade'].items():
                need(g['verdict'] in {'pass','fail','unknown','na'} and g['reason'].strip(),'criterion verdict')
                if g['verdict'] in {'pass','fail'}:
                    need(bool(g['excerpt'].strip()) and g['excerpt'] in raw,'unmatched decisive excerpt')
        need(set(cells)==set(expected),'incomplete scheduled ledger')
        if mask:
            artifact(m['gradeFreeze']);artifact(m['maskMap'])
        status=m['status']
        need(status in {'complete','partial','blocked'},'return status')
        if status=='complete':need(answered==len(expected)==len(mask),'incomplete complete return')
        else:need(m['stopReason'].strip(),'missing stop reason')
        if status=='blocked':need(not answered,'usable answers require partial return')
        counts=Counter()
        for i in {k[0] for k in cells}:
            pair=[(cells[i,arm].get('grade') or {}).get('whole',{}).get('verdict') for arm in ('signal-v2','signal-v4')]
            counts[{('pass','pass'):'preserved',('fail','pass'):'rescued',('pass','fail'):'regressed',('fail','fail'):'persistent'}.get(tuple(pair),'inconclusive')]+=1
        return dict(status=status,attempted=attempted,answered=answered,graded=len(mask),whole=dict(counts))
if __name__=='__main__':print(json.dumps(verify(*sys.argv[1:]),indent=2))

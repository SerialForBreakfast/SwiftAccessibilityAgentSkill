"""Offline controller reconciliation. Read only artifacts, never run returned code."""
import hashlib,json,sys
from collections import Counter
from pathlib import Path
from zipfile import ZipFile
D=Path(__file__).resolve().parent
sys.path.insert(0,str(D.parent/'readiness'))
from check_return import verify, AXES
H=lambda b:hashlib.sha256(b).hexdigest()
p=D.parent/'readiness/held.zip'
r=D.parents[3]/'evals/results/signal-v4-review/signal-v4-return.zip'
assert H(r.read_bytes())=='f14305f1ff84de8bd03a79752e70e15e51b0fe8e5f70008b3be855a8bfb7ff09'
summary=verify(p,'5e73c208ef105df6a93364a7925363178dd527b3b7d5c8e7cbd5ed1c9180f103',r)
with ZipFile(r) as z, ZipFile(p) as pkt:
    m=json.loads(z.read('return.json'))
    def data(ref):
        b=z.read(ref['path']);assert H(b)==ref['sha256'];return b
    def load(ref):return json.loads(data(ref))
    def links(v):
        if isinstance(v,list):
            for x in v:links(x)
        elif isinstance(v,dict):
            if 'path' in v and 'sha256' in v:data(v)
            else:
                for x in v.values():links(x)
    links(load(m['gradeFreeze']))
    mapping=load(m['maskMap'])
    board={x['id']:x for x in json.loads(pkt.read('controller/criteria.json'))}
    stats={arm:Counter() for arm in ['signal-v2','signal-v4']}
    for c in m['cells']:
        i,a=c['id'],c['arm'];s=stats[a]
        q=pkt.read('subjects/'+i+'.txt').decode()
        assert q in load(c['request'])['argv'] and load(c['graderInput'])['question']==q
        assert mapping[c['mask']]==i+'.'+a and load(c['graderOutput'])['grade']==c['grade']
        receipt=load(c['receipt'])
        assert receipt['answer_sha256']==H(data(c['answer']))
        trace=load(c['trace']);links(trace['steps'])
        reads=[x['path'] for x in trace['reads'] if x['status']==3 and x['returnedExcerpt']]
        s['body']+=any(x.endswith('/SKILL.md') for x in reads)
        s['refs']+=any('/references/' in x for x in reads)
        s['tokens']+=load(c['usage'])['usage']['total_tokens']
        g={k:c['grade'][k]['verdict'] for k in AXES}
        board[i][a]=(g,c['critical'])
        s.update(k for k,v in g.items() if v=='pass')
    lines=['| Case | Platform/framework | Family | Whole v2/v4 | Primary v2/v4 | Verification v2/v4 | Failing v4 criteria | Critical v2/v4 |',
           '|---|---|---|---|---|---|---|---|']
    for i,row in sorted(board.items()):
        (b,bc),(v,vc)=row['signal-v2'],row['signal-v4']
        cells=[i,row['platform']+'/'+row['framework'],row['family'],*[b[k]+'/'+v[k] for k in ('whole','primary','verification')],
               ', '.join(k for k in AXES if k!='whole' and v[k]=='fail') or 'none',str(int(bc))+'/'+str(int(vc))]
        lines.append('| '+' | '.join(cells)+' |')
    out='\n'.join(lines)+'\n'
    if '--check' in sys.argv:assert (D/'PAIRS.md').read_text()==out
    else:(D/'PAIRS.md').write_text(out)
    print(summary,stats)

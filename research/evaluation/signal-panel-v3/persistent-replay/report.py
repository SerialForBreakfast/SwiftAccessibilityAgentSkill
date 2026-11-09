"""Verify input/receipt provenance; publish controller-only outcomes, not model answers."""
from stage import D,ROOT,H,packet
from collections import Counter
import json,re,sys
BASE=ROOT/'evals/results/persistent-replay'
first=BASE/'tmp6xijam9k'
follow=BASE/'adapters-o1xp27st'
registration=BASE/'registrations-tg6h920p'
final=BASE/'registrations-nch3vflc'
ret=packet(ROOT/'evals/results/signal-v2-review-20261108/signal-panel-v2-return.zip','9929eb1bddb1eb850bdc6ff026bb0469852e8ecab19ef7100689595788990368')
pkt=packet(D.parents[1]/'signal-panel-v2/held.zip','51bf28327715ad63929a107b9c8b3e3c364669916e3f2c0107f61b6300b45acd')
expected={r['id'] for r in json.loads(ret.read('transitions.json')) if r['transitions']['whole']=='persistent'}
grades={(g['id'],g['arm']):g for g in json.loads(ret.read('grades.json'))}
assert len(expected)==40 and {p.name for p in first.glob('P-*')}=={i+'.'+a for i in expected for a in ('skill','unaided')}
assert {p.name for p in follow.glob('P-*')}<={p.name for p in first.glob('P-*')}
def read(p):return json.loads(p.read_bytes())
rows=[]
for i in sorted(expected):
 for arm in ('unaided','skill'):
    cell=i+'.'+arm
    attempts=[];effective={}
    for base in (first,follow,registration,final):
        p=base/cell
        if not p.exists():continue
        r=read(p/'input.json');assert r['id']==i and r['arm']==arm
        assert all(H((p/n).read_bytes())==v for n,v in r['inputs'].items())
        assert (p/'answer.txt').read_bytes()==ret.read('records/'+cell+'/answer.txt')
        assert (p/'question.txt').read_bytes()==pkt.read('subjects/'+i+'.txt')
        for path,sha in r['oracle'].items():
            if path!='method':assert H((ROOT/path).read_bytes())==sha
        attempt=dict(run=base.name,selection=r['selection'],inputs=r['inputs'],oracle=r['oracle'])
        for lane in ('contract','proof'):
            if lane=='proof' and base!=first and not r['repeatproof']:continue
            z=read(p/(lane+'.json'));log=p/(lane+'.log')
            if log.exists():
                data=log.read_bytes()
                if z['status']!='orchestrator-interrupted':assert H(data)==z['log']
                intent=read(p/(lane+'-intent.json'));assert intent['source']==r['inputs']['Subject.swift']
                z=dict(z,firstIntent=H((p/(lane+'-intent.json')).read_bytes()),testFiles=intent['checks'])
                if z['status']=='orchestrator-interrupted' and b'** BUILD SUCCEEDED **' in data:
                    z.update(observed='compile-only',finalLog=H(data))
                if lane=='proof' and z['status']=='unit-failure' and b'Bundle.main.url(forResource: "test_media"' in data:
                    z.update(observed='missing-proof-fixture')
                # Swift Testing issues are not necessarily emitted as compiler-style errors.
                z['issues']=[line.replace(str(p),'<cell>')[:500] for line in data.decode(errors='replace').splitlines()
                             if 'recorded an issue at' in line or re.match(r'^Checks/.*(?:Assertion failed|Fatal error)',line)][:6]
            status=z.get('observed',z['status'])
            if status=='test-compile-failure' and lane=='contract':status='oracle-interface-gap'
            if status=='no-executable-proof':status='no-executable-proof-submitted'
            attempt[lane]=z
            effective[lane]=status
        attempts.append(attempt)
    grade=grades[i,arm]
    assert grade['whole']=='fail'
    rows.append(dict(id=i,arm=arm,platform=r['platform'],family=r['family'],criterion=r['criterion'],bindings=r['bindings'],
                     frozenSourceGrade={a:grade[a] for a in ('primary','verification','integration','whole','critical')},
                     effective=effective,attempts=attempts))
counts={lane:dict(sorted(Counter(r['effective'][lane] for r in rows).items())) for lane in ('contract','proof')}
result=dict(environments=read(first/'environment.json'),counts=counts,rows=rows)
assert result['environments']==read(follow/'environment.json')
assert result['environments']==read(registration/'environment.json')==read(final/'environment.json')
board=['# All 40 matched cases','',
       'U = unaided; S = installed signal-v2. Each cell lists the strongest executed original-contract check, not overall accessibility. Proof is the answer\'s own submission. Compile-only is not a unit pass. Source-only questions retain their original source grades. See evidence.json for both attempts, frozen grades, criteria, diagnostics, and digests.','',
       '| ID | Platform / family | Contract U | Contract S | Proof U | Proof S | Frozen primary U/S | Frozen verification U/S |','|---|---|---|---|---|---|---|---|']
for u,s in zip(rows[::2],rows[1::2]):
    assert u['id']==s['id']
    board.append('| '+' | '.join([u['id'],u['platform']+' / '+u['family'],u['effective']['contract'],s['effective']['contract'],u['effective']['proof'],s['effective']['proof']]+[' / '.join(r['frozenSourceGrade'][k] for r in (u,s)) for k in ('primary','verification')])+' |')
for name,b in [('evidence.json',(json.dumps(result,indent=2)+'\n').encode()),('CASES.md',('\n'.join(board)+'\n').encode())]:
    if '--check' in sys.argv:assert (D/name).read_bytes()==b
    else:(D/name).write_bytes(b)
print(json.dumps(counts,indent=2))

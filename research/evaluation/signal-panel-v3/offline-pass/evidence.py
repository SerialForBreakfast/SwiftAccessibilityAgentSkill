"""Index the first local attempts; never substitute a subsequent run."""
import hashlib,json,re,sys
from pathlib import Path
D=Path(__file__).resolve().parent
BASE=D.parents[3]/'evals/results/signal-dismissal-replay/tmpp8oicrif'
h=lambda b:hashlib.sha256(b).hexdigest()
rows=[]
for case in ('panel','sheet'):
    raw=(BASE/(case+'.txt')).read_bytes()
    blocks=re.findall(rb'(?m)^\x60{3}swift\r?\n(.*?)^\x60{3}\s*$',raw,re.S)
    for mode in ('submitted','contract'):
        p=BASE/case/mode
        # Freeze XCTest output independently of Xcode's optional diagnostic collector.
        snapshot=p/'first-xctest.log'
        if not snapshot.exists() and '--check' not in sys.argv:
            log=(p/'first.log').read_bytes()
            assert re.search(rb"Test Suite 'All tests' (passed|failed)",log)
            with snapshot.open('xb') as f:f.write(log)
        log=snapshot.read_bytes()
        r=json.loads((p/'intent.json').read_bytes())
        test=(p/'Tests/ReplayTests/Tests.swift').read_bytes()
        assert (p/'Sources/YourAppModule/Answer.swift').read_bytes()==blocks[0]
        assert test==(blocks[1] if mode=='submitted' else (D/(case+'.swift')).read_bytes())
        assert (r['answer'],r['source'],r['tests'])==(h(raw),h(blocks[0]),h(test))
        counts=sorted(set(re.findall(rb'Executed (\d+) tests?, with (\d+) failures?',log)))
        expected=(4,0) if mode=='submitted' else ((2,2) if case=='panel' else (1,1))
        assert counts==[tuple(str(i).encode() for i in expected)]
        rows.append({**{k:r[k] for k in ('case','mode','answer','source','tests','xcode','sdk')},
                     'logSnapshot':h(log),'diagnostics':[l.replace(str(p),'<attempt>') for l in log.decode().splitlines() if ': error: -[' in l],
                     'runtime':'iOS 26.5','deployment':'26.0','executed':expected[0],'failed':expected[1]})
data=(json.dumps(rows,indent=2)+'\n').encode()
if '--check' in sys.argv: assert data==(D/'first-results.json').read_bytes()
else:
    with (D/'first-results.json').open('xb') as f:f.write(data)

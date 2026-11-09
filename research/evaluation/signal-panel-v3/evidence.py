"""Summarize named immutable attempts, checking input hashes and actual assertions."""
from pathlib import Path
import hashlib,json,re,sys
D=Path(__file__).resolve().parent
BASE=D.parents[2]/'evals/results/signal-v3-native'
h=lambda data:hashlib.sha256(data).hexdigest()
p=D/'evidence.json'
check=sys.argv[1:]==['--check']
names=([r['attempt'] for r in json.loads(p.read_bytes())] if check else sys.argv[1:])
rows=[]
for name in names:
    assert Path(name).name==name
    run=BASE/name
    record=json.loads((run/'receipt.json').read_bytes())
    for n,sig in record['inputs'].items():assert h((run/n).read_bytes())==sig
    log=(run/'native.log').read_bytes()
    failures=[line.split(' : ',1)[-1].replace(str(run),'<attempt>') for line in log.decode().splitlines() if ': error: -[' in line]
    rows.append(dict(attempt=name,platform=record['platform'],variant=record['mode'],accepted=record['accepted'],
                     runtime=record['runtime'],sdk=record['sdk'],xcode=record['xcode'],deployment=record['deployment'],
                     tests=record['tests'],inputs=record['inputs'],diagnostics=failures,logSHA256=h(log),
                     receiptSHA256=h((run/'receipt.json').read_bytes())))
assert len({(r['platform'],r['variant']) for r in rows if r['accepted']})==6
data=(json.dumps(rows,indent=2)+'\n').encode()
if check:assert p.read_bytes()==data
else:
    with p.open('xb') as f:f.write(data)
print('Verified',len(rows),'native receipts and their staged inputs.')

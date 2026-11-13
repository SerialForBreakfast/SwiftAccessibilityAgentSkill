"""Offline-only, deterministic assembly of the held comparison. No dispatch path."""
import hashlib
import io
import json
import sys
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo

D = Path(__file__).resolve().parent
R = D.parents[1]
START = R/'evals/qualification-56/starter-v2'
V6 = R/'research/evaluation/signal-panel-v6/readiness/held.zip'
pins = {'0.2.2':'286beabd5bca40b7a4ff3fb0b67f8cb819ed50e184a03e811c3bbdc1d65d1655',
        'rc.2':'a1449f8863ee1c8724da8181d928cf8a58a963202da548b5fc1a1360e5b28aa5'}
def sha(data): return hashlib.sha256(data).hexdigest()
def encode(obj): return (json.dumps(obj, indent=2, sort_keys=True)+'\n').encode()

def packet():
    src = json.loads((START/'manifest.json').read_bytes())
    assert set(src)==set('4ec9 5d12 6d2d c04c c6b2 f483 4840 da78'.split())
    files={'controller/HANDOFF.md':(D/'HANDOFF.md').read_bytes()}
    with ZipFile(V6) as z: files['arms/0.2.2.zip']=z.read('arms/release-0.2.2.zip')
    files['arms/rc.2.zip']=(R/'evals/rc2/swift-accessibility-agent-0.3.0-rc.2.zip').read_bytes()
    for arm,h in pins.items(): assert sha(files['arms/'+arm+'.zip'])==h
    rubrics={r['id']:r for r in json.loads((R/'research/evaluation/signal-panel-v4/controller.json').read_bytes())}
    scoring={}; cells=[]
    for ix,(k,r) in enumerate(sorted(src.items())):
        path='starters/'+k+'.zip'
        blob=(START/'subjects'/(k+'.zip')).read_bytes();files[path]=blob
        assert sha(blob)==r['archive']
        with ZipFile(io.BytesIO(blob)) as z:
            assert {n:sha(z.read(n)) for n in z.namelist()}==r['members']
            q=z.read('QUESTION.md')
        original=rubrics[r['original']]
        scoring[k]=dict(platform=r['platform'],original=r['original'],criterion=original['caseSpecificCriterion'],
                        scope=original['verificationScope'])
        for arm in (list(pins) if ix%2==0 else list(reversed(pins))):
            cells.append(dict(index=len(cells)+1,case=k,arm=arm,skill='arms/'+arm+'.zip',skillSHA256=pins[arm],
                              starter=path,starterSHA256=sha(blob),questionSHA256=sha(q)))
    m=dict(job='rc2-local-starters-1',state='held',sourceCheckpoint='2af3b1103bd30ade2459d65499d333e654c84b89',
           instruction='Use the installed swift-accessibility-agent skill. Read the supplied local starter and return your proposed answer, including any requested code and tests. Do not execute code.',
           cells=cells,proposedAttempts=16,retries=0,incrementalSpend=0)
    assert len(cells)==16 and all(a['case']==b['case'] and a['arm']!=b['arm'] and
        a['starterSHA256']==b['starterSHA256'] and a['questionSHA256']==b['questionSHA256']
        for a,b in zip(cells[::2],cells[1::2]))
    files['controller/rubrics.json']=encode(scoring)
    files['controller/single-exchange.md']=(R/'evals/BIGDOG-SINGLE-EXCHANGE.md').read_bytes()
    files['manifest.json']=encode(m)
    files['index.json']=encode({n:sha(b) for n,b in files.items()})
    out=io.BytesIO()
    with ZipFile(out,'w') as z:
        for n,b in sorted(files.items()):
            info=ZipInfo(n,(2026,1,1,0,0,0));info.create_system=3;info.external_attr=0o100644<<16
            z.writestr(info,b,compress_type=ZIP_DEFLATED)
    return out.getvalue()

if __name__=='__main__':
    b=packet();path=D/'held.zip';seal=D/'SHA256SUMS';record=f'{sha(b)}  held.zip\n'
    if sys.argv[1:]==['--check']:
        assert path.read_bytes()==b and seal.read_text()==record
    elif not sys.argv[1:]:
        path.write_bytes(b);seal.write_text(record)
    else:raise SystemExit('usage: seal.py [--check]')
    print(record.strip())

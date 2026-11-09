"""Build a research-only skill and controller overlay. No model, package install or network."""
import csv, hashlib, io, json, posixpath, re, sys
from collections import Counter
from pathlib import Path
from zipfile import ZipFile, ZipInfo, ZIP_DEFLATED

D = Path(__file__).resolve().parent
ROOT = D.parents[2]
PREFIX = 'swift-accessibility-agent/'
def digest(b): return hashlib.sha256(b).hexdigest()
def packet(path, expected):
    b = path.read_bytes()
    if digest(b) != expected: raise ValueError(f'Input changed: {path.name}')
    return ZipFile(io.BytesIO(b))

def candidate():
    with packet(D.parent/'signal-panel-v3/rescue-replay/candidate.zip','ae40c671b714aef0c25222099fa4e933caf16f0d98147238ead0f0e1451cd956') as z:
        files={n:z.read(n) for n in z.namelist()}
    entry=PREFIX+'SKILL.md'
    files[entry]=files[entry].split(b'# Swift Accessibility Agent\n',1)[0].replace(b'signal-v3-rescue.1',b'signal-v4')+b'# Swift Accessibility Agent\n\n'+(D/'entry.md').read_bytes()
    for name in ('actions','validation','media','return'):
        files[PREFIX+'references/'+name+'.md']=(D/'cards'/f'{name}.md').read_bytes()
    out=io.BytesIO()
    with ZipFile(out,'w') as z:
        for n,data in sorted(files.items()):
            for link in re.findall(rb'\]\(([^)]+)\)',data):
                if not link.startswith(b'https:') and posixpath.normpath(posixpath.join(posixpath.dirname(n),link.decode())) not in files: raise ValueError(link)
            z.writestr(ZipInfo(n,(2026,1,1,0,0,0)),data,compress_type=ZIP_DEFLATED)
    return out.getvalue()

def board():
    by_scope=json.loads((D/'scopes.json').read_bytes())
    scopes={i:s for s,ids in by_scope.items() for i in ids}
    assert len(scopes)==sum(map(len,by_scope.values()))==56
    calibration=ROOT/'evals/native-calibration'
    sensitivity=json.loads((calibration/'proof-sensitivity/evidence.json').read_bytes())['rows']
    replay=json.loads((calibration/'calibration.json').read_bytes())['rows']
    witnesses={}
    with (D/'witnesses.tsv').open() as f:
        for group,contrast,weak in list(csv.reader(f,delimiter='\t'))[1:]:
            for family in group.split():
                if family in witnesses: raise ValueError(family)
                witnesses[family]=(contrast,weak)
    with packet(D.parent/'signal-panel-v2/held.zip','51bf28327715ad63929a107b9c8b3e3c364669916e3f2c0107f61b6300b45acd') as z, packet(ROOT/'evals/results/signal-v2-review-20261108/signal-panel-v2-return.zip','9929eb1bddb1eb850bdc6ff026bb0469852e8ecab19ef7100689595788990368') as ret:
        transition={r['id']:r['transitions']['whole'] for r in json.loads(ret.read('transitions.json'))}
        rows=[]
        for r in json.loads(z.read('controller/panel.json')):
            i=r['id']; data=z.read('subjects/'+i+'.txt')
            scope=scopes[i]
            contrast,weak=witnesses[r['family']]
            rows.append(dict(id=i,questionSHA256=digest(data),platform=r['platform'],framework=r['framework'],
                             family=r['family'],historicalTransition=transition[i],verificationScope=scope,
                             originalCriterion=r['criterion'],caseSpecificCriterion=r['reviewProposal'],
                             source=r['source'],assertions=r['assertions'],contrast=contrast,insufficientAlone=weak,
                             originalReplay={x['arm']:{k:x[k] for k in ('behavior','proofExecution','proofAdequacy')} for x in replay if x['id']==i},
                             qualifiedProofComparison={x['arm']:x['outcome'] for x in sensitivity if x['id']==i}))
        assert len(rows)==len(transition)==56 and {r['family'] for r in rows}==set(witnesses)
        return rows

if __name__=='__main__':
    rows=board()
    for name,data in [('candidate.zip',candidate()),('controller.json',(json.dumps(rows,indent=2)+'\n').encode())]:
        if '--check' in sys.argv:
            if (D/name).read_bytes()!=data: raise SystemExit(name+' is stale')
        else: (D/name).write_bytes(data)
    print(len(rows),'cases;', len({r['family'] for r in rows}),'families;',dict(Counter(r['verificationScope'] for r in rows)))

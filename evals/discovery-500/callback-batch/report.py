"""Build a sanitized per-answer board from immutable, locally recorded evidence."""
import argparse, csv, hashlib, io, json
from pathlib import Path

D=Path(__file__).resolve().parent
TABLE={
    'macOS-document':('testDocument','retired delete removed B'),
    'tvOS-shelf':('testShelf','retired control selected replacement'),
    'iOS-edit':('testLiveEdit','obsolete error reached current field'),
    'tvOS-edit':('testLiveEdit','obsolete error reached current field'),
    'macOS-sheet':('testLateAThenBTwice','late A must not consume B'),
    'iOS-panel':('testPanel','restored before completion'),
}
PROOFS={'9d04eb':'iOS-edit','64ff0d':'tvOS-edit','99d6c6':'macOS-sheet'}
SOLUTIONS={'1b1d51':'no-change starter','8b494a':'no-change starter','f32498':'unchanged document adapter; submitted view calls domain methods directly',
           'c6f0a2':'unchanged view; hosted registration seam','61e7b4':'unchanged button action','5376a3':'unchanged panel'}
PATCHES={'62bbd5','20d89c','015170'}
SUBMITTED={'c13f93':'test_dismissalCancellation_doesNotExecuteStaleCompletion','015170':'test_earlyFocusDismissal_andCancellationIntegrity'}
def selected(r):
    return r['family'] in ('actual-edit','retired-action','dismiss-owner','dismiss-timing') or r['id'][2:8] in PROOFS
def contract(r):
    return PROOFS.get(r['id'][2:8]) or {
        'actual-edit':r['platform']+'-edit','retired-action':{'macOS':'macOS-document','tvOS':'tvOS-shelf'} .get(r['platform']),
        'dismiss-owner':'macOS-sheet','dismiss-timing':'iOS-panel'}[r['family']]
def verdict(cell, method, marker=None):
    events=[v for name,v in cell['events'] if name.endswith(' '+method)]
    if events==['passed']:return 'pass'
    if events==['failed'] and any(method in e and (marker is None or marker in e) for e in cell['errors']):return 'assertion failure'
    return 'not established'
def build(data):
    grades=list(csv.DictReader((D.parent/'grade350/grades.csv').open()))
    rows=[]; families={}
    for r in filter(selected,grades):
        key=contract(r);method,marker=TABLE[key];p=r['platform'];prefix=r['id'][2:8]
        vals=[verdict(data[p+'-'+v],method,marker) for v in ('working','alternative','defect')]
        qualifies=vals==['pass','pass','assertion failure'];families[key]=qualifies
        binding=SOLUTIONS.get(prefix,'source judgment only')
        if prefix in PATCHES:
            binding='unchanged proposed patch in original starter'
            answer=verdict(data[p+'-patch'],method)
        elif prefix in SOLUTIONS:
            answer=verdict(data['iOS-answer-hook-repair' if p=='iOS' else p+'-answer'],'testRetainedRegistrations' if key=='macOS-sheet' else method)
        else:answer='not a complete production submission'
        if prefix in SUBMITTED:
            proof=' / '.join(verdict(data[p+'-'+v],SUBMITTED[prefix]) for v in ('working','alternative','defect'))
        elif prefix in PROOFS:
            proof='source only: expected assertions are prose; helper bypasses defective path'
        else:proof='no independently executable submitted proof bound'
        rows.append({'id':r['id'],'answerSHA256':r['answerSHA256'],'contract':key,'test':method,'working':vals[0],'alternative':vals[1],'mutant':vals[2],'qualified':qualifies,'sourceFinding':r['reason'],'replayBinding':binding,'productionReplay':answer,'submittedProofWorkingAlternativeDefect':proof})
    assert len(rows)==18 and len(set(r['id'] for r in rows))==18 and set(families)==set(TABLE)
    out=io.StringIO();w=csv.DictWriter(out,fieldnames=list(rows[0]),lineterminator='\n');w.writeheader();w.writerows(rows)
    return out.getvalue(),families
if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('batch',type=Path);parser.add_argument('patch_batch',type=Path);parser.add_argument('--write',action='store_true');args=parser.parse_args()
    data={}
    for batch in (args.batch,args.patch_batch):
      records=json.loads((batch/'results.json').read_text())
      repair=batch/'iOS-answer-hook-repair/result.json'
      if repair.exists():records[repair.parent.name]=json.loads(repair.read_text())
      for k,c in records.items():
        assert k not in data
        data[k]=c
        cell=batch/k
        for name,h in {**c['inputs'],'first.log':c['logSHA256']}.items():
            assert hashlib.sha256((cell/name).read_bytes()).hexdigest()==h,(k,name)
    board,families=build(data)
    for name,content in [('board.csv',board),('evidence.json',json.dumps(data,indent=2)+'\n')]:
        if args.write:(D/name).write_text(content)
        else:assert (D/name).read_text()==content
    print(families)

"""Materialize private subject and grading inputs from the pinned delivery."""
import csv, hashlib, json, re, sys, zipfile
from pathlib import Path
from alternatives import CHANGES
D=Path(__file__).resolve().parent; R=D.parents[1]
H=lambda b: hashlib.sha256(b).hexdigest()
J=lambda v: json.dumps(v,indent=2)+'\n'
PACKET='f20f90d25132e62b2b926ed3c4f9bed6c146e3d56d21d762b260e37b301bd7bf'
def body(s,method):
    start=s.index('{',s.index('func '+method+'(')); depth=1
    for j in range(start+1,len(s)):
        depth+=(s[j]=='{')-(s[j]=='}')
        if not depth:return start+1,j
    raise ValueError(method)
def prepare(packet,base):
    assert H(packet.read_bytes())==PACKET
    cases={x['id']:x for x in csv.DictReader((D/'cases.tsv').read_text().splitlines(),delimiter='\t')}
    z=zipfile.ZipFile(packet); manifest=json.loads(z.read('manifest.json')); assert set(cases)==set(CHANGES)=={r['id'] for r in manifest}
    for r in manifest:
        i=r['id']; t=cases[i]; a=base/i; a.mkdir(parents=True)
        sourcepath=r['replacementTarget']; source=z.read(i+'/'+sourcepath).decode()
        paths=sorted(p for p in (R/'code-examples').glob('*/*/Sources/'+Path(sourcepath).name) if p.read_text()==source)
        paths.sort(key=lambda p:r['platform'].lower() not in str(p))
        pkg=paths[0].parent.parent
        path=next(f for f in (pkg/'Tests').glob('*.swift') if 'func '+t['method']+'(' in f.read_text())
        canonical=path.read_text(); l,h=body(canonical,t['method']); repaired=canonical[l:h]
        weak=z.read(i+'/Tests/CurrentTests.swift').decode(); l,h=body(weak,'testCurrentBehavior')
        # Keep the supplied helpers and the weak assertions; add the stronger test in its own local scope.
        proof=weak[:h]+'\n        do {'+repaired+'\n        }\n    '+weak[h:]
        if i=='Q024':
            proof=proof.replace('        do {','        do {\n        replies.removeAll() // Isolate validator replies from the preceding check.',1)
        old,new=CHANGES[i]; assert source.count(old)==1,i
        alt=source.replace(old,new)
        if i=='Q066':alt=alt.replace('save.target = self; save.action = #selector(saveItem)','// Binding belongs to the button initializer.')
        starter=a/'subject'; starter.mkdir()
        for n in z.namelist():
            if n.startswith((i+'/Sources/',i+'/Tests/')):
                p=starter/n[len(i)+1:]; p.parent.mkdir(exist_ok=True);p.write_bytes(z.read(n))
        (starter/'QUESTION.md').write_text(t['question']+'\n\nReturn the revised XCTest and explain which observable would distinguish a regression. Production sources are supplied as context; do not change them.\n')
        for v in ('working','alternative','defect'):
            w=a/v
            for p in starter.rglob('*.swift'):
                dest=w/p.relative_to(starter);dest.parent.mkdir(exist_ok=True,parents=True)
                b=p.read_bytes()
                if p.name=='CurrentTests.swift':b=proof.encode()
                elif p.relative_to(starter).as_posix()==sourcepath:
                    b={'working':source.encode(),'alternative':alt.encode(),'defect':z.read(i+'/defect.swift')}[v]
                dest.write_bytes(b)
            (w/'Package.swift').write_text('// swift-tools-version: 5.9\nimport PackageDescription\nlet package=Package(name:"AccessibilityExamples",platforms:[.macOS("26.0"),.iOS("26.0"),.tvOS("26.0")],products:[.library(name:"AccessibilityExamples",targets:["AccessibilityExamples"])],targets:[.target(name:"AccessibilityExamples",path:"Sources"),.testTarget(name:"Checks",dependencies:["AccessibilityExamples"],path:"Tests")])\n')
        (a/'case.json').write_text(J(dict(**r,sourcePackage=str(pkg.relative_to(R)),assertionSource=str(path.relative_to(R)),method=t['method'],proofSHA256=H(proof.encode()),weakSHA256=H(weak.encode()))))
if __name__=='__main__':prepare(Path(sys.argv[1]),Path(sys.argv[2]))

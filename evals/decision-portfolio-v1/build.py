"""Build separate subject inputs and controller data; --check performs no writes."""
import argparse, csv, hashlib, io, json, re, zipfile
from pathlib import Path
D=Path(__file__).resolve().parent
R=D.parents[1]
A=D/'authoring'
H=lambda b:hashlib.sha256(b).hexdigest()
J=lambda x:(json.dumps(x,indent=2,sort_keys=True)+'\n').encode()
idof=lambda b:'Q-'+H(b)[:16]
def pack(members):
    out=io.BytesIO()
    with zipfile.ZipFile(out,'w') as z:
        for name,data in sorted(members.items()):
            info=zipfile.ZipInfo(name,(2026,1,1,0,0,0));info.create_system=3;info.external_attr=0o100644<<16
            z.writestr(info,data,compress_type=zipfile.ZIP_DEFLATED)
    return out.getvalue()
def swap(s,old,new):
    assert s.count(old)==1
    return s.replace(old,new)
direct=[
 ('Search','macOS','SwiftUI/AppKit','d82c','We are reviewing the recipient bar in our Mac mail composer. Keyboard users type and select text in the native field. Is the field exposed once for someone navigating with VoiceOver? Explain what the source establishes, change only what is needed, and give a focused check.',
  'RecipientField()\n','RecipientField().accessibilityHidden(true)\n','Leave the editable field exposed; only decoration should be hidden. Source does not establish an exact spoken stop count.','Remove redundant wrapper semantics or keep the native view transparent to the wrapper.','Hiding the field or its parent removes the editing target.'),
 ('Tap','iOS','SwiftUI','f93b','Our rehearsal app has a cue pad. A single tap should play or pause, dragging should seek, and a VoiceOver adjustment should change the cue without toggling playback. Does this version support all three? Supply only necessary edits and a focused check.',
  '.onTapGesture { transport.activate() }','.accessibilityAction { transport.activate() }','Check the actual single-tap registration separately from adjustment and drag. An accessibility action alone is not a touch handler.','A TapGesture or onTapGesture on the same surface may coexist with the existing drag and adjustable action.','Testing Transport.activate alone cannot show the view installs a tap handler.'),
 ('Inspector','iOS','UIKit/AVFoundation','9c45','Our preview inspector may open before a clip is assigned. Once a clip arrives it might have no audio group. Can we tell these situations apart and ship the supplied test with this payload? Review the source and test as a pair; keep the returned track information.',
  'guard case .waiting = before else { return XCTFail("before assignment") }','XCTAssertEqual(before, .waiting)','Distinguish missing item from inspected empty group; compare cases or relevant fields without a spurious payload equality requirement.','A switch, pattern match, or meaningful equality that really compiles and preserves the payload.','A test using XCTAssertEqual on an enum without Equatable cannot build.')]
def build():
    evidence=json.loads((R/'research/evaluation/prompt-improvements-v1/items.json').read_bytes())['items']
    answer_index={x['id']:x for x in json.loads((R/'research/evaluation/prompt-improvements-v1/next-pass/board.json').read_bytes())}
    originals={x['id']:x['prompt'] for x in map(json.loads,(R/'evals/gemini-discovery/subjects.jsonl').read_text().splitlines())}
    outputs={};rows=[]
    def add(question,assets,row):
        contents={'QUESTION.md':question.encode(),**assets}
        data=pack(contents);i=idof(data)
        assert not any(r['id']==i for r in rows)
        outputs['subjects/'+i+'.zip']=data
        rows.append(dict(row,id=i,sha256=H(data),questionSHA256=H(contents['QUESTION.md']),members={n:H(b) for n,b in contents.items()}))
    for name,os,fw,prior,q,old,new,criterion,alt,bad in direct:
        for mode in ['repair','preserve']:
            prod=(A/(name+'.swift')).read_text();test=(A/(name+'Tests.swift')).read_text()
            if mode=='repair':
                if name=='Inspector':test=swap(test,old,new)
                else:prod=swap(prod,old,new)
            pkg='// swift-tools-version: 5.9\nimport PackageDescription\nlet package = Package(name:"Feature", platforms:[.macOS("26.0"),.iOS("26.0")], products:[.library(name:"Feature",targets:["Feature"])], targets:[.target(name:"Feature"),.testTarget(name:"Checks",dependencies:["Feature"])])\n'
            add(q+'\n',{ 'Package.swift':pkg.encode(),'Sources/Feature/Feature.swift':prod.encode(),'Tests/Checks/Checks.swift':test.encode()},dict(lane='rc2-direct',family=name,platform=os,framework=fw,origin=prior,mode=mode,criterion=criterion,alternative=alt,negative=bad))
    rev=list(csv.DictReader((A/'revisions.tsv').read_text().splitlines(),delimiter='\t'))
    for row in rev:
        [x]=[x for x in evidence if x['id'][2:6]==row['origin']]
        q=originals[x['id']];assert x['verdict']=='fail' and H(q.encode())==x['questionSHA256']
        assert (x['audit'] or {}).get('blindWhole')!='pass'
        # Keep the full original request as specification, including starter and incidental constraints.
        # Replace the opening instead when the original has supplied source.
        prefix,sep,tail=q.partition('```')
        task=row['question']
        if sep:
            if row['origin']=='8b4c':task+=' Keep CheckoutViewController, totalLabel, payButton, formattedTotal, payCount and pay() names and types. Return the complete Swift file.'
            if row['origin']=='a32f':task+=' There are no other animations or parent transactions.'
            if row['origin']=='5f43':task+=' Include cancellation and retry behavior.'
            if x['lane']=='repair':task+=' If it already meets the requirement, leave it intact; otherwise include the smallest integrated change and a focused unit check.'
            task+='\n\nSupplied source:\n\n'+sep+tail
        else:task+='\n\nProject requirements:\n'+q.strip()
        task=x['platform']+' 26 / '+x['framework']+'\n\n'+task.strip()+'\n'
        add(task,{},dict(lane='development',family=row['family'],platform=x['platform'],framework=x['framework'],origin=x['id'],originalSHA256=x['questionSHA256'],originalAnswerSHA256=answer_index[x['id']]['answerSHA256'],priorWhole=x['verdict'],priorPrimary=x['primary'],priorRationale=x['rationale'],priorBlindAudit=x['audit'],criterion=row['criterion'],alternative=row['alternative'],negative=row['counterexample'],assertions=x['assertions'],source=x['source']))
    assert len(rev)>=24 and len({r['family'] for r in rev})==len(rev)
    for name,*_ in direct:
        aa,bb=[r for r in rows if r['family']==name];assert aa['questionSHA256']==bb['questionSHA256'] and sum(aa['members'][n]!=bb['members'][n] for n in aa['members'])==1
    outputs['controller/board.json']=J(rows)
    outputs['freeze.json']=J({'artifacts':{k:H(v) for k,v in sorted(outputs.items())},'gradingSHA256':H((D/'GRADING.md').read_bytes())})
    return outputs
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--check',action='store_true');args=ap.parse_args()
    outputs=build()
    if args.check:assert set(p.name for p in (D/'subjects').glob('*.zip'))=={Path(k).name for k in outputs if k.startswith('subjects/')}
    for k,v in outputs.items():
        p=D/k
        if args.check:assert p.read_bytes()==v,p
        else:p.parent.mkdir(exist_ok=True);p.write_bytes(v)
    print('verified' if args.check else 'built',sum(k.startswith('subjects/') for k in outputs),'subject ZIPs')

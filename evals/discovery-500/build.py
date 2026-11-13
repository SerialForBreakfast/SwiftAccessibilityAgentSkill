"""Assemble a held, deterministic discovery portfolio. No runner or dispatch."""
import argparse, csv, difflib, hashlib, io, json, re, zipfile
from collections import Counter, defaultdict
from pathlib import Path
D=Path(__file__).resolve().parent; R=D.parents[1]; G=R/'evals/gemini-discovery'
I=R/'research/evaluation/prompt-improvements-v1'
def read(p):return json.loads(p.read_bytes())
def H(b):return hashlib.sha256(b).hexdigest()
def J(x):return (json.dumps(x,sort_keys=True,ensure_ascii=True,indent=1)+'\n').encode()
def table(n):return list(csv.DictReader((D/n).read_text().splitlines(),delimiter='\t'))
def clean(s):return re.sub(r'/\*[^*\n]*\*/','',re.sub(r'(?m)^\s*//[^\n]*$','',s)).strip()
def archive(files):
    b=io.BytesIO()
    with zipfile.ZipFile(b,'w') as z:
        for n,data in sorted(files.items()):
            info=zipfile.ZipInfo(n,(2026,1,1,0,0,0));info.create_system=3;info.external_attr=0o100644<<16
            z.writestr(info,data,compress_type=zipfile.ZIP_DEFLATED)
    return b.getvalue()
def build():
    old={r['id']:r for r in read(I/'items.json')['items']}
    history={r['id']:r for r in read(I/'next-pass/board.json')}
    reviews={r['id']:r for p in sorted((I/'shards').glob('*.json')) for r in read(p)}
    inputs={r['id']:r['prompt'] for r in map(json.loads,(G/'subjects.jsonl').read_text().splitlines())}
    scenarios={r['family']:r for r in table('scenarios.tsv')};assert len(scenarios)==80
    groups=defaultdict(list)
    for r in read(G/'controller.json'):
        if r['lane']=='repair':groups[r['decision']].append(r)
    assert groups.keys()==scenarios.keys()
    priority={'real-model-gap':0,'evidence-only':1,'rework-only':2}
    def rank(r):
        x=old[r['id']];rev=reviews[r['id']]
        return (0 if x['verdict']=='fail' and (x['audit'] or {}).get('blindWhole')!='pass' and rev['problem'] in priority else 1, priority.get(rev['problem'],5),r['id'])
    for fam in groups:groups[fam].sort(key=rank)
    records=[];files={};counts=Counter()
    def add(mode,platform,fw,body,fams,refs,required,negative,alternative,control=False,product=None):
        prompt=f'{platform} 26 / {fw}\n\n'+body.strip()+'\n'
        b=prompt.encode();i='Q-'+H(b)[:16];n='questions/'+i+'.md';assert n not in files and prompt not in inputs.values()
        assert not any(s in prompt for s in ('failureIds','mutant-','NegativeFixtures/','blindWhole','expected route','Disposition:'))
        files[n]=b;counts[mode]+=1
        ancestors=[]
        for r in refs:
            x=old[r['id']];grade=history[r['id']]
            ancestors.append(dict(id=r['id'],priorWhole=x['verdict'],blindWhole=(x['audit'] or {}).get('blindWhole'),priorDiagnosis=reviews[r['id']]['problem'],priorAnswerSHA256=grade['answerSHA256'],oldQuestionSHA256=r['inputSHA256'],assertions=r.get('assertions',[]),claims=r.get('claims',[]),source=r['source'],check=r.get('check'),rubric=r.get('rubric'),criterion=r.get('criterion')))
        records.append(dict(id=i,path=n,promptSHA256=H(b),mode=mode,platform=platform,framework=fw,families=fams,ancestors=ancestors,workingControl=control,required=required,reject=negative,accepted=alternative,productCode=product,baseline='unmeasured',pairedSkill='unmeasured'))
    def lines(r):
        q=inputs[r['id']];assert H(q.encode())==r['inputSHA256']
        # DOTALL for file body only; preserve file boundaries.
        blocks=re.findall(r'(?m)^([^\n]+\.swift):\n```swift\n([\s\S]*?)\n```',q)
        assert blocks
        pkg=R/r['source'];m=read(pkg);ch=next(c for c in m['checks'] if c['id']==r['check'])
        def get(n):
            b=(pkg.parent/n).read_bytes();assert H(b)==next(f['sha256'] for f in m['files'] if f['path']==n);return clean(b.decode())
        rep=ch['replacement'];target=Path(rep['target']).name;bad=get(rep['source']);good=get(rep['target'])
        assert sum(n==target and s==bad for n,s in blocks)==1 and bad!=good
        def render(ok):return '\n\n'.join(f'{n}:\n```swift\n'+(good if ok and n==target else s)+'\n```' for n,s in blocks)
        return render(False),render(True),bad,good
    catalog={r['id']:r for r in read(G/'controller.json')}
    eligible=defaultdict(list)
    for i,x in old.items():
        v=reviews[i]
        if (x['verdict']=='fail' and (x['audit'] or {}).get('blindWhole')!='pass'
            and i[2:6] not in ('d7b1','6f19') and v['problem'] in priority and v['disposition']!='retire-duplicate'):
            eligible[x['platform'],x['framework']].append(catalog[i])
    for rs in eligible.values():rs.sort(key=rank)
    # Round-robin across real platform/framework cells; never relabel a UIKit fixture SwiftUI.
    assert sum(map(len,eligible.values())) >= 50, 'Not enough distinct qualifying predecessors'
    chosen=[]
    while len(chosen)<50:
        for cell in sorted(eligible):
            if eligible[cell] and len(chosen)<50:chosen.append(eligible[cell].pop(0))
    for r in chosen:
        i=r['id'];review=reviews[i];q=inputs[i];assert H(q.encode())==r['inputSHA256']
        context=q.partition('\n\nReview the supplied implementation')[0] if '\n\nReview the supplied implementation' in q else q.split('```')[0].strip()
        # Include all supplied files. The background is the team's original feature request,
        # not a new instruction to solve every old task in every format.
        codepart=q[q.index('```'):] if '```' in q else ''
        background=context.split('Here is the complete')[0].strip()
        fam=r.get('decision') or r['source']
        for mode,ask,req in [
          ('decision','What should the app do here, and what should remain unchanged? Give a design answer rather than a patch.','Identify the requested behavior and one plausible overcorrection.'),
          ('incident-triage','Support reported this interaction, but we do not have a recording. Give two plausible explanations, a sequence that distinguishes them, and what you could conclude from each result.','Distinguish hypotheses by different observed outcomes; do not present a report as a confirmed defect.'),
          ('integrated-solution','What would you ship for this request? Follow the interaction from the existing control to its effect; provide integrated Swift where needed, or explain why the existing implementation is sufficient.','Integrate the change into the actual owner and preserve ordinary use.'),
          ('proof','What focused unit check would tell us this works, rather than merely compiling? Give setup, triggering path, expected result, and a defect this check would actually reject. If a part is outside unit scope, separate it.','A discriminating sequence that distinguishes the stated defect, plus the evidence boundary.'),
          ('preservation-review','Before changing this feature, what working behavior is most at risk? Compare a narrowly scoped approach with a tempting alternative that would break that behavior. Give a concrete before/after check.','Identify a real preservation obligation and a counterexample to an overbroad fix.'),
          ('acceptance-plan','You are reviewing a proposed implementation of the feature below. Set acceptance criteria that would accept two different correct implementations, reject a plausible wrong one, and distinguish a grader/setup problem from a product defect.','State two acceptable approaches, a rejectable behavior and what evidence would settle the distinction.')]:
            body=ask+'\n\nBackground from the original feature request (answer the question above):\n'+background
            if codepart:body+='\n\nSupplied implementation:\n'+codepart
            add(mode,r['platform'],r['framework'],body,[fam],[r],req+' Case-specific evidence guide (apply only the portions requested above; do not require submitted code for design or triage): '+review['oracleChange'],
                review['diagnosis'],r.get('criterion') or ('Use the observable contract, not a preferred spelling; see '+str(r.get('rubric') or r.get('assertions',[]))),
                product='integrated Swift when necessary' if mode=='integrated-solution' else None)
    for j,(family,sc) in enumerate(sorted(scenarios.items())):
        r=groups[family][0]; b,g,bad,good=lines(r);valid=j%5==0
        add('code-review',r['platform'],r['framework'],sc['situation']+' Does this version meet the requirement? Trace the actual path. Leave it alone if it works; otherwise give the smallest integrated correction.\n\n'+(g if valid else b),[family],[r],('Preserve the working path. ' if valid else 'Repair the supplied path. ')+sc['expected'],sc['decoy'],'Any equivalent integration satisfying the observable.',control=valid)
        if j<70:
            before,after=(good,bad) if j%2 else (bad,good)
            diff='\n'.join(difflib.unified_diff(before.splitlines(),after.splitlines(),fromfile='before.swift',tofile='after.swift',n=4,lineterm=''))
            add('patch-review',r['platform'],r['framework'],sc['situation']+' Would you merge this change? Give a concrete input that distinguishes before from after, and identify a behavior that must stay intact.\n\n```diff\n'+diff+'\n```',[family],[r],('Reject the regression. ' if j%2 else 'Accept the scoped fix. ')+sc['expected'],sc['decoy'],'Equivalent source-backed reasoning about the changed path.')
    for x in table('workflows.tsv'):
        fs=[x['first'],x['second']];ref=[next((r for r in groups[f] if (r['platform'],r['framework'])==(x['platform'],x['framework'])),groups[f][0]) for f in fs]
        # Cross-platform analogies motivate questions, not API availability.
        for mode,request in [('architecture','What should own each piece of state, and what should the developer preserve when the screen updates? Give a bounded implementation plan; call out anything the description does not establish.'),
                             ('acceptance','Design a regression test for this interaction. Give a realistic sequence, expected intermediate and final results, and a change that would make the test fail for the right reason. Separate what units prove from what they cannot observe.')][table('workflows.tsv').index(x)%2::2]:
            add(mode,x['platform'],x['framework'],x['brief']+' '+request,fs,ref,' AND '.join(scenarios[f]['expected'] for f in fs)+(' Specify a discriminating sequence.' if mode=='acceptance' else ' Identify owners and boundaries.'),' OR '.join(scenarios[f]['decoy'] for f in fs),'Equivalent decisions supported for the requested platform; do not require a named API from an analogous platform.')
    assert counts=={**dict.fromkeys(('decision','incident-triage','integrated-solution','proof','preservation-review','acceptance-plan'),50),'code-review':80,'patch-review':70,'architecture':25,'acceptance':25}
    assert len(records)==len(files)==500 and len({r['promptSHA256'] for r in records})==500
    order=sorted(records,key=lambda r:H(('discovery-500-v1/'+r['id']).encode()))
    files['schedule.json']=J([{'index':i,'id':r['id'],'path':r['path'],'sha256':r['promptSHA256']} for i,r in enumerate(order,1)])
    out={'subjects.zip':archive(files),'controller.json':J(records)}
    out['freeze.json']=J(dict(status='held',count=500,fixtureFamilies=80,failedPredecessors=len(chosen),targetedVariants=6*len(chosen),explicitWorkingControls=sum(r['workingControl'] for r in records),formats=dict(counts),platforms=dict(Counter(r['platform'] for r in records)),frameworkCells=dict(Counter(r['platform']+'/'+r['framework'] for r in records)),sha256={n:H(v) for n,v in out.items()},gradingSHA256=H((D/'GRADING.md').read_bytes()),handoffSHA256=H((D/'HANDOFF.md').read_bytes())))
    return out
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--check',action='store_true');a=ap.parse_args()
    for n,v in build().items():
        if a.check:assert (D/n).read_bytes()==v,n
        else:(D/n).write_bytes(v)
    print('500 subject hashes, 80 fixture families plus failure seeds, ten formats; '+('verified' if a.check else 'built'))

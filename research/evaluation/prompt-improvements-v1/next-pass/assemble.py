"""Assemble or verify the offline portfolio. Never starts a worker or calls a model."""
import argparse
from collections import Counter, defaultdict
import hashlib
from io import BytesIO
import json
from pathlib import Path
from zipfile import ZipFile, ZipInfo, ZIP_DEFLATED

HERE = Path(__file__).resolve().parent
BASE = HERE.parent
ROOT = BASE.parents[2]
GD = ROOT/'evals/gemini-discovery'
REV = GD/'audit-revision-1'
PRIVATE = ROOT/'evals/results'
sha = lambda b: hashlib.sha256(b).hexdigest()
load = lambda p: json.loads(p.read_bytes())
dump = lambda x: (json.dumps(x, ensure_ascii=False, indent=2)+'\n').encode()
REQUEST = 'Explain your conclusion and give a focused check. Include integrated Swift changes if the requested behavior needs them.'


def archive(files):
    out = BytesIO()
    with ZipFile(out, 'w') as z:
        for name, data in sorted(files.items()):
            z.writestr(ZipInfo(name, (2026,1,1,0,0,0)), data, compress_type=ZIP_DEFLATED)
    return out.getvalue()


def main(check):
    out = {}
    items = {r['id']:r for r in load(BASE/'items.json')['items']}
    controls = {r['id']:r for r in load(GD/'controller.json')}
    orig = {r['id']:r['prompt'] for r in map(json.loads,(GD/'subjects.jsonl').read_text().splitlines())}
    bundles = PRIVATE/'gemini-discovery-20261108/bundles'
    for line in (bundles.parent/'SHA256SUMS').read_text().splitlines():
        digest, name = line.split()
        assert sha((bundles/name).read_bytes()) == digest
    with ZipFile(next(bundles.glob('*375*'))) as z:
        rawindex, grades = z.read('combined-answer-index.json'), z.read('grade-ledger.json')
        freeze=json.loads(z.read('grade-freeze.json'))
        assert sha(rawindex)==freeze['combinedAnswerIndexSHA256'] and sha(grades)==freeze['gradeSHA256']==load(GD/'baseline-metrics.json')['grade_ledger_sha256']
        ix={r['id']:r for r in json.loads(rawindex)}
        ledger={r['id']:r for r in json.loads(grades)}
    assert len(items)==384 and items.keys()==orig.keys()==controls.keys()==ix.keys()==ledger.keys()
    cases=load(REV/'cases.json')
    children=defaultdict(list)
    for n,v in cases.items(): children[v['parent']].append((n,v))
    neutral=dict(line.split('\t') for line in (HERE/'neutral.tsv').read_text().splitlines())
    native=load(BASE/'native-results.json')
    receipt=load(ROOT/native['privateReceipt']/'scorecard.json')
    assert not receipt.get('infrastructureError') and len(native['checks'])==len(receipt['rows'])==50
    observed={}
    for c,r in zip(native['checks'],receipt['rows']):
        assert all(c[k]==r[k] for k in ('task','variant','oracleSHA256','submissionSHA256','status'))
        if c['expected']: assert c['status']==c['expected']
        else: observed[c['task']]=c['status']
    controller=[]; subjects={}; shards=defaultdict(list); board=[]; states=Counter()
    for i,x in items.items():
        q=orig[i]; c=controls[i]; g=ledger[i]; a=ix[i]
        assert sha(q.encode())==a['inputSHA256']==x['questionSHA256']==c['inputSHA256']
        packet=load(PRIVATE/'prompt-improvements-v1/items'/f'{i}.json')
        assert packet['question']==q and packet['ledger']==g
        if a.get('answerSHA256'): assert sha(packet['answer'].encode())==a['answerSHA256']
        else: assert a['state']=='attempt-error' and packet['answer'] is None
        states[a['state']]+=1
        audit=x['audit']; pair=x['pair']; k=x['decision']; task=Path(c['source']).parent.name
        diagnostic=(('Audit '+audit['mask']+': '+audit['finding']) if audit else 'First source grade: '+x['rationale'])
        if a['state']=='attempt-error': diagnostic='The transport returned an attempt error; there is no answer to grade.'
        if x['lane']=='integration':
            diagnostic+=' Unchanged submission: '+(observed.get(task) or 'not admitted by the local review screen')+'.'
        options=children.get(i) or (children.get(pair['partner']) if pair else None)
        questions=[]; specs=[]; wordings=[]; ids=[]
        if options:
            for name, v in options:
                parts=q.split('\n\n',2); opening=v['opening']
                new='\n\n'.join([opening,REQUEST,parts[2]]) if len(parts)==3 else opening+'\n'
                if v['parent']==i: assert sha(new.encode())==v['prompt_sha256']
                questions.append(new); wordings.append(opening); specs.append(v['criterion'])
        elif pair:
            opening=f"{x['platform']} 26.0, {x['framework']}. "+neutral[k]
            if x['check']=='stale-status': opening=f"{x['platform']} 26.0, {x['framework']}. After selecting a search result, what status and label does the control expose?"
            if 'media-' in c['source'] and k=='request-generation': opening=f"{x['platform']} 26.0, {x['framework']}. Reload the track choices twice, then finish the older load last. What state does the inspector show?"
            questions=['\n\n'.join((opening,REQUEST,q.split('\n\n',2)[2]))]; wordings=[opening]
        else: questions=[q]
        changed=questions!=[q]
        disposition=('split-criteria' if len(questions)>1 else 'specify-policy' if options else 'rewrite-neutral' if changed else
                     'repair-oracle' if audit and audit['blindPrimary']!=x['primary'] else 'grade-components' if x['verdict']!='pass' else 'keep-control')
        problem=('grader-uncertain' if x['verdict']=='inconclusive' else 'oracle-mismatch' if disposition in ('split-criteria','repair-oracle') else
                 'ambiguous-policy' if options else 'symptom-as-fact' if changed else 'good-as-is' if x['verdict']=='pass' else
                 'real-model-gap' if audit and audit['blindPrimary']=='fail' else 'bundled-criteria')
        codes=[]
        if pair: codes.append('S1')
        if 'test' in diagnostic.lower() or 'check' in diagnostic.lower(): codes.append('S2')
        if k in ('presentation-owner','dismissal-completion','eligible-target','window-focus-isolation'): codes.append('S4')
        if k in ('rebound-action','request-generation','input-snapshot','interop-rebind'): codes.append('S3')
        if k in ('forced-vs-full','stale-off','audio-description-tag'): codes.append('S7')
        if k=='range-coordinate': codes.append('S6')
        if k in ('visible-title','edit-category','tv-text-reflow','conflicting-state-text'): codes.append('S5')
        if audit and audit['blindPrimary']=='pass' and audit['blindWhole']=='fail': codes.append('S8')
        criterion=' / '.join(specs) or c.get('criterion') or c.get('rubric') or '; '.join(c.get('assertions',[])) or c['grade']
        for j,new in enumerate(questions):
            digest=sha(new.encode()); sid='N-'+digest[:16]
            assert subjects.setdefault(sid,new)==new
            ids.append(sid)
            controller.append(dict(subject=sid,parent=i,platform=x['platform'],framework=x['framework'],family=k or c['source'],
                criterion=specs[j] if specs else criterion,originalController=c,originalPromptSHA256=a['inputSHA256'],
                answerSHA256=a.get('answerSHA256'),sourceGrade=g['verdict'],native=observed.get(task) if x['lane']=='integration' else None))
        pr='P0' if problem in ('oracle-mismatch','real-model-gap') else 'P1' if changed else 'P3' if disposition=='keep-control' else 'P2'
        rec=dict(id=i,diagnosis=diagnostic,problem=problem,disposition=disposition,
                 promptChange='none' if disposition=='keep-control' else ('Separate the two ownership or lifecycle conditions.' if len(questions)>1 else
                  'Use the same neutral scenario for both supplied implementations.' if pair else 'Use the calibrated developer contract.' if changed else 'Keep the request bytes; grade component outcomes separately.'),
                 proposedWording=' ‖ '.join(wordings) or None,oracleChange=criterion,skill=codes,
                 skillWhy=(f"Use the {k or task} case to test the linked distinctions; a case association is not a measured rescue." if codes else 'none'),
                 priority=pr,confidence='low' if x['verdict']=='inconclusive' else 'high' if audit or task in observed else 'medium',
                 transfer=('n/a' if not k else f'Test {k} in a separately authored product and ownership graph, not another variant of {task}.'))
        shards[x['platform'].lower()].append(rec)
        board.append(dict(id=i,subjectIDs=ids,disposition=disposition,changed=changed,pair=pair and pair['partner'],
                    originalAnswerStatus=a['state'],answerSHA256=a.get('answerSHA256'),grade=x['verdict'],blindAudit=audit and audit['mask'],
                    historicalComparison='ineligible: missing answer' if not a.get('answerSHA256') else 'new question' if changed else 'descriptive only',
                    nativeStatus=(observed.get(task,'held') if x['lane']=='integration' else None)))
    assert sum(v for k,v in states.items() if k=='completed')==383
    for key,rows in shards.items(): out['shards/'+key+'.json']=dump(rows)
    out['board.json']=dump(board)
    candidate={'SKILL.md':(HERE/'entry.md').read_bytes()}
    for n in ('actions','return','media','font'): candidate[f'references/{n}.md']=(HERE/f'{n}.md').read_bytes()
    candidate['agents/openai.yaml']=(HERE/'agents.yaml').read_bytes()
    skill=archive({'swift-accessibility-agent/'+k:v for k,v in candidate.items()})
    out['candidate.zip']=skill
    n=len(subjects)
    payload={'subjects/'+i+'.txt':q.encode() for i,q in subjects.items()}
    payload.update({'candidate.zip':skill,'controller/cases.json':dump(controller),'controller/board.json':out['board.json'],
        'controller/calibration.json':(REV/'calibration.json').read_bytes(),'controller/CALIBRATION.md':(REV/'CALIBRATION.md').read_bytes(),
        'controller/GRADING.md':(HERE/'GRADING.md').read_bytes(),'controller/single-exchange.md':(ROOT/'evals/BIGDOG-SINGLE-EXCHANGE.md').read_bytes()})
    for c in controls.values():
        for s in (c['source'],c.get('rubric')):
            if s:
                p=s.split('#')[0]; payload['controller/repository/'+p]=(ROOT/p).read_bytes()
    handoff=(HERE/'handoff-template.md').read_text().replace('{N}',str(n)).replace('{CELLS}',str(n*2)).replace('{EST}',f"{1721241*n*2/384:,.0f}")
    out['HANDOFF.md']=payload['HANDOFF.md']=handoff.encode()
    payload['seal.json']=dump({k:sha(v) for k,v in sorted(payload.items())})
    out['bigdog-held.zip']=archive(payload)
    out['receipt.json']=dump(dict(state='prepared_not_sent',parents=len(board),distinctSubjects=n,armAttempts=2*n,
        changedParents=sum(r['changed'] for r in board),baselineStates=states,dispositions=Counter(r['disposition'] for r in board),
        archiveSHA256=sha(out['bigdog-held.zip']),candidateSHA256=sha(skill),sourceGradeSHA256=sha(grades),answerIndexSHA256=sha(rawindex)))
    for path,data in out.items():
        p=HERE/path
        if check: assert p.read_bytes()==data,path
        else: p.parent.mkdir(exist_ok=True,parents=True); p.write_bytes(data)
    print(out['receipt.json'].decode())

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--check',action='store_true');main(p.parse_args().check)

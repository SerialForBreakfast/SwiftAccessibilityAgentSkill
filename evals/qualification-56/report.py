"""Bind immutable first answers, first replay receipts and rubric decision controls."""
from common import *
from starters import sources
from native_controls import suites
from more_controls import specs
from final_controls import specs as final_specs
from collections import Counter
import csv,re

E=ROOT/'evals/results/qualification-56'
EXISTING={'db6a':'testLiveEdit','4099':'testLiveEdit','3454':'testPanelReopen','9062':'testSurvivingOrigin',
          'be25':'testAttachedRefusal','d4bd':'testPickerWritesPlayerItem','dc1e':'testPickerWritesPlayerItem'}
def read(p):return json.loads(p.read_bytes())
def digest(p):return H(p.read_bytes())
def outcome(log,method):
    matches=re.findall(r"Test Case '[^']* "+method+r"\]' (passed|failed)",log)
    if len(matches)!=1:return 'no unique verdict'
    if matches==['failed'] and method.endswith('Mutant') and any(
        ': error: -[' in x and ' '+method+']' in x and 'witness' in x for x in log.splitlines()):
        return 'caught at witness'
    return matches[0]
def check_inputs(w,manifest):
    for name,h in manifest.items():assert digest(w/name)==h,(w,name)
def receipts(w):
    intent=read(w/'intent.json');check_inputs(w,intent['inputs'])
    log=(w/'native.log').read_bytes()
    if (w/'receipt.json').exists():
        r=read(w/'receipt.json');assert r['intent']==digest(w/'intent.json') and r['log']==H(log),w
    return intent,log.decode(errors='replace')
def build(batches):
    starts={r['id']:(r,src) for r,q,src in sources()}
    rows={r['id']:dict(id=r['id'],platform=r['platform'],framework=r['framework'],questionSHA256=r['questionSHA256'],
        criterion=r['caseSpecificCriterion'],originalCriterion=r['originalCriterion'],verification=r['verificationScope'],
        starter=None,answers={},controls=[]) for r in PANEL}
    w=E/'starters-hkvuft59'
    for plat in {r['platform'] for r in PANEL}:
        d=w/plat; intent,log=receipts(d);assert read(d/'receipt.json')['exit']==0 and 'testModulesLoad' in log
        for i,(r,data) in starts.items():
            if plat!=r['platform']:continue
            p=d/'Sources'/('Starter'+i[2:])/'Starter.swift';assert p.read_bytes()==data
            rows[i]['starter']={'source':H(data),'kind':'new scaffold' if (D/'scaffolds'/(i[2:6]+'.swift')).exists() else 'original fence','receipt':digest(d/'receipt.json')}
    with answers() as ret:
        cells=json.loads(ret.read('return.json'))['cells'];assert len(cells)==112
        for c in cells:
            row=rows[c['id']];arm=c['arm'];assert arm not in row['answers']
            dirs=[BASE/b/(c['id']+'.'+arm) for b in ('v4-paired-jwlc74x4','panel56-o8ki66kc')]
            d,=[d for d in dirs if d.exists()]
            inp=read(d/'input.json');check_inputs(d,inp['inputs'])
            assert H(ret.read(c['answer']['path']))==c['answer']['sha256']==digest(d/'answer.txt')
            assert c['questionSHA256']==row['questionSHA256']==digest(d/'question.txt')
            a={'batch':d.parent.name,'inputSHA256':digest(d/'input.json'),'selection':inp['selection'],'answerSHA256':c['answer']['sha256'],
               'sourceGrades':{k:v['verdict'] for k,v in c['grade'].items()}}
            for lane in ['contract','proof']:
                p=d/(lane+'.json');v=read(p);a[lane]={'first':v['status'],'receiptSHA256':digest(p)}
                if 'log' in v:
                    assert digest(d/(lane+'.log'))==v['log']
                    a[lane]['logSHA256']=v['log']
                    a[lane]['firstDiagnostic']=next(iter(v.get('diagnostics',[])),None)
            row['answers'][arm]=a
    specmap={s['ids'][0]:s for s in suites()+specs()+final_specs()}
    # Preserve every attempted platform host, including stalls and controller repairs.
    hosts=[]
    for batch in batches:
        for d in sorted((E/batch).glob('*/intent.json')):
            w=d.parent; intent,log=receipts(w)
            host=str(w.relative_to(E))
            rc=read(w/'receipt.json')['exit'] if (w/'receipt.json').exists() else None
            hosts.append(dict(host=host,intent=digest(d),log=digest(w/'native.log'),exit=rc))
            for first in sorted({v['cases'][0] for v in intent['methods'].values()}):
                s=specmap[first]; outcomes={}
                for v in ('Reference','Alternative','Mutant'):
                    method='testC'+first+v;assert intent['methods'][method]==dict(cases=s['ids'],variant=v)
                    outcomes[v]=outcome(log,method)
                    source=w/'Sources'/method[4:]/'Subject.swift'
                    assert source.read_text()==s['src'][('Reference','Alternative','Mutant').index(v)],source
                    probe=(w/'Tests'/(method[4:]+'Tests')/'Probe.swift').read_text()
                    if 'MOVIE' in s['body']:
                        movie,=set(re.findall(r'fileURLWithPath:"([^"]+\.mov)"',probe))
                        assert digest(Path(movie))=='c08c9e5d23f035221aedfd9004dde8873a1b9edeff1d21b45a73a4b5626f76f3'
                        probe=probe.replace(movie,'MOVIE')
                    assert s['body'] in probe,(host,method)
                good=outcomes=={'Reference':'passed','Alternative':'passed','Mutant':'caught at witness'} and rc==65
                for k in s['ids']:
                    row,=[r for i,r in rows.items() if i[2:6]==k];assert row['platform']==w.name
                    row['controls'].append(dict(host=host,methodPrefix='testC'+first,origin=s['origin'],qualified=good,verdicts=outcomes))
    cal=read(ROOT/'evals/native-calibration/calibration.json')['controllerProbes']
    with (D/'source-calibration.tsv').open() as f:examples={e['prefix']:e for e in csv.DictReader(f,delimiter='\t')}
    for i,row in rows.items():
        k=i[2:6]
        assert set(row['answers'])=={'signal-v2','signal-v4'}
        if k in EXISTING:
            p,=[x for x in cal if (x['platform'],x['method'])==(row['platform'],EXISTING[k])]
            row['priorControl']=p
        if k in examples:
            e=examples[k];assert all(e.values()) and len({e['reference'],e['alternative'],e['mutant']})==3
            row['sourceExamples']=k
        assert sum(map(bool,[row['controls'],row.get('priorControl'),row.get('sourceExamples')]))==1,i
        row['qualification']='source contrast' if k in examples else 'native decision' if k in EXISTING or any(c['qualified'] for c in row['controls']) else 'open oracle'
    return dict(controlBatches=batches,hosts=hosts,sourceCalibrationSHA256=digest(D/'source-calibration.tsv'),questions=list(rows.values()))
def chart(board):
    rows=board['questions']
    def score(group,dimension):
        pairs=Counter()
        for r in group:
            a,b=(r['answers'][arm]['sourceGrades'][dimension] for arm in ('signal-v2','signal-v4'))
            if a==b=='na':continue
            assert {a,b} <= {'pass','fail'},(r['id'],dimension,a,b)
            pairs[a,b]+=1
        both=pairs['pass','pass'];gain=pairs['fail','pass'];loss=pairs['pass','fail'];n=sum(pairs.values())
        return f'{both+loss}/{n} | {both+gain}/{n} | {gain-loss:+d} | {gain} | {loss}'
    header='Before: signal-v2 | After: signal-v4 | Net passes | Fixed | Regressed |'
    divider='|---|---:|---:|---:|---:|---:|'
    lines=['# Did the new skill produce better answers?', '',
           '**Whole-answer score: tied.** Same 56 development questions, one first answer per version and question. These are the original source grades, not compile counts.', '',
           '| What passed | '+header,divider]
    for label,key in [('Whole developer task','whole'),('Primary behavior','primary'),('Integrated with the supplied code','integration'),
                      ('Preserved ordinary actions and behavior','preservation'),('Supplied requested verification','verification'),('Avoided unnecessary changes','rework')]:
        lines.append(f'| {label} | {score(rows,key)} |')
    lines+=['','Fixed = failed before, passed after. Regressed = passed before, failed after. Ten questions did not require verification.',
            '','| Whole-task passes by platform | '+header,divider]
    for platform in ('iOS','macOS','tvOS'):
        lines.append(f"| {platform} | {score([r for r in rows if r['platform']==platform],'whole')} |")
    lines+=['','**Promotion: keep 0.2.2.** The measured comparison is between two research versions. The v4 chapter answer lost ordinary tap-to-play. Released 0.2.2 and the newest candidate, signal-v5, have not been scored head-to-head on this panel; their difference is unknown.',
            '','[All 56 before/after grades](../../research/evaluation/signal-panel-v4/results/PAIRS.md) | [Offline replay and grading coverage](REPLAY.md)']
    return '\n'.join(lines)+'\n'
def replay_chart(board):
    rows=board['questions']
    lines=['# Grading packet at a glance','','| Platform | Questions | Runnable starters | Native decision qualified | Source contrast | Open oracle | First answers |',
    '|---|---:|---:|---:|---:|---:|---:|']
    for p in ['iOS','macOS','tvOS','Total']:
        rr=[r for r in rows if p=='Total' or p==r['platform']];n=Counter(r['qualification'] for r in rr)
        lines.append(f"| {p} | {len(rr)} | {sum(bool(r['starter']) for r in rr)} | {n['native decision']} | {n['source contrast']} | {n['open oracle']} | {2*len(rr)} |")
    lines+=['','Native decision = two implementations accepted and one intended defect caught on the recorded platform. One probe can serve two questions. Source contrast = two acceptable answers and a rejected counterexample, assessed against the written criterion, not by XCTest. Neither column certifies every secondary criterion.','','| First host result | Original contract | Submitted proof |','|---|---:|---:|']
    counts=[Counter(a[l]['first'] for r in rows for a in r['answers'].values()) for l in ['contract','proof']]
    for k in sorted(set(counts[0])|set(counts[1])):lines.append(f'| {k} | {counts[0][k]} | {counts[1][k]} |')
    lines+=['','| Question | Platform | Grading control | v2 contract / proof | v4 contract / proof |','|---|---|---|---|---|']
    for r in rows:
        def arm(k):
            a=r['answers']['signal-'+k];return a['contract']['first']+' / '+a['proof']['first']
        lines.append(f"| {r['id']} | {r['platform']} | {r['qualification']} | {arm('v2')} | {arm('v4')} |")
    return '\n'.join(lines)+'\n'
if __name__=='__main__':
    path=D/'board.json';frozen='--check' in sys.argv
    batches=read(path)['controlBatches'] if frozen else sorted(p.name for p in E.glob('controls-*'))
    b=build(batches)
    for p,data in [(path,json.dumps(b,indent=2)+'\n'),(D/'CHART.md',chart(b)),(D/'REPLAY.md',replay_chart(b))]:
        if frozen:assert p.read_text()==data,p
        else:p.write_text(data)
    print(Counter(r['qualification'] for r in b['questions']))

"""Verify private first receipts and publish answer-level dispositions, without regrading."""
import json,re,sys
from zipfile import ZipFile
from prepare import D, BASE, ROOT, H
R=BASE/'persistent-replay'
first='sheet-answers-gyyquia1'
fixed='sheet-answers-ea4h1pu_'
extra='sheet-extra-0suc98ey'
items='sheet-items-h9gg5cpa'
def result(run,name):
    c=R/run/name
    inputs=json.loads((c/'input.json').read_bytes())['inputs']
    assert all(H((c/p).read_bytes())==h for p,h in inputs.items())
    intent=json.loads((c/'contract-intent.json').read_bytes())
    assert intent['source']==inputs['Subject.swift'] and intent['checks']==[inputs['Contract.swift']]
    receipt=(c/'contract.json').read_bytes()
    log=(c/'contract.log').read_bytes()
    r=json.loads(receipt)
    assert r['log']==H(log)
    statuses=re.findall(rb"Test Case '[^'\n]+ test(?:RetainedRegistrations|RegisteredItems)\]' (passed|failed|skipped) \(",log)
    assert len(statuses)==1
    status=statuses[0].decode()
    assert r['exit']==(65 if status=='failed' else 0)
    return dict(batch=run,cell=name,method=status,inputs=inputs,log=H(log),receipt=H(receipt),
                diagnostics=[s.split(' : ',1)[-1] for s in r['diagnostics']])
notes={
'dismiss-owner.text':'Two separate sheets. B has no onDismiss; no B callback to fire. Source finding.',
'G-370808352ca7dc':'Custom DetailsPanelView; coordinator helper is not an installed sheet registration.',
'G-1c220f178060c8':'Two item presentations, no sheet onDismiss supplied; content-specific close path.',
'G-22af858f9af21f':'Binding setter performs dismissal; no sheet completion to retain. tvOS not scored.',
'G-f981e62bcf7bd1':'DetailsPanel.onDisappear invokes a captured token. Content-disappearance host required.',
'G-90629dd9d60ff9':'Reads currentGeneration at callback time; internally stored coordinator, no qualified request observer.',
'P-90629dd9d60ff906.skill':'Reads activeGeneration inside callback; writes view-private focus. Prior helper proof passed; separate surviving-origin test failed.',
'P-90629dd9d60ff906.unaided':'No sheet completion; content receives a token. Requires content-lifecycle adapter.',
'P-90629dd9d60ff906.signal-v2':'Capture list snapshots generation. Private coordinator and view-driven focus; no qualified observer. Not a failure.',
'b03-2':'Current-session lookup inside item callback; internally created coordinator. Source risk only.',
'b04-1':'Completion registered on content disappearance, not sheet onDismiss. Helper alone insufficient.',
'b04-6':'Explicitly serializes presentations and documents a placeholder. Not compatible with required overlap.',
'b05-5':'Reads mutable currentPresentationID. Private coordinator; no audited observer of requests.',
'b05-7':'Coordinator and detail container; no registered sheet completion in answer.'}
def collect():
    rows=json.loads((R/fixed/'catalog.json').read_bytes())
    discovery=next(BASE.glob('gemini-discovery*/bundles/*375*'))
    legacy=next(BASE.glob('failure-inventory/bundles/dev7*'))
    with ZipFile(discovery) as z:
        for k in ('G-16de77ef3240aa','G-370808352ca7dc'):
            n=k+'/answer.txt';rows.append(dict(archive=discovery.name,member=n,answerSHA256=H(z.read(n))))
    with ZipFile(legacy) as z:
        for r in json.loads(z.read('answers-and-grades.json')):
            if r['case'].endswith('swiftui-lifecycle'):
                rows.append(dict(archive=legacy.name,member=r['id'],answerSHA256=H(r['original_answer'].encode())))
    orig={x['id']:x for x in json.loads((ROOT/'research/evaluation/signal-panel-v4/controller.json').read_bytes())}
    for r in rows:
        key=r['member'].split('/')[-2] if '/' in r['member'] else r['member']
        r.pop('proof',None)
        if key.startswith('P-'):
            i,arm=key.split('.')
            if arm in ('skill','unaided'):r['priorProof']=orig[i]['originalReplay'][arm]
        if 'cell' in r:
            f=result(first,r['cell']);assert f['method']=='skipped'
            r['firstHost']=f
            q=result(fixed,r['cell'])
        elif key=='P-90629dd9d60ff906.signal-v4':q=result(extra,'P-9062-v4')
        elif key=='G-16de77ef3240aa':q=result(extra,'P-'+key)
        elif key in ('G-fe05e95d638c25','b03-7'):q=result(items,'P-'+key)
        else:
            r['decision']=notes[key];continue
        assert q['inputs']['answer.txt']==r['answerSHA256']
        r['hosted']=q
        if q['method']=='skipped':
            assert key=='P-da7833399aac7f87.signal-v4'
            r['decision']='Second Open blocked by showing guard. Overlap not established; callback ungraded.'
        else:
            assert q['method']=='failed'
            if key=='b03-7':
                assert '("0")' in q['diagnostics'][0] and 'first B' in q['diagnostics'][0]
                r['decision']='Empty completion: B made no request.'
            elif key=='G-fe05e95d638c25':
                assert 'first-copy' in q['diagnostics'][0] and 'addButton' in q['diagnostics'][1]
                r['decision']='A restored copy; B replaced focus with Add.'
            else:
                assert 'late-A:' in q['diagnostics'][0]
                r['decision']='A issued restoration; B could not own the first request.'
    control=result(extra,'P-control-captured');assert control['method']=='passed'
    return dict(rows=rows,positiveHostControl=control,anchors=json.loads((R/fixed/'environment.json').read_bytes()))
value=collect()
dest=D/'evidence.json'
if sys.argv[1:]==['--record']:
    with dest.open('x') as out:out.write(json.dumps(value,indent=2)+'\n')
else:assert value==json.loads(dest.read_bytes())
print(len(value['rows']),'screened;',sum('hosted' in x for x in value['rows']),'submitted to the host')

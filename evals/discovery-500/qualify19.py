"""Bind the 19 missing assertion pointers without editing the frozen questions or grades."""
import csv,hashlib,json,subprocess,sys
from pathlib import Path
D=Path(__file__).resolve().parent;R=D.parents[1];Q=R/'evals/qualification-56'
def read(p):return json.loads(p.read_bytes())
def h(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def build():
    panel={x['id'][2:6]:x for x in read(Q/'board.json')['questions']}
    parent=R/'evals/decision-portfolio-v1/controller/board.json'
    old=read(parent);assert h(parent)==read(parent.parent.parent/'freeze.json')['artifacts']['controller/board.json']
    texts={x['prefix']:x for x in csv.DictReader((Q/'source-calibration.tsv').read_text().splitlines(),delimiter='\t')}
    prior={x['id'][2:6]:x for x in read(R/'research/evaluation/v6-failure-audit/audit.json')['rows']}
    notes={
    '1079':('Replace the previous Open UIAction by identifier on each configure.','Accumulating Open handlers dispatches obsolete callbacks.','Check both buttons, contextual labels and the decorative star separately.'),
    '3454':('Restore the prior background value via a captured restoration closure.','On ordinary finish force the background visible rather than restore its original state.','Does not prove every stale-callback, fallback or teardown path.'),
    'debf':('Consume the active download ID at terminal delivery.','Allow a second terminal event; expected one terminal announcement.','Notification requests only, not spoken delivery.'),
    'dd7e':('Use registry membership by object identity.','Accept a detached node and serve its obsolete children.','Not a full proof of preserved expansion/selection on a rendered outline.')}
    rows=[]
    for x in old:
        if x['lane']!='development' or x['assertions']:continue
        k=x['origin'][2:6];p=panel.get(k,{});out=dict(id=x['id'],origin=x['origin'],family=x['family'],decision=x['criterion'])
        if k=='8b4c':
            base=R/'evals/results/pool/attempt-yxl9okt5';sc=read(base/'scorecard.json')
            vs={}
            for v in sc['rows']:
                if v['task']!='checkout-integrated':continue
                w=R/v['artifacts'];assert read(w/'outcome.json')==v and h(w/'Submission.swift')==v['submissionSHA256'] and h(w/'Oracle.swift')==v['oracleSHA256']
                vs[v['variant']]=v['status']
            assert vs['alternative-vertical']==vs['reference']=='pass' and vs['mutant-pay-rewired']=='contract-failure'
            out.update(lane='native',method='checkout-integrated/test.swift',alternative='Working vertical checkout layout.',defect='Rewired Pay, fixed height and shrinking text fail the contract; out-of-scope local stack fails compilation, not an assertion.',gap='Layout and callback contract, not delivered interaction.',receipt=h(base/'scorecard.json'),variants=vs)
        elif p.get('controls') or p.get('priorControl'):
            c=p.get('priorControl') or next(v for v in p['controls'] if v['qualified'])
            if k in notes:a,b,gap=notes[k]
            else:
                v=prior[k];a,b,gap=v['alternative'],v['witness'],v['nextAction']
            out.update(lane='native',method=c.get('method',c.get('methodPrefix')),alternative=a,defect=b,gap=gap,receipt=c)
        elif k in texts:
            t=texts[k];out.update(lane='source-only',method='source-calibration.tsv#'+k,alternative=t['alternative'],defect=t['mutant'],gap=t['rejection'],reference=t['reference'])
        elif k=='96a8':
            out.update(lane='source-only',method='Local written contrast against supplied Toggle',alternative='Leave the labeled Toggle forwarding the existing Binding; equivalent factoring must still write to the same owner.',defect='Replace the binding with private initial State; subsequent edits never reach the preference store.',gap='Source grading only, no runtime AX claim or invocation evidence.')
        elif k=='5f43':
            c=prior['f483'];out.update(lane='partial-native',method=c['method'],alternative=c['alternative'],defect=c['witness'],receipt=c['control'],gap='Related macOS request, not this full starter. Qualify lifetime across leaving/returning and retry before scoring the full workflow natively.')
        elif k=='5f3c':
            out.update(lane='open',method=None,alternative=x['alternative'],defect=x['negative'],gap='Need an integrated tvOS card with stale callbacks on two successive loads of the SAME file, optional help/status clearing, and surviving ordinary Open. Single-row status or item-only checks do not qualify it.')
        else:raise ValueError(k)
        rows.append(out)
    assert len(rows)==len({r['id'] for r in rows})==19
    return rows
if __name__=='__main__':
    for script in [Q/'report.py',R/'evals/native-calibration/grade.py']:
        subprocess.run([sys.executable,'-B',str(script),'--check'],check=True,cwd=R)
    rows=build();(D/'qualification19.json').write_text(json.dumps(rows,indent=2)+'\n')
    t=['# Nineteen previously unbound questions','','Native means the recorded reference and a different implementation passed, and the named mutant failed at its witness. It is not a whole-answer verdict on the revised question. Source-only means two acceptable approaches and a rejectable alternative are assessed from the text, not executed.','', '| Target | Evidence | Valid alternative | Defect the check distinguishes | Boundary or remaining work |','|---|---|---|---|---|']
    for r in rows:t.append('| '+' | '.join([r['family'],r['lane']+': '+(r['method'] or 'not qualified'),r['alternative'],r['defect'],r['gap']])+' |')
    (D/'QUALIFICATION.md').write_text('\n'.join(t)+'\n')

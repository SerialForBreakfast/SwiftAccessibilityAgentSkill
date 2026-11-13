"""Verify replay receipts and publish anonymized outcomes, without grading build failures."""
from pathlib import Path
import hashlib,json,re,sys
D=Path(__file__).resolve().parent;R=D.parents[2];E=R/'evals/results'
H=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
variants=('ref','mut','alt')
def collect(batches):
    cells={}
    for b in batches:
        for receipt in b.glob('P-*/receipt.json'):
            d=receipt.parent;r=json.loads(receipt.read_bytes())
            orig=E/'mutation-grade-calibration/trial1'/(d.name.rsplit('.',1)[0]+'.ref')
            intent=json.loads((d/'intent.json').read_bytes())
            assert H(orig/'Proof0.swift')==H(d/'Tests/Proof0.swift')==r['proof']==intent['proof']
            assert H(d/'first.log')==r['log']
            assert all(H(d/'Subject'/f)==v for f,v in intent['sources'].items())
            r['tests']=[t for t in r['tests'] if not t[0].startswith('run with ')]
            log=(d/'first.log').read_text(errors='replace')
            if r['exit']==124:
                r['driverTimeout']=True
                if "Test Suite 'All tests' passed" in log and r['tests'] and all(s=='passed' for _,s in r['tests']):
                    r['status']='pass'
                elif "Test Suite 'All tests' failed" not in log:
                    r['status']='harness-timeout'
            first=cells.setdefault(r['id'],{}).get(r['variant'])
            if first:r['priorAttempt']={k:first[k] for k in ('status','log','attempt')}
            r['attempt']=b.name
            cells[r['id']][r['variant']]=r
    assert len(cells)==8 and all(set(v)==set(variants) for v in cells.values())
    return cells

if __name__=='__main__':
    results=collect([E/x for x in sys.argv[1:]])
    rows=['# Frozen starter-interface replay','','All are signal-v6, trial 1, receipt 1507. Outcomes below are for the submitted proof, not the whole answer. Ref and alt are valid implementations; mut is the deliberately defective one.','',
          '| Case | Reference | Defect | Alternative | Interpretation |','|---|---|---|---|---|']
    for k,v in sorted(results.items()):
        statuses=[v[x]['status'] for x in variants]
        if statuses==['pass','pass','pass']:note='Accepts both valid variants but misses the defect.'
        elif statuses==['pass','assertion-failure','pass']:note='Distinguishes the defect; accepts the alternative (see failing assertion).'
        elif statuses[0]=='assertion-failure':note='Rejects the reference; a mutant failure does not establish discrimination.'
        elif 'compile-error' in statuses:note='No behavioral grade: compile diagnostic remains.'
        elif 'compile-only' in statuses:note='Remote URLs: compiled only; runtime discrimination unmeasured.'
        else:note='Unresolved; inspect first diagnostics.'
        notes={
            '4840':'Direct ticket helper, not installed A/B closure. First attempt lacked macro visibility; separate test support file fixed discovery.',
            'da78':'Direct ticket helper, not installed closure; duplicate B check passes even on shared-ticket wiring.',
            '4ec9':'The nil-item subtest passes only the defective phase. On all variants replacement expected nil although the local fixture auto-selected a forced track; unknown-ID subtest passed.',
            '5d12':'Proof calls AVMediaSelectionOption.unicodeLanguageIdentifier, unavailable in the target SDK. No fabricated extension.',
            '6d2d':'Remote HLS URL in the submitted load. All three variants typecheck; no assertion executed.',
            'c04c':'Remote player-item URLs in the suite; unchanged proof compiled on all variants, no behavioral verdict.',
            'c6b2':'Remote item URLs in the submitted tests; async loader type bound on all variants, no behavioral verdict.',
            'f483':'Injected string-option state only; does not inspect native legible selection.'}
        rows.append('| '+' | '.join([k,*statuses,note+' '+notes[k]])+' |')
        for r in v.values():r['errors']=[re.sub(r'/Users/[^:]*?/starter-eight-[^:]*?(?=:|$)','<fixture>',s) for s in r['errors']]
    (D/'RESULTS.md').write_text('\n'.join(rows)+'\n')
    (D/'receipts.json').write_text(json.dumps(results,indent=1)+'\n')

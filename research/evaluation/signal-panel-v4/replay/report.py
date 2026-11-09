"""Reconcile immutable lane receipts and method diagnostics; never alter frozen source grades."""
from prepare import ROOT,D,H
import json,re,sys
from collections import Counter

BASE=ROOT/'evals/results/persistent-replay'
BATCHES={'original':'v4-paired-jwlc74x4','chapter':'v4-chapter-ymeth6l8','focused':'v4-focused-adkfoyzt','integration':'v4-integrated-sfb3ke37','contrasts':'v4-contrasts-3kxiy5ss','registration':'v4-registration-2t8p1hxq'}
BATCHES['binding']='v4-binding-cpq3qelu'
def collect():
    records=[]
    for lane,batch in BATCHES.items():
        base=BASE/batch
        for cell in sorted(base.glob('P-*')):
            meta=json.loads((cell/'input.json').read_bytes())
            for name,h in meta['inputs'].items(): assert H((cell/name).read_bytes())==h
            initial=BASE/BATCHES['original']/cell.name
            if lane=='chapter':
                source=(initial/'Subject.swift').read_bytes()
                assert (cell/'Contract.swift').read_bytes().startswith(source) and H(source)==meta['originalSubjectSHA256']
            if lane in ('focused','contrasts'): assert (cell/'Subject.swift').read_bytes()==(initial/'Subject.swift').read_bytes()
            if lane=='integration': assert (cell/'Subject.swift').read_bytes().endswith((initial/'Subject.swift').read_bytes())
            if lane=='registration': assert (cell/'Subject.swift').read_bytes().startswith((initial/'Subject.swift').read_bytes())
            if lane=='binding':
                parent=BASE/BATCHES['integration' if cell.name.startswith('P-d4bd') else 'focused']/cell.name
                assert (cell/'Subject.swift').read_bytes()==(parent/'Subject.swift').read_bytes()
            row=dict(batch=lane,id=meta['id'],arm=meta['arm'],selection=meta['selection'],inputs=meta['inputs'],oracle=meta['oracle'])
            for key in ['contract','proof'] if lane in ('original','integration','registration') else ['contract']:
                r=json.loads((cell/(key+'.json')).read_bytes());status=r['status']
                result=dict(status=status,receiptSHA256=H((cell/(key+'.json')).read_bytes()))
                if 'log' in r:
                    log=(cell/(key+'.log')).read_bytes();assert H(log)==r['log']
                    result.update(logSHA256=r['log'],exit=r['exit'],diagnostics=r['diagnostics'],methods=re.findall(r"Test Case '.*? ([^\s]+)\]' (passed|failed)",log.decode(errors='replace')))
                row[key]=result
            records.append(row)
    assert Counter(r['batch'] for r in records)==dict(original=46,chapter=2,focused=9,integration=1,contrasts=10,registration=1,binding=2)
    return dict(batches=BATCHES,environments={k:json.loads((BASE/v/'environment.json').read_bytes()) for k,v in BATCHES.items()},records=records)
def main():
    result=collect()
    assert len({repr(v) for v in result['environments'].values()})==1
    data=json.dumps(result,indent=2)+'\n'
    board=['| Case | Arm | Original contract | Submitted proof | Additional controller result |','|---|---|---|---|---|']
    for row in result['records']:
        if row['batch']!='original':continue
        extra=[r for r in result['records'] if r['id']==row['id'] and r['arm']==row['arm'] and r['batch']!='original']
        board.append('| '+' | '.join([row['id'],row['arm'],row['contract']['status'],row['proof']['status'],', '.join(r['batch']+': '+r['contract']['status'] for r in extra) or 'n/a'])+' |')
    for f,s in [('evidence.json',data),('CASES.md','\n'.join(board)+'\n')]:
        if '--check' in sys.argv:assert (D/f).read_text()==s
        else:(D/f).write_text(s)
    for key in ('contract','proof'):
        print(key,Counter(r[key]['status'] for r in result['records'] if r['batch']=='original'))
if __name__=='__main__':main()

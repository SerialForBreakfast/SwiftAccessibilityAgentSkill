"""Render the case-by-case board without publishing raw model answers or private paths."""
from collections import Counter
from stage import D
from pathlib import Path
import json,csv
HERE=Path(__file__).resolve().parent
inv=json.loads((D/'inventory.json').read_bytes()); rows=json.loads((D/'board.json').read_bytes())
topics={r['id']:r['observable'] for r in csv.DictReader((HERE.parent/'witnesses.tsv').read_text().splitlines(),delimiter='\t')}
counts=Counter(x['outcome'] for x in rows)
table=['# Preserved proof replay: all 20 triplets','',f"{len(inv['origins'])} unique answer texts in {len(inv['archives'])} answer-bearing returns. {len(rows)} production-owner matches; this is a proof-block count, not a model or original-task pass rate.",'','| Case | Observable | Caught | Missed | Rejected valid | Compile gap | Crash/exception |','|---|---|---:|---:|---:|---:|---:|']
detail=[]
for i,o in topics.items():
    group=[x for x in rows if x['case']==i];c=Counter(x['outcome'] for x in group)
    cells=[c[k] for k in ('differential assertion','misses defect','rejects valid code')]
    table.append(f"| {i} | {o} | "+' | '.join(str(k) for k in cells+[c['interface/discovery gap'],len(group)-sum(cells)-c['interface/discovery gap']])+' |')
    detail+=['','## '+i,'','| Submitted proof | Native result | Evidence |','|---|---|---|']
    for x in group:
        outcome=x['outcome'];summ=x.get('detail') or ''
        if outcome=='differential assertion':
            e=next(f for m in x['arms']['defect'] for f in m['failures'] if f['assertion']);summ=e['assertion'];outcome='catches supplied defect'
        elif outcome=='rejects valid code':
            arm=next(v for v in ('working','alternative') if any(m['status']!='Passed' for m in x['arms'][v]));summ=arm+': '+next((f['message'] for m in x['arms'][arm] for f in m['failures']),'see first result')
        elif outcome=='misses defect':summ=', '.join(m['method'] for m in x['arms']['working'])
        detail.append('| `'+x['hash'][:12]+'` | '+outcome+' | '+summ.replace('|','\\|').replace('\n',' ')+' |')
(HERE/'RESULTS.md').write_text('\n'.join(table+detail)+'\n')

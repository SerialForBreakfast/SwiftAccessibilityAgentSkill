"""python3 score.py panel.json unmasked-grades.json ; never generates or judges answers."""
from collections import Counter, defaultdict
import json
import sys
AXES=('primary','preservation','verification','rework','integration','whole')
def score(panel,grades):
    cells={}; ids={r['id'] for r in panel}
    for g in grades:
        key=g['id'],g['arm']
        if key[0] not in ids or key[1] not in ('unaided','skill') or key in cells:raise ValueError(key)
        if any(g.get(a) not in ('pass','fail','unknown','na') for a in AXES) or type(g.get('critical'))!=bool:raise ValueError(key)
        cells[key]=g
    def transition(i,axis):
        a,b=(cells.get((i,k),{}).get(axis) for k in ('unaided','skill'))
        if a not in ('pass','fail') or b not in ('pass','fail'):return 'inconclusive'
        return {('pass','fail'):'regression',('fail','pass'):'rescue',('fail','fail'):'persistent',('pass','pass'):'preserved'}[a,b]
    byaxis=defaultdict(Counter);families=defaultdict(list);slices=defaultdict(Counter);crit=[];pairs=Counter();trace=[]
    byparent={r['parent']:r for r in panel}
    for r in panel:
        i=r['id'];axis=r['axis'];t=transition(i,'whole' if axis=='sentinel' else axis)
        byaxis[axis][t]+=1;slices[r['platform']+'/'+r['framework']][transition(i,'whole')]+=1
        trace.append(dict(id=i,target=t,whole=transition(i,'whole')))
        families[r['family']].append(t)
        if cells.get((i,'skill'),{}).get('critical'):crit.append(i)
        if r['counterpart'] and r['parent']<r['counterpart']:
            j=byparent[r['counterpart']]['id']
            for arm in ('unaided','skill'):
                v=[cells.get((s,arm),{}).get('whole') for s in (i,j)]
                pairs[arm+':'+('inconclusive' if any(z not in ('pass','fail') for z in v) else 'both correct' if v==['pass','pass'] else 'not both correct')]+=1
    return dict(planned=len(ids)*2,returned=len(cells),targetAxes=byaxis,wholeByCell=slices,twins=pairs,
                familiesWithRescueAndNoObservedLossOrUnknown=sorted(k for k,vs in families.items() if 'rescue' in vs and not {'regression','inconclusive','persistent'}.intersection(vs)),
                candidateCriticalFlagsRequiringReview=crit,cases=trace)
if __name__=='__main__':
    print(json.dumps(score(*(json.load(open(p)) for p in sys.argv[1:])),indent=2))

"""Build the held, failure-enriched research packet; --check only verifies bytes."""
from collections import Counter
from hashlib import sha256
from io import BytesIO
import json
from pathlib import Path
import sys
from zipfile import ZipFile, ZipInfo, ZIP_DEFLATED

D=Path(__file__).resolve().parent
BASE=D.parent/'prompt-improvements-v1'
PRE=BASE/'next-pass'
ROOT=D.parents[2]
read=lambda p:json.loads(p.read_bytes())
dump=lambda x:(json.dumps(x,indent=2,ensure_ascii=False)+'\n').encode()
h=lambda b:sha256(b).hexdigest()
def pack(files):
    buf=BytesIO()
    with ZipFile(buf,'w') as z:
        for n,b in sorted(files.items()):
            z.writestr(ZipInfo(n,(2026,1,1,0,0,0)),b,compress_type=ZIP_DEFLATED)
    return buf.getvalue()

# One historically passing matched counterpart in each framework/platform cell.
twins=['a1aff76682fe0a','01c10c6a8573fa','9ce845a566d425','79fa7510bdf4bc','61cfbceeb763f0','51c53f30543cc0']
neutral={
'da89005c6d3613':'Close a panel, then finish or cancel dismissal. At which points does this implementation request focus?',
'd95da35e90afc0':'For an editor with optional edit-action grouping, how are the actions categorized with the option on and off?',
'5b313c25cc544a':'Start validation, change the text, then deliver the original reply. Which text and result does this form show?',
'2ae6e6631d0d54':'Edit the entry while a validation request is outstanding. After the reply, can I submit the current entry?',
'ed8bff5491ab72':'Someone using the remote wants to tell these two buttons apart by looking at the screen. What titles does this setup show?',
'60133c52c4694a':'Open the inspector before assigning a player item, then inspect an item with no matching tracks. What result does the caller receive each time?',
}
def build():
    items={x['id']:x for x in read(BASE/'items.json')['items']}
    proposals={r['id']:r for p in (BASE/'shards').glob('*.json') for r in read(p)}
    assert items.keys()==proposals.keys() and len(items)==384
    tasks={}; seeds={}
    for l in (D/'families.tsv').read_text().splitlines():
        if l and not l.startswith('#'):
            i,key,axis=l.split('\t'); assert 'G-'+i not in tasks
            tasks['G-'+i]=(key,axis)
    for id in twins:
        i='G-'+id; j=items[i]['pair']['partner']; assert j not in tasks and items[j]['verdict']=='pass'
        tasks[j]=(tasks[i][0],'sentinel'); seeds[j]=i
    old=(PRE/'bigdog-held.zip').read_bytes()
    assert h(old)==read(PRE/'receipt.json')['archiveSHA256']
    p={}; rows=[]; counts=Counter(); usage=0
    with ZipFile(BytesIO(old)) as z:
        mapping={r['parent']:r for r in json.loads(z.read('controller/cases.json')) if r['parent'] in tasks}
        assert len(mapping)==len(tasks)==len([r for r in json.loads(z.read('controller/cases.json')) if r['parent'] in tasks])
        for i,(key,axis) in sorted(tasks.items()):
            x,s=items[i],proposals[i]; row=mapping[i]; oldq=z.read('subjects/'+row['subject']+'.txt').decode(); q=oldq
            if i[2:] in neutral:
                assert not x['pair'] and x['lane']=='repair'
                q=f"{x['platform']} 26.0, {x['framework']}. "+neutral[i[2:]]+'\n\n'+oldq.split('\n\n',1)[1]
            sid='P-'+h(q.encode())[:16]; assert 'subjects/'+sid+'.txt' not in p
            p['subjects/'+sid+'.txt']=q.encode()
            assert q.split('```')[1::2]==oldq.split('```')[1::2]
            rows.append(dict(id=sid,parent=i,family=key,axis=axis,platform=x['platform'],framework=x['framework'],
                counterpart=seeds.get(i) or (x['pair']['partner'] if x['pair'] and x['pair']['partner'] in seeds else None),
                frozenWhole=x['verdict'],blind=x['audit'] and x['audit']['mask'],evidence=s['diagnosis'],
                criterion=row['criterion'],reviewProposal=s['oracleChange'],source=x['source'],assertions=x['assertions']))
            counts[axis]+=1
            for n in [x['source'],x.get('rubric')]:
                if n:
                    path='controller/repository/'+n.split('#')[0]; p[path]=z.read(path)
        with ZipFile(BytesIO(z.read('candidate.zip'))) as skill:
            files={n:skill.read(n) for n in skill.namelist()}
        prefix='swift-accessibility-agent/'
        name=prefix+'SKILL.md'
        files[name]=files[name].replace(b'discovery-v2',b'signal-v1')+b'- [Platform distinctions](references/facts.md) when a title, role, edit category or system text setting determines the answer.\n'
        files[prefix+'references/facts.md']=(D/'facts.md').read_bytes()
        files[prefix+'references/actions.md']+=b'\nWhen the action is installed, capture its intended owner. At delivery, compare it with current state before dispatch. Reading the latest token twice cannot identify an obsolete callback. Rebinding should neither accumulate handlers nor disable the current ordinary action.\n'
        candidate=pack(files);p['candidate.zip']=candidate
        p['controller/GRADING.md']=z.read('controller/GRADING.md')
    # Selected-case usage is a planning estimate only, not a new bill or quota authorization.
    p['controller/panel.json']=dump(rows)
    p['controller/return-checklist.md']=(ROOT/'evals/BIGDOG-SINGLE-EXCHANGE.md').read_bytes()
    p['controller/score.py']=(D/'score.py').read_bytes()
    p['HANDOFF.md']=(D/'HANDOFF.md').read_bytes()
    p['seal.json']=dump({k:h(v) for k,v in sorted(p.items())})
    b=pack(p)
    selections=set(tasks)
    assert not selections.intersection({'G-d7b1d47b70ec1b','G-6f19bb8fa70065','G-19d3be9a5d1d73'})
    assert len({(r['platform'],r['framework']) for r in rows if r['axis']=='sentinel'})==6
    for r in rows:
        if r['counterpart']:
            other=next(v for v in rows if v['parent']==r['counterpart'])
            assert p['subjects/'+r['id']+'.txt'].split(b'\n\n',2)[:2]==p['subjects/'+other['id']+'.txt'].split(b'\n\n',2)[:2]
    return {'candidate.zip':candidate,'held.zip':b,'panel.json':dump(rows),'receipt.json':dump(dict(status='held-not-sent',cases=len(rows),arms=2,attempts=2*len(rows),axes=counts,
      familyKeys=len(set(k for k,a in tasks.values() if a!='sentinel')),historicalWhole=Counter(r['frozenWhole'] for r in rows),
      excluded=len(items)-len(tasks),packetSHA256=h(b),candidateSHA256=h(candidate),supersedesForRoutineRuns=h(old)))}
if __name__=='__main__':
    for n,b in build().items():
        if '--check' in sys.argv: assert (D/n).read_bytes()==b,n
        else: (D/n).write_bytes(b)
        if n=='receipt.json':print(b.decode())

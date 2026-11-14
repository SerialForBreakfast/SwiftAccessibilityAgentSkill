"""Build the held comparison only. No provider, dispatch or execution code."""
import argparse
from collections import Counter
from hashlib import sha256
from io import BytesIO
import json
from pathlib import Path
import re
from zipfile import ZipFile, ZipInfo, ZIP_DEFLATED

D = Path(__file__).resolve().parent
V2 = D.parent
V1 = V2.parent / "decision-batch-v1"
ROOT = D.parents[3]
ARMS = {"decision-batch-v1": (V1, "aa23b85f2235f1eb74f7738c8541529950b44b9a048fdf38f2660024ceed7b5c"),
        "decision-batch-v2": (V2, "026662ac8268f4645d0e24d15d0c4dec3ffae819c2688149dc285de51728ed33")}
TOPICS = {"retained-actions","editable-wrapper","text-units","appkit-row","caption-selection","description-tag",
          "native-slider","live-field","visible-title","dismissal"}
def h(b): return sha256(b).hexdigest()
def j(obj): return (json.dumps(obj,indent=2,sort_keys=True)+"\n").encode()
def archive(files):
    output=BytesIO()
    with ZipFile(output,"w") as z:
        for k,v in sorted(files.items()):
            info=ZipInfo(k);info.create_system=3;info.external_attr=0o100644<<16
            z.writestr(info,v,compress_type=ZIP_DEFLATED)
    return output.getvalue()
def tokens(s): return re.findall(r"[a-z0-9]+",s.lower())
def shingles(s):
    t=tokens(s)
    return set(zip(t,t[1:],t[2:],t[3:],t[4:]))
def build():
    arms={}
    for name,(folder,digest) in ARMS.items():
        data=(folder/'candidate.zip').read_bytes()
        assert h(data)==digest
        arms['arms/'+name+'.zip']=data
    history={}
    for prefix,path in [('discovery',ROOT/'evals/discovery-500/subjects.zip'),('focused',V1/'questions.zip')]:
        with ZipFile(path) as z:
            for n in z.namelist():
                if n.startswith('questions/') and n.endswith('.md'):
                    history[prefix+'/'+n]=z.read(n).decode()
    old={k:shingles(v) for k,v in history.items()}
    subjects,criteria,pairs,overlap={},{},{},{}
    for block in (D/'cases.txt').read_text().strip().split('\n\n'):
        lines=block.splitlines()
        if lines[0].startswith('#'):lines=lines[1:]
        meta,question,first,p1,second,p2,ordinary,alternative,reject=lines
        assert [x[0] for x in [meta,first,p1,second,p2,ordinary,alternative,reject]]==list('@=+=+!~-')
        topic,pair,platform,framework=meta[1:].split('|');assert pair not in pairs
        pairs[pair]=[]
        for starter,primary in [(first,p1),(second,p2)]:
            body=f"{platform} 26 / {framework}\n\n{question}\n\n{starter[1:]}\n"
            data=body.encode();qid='Q-'+h(data)[:16]; path=f'questions/{qid}.md'
            assert path not in subjects and body not in history.values()
            subjects[path]=data
            criteria[qid]=dict(pair=pair,topic=topic,platform=platform,framework=framework,primary=primary[1:],
                ordinary=ordinary[1:],acceptedAlternative=alternative[1:],reject=reject[1:],promptSHA256=h(data))
            pairs[pair].append(qid)
            grams=shingles(body)
            score,nearest=max((len(grams & v)/len(grams | v),k) for k,v in old.items())
            overlap[qid]=dict(nearest=nearest,fiveWordJaccard=round(score,5))
    assert len(subjects)==24 and len(pairs)==12 and {r['topic'] for r in criteria.values()}==TOPICS
    assert len({(r['platform'],r['framework']) for r in criteria.values()})==6
    assert all(criteria[a]['primary']!=criteria[b]['primary'] and criteria[a]['ordinary']==criteria[b]['ordinary'] for a,b in pairs.values())
    # Seed-independent order: opaque content IDs, with explicit counterbalancing.
    order=sorted(criteria,key=lambda q:h(('held-v2:'+q).encode()))
    schedule=[dict(question=q,arm=arm,promptSHA256=criteria[q]['promptSHA256'])
              for i,q in enumerate(order) for arm in (list(ARMS) if i%2==0 else list(reversed(ARMS)))]
    assert len({(r['question'],r['arm']) for r in schedule})==48
    subjects_zip=archive(subjects)
    files={**arms,'subjects.zip':subjects_zip,'controller/criteria.json':j(criteria),
           'controller/pairs.json':j(pairs),'controller/schedule.json':j(schedule),
           'controller/protocol.md':(D/'PROTOCOL.md').read_bytes(),'controller/score.py':(D/'score.py').read_bytes()}
    manifest={'status':'held_not_authorized','job':'decision-batch-v2-counterexamples-1','cases':24,'pairs':12,
              'plannedFirstAttempts':48,'files':{k:h(v) for k,v in files.items()}}
    return {'held.zip':archive({**files,'manifest.json':j(manifest)}),'manifest.json':j(manifest),
            'overlap.json':j(dict(historyEntries=len(history),cases=overlap))}
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--check',action='store_true');args=p.parse_args()
    for n,b in build().items():
        if args.check:
            if (D/n).read_bytes()!=b:raise SystemExit('stale: '+n)
        else:(D/n).write_bytes(b)
        print(n,h(b))

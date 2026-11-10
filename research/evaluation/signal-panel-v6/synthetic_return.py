"""Synthetic graded return for testing the v6 checker and analysis. Not model output."""
import hashlib,json,sys,zipfile
H=lambda b:hashlib.sha256(b).hexdigest()
held,out,copy=sys.argv[1],sys.argv[2],'--copy' in sys.argv
seal=H(open(held,'rb').read()); sched=json.loads(zipfile.ZipFile(held).read('schedule.json'))
ids=sorted({r['id'] for r in sched}); limit={'unaided':10,'release-0.2.2':20,'signal-v6':40}
files={};cells=[]
def put(path,b):
    b=b if isinstance(b,bytes) else b.encode(); files[path]=b; return {'path':path,'sha256':H(b)}
for n,r in enumerate(sched):
    p=f'cells/{n}/'; ok=ids.index(r['id'])<limit[r['arm']]
    ans=f"Answer {n}. Fix: synthetic excerpt {n}."
    c=dict(id=r['id'],arm=r['arm'],trial=r['trial'],state='answered',attempts=1,questionSHA256=r['questionSHA256'],skillSHA256=r['skillSHA256'],
      request=put(p+'request.json','{}'),receipt=put(p+'receipt.json','{}'),transport=put(p+'transport.json','{}'),
      usage=put(p+'usage.json',json.dumps({'usage':{'total_tokens':1000+n}})),
      trace=put(p+'trace.json',json.dumps({'reads':[{'path':'swift-accessibility-agent/SKILL.md'}] if r['arm']!='unaided' else []})),
      answer=put(p+'answer.txt',ans),mask=f'M{n:04}',critical=('--critical-swap' in sys.argv and r['trial']==1 and (r['arm'],r['id']) in {('release-0.2.2',ids[0]),('signal-v6',ids[1])}),graderInput=put(p+'gin.txt','x'),graderOutput=put(p+'gout.txt','y'))
    v='pass' if ok else 'fail'
    c['grade']={k:{'verdict':v,'reason':('same reason' if copy and n==0 else f'{k} reason {n}'),'excerpt':f'synthetic excerpt {n}'} for k in ('primary','preservation','integration','verification','rework','whole')}
    cells.append(c)
m=dict(job='signal-v6-run1',packetSHA256=seal,status='complete',stopReason='',report=put('report.md','r'),runLedger=put('ledger.json','{}'),
  gradeFreeze=put('freeze.json','{}'),maskMap=put('mask.json','{}'),cells=cells)
with zipfile.ZipFile(out,'w') as z:
    z.writestr('return.json',json.dumps(m))
    for k,b in files.items():z.writestr(k,b)
print(seal)

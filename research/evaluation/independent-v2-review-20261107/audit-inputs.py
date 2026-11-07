import hashlib,json
from pathlib import Path
ROOT=Path.cwd(); OUT=ROOT/'research/evaluation/independent-v2-review-20261107'; P=ROOT/'research/evaluation/milestone-package-v2'
seen={}; errors=[]
def read(path):
 p=Path(path); p=p if p.is_absolute() else ROOT/p
 data=p.read_bytes();seen[str(p.relative_to(ROOT))]={'sha256':hashlib.sha256(data).hexdigest(),'bytes':len(data)};return data
def js(path):return json.loads(read(path))
def pin(path,sha):
 try: got=hashlib.sha256(read(path)).hexdigest();ok=got==sha
 except FileNotFoundError:got=None;ok=False
 if not ok:errors.append({'path':path,'expected':sha,'actual':got})
 return ok
m=js(P/'manifest.json');r=js('research/evaluation/rubric-closure-v1/rubrics.json');b=js('research/evaluation/assertion-bindings-v1/bindings.json');ctl=js('research/evaluation/failure-driven/candidates/0.3.0-dev.5/evaluation/controller.json')
for path in ['AGENTS.md','AGENT.md','research/evaluation/failure-driven/PRD.md','research/evaluation/failure-driven/TASKS.md','research/evaluation/prompt-records-v1/README.md']+['research/evaluation/milestone-package-v2/'+n for n in ['README.md','REVIEW.md','preflight.json','sdk-evidence.json']]:read(path)
for inp in m['inputs']:pin(inp['path'],inp['sha256'])
rows={x['id']:x for x in r['rows']};contracts={**b['contracts'],**{x['id']:x for x in r['supplementalContracts']}};selected={};pairs=[]
for case in m['cases']:
 rr=rows[case['id']]; pin(rr['subject']['path'],rr['subject']['sha256']); arms=[]
 for plan in case['plans']:
  pin(P/plan['path'],plan['sha256']);a=js(P/plan['path']);u=json.loads(a['messages'][1]['content']);arms.append((a,u))
  for ref in u['suppliedReferences']:
   expected=next(x['sha256'] for x in plan['suppliedReferences'] if x['path']==ref['path']);actual=hashlib.sha256(ref['content'].encode()).hexdigest()
   if actual!=expected:errors.append({'embeddedReference':ref['path'],'expected':expected,'actual':actual})
 pairs.append({'id':case['id'],'sameRequest':arms[0][1]['request']==arms[1][1]['request'],'subjectFileEqualsRequest':read(rr['subject']['path']).decode()==arms[0][1]['request'],'genericNoReferences':arms[0][1]['suppliedReferences']==[], 'payloads':[{**plan,'path':str((P/plan['path']).relative_to(ROOT))} for plan in case['plans']]})
 for s in rr['sources']:pin(s['path'],s['sha256'])
 for criterion in rr['criteria']:
  for key in criterion['priorContractIds']+criterion['supplementalContractIds']: selected[key]=contracts[key]
checks=[]
for key,c in selected.items():
 pin(c['file'],c['fileSha256']);data=read(c['file']);method=c.get('method',c);sub=data[method['startByte']:method['endByte']];sha=hashlib.sha256(sub).hexdigest();ok=sha==c['methodSha256']
 if not ok:errors.append({'method':key,'actual':sha,'expected':c['methodSha256']})
 pin(c['manifest'],c['manifestSha256']);receipt=c['receipt'];rp=receipt.get('path') or receipt.get('index');rs=receipt.get('sha256') or receipt.get('indexSha256');pin(rp,rs)

 for neg in c.get('negativeControls',[]):
  pin(neg['index'],neg['indexSha256'])
 checks.append({'id':key,'file':c['file'],'methodSha256':sha,'exactMethodBytesMatch':ok,'receiptPath':rp,'receiptAttempt':receipt.get('attempt'),'environment':receipt.get('environment'),'negativeControls':c.get('negativeControls',[]),'scope':'Method body and saved receipt identity inspected; historical native execution not repeated; no subject answer exists.'})
sdk=js(P/'sdk-evidence.json');sdkhost=[{'id':x['id'],'capturedPath':x['file'],'currentHostAvailable':Path(x['file']).exists(),'freshSDKVerification':'unknown: captured SDK absent on current host'} for x in sdk['records']]
(OUT/'input-audit.json').write_text(json.dumps({'files':seen,'selectedAssertionContracts':checks,'pairs':pairs,'sdkCurrentHost':sdkhost,'integrityErrors':errors,'summary':{'pairs':len(pairs),'contracts':len(checks),'filesHashed':len(seen),'errors':len(errors)}},indent=2)+'\n')
print(json.dumps({'pairs':len(pairs),'methods':len(checks),'files':len(seen),'errors':errors,'pairEquality':all(x['sameRequest'] and x['subjectFileEqualsRequest'] and x['genericNoReferences'] for x in pairs)},indent=2))

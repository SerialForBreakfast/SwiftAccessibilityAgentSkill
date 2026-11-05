/** Offline campaign planning/coverage only. This module never contacts a model. */
import fs from 'node:fs';import path from 'node:path';import {pathToFileURL} from 'node:url';
import {repo,hash,fingerprint,files} from './lib.mjs';import {contextScenario} from './grading.mjs';
const read=name=>JSON.parse(fs.readFileSync(path.join(repo,'evals',name)));
export function planCampaign({worker='bigdog',profile='standard',split='development'}={}){
 const execution=read('execution-profiles.json'),complexity=read('complexity.json'),scenarios=read('scenarios.json');
 if(!execution.workers[worker]||!execution.profiles[profile])throw Error('Unknown worker/profile');
 if(!['development','heldout','all'].includes(split))throw Error('Unknown split');
 const selected=scenarios.filter(s=>split==='all'||s.split===split),budget=execution.profiles[profile];
 const pins=Object.fromEntries(['scenarios.json','rubrics.json','complexity.json','execution-profiles.json','release-gates.json','evidence/grading-evidence.json'].map(p=>[p,hash(fs.readFileSync(path.join(repo,'evals',p)))]));
 pins.runner=hash(files(path.join(repo,'evals/runner')).map(p=>path.relative(repo,p)+'\0'+hash(fs.readFileSync(p))).join('\n'));
 const roots={baseline:{relativePath:'evals/baselines/0.2.2/files',skillHash:fingerprint(path.join(repo,'evals/baselines/0.2.2/files'))},candidate:{relativePath:'.',skillHash:fingerprint(repo)}};
 const jobs=selected.flatMap(s=>s.os.flatMap(os=>Object.keys(roots).flatMap(release=>execution.conditions.flatMap(condition=>Array.from({length:execution.repetitions},(_,repeat)=>{
  const details={family:s.id,split:s.split,lane:s.lane,platform:s.platform,os,complexity:complexity.families[s.id]?.level,release,condition,repeat,profile,budget};if(!details.complexity)throw Error('Missing complexity');
  return {...details,id:hash(JSON.stringify({...details,pins,skillHash:roots[release].skillHash})),userTurns:contextScenario(s,os).turns,referencePaths:s.references,lookupExpected:condition==='C3'&&s.references.some(p=>!p.endsWith('unavailable-fixture.md'))};
 })))));
 const payload={schemaVersion:1,fingerprintPolicy:'skill-v2-no-os-metadata',execution:'requirements-only; no inference on the orchestration machine',requestedWorker:worker,profile,split,budget,pins,roots,modelRequirement:'Worker must return immutable model/tokenizer/template/backend/build/quantization and effective settings before execution.',jobs};
 return {...payload,planHash:hash(JSON.stringify(payload))};
}
export const outcomeStatuses=['completed','truncated','context_overflow','unsupported_tools','tokenizer_unavailable','timeout','transport_error','worker_unavailable','cancelled','unknown_outcome'];
export function coverage(plan,records){
 const {planHash,...body}=plan;if(hash(JSON.stringify(body))!==planHash)throw Error('Plan hash mismatch');
 const seen=new Map();for(const r of records){if(r.planHash!==planHash)throw Error('Receipt plan mismatch');if(!outcomeStatuses.includes(r.status))throw Error('Unknown outcome');if(!plan.jobs.some(j=>j.id===r.jobId))throw Error('Unknown job');if(seen.has(r.jobId))throw Error('Duplicate outcome; reconcile attempts before import');if(r.workerId!==plan.requestedWorker)throw Error('Wrong worker; create a separately pinned dispatch');if(!['bigdog','maxmini'].includes(r.workerId)||!r.modelRevision||!r.runtimeRevision)throw Error('Missing worker/model/runtime identity');if(!Number.isInteger(r.generationRequests)||r.generationRequests<0)throw Error('Missing request count');if(['completed','truncated'].includes(r.status)&&r.generationRequests===0)throw Error('Generated output needs an attempt');seen.set(r.jobId,r);}
 const slices={};for(const j of plan.jobs){for(const axis of ['overall','complexity','profile','condition','release','platform','lane']){const key=axis==='overall'?'overall':axis+':'+j[axis];const s=slices[key]??={planned:0,returned:0,missing:0,generationRequests:0,outcomes:{},qualityGraded:0,lookupEligible:0,lookupWithRead:0,lookupWithExpectedRead:0};s.planned++;if(j.lookupExpected)s.lookupEligible++;const r=seen.get(j.id);if(!r){s.missing++;continue;}s.returned++;s.generationRequests+=r.generationRequests;s.outcomes[r.status]=(s.outcomes[r.status]||0)+1;
 if(Number.isFinite(r.quality)&&r.quality>=0&&r.quality<=1)s.qualityGraded++;
 if(j.lookupExpected){const reads=r.referenceReads?.filter(x=>x.origin==='model-tool'&&x.path?.startsWith('references/')&&x.bytes>0&&/^[a-f0-9]{64}$/.test(x.sha256))||[];if(reads.length)s.lookupWithRead++;if(reads.some(x=>j.referencePaths.includes(x.path)))s.lookupWithExpectedRead++;}
 }}
 return {planHash,requestedWorker:plan.requestedWorker,totalPlanned:plan.jobs.length,totalReturned:seen.size,totalMissing:plan.jobs.length-seen.size,coverageComplete:seen.size===plan.jobs.length,slices,interpretation:'Complete accounting is not a quality pass. Expected failures remain failures. Use independent grades and paired, model/profile-matched comparisons.'};
}
if(process.argv[1]&&import.meta.url===pathToFileURL(process.argv[1]).href){const [command,...args]=process.argv.slice(2);if(command==='plan'){const options={};for(let i=0;i<args.length;i+=2){const key=args[i].replace(/^--/,'');if(!['worker','profile','split'].includes(key)||!args[i+1])throw Error('Expected --worker/--profile/--split value');options[key]=args[i+1];}console.log(JSON.stringify(planCampaign(options),null,2));}else if(command==='coverage'){const p=JSON.parse(fs.readFileSync(args[0])),raw=fs.readFileSync(args[1],'utf8').trim();const records=raw?raw.split('\n').map(line=>JSON.parse(line)):[];console.log(JSON.stringify(coverage(p,records),null,2));}else throw Error('Usage: campaign.mjs plan [--worker bigdog|maxmini] [--profile tiny|compact|standard|frontier] [--split development|heldout|all] OR coverage plan.json receipts.jsonl');}

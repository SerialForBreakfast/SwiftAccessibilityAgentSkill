// Controller-only audit. Never invokes a provider, simulator or compiler.
import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {createHash} from 'node:crypto';
const root=fileURLToPath(new URL('../../../',import.meta.url));
const subjectBase='research/evaluation/failure-driven/candidates/0.3.0-dev.5/';
export const hash=b=>createHash('sha256').update(b).digest('hex');
const read=p=>fs.readFileSync(path.join(root,p));
function files(dir){return fs.readdirSync(path.join(root,dir),{withFileTypes:true}).flatMap(e=>e.isSymbolicLink()?[]:e.isDirectory()?files(dir+'/'+e.name):[dir+'/'+e.name]);}
// Matching metadata is necessary, but never sufficient to qualify a question.
export function receiptIssues(manifest,manifestHash,check,attempt,sourcePinsMatch=true){
 const issues=[];const x=attempt.execution??{};
 if(attempt.manifestHash!==manifestHash)issues.push('manifest-mismatch');
 if(attempt.package!==manifest.id||String(attempt.revision)!==String(manifest.revision))issues.push('package-revision-mismatch');
 if(attempt.checkId!==check.id)issues.push('check-mismatch');
 if(attempt.status!=='passed'||attempt.observed!==check.expected)issues.push('unexpected-outcome');
 if(x.infrastructureError||x.signal||x.build!=='passed')issues.push('infrastructure-or-build');
 if(!Number.isInteger(x.exitCode)||(check.expected==='success'?x.exitCode!==0:x.exitCode===0))issues.push('process-outcome-mismatch');
 if(x.skippedTests!==0)issues.push('skipped-or-missing-count');
 if(JSON.stringify([...(x.executedTestIds??[])].sort())!==JSON.stringify([...(check.testIds??[])].sort()))issues.push('executed-tests-mismatch');
 if(JSON.stringify([...(x.failedTestIds??[])].sort())!==JSON.stringify([...(check.failureIds??[])].sort()))issues.push('failed-tests-mismatch');
 if(attempt.environment?.platform!==manifest.platform||attempt.environment?.deploymentTarget!==manifest.deploymentTarget)issues.push('target-mismatch');
 if(!attempt.environment?.sdkVersion||!attempt.environment?.compiler)issues.push('missing-toolchain');
 if(check.lane==='unit'&&!attempt.environment?.runtimeVersion)issues.push('missing-runtime');
 if(!sourcePinsMatch)issues.push('source-pins-mismatch');
 return issues;
}
const topicPatterns={semantics:/name|label|toggle|trait|selected|semantic/i,state:/stale|current|reuse|clear|request|callback|rebind|status/i,actions:/action|callback|dispatch|delete|disabled|handler/i,structure:/landmark|group|order|rotor|range|selection|document/i,text:/font|text|large|layout|scal|checkout/i,lifecycle:/dismiss|restor|session|cancel|reentrant|observer|teardown/i,media:/media|track|metadata|caption|audio|selection|player/i,testing:/./};
export function audit(){
 const inputPath=subjectBase+'evaluation/controller.json';const catalog=JSON.parse(read(inputPath));
 const receiptFiles=files('research/evaluation').filter(p=>p.endsWith('/results-index.json'));
 const receipts=receiptFiles.flatMap(p=>{const bytes=read(p);return (JSON.parse(bytes).attempts??[]).map(a=>({path:p,sha256:hash(bytes),attempt:a}));});
 // Older UIKit receipts use package-local row records, not research indexes.
 for(const p of files('code-examples').filter(p=>/\/validation\/[^/]+\.json$/.test(p))){
  const bytes=read(p),d=JSON.parse(bytes);if(!d.manifestHash||!Array.isArray(d.rows))continue;
  const manifestPath=p.split('/validation/')[0]+'/manifest.json';
  if(!fs.existsSync(path.join(root,manifestPath)))continue;
  const m=JSON.parse(read(manifestPath));
  for(const a of d.rows)receipts.push({path:p,sha256:hash(bytes),attempt:{...a,attempt:a.check,checkId:a.check,manifestHash:d.manifestHash,package:m.id,revision:d.revision,originalResultHash:a.originalRecordHash}});
 }
 const rows=catalog.cases.map(c=>{
  const row={id:c.id,platform:c.platform,framework:c.framework,topic:c.topic,subject:c.subject,status:'draft-not-independently-qualified',sourceGap:c.controller.sourceGap??false,criteria:c.controller.criteria.map((text,index)=>({index,text,status:'requires-semantic-review',reason:'A text match or nearby unit does not establish this complete criterion.'})),sourceEvidence:[],checks:[],candidateTestLeads:[],blockers:['Independent prompt/oracle review pending','No paired candidate model outcome'],modelOutcome:'not-run'};
  if(c.controller.expectedRoute){const p=c.controller.expectedRoute,b=read(p);row.sourceEvidence.push({path:p,sha256:hash(b),appleLinks:[...b.toString().matchAll(/https:\/\/(?:developer|support|www)\.apple\.com\/[^\s)>]+/g)].map(m=>m[0]),freshness:'Existing local document; not reverified against live Apple documentation in this audit'});}
  if(row.sourceGap)row.blockers.push('Primary-source mapping missing');
  const mp=c.controller.exampleManifest;
  if(!mp){row.blockers.push('No exact executable contract bound');return row;}
  const bytes=read(mp),m=JSON.parse(bytes),mh=hash(bytes),folder=path.posix.dirname(mp);
  const sourcePins=(m.files??[]).map(f=>({path:folder+'/'+f.path,expected:f.sha256,actual:hash(read(folder+'/'+f.path))}));
  row.manifest={path:mp,sha256:mh,id:m.id,revision:m.revision,limitations:m.limitations,sourcePins};
  const sourcePinsMatch=sourcePins.every(p=>p.expected===p.actual);
  for(const check of m.checks){
   const matches=receipts.filter(r=>r.attempt.manifestHash===mh&&r.attempt.checkId===check.id);
   const attempts=matches.map(r=>({index:r.path,indexSha256:r.sha256,attempt:r.attempt.attempt,environment:r.attempt.environment,issues:receiptIssues(m,mh,check,r.attempt,sourcePinsMatch),executedTestIds:r.attempt.execution?.executedTestIds??[],originalResultHash:r.attempt.originalResultHash}));
   row.checks.push({id:check.id,lane:check.lane,expected:check.expected,matchingReceipts:attempts,status:attempts.some(a=>!a.issues.length)?'receipt-verified-contract-only':'matching-evidence-unavailable-or-invalid'});
   for(const id of check.testIds??[])if(topicPatterns[c.topic].test(id))row.candidateTestLeads.push({check:check.id,testId:id,relation:'Lexical lead only; requires assertion and criterion review'});
  }
  if(!row.checks.some(c=>c.status==='receipt-verified-contract-only'))row.blockers.push('No valid matching receipt in public research indexes');
  row.blockers.push('Exact criterion-to-assertion binding requires review');
  row.claims=m.claims??[];
  return row;
 });
 return {schema:1,status:'local-evidence-triage-not-gold-promotion',input:{path:inputPath,sha256:hash(read(inputPath))},scope:'Existing public receipts inspected; no native reruns, live source audit or model calls',rows,summary:{cases:rows.length,sourceGaps:rows.filter(r=>r.sourceGap).length,withManifest:rows.filter(r=>r.manifest).length,withValidContractReceipt:rows.filter(r=>r.checks.some(c=>c.status==='receipt-verified-contract-only')).length,qualifiedGold:0,modelCalls:0},limitations:['Receipt joins establish recorded contract execution only, not entire question coverage.','Lexical test leads do not qualify an assertion or API claim.','Research index hashes are reproducibility pins, not independent authentication of private native archives.','No generalization to untested versions or accessibility interaction outcomes.']};
}
if(process.argv[1]&&path.resolve(process.argv[1])===fileURLToPath(import.meta.url))console.log(JSON.stringify(audit(),null,2));

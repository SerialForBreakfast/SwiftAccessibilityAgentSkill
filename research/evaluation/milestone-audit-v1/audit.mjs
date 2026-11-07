// Author/controller audit of existing sealed messages; no generation or native execution.
import fs from 'node:fs';import path from 'node:path';import {fileURLToPath} from 'node:url';import {createHash} from 'node:crypto';
const root=fileURLToPath(new URL('../../../',import.meta.url));
const sealed='research/evaluation/milestone-package-v1/';
export const hash=b=>createHash('sha256').update(b).digest('hex');
const bytes=p=>fs.readFileSync(path.join(root,p));const read=p=>JSON.parse(bytes(p));
export function audit(){
 const m=read(sealed+'manifest.json'),rows=[],proposals=[];
 for(const c of m.cases){
  const files=c.plans.map(p=>({plan:p,payload:read(sealed+p.path)}));const before=JSON.parse(files[0].payload.messages[1].content),after=JSON.parse(files[1].payload.messages[1].content);
  const findings=[];const references=after.suppliedReferences.map(r=>{
   const platforms=r.content.match(/^- Platforms:\s*(.+)$/m)?.[1]?.split(',').map(s=>s.trim())??null;
   const undeclared=platforms!==null&&!platforms.includes(c.platform);
   if(undeclared)findings.push({id:'declared-platform-scope',severity:'review-warning',reference:r.path,observation:'Requested '+c.platform+'; reference declares '+platforms.join(', '),effect:'Metadata mismatch is not proof of API unavailability. Review exact claims/declarations before treating this as target-specific support.'});
   if(c.id==='macos-appkit-testing'&&r.path.endsWith('m-010-testing-workflow.md'))findings.push({id:'mandatory-manual-policy-conflict',severity:'revision-required',reference:r.path,quote:r.content.split('\n').find(l=>l.startsWith('Every significant macOS UI change must pass')),effect:'Source workflow conflicts with the requested unit-only scope. Higher-priority candidate instructions may resist it, but source selection is a repairable context defect.'});
   if(c.id==='tvos-swiftui-testing'&&r.path.endsWith('g-014-lists-forms-complex-rows.md'))findings.push({id:'wrong-topic-reference',severity:'revision-required',reference:r.path,quote:r.content.split('\n')[0],effect:'Lists/forms guidance is not the requested compile/unit evidence workflow.'});
   const future=r.content.includes('## OS 27');
   if(future)findings.push({id:'future-os-context',severity:'context-review',reference:r.path,effect:'Deployment26 question receives an OS27 addendum. Do not assume the later feature is available or delete valid version-boundary guidance automatically.'});
   return {path:r.path,sha256:hash(r.content),bytes:Buffer.byteLength(r.content),declaredPlatforms:platforms,outOfDeclaredScope:undeclared,futureOsAddendum:future};
  });
  if(before.request!==after.request)throw Error('Unequal paired request');
  if(findings.some(f=>f.severity==='revision-required')){
   const patched=structuredClone(files[1].payload),user=JSON.parse(patched.messages[1].content);
   const keep=user.suppliedReferences.filter(r=>r.path==='references/tasks/testing.md');if(keep.length!==1)throw Error('Expected single existing testing note');user.suppliedReferences=keep;patched.messages[1].content=JSON.stringify(user);
   const output=JSON.stringify(patched,null,2)+'\n';
   proposals.push({caseId:c.id,originalPath:sealed+c.plans[1].path,originalSha256:c.plans[1].sha256,proposedPath:'proposals/'+c.id+'.json',proposedPayload:output,proposedSha256:hash(output),beforeBytes:c.plans[1].bytes,afterBytes:Buffer.byteLength(output),keptReferences:keep.map(r=>r.path),contextProfile:'C2-project-policy-only',scope:'Reference-selection repair proposal, not a frozen new candidate or model-evaluated improvement',independentlyApproved:false,liveRunsAuthorized:false});
  }
  rows.push({id:c.id,platform:c.platform,framework:c.framework,topic:c.topic,subjectSha256:c.subjectSha256,pairedRequestEqual:true,promptInputs:'Design/debugging request with no hidden project source promised',references,findings,status:findings.some(f=>f.severity==='revision-required')?'reference-revision-required':findings.some(f=>f.id==='declared-platform-scope')?'platform-applicability-review':'author-pre-review-complete-not-independent',independentAcceptance:false});
 }
 return {schema:1,reviewKind:'local-author-pre-review-not-independent',input:{path:sealed+'manifest.json',sha256:hash(bytes(sealed+'manifest.json'))},rows,proposals,summary:{cases:rows.length,requiredReferenceRepairs:proposals.length,platformScopeWarningCases:rows.filter(r=>r.findings.some(f=>f.id==='declared-platform-scope')).length,futureOsAddendumCases:rows.filter(r=>r.findings.some(f=>f.id==='future-os-context')).length,independentlyAccepted:0,modelCalls:0,newNativeRuns:0},limits:['Source mismatch is an observed input issue, not a model failure or evidence of an unavailable API.','The original package and candidate instructions remain unchanged. Proposed references require new package revision and independent review.','Project testing policy is not Apple platform/API evidence. No primary-source gap is silently resolved.']};
}
if(process.argv[1]&&path.resolve(process.argv[1])===fileURLToPath(import.meta.url))console.log(JSON.stringify(audit(),null,2));

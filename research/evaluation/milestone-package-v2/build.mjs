// Offline v2 revision. Original messages and candidate snapshots remain read-only.
import fs from 'node:fs';import path from 'node:path';import {fileURLToPath} from 'node:url';import {createHash} from 'node:crypto';
const root=fileURLToPath(new URL('../../../',import.meta.url)),base='research/evaluation/milestone-package-v2/',prior='research/evaluation/milestone-package-v1/';
export const hash=b=>createHash('sha256').update(b).digest('hex');const bytes=p=>fs.readFileSync(path.join(root,p)),read=p=>JSON.parse(bytes(p));
const profiles={
 'macos-swiftui-state':{name:'macos-values',records:['macos-value'],description:'Value-description modifier availability on macOS; application update/ownership policy remains separate.'},
 'macos-swiftui-text':{name:'macos-text-sizing',records:['macos-dynamic-size','macos-scaled-metric'],description:'Explicit DynamicTypeSize environment and ScaledMetric declarations on macOS. These declarations do not establish a system settings source or automatic settings propagation; that integration is application-dependent.'},
 'macos-swiftui-lifecycle':{name:'macos-focus-requests',records:['macos-focus'],description:'Focus-state modifier availability on macOS; requests are not proof that focus was delivered.'},
 'tvos-swiftui-actions':{name:'tvos-actions',records:['tvos-action'],description:'Named action modifier availability on tvOS; activation and current application state are separate behavioral contracts.'},
 'tvos-swiftui-structure':{name:'tvos-children',records:['tvos-children'],description:'Child-behavior modifier availability on tvOS; generated hierarchy and actual navigation require separate evidence.'}
};
export function build(){
 const original=read(prior+'manifest.json'),sdk=read(base+'sdk-evidence.json'),audit=read('research/evaluation/milestone-audit-v1/audit.json'),leads=read('research/evaluation/milestone-audit-v1/platform-evidence-leads.json');
 for(const pin of read(prior+'checkpoint.json').pins)if(hash(bytes(pin.path))!==pin.sha256)throw Error('Original package drift');
 const files={},cards={},resolutions=[];
 for(const [id,profile] of Object.entries(profiles)){
  const c=original.cases.find(c=>c.id===id);const declarations=profile.records.map(id=>{const r=sdk.records.find(r=>r.id===id);if(!r)throw Error('Missing declaration');if(r.platform!==c.platform||r.deploymentTarget!=='26.0'||r.declaredSupportedAtTarget!==true)throw Error('Target mismatch');return r;});
  const lines=['# SwiftUI '+profile.name,'','## Platforms','',c.platform+'; deployment target 26.0. Source: installed public SDK27 declarations.','',profile.description,'','## Declared APIs',''];
  for(const r of declarations)lines.push('- '+r.api+': SDK @available annotation includes '+r.platform+' '+r.version+'.','','```text',r.excerpt,'```','','Source: '+r.module+'/'+path.basename(r.file)+':'+r.line+'; full-interface SHA256 '+r.fileSha256+'.','');
  lines.push('## Evidence scope','','These are declaration/availability excerpts, not application snippets. Module migration annotations are not introduction dates. API availability does not establish rendered layout, generated semantics, automatic environment propagation, spoken output or delivered focus.','');
  const p='references/scoped-sdk/'+profile.name+'.md',content=lines.join('\n');files['reference-cards/'+profile.name+'.md']=content;cards[id]={path:p,content,sha256:hash(content)};
  const lead=leads.rows.find(l=>l.id===id);if(!lead)throw Error('Missing target compile lead');const m=read(lead.manifest.path);
  if(hash(bytes(lead.manifest.path))!==lead.manifest.sha256||lead.compile.environment.platform!==c.platform||lead.compile.environment.deploymentTarget!=='26.0'||hash(bytes(lead.compile.index))!==lead.compile.sha256)throw Error('Compile evidence mismatch');
  for(const f of lead.manifest.sourcePins)if(hash(bytes(f.path))!==f.sha256)throw Error('Native source changed');
  resolutions.push({id,oldReference:audit.rows.find(r=>r.id===id).references.find(r=>r.outOfDeclaredScope).path,resolution:'replace-ios-only-guide-with-target-sdk-card',declaredPlatforms:[c.platform],declarationIds:profile.records,compileEvidence:{manifest:lead.manifest,index:lead.compile.index,indexSha256:lead.compile.sha256,attempt:lead.compile.attempt,environment:lead.compile.environment,limitations:m.limitations},supportedScope:'Declared API availability and recorded composition compilation only',behaviorClaims:'Not broadened; no automatic text-setting propagation, generated-tree, speech or focus-delivery guarantee',independentlyAccepted:false});
 }
 const updated=structuredClone(original),changes=[];
 for(const c of updated.cases)for(const p of c.plans){
  const old=bytes(prior+p.path);if(hash(old)!==p.sha256)throw Error('Original payload drift');let output=old.toString();
  if(p.arm==='candidate-controlled'){
   const proposal=audit.proposals.find(q=>q.caseId===c.id);
   if(proposal){output=bytes('research/evaluation/milestone-audit-v1/'+proposal.proposedPath).toString();if(hash(output)!==proposal.proposedSha256)throw Error('Correction proposal drift');p.condition='C2-project-policy-only';resolutions.push({id:c.id,resolution:c.id==='tvos-swiftui-testing'?'replace-wrong-topic-ios-guide-with-project-testing-note':'remove-mandatory-manual-workflow-from-unit-only-context',supportedScope:'Project compile/unit evidence policy, not Apple interaction-validation requirements',independentlyAccepted:false});}
   else if(cards[c.id]){const payload=JSON.parse(output),user=JSON.parse(payload.messages[1].content);const note=user.suppliedReferences.filter(r=>r.path.startsWith('references/tasks/'));if(note.length!==1)throw Error('Expected one task note');const {path,content}=cards[c.id];user.suppliedReferences=[...note,{path,content}];payload.messages[1].content=JSON.stringify(user);output=JSON.stringify(payload,null,2)+'\n';p.condition='C2-sdk-scoped';}
  }
  const payload=JSON.parse(output),user=JSON.parse(payload.messages[1].content);p.suppliedReferences=user.suppliedReferences.map(r=>({path:r.path,sha256:hash(r.content)}));
  if(output!==old.toString())changes.push({caseId:c.id,arm:p.arm,path:p.path,originalSha256:p.sha256,beforeBytes:p.bytes,afterBytes:Buffer.byteLength(output),condition:p.condition});
  p.sha256=hash(output);p.bytes=Buffer.byteLength(output);p.tokens=null;p.readTraceClaim='Controlled supplied reference content; no model/tool read trace exists';files[p.path]=output;
 }
 updated.id='controlled-skill-lift-milestone-2';updated.status='author-scoped-platform-resolution-independent-review-pending';updated.preparationBaseCommit='760554c';updated.authorization.id=updated.id;updated.authorization.status='v2-author-scoped-independent-review-pending';updated.contextRevision='policy-and-target-sdk-v2';
 updated.inputs=[...original.inputs,{path:prior+'manifest.json',sha256:hash(bytes(prior+'manifest.json'))},{path:base+'sdk-evidence.json',sha256:hash(bytes(base+'sdk-evidence.json'))},{path:'research/evaluation/milestone-audit-v1/audit.json',sha256:hash(bytes('research/evaluation/milestone-audit-v1/audit.json'))}];
 updated.sourceResolutions=resolutions;updated.changes=changes;updated.authorReview={requiredReferenceRepairsApplied:2,originalPlatformScopeWarnings:6,platformScopeQuestionsAddressed:6,remainingInheritedScopeWarnings:0,platformBehaviorVerified:false,independentAcceptance:false,remainingContextFlags:['Two existing OS27 media addenda require version-aware interpretation; no deployment26 availability inferred.'],primaryMappingQuarantinesPreserved:3};
 return {manifest:updated,files};
}
export function preflight(manifest,loader=p=>bytes(base+p)){
 const errors=[];let expected;try{expected=build();if(JSON.stringify(expected.manifest)!==JSON.stringify(manifest))errors.push('manifest-or-input-drift');}catch{errors.push('source-or-evidence-invalid');}
 if(expected)for(const [p,text] of Object.entries(expected.files)){try{if(hash(loader(p))!==hash(text))errors.push('artifact-drift:'+p);}catch{errors.push('missing-artifact:'+p);}}
 return {schema:1,integrityPassed:errors.length===0,integrityErrors:errors,authorScopeResolution:'API annotations and existing compilation, not runtime interaction',independentAcceptance:false,liveRunsAuthorized:false,modelCalls:0,blockers:['independent-oracle-and-source-review','actual-clean-harness-isolation','provider-and-model-identity','explicit-quota-output-total-token-and-time-limits','owner-run-authorization']};
}
if(process.argv[1]&&path.resolve(process.argv[1])===fileURLToPath(import.meta.url)){
 const [mode,...extra]=process.argv.slice(2);if(extra.length||!['build','check'].includes(mode))throw Error('Usage: build.mjs build|check (offline only)');
 if(mode==='build'){if(fs.existsSync(path.join(root,base+'manifest.json')))throw Error('Refusing to overwrite sealed v2');const {manifest,files}=build();for(const [p,s] of Object.entries(files)){const full=path.join(root,base+p);fs.mkdirSync(path.dirname(full),{recursive:true});fs.writeFileSync(full,s,{flag:'wx'});}fs.writeFileSync(path.join(root,base+'manifest.json'),JSON.stringify(manifest,null,2)+'\n',{flag:'wx'});console.log(JSON.stringify({cells:48,changedCells:manifest.changes.length,referenceCorrections:2,scopeQuestionsAddressed:6,modelCalls:0},null,2));}
 else{const result=preflight(read(base+'manifest.json'));console.log(JSON.stringify(result,null,2));if(!result.integrityPassed)process.exitCode=1;}
}

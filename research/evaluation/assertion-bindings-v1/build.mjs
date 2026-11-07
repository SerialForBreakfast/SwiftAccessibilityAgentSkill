// Controller-only binding builder: explicit selection + syntax spans + exact historical receipts.
import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {spawnSync} from 'node:child_process';
import {createHash} from 'node:crypto';
import {receiptIssues} from '../local-qualification-v1/audit.mjs';
import {selections} from './spec.mjs';
const root=fileURLToPath(new URL('../../../',import.meta.url));
const base='research/evaluation/assertion-bindings-v1/';
const input='research/evaluation/failure-driven/candidates/0.3.0-dev.5/evaluation/controller.json';
export const hash=b=>createHash('sha256').update(b).digest('hex');
const bytes=p=>fs.readFileSync(path.join(root,p)),read=p=>JSON.parse(bytes(p));
function files(dir){return fs.readdirSync(path.join(root,dir),{withFileTypes:true}).flatMap(e=>e.isSymbolicLink()?[]:e.isDirectory()?files(dir+'/'+e.name):[dir+'/'+e.name]);}
export function collectReceipts(){
 const receipts=[];
 for(const p of files('research/evaluation').filter(p=>p.endsWith('/results-index.json'))){const d=read(p);for(const a of d.attempts??[])receipts.push({path:p,sha256:hash(bytes(p)),attempt:a});}
 for(const p of files('code-examples').filter(p=>/\/validation\/[^/]+\.json$/.test(p))){const d=read(p);if(!d.manifestHash||!Array.isArray(d.rows))continue;const mp=p.split('/validation/')[0]+'/manifest.json';if(!fs.existsSync(path.join(root,mp)))continue;const m=read(mp);for(const a of d.rows)receipts.push({path:p,sha256:hash(bytes(p)),attempt:{...a,attempt:a.check,checkId:a.check,manifestHash:d.manifestHash,package:m.id,revision:d.revision,originalResultHash:a.originalRecordHash}});}
 return receipts;
}
export function selectReceipt(m,mh,testId,receipts,sourcePinsMatch){
 const checks=m.checks.filter(c=>c.lane==='unit'&&c.expected==='success'&&c.testIds.includes(testId));
 for(const check of checks)for(const r of receipts)if(!receiptIssues(m,mh,check,r.attempt,sourcePinsMatch).length)return {check,r};
 return null;
}
export function verifySpans(source,method){
 if(!Number.isInteger(method.startByte)||!Number.isInteger(method.endByte)||method.startByte<0||method.endByte>source.length||method.endByte<=method.startByte)throw Error('Invalid method byte range');
 for(const a of method.assertionSites){
  if(a.startByte<method.startByte||a.endByte>method.endByte||a.endByte<=a.startByte)throw Error('Assertion outside method');
  if(source.subarray(a.startByte,a.endByte).toString()!==a.expression)throw Error('Assertion source range drift');
 }
}
export function build(){
 const cases=read(input).cases,selected=new Map(cases.map(c=>[c.id,selections(c)]));
 const manifests=[...new Set([...selected.values()].flatMap(m=>Object.values(m).flat().map(b=>b.manifest)))];
 const testFiles=[...new Set(manifests.flatMap(mp=>read(mp).files.filter(f=>/\bTests\/.+\.swift$/.test(f.path)).map(f=>path.posix.join(path.posix.dirname(mp),f.path))))].sort();
 const command='tools/local-analysis/.cache/syntax-probe';
 const p=spawnSync(path.join(root,command),testFiles,{cwd:root,encoding:'utf8',maxBuffer:30*1024*1024,timeout:120000});
 if(p.status!==0)throw Error('Syntax extraction failed: '+p.stderr);
 const syntax=JSON.parse(p.stdout);if(syntax.some(s=>s.hasParserError))throw Error('Parser error in selected assertions');
 const receipts=collectReceipts(),contracts={},issues=[];
 function contract(mp,testId,platform){
  const id=mp+'#'+testId;if(contracts[id])return id;
  const m=read(mp),mh=hash(bytes(mp)),folder=path.posix.dirname(mp);
  if(m.platform!==platform)throw Error('Cross-platform evidence prohibited');
  const pins=m.files.map(f=>({path:path.posix.join(folder,f.path),sha256:f.sha256}));
  const sourcePinsMatch=pins.every(f=>hash(bytes(f.path))===f.sha256);
  const [owner,name]=testId.split('/');
  const methods=syntax.filter(s=>m.files.some(f=>path.posix.join(folder,f.path)===s.path)).flatMap(s=>s.functions.filter(f=>f.ownerType===owner&&f.name===name).map(f=>({file:s.path,method:f})));
  if(methods.length!==1)throw Error('Expected one syntax declaration for '+id+', got '+methods.length);
  const {file,method}=methods[0],source=bytes(file);verifySpans(source,method);
  if(!method.assertionSites.length)throw Error('No direct assertion sites: '+id);
  const match=selectReceipt(m,mh,testId,receipts,sourcePinsMatch);
  if(!match){issues.push({id,reason:'No exact current-manifest successful unit receipt'});return null;}
  contracts[id]={id,manifest:mp,manifestSha256:mh,sourcePins:pins,testId,file,fileSha256:hash(source),line:method.line,startByte:method.startByte,endByte:method.endByte,methodSha256:hash(source.subarray(method.startByte,method.endByte)),methodSource:source.subarray(method.startByte,method.endByte).toString(),assertions:method.assertionSites.map(a=>({...a,sha256:hash(source.subarray(a.startByte,a.endByte))})),receipt:{index:match.r.path,indexSha256:match.r.sha256,attempt:match.r.attempt.attempt,check:match.check.id,originalResultHash:match.r.attempt.originalResultHash,environment:match.r.attempt.environment},sourceClaims:m.claims,limitations:m.limitations,executionScope:'Enclosing method executed. Individual assertion/closure/conditional branch execution is not separately instrumented.'};
  contracts[id].negativeControls=m.checks.filter(c=>c.expected==='failure'&&c.failureIds?.includes(testId)).flatMap(check=>receipts.filter(r=>!receiptIssues(m,mh,check,r.attempt,sourcePinsMatch).length).map(r=>({check:check.id,index:r.path,indexSha256:r.sha256,attempt:r.attempt.attempt,failureIds:check.failureIds,scope:'Recorded deliberate rejection for this test ID; no new mutant execution.'})));
  return id;
 }
 const rows=cases.map(c=>({id:c.id,platform:c.platform,framework:c.framework,topic:c.topic,subject:c.subject,status:'author-bound-not-independently-qualified',acceptedAlternatives:c.controller.acceptedAlternatives,sourceGap:c.controller.sourceGap??false,criteria:c.controller.criteria.map((text,index)=>{
  const bindings=(selected.get(c.id)[index]??[]).map(s=>({...s,contractIds:s.testIds.map(id=>contract(s.manifest,id,c.platform)).filter(Boolean)}));
  return {index,text,disposition:bindings.some(b=>b.contractIds.length)?'unit-subset-bound':c.topic==='testing'||!c.controller.note?'answer-protocol-or-source-review':'unit-evidence-not-bound',bindings,remaining:bindings.length?'Narrow observations only. Entire criterion, API applicability and answer quality still need review.':'No suitable direct unit assertion selected. Preserve this gap rather than substituting an unrelated passing test.'};
 }),modelOutcome:'not-run',qualification:'Independent rubric review and paired evaluation pending'}));
 return {schema:1,input:{path:input,sha256:hash(bytes(input))},tool:{source:'tools/local-analysis/SyntaxProbe.swift',sha256:hash(bytes('tools/local-analysis/SyntaxProbe.swift')),binarySha256:hash(bytes(command))},selection:{path:base+'spec.mjs',sha256:hash(bytes(base+'spec.mjs'))},rows,contracts,issues,summary:{cases:rows.length,criteria:rows.reduce((n,r)=>n+r.criteria.length,0),criteriaWithUnitSubset:rows.reduce((n,r)=>n+r.criteria.filter(c=>c.disposition==='unit-subset-bound').length,0),casesWithUnitSubset:rows.filter(r=>r.criteria.some(c=>c.disposition==='unit-subset-bound')).length,uniqueMethods:Object.keys(contracts).length,assertionSites:Object.values(contracts).reduce((n,c)=>n+c.assertions.length,0),missingExecutionBindings:issues.length,qualifiedGold:0,modelCalls:0,nativeRuns:0},limits:['Assertions are syntax-bound and enclosing methods have matching recorded executions; per-site execution is not inferred.','A narrow unit observation does not prove the whole rubric, platform defaults, rendered semantics or model-answer correctness.','Source links come from existing manifests; no live Apple source refresh or availability promotion performed.','Related platform variants remain related development families, not independent holdouts.']};
}
if(process.argv[1]&&path.resolve(process.argv[1])===fileURLToPath(import.meta.url)){
 const result=build();console.log(JSON.stringify(result,null,2));
}

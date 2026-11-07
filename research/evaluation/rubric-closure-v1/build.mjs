import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {spawnSync} from 'node:child_process';
import {topicRules,controlRules,caseAlternatives} from './rules.mjs';
import {hash,selectReceipt,verifySpans} from '../assertion-bindings-v1/build.mjs';
const root=fileURLToPath(new URL('../../../',import.meta.url));
const base='research/evaluation/rubric-closure-v1/';
const input='research/evaluation/failure-driven/candidates/0.3.0-dev.5/evaluation/controller.json';
const prior='research/evaluation/assertion-bindings-v1/bindings.json';
const read=p=>fs.readFileSync(path.join(root,p)),json=p=>JSON.parse(read(p));
export function anchor(p,needle,max=800){const raw=read(p),text=raw.toString(),start=text.indexOf(needle);if(start<0)throw Error('Missing source section '+p+' '+needle);let end=text.indexOf(needle.startsWith('## ')?'\n## ':'\n',start+needle.length);if(end<0)end=text.length;end=Math.min(end,start+max);return {path:p,sha256:hash(raw),startUTF16:start,endUTF16:end,quote:text.slice(start,end),line:text.slice(0,start).split('\n').length,scope:'Existing local evidence / project grading rationale; not a fresh Apple source verification'};}
export function supplementalCheckout(){
 const mp='research/evaluation/failure-driven/checkout-contract-v1/manifest.json',folder=path.posix.dirname(mp),raw=read(mp),m=JSON.parse(raw),mh=hash(raw),vp=folder+'/validation.json',v=json(vp);
 const receipts=v.rows.map(a=>({path:vp,sha256:hash(read(vp)),attempt:{...a,package:m.id,checkId:a.check,attempt:a.check+'-r'+a.revision,originalResultHash:a.originalRecordHash}}));
 const pins=m.files.map(f=>({path:path.posix.join(folder,f.path),sha256:f.sha256}));const valid=pins.every(p=>hash(read(p.path))===p.sha256);
 const file=folder+'/Tests/CheckoutSummaryTests.swift',process=spawnSync(path.join(root,'tools/local-analysis/.cache/syntax-probe'),[file],{cwd:root,encoding:'utf8',timeout:30000});
 if(process.status!==0)throw Error('Checkout syntax probe failed');const parsed=JSON.parse(process.stdout)[0];if(parsed.hasParserError)throw Error('Checkout parser error');
 return ['testPreservesExistingButtonIdentityTypographyAndTitle','testRepeatedUpdatesPreserveExistingActionExactlyOnce','testFlexibleTextConfigurationAndNoFixedEnclosingHeight'].map(name=>{
  const method=parsed.functions.find(f=>f.ownerType==='CheckoutSummaryTests'&&f.name===name);if(!method)throw Error('Missing checkout method');const source=read(file);verifySpans(source,method);
  const id=method.ownerType+'/'+method.name,receipt=selectReceipt(m,mh,id,receipts,valid);if(!receipt)throw Error('Missing exact successful checkout execution');
  return {id:mp+'#'+id,manifest:mp,manifestSha256:mh,sourcePins:pins,testId:id,file,fileSha256:hash(source),method,methodSha256:hash(source.subarray(method.startByte,method.endByte)),receipt:{path:receipt.r.path,sha256:receipt.r.sha256,attempt:receipt.r.attempt.attempt,originalResultHash:receipt.r.attempt.originalResultHash,environment:receipt.r.attempt.environment},claimScope:'Existing native UIKit checkout fixture only; original model answers were not altered or executed',sourceClaims:m.claims};
 });
}
const policies={
 semantics:['FR-03 Neutral questions','FR-02 Trustworthy oracle'],state:['FR-01 Traceable pairs','FR-07 Version specificity'],actions:['FR-02 Trustworthy oracle','FR-10 Feature completion'],structure:['NFR-04 Maintainability','FR-07 Version specificity'],text:['FR-02 Trustworthy oracle','FR-07 Version specificity'],lifecycle:['FR-07 Version specificity','FR-02 Trustworthy oracle'],media:['FR-07 Version specificity','FR-02 Trustworthy oracle'],testing:['FR-06 Honest outcomes','NFR-04 Maintainability']
};
export function build(){
 const catalog=json(input),old=json(prior),supplement=supplementalCheckout();
 const rows=catalog.cases.map(c=>{const previous=old.rows.find(r=>r.id===c.id),control=!c.controller.note,rs=control?controlRules(c):topicRules[c.topic];if(rs.length!==previous.criteria.length)throw Error('Criterion count mismatch');
 const sources=(policies[c.topic]??policies.testing).map(n=>anchor('research/evaluation/failure-driven/PRD.md','| '+n));
 if(c.controller.expectedRoute)sources.push(anchor(c.controller.expectedRoute,'## Rule'));
 if(c.topic==='testing'||control)sources.push(anchor('research/evaluation/failure-driven/PRD.md','| FR-04 Independent evaluation'));
 return {id:c.id,platform:c.platform,framework:c.framework,topic:c.topic,subject:c.subject,cohort:c.cohort,status:'author-operationalized-independent-review-pending',originalAlternatives:c.controller.acceptedAlternatives,acceptedAlternatives:caseAlternatives(c),alternativeChange:control?'Removed irrelevant generic no-change alternative; accepted paths now match this control.':'Original alternatives retained.',sources,sourceGap:c.controller.sourceGap??false,criteria:rs.map((r,index)=>({id:c.id+'/criterion-'+index,index,originalText:previous.criteria[index].text,...r,evidenceReview:'semantic decision by independent reviewer; deterministic checks validate provenance, not meaning',priorDisposition:previous.criteria[index].disposition,priorContractIds:[...new Set(previous.criteria[index].bindings.flatMap(b=>b.contractIds))],supplementalContractIds:c.id==='ios-uikit-text'?(index===0?[supplement[2].id]:index===1?supplement.slice(0,2).map(s=>s.id):[]):[],scope:previous.criteria[index].remaining})),answerStatus:'not-run',independentAcceptance:false};
 });
 return {schema:1,rubricRevision:'operational-1',comparability:'New controller revision: historical grades unchanged. Rescore both matched conditions with the same revision before comparison.',status:'grading-specification-complete-not-gold-qualified',inputs:[input,prior].map(p=>({path:p,sha256:hash(read(p))})),supplementalContracts:supplement,rows,summary:{cases:rows.length,criteria:rows.reduce((n,r)=>n+r.criteria.length,0),previouslyUnboundCriteriaSpecified:old.rows.flatMap(r=>r.criteria).filter(c=>c.disposition!=='unit-subset-bound').length,controlsWithTargetedAlternatives:rows.filter(r=>r.alternativeChange.startsWith('Removed')).length,additionalExecutedMethodsLinked:supplement.length,primarySourceGaps:rows.filter(r=>r.sourceGap).length,independentlyQualified:0,realAnswersGraded:0,modelCalls:0,newNativeRuns:0},boundaries:['A complete grading specification is not complete accessibility coverage.','Legacy fixture evidence does not grade a new answer or transfer defaults across frameworks.','All 198 criteria still require semantic review of actual captured answers; no substring grader claims general correctness.','Three primary-source mappings remain unresolved; no new API availability claim is inferred.']};
}
if(process.argv[1]&&path.resolve(process.argv[1])===fileURLToPath(import.meta.url))console.log(JSON.stringify(build(),null,2));

// Forward-use guards. Historical modules, grades and sealed payloads stay unchanged.
import {preflight} from '../milestone-package-v1/package.mjs';
import {comparePairs} from '../skill-lift-v1/compare.mjs';
const object=v=>v!==null&&typeof v==='object'&&!Array.isArray(v);
export function safePreflight(manifest,loader){
 const errors=[];
 if(!object(manifest)||!Array.isArray(manifest.cases)||!object(manifest.authorization)||!object(manifest.summary))errors.push('invalid-root-shape');
 else{
  for(const c of manifest.cases){
   if(!object(c)||typeof c.id!=='string'||!Array.isArray(c.plans)||c.plans.length!==2){errors.push('invalid-case-shape');continue;}
   for(const p of c.plans){if(!object(p)||typeof p.path!=='string'||!p.path.startsWith('payloads/')||p.path.includes('\\')||p.path.split('/').includes('..')||!Number.isSafeInteger(p.bytes)||p.bytes<=0||!/^[a-f0-9]{64}$/.test(p.sha256??''))errors.push('invalid-payload-descriptor');}
  }
  for(const k of ['independentReview','sourceApplicabilityReview','harnessIsolationAttested','liveAuthorization'])if(typeof manifest.authorization[k]!=='boolean')errors.push('invalid-review-flag:'+k);
  if(!Number.isSafeInteger(manifest.authorization.approvedCalls)||manifest.authorization.approvedCalls<0)errors.push('invalid-call-budget');
  if(!Number.isSafeInteger(manifest.authorization.maxInputBytes)||manifest.authorization.maxInputBytes<=0)errors.push('invalid-input-limit');
  for(const k of ['maxOutputTokens','totalTokenCeiling','deadlineSeconds'])if(manifest.authorization[k]!==null&&(!Number.isSafeInteger(manifest.authorization[k])||manifest.authorization[k]<=0))errors.push('invalid-limit:'+k);
  if(!Number.isSafeInteger(manifest.summary.cells)||manifest.summary.cells!==manifest.cases.reduce((n,c)=>n+(Array.isArray(c?.plans)?c.plans.length:0),0))errors.push('cell-count-mismatch');
 }
 if(errors.length)return {integrityPassed:false,integrityErrors:[...new Set(errors)],blockers:['malformed-package'],liveRunsAuthorized:false,modelCalls:0};
 try{return preflight(manifest,loader);}catch{return {integrityPassed:false,integrityErrors:['unhandled-legacy-preflight-error'],blockers:['invalid-package'],liveRunsAuthorized:false,modelCalls:0};}
}
// Model tags and human-readable "not recorded" labels are not pinned identities.
const unavailable=/^unknown\b|\bunavailable\b|\bnot\s+(?:independently\s+)?(?:exposed|recorded|known|provided|verified)\b|\brequested\s+only\b|(?:^|:)latest$/i;
export function guardedCompare(pairs){
 const copy=structuredClone(pairs),rejections=[];
 for(const p of copy)for(const arm of ['before','after'])for(const k of ['modelRevision','environmentFingerprint','samplingFingerprint','tokenConvention']){
  const value=p[arm]?.[k];if(typeof value==='string'&&unavailable.test(value.replace(/[_-]+/g,' '))){rejections.push({pair:p.id,arm,field:k,reason:'Identity/accounting explicitly unverified'});p[arm][k]=null;}
 }
 const result=comparePairs(copy);return {...result,guardRejections:rejections,scope:'Identity guard plus legacy arithmetic. This is not origin authentication or a regrading of historical reports.'};
}

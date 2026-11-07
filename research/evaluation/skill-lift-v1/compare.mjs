// Pure offline comparisons. No provider, evaluation runner or source-code execution.
export function transition(before,after){
 const allowed=['pass','fail','inconclusive','missing'];
 if(!allowed.includes(before)||!allowed.includes(after))throw Error('Unknown outcome');
 if(before==='missing'||after==='missing')return 'missing';
 if(before==='inconclusive'||after==='inconclusive')return 'inconclusive';
 return before==='pass'?(after==='pass'?'preserved':'regression'):(after==='pass'?'gain':'persistent-failure');
}
const exactKeys=['scenarioId','scenarioFamily','platform','framework','topic','taskClass','subjectSha256','modelRevision','harnessSha256','rubricSha256','environmentFingerprint','samplingFingerprint','tokenConvention'];
const hashKeys=['subjectSha256','harnessSha256','rubricSha256'];
const unknown=/^(unknown|unavailable|not-exposed|latest|unspecified)$|:latest$/i;
export function matchIssues(a,b){
 const errors=[];
 for(const k of exactKeys){
  if(typeof a[k]!=='string'||typeof b[k]!=='string'||!a[k].trim()||!b[k].trim()||unknown.test(a[k])||unknown.test(b[k]))errors.push('missing-'+k);
  else if(a[k]!==b[k])errors.push('mismatch-'+k);
  if(hashKeys.includes(k)&&(!/^[a-f0-9]{64}$/.test(a[k]??'')||!/^[a-f0-9]{64}$/.test(b[k]??'')))errors.push('invalid-'+k);
 }
 if(a.conditionId===b.conditionId)errors.push('identical-conditions');
 for(const r of [a,b]){
  if(typeof r.conditionId!=='string'||!r.conditionId.trim())errors.push('missing-condition');
  if(!['focused','broad'].includes(r.taskClass))errors.push('invalid-task-class');
  if(!['pass','fail','inconclusive','missing'].includes(r.outcome))errors.push('invalid-outcome');
  if(r.quality!==null&&(!Number.isFinite(r.quality)||r.quality<0||r.quality>1))errors.push('invalid-quality');
 }
 return [...new Set(errors)];
}
export function median(values){if(!values.length)return null;const s=[...values].sort((a,b)=>a-b),i=Math.floor(s.length/2);return s.length%2?s[i]:(s[i-1]+s[i])/2;}
// Repetitions/variants contribute within their family; families are the resampling unit.
export function familyInterval(rows,field='qualityDelta',iterations=2000){
 if(!Number.isSafeInteger(iterations)||iterations<100||iterations>100000)throw Error('Bootstrap iterations must be 100-100000');
 const groups=new Map();for(const r of rows){if(!Number.isFinite(r[field]))continue;const g=groups.get(r.family)??[];g.push(r[field]);groups.set(r.family,g);}
 const means=[...groups.values()].map(xs=>xs.reduce((a,b)=>a+b,0)/xs.length);
 if(means.length<2)return {families:means.length,mean:means.length?means[0]:null,interval95:null,reason:'At least two independent families needed; no precision claim from repeats alone'};
 let seed=1701;const random=()=>{seed=(Math.imul(seed,1664525)+1013904223)>>>0;return seed/4294967296;};
 const samples=[];for(let i=0;i<iterations;i++){let sum=0;for(let j=0;j<means.length;j++)sum+=means[Math.floor(random()*means.length)];samples.push(sum/means.length);}samples.sort((a,b)=>a-b);
 return {families:means.length,mean:means.reduce((a,b)=>a+b,0)/means.length,interval95:[samples[Math.floor(iterations*0.025)],samples[Math.floor(iterations*0.975)]],method:'Seeded percentile bootstrap over family means; not a guarantee of generalization'};
}
export function comparePairs(pairs){
 const ids=pairs.map(p=>p.id);if(ids.some(id=>typeof id!=='string'||!id)||new Set(ids).size!==ids.length)throw Error('Unique nonempty pair IDs required');
 const rows=pairs.map(({id,before,after})=>{
  const issues=matchIssues(before,after);
  const validTelemetry=v=>v===null||v===undefined||Number.isFinite(v)&&v>=0;
  const telemetryFields=['inputTokens','outputTokens','totalTokens','reasoningTokens','loadedReferenceBytes','toolCalls','latencyMs','costUSD'];
  if(telemetryFields.some(k=>!validTelemetry(before[k])||!validTelemetry(after[k])))issues.push('invalid-telemetry');
  const changes=Object.fromEntries(telemetryFields.map(k=>[k,Number.isFinite(before[k])&&before[k]>0&&Number.isFinite(after[k])?after[k]/before[k]-1:null]));
  const validCritical=r=>Array.isArray(r.criticalErrors)&&r.criticalErrors.every(x=>typeof x==='string'&&x.length>0);
  return {id,family:before.scenarioFamily,platform:before.platform,framework:before.framework,topic:before.topic,focused:before.taskClass==='focused',beforeOutcome:before.outcome,afterOutcome:after.outcome,issues,transition:issues.length?'unmatched':transition(before.outcome,after.outcome),qualityDelta:!issues.length&&Number.isFinite(before.quality)&&Number.isFinite(after.quality)?after.quality-before.quality:null,inputTokenChange:!issues.length?changes.inputTokens:null,telemetryChanges:issues.length?Object.fromEntries(telemetryFields.map(k=>[k,null])):changes,newCriticalErrors:!issues.length&&validCritical(before)&&validCritical(after)?after.criticalErrors.filter(x=>!before.criticalErrors.includes(x)):null};
 });
 const interval=familyInterval(rows.filter(r=>!r.issues.length));
 const focused=rows.filter(r=>!r.issues.length&&r.focused);
 const tokenPairs=focused.filter(r=>Number.isFinite(r.inputTokenChange)).length;
 const qualityComplete=rows.length>0&&rows.every(r=>!r.issues.length&&Number.isFinite(r.qualityDelta));
 const totalChanges=focused.map(r=>r.telemetryChanges.totalTokens).filter(Number.isFinite);
 return {rows,counts:Object.fromEntries(['gain','regression','preserved','persistent-failure','inconclusive','missing','unmatched'].map(k=>[k,rows.filter(r=>r.transition===k).length])),quality:interval,qualityEvidenceComplete:qualityComplete,focusedPairs:focused.length,tokenTelemetryPairs:tokenPairs,inputTelemetryComplete:focused.length>0&&tokenPairs===focused.length,totalTelemetryComplete:focused.length>0&&totalChanges.length===focused.length,medianTotalTokenChange:median(totalChanges),medianInputTokenChange:median(focused.map(r=>r.inputTokenChange).filter(Number.isFinite)),newCriticalErrors:rows.flatMap(r=>r.newCriticalErrors??[]),criticalEvidenceComplete:rows.length>0&&rows.every(r=>!r.issues.length&&r.newCriticalErrors!==null),scope:'Strict matched comparisons only. Descriptive historical transitions require separate qualification.'};
}
export function gates(result,{packagingPassed=null,independentReviewPassed=null,holdoutPassed=null,platformReviewPassed=null}={}){
 const issues=[];
 if(packagingPassed!==true)issues.push('packaging-unverified-or-failed');
 if(independentReviewPassed!==true)issues.push('independent-review-pending');
 if(holdoutPassed!==true)issues.push('heldout-review-pending');
 if(platformReviewPassed!==true)issues.push('platform-review-pending');
 if(!result.criticalEvidenceComplete)issues.push('critical-evidence-incomplete');
 if(result.newCriticalErrors.length)issues.push('new-critical-errors');
 if(result.rows.some(r=>['unmatched','missing','inconclusive'].includes(r.transition)))issues.push('unresolved-pairs');
 if(!result.quality.interval95||result.quality.interval95[0]<-0.02)issues.push('quality-noninferiority-not-established');
 if(!result.qualityEvidenceComplete)issues.push('quality-evidence-incomplete');
 return {releaseEligible:issues.length===0,reasons:issues,qualityImprovementSupported:issues.length===0&&result.quality.interval95[0]>0,focusedInputTokenTargetMet:result.inputTelemetryComplete?result.medianInputTokenChange<=-0.15:null,focusedInputSavingsSupported:issues.length===0&&result.inputTelemetryComplete&&result.medianInputTokenChange<=-0.15,efficiencyClaimSupported:issues.length===0&&result.inputTelemetryComplete&&result.medianInputTokenChange<=-0.15&&result.totalTelemetryComplete&&result.medianTotalTokenChange<=0,promotionAuthorized:false,liveRunsAuthorized:false,policy:'Quality is a predeclared 0-1 normalized rubric score; two-percentage-point margin. Broader token efficiency also requires measured total tokens not worsening. Monetary savings are not inferred. Flags require externally verified artifacts. Numeric eligibility never authorizes promotion or model runs.'};
}

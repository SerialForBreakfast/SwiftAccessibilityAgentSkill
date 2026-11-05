import fs from 'node:fs';import path from 'node:path';
import {repo,hash,readReference} from './lib.mjs';
export function rubricBundle(){return JSON.parse(fs.readFileSync(path.join(repo,'evals/rubrics.json')));}
export function buildEvidence(){
 const rubric=rubricBundle(),paths=[...new Set(Object.values(rubric.cases).flatMap(c=>c.referencePaths))].sort();
 return {reviewStatus:'Repository guidance evidence; adjudicate source gaps before final grading.',rubricHash:hash(fs.readFileSync(path.join(repo,'evals/rubrics.json'))),references:paths.map(p=>readReference(repo,p))};
}
export function contextScenario(s,os){
 if(!s.os.includes(os))throw Error('Unsupported OS context');
 const context=s.os_platform?`${s.os_platform} ${os}${['swiftui','uikit'].includes(s.platform)?' using '+(s.platform==='swiftui'?'SwiftUI':'UIKit'):''}`:null;
 return {...s,os:[os],turns:s.turns.map((t,i)=>i===0&&context?t+'\nDeployment context: '+context+'.':t)};
}
export function validateGrade(grade,rubric=rubricBundle()){
 if(grade?.status!=='graded')throw Error('Unadjudicated or ungradable answer');
 const dimensions=Object.keys(rubric.dimensions);
 if(!grade.dimensions||Object.keys(grade.dimensions).length!==dimensions.length)throw Error('Expected anchored dimension scores');
 for(const key of dimensions)if(!Number.isInteger(grade.dimensions[key])||grade.dimensions[key]<0||grade.dimensions[key]>4)throw Error('Dimension score must be 0..4');
 if(typeof grade.reason!=='string'||!grade.reason.trim()||!Array.isArray(grade.criticalErrors))throw Error('Missing grade rationale/errors');
 const seen=new Set();for(const e of grade.criticalErrors){if(!rubric.critical_categories[e.category]||!e.explanation?.trim()||!e.evidence?.trim()||!e.excerpt?.trim()||seen.has(e.category+'\0'+e.excerpt))throw Error('Critical error needs category, excerpt, evidence and explanation');seen.add(e.category+'\0'+e.excerpt);}
 return {quality:dimensions.reduce((n,k)=>n+grade.dimensions[k]/4*rubric.dimensions[k].weight,0),criticalErrors:grade.criticalErrors.length};
}
export function mergeGrades(mapping,grades){
 if(new Set(mapping.map(p=>p.id)).size!==mapping.length)throw Error('Duplicate mapping');
 const seen=new Set(),rows=[];
 for(const g of grades){if(seen.has(g.id))throw Error('Duplicate grade');seen.add(g.id);const pair=mapping.find(p=>p.id===g.id);if(!pair)throw Error('Unknown packet');if(!g.judge?.trim())throw Error('Missing judge identity');for(const side of ['A','B']){const v=g[side],scores=validateGrade(v);rows.push({...pair[side],...scores,dimensions:v.dimensions,criticalErrorDetails:v.criticalErrors,gradingReason:v.reason,judge:g.judge});}}
 if(seen.size!==mapping.length)throw Error('Missing grades');return rows;
}

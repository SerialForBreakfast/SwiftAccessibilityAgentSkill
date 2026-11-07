// Validates a reviewer's evidence record; does not infer the semantics of an answer.
import fs from 'node:fs';
import {createRequire} from 'node:module';
import {hash} from '../assertion-bindings-v1/build.mjs';
const require=createRequire(new URL('../../../tools/local-analysis/package.json',import.meta.url));
const Ajv=require('ajv');
const check=new Ajv({allErrors:true,strict:true}).compile(JSON.parse(fs.readFileSync(new URL('./review-schema.json',import.meta.url))));
function boundary(text,i){if(i<=0||i>=text.length)return true;const before=text.charCodeAt(i-1),after=text.charCodeAt(i);return !(before>=0xD800&&before<=0xDBFF&&after>=0xDC00&&after<=0xDFFF);}
export function validateReview(record,corpus){
 if(!check(record))return {valid:false,errors:structuredClone(check.errors)};
 const errors=[],row=corpus.rows.find(r=>r.id===record.caseId);
 if(!row)return {valid:false,errors:['unknown-case']};
 if(record.subjectSha256!==row.subject.sha256)errors.push('subject-mismatch');
 if(record.rubricSha256!==hash(JSON.stringify(corpus)))errors.push('rubric-mismatch');
 if(hash(record.answer.text)!==record.answer.sha256)errors.push('answer-mismatch');
 const ids=record.review.decisions.map(d=>d.criterionId);
 if(new Set(ids).size!==ids.length)errors.push('duplicate-criterion');
 if(ids.length!==row.criteria.length||row.criteria.some(c=>!ids.includes(c.id)))errors.push('incomplete-or-foreign-criteria');
 for(const d of record.review.decisions){
  if(['met','gap'].includes(d.outcome)&&!d.quote)errors.push('decisive-outcome-needs-excerpt');
  if(['met','gap'].includes(d.outcome)&&!d.sourceRefs.length)errors.push('decisive-outcome-needs-rationale-source');
  if(d.quote){const q=d.quote,t=record.answer.text;if(q.startUTF16>=q.endUTF16||q.endUTF16>t.length||!boundary(t,q.startUTF16)||!boundary(t,q.endUTF16)||t.slice(q.startUTF16,q.endUTF16)!==q.text)errors.push('quote-mismatch');}
  if(d.sourceRefs.some(i=>i>=row.sources.length))errors.push('unknown-source');
 }
 if(errors.length)return {valid:false,errors};
 return {valid:true,recordKindClaim:record.answer.provenance,originVerified:false,counts:Object.fromEntries(['met','gap','inconclusive','not-applicable'].map(k=>[k,record.review.decisions.filter(d=>d.outcome===k).length])),independentAcceptance:false,claim:'Record schema, identity and excerpt consistency validated; origin, outcome meaning and independence are not verified. Synthetic records are never model results.'};
}

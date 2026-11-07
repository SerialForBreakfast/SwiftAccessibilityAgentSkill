import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import {build} from './build.mjs';
import {validateReview} from './review.mjs';
import {hash,verifySpans} from '../assertion-bindings-v1/build.mjs';
const base='research/evaluation/rubric-closure-v1/';
const d=JSON.parse(fs.readFileSync(base+'rubrics.json'));
const original=JSON.parse(fs.readFileSync(d.inputs[0].path));
for(const row of d.rows){
 test(row.id+' exact inputs, applicable alternatives and meaningful source anchors',()=>{
  const old=original.cases.find(c=>c.id===row.id);assert.equal(hash(fs.readFileSync(row.subject.path)),row.subject.sha256);
  assert.deepEqual(row.originalAlternatives,old.controller.acceptedAlternatives);
  assert.equal(row.criteria.length,old.controller.criteria.length);
  for(const s of row.sources){const b=fs.readFileSync(s.path);assert.equal(hash(b),s.sha256);assert.equal(b.toString().slice(s.startUTF16,s.endUTF16),s.quote);assert.ok(s.quote.length>20);if(s.quote.startsWith('## Rule'))assert.ok(s.quote.trim().length>'## Rule'.length+10);}
  assert.equal(row.independentAcceptance,false);assert.equal(row.answerStatus,'not-run');
  if(row.alternativeChange.startsWith('Removed'))assert.ok(!row.acceptedAlternatives.some(a=>a==='No change when the supplied implementation is already valid.'));
 });
 for(const c of row.criteria)test(c.id+' actionable pass/fail/inconclusive and retained evidence boundary',()=>{
  assert.ok(c.pass.length>30);assert.ok(c.fail.length>30);assert.ok(c.missing.length>30);
  assert.notEqual(c.pass,c.fail);assert.ok(c.channels.includes('answer-review'));
  assert.equal(c.originalText,original.cases.find(r=>r.id===row.id).controller.criteria[c.index]);
  assert.match(c.evidenceReview,/semantic decision/);
  assert.ok(c.scope);for(const id of c.supplementalContractIds)assert.ok(d.supplementalContracts.some(s=>s.id===id));
 });
}
for(const c of d.supplementalContracts)test(c.testId+' actual existing checkout source and receipt',()=>{
 const source=fs.readFileSync(c.file);assert.equal(hash(source),c.fileSha256);verifySpans(source,c.method);
 assert.equal(hash(source.subarray(c.method.startByte,c.method.endByte)),c.methodSha256);
 assert.equal(hash(fs.readFileSync(c.manifest)),c.manifestSha256);for(const p of c.sourcePins)assert.equal(hash(fs.readFileSync(p.path)),p.sha256);
 assert.equal(hash(fs.readFileSync(c.receipt.path)),c.receipt.sha256);assert.equal(c.receipt.environment.platform,'iOS');assert.equal(c.receipt.environment.runtimeVersion,'26.5');
});
function fixture(){const row=d.rows[0],text='Controller-authored review-record fixture. No model answer was generated.';return {schema:1,caseId:row.id,subjectSha256:row.subject.sha256,rubricSha256:hash(JSON.stringify(d)),answer:{text,sha256:hash(text),provenance:'synthetic-controller-fixture'},review:{reviewer:'offline-fixture',independentClaimed:false,decisions:row.criteria.map(c=>({criterionId:c.id,outcome:'inconclusive',basis:'answer-review',rationale:'Synthetic fixture only; semantic content is deliberately not graded.',quote:null,sourceRefs:[]}))}};}
test('review record can retain inconclusive outcomes without invented quotes or scores',()=>{const r=validateReview(fixture(),d);assert.equal(r.valid,true);assert.equal(r.counts.met,0);assert.equal(r.recordKindClaim,'synthetic-controller-fixture');assert.equal(r.independentAcceptance,false);});
const mutations={
 'stale subject':r=>r.subjectSha256='0'.repeat(64),
 'stale rubric':r=>r.rubricSha256='0'.repeat(64),
 'changed answer':r=>r.answer.text+=' mutated',
 'duplicate decision':r=>r.review.decisions.push(r.review.decisions[0]),
 'missing decision':r=>r.review.decisions.pop(),
 'foreign criterion':r=>r.review.decisions[0].criterionId='other/criterion-0',
 'decisive result without quote':r=>r.review.decisions[0].outcome='met',
 'invented quote':r=>r.review.decisions[0].quote={startUTF16:0,endUTF16:3,text:'bad'},
 'unknown source':r=>r.review.decisions[0].sourceRefs=[999],
 'fixture pass used as answer grade':r=>r.review.decisions[0].basis='fixture-pass',
 'LLM judge field':r=>r.provider='llm',
 'out of range quote':r=>r.review.decisions[0].quote={startUTF16:0,endUTF16:10000000,text:r.answer.text},
 'invented provenance':r=>r.answer.provenance='frontier-evaluated'
};
for(const [name,mutate] of Object.entries(mutations))test('review validator rejects '+name,()=>{const r=fixture();mutate(r);assert.equal(validateReview(r,d).valid,false);});
test('valid excerpt is provenance, not proof the review decision is semantically right',()=>{const r=fixture(),a=r.review.decisions[0];a.outcome='gap';a.quote={startUTF16:0,endUTF16:r.answer.text.length,text:r.answer.text};a.sourceRefs=[0];r.review.independentClaimed=true;const v=validateReview(r,d);assert.equal(v.valid,true);assert.equal(v.independentAcceptance,false);assert.equal(v.recordKindClaim,'synthetic-controller-fixture');});
test('UTF-16 excerpt cannot split a surrogate pair',()=>{const r=fixture();r.answer.text='\uD83D\uDE00';r.answer.sha256=hash(r.answer.text);r.review.decisions[0].quote={startUTF16:0,endUTF16:1,text:r.answer.text.slice(0,1)};assert.equal(validateReview(r,d).valid,false);});
test('all117 former grading gaps specified without claiming new unit coverage',()=>{assert.equal(d.summary.criteria,198);assert.equal(d.summary.previouslyUnboundCriteriaSpecified,117);assert.equal(d.summary.controlsWithTargetedAlternatives,12);assert.equal(d.summary.additionalExecutedMethodsLinked,3);assert.equal(d.summary.primarySourceGaps,3);assert.equal(d.summary.independentlyQualified,0);assert.equal(d.summary.realAnswersGraded,0);assert.equal(d.summary.modelCalls,0);assert.equal(d.summary.newNativeRuns,0);});
test('entire additive rubric overlay reproduces from frozen inputs',()=>assert.deepEqual(build(),d));

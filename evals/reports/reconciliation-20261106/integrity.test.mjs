import test from 'node:test';import assert from 'node:assert/strict';import fs from 'node:fs';import {hash} from '../../../code-examples/tools/contracts.mjs';
const read=p=>JSON.parse(fs.readFileSync(p));const evidence=read('evals/reports/reconciliation-20261106/reconciliation.json');
const local=read('evals/reports/local-compact-b-20261106/summary.json'),agy=read('evals/reports/skill-0.3.0-dev.1-vs-0.3.0-dev.2-20261106/summary.json');
test('reconciliation preserves source reports and historical checkpoint bytes',()=>{for(const pin of evidence.sourcePins)assert.equal(hash(fs.readFileSync(pin.path)),pin.sha256);assert.equal(hash(fs.readFileSync('evals/reports/local-compact-b-20261106/source-review.json')),local.sourceReviewHash);assert.equal(hash(fs.readFileSync('evals/reports/local-compact-b-20261106-criteria.json')),local.criteriaHash);});
test('local token and core counts reconcile to36 distinct answers',()=>{
 assert.equal(local.rows.length,36);assert.equal(new Set(local.rows.map(r=>r.id)).size,36);
 for(const [model,conditions]of Object.entries(local.summary))for(const condition of ['F','BR']){const rows=local.rows.filter(r=>r.model===model&&r.condition===condition),s=conditions[condition];assert.equal(rows.length,6);assert.equal(rows.reduce((n,r)=>n+r.inputTokens+r.outputTokens,0),s.totalTokens);assert.equal(rows.filter(r=>r.core==='met').length,s.coreMet);assert.equal(rows.filter(r=>r.core==='inconclusive').length,s.inconclusive);}
 assert.equal(local.probeCounts.answersWithCode,34);assert.equal(local.probeCounts.codeProbes,36);assert.equal(local.rows.filter(r=>r.compiler==='typecheck_failed').length,10);
});
test('AGY totals and paired deltas support the missed efficiency screen',()=>{
 const [a,b]=Object.values(agy.skill_versions);for(const s of [a,b]){const x=s.accounting;assert.equal(x.input_tokens+x.output_tokens,x.total_tokens);assert.equal(Object.values(x.case_total_tokens).reduce((n,v)=>n+v,0),x.total_tokens);assert.equal(s.meets+s['material-gap']+s['not-assessable'],7);}
 assert.equal(a.accounting.total_tokens+b.accounting.total_tokens,65400);assert.equal(evidence.agy.totalDelta,326);assert.equal(evidence.agy.inputDelta,575);assert.equal(evidence.agy.outputDelta,-249);assert.equal(Object.values(evidence.agy.caseDeltas).filter(x=>x>0).length,5);assert.ok(b.accounting.median_total_tokens>a.accounting.median_total_tokens);assert.equal(a['not-assessable'],1);assert.equal(a['material-gap'],0);
});
test('versioned candidates are immutable and not the historical local B body',()=>{
 const registry=read('research/evaluation/failure-driven/candidates/VERSIONS.json');assert.equal(registry.released_version,'0.2.2');for(const c of registry.candidates)assert.equal(hash(fs.readFileSync(c.entrypoint_file)),c.entrypoint_sha256);assert.notEqual(local.candidateBodyHash,registry.candidates.find(c=>c.version==='0.3.0-dev.2').body_sha256);
});
test('pending execution and communication stay separate from completed source review',()=>{
 assert.equal(agy.calls_completed,14);assert.equal(agy.claude_calls,0);assert.equal(agy.native_answer_checks,'not_run');assert.equal(evidence.verification.modelCallsThisTurn,0);assert.equal(evidence.comparability.pooled,false);assert.equal(evidence.agy.releaseQualified,false);assert.equal(evidence.coordination.incomingMessages,0);assert.equal(evidence.coordination.newMessagesSent,0);
});

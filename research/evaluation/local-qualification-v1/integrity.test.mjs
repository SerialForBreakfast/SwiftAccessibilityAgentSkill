import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import {audit,hash,receiptIssues} from './audit.mjs';
const base='research/evaluation/local-qualification-v1/';
const ledger=JSON.parse(fs.readFileSync(base+'evidence-ledger.json'));
const manifest={id:'fixture',revision:'1',platform:'iOS',deploymentTarget:'26.0'};
const check={id:'positive',lane:'unit',expected:'success',testIds:['State/testCurrent'],failureIds:[]};
const good=()=>({manifestHash:'frozen',package:'fixture',revision:'1',checkId:'positive',status:'passed',observed:'success',environment:{platform:'iOS',deploymentTarget:'26.0',sdkVersion:'27.0',compiler:'Swift',runtimeVersion:'26.5'},execution:{exitCode:0,build:'passed',signal:null,infrastructureError:null,skippedTests:0,executedTestIds:['State/testCurrent'],failedTestIds:[]}});
test('known-good receipt is accepted within its narrow contract',()=>assert.deepEqual(receiptIssues(manifest,'frozen',check,good()),[]));
const mutants={
 'stale manifest':a=>a.manifestHash='old',
 'wrong package':a=>a.package='another',
 'stale revision':a=>a.revision='0',
 'wrong check':a=>a.checkId='compile',
 'failed outcome':a=>a.status='failed',
 'wrong observation':a=>a.observed='failure',
 'infrastructure timeout':a=>a.execution.infrastructureError='timeout',
 'terminated process':a=>a.execution.signal='SIGTERM',
 'failed build':a=>a.execution.build='failed',
 'skipped method':a=>a.execution.skippedTests=1,
 'missing skip count':a=>delete a.execution.skippedTests,
 'missing execution':a=>a.execution.executedTestIds=[],
 'extra method':a=>a.execution.executedTestIds.push('Other/testOther'),
 'unexpected failing assertion':a=>a.execution.failedTestIds=['State/testCurrent'],
 'wrong platform':a=>a.environment.platform='tvOS',
 'wrong deployment target':a=>a.environment.deploymentTarget='27.0',
 'missing compiler':a=>delete a.environment.compiler,
 'missing SDK':a=>delete a.environment.sdkVersion,
 'missing unit runtime':a=>delete a.environment.runtimeVersion
};
for(const [name,mutate] of Object.entries(mutants))test('reject deliberate receipt defect: '+name,()=>{const a=good();mutate(a);assert.ok(receiptIssues(manifest,'frozen',check,a).length);});
test('modified sources cannot inherit an earlier passing receipt',()=>assert.ok(receiptIssues(manifest,'frozen',check,good(),false).includes('source-pins-mismatch')));
test('expected assertion rejection is not confused with infrastructure failure',()=>{const c={...check,expected:'failure',failureIds:['State/testCurrent']},a=good();a.observed='failure';a.execution.exitCode=1;a.execution.failedTestIds=['State/testCurrent'];assert.deepEqual(receiptIssues(manifest,'frozen',c,a),[]);a.execution.build='failed';assert.ok(receiptIssues(manifest,'frozen',c,a).includes('infrastructure-or-build'));});
test('compile receipt does not require an invented runtime',()=>{const c={...check,lane:'compile',testIds:[]},a=good();a.environment.runtimeVersion=null;a.execution.executedTestIds=[];assert.deepEqual(receiptIssues(manifest,'frozen',c,a),[]);});
for(const r of ledger.rows)test(r.id+' exact inputs retained without blanket gold promotion',()=>{
 assert.equal(hash(fs.readFileSync(r.subject.path)),r.subject.sha256);
 assert.equal(r.status,'draft-not-independently-qualified');
 assert.equal(r.modelOutcome,'not-run');
 assert.ok(r.criteria.every(c=>c.status==='requires-semantic-review'));
 for(const s of r.sourceEvidence)assert.equal(hash(fs.readFileSync(s.path)),s.sha256);
 for(const c of r.checks)for(const a of c.matchingReceipts){assert.equal(hash(fs.readFileSync(a.index)),a.indexSha256);if(c.status==='receipt-verified-contract-only')assert.ok(c.matchingReceipts.some(a=>!a.issues.length));}
});
test('ledger is fully reproducible from unchanged public inputs',()=>assert.deepEqual(audit(),ledger));
test('all sixty drafts accounted for without model or gold claims',()=>{assert.equal(ledger.summary.cases,60);assert.equal(ledger.summary.modelCalls,0);assert.equal(ledger.summary.qualifiedGold,0);assert.equal(ledger.summary.sourceGaps,3);});
test('successful label cannot conceal a failing process',()=>{const a=good();a.execution.exitCode=65;assert.ok(receiptIssues(manifest,'frozen',check,a).includes('process-outcome-mismatch'));});
test('missing process status is not silently accepted',()=>{const a=good();delete a.execution.exitCode;assert.ok(receiptIssues(manifest,'frozen',check,a).includes('process-outcome-mismatch'));});

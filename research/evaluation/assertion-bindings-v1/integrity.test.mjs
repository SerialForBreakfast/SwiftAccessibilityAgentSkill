import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import {build,hash,verifySpans,selectReceipt,collectReceipts} from './build.mjs';
import {selections} from './spec.mjs';
const base='research/evaluation/assertion-bindings-v1/';
const d=JSON.parse(fs.readFileSync(base+'bindings.json'));
const catalog=JSON.parse(fs.readFileSync(d.input.path));
const receipts=collectReceipts();
for(const row of d.rows)test(row.id+' exact criterion identity and bounded classification',()=>{
 const original=catalog.cases.find(c=>c.id===row.id);
 assert.equal(hash(fs.readFileSync(row.subject.path)),row.subject.sha256);
 assert.deepEqual(row.acceptedAlternatives,original.controller.acceptedAlternatives);
 assert.equal(row.criteria.length,original.controller.criteria.length);
 for(const c of row.criteria){assert.equal(c.text,original.controller.criteria[c.index]);for(const b of c.bindings){assert.ok(b.proves);assert.ok(b.remaining);for(const id of b.contractIds){assert.ok(d.contracts[id]);assert.equal(d.contracts[id].receipt.environment.platform,row.platform);}}}
 assert.equal(row.status,'author-bound-not-independently-qualified');assert.equal(row.modelOutcome,'not-run');
});
for(const c of Object.values(d.contracts))test(c.testId+' '+c.manifest+' pinned assertion and executed method',()=>{
 const source=fs.readFileSync(c.file);assert.equal(hash(source),c.fileSha256);
 assert.equal(hash(source.subarray(c.startByte,c.endByte)),c.methodSha256);
 assert.equal(source.subarray(c.startByte,c.endByte).toString(),c.methodSource);
 verifySpans(source,{...c,assertionSites:c.assertions});
 for(const a of c.assertions)assert.equal(hash(source.subarray(a.startByte,a.endByte)),a.sha256);
 for(const pin of c.sourcePins)assert.equal(hash(fs.readFileSync(pin.path)),pin.sha256);
 const m=JSON.parse(fs.readFileSync(c.manifest));assert.equal(hash(fs.readFileSync(c.manifest)),c.manifestSha256);
 const receipt=selectReceipt(m,c.manifestSha256,c.testId,receipts,true);assert.ok(receipt);
 assert.equal(receipt.r.path,c.receipt.index);assert.equal(receipt.r.sha256,c.receipt.indexSha256);
 assert.equal(receipt.r.attempt.attempt,c.receipt.attempt);
 for(const n of c.negativeControls){assert.equal(hash(fs.readFileSync(n.index)),n.indexSha256);assert.ok(n.failureIds.includes(c.testId));}
});
test('all198 criteria classified without inventing complete gold coverage',()=>{assert.equal(d.summary.cases,60);assert.equal(d.summary.criteria,198);assert.equal(d.summary.criteriaWithUnitSubset,81);assert.equal(d.summary.casesWithUnitSubset,35);assert.equal(d.summary.uniqueMethods,143);assert.equal(d.summary.assertionSites,317);assert.equal(d.summary.missingExecutionBindings,0);assert.equal(d.summary.qualifiedGold,0);assert.equal(d.summary.nativeRuns,0);assert.equal(d.summary.modelCalls,0);});
test('builder reproduces the checked-in controller overlay',()=>assert.deepEqual(build(),d));
test('bindings retain exact original subject and controller bytes',()=>assert.equal(hash(fs.readFileSync(d.input.path)),d.input.sha256));
test('scope controls and unsupported axes do not acquire borrowed unit evidence',()=>{for(const c of catalog.cases.filter(c=>!c.controller.note))assert.deepEqual(selections(c),{});for(const [platform,framework] of [['watchOS','SwiftUI'],['visionOS','SwiftUI'],['macOS','UIKit'],['iOS','AppKit']])assert.deepEqual(selections({platform,framework,topic:'semantics',controller:{note:'fixture'}}),{});});
test('statement drift and byte-boundary corruption reject a source binding',()=>{const c=Object.values(d.contracts)[0],source=fs.readFileSync(c.file),method={...c,assertionSites:structuredClone(c.assertions)};method.assertionSites[0].expression+=' stale';assert.throws(()=>verifySpans(source,method),/drift/);method.assertionSites=structuredClone(c.assertions);method.assertionSites[0].startByte=c.startByte-1;assert.throws(()=>verifySpans(source,method),/outside/);assert.throws(()=>verifySpans(source,{...method,startByte:-1}),/Invalid/);});
test('unexecuted method, stale manifest and changed sources cannot inherit a pass',()=>{const c=Object.values(d.contracts)[0],m=JSON.parse(fs.readFileSync(c.manifest));assert.equal(selectReceipt(m,'stale',c.testId,receipts,true),null);assert.equal(selectReceipt(m,c.manifestSha256,'Missing/testInvented',receipts,true),null);assert.equal(selectReceipt(m,c.manifestSha256,c.testId,receipts,false),null);});
test('syntax source pin and conditional scopes remain explicit',()=>{assert.equal(hash(fs.readFileSync(d.tool.source)),d.tool.sha256);for(const c of Object.values(d.contracts)){assert.match(c.executionScope,/Individual assertion/);for(const a of c.assertions)assert.ok(Array.isArray(a.conditionalCompilation));}});

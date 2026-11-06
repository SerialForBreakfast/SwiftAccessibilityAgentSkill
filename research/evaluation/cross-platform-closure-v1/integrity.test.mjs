import test from 'node:test';import assert from 'node:assert/strict';import fs from 'node:fs';import path from 'node:path';import {hash} from '../../../code-examples/tools/contracts.mjs';
const base='research/evaluation/cross-platform-closure-v1/',read=p=>JSON.parse(fs.readFileSync(p));
const folders=['ios-closure-v1','macos-closure-v1','tvos-closure-v1','macos-closure-details-v1','tvos-state-recovery-v1'];
test('bounded corpus stays507 clauses and36 source rules',()=>{
 const inv=read(base+'inventory.json'),ledger=read(base+'clause-ledger.json');assert.equal(inv.documents.length,36);assert.equal(ledger.clauses.length,507);assert.equal(ledger.rules.length,36);assert.equal(new Set(ledger.clauses.map(c=>c.id)).size,507);
 assert.equal(ledger.inventoryHash,hash(fs.readFileSync(base+'inventory.json')));for(const d of inv.documents)assert.equal(hash(fs.readFileSync(d.path)),d.sha256);
 assert.ok(ledger.clauses.every(c=>c.status!=='pending-clause-review'&&c.rationale));
 for(const c of ledger.clauses.filter(c=>c.id.startsWith('U-'))){const old=read(c.priorLedger).clauses.find(x=>x.id===c.id);assert.equal(c.status,old.status);assert.equal(c.rationale,old.rationale);}
});
test('new positive and deliberate-negative results match exact hashed manifests',()=>{
 const report=read(base+'results-index.json');let methods=0,negatives=0;
 for(const folder of folders){const bytes=fs.readFileSync('code-examples/platforms/'+folder+'/manifest.json'),m=JSON.parse(bytes);methods+=m.checks.find(c=>c.id==='positive').testIds.length;
 for(const c of m.checks){const rs=report.attempts.filter(r=>r.manifestHash===hash(bytes)&&r.checkId===c.id);assert.equal(rs.length,1);const r=rs[0];assert.equal(r.status,'passed');assert.equal(r.observed,c.expected);assert.deepEqual([...r.execution.executedTestIds].sort(),[...c.testIds].sort());assert.deepEqual([...r.execution.failedTestIds].sort(),[...c.failureIds].sort());if(c.expected==='failure')negatives++;}}
 assert.equal(methods,126);assert.equal(negatives,23);assert.equal(report.attempts.filter(r=>r.status==='failed').length,2);
 for(const pin of report.pins)assert.equal(hash(fs.readFileSync(pin.path)),pin.sha256);
});
test('all36 platform questions have complete available inputs and honest output status',()=>{
 const indices=['prompt-records-v1/platform-prompts.json','platform-lifecycle-v1/prompt-records.json','platform-media-v1/prompt-records.json','platform-structure-v1/prompt-records.json','cross-platform-closure-v1/prompt-records.json'].map(p=>read('research/evaluation/'+p).cases),cases=indices.flat();assert.deepEqual(indices.map(x=>x.length),[9,4,6,4,13]);
 const found=fs.readdirSync('code-examples/platforms').filter(n=>!n.startsWith('.')).flatMap(n=>{const dir='code-examples/platforms/'+n+'/evaluation';return fs.existsSync(dir)?fs.readdirSync(dir).filter(f=>f.endsWith('.prompt.md')).map(f=>dir+'/'+f):[];});assert.deepEqual(cases.map(c=>c.subject.path).sort(),found.sort());assert.equal(new Set(cases.map(c=>c.id)).size,36);
 for(const c of indices[4]){assert.equal(c.subject.text,fs.readFileSync(c.subject.path,'utf8'));assert.equal(c.subject.sha256,hash(fs.readFileSync(c.subject.path)));assert.equal(c.analysis.sha256,hash(fs.readFileSync(c.analysis.path)));assert.equal(c.outputs.status,'not-run');assert.deepEqual(c.outputs.attempts,[]);assert.equal(c.analysis.answerAnalysis,null);assert.ok(c.testIds.length);}
});
test('historical global checker and first failed source remain recoverable',()=>{
 const a=read(base+'inventory-amendment.json');assert.equal(hash(fs.readFileSync(a.preservedOriginal)),a.originalSha256);
 const old=JSON.parse(fs.readFileSync(base+'incidents/mac-first-manifest.json.txt'));assert.equal(old.revision,'1');assert.ok(fs.readFileSync(base+'incidents/mac-first-diagnostics.txt','utf8').includes('has been renamed'));
 const m=read('code-examples/platforms/macos-closure-v1/manifest.json');assert.equal(m.revision,'2');
});
test('executed ledger bindings resolve selected methods and real receipt hashes',()=>{
 const ledger=read(base+'clause-ledger.json');for(const b of Object.values(ledger.bindings)){
 assert.equal(hash(fs.readFileSync(b.manifest)),b.manifestHash);assert.equal(b.evidenceStatus,'executed');assert.ok(b.tests.length);
 for(const e of b.execution){const r=read(e.index).attempts.find(x=>x.attempt===e.attempt);assert.equal(r.originalResultHash,e.resultHash);assert.equal(r.manifestHash,b.manifestHash);assert.ok(b.tests.every(t=>r.execution.executedTestIds.includes(t)));}}
});

test('recovery preserves the first failing assertions and candidate route uses repaired source',()=>{
 const failed=read(base+'results-index.json').attempts.find(r=>r.attempt==='closure-recovery-positive-r1');assert.equal(failed.status,'failed');assert.equal(failed.execution.failedTestIds.length,2);
 const first=JSON.parse(fs.readFileSync(base+'incidents/tv-state-first-manifest.json.txt'));assert.equal(first.revision,'1');const current=read('code-examples/platforms/tvos-state-recovery-v1/manifest.json');assert.equal(current.revision,'2');
 assert.equal(first.files.find(f=>f.path==='Sources/StateContracts.swift').sha256,hash(fs.readFileSync('code-examples/platforms/tvos-state-recovery-v1/NegativeFixtures/stale_status.swift')));
});
test('retrieval telemetry is actual bytes and hashes, with unavailable token counts',()=>{
 const rows=read(base+'retrieval-measurements.json');assert.equal(rows.length,39);
 for(const r of rows){assert.equal(r.tokens,null);assert.equal(r.loadedBytes,r.trace.reduce((n,t)=>n+t.bytes,0));for(const t of r.trace){assert.equal(t.bytes,fs.readFileSync(t.path).length);assert.equal(t.sha256,hash(fs.readFileSync(t.path)));}}
});

import test from 'node:test';import assert from 'node:assert/strict';import fs from 'node:fs';import path from 'node:path';import {fileURLToPath} from 'node:url';import {hash} from '../../../code-examples/tools/contracts.mjs';
const root=fileURLToPath(new URL('../../../',import.meta.url));const read=p=>fs.readFileSync(root+p);const base='research/evaluation/platform-structure-v1/';
const report=JSON.parse(read(base+'results-index.json'));
for(const [folder,count] of [['macos-structure-v1',28],['tvos-structure-v1',29]])test(folder+' exact current native receipts',()=>{
 const b=read('code-examples/platforms/'+folder+'/manifest.json'),m=JSON.parse(b);assert.equal(m.checks.find(c=>c.id==='positive').testIds.length,count);
 for(const c of m.checks){const rs=report.attempts.filter(a=>a.manifestHash===hash(b)&&a.checkId===c.id);assert.equal(rs.length,1);const r=rs[0];assert.equal(r.status,'passed');assert.equal(r.observed,c.expected);assert.deepEqual([...r.execution.executedTestIds].sort(),[...c.testIds].sort());assert.deepEqual([...r.execution.failedTestIds].sort(),[...c.failureIds].sort());assert.equal(r.environment.platform,m.platform);if(c.lane==='unit')assert.equal(Number(r.environment.runtimeVersion.split('.')[0]),m.runtimeMajor);}
});
test('substantive inputs and historical checker preserved',()=>{
 assert.equal(report.attempts.length,18);assert.ok(report.attempts.every(r=>r.status==='passed'));
 assert.equal(report.attempts.filter(r=>r.observed==='failure').length,14);
 assert.equal(report.attempts.reduce((n,r)=>n+r.execution.executedTestIds.length,0),71);
 for(const p of report.pins){assert.equal(hash(read(p.path)),p.sha256);assert.ok(!p.path.split('/').some(s=>s.startsWith('.')));}
 const amendment=JSON.parse(read(base+'inventory-amendment.json'));assert.equal(hash(read(amendment.preservedOriginal)),amendment.originalSha256);
});
test('all23 platform questions accounted for without expanding prior indices',()=>{
 const indices=['prompt-records-v1/platform-prompts.json','platform-lifecycle-v1/prompt-records.json','platform-media-v1/prompt-records.json','platform-structure-v1/prompt-records.json'].map(p=>JSON.parse(read('research/evaluation/'+p)).cases);
 assert.deepEqual(indices.map(c=>c.length),[9,4,6,4]);const all=indices.flat();
 const found=fs.readdirSync(root+'code-examples/platforms').filter(n=>!n.startsWith('.')&&!n.includes('-closure-')&&!n.includes('-state-recovery-')).flatMap(n=>{const d=`code-examples/platforms/${n}/evaluation`;return fs.existsSync(root+d)?fs.readdirSync(root+d).filter(f=>f.endsWith('.prompt.md')).map(f=>d+'/'+f):[];});
 assert.deepEqual(all.map(c=>c.subject.path).sort(),found.sort());assert.equal(new Set(all.map(c=>c.id)).size,23);
 for(const c of indices[3]){assert.equal(c.subject.text,read(c.subject.path).toString());assert.equal(c.subject.sha256,hash(read(c.subject.path)));assert.equal(c.analysis.sha256,hash(read(c.analysis.path)));assert.equal(c.outputs.status,'not-run');assert.deepEqual(c.outputs.attempts,[]);assert.equal(c.analysis.answerAnalysis,null);assert.ok(fs.existsSync(root+c.nativeManifest));}
});
test('retrieval measurements match actual files with tokens unavailable',()=>{
 const rows=JSON.parse(read(base+'retrieval-measurements.json'));assert.equal(rows.length,12);
 for(const r of rows){assert.equal(r.tokens,null);assert.equal(r.loadedBytes,r.trace.reduce((n,t)=>n+t.bytes,0));for(const t of r.trace){assert.equal(t.bytes,read(t.path).length);assert.equal(t.sha256,hash(read(t.path)));}}
});

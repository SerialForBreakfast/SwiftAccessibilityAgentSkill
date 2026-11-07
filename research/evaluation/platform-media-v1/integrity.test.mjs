import test from 'node:test';import assert from 'node:assert/strict';import fs from 'node:fs';import path from 'node:path';import {fileURLToPath} from 'node:url';import {hash} from '../../../code-examples/tools/contracts.mjs';
const root=fileURLToPath(new URL('../../../',import.meta.url));const read=p=>fs.readFileSync(root+p);const base='research/evaluation/platform-media-v1/';
const report=JSON.parse(read(base+'results-index.json'));
for(const folder of ['macos-media-v1','tvos-media-v1'])test(folder+' final checks match native receipts',()=>{
 const b=read('code-examples/platforms/'+folder+'/manifest.json'),m=JSON.parse(b);
 assert.equal(m.checks.find(c=>c.id==='positive').testIds.length,25);
 for(const c of m.checks){const rs=report.attempts.filter(a=>a.manifestHash===hash(b)&&a.checkId===c.id);assert.equal(rs.length,1);const r=rs[0];assert.equal(r.status,'passed');assert.equal(r.observed,c.expected);assert.deepEqual([...r.execution.executedTestIds].sort(),[...c.testIds].sort());assert.deepEqual([...r.execution.failedTestIds].sort(),[...c.failureIds].sort());assert.equal(r.environment.platform,m.platform);if(c.lane==='unit')assert.equal(Number(r.environment.runtimeVersion.split('.')[0]),m.runtimeMajor);}
});
test('first failed oracle, substantive pins and reuse remain intact',()=>{
 assert.equal(report.attempts.length,20);assert.equal(report.attempts.filter(a=>a.status==='passed').length,19);
 const first=report.attempts.find(a=>a.attempt==='media-mac-positive-r1');assert.equal(first.status,'failed');assert.deepEqual(first.execution.failedTestIds,['MediaChoiceTests/testRequiredAudioGroupRefusesOff']);assert.equal(first.execution.executedTestIds.length,23);
 assert.equal(report.attempts.reduce((n,a)=>n+a.execution.executedTestIds.length,0),87);
 for(const p of report.pins){assert.equal(hash(read(p.path)),p.sha256);assert.ok(!p.path.split('/').some(s=>s.startsWith('.')));}
 for(const folder of ['macos-media-v1','tvos-media-v1']){const original=JSON.parse(read(base+'incidents/'+folder+'-first-manifest.json.txt'));for(const p of ['Sources/MediaChoice.swift','Tests/MediaChoiceTests.swift'])assert.equal(hash(read(base+'incidents/'+folder+'-first-'+p.replaceAll('/','-')+'.txt')),original.files.find(f=>f.path===p).sha256);}
 for(const p of JSON.parse(read(base+'reuse-provenance.json'))){assert.equal(hash(read(p.original)),p.sha256);assert.equal(hash(read(p.copy)),p.sha256);}
});
test('nineteen historical platform prompts have exact inputs within their declared packages',()=>{
 const previous=JSON.parse(read('research/evaluation/prompt-records-v1/platform-prompts.json')).cases;
 const lifecycle=JSON.parse(read('research/evaluation/platform-lifecycle-v1/prompt-records.json')).cases;
 const current=JSON.parse(read(base+'prompt-records.json')).cases;
 assert.equal(previous.length,9);assert.equal(lifecycle.length,4);assert.equal(current.length,6);
 const all=[...previous,...lifecycle,...current];const found=[...new Set(all.map(c=>path.dirname(c.subject.path)))].flatMap(d=>{return fs.existsSync(root+d)?fs.readdirSync(root+d).filter(f=>f.endsWith('.prompt.md')).map(f=>d+'/'+f):[];});
 assert.deepEqual(all.map(c=>c.subject.path).sort(),found.sort());assert.equal(new Set(all.map(c=>c.id)).size,19);
 for(const c of current){assert.equal(c.subject.text,read(c.subject.path).toString());assert.equal(c.subject.sha256,hash(read(c.subject.path)));assert.equal(c.analysis.sha256,hash(read(c.analysis.path)));assert.equal(c.outputs.status,'not-run');assert.deepEqual(c.outputs.attempts,[]);assert.equal(c.analysis.answerAnalysis,null);assert.ok(fs.existsSync(root+c.nativeManifest));}
});
test('recorded retrieval reads are minimal, hashed and tokens unavailable',()=>{
 const rows=JSON.parse(read(base+'retrieval-measurements.json'));assert.equal(rows.length,18);
 for(const r of rows){assert.equal(r.tokens,null);assert.equal(r.evidenceFramework,'AVFoundation');assert.equal(r.loadedBytes,r.trace.reduce((n,t)=>n+t.bytes,0));for(const t of r.trace){assert.equal(t.bytes,read(t.path).length);assert.equal(t.sha256,hash(read(t.path)));}}
});

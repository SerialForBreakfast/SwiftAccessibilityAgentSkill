import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {hash} from '../../../code-examples/tools/contracts.mjs';
const root=fileURLToPath(new URL('../../../',import.meta.url));
const read=p=>fs.readFileSync(root+p);
const base='research/evaluation/platform-lifecycle-v1/';
const report=JSON.parse(read(base+'results-index.json'));
for(const folder of ['macos-lifecycle-v1','tvos-lifecycle-v1'])test(folder+' current checks have exact matching receipts',()=>{
 const bytes=read('code-examples/platforms/'+folder+'/manifest.json'),m=JSON.parse(bytes);
 for(const c of m.checks){
  const rs=report.attempts.filter(r=>r.manifestHash===hash(bytes)&&r.checkId===c.id&&r.status==='passed');
  assert.equal(rs.length,1,c.id);
  const r=rs[0];assert.equal(r.observed,c.expected);
  assert.deepEqual([...r.execution.executedTestIds].sort(),[...c.testIds].sort());
  assert.deepEqual([...r.execution.failedTestIds].sort(),[...c.failureIds].sort());
  assert.equal(r.environment.platform,m.platform);
  if(c.lane==='unit')assert.equal(Number(r.environment.runtimeVersion.split('.')[0]),m.runtimeMajor);
 }
});
test('pins preserve substantive inputs, original source and distinct revisions',()=>{
 for(const p of report.pins){assert.ok(!p.path.split('/').some(x=>x.startsWith('.')));assert.equal(hash(read(p.path)),p.sha256);}
 assert.equal(report.attempts.length,19);
 assert.equal(report.attempts.filter(a=>a.observed==='failure').length,11);
 assert.ok(report.attempts.every(a=>a.status==='passed'));
 assert.equal(report.attempts.reduce((n,a)=>n+a.execution.executedTestIds.length,0),124);
 const initial=JSON.parse(read(base+'incidents/mac-first-manifest.json.txt'));
 assert.equal(initial.checks.find(c=>c.id==='positive').testIds.length,27);
 assert.equal(hash(read(base+'incidents/mac-original-no-responder-check.swift.txt')),initial.files.find(f=>f.path==='Sources/DesktopLifecycle.swift').sha256);
 assert.equal(hash(read(base+'incidents/mac-first-tests.swift.txt')),initial.files.find(f=>f.path==='Tests/DesktopLifecycleTests.swift').sha256);
 assert.equal(hash(read(base+'incidents/mac-original-no-responder-check.swift.txt')),hash(read('code-examples/platforms/macos-lifecycle-v1/NegativeFixtures/OriginalNoResponderCheck.swift')));
 const tv=JSON.parse(read(base+'incidents/tv-first-manifest.json.txt'));
 assert.equal(hash(read(base+'incidents/tv-first-ownership-mutant.swift.txt')),tv.files.find(f=>f.path==='NegativeFixtures/ForeignTarget.swift').sha256);
 const now=JSON.parse(read('code-examples/platforms/tvos-lifecycle-v1/manifest.json'));
 for(const p of ['Sources/TelevisionLifecycle.swift','Tests/TelevisionLifecycleTests.swift'])assert.equal(tv.files.find(f=>f.path===p).sha256,now.files.find(f=>f.path===p).sha256);
});
test('original nine plus four lifecycle records account for their indexed packages',()=>{
 const original=JSON.parse(read('research/evaluation/prompt-records-v1/platform-prompts.json'));
 const added=JSON.parse(read(base+'prompt-records.json'));
 assert.equal(original.cases.length,9);assert.equal(added.cases.length,4);
 const all=[...original.cases,...added.cases];
 const folders=[...new Set(all.map(c=>path.dirname(c.subject.path)))];
 const found=folders.flatMap(d=>{
  return fs.existsSync(root+d)?fs.readdirSync(root+d).filter(f=>f.endsWith('.prompt.md')).map(f=>d+'/'+f):[];
 });
 assert.deepEqual(all.map(c=>c.subject.path).sort(),found.sort());
 assert.equal(new Set(all.map(c=>c.id)).size,13);
 for(const c of added.cases){
  assert.equal(c.subject.text,read(c.subject.path).toString());assert.equal(c.subject.sha256,hash(read(c.subject.path)));
  assert.equal(c.analysis.sha256,hash(read(c.analysis.path)));
  assert.equal(c.outputs.status,'not-run');assert.deepEqual(c.outputs.attempts,[]);assert.equal(c.analysis.answerAnalysis,null);
  assert.equal(c.lifecycle,'draft-not-run');assert.ok(fs.existsSync(root+c.nativeManifest));
 }
});
test('retrieval measurement bytes reflect actual files and absent token telemetry',()=>{
 const measurements=JSON.parse(read(base+'retrieval-measurements.json'));
 assert.equal(measurements.length,12);
 for(const r of measurements){assert.equal(r.tokens,null);assert.equal(r.loadedBytes,r.trace.reduce((n,t)=>n+t.bytes,0));for(const t of r.trace){assert.equal(t.sha256,hash(read(t.path)));assert.equal(t.bytes,read(t.path).length);}}
});

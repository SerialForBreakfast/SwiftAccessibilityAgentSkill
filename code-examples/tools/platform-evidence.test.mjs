import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import {fileURLToPath} from 'node:url';
import {hash} from './contracts.mjs';
const root = fileURLToPath(new URL('../../', import.meta.url));
const read = p=>fs.readFileSync(root+p);
const report = JSON.parse(read('research/evaluation/platform-expansion-v1/results-index.json'));
const amendment = JSON.parse(read('research/evaluation/platform-expansion-v1-amendment/amendment.json'));
for(const folder of ['macos-appkit-v1','tvos-uikit-v1']) {
  test(`${folder}: every current check has an exact successful validation receipt`,()=>{
    const bytes=read(`code-examples/platforms/${folder}/manifest.json`),m=JSON.parse(bytes);
    for(const check of m.checks) {
      const records=report.attempts.filter(r=>r.manifestHash===hash(bytes)&&r.checkId===check.id&&r.status==='passed');
      assert.equal(records.length,1,check.id);
      const r=records[0];
      assert.equal(r.observed,check.expected);
      assert.deepEqual([...r.execution.executedTestIds].sort(),[...check.testIds].sort());
      assert.deepEqual([...r.execution.failedTestIds].sort(),[...check.failureIds].sort());
      assert.equal(r.environment.platform,m.platform);
      if(check.lane==='unit')assert.equal(Number(r.environment.runtimeVersion.split('.')[0]),m.runtimeMajor);
      else assert.equal(r.environment.runtimeVersion,null);
    }
  });
}
test('first failures and source pins remain explicit',()=>{
  assert.ok(report.attempts.some(r=>r.status==='blocked'&&r.reason==='Ambiguous or unavailable native Mac destination'));
  assert.ok(report.attempts.some(r=>r.status==='failed'&&r.execution?.failedTestIds.includes('DesktopActionsTests/testShortcutDoesNotRetainRow')));
  assert.equal(hash(read(amendment.originalIndex.path)),amendment.originalIndex.sha256);
  assert.deepEqual(amendment.excludedNonEvidence.map(p=>p.path),['code-examples/platforms/.DS_Store']);
  assert.deepEqual(amendment.supersededVerifiers.map(p=>p.path),['code-examples/tools/platform-evidence.test.mjs']);
  for(const pin of report.pins) {
    const excluded=amendment.excludedNonEvidence.find(p=>p.path===pin.path);
    if(excluded) { assert.equal(excluded.sha256,pin.sha256); continue; }
    const original=amendment.supersededVerifiers.find(p=>p.path===pin.path);
    if(original) assert.equal(original.sha256,pin.sha256);
    assert.equal(hash(read(original?.preservedPath??pin.path)),pin.sha256,pin.path);
  }
});
test('all new positive methods have paired controller rubrics and isolated questions',()=>{
  for(const folder of ['macos-appkit-v1','tvos-uikit-v1']) {
    const base=`code-examples/platforms/${folder}/`,m=JSON.parse(read(base+'manifest.json'));
    const rubrics=fs.readdirSync(root+base+'evaluation').filter(f=>f.endsWith('.rubric.md'));
    const text=rubrics.map(f=>read(base+'evaluation/'+f).toString()).join('\n');
    for(const id of m.checks.find(c=>c.id==='positive').testIds)assert.ok(text.includes(id),id);
    for(const r of rubrics){const prompt=read(base+'evaluation/'+r.replace('.rubric.md','.prompt.md')).toString();assert.ok(!/ROUTING:|test[A-Z]|NegativeFixtures|rubric|manifest\.json/.test(prompt));}
  }
});

import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import {hash} from '../../../code-examples/tools/contracts.mjs';
const root = 'research/evaluation/swiftui-closure-v1';
const read = p => JSON.parse(fs.readFileSync(p));
const attempts = read(root + '/results-index.json').attempts;
const pairs = read(root + '/prompt-records.json').cases;
for (const platform of ['iOS', 'macOS', 'tvOS']) test(platform + ' final positive contracts have matching native evidence', () => {
  const cases = pairs.filter(c => c.platform === platform), m = read(cases[0].manifest);
  for (const check of m.checks) {
    const a = attempts.find(a => a.package === m.id && a.revision === m.revision && a.checkId === check.id);
    assert.ok(a, m.id + '/' + check.id); assert.equal(a.status, 'passed');
    assert.equal(a.observed, check.expected); assert.equal(a.manifestHash, hash(fs.readFileSync(cases[0].manifest)));
    assert.deepEqual([...a.execution.executedTestIds].sort(), [...check.testIds].sort());
    assert.deepEqual([...a.execution.failedTestIds].sort(), [...check.failureIds].sort());
    assert.equal(a.environment.platform, platform); assert.equal(a.environment.deploymentTarget, '26.0');
    assert.equal(a.environment.sdkVersion, '27.0');
    assert.equal(a.execution.build, 'passed'); assert.equal(a.execution.skippedTests, 0);
    assert.equal(hash(fs.readFileSync(a.publicResult.path)), a.publicResult.sha256);
    if (check.lane === 'unit') assert.equal(a.environment.runtimeVersion, platform === 'macOS' ? '27.0' : '26.5');
    else assert.equal(a.environment.runtimeVersion, null);
    for (const artifact of a.artifacts) assert.equal(hash(fs.readFileSync(artifact.path)), artifact.sha256);
  }
});
test('each new draft rubric binds only to methods actually executed by its final positive suite', () => {
  for (const c of pairs) {
    const m = read(c.manifest), a = attempts.find(a => a.package === m.id && a.revision === m.revision && a.checkId === 'positive');
    assert.ok(a); for (const id of c.testIds) assert.ok(a.execution.executedTestIds.includes(id));
    assert.deepEqual(c.outputs, {status: 'not-run', attempts: []});
  }
});
test('first compiler failures, blocked adapter and failed oracle executions stay visible', () => {
  assert.equal(attempts.filter(a => a.status === 'error').length, 2);
  assert.equal(attempts.filter(a => a.status === 'blocked').length, 1);
  const failures = attempts.filter(a => a.status === 'failed'); assert.equal(failures.length, 3);
  for (const a of failures) assert.deepEqual(a.execution.failedTestIds, ['MediaSelectionTests/testReplacedItemRejectsOldChoice']);
  for (const a of attempts.filter(a => ['error', 'blocked'].includes(a.status))) assert.equal(a.execution, null);
});
test('SDK captures locate the actual selector rather than a comment about deprecated neighbors', () => {
  const d = read(root + '/declarations.json'); assert.equal(d.records.length, 15);
  for (const r of d.records) {
    assert.equal(r.status, 'declaration-located'); assert.ok(r.declaration.startsWith(r.selector));
    assert.equal(r.deploymentTarget, '26.0');
    if (r.api === 'AVAsset.loadMediaSelectionGroup') {
      assert.match(r.declaration, /API_AVAILABLE\(macos\(12\.0\), ios\(15\.0\), tvos\(15\.0\)/);
      assert.doesNotMatch(r.declaration, /API_DEPRECATED/);
    }
  }
});
test('mutant source variants actually differ and are not a build failure credited as rejection', () => {
  const c = pairs.find(c => c.platform === 'macOS'), m = read(c.manifest), dir = c.manifest.replace('/manifest.json', '');
  for (const check of m.checks.filter(c => c.expected === 'failure')) {
    assert.notEqual(hash(fs.readFileSync(dir + '/' + check.replacement.target)), hash(fs.readFileSync(dir + '/' + check.replacement.source)));
    const a = attempts.find(a => a.package === m.id && a.revision === m.revision && a.checkId === check.id);
    assert.equal(a.execution.build, 'passed'); assert.equal(a.execution.failedTestIds.length, 1);
  }
});

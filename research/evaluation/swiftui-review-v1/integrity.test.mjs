import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';
import {hash, validateManifest} from '../../../code-examples/tools/contracts.mjs';
const base = 'research/evaluation/swiftui-review-v1/';
const read = p => JSON.parse(fs.readFileSync(p));
const records = read(base + 'results-index.json').attempts, pairs = read(base + 'prompt-records.json').cases;
test('original closure batch stays byte-identical throughout review correction', () => {
  for (const pin of read(base + 'prior-batch-pins.json').files) assert.equal(hash(fs.readFileSync(pin.path)), pin.sha256, pin.path);
});
test('three genuine failure cases reproduced against unchanged prior production source', () => {
  const a = records.find(a => a.package === 'swiftui-media-review-repro-v1');
  assert.equal(a.observed, 'failure'); assert.equal(a.execution.build, 'passed');
  assert.equal(a.execution.executedTestIds.length, 3); assert.equal(a.execution.failedTestIds.length, 3);
  const source = fs.readFileSync('code-examples/swiftui/media-review-repro-v1/Sources/MediaSelection.swift');
  assert.equal(hash(source), hash(fs.readFileSync('code-examples/swiftui/media-shared-v1/MediaSelection.swift')));
});
for (const platform of ['iOS', 'macOS', 'tvOS']) test(platform + ' corrected source/tests have actual matching native receipts', () => {
  const cases = pairs.filter(c => c.platform === platform), m = read(cases[0].manifest);
  validateManifest(m, path.dirname(cases[0].manifest));
  for (const check of m.checks) {
    const a = records.find(a => a.package === m.id && a.checkId === check.id);
    assert.ok(a); assert.equal(a.status, 'passed'); assert.equal(a.observed, check.expected);
    assert.equal(a.manifestHash, hash(fs.readFileSync(cases[0].manifest)));
    assert.deepEqual([...a.execution.executedTestIds].sort(), [...check.testIds].sort());
    assert.deepEqual([...a.execution.failedTestIds].sort(), [...check.failureIds].sort());
    assert.equal(a.execution.build, 'passed'); assert.equal(a.execution.skippedTests, 0);
    assert.equal(a.environment.deploymentTarget, '26.0'); assert.equal(a.environment.sdkVersion, '27.0');
    if (check.lane === 'unit') assert.equal(a.environment.runtimeVersion, platform === 'macOS' ? '27.0' : '26.5');
    for (const artifact of a.artifacts) assert.equal(hash(fs.readFileSync(artifact.path)), artifact.sha256);
  }
  const positive = m.checks.find(c => c.id === 'positive').testIds;
  assert.equal(positive.length, 44);
  const graded = cases.flatMap(c => c.testIds);
  assert.equal(graded.length, new Set(graded).size);
  assert.equal(graded.length + 3, positive.length);
  assert.ok(!graded.includes('MediaSelectionTests/testInvalidChoiceDoesNotInvalidateObservableSelection'));
});
for (const c of pairs) test(c.id + ' fair complete prompt and unrun answer record', () => {
  assert.equal(hash(fs.readFileSync(c.subject.path)), c.subject.sha256);
  assert.equal(fs.readFileSync(c.subject.path, 'utf8'), c.subject.text);
  assert.doesNotMatch(c.subject.text, /FormMediaState|active = ticket|generation|ROUTING:|controller|NegativeFixtures/);
  assert.match(c.subject.text, /unit tests/); assert.match(c.subject.text, /```swift/);
  const rubric = fs.readFileSync(c.rubric.path, 'utf8');
  assert.equal(hash(rubric), c.rubric.sha256); assert.match(rubric, /Harmless/);
  assert.match(rubric, /correctness and controller execution evidence are separate/);
  assert.deepEqual(c.outputs, {status: 'not-run', attempts: []});
  for (const id of c.testIds) assert.ok(rubric.includes(id));
});
test('reviews distinguish source acceptance from runtime reruns and model lift', () => {
  const first = JSON.stringify(read(base + 'original-review.json'));
  const follow = JSON.stringify(read(base + 'followup-review.json'));
  assert.match(first, /Old Off callbacks/); assert.match(follow, /F1 closed/);
  assert.match(follow, /not executed/); assert.match(follow, /not represented as passed/);
});

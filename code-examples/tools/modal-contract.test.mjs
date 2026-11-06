import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import {fileURLToPath} from 'node:url';
import {nativePlan} from './native-core.mjs';
import {hash} from './contracts.mjs';

const base = new URL('../pilots/uikit-modal-v1/', import.meta.url);
const read = name => fs.readFileSync(new URL(name, base));
const manifest = JSON.parse(read('manifest.json'));

test('modal coverage binds thirteen tests and five scoped negative controls', () => {
  const coverage = JSON.parse(read('coverage.json'));
  const positives = manifest.checks.find(c => c.id === 'modal-unit').testIds;
  assert.equal(manifest.revision, '3');
  assert.equal(positives.length, 13);
  assert.equal(new Set(coverage.assertions.map(a => a.testId)).size, 13);
  assert.deepEqual(coverage.assertions.map(a => a.testId).sort(), [...positives].sort());
  for (const a of coverage.assertions) {
    assert.ok(manifest.claims.some(c => c.id === a.claimId));
    assert.ok(read('Tests/ModalUIKitTests.swift').toString().includes('func ' + a.testId.split('/')[1] + '('));
    assert.equal(a.promptStatus, 'draft-not-gold');
  }
  assert.equal(manifest.checks.filter(c => c.expected === 'failure').length, 5);
  for (const c of manifest.checks) nativePlan(manifest, fileURLToPath(base), c.id);
});

test('modal draft keeps subject question separate from controller artifacts', () => {
  const prompt = JSON.parse(read('evaluation/prompt.json'));
  assert.deepEqual(Object.keys(prompt).sort(), ['id', 'prompt', 'revision']);
  assert.ok(!/NegativeFixtures|testRetained|ROUTING:|FR-01/.test(prompt.prompt));
  const record = JSON.parse(read('evaluation/case.json'));
  assert.equal(record.status, 'draft-independent-review-pending');
  assert.equal(record.split, 'development');
  assert.equal(record.modelRuns, 0);
  assert.deepEqual(record.subjectFiles, ['evaluation/prompt.json']);
  for (const file of record.files) assert.equal(hash(read(file.path)), file.sha256, file.path);
});

test('modal history preserves green-suite gap and actual pre-repair regression', () => {
  const first = JSON.parse(read('validation/revision-1.json'));
  assert.equal(first.manifestHash, hash(read('history/revision-1/manifest.json')));
  assert.ok(first.rows.every(r => r.status === 'passed'));
  const failing = JSON.parse(read('validation/revision-2.json'));
  assert.equal(failing.manifestHash, hash(read('history/revision-2/manifest.json')));
  assert.equal(failing.rows.length, 1);
  const row = failing.rows[0];
  assert.equal(row.expected, 'success');
  assert.equal(row.status, 'failed');
  assert.equal(row.observed, 'failure');
  assert.equal(row.execution.build, 'passed');
  assert.equal(row.execution.infrastructureError, null);
  assert.equal(row.execution.executedTestIds.length, 12);
  assert.deepEqual(row.execution.failedTestIds, ['ModalUIKitTests/testRetainedButRemovedTargetPostsNil']);
  assert.equal(hash(read('history/revision-1/Sources/ModalUIKit.swift')), hash(read('history/revision-2/Sources/ModalUIKit.swift')));
  assert.equal(hash(read('NegativeFixtures/DetachedTarget.swift')), hash(read('history/revision-2/Sources/ModalUIKit.swift')));
  for (const revision of ['1', '2']) {
    const prefix = 'history/revision-' + revision + '/';
    const old = JSON.parse(read(prefix + 'manifest.json'));
    for (const check of old.checks) nativePlan(old, fileURLToPath(new URL(prefix, base)), check.id);
  }
});

test('modal current evidence binds all seven expected outcomes', () => {
  const report = JSON.parse(read('validation/revision-3.json'));
  assert.equal(report.manifestHash, hash(read('manifest.json')));
  assert.equal(report.rows.length, manifest.checks.length);
  assert.equal(new Set(report.rows.map(r => r.check)).size, manifest.checks.length);
  for (const check of manifest.checks) {
    const row = report.rows.find(r => r.check === check.id);
    assert.equal(row.status, 'passed');
    assert.equal(row.observed, check.expected);
    assert.equal(row.execution.build, 'passed');
    assert.equal(row.execution.infrastructureError, null);
    assert.equal(row.execution.skippedTests, 0);
    assert.deepEqual([...row.execution.executedTestIds].sort(), [...check.testIds].sort());
    assert.deepEqual([...row.execution.failedTestIds].sort(), [...check.failureIds].sort());
  }
});

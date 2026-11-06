import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import {fileURLToPath} from 'node:url';
import {nativePlan} from './native-core.mjs';
import {hash} from './contracts.mjs';

const base = new URL('../pilots/uikit-media-inspection-v1/', import.meta.url);
const read = name => fs.readFileSync(new URL(name, base));
const manifest = JSON.parse(read('manifest.json'));

test('media inspection coverage binds nine tests and three mutation checks', () => {
  const coverage = JSON.parse(read('coverage.json'));
  const positive = manifest.checks.find(c => c.id === 'inspection-unit');
  assert.equal(positive.testIds.length, 9);
  assert.deepEqual(coverage.assertions.map(a => a.testId).sort(), [...positive.testIds].sort());
  for (const a of coverage.assertions) {
    assert.ok(manifest.claims.some(c => c.id === a.claimId));
    assert.deepEqual(a.guidelines, ['U-015']);
    assert.equal(a.promptStatus, 'draft-not-gold');
    assert.ok(read('Tests/MediaInspectionTests.swift').toString().includes('func ' + a.testId.split('/')[1] + '('));
  }
  assert.equal(manifest.checks.filter(c => c.expected === 'failure').length, 3);
  for (const check of manifest.checks) nativePlan(manifest, fileURLToPath(base), check.id);
});

test('media inspection subject input stays separate from pinned controller material', () => {
  const prompt = JSON.parse(read('evaluation/prompt.json'));
  assert.deepEqual(Object.keys(prompt).sort(), ['id', 'prompt', 'revision']);
  assert.ok(!/NegativeFixtures|testLoaded|ROUTING:|MI03/.test(prompt.prompt));
  const record = JSON.parse(read('evaluation/case.json'));
  assert.equal(record.status, 'draft-independent-review-pending');
  assert.equal(record.split, 'development');
  assert.equal(record.modelRuns, 0);
  assert.deepEqual(record.subjectFiles, ['evaluation/prompt.json']);
  for (const f of record.files) assert.equal(hash(read(f.path)), f.sha256, f.path);
});

test('media inspection native evidence records exact positive and negative outcomes', () => {
  const report = JSON.parse(read('validation/revision-1.json'));
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

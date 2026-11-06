import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import {fileURLToPath} from 'node:url';
import {nativePlan} from './native-core.mjs';
import {hash} from './contracts.mjs';

const base = new URL('../pilots/uikit-contrast-v1/', import.meta.url);
const read = name => fs.readFileSync(new URL(name, base));
const manifest = JSON.parse(read('manifest.json'));

test('contrast coverage distinguishes Apple claims, W3C math and project policy', () => {
  const coverage = JSON.parse(read('coverage.json'));
  const supplemental = JSON.parse(read('supplemental-sources.json')).sources;
  const positive = manifest.checks.find(c => c.id === 'contrast-unit').testIds;
  assert.equal(positive.length, 9);
  assert.equal(new Set(coverage.assertions.map(a => a.testId)).size, 9);
  assert.deepEqual(coverage.assertions.map(a => a.testId).sort(), [...positive].sort());
  for (const a of coverage.assertions) {
    assert.ok(read('Tests/ContrastUIKitTests.swift').toString().includes('func ' + a.testId.split('/')[1] + '('));
    assert.ok(a.claimIds.length || a.supplementalSourceIds.length || a.policy);
    for (const id of a.claimIds) assert.ok(manifest.claims.some(c => c.id === id));
    for (const id of a.supplementalSourceIds) assert.ok(supplemental.some(s => s.id === id));
    assert.equal(a.promptStatus, 'draft-not-gold');
  }
  assert.ok(supplemental.every(s => new URL(s.url).hostname === 'www.w3.org'));
  assert.equal(manifest.checks.filter(c => c.expected === 'failure').length, 4);
  for (const c of manifest.checks) nativePlan(manifest, fileURLToPath(base), c.id);
});

test('contrast draft pins author material separately from the subject question', () => {
  const prompt = JSON.parse(read('evaluation/prompt.json'));
  assert.deepEqual(Object.keys(prompt).sort(), ['id', 'prompt', 'revision']);
  assert.ok(!/NegativeFixtures|testDynamic|ROUTING:|FR-01/.test(prompt.prompt));
  const record = JSON.parse(read('evaluation/case.json'));
  assert.equal(record.status, 'draft-independent-review-pending');
  assert.equal(record.split, 'development');
  assert.equal(record.modelRuns, 0);
  assert.deepEqual(record.subjectFiles, ['evaluation/prompt.json']);
  for (const file of record.files) assert.equal(hash(read(file.path)), file.sha256, file.path);
});

test('contrast evidence binds six checks and four actual trait observations', () => {
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
    assert.match(row.nativeLogHash, /^[a-f0-9]{64}$/);
    assert.match(row.originalRecordHash, /^[a-f0-9]{64}$/);
  }
  const measurements = report.rows.find(r => r.check === 'contrast-unit').semanticMeasurements;
  assert.equal(measurements.length, 4);
  assert.equal(new Set(measurements.map(m => m.style + '/' + m.contrast)).size, 4);
  assert.ok(measurements.every(m => Number.isFinite(m.ratio) && m.ratio >= 4.5));
});

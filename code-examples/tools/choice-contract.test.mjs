import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import {fileURLToPath} from 'node:url';
import {nativePlan} from './native-core.mjs';
import {hash} from './contracts.mjs';

const base = new URL('../pilots/uikit-choice-v1/', import.meta.url);
const read = name => fs.readFileSync(new URL(name, base));
const manifest = JSON.parse(read('manifest.json'));

test('choice tranche binds nine real tests and four isolated mutants', () => {
  const coverage = JSON.parse(read('coverage.json'));
  const positives = manifest.checks.find(c => c.id === 'choice-unit').testIds;
  assert.equal(positives.length, 9);
  assert.equal(new Set(coverage.assertions.map(a => a.testId)).size, 9);
  assert.deepEqual(coverage.assertions.map(a => a.testId).sort(), [...positives].sort());
  for (const a of coverage.assertions) {
    assert.ok(manifest.claims.some(c => c.id === a.claimId));
    assert.ok(read('Tests/ChoiceUIKitTests.swift').toString().includes('func ' + a.testId.split('/')[1] + '('));
    assert.equal(a.evaluationFamily, 'UPAIR-02');
    assert.equal(a.promptStatus, 'draft-not-gold');
  }
  assert.equal(manifest.checks.filter(c => c.expected === 'failure').length, 4);
  for (const check of manifest.checks) {
    nativePlan(manifest, fileURLToPath(base), check.id);
    if (check.lane === 'unit') assert.ok(check.testIds.every(id => positives.includes(id)));
  }
});

test('choice draft separates subject input from pinned controller material', () => {
  const prompt = JSON.parse(read('evaluation/prompt.json'));
  assert.deepEqual(Object.keys(prompt).sort(), ['id', 'prompt', 'revision']);
  assert.ok(!/NegativeFixtures|testSelection|ROUTING:|FR-01/.test(prompt.prompt));
  const record = JSON.parse(read('evaluation/case.json'));
  assert.equal(record.status, 'draft-independent-review-pending');
  assert.equal(record.split, 'development');
  assert.equal(record.modelRuns, 0);
  for (const file of record.files) assert.equal(hash(read(file.path)), file.sha256, file.path);
  assert.deepEqual(record.subjectFiles, ['evaluation/prompt.json']);
});

test('choice public evidence binds all six exact expected outcomes', () => {
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
});

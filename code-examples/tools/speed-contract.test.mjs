import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import {fileURLToPath} from 'node:url';
import {nativePlan} from './native-core.mjs';
import {hash} from './contracts.mjs';

const base = new URL('../pilots/uikit-speed-v1/', import.meta.url);
const read = p => fs.readFileSync(new URL(p, base));
const manifest = JSON.parse(read('manifest.json'));

test('speed coverage binds eight native methods and three isolated mutants', () => {
  const rows = JSON.parse(read('coverage.json')).assertions;
  const tests = manifest.checks.find(c => c.id === 'speed-unit').testIds;
  assert.equal(tests.length, 8);
  assert.deepEqual(rows.map(r => r.testId).sort(), [...tests].sort());
  for (const r of rows) {
    assert.ok(manifest.claims.some(c => c.id === r.claimId));
    assert.equal(r.promptStatus, 'draft-not-gold');
    assert.ok(read('Tests/PlaybackSpeedTests.swift').toString().includes('func ' + r.testId.split('/')[1] + '('));
  }
  assert.equal(manifest.checks.filter(c => c.expected === 'failure').length, 3);
  for (const c of manifest.checks) nativePlan(manifest, fileURLToPath(base), c.id);
});

test('speed prompt is separated from pinned grading material', () => {
  assert.deepEqual(Object.keys(JSON.parse(read('evaluation/prompt.json'))).sort(), ['id', 'prompt', 'revision']);
  const c = JSON.parse(read('evaluation/case.json'));
  assert.equal(c.status, 'draft-independent-review-pending');
  assert.equal(c.split, 'development');
  assert.equal(c.modelRuns, 0);
  assert.deepEqual(c.subjectFiles, ['evaluation/prompt.json']);
  for (const f of c.files) assert.equal(hash(read(f.path)), f.sha256);
});

test('speed native report binds positive and intended failure outcomes', () => {
  const report = JSON.parse(read('validation/revision-1.json'));
  assert.equal(report.manifestHash, hash(read('manifest.json')));
  assert.equal(report.rows.length, manifest.checks.length);
  assert.equal(new Set(report.rows.map(r => r.check)).size, manifest.checks.length);
  for (const c of manifest.checks) {
    const r = report.rows.find(r => r.check === c.id);
    assert.equal(r.status, 'passed');
    assert.equal(r.observed, c.expected);
    assert.equal(r.execution.infrastructureError, null);
    assert.equal(r.execution.build, 'passed');
    assert.equal(r.execution.skippedTests, 0);
    assert.deepEqual([...r.execution.executedTestIds].sort(), [...c.testIds].sort());
    assert.deepEqual([...r.execution.failedTestIds].sort(), [...c.failureIds].sort());
  }
});

test('speed compile append preserves original sixteen-pilot audit results', () => {
  const a = new URL('../audits/availability-v1/', import.meta.url);
  const json = p => JSON.parse(fs.readFileSync(new URL(p, a)));
  const old = json('history/sweep-1/compile-results.json');
  const current = json('compile-results.json');
  assert.equal(old.rows.length, 16);
  for (const r of old.rows) assert.deepEqual(current.rows.find(c => c.pilot === r.pilot), r);
  assert.equal(old.inventoryHash, hash(fs.readFileSync(new URL('history/sweep-1/inventory.json', a))));
  assert.ok(current.rows.some(r => r.pilot === 'uikit-speed-v1'));
});

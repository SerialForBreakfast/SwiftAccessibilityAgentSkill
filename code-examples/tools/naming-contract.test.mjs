import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import {fileURLToPath} from 'node:url';
import {nativePlan} from './native-core.mjs';
import {hash} from './contracts.mjs';

const base = new URL('../pilots/uikit-naming-v1/', import.meta.url);
const read = name => fs.readFileSync(new URL(name, base));
const manifest = JSON.parse(read('manifest.json'));

test('naming tranche binds eight tests, three mutants and a neutral draft prompt', () => {
  const coverage = JSON.parse(read('coverage.json'));
  const positives = manifest.checks.find(c => c.id === 'naming-unit').testIds;
  assert.equal(positives.length, 8);
  assert.deepEqual(coverage.assertions.map(a => a.testId).sort(), [...positives].sort());
  for (const a of coverage.assertions) {
    assert.ok(manifest.claims.some(c => c.id === a.claimId));
    assert.ok(read('Tests/NamingUIKitTests.swift').toString().includes('func ' + a.testId.split('/')[1] + '('));
    assert.equal(a.promptStatus, 'draft-not-gold');
  }
  assert.equal(manifest.checks.filter(c => c.expected === 'failure').length, 3);
  for (const check of manifest.checks) nativePlan(manifest, fileURLToPath(base), check.id);
  const prompt = JSON.parse(read('evaluation/prompt.json'));
  assert.deepEqual(Object.keys(prompt).sort(), ['id', 'prompt', 'revision']);
  assert.ok(!/NegativeFixtures|testDecoration|ROUTING:|FR-01/.test(prompt.prompt));
});

test('naming public evidence matches manifest and exact expected outcomes', () => {
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
    assert.deepEqual([...row.execution.executedTestIds].sort(), [...check.testIds].sort());
    assert.deepEqual([...row.execution.failedTestIds].sort(), [...check.failureIds].sort());
  }
});

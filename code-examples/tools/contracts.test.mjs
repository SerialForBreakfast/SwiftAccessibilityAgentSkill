// Synthetic records exercise harness contracts, not Apple API behavior.
import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import {spawnSync} from 'node:child_process';
import {fileURLToPath} from 'node:url';
import {hash, artifact, validateManifest, validateResult, appendResult} from './contracts.mjs';

function fixture(t, lane = 'unit', expected = 'success') {
  const root = fs.mkdtempSync(path.join(os.tmpdir(), 'adr003-contract-'));
  t.after(() => fs.rmSync(root, {recursive: true, force: true}));
  fs.writeFileSync(path.join(root, 'example.swift'), '// synthetic example');
  fs.writeFileSync(path.join(root, 'evidence.txt'), 'synthetic evidence');
  const m = {schema: 1, id: 'example', revision: '1', platform: 'iOS', deploymentTarget: '26.0', runtimeMajor: 26,
    limitations: 'Synthetic harness fixture, not native validation.',
    claims: [{id: 'claim', url: 'https://developer.apple.com/documentation/uikit', section: 'Synthetic locator',
      reviewedOn: '2026-11-05', availability: 'Synthetic only', statement: 'Synthetic claim'}],
    files: [{path: 'example.swift', sha256: hash('// synthetic example')}],
    checks: [{id: 'check', lane, expected, claimIds: ['claim'], testIds: lane === 'unit' ? ['Example/test'] : [],
      failureIds: expected === 'failure' ? [lane === 'unit' ? 'Example/test' : 'expected-diagnostic'] : []}]};
  const pin = hash(JSON.stringify(m));
  const r = {schema: 1, runId: 'synthetic-run', manifestHash: pin, recordedAt: '2026-11-05T12:00:00Z',
    sourceRevision: 'synthetic', provenance: 'synthetic', checkId: 'check', status: 'passed', observed: expected,
    environment: {platform: 'iOS', deploymentTarget: '26.0', xcode: 'synthetic', compiler: 'synthetic',
      sdkVersion: '27.0', sdkBuild: 'synthetic', architecture: 'arm64', destinationType: 'simulator',
      runtimeVersion: lane === 'unit' ? '26.5' : null, runtimeBuild: lane === 'unit' ? 'synthetic' : null},
    command: ['not-executed'], artifacts: [{path: 'evidence.txt', sha256: hash('synthetic evidence')}],
    execution: {exitCode: expected === 'success' ? 0 : 1, signal: null, infrastructureError: null,
      build: lane === 'unit' || expected === 'success' ? 'passed' : 'failed', skippedTests: 0,
      executedTestIds: lane === 'unit' ? ['Example/test'] : [],
      failedTestIds: lane === 'unit' && expected === 'failure' ? ['Example/test'] : [],
      diagnosticIds: lane === 'compile' && expected === 'failure' ? ['expected-diagnostic'] : []}};
  return {root, m, r, pin, validate: () => validateResult(m, pin, r, root)};
}

for (const lane of ['compile', 'unit']) for (const expected of ['success', 'failure']) {
  test(`${lane} validates exact ${expected} evidence`, t => {
    const f = fixture(t, lane, expected); validateManifest(f.m, f.root); f.validate();
  });
}
for (const [name, mutate] of [
  ['wrong platform', f => f.r.environment.platform = 'tvOS'],
  ['wrong runtime major', f => f.r.environment.runtimeVersion = '27.0'],
  ['missing SDK identity', f => delete f.r.environment.sdkBuild],
  ['changed manifest', f => f.r.manifestHash = 'b'.repeat(64)],
  ['zero tests', f => f.r.execution.executedTestIds = []],
  ['wrong test', f => f.r.execution.executedTestIds = ['Other/test']],
  ['duplicate test', f => f.r.execution.executedTestIds.push('Example/test')],
  ['skipped test as pass', f => f.r.execution.skippedTests = 1],
  ['build failure as pass', f => f.r.execution.build = 'failed'],
  ['timeout as pass', f => f.r.execution.infrastructureError = 'ETIMEDOUT'],
  ['signal as pass', f => f.r.execution.signal = 'SIGKILL'],
  ['changed artifact', f => fs.writeFileSync(path.join(f.root, 'evidence.txt'), 'changed')],
  ['failed test outside selection', f => f.r.execution.failedTestIds = ['Other/test']],
]) test('rejects ' + name, t => {const f = fixture(t); mutate(f); assert.throws(f.validate);});

test('unrelated compile error is a failed expectation, not a negative pass', t => {
  const f = fixture(t, 'compile', 'failure');
  f.r.execution.diagnosticIds = ['unrelated-syntax-error'];
  assert.throws(f.validate); f.r.status = 'failed'; f.validate();
});
test('surviving unit mutation is preserved as failed', t => {
  const f = fixture(t, 'unit', 'failure');
  Object.assign(f.r.execution, {exitCode: 0, failedTestIds: []});
  assert.throws(f.validate); Object.assign(f.r, {observed: 'success', status: 'failed'}); f.validate();
});
for (const status of ['blocked', 'error', 'skipped']) test(status + ' cannot imply an observation', t => {
  const f = fixture(t); f.r.status = status; f.r.reason = 'declared limitation';
  assert.throws(f.validate); f.r.observed = 'not-assessed';
  if (status === 'skipped') {assert.throws(f.validate); f.m.checks[0].skipCondition = f.r.reason;}
  f.validate();
});
test('rejects traversal, absolute paths and symlink escape', t => {
  const f = fixture(t);
  for (const p of ['../example.swift', '/etc/passwd', '..\\example.swift']) assert.throws(() => artifact(f.root, {path: p, sha256: hash('x')}));
  fs.symlinkSync(os.tmpdir(), path.join(f.root, 'escape'));
  assert.throws(() => artifact(f.root, {path: 'escape', sha256: hash('x')}));
});
test('rejects unresolved claims, UI lanes and disguised Apple domains', t => {
  for (const change of [m => m.checks[0].claimIds = ['missing'], m => m.checks[0].lane = 'ui',
    m => m.claims[0].url = 'https://apple.com.example.org/docs']) {
    const f = fixture(t); change(f.m); assert.throws(() => validateManifest(f.m, f.root));
  }
});
test('ledger preserves existing records and symlink targets', t => {
  const f = fixture(t), ledger = path.join(f.root, 'ledger'); f.validate();
  const file = appendResult(ledger, f.r, f.root), original = fs.readFileSync(file);
  assert.throws(() => appendResult(ledger, f.r, f.root)); assert.deepEqual(fs.readFileSync(file), original);
  fs.unlinkSync(path.join(f.root, 'evidence.txt'));
  validateResult(f.m, f.pin, JSON.parse(original), path.dirname(file));
  f.r.runId = 'alias'; fs.symlinkSync(path.dirname(file), path.join(ledger, 'alias'));
  assert.throws(() => appendResult(ledger, f.r, f.root)); assert.deepEqual(fs.readFileSync(file), original);
});
test('CLI plans only and records no execution', t => {
  const f = fixture(t), manifest = path.join(f.root, 'manifest.json');
  fs.writeFileSync(manifest, JSON.stringify(f.m));
  const cli = fileURLToPath(new URL('./cli.mjs', import.meta.url));
  const result = spawnSync(process.execPath, [cli, 'plan', manifest], {encoding: 'utf8'});
  assert.equal(result.status, 0); assert.equal(JSON.parse(result.stdout).execution, false);
  const rejected = spawnSync(process.execPath, [cli, 'execute', manifest], {encoding: 'utf8'});
  assert.notEqual(rejected.status, 0);
  const record = path.join(f.root, 'input-result.json'), ledger = path.join(f.root, 'saved');
  fs.writeFileSync(record, JSON.stringify(f.r));
  const saved = spawnSync(process.execPath, [cli, 'record', manifest, record, ledger], {encoding: 'utf8'});
  assert.equal(saved.status, 0, saved.stderr);
  const receipt = JSON.parse(saved.stdout); assert.equal(receipt.execution, false);
  validateResult(f.m, f.pin, JSON.parse(fs.readFileSync(receipt.file)), path.dirname(receipt.file));
  const duplicate = spawnSync(process.execPath, [cli, 'record', manifest, record, ledger], {encoding: 'utf8'});
  assert.notEqual(duplicate.status, 0);
});

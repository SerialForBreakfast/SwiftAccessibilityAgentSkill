import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import {hash} from './contracts.mjs';
import {fingerprint, requireSame, inventory, verifyInputs, classify} from './campaign-core.mjs';

test('fingerprint distinguishes SDK/runtime/source settings', () => {
  assert.notEqual(fingerprint({sdk: '27', runtime: '26.5'}), fingerprint({sdk: '27', runtime: '26.6'}));
  assert.throws(() => requireSame({sdk: '27'}, {sdk: '26'}, 'drift'), /drift/);
  requireSame({sdk: '27'}, {sdk: '27'}, 'drift');
});
for (const [status, expected, result] of [
  ['passed', 'success', 'positive-pass'], ['passed', 'failure', 'intended-negative-rejection'],
  ['failed', 'success', 'unexpected-contract-failure'], ['failed', 'failure', 'negative-oracle-disagreement'],
  ['error', 'failure', 'infrastructure-or-unassessed'], ['blocked', 'success', 'infrastructure-or-unassessed'],
  ['skipped', 'success', 'infrastructure-or-unassessed']
]) test(`${status}/${expected} is classified without hiding first failure`, () => {
  assert.equal(classify({status}, {expected}), result);
});
test('source tampering is rejected on resume', t => {
  const root = fs.mkdtempSync(path.join(os.tmpdir(), 'campaign-offline-'));
  t.after(() => fs.rmSync(root, {recursive: true, force: true}));
  fs.writeFileSync(path.join(root, 'source'), 'first');
  const inputs = [{path: 'source', sha256: hash('first')}];
  verifyInputs(root, inputs);
  fs.writeFileSync(path.join(root, 'source'), 'repair');
  assert.throws(() => verifyInputs(root, inputs), /Frozen input changed/);
});
test('inventory rejects a non-UIKit/OS26 package', t => {
  const root = fs.mkdtempSync(path.join(os.tmpdir(), 'campaign-inventory-'));
  t.after(() => fs.rmSync(root, {recursive: true, force: true}));
  fs.mkdirSync(path.join(root, 'pkg'));
  fs.writeFileSync(path.join(root, 'pkg', 'source.swift'), 'import UIKit');
  const manifest = {schema: 1, id: 'synthetic', revision: '1', platform: 'macOS', deploymentTarget: '26.0', runtimeMajor: 26,
    limitations: 'synthetic only', claims: [{id: 'c', url: 'https://developer.apple.com/documentation/uikit',
      statement: 'synthetic', section: 'synthetic', availability: 'synthetic', reviewedOn: '2026-11-06'}],
    files: [{path: 'source.swift', sha256: hash('import UIKit')}],
    checks: [{id: 'compile', lane: 'compile', expected: 'success', claimIds: ['c'], testIds: [], failureIds: []}]};
  fs.writeFileSync(path.join(root, 'pkg', 'manifest.json'), JSON.stringify(manifest));
  assert.throws(() => inventory(root, ['pkg']), /UIKit OS26 scope/);
  manifest.platform = 'iOS';
  fs.writeFileSync(path.join(root, 'pkg', 'manifest.json'), JSON.stringify(manifest));
  const plan = inventory(root, ['pkg']);
  assert.equal(plan.packages.length, 1);
  assert.equal(plan.checks.length, 1);
  assert.equal(plan.inputs.length, 2);
});

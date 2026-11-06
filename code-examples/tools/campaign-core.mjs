import fs from 'node:fs';
import path from 'node:path';
import {hash, validateManifest, validateResult} from './contracts.mjs';

export function fingerprint(value) { return hash(JSON.stringify(value)); }
export function requireSame(actual, expected, message) {
  if (fingerprint(actual) !== fingerprint(expected)) throw Error(message);
}
export function selectedPackages(root) {
  const base = 'code-examples/pilots';
  return [...fs.readdirSync(path.join(root, base)).filter(n =>
    fs.existsSync(path.join(root, base, n, 'manifest.json'))).sort().map(n => `${base}/${n}`),
    'research/evaluation/failure-driven/checkout-contract-v1'];
}
export function inventory(root, directories) {
  const inputs = [], checks = [], packages = [];
  for (const directory of directories) {
    const manifestPath = `${directory}/manifest.json`;
    const bytes = fs.readFileSync(path.join(root, manifestPath));
    const m = validateManifest(JSON.parse(bytes), path.join(root, directory));
    if (m.platform !== 'iOS' || m.runtimeMajor !== 26) throw Error('UIKit OS26 scope required');
    const key = `p${String(packages.length + 1).padStart(2, '0')}`;
    inputs.push({path: manifestPath, sha256: hash(bytes)});
    for (const f of m.files) inputs.push({path: `${directory}/${f.path}`, sha256: f.sha256});
    packages.push({key, path: directory, manifestHash: hash(bytes), id: m.id});
    for (const c of m.checks) checks.push({key: `${key}-${c.id}`, package: key, check: c.id,
      lane: c.lane, expected: c.expected, testIds: c.testIds, failureIds: c.failureIds});
  }
  return {inputs, packages, checks};
}
export function verifyInputs(root, inputs) {
  for (const input of inputs) {
    if (hash(fs.readFileSync(path.join(root, input.path))) !== input.sha256)
      throw Error('Frozen input changed: ' + input.path);
  }
}
export function classify(record, check) {
  if (['error', 'blocked', 'skipped'].includes(record.status)) return 'infrastructure-or-unassessed';
  if (record.status === 'passed') return check.expected === 'failure' ? 'intended-negative-rejection' : 'positive-pass';
  return check.expected === 'failure' ? 'negative-oracle-disagreement' : 'unexpected-contract-failure';
}
export function verifyReceipt(manifest, manifestHash, record, output, expectedEnvironment) {
  validateResult(manifest, manifestHash, record, output);
  if (record.environment) {
    for (const key of ['xcode', 'compiler', 'sdkVersion', 'sdkBuild', 'architecture']) {
      if (record.environment[key] !== expectedEnvironment[key]) throw Error('Result environment drift: ' + key);
    }
    if (record.environment.destinationType === 'simulator') {
      for (const key of ['runtimeVersion', 'runtimeBuild'])
        if (record.environment[key] !== expectedEnvironment[key]) throw Error('Result runtime drift');
    }
  }
}

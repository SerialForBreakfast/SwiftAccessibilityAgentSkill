// Offline ADR-003 contracts. Validation never executes a manifest command.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';

export const hash = bytes => crypto.createHash('sha256').update(bytes).digest('hex');
const requireValue = (ok, message) => { if (!ok) throw Error(message); };
const text = value => typeof value === 'string' && value.trim().length > 0;
const id = value => typeof value === 'string' && /^[a-z0-9][a-z0-9._-]*$/i.test(value);
const same = (a, b) => JSON.stringify([...a].sort()) === JSON.stringify([...b].sort());
function strings(values) {
  return Array.isArray(values) && values.every(text) && new Set(values).size === values.length;
}
export function artifact(root, item) {
  requireValue(item && text(item.path) && !path.isAbsolute(item.path) &&
    !item.path.split(/[\\/]/).some(p => p === '..' || p === '.') &&
    !item.path.includes('\\'), 'Unsafe artifact path');
  const base = fs.realpathSync(root), resolved = fs.realpathSync(path.join(base, item.path));
  requireValue(resolved.startsWith(base + path.sep) && fs.statSync(resolved).isFile(), 'Artifact escapes root or is not a file');
  requireValue(/^[a-f0-9]{64}$/.test(item.sha256 ?? '') &&
    hash(fs.readFileSync(resolved)) === item.sha256, 'Artifact hash mismatch');
  return resolved;
}

export function validateManifest(manifest, root) {
  requireValue(manifest?.schema === 1 && id(manifest.id) && id(manifest.revision), 'Invalid manifest identity');
  requireValue(['iOS', 'tvOS', 'macOS', 'visionOS', 'watchOS'].includes(manifest.platform), 'Invalid platform');
  requireValue(/^\d+\.\d+(\.\d+)?$/.test(manifest.deploymentTarget ?? '') &&
    Number.isInteger(manifest.runtimeMajor) && manifest.runtimeMajor > 0, 'Invalid target/runtime');
  requireValue(text(manifest.limitations) && manifest.claims?.length > 0, 'Missing bounded claims');
  for (const claim of manifest.claims) {
    const url = new URL(claim.url);
    requireValue(id(claim.id) && text(claim.statement) && text(claim.section) && text(claim.availability) &&
      /^\d{4}-\d{2}-\d{2}$/.test(claim.reviewedOn ?? '') &&
      url.protocol === 'https:' && (url.hostname === 'apple.com' || url.hostname.endsWith('.apple.com')) &&
      !url.username && !url.password, 'Invalid Apple claim provenance');
  }
  requireValue(new Set(manifest.claims.map(c => c.id)).size === manifest.claims.length, 'Duplicate claim ID');
  requireValue(manifest.files?.length > 0 && new Set(manifest.files.map(f => f.path)).size === manifest.files.length, 'Missing or duplicate source files');
  manifest.files.forEach(f => artifact(root, f));
  requireValue(manifest.checks?.length > 0 && new Set(manifest.checks.map(c => c.id)).size === manifest.checks.length, 'Missing or duplicate checks');
  for (const check of manifest.checks) {
    requireValue(id(check.id) && ['compile', 'unit'].includes(check.lane) &&
      ['success', 'failure'].includes(check.expected), 'Invalid check');
    requireValue(strings(check.claimIds) && check.claimIds.length > 0 &&
      check.claimIds.every(c => manifest.claims.some(x => x.id === c)), 'Unresolved claim');
    requireValue(strings(check.testIds) && strings(check.failureIds), 'Invalid test/failure IDs');
    requireValue(check.lane === 'unit' ? check.testIds.length > 0 : check.testIds.length === 0, 'Invalid test selection');
    requireValue(check.expected === 'failure' ? check.failureIds.length > 0 : check.failureIds.length === 0, 'Missing or unexpected negative expectation');
    if (check.lane === 'unit') requireValue(check.failureIds.every(x => check.testIds.includes(x)), 'Failure outside selected tests');
  }
  return manifest;
}

export function validateResult(manifest, manifestHash, record, evidenceRoot) {
  requireValue(record?.schema === 1 && id(record.runId) && record.manifestHash === manifestHash &&
    /^[a-f0-9]{64}$/.test(manifestHash), 'Invalid result identity');
  requireValue(text(record.recordedAt) && Number.isFinite(Date.parse(record.recordedAt)) &&
    text(record.sourceRevision) && ['maintainer', 'user-rerun', 'synthetic'].includes(record.provenance), 'Missing run provenance');
  const check = manifest.checks.find(c => c.id === record.checkId);
  requireValue(check, 'Unknown check');
  requireValue(['passed', 'failed', 'skipped', 'blocked', 'error'].includes(record.status), 'Invalid result status');
  if (['blocked', 'skipped', 'error'].includes(record.status)) {
    requireValue(text(record.reason) && record.observed === 'not-assessed', 'Non-result requires reason and no capability conclusion');
    if (record.status === 'skipped') requireValue(text(check.skipCondition) && record.reason === check.skipCondition, 'Undeclared skip');
    return record;
  }
  const env = record.environment;
  requireValue(env && env.platform === manifest.platform && env.deploymentTarget === manifest.deploymentTarget &&
    ['xcode', 'compiler', 'sdkVersion', 'sdkBuild', 'architecture', 'destinationType'].every(k => text(env[k])), 'Missing or mismatched toolchain');
  if (check.lane === 'unit') requireValue(text(env.runtimeVersion) &&
    Number(env.runtimeVersion.split('.')[0]) === manifest.runtimeMajor && text(env.runtimeBuild), 'Missing or wrong runtime');
  else requireValue(env.runtimeVersion === null && env.runtimeBuild === null, 'Compile-only result must not claim runtime execution');
  requireValue(Array.isArray(record.command) && record.command.length > 0 && record.command.every(text), 'Missing recorded command');
  requireValue(record.artifacts?.length > 0, 'Missing evidence artifacts');
  record.artifacts.forEach(a => artifact(evidenceRoot, a));
  const run = record.execution;
  requireValue(run && Number.isInteger(run.exitCode) && run.signal === null && run.infrastructureError === null &&
    strings(run.executedTestIds) && strings(run.failedTestIds) && strings(run.diagnosticIds) &&
    Number.isInteger(run.skippedTests) && run.skippedTests === 0, 'Incomplete or infrastructure execution');
  if (check.lane === 'unit') {
    requireValue(run.build === 'passed' && same(run.executedTestIds, check.testIds) &&
      run.failedTestIds.every(t => run.executedTestIds.includes(t)) && run.diagnosticIds.length === 0, 'Unit build or test selection mismatch');
  } else requireValue(run.executedTestIds.length === 0 && run.failedTestIds.length === 0 &&
    ['passed', 'failed'].includes(run.build), 'Invalid compile execution');
  const failures = check.lane === 'unit' ? run.failedTestIds : run.diagnosticIds;
  const succeeded = run.exitCode === 0;
  requireValue(succeeded ? failures.length === 0 && run.build === 'passed' : failures.length > 0, 'Exit/outcome mismatch');
  if (check.lane === 'compile') requireValue(succeeded === (run.build === 'passed'), 'Compile build mismatch');
  const expected = check.expected === 'success' ? succeeded : !succeeded && same(failures, check.failureIds);
  requireValue(record.observed === (succeeded ? 'success' : 'failure') &&
    record.status === (expected ? 'passed' : 'failed'), 'Misclassified result');
  return record;
}

export function appendResult(directory, record, evidenceRoot) {
  requireValue(id(record.runId), 'Unsafe run ID');
  // Callers validate first. Exclusive creation prevents replacing historical evidence.
  fs.mkdirSync(directory, {recursive: true, mode: 0o700});
  const runDirectory = path.join(fs.realpathSync(directory), record.runId);
  fs.mkdirSync(runDirectory, {mode: 0o700});
  // An interrupted copy leaves an incomplete directory, never a successful receipt.
  const saved = structuredClone(record);
  saved.artifacts = (record.artifacts ?? []).map((item, index) => {
    const bytes = fs.readFileSync(artifact(evidenceRoot, item));
    requireValue(hash(bytes) === item.sha256, 'Artifact changed during copy');
    const name = `artifact-${index}.bin`;
    fs.writeFileSync(path.join(runDirectory, name), bytes, {flag: 'wx', mode: 0o600});
    return {path: name, originalPath: item.path, sha256: item.sha256};
  });
  const file = path.join(runDirectory, 'result.json');
  const fd = fs.openSync(file, 'wx', 0o600);
  try { fs.writeFileSync(fd, JSON.stringify(saved, null, 2) + '\n'); fs.fsyncSync(fd); }
  finally { fs.closeSync(fd); }
  return file;
}

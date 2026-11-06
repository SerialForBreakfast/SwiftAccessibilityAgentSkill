// One explicitly authorized sequential campaign. No models, installs or repairs.
import fs from 'node:fs';
import path from 'node:path';
import os from 'node:os';
import {fileURLToPath} from 'node:url';
import {spawnSync} from 'node:child_process';
import {hash} from './contracts.mjs';
import {selectDestination} from './native-core.mjs';
import {inventory, selectedPackages, verifyInputs, requireSame, classify, verifyReceipt} from './campaign-core.mjs';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '../..');
const [mode, output, uuid, ...extra] = process.argv.slice(2);
if (!['freeze', 'run'].includes(mode) || !output || !path.isAbsolute(output) || !uuid || extra.length)
  throw Error('Usage: campaign.mjs freeze|run NEW_OR_EXISTING_PRIVATE_ROOT IOS26_UUID');
function probe(command, args) {
  const r = spawnSync(command, args, {encoding: 'utf8', timeout: 120000});
  if (r.status !== 0 || r.error || r.signal) throw Error('Environment probe failed: ' + command);
  return r.stdout.trim();
}
function environment() {
  const destination = selectDestination(JSON.parse(probe('xcrun', ['simctl', 'list', 'devices', 'available', '--json'])),
    JSON.parse(probe('xcrun', ['simctl', 'list', 'runtimes', '--json'])), uuid, 26);
  return {xcode: probe('xcodebuild', ['-version']), compiler: probe('xcrun', ['swiftc', '--version']),
    sdkVersion: probe('xcrun', ['--sdk', 'iphonesimulator', '--show-sdk-version']),
    sdkBuild: probe('xcrun', ['--sdk', 'iphonesimulator', '--show-sdk-build-version']),
    architecture: os.arch(), runtimeVersion: destination.version, runtimeBuild: destination.build, uuid};
}
const adapters = ['native.mjs', 'native-core.mjs', 'contracts.mjs', 'campaign.mjs', 'campaign-core.mjs']
  .map(n => ({path: 'code-examples/tools/' + n, sha256: hash(fs.readFileSync(path.join(root, 'code-examples/tools', n)))}));
if (mode === 'freeze') {
  const plan = {schema: 1, createdAt: new Date().toISOString(), environment: environment(),
    ...inventory(root, selectedPackages(root)), adapters};
  fs.mkdirSync(output, {mode: 0o700});
  for (const f of [...plan.inputs, ...adapters]) {
    const destination = path.join(output, 'snapshot', f.path);
    fs.mkdirSync(path.dirname(destination), {recursive: true});
    fs.writeFileSync(destination, fs.readFileSync(path.join(root, f.path)), {flag: 'wx', mode: 0o600});
  }
  const bytes = JSON.stringify(plan, null, 2) + '\n';
  fs.writeFileSync(path.join(output, 'plan.json'), bytes, {flag: 'wx', mode: 0o600});
  fs.writeFileSync(path.join(output, 'plan.sha256'), hash(bytes), {flag: 'wx', mode: 0o600});
  console.log(JSON.stringify({status: 'frozen-not-executed', packages: plan.packages.length, checks: plan.checks.length}));
} else {
  const planBytes = fs.readFileSync(path.join(output, 'plan.json'));
  if (hash(planBytes) !== fs.readFileSync(path.join(output, 'plan.sha256'), 'utf8')) throw Error('Plan hash mismatch');
  const plan = JSON.parse(planBytes);
  requireSame(environment(), plan.environment, 'Environment fingerprint mismatch');
  requireSame(adapters, plan.adapters, 'Adapter fingerprint mismatch');
  verifyInputs(root, plan.inputs);
  verifyInputs(path.join(output, 'snapshot'), [...plan.inputs, ...plan.adapters]);
  const lock = path.join(output, 'execution.lock');
  if (fs.existsSync(lock)) {
    const prior = JSON.parse(fs.readFileSync(lock));
    if (prior.host !== os.hostname() || !Number.isInteger(prior.pid) || prior.pid <= 0) throw Error('Unverifiable campaign lock');
    try { process.kill(prior.pid, 0); throw Error('Campaign already running'); }
    catch (error) {
      if (error.code !== 'ESRCH') throw error;
      fs.renameSync(lock, path.join(output, `abandoned-lock-${Date.now()}.json`));
    }
  }
  fs.writeFileSync(lock, JSON.stringify({pid: process.pid, host: os.hostname(), started: new Date().toISOString()}), {flag: 'wx'});
  const rows = [];
  try {
    for (const check of plan.checks) {
      const pkg = plan.packages.find(p => p.key === check.package);
      const manifestPath = path.join(output, 'snapshot', pkg.path, 'manifest.json');
      const manifest = JSON.parse(fs.readFileSync(manifestPath));
      const run = path.join(output, check.key);
      const resultPath = path.join(run, 'result.json');
      if (fs.existsSync(run) && !fs.existsSync(resultPath)) throw Error('Interrupted attempt retained: ' + check.key);
      if (!fs.existsSync(resultPath)) {
        verifyInputs(root, plan.inputs);
        const r = spawnSync(process.execPath, [path.join(output, 'snapshot/code-examples/tools/native.mjs'),
          'execute', manifestPath, check.check, run, uuid], {encoding: 'utf8', timeout: 900000, maxBuffer: 4 * 1024 * 1024});
        fs.writeFileSync(path.join(output, check.key + '-adapter-process.json'), JSON.stringify({exitCode: r.status,
          signal: r.signal, error: r.error?.code ?? null, stdout: r.stdout, stderr: r.stderr}), {flag: 'wx', mode: 0o600});
        if (r.error || r.signal || !fs.existsSync(resultPath)) throw Error('Adapter infrastructure failure: ' + check.key);
      }
      const record = JSON.parse(fs.readFileSync(resultPath));
      if (record.checkId !== check.check) throw Error('Receipt check mismatch');
      verifyReceipt(manifest, pkg.manifestHash, record, run, plan.environment);
      const row = {key: check.key, package: pkg.path, check: check.check, lane: check.lane, expected: check.expected,
        status: record.status, observed: record.observed, classification: classify(record, check),
        resultHash: hash(fs.readFileSync(resultPath)), execution: record.execution ?? null};
      rows.push(row); console.log(JSON.stringify(row));
      if (row.classification === 'infrastructure-or-unassessed') throw Error('Stop after infrastructure/unassessed result: ' + check.key);
    }
    console.log(JSON.stringify({status: 'execution-complete', checks: rows.length}));
  } finally {
    // Index is a derived view; original per-attempt receipts are never rewritten.
    fs.writeFileSync(path.join(output, 'index.json'), JSON.stringify({schema: 1, rows,
      remaining: plan.checks.length - rows.length}, null, 2) + '\n', {mode: 0o600});
    fs.unlinkSync(lock);
  }
}

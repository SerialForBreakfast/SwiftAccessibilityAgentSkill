import {classifyUnitFailure} from './swiftui-media-diagnostics.mjs';
// Explicit native execution only. Never executes commands supplied by a manifest.
import fs from 'node:fs';
import path from 'node:path';
import os from 'node:os';
import {spawnSync} from 'node:child_process';
import {hash, artifact, validateResult} from './contracts.mjs';
import {nativePlan, selectDestination, compileOutcome, unitOutcome, packageSource} from './native-core.mjs';

const [mode, manifestFile, checkId, output, uuid, ...extra] = process.argv.slice(2);
if (!['plan', 'execute'].includes(mode) || !manifestFile || !checkId || extra.length ||
    (mode === 'plan' && (output || uuid)) || (mode === 'execute' && (!output || !path.isAbsolute(output)))) {
  throw Error('Usage: native.mjs plan MANIFEST CHECK | execute MANIFEST CHECK NEW_PRIVATE_OUTPUT [IOS_UUID]');
}
const manifestBytes = fs.readFileSync(manifestFile), manifest = JSON.parse(manifestBytes);
const root = path.dirname(path.resolve(manifestFile));
const plan = nativePlan(manifest, root, checkId), check = plan.check;
if (mode === 'plan') {console.log(JSON.stringify(plan, null, 2)); process.exit(0);}
if (fs.existsSync(output)) throw Error('Output must be new; previous runs are immutable');
fs.mkdirSync(output, {mode: 0o700});
const evidence = [];
function save(name, bytes) {
  fs.writeFileSync(path.join(output, name), bytes, {flag: 'wx', mode: 0o600});
  evidence.push({path: name, sha256: hash(bytes)});
}
function invoke(executable, args, cwd = output) {
  return spawnSync(executable, args, {cwd, encoding: 'utf8', timeout: executable === 'xcodebuild' ? 600000 : 120000,
    killSignal: 'SIGKILL', maxBuffer: 32 * 1024 * 1024});
}
function probe(name, executable, args) {
  const result = invoke(executable, args);
  save(name, (result.stdout ?? '') + (result.stderr ?? ''));
  if (result.status !== 0 || result.error || result.signal) throw Error('Preflight unavailable: ' + name);
  return result.stdout.trim();
}
const record = {schema: 1, runId: checkId + '-' + Date.now(), manifestHash: hash(manifestBytes), checkId,
  recordedAt: new Date().toISOString(), sourceRevision: 'manifest-sha256:' + hash(manifestBytes),
  provenance: 'maintainer', status: 'blocked', observed: 'not-assessed', artifacts: evidence};
let phase = 'preflight';
try {
  save('manifest.json', manifestBytes);
  for (const name of ['native.mjs', 'native-core.mjs', 'contracts.mjs', 'swiftui-media-diagnostics.mjs']) {
    save('adapter-' + name, fs.readFileSync(new URL(name, import.meta.url)));
  }
  // Snapshot only listed, verified inputs; no dependency resolution or arbitrary Package.swift.
  const workspace = path.join(output, 'workspace'); fs.mkdirSync(workspace);
  const snapshots = new Map();
  for (const input of manifest.files) {
    const bytes = fs.readFileSync(artifact(root, input));
    if (hash(bytes) !== input.sha256) throw Error('Input changed while copying');
    const relative = 'inputs/' + input.path;
    fs.mkdirSync(path.dirname(path.join(output, relative)), {recursive: true});
    save(relative, bytes); snapshots.set(input.path, bytes);
  }
  for (const input of plan.inputs) {
    const folder = input.path.startsWith('Sources/') ? 'Sources/AccessibilityExamples' : 'Tests/AccessibilityExamplesTests';
    const destination = path.join(workspace, folder, path.basename(input.path));
    fs.mkdirSync(path.dirname(destination), {recursive: true});
    const source = check.replacement?.target === input.path ? check.replacement.source : input.path;
    fs.writeFileSync(destination, snapshots.get(source));
  }
  const packageBytes = packageSource(manifest.deploymentTarget);
  fs.writeFileSync(path.join(workspace, 'Package.swift'), packageBytes); save('generated-package.swift', packageBytes);
  const xcode = probe('xcode.txt', 'xcodebuild', ['-version']);
  const compiler = probe('compiler.txt', 'xcrun', ['swiftc', '--version']);
  const sdkPath = probe('sdk-path.txt', 'xcrun', ['--sdk', 'iphonesimulator', '--show-sdk-path']);
  const sdkVersion = probe('sdk-version.txt', 'xcrun', ['--sdk', 'iphonesimulator', '--show-sdk-version']);
  const sdkBuild = probe('sdk-build.txt', 'xcrun', ['--sdk', 'iphonesimulator', '--show-sdk-build-version']);
  const architecture = os.arch() === 'arm64' ? 'arm64' : os.arch() === 'x64' ? 'x86_64' : null;
  if (!architecture) throw Error('Unsupported architecture');
  let destination = null;
  if (check.lane === 'unit') {
    const devices = JSON.parse(probe('devices.json', 'xcrun', ['simctl', 'list', 'devices', 'available', '--json']));
    const runtimes = JSON.parse(probe('runtimes.json', 'xcrun', ['simctl', 'list', 'runtimes', '--json']));
    destination = {...selectDestination(devices, runtimes, uuid, manifest.runtimeMajor), uuid};
  }
  record.environment = {platform: manifest.platform, deploymentTarget: manifest.deploymentTarget,
    xcode, compiler, sdkVersion, sdkBuild, architecture, destinationType: check.lane === 'unit' ? 'simulator' : 'compile-only',
    runtimeVersion: destination?.version ?? null, runtimeBuild: destination?.build ?? null};
  let executable, args;
  if (check.lane === 'compile') {
    executable = 'xcrun';
    const sources = check.compileSources ? check.compileSources.map(f => path.join(output, 'inputs', f)) :
      plan.inputs.filter(f => f.path.startsWith('Sources/')).map(f => path.join(workspace, 'Sources/AccessibilityExamples', path.basename(f.path)));
    args = ['swiftc', '-sdk', sdkPath, '-target', `${architecture}-apple-ios${manifest.deploymentTarget}-simulator`,
      '-typecheck', '-parse-as-library', '-module-name', 'AccessibilityExamples', '-module-cache-path', path.join(output, 'ModuleCache'), ...sources];
  } else {
    executable = 'xcodebuild';
    args = ['test', '-scheme', 'AccessibilityExamples', '-destination', `platform=iOS Simulator,id=${uuid}`,
      '-derivedDataPath', path.join(output, 'DerivedData'), '-resultBundlePath', path.join(output, 'tests.xcresult'),
      '-parallel-testing-enabled', 'NO', '-collect-test-diagnostics', 'never',
      ...check.testIds.map(id => '-only-testing:AccessibilityExamplesTests/' + id), 'CODE_SIGNING_ALLOWED=NO'];
  }
  record.command = [executable, ...args];
  save('intent.json', JSON.stringify({manifestHash: record.manifestHash, check, environment: record.environment, command: record.command}, null, 2));
  phase = 'execution';
  const result = invoke(executable, args, workspace);
  const log = (result.stdout ?? '') + (result.stderr ?? ''); save('native.log', log);
  save('process.json', JSON.stringify({exitCode: result.status, signal: result.signal, error: result.error?.code ?? null}));
  if (check.lane === 'compile') record.execution = compileOutcome(result, log, check);
  else {
    const summaryResult = invoke('xcrun', ['xcresulttool', 'get', 'test-results', 'summary', '--path', path.join(output, 'tests.xcresult'), '--format', 'json']);
    save('summary-process.txt', (summaryResult.stdout ?? '') + (summaryResult.stderr ?? ''));
    if (summaryResult.status !== 0 || summaryResult.error || summaryResult.signal) throw Error('Missing readable xcresult summary');
    const summary = JSON.parse(summaryResult.stdout); save('summary.json', JSON.stringify(summary, null, 2));
    const diagnosis = classifyUnitFailure(result, log, summary);
    if (diagnosis) { record.failureClassification = diagnosis; throw Error(diagnosis.kind + '; zero credited tests'); }
    record.execution = unitOutcome(result, log, summary, check, destination);
  }
  record.observed = result.status === 0 ? 'success' : 'failure';
  const failures = check.lane === 'unit' ? record.execution.failedTestIds : record.execution.diagnosticIds;
  record.status = record.observed === check.expected &&
    JSON.stringify([...failures].sort()) === JSON.stringify([...check.failureIds].sort()) ? 'passed' : 'failed';
  validateResult(manifest, hash(manifestBytes), record, output);
} catch (error) {
  record.status = phase === 'preflight' ? 'blocked' : 'error'; record.observed = 'not-assessed'; record.reason = error.message;
}
fs.writeFileSync(path.join(output, 'result.json'), JSON.stringify(record, null, 2) + '\n', {flag: 'wx', mode: 0o600});
console.log(JSON.stringify({check: checkId, status: record.status, observed: record.observed, reason: record.reason ?? null, output}));
if (record.status !== 'passed') process.exitCode = 1;

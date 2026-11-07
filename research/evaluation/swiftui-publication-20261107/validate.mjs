// Offline post-merge verification. Does not invoke models, native builds or Git writes.
import fs from 'node:fs';
import path from 'node:path';
import {spawnSync} from 'node:child_process';
import {runEnvironment, projectOutputPath} from '../../../evals/runner/workspace-paths.mjs';
const output = projectOutputPath('evals/results/publication-swiftui-20261107');
const env = runEnvironment(output);
const snapshot = path.join(output, 'checkpoint-3cf7cb5');
function run(command, args, options = {}) {
  const r = spawnSync(command, args, {encoding: 'utf8', env, timeout: 120000, maxBuffer: 24 * 1024 * 1024, ...options});
  if (r.error || r.signal || r.status !== 0) throw Error(command + ' failed: ' + (r.stderr ?? '') + (r.stdout ?? ''));
  return r.stdout;
}
if (!fs.existsSync(snapshot)) {
  fs.mkdirSync(snapshot, {mode: 0o700});
  const archive = spawnSync('git', ['archive', '3cf7cb5'], {env, maxBuffer: 64 * 1024 * 1024});
  if (archive.status !== 0 || archive.error) throw Error('Historical source export failed');
  run('tar', ['-x', '-C', snapshot], {input: archive.stdout});
  fs.writeFileSync(path.join(snapshot, '.export-complete'), '3cf7cb5\n', {flag: 'wx'});
}
if (fs.readFileSync(path.join(snapshot, '.export-complete'), 'utf8') !== '3cf7cb5\n') throw Error('Incomplete checkpoint fixture');
const historical = run(process.execPath, ['--test', 'research/evaluation/swiftui-closure-v1/integrity.test.mjs'], {cwd: snapshot});
fs.writeFileSync(path.join(output, 'historical-guard.log'), historical);
function scan(p) {
  return fs.readdirSync(p, {withFileTypes: true}).flatMap(e => e.isDirectory() ? scan(p + '/' + e.name) : /\.test\.mjs$/.test(e.name) ? [p + '/' + e.name] : []);
}
const historicalName = 'all tracked checkpoint inputs outside permitted task notes remain byte-identical';
const current = run(process.execPath, ['--test', '--test-skip-pattern=' + historicalName,
  ...scan('code-examples/tools'), ...scan('research/evaluation'), 'evals/runner/test.mjs', 'evals/runner/workspace-paths-test.mjs']);
fs.writeFileSync(path.join(output, 'reconciled-tests.log'), current);
console.log(historical.slice(-180)); console.log(current.slice(-180));
console.log('One epoch-specific guard runs unchanged in its source checkpoint; the live replacement checks every drift against exact authorized upstream blobs.');

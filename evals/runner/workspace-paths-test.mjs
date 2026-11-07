import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';
import {execFileSync} from 'node:child_process';
import {fileURLToPath} from 'node:url';
import {projectRoot, projectOutputPath, runEnvironment} from './workspace-paths.mjs';

function fixture(t) {
  const parent = path.join(projectRoot, 'evals/results');
  fs.mkdirSync(parent, {recursive: true});
  const folder = fs.mkdtempSync(path.join(parent, 'workspace-paths-test-'));
  t.after(() => fs.rmSync(folder, {recursive: true, force: true}));
  return folder;
}

test('accepts project-relative paths and rejects parent/sibling/outside destinations', t => {
  const root = fixture(t);
  assert.equal(projectOutputPath('runs/new', root), path.join(root, 'runs/new'));
  assert.equal(fs.existsSync(path.join(root, 'runs')), false);
  for (const name of ['..', '../sibling/new', root + '-sibling/new', '/private/tmp/forbidden-output', '.']) {
    assert.throws(() => projectOutputPath(name, root), /inside the project/);
  }
});

test('rejects a symlink escape without writing to its destination', t => {
  const folder = fixture(t);
  const root = path.join(folder, 'project');
  const outside = path.join(folder, 'sibling');
  fs.mkdirSync(root); fs.mkdirSync(outside);
  fs.symlinkSync(outside, path.join(root, 'escape'), 'dir');
  assert.throws(() => projectOutputPath('escape/new', root), /symlink escapes/);
  assert.deepEqual(fs.readdirSync(outside), []);
});

test('scratch and compiler caches resolve inside the run directory', t => {
  const out = path.join(fixture(t), 'run');
  const env = runEnvironment(out);
  for (const key of ['TMPDIR', 'TMP', 'TEMP', 'CLANG_MODULE_CACHE_PATH', 'SWIFT_MODULECACHE_PATH']) {
    const relative = path.relative(out, env[key]);
    assert.ok(relative && !relative.startsWith('..') && !path.isAbsolute(relative));
    assert.ok(fs.statSync(env[key]).isDirectory());
  }
});

test('all three local CLIs reject an external output before inference or compilation', t => {
  const env = runEnvironment(path.join(fixture(t), 'checks'));
  const probes = [
    ['local-os26-comparison.mjs', '--execute', '/private/tmp/forbidden-comparison'],
    ['reviewed-swift-probes.mjs', 'missing-records', 'missing-plan', '/private/tmp/forbidden-probe'],
    ['local-os26-code-gate.mjs', '--records', 'missing-records', '--out', '/private/tmp/forbidden-gate.json']
  ];
  for (const [name, ...args] of probes) {
    const script = fileURLToPath(new URL(name, import.meta.url));
    assert.throws(() => execFileSync(process.execPath, [script, ...args], {env, stdio: 'pipe'}),
      error => /Output must stay inside the project directory/.test(error.stderr?.toString() || ''));
  }
});

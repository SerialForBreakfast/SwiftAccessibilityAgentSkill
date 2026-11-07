import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import {spawnSync} from 'node:child_process';
import {hash} from '../../../code-examples/tools/contracts.mjs';
const reconciliation = JSON.parse(fs.readFileSync('research/evaluation/swiftui-publication-20261107/reconciliation.json'));
const git = args => {
  const r = spawnSync('git', args);
  assert.equal(r.status, 0, 'Git read failed');
  return r.stdout;
};
test('live checkpoint pins allow only exact authorized upstream non-runtime changes', () => {
  const pins = JSON.parse(fs.readFileSync('research/evaluation/swiftui-closure-v1/protected-inputs.json')).files;
  const allowed = new Map(reconciliation.authorizedIncoming.map(p => [p.path, p]));
  const drift = [];
  for (const pin of pins) {
    const current = hash(fs.readFileSync(pin.path));
    if (current === pin.sha256) continue;
    const incoming = allowed.get(pin.path); assert.ok(incoming, pin.path);
    assert.equal(pin.sha256, incoming.baseSha256);
    assert.equal(hash(git(['show', reconciliation.baseCommit + ':' + pin.path])), pin.sha256);
    assert.equal(hash(git(['show', reconciliation.incomingCommit + ':' + pin.path])), incoming.incomingSha256);
    assert.equal(current, incoming.incomingSha256);
    assert.doesNotMatch(pin.path, /^(?:SKILL\.md|VERSION|references\/|skill\/manifests\/|evals\/baselines\/|research\/evaluation\/milestone-package-v2\/)/);
    drift.push(pin.path);
  }
  assert.deepEqual(drift.sort(), [...allowed.keys()].sort());
});
test('both merge parents and both task histories remain preserved', () => {
  for (const commit of [reconciliation.localCheckpoint, reconciliation.incomingCommit]) git(['merge-base', '--is-ancestor', commit, 'HEAD']);
  const base = git(['show', reconciliation.baseCommit + ':Tasks.txt']).toString();
  const current = fs.readFileSync('Tasks.txt', 'utf8');
  for (const commit of [reconciliation.localCheckpoint, reconciliation.incomingCommit]) {
    const text = git(['show', commit + ':Tasks.txt']).toString();
    assert.ok(text.startsWith(base)); assert.ok(current.includes(text.slice(base.length).trim()));
  }
  assert.doesNotMatch(current, /^(?:<<<<<<< |=======$|>>>>>>> )/m);
});
test('released baseline and sealed candidate/controller inputs retain their pins', () => {
  const pins = JSON.parse(fs.readFileSync('research/evaluation/failure-driven/candidates/0.3.0-dev.6/parent-pins.json')).files;
  for (const pin of pins) assert.equal(hash(fs.readFileSync(pin.path)), pin.sha256, pin.path);
  const previous = JSON.parse(fs.readFileSync('research/evaluation/swiftui-review-v1/prior-batch-pins.json')).files;
  for (const pin of previous) assert.equal(hash(fs.readFileSync(pin.path)), pin.sha256, pin.path);
});

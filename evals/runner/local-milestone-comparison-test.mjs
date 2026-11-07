import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';
import {spawnSync} from 'node:child_process';
import {plan, hash, continuation, unattemptedContinuation, prioritizePending, hasFullRequestBudget} from './local-milestone-comparison.mjs';
import {projectRoot} from './workspace-paths.mjs';

test('bounded matrix retains exact sealed payloads and matched reference contexts', () => {
  const p = plan();
  assert.equal(p.jobs.length, 36);
  assert.equal(new Set(p.jobs.map(j => j.id)).size, 36);
  for (const model of p.models) for (const caseId of p.selection) {
    const jobs = p.jobs.filter(j => j.model === model && j.caseId === caseId);
    const get = arm => jobs.find(j => j.condition === arm);
    assert.equal(get('R').messages[1].content, get('D5').messages[1].content);
    assert.equal(JSON.parse(get('C0').messages[1].content).request, JSON.parse(get('D5').messages[1].content).request);
    for (const [arm, file] of [['C0', 'generic-C0'], ['D5', 'candidate-controlled']]) {
      const sealed = JSON.parse(fs.readFileSync(`research/evaluation/milestone-package-v2/payloads/${caseId}/${file}.json`));
      assert.deepEqual(get(arm).messages, sealed.messages);
      assert.equal(get(arm).payloadHash, hash(JSON.stringify(sealed.messages)));
    }
    for (const j of jobs) {
      assert.equal(j.messages.length, 2);
      assert.ok(j.inputBytes < p.limits.inputBytes);
    }
  }
});

test('outside-project output rejected before model contact', () => {
  const r = spawnSync('node', ['evals/runner/local-milestone-comparison.mjs', '--execute', '../forbidden-local-test'], {encoding: 'utf8'});
  assert.notEqual(r.status, 0);
  assert.match(r.stderr, /inside the project directory/);
});

test('continuation cannot replay a completed cell or hide an active/changed attempt', () => {
  const dir = fs.mkdtempSync(path.join(projectRoot, 'evals/results/local-milestone-test-'));
  try {
    const p = plan(), job = p.jobs[0];
    const old = {...p, startedAt: '2026-11-07T16:11:06.021Z', identities: Object.fromEntries(p.models.map(m => [m, {tag: {digest: 'synthetic'}}]))};
    const status = {state: 'stopped', active: null, error: 'Input changed: evals/runner/local-milestone-comparison.mjs', completed: [job.id], unattempted: p.jobs.slice(1).map(j => j.id)};
    const save = (name, value) => fs.writeFileSync(path.join(dir, name), JSON.stringify(value));
    save('manifest.json', old); save('status.json', status);
    fs.writeFileSync(path.join(dir, 'records.jsonl'), JSON.stringify({id: job.id, payloadHash: job.payloadHash, output: 'synthetic', outputHash: hash('synthetic')}) + '\n');
    const next = continuation(dir, p);
    assert.equal(next.jobs.length, 35);
    assert.ok(!next.jobs.some(j => j.id === job.id));
    assert.equal(next.limits.campaignSeconds, 5400);
    assert.equal(next.campaignStartedAt, old.startedAt);
    save('status.json', {...status, active: p.jobs[1].id});
    assert.throws(() => continuation(dir, p), /unknown active attempt/);
    save('status.json', status);
    const edited = structuredClone(old);
    edited.jobs[1].messages[1].content += 'changed';
    save('manifest.json', edited);
    assert.throws(() => continuation(dir, p), /Planned cell changed/);
  } finally { fs.rmSync(dir, {recursive: true, force: true}); }
});

test('timeout recovery skips the failed call and requires confirmed model unloading', () => {
  const dir = fs.mkdtempSync(path.join(projectRoot, 'evals/results/local-milestone-test-'));
  try {
    const p = plan(), jobs = p.jobs.slice(0, 2);
    const old = {...p, startedAt: '2026-11-07T16:11:06.021Z', identities: Object.fromEntries(p.models.map(m => [m, {tag: {digest: 'synthetic'}}]))};
    const save = (name, value) => fs.writeFileSync(path.join(dir, name), JSON.stringify(value));
    save('manifest.json', old);
    for (const pin of p.pins) {
      const dest = path.join(dir, 'frozen-inputs', pin.path);
      fs.mkdirSync(path.dirname(dest), {recursive: true});
      fs.copyFileSync(path.join(projectRoot, pin.path), dest);
    }
    const events = jobs.map(j => {
      const request = {model: j.model, messages: j.messages, options: p.settings};
      save(j.id + '-request.json', request);
      return {type: 'request', id: j.id, requestHash: hash(JSON.stringify(request))};
    });
    events.push({type: 'stopped', at: '2026-11-07T16:20:00Z'}, {type: 'unloaded', at: '2026-11-07T16:20:01Z', model: jobs[1].model});
    const writeEvents = () => fs.writeFileSync(path.join(dir, 'events.jsonl'), events.map(e => JSON.stringify(e)).join('\n') + '\n');
    writeEvents();
    save('status.json', {state: 'stopped', active: jobs[1].id, error: 'The operation was aborted due to timeout', completed: [jobs[0].id], unattempted: p.jobs.slice(2).map(j => j.id)});
    fs.writeFileSync(path.join(dir, 'records.jsonl'), JSON.stringify({id: jobs[0].id, output: 'synthetic', outputHash: hash('synthetic')}) + '\n');
    const next = unattemptedContinuation([dir], p);
    assert.equal(next.jobs.length, 34);
    assert.deepEqual(next.previous.failed, [jobs[1].id]);
    assert.ok(next.jobs.every(j => !jobs.some(old => old.id === j.id)));
    events.pop(); writeEvents();
    assert.throws(() => unattemptedContinuation([dir], p), /confirmed timeout\/unload/);
  } finally { fs.rmSync(dir, {recursive: true, force: true}); }
});

test('coverage priority changes only case scheduling, preserving calls and paired arm order', () => {
  const p = plan(), before = JSON.stringify(p);
  const next = prioritizePending(p, ['tvos-swiftui-actions']);
  assert.equal(JSON.stringify(p), before);
  assert.equal(next.jobs[0].caseId, 'tvos-swiftui-actions');
  assert.deepEqual(next.jobs.map(j => j.id).sort(), p.jobs.map(j => j.id).sort());
  for (const model of p.models) for (const id of p.selection) {
    const choose = m => m.jobs.filter(j => j.model === model && j.caseId === id);
    assert.deepEqual(choose(next), choose(p));
  }
  assert.deepEqual(next.settings, p.settings);
  assert.deepEqual(next.limits, p.limits);
  const paired = prioritizePending(p, ['tvos-swiftui-actions'], ['D5', 'R', 'C0']);
  for (const model of p.models) assert.deepEqual(paired.jobs.filter(j => j.model === model && j.caseId === 'tvos-swiftui-actions').map(j => j.condition), ['D5', 'R', 'C0']);
  assert.deepEqual(paired.jobs.map(j => j.id).sort(), p.jobs.map(j => j.id).sort());
  assert.throws(() => prioritizePending(p, ['tvos-swiftui-actions'], ['D5', 'D5', 'C0']), /Invalid priority arms/);
});

test('a campaign tail cannot dispatch a request without its full reserved window', () => {
  assert.equal(hasFullRequestBudget(5400000, 5397170, 240), false);
  assert.equal(hasFullRequestBudget(5400000, 5160001, 240), false);
  assert.equal(hasFullRequestBudget(5400000, 5160000, 240), true);
  assert.equal(hasFullRequestBudget(5400000, 5400001, 240), false);
});

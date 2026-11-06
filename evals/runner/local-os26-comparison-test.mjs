import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import {execFileSync} from 'node:child_process';
import {fileURLToPath} from 'node:url';

// The default CLI path constructs an offline plan and cannot dispatch inference.
const plan = JSON.parse(execFileSync(process.execPath, [fileURLToPath(new URL('./local-os26-comparison.mjs', import.meta.url))], {encoding: 'utf8'}));
const prompts = JSON.parse(fs.readFileSync(new URL('../os26/prompts.json', import.meta.url)));

test('offline plan bounds exactly 36 unique local generations with no retries', () => {
  assert.equal(plan.jobs.length, 36);
  assert.equal(new Set(plan.jobs.map(j => j.id)).size, 36);
  assert.equal(plan.limits.retries, 0);
  assert.equal(plan.limits.concurrency, 1);
  assert.equal(plan.settings.num_predict, 1024);
  assert.ok(plan.jobs.every(j => j.inputBytes <= plan.limits.inputBytes));
});

test('each paired cell holds exact user task and reference hashes constant', () => {
  for (const model of plan.models) for (const p of prompts.cases) {
    const rs = plan.jobs.filter(j => j.model === model && j.prompt.id === p.id);
    assert.equal(rs.length, 2);
    assert.deepEqual(rs.map(r => r.condition).sort(), ['BR', 'F']);
    assert.equal(rs[0].prompt.prompt, p.prompt);
    assert.equal(rs[1].prompt.prompt, p.prompt);
    assert.deepEqual(rs[0].references, rs[1].references);
    assert.notEqual(rs[0].payloadHash, rs[1].payloadHash);
  }
});

test('each model alternates which entrypoint is dispatched first across cases', () => {
  for (const model of plan.models) {
    const jobs = plan.jobs.filter(j => j.model === model);
    const first = jobs.filter((_, i) => i % 2 === 0);
    assert.equal(first.filter(j => j.condition === 'F').length, 3);
    assert.equal(first.filter(j => j.condition === 'BR').length, 3);
  }
});

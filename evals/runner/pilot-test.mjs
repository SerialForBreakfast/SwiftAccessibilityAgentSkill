import test from 'node:test';
import assert from 'node:assert/strict';
import { planPilot } from './pilot.mjs';
import { coverage } from './campaign.mjs';

test('pilot is finite, development-only and covers all four complexity levels', () => {
  const p = planPilot('bigdog');
  assert.equal(p.jobs.length, 64);
  assert.equal(p.limits.minimumGenerationRequests, 136);
  assert.equal(p.limits.maximumGenerationRequests, 200);
  assert.deepEqual([...new Set(p.jobs.map(j => j.complexity))].sort(), ['L1','L2','L3','L4']);
  assert.ok(p.jobs.every(j => j.split === 'development' && j.repeat === 0));
  assert.equal(p.jobs.filter(j => j.family === 'D38').length, 16);
  assert.equal(new Set(p.jobs.map(j => j.id)).size, 64);
  assert.equal(coverage(p, []).totalMissing, 64);
});

test('worker plans preserve identical comparisons but separate dispatch identities', () => {
  const a = planPilot('bigdog'), b = planPilot('maxmini');
  assert.notEqual(a.planHash, b.planHash);
  assert.deepEqual(a.jobs, b.jobs);
  assert.equal(a.planHash, planPilot('bigdog').planHash);
  assert.throws(() => planPilot('unknown'));
});

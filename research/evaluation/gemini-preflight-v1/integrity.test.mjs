import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';
import {build, exportSubjects} from './build.mjs';
import {validateTransport, quotaDecision} from './transport-contract.mjs';
import {hash} from '../../../code-examples/tools/contracts.mjs';
const base = 'research/evaluation/gemini-preflight-v1/';
const b = build();
const fixture = () => ({schema: 1, provenance: 'observed-source-inspection', requestedModel: 'gemini-4-argon-high',
  client: {version: '1.5.3', executableSha256: 'a'.repeat(64), adapterSha256: 'b'.repeat(64)},
  transport: {mode: 'isolated-text-two-message', systemRolePreserved: true, clientAddedMessages: 0,
    freshContextPerSubject: true, controllerWorkspaceAccessible: false, globalSkillsEnabled: false,
    globalRulesEnabled: false, tools: [], filesystemAccess: false, networkToolsEnabled: false,
    inputFraming: 'single-messages-envelope'},
  sourceEvidence: [{path: 'synthetic-fixture-not-provider-proof', sha256: 'c'.repeat(64)}],
  isolationReview: {accepted: true, reviewer: 'synthetic-reviewer', evidenceSha256: 'd'.repeat(64)},
  offlineSerialization: b.jobs.map(j => ({cell: j.cell, kind: 'offline-serialization-not-provider-response',
    payloadSha256: j.payloadSha256, messages: structuredClone(j.messages)}))});

test('freeze all 48 original payloads with 78 criteria, three overrides and five provenance fixes', () => {
  assert.equal(b.jobs.length, 48); assert.equal(b.controller.rows.length, 24);
  assert.equal(b.controller.rows.reduce((n, r) => n + r.criteria.length, 0), 78);
  assert.equal(b.controller.appliedActionOverrides.length, 3); assert.equal(b.controller.reboundCriteria.length, 24);
  assert.equal(b.controller.correctedProvenance.length, 5); assert.equal(b.identity.relatedFamilies, 12);
  for (const c of b.controller.rows.flatMap(r => r.criteria)) {
    assert.deepEqual(c.appliesEquallyTo, ['generic-C0', 'candidate-controlled']);
    if (b.controller.correctedProvenance.includes(c.id)) {
      const note = c.sourceBinding.application_acceptance_sources.find(s => s.path.endsWith('/references/tasks/testing.md'));
      assert.equal(note.subjectCitationRequired, false); assert.match(note.scope, /Controller-side/);
    }
  }
});
test('derived controller identity is pinned and does not include dev.6 or live approval', () => {
  assert.equal(hash(fs.readFileSync(base + 'controller.json')), b.identity.controllerSha256);
  assert.deepEqual(JSON.parse(fs.readFileSync(base + 'comparison-identity.json')), b.identity);
  assert.equal(b.identity.dev6Included, false); assert.equal(b.identity.modelCallsAuthorized, 0);
  assert.equal(b.controller.executedCalibration, false);
  for (const j of b.jobs) assert.equal(hash(fs.readFileSync(j.payloadPath)), j.payloadSha256);
});
test('export contains exact messages only; controller metadata stays out of subject files', () => {
  fs.mkdirSync('evals/results', {recursive: true});
  const dir = fs.mkdtempSync('evals/results/gemini-export-fixture-');
  const out = path.join(dir, 'new');
  try {
    assert.equal(exportSubjects(out).providerCalls, 0);
    assert.equal(fs.readdirSync(path.join(out, 'subjects')).length, 48);
    for (const j of b.jobs) {
      const raw = fs.readFileSync(path.join(out, 'subjects', j.opaqueId + '.json'));
      assert.equal(hash(raw), j.payloadSha256); assert.deepEqual(Object.keys(JSON.parse(raw)), ['messages']);
    }
    assert.throws(() => exportSubjects(out));
    assert.throws(() => exportSubjects('../outside-project-fixture'));
  } finally { fs.rmSync(dir, {recursive: true, force: true}); }
});
test('schema-consistent synthetic data never establishes runtime qualification or run authority', () => {
  const r = validateTransport(fixture(), b.jobs);
  assert.equal(r.evidenceConsistent, true); assert.equal(r.runtimeQualified, false);
  assert.equal(r.runAuthorized, false); assert.equal(r.modelCalls, 0);
  const synthetic = fixture(); synthetic.provenance = 'synthetic-fixture';
  assert.ok(validateTransport(synthetic, b.jobs).errors.includes('not-synthetic-evidence'));
});
const mutations = {
  'agent mode': r => { r.transport.mode = 'agent-cli'; },
  'extra system instructions': r => { r.transport.clientAddedMessages = 1; },
  'lost system role': r => { r.transport.systemRolePreserved = false; },
  'global skills': r => { r.transport.globalSkillsEnabled = true; },
  'ancestor/global rules': r => { r.transport.globalRulesEnabled = true; },
  'filesystem exposure': r => { r.transport.filesystemAccess = true; },
  'controller exposure': r => { r.transport.controllerWorkspaceAccessible = true; },
  'tool registry': r => { r.transport.tools = ['Read']; },
  'network tool': r => { r.transport.networkToolsEnabled = true; },
  'session reuse': r => { r.transport.freshContextPerSubject = false; },
  'role lines as turns': r => { r.transport.inputFraming = 'one-turn-per-role-line'; },
  'old CLI': r => { r.client.version = '1.5.2'; },
  'model substitution': r => { r.requestedModel = 'gemini-3.8-flash-high'; },
  'lost payload': r => { r.offlineSerialization.pop(); },
  'duplicate cell': r => { r.offlineSerialization[1] = r.offlineSerialization[0]; },
  'extra role': r => { r.offlineSerialization[0].messages.push({role: 'user', content: 'extra'}); },
  'changed content': r => { r.offlineSerialization[0].messages[0].content += 'changed'; },
  'hidden request field': r => { r.offlineSerialization[0].tools = []; },
  'missing source inspection': r => { r.sourceEvidence = []; },
  'unreviewed isolation': r => { r.isolationReview.accepted = false; }
};
for (const [name, mutate] of Object.entries(mutations)) test('reject transport drift: ' + name, () => {
  const r = fixture(); mutate(r); assert.equal(validateTransport(r, b.jobs).evidenceConsistent, false);
});
test('malformed reports and matrices fail closed without exceptions', () => {
  for (const report of [null, {}, {schema: 1}, {sourceEvidence: [null]}]) assert.equal(validateTransport(report, b.jobs).evidenceConsistent, false);
  for (const jobs of [null, [], [null]]) assert.equal(validateTransport(fixture(), jobs).evidenceConsistent, false);
});
const quota = () => ({start: {fiveHour: {usedPercent: 10, resetIdentity: 'window-a'}},
  current: {fiveHour: {usedPercent: 11, resetIdentity: 'window-a'}}, allowance: {fiveHour: 5},
  observedAtMs: 1000, nowMs: 2000, deadlineMs: 4000});
test('quota decision is observational, not a hard provider cap or authorization', () => {
  assert.equal(quotaDecision(quota()).decision, 'within-observed-threshold');
});
for (const [name, mutate] of Object.entries({
  threshold: q => { q.current.fiveHour.usedPercent = 15; },
  missing: q => { q.current = null; }, reset: q => { q.current.fiveHour.resetIdentity = 'window-b'; },
  rollback: q => { q.current.fiveHour.usedPercent = 9; },
  stale: q => { q.nowMs = 62000; q.deadlineMs = 100000; },
  future: q => { q.observedAtMs = 3000; }, deadline: q => { q.nowMs = 4000; },
  malformed: q => { q.allowance.fiveHour = NaN; }
})) test('stop on quota uncertainty: ' + name, () => { const q = quota(); mutate(q); assert.equal(quotaDecision(q).decision, 'stop'); });
test('local CLI observation is metadata-only and records the role-line framing risk', () => {
  const o = JSON.parse(fs.readFileSync(base + 'local-cli-observation.json'));
  assert.equal(o.inferenceCalls, 0); assert.equal(hash(fs.readFileSync(o.help.path)), o.help.sha256);
  assert.match(fs.readFileSync(o.help.path, 'utf8'), /runs a turn for each/);
});

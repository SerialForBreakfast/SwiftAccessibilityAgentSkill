// Offline evidence validation only. No network, CLI inference or execution mode.
import {hash} from '../../../code-examples/tools/contracts.mjs';
const digest = x => hash(JSON.stringify(x));
const sha = x => typeof x === 'string' && /^[a-f0-9]{64}$/.test(x);
const meaningful = x => typeof x === 'string' && x.trim().length > 0 &&
  !/^(?:unknown|unavailable|unverified|latest|auto|default)$/i.test(x.trim());

export function validateTransport(report, jobs) {
  const errors = [], add = (ok, id) => { if (!ok) errors.push(id); };
  if (!Array.isArray(jobs) || jobs.length !== 48 ||
      !jobs.every(j => j && meaningful(j.cell) && sha(j.payloadSha256) && sha(j.messagesSha256)) ||
      new Set(jobs.map(j => j.cell)).size !== 48) {
    return {schema: 1, evidenceConsistent: false, errors: ['invalid-sealed-job-matrix'],
      runtimeQualified: false, independentAcceptanceRequired: true, runAuthorized: false, modelCalls: 0};
  }
  add(report?.schema === 1, 'schema');
  add(report?.client?.version === '1.5.3', 'client-version');
  add(sha(report?.client?.executableSha256) && sha(report?.client?.adapterSha256), 'client-and-adapter-pins');
  add(meaningful(report?.requestedModel) && report.requestedModel === 'gemini-4-argon-high', 'named-proposed-model');
  const t = report?.transport;
  add(t?.mode === 'isolated-text-two-message', 'not-an-agent-conversation');
  add(t?.systemRolePreserved === true && t?.clientAddedMessages === 0, 'system-role-and-hidden-client-injection');
  add(t?.freshContextPerSubject === true && t?.controllerWorkspaceAccessible === false, 'subject-isolation');
  add(t?.globalSkillsEnabled === false && t?.globalRulesEnabled === false, 'global-context');
  add(Array.isArray(t?.tools) && t.tools.length === 0 && t?.filesystemAccess === false &&
    t?.networkToolsEnabled === false, 'tools-and-filesystem');
  add(t?.inputFraming !== 'one-turn-per-role-line' && t?.inputFraming === 'single-messages-envelope', 'role-lines-are-not-turns');
  add(Array.isArray(report?.sourceEvidence) && report.sourceEvidence.length > 0 &&
    report.sourceEvidence.every(p => meaningful(p?.path) && sha(p?.sha256)), 'inspection-evidence');
  add(report?.isolationReview?.accepted === true && meaningful(report.isolationReview.reviewer) &&
    sha(report.isolationReview.evidenceSha256), 'independent-isolation-review');
  add(report?.provenance === 'observed-source-inspection', 'not-synthetic-evidence');
  const captures = report?.offlineSerialization;
  add(Array.isArray(captures) && captures.length === jobs.length, 'complete-offline-serialization');
  const used = new Set();
  if (Array.isArray(captures)) for (const capture of captures) {
    const key = capture?.cell;
    const job = jobs.find(j => j.cell === key);
    add(!!job && !used.has(key), 'unknown-or-duplicate-cell'); used.add(key);
    if (!job) continue;
    add(capture.kind === 'offline-serialization-not-provider-response', 'serialization-provenance');
    add(capture.payloadSha256 === job.payloadSha256, 'sealed-payload-drift');
    add(Array.isArray(capture.messages) && capture.messages.length === 2 &&
      capture.messages[0]?.role === 'system' && capture.messages[1]?.role === 'user', 'exact-two-message-roles');
    add(digest(capture.messages) === job.messagesSha256, 'message-content-drift');
    add(Object.keys(capture).every(k => ['cell', 'kind', 'payloadSha256', 'messages'].includes(k)), 'unexpected-capture-fields');
  }
  return {schema: 1, evidenceConsistent: errors.length === 0, errors: [...new Set(errors)],
    runtimeQualified: false, independentAcceptanceRequired: true,
    runAuthorized: false, modelCalls: 0,
    scope: 'Schema/byte consistency cannot prove runtime isolation or authorize subscription use.'};
}

export function quotaDecision({start, current, allowance, observedAtMs, nowMs, deadlineMs}) {
  const stop = reason => ({decision: 'stop', reason});
  if (![nowMs, observedAtMs, deadlineMs].every(Number.isFinite) || nowMs >= deadlineMs) return stop('deadline-or-clock');
  if (observedAtMs > nowMs || nowMs - observedAtMs > 60000) return stop('stale-quota');
  if (!start || !current || !allowance || !Object.keys(allowance).length) return stop('missing-quota');
  for (const key of Object.keys(allowance)) {
    const a = start[key], b = current[key], limit = allowance[key];
    if (!a || !b || !Number.isFinite(limit) || limit <= 0 || limit > 100 ||
      ![a.usedPercent, b.usedPercent].every(x => Number.isFinite(x) && x >= 0 && x <= 100)) return stop('invalid-quota');
    if (!meaningful(a.resetIdentity) || a.resetIdentity !== b.resetIdentity) return stop('quota-reset');
    if (b.usedPercent < a.usedPercent) return stop('nonmonotonic-quota');
    if (b.usedPercent - a.usedPercent >= limit) return stop('observed-allowance-reached');
  }
  return {decision: 'within-observed-threshold', reason: 'Not a provider-enforced cap; one subject may overshoot and other account usage counts.'};
}

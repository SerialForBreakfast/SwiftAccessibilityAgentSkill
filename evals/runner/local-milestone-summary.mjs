// Reconcile retained evidence, not an automatic semantic judge.
import fs from 'node:fs';
import path from 'node:path';
import {createHash} from 'node:crypto';
import {projectOutputPath} from './workspace-paths.mjs';

const hash = x => createHash('sha256').update(x).digest('hex');
const json = p => JSON.parse(fs.readFileSync(p));
const lines = p => fs.existsSync(p) ? fs.readFileSync(p, 'utf8').split('\n').filter(Boolean).map(JSON.parse) : [];
const median = a => { a = [...a].sort((a, b) => a - b); return a.length ? (a[Math.floor((a.length - 1) / 2)] + a[Math.floor(a.length / 2)]) / 2 : null; };
const args = process.argv.slice(2), output = args.pop();
if (!output || !args.length) throw Error('Usage: local-milestone-summary.mjs PHASE... PROJECT_REPORT_DIRECTORY');
const out = projectOutputPath(output), phases = args.map(p => projectOutputPath(p));
const manifests = phases.map(p => json(path.join(p, 'manifest.json')));
const expected = manifests[0].jobs;
const records = [], requests = [], reviews = [], probes = [], statuses = [], failures = [], corrections = [];
for (let i = 0; i < phases.length; i++) {
  const dir = phases[i], m = manifests[i];
  for (const p of m.pins) if (hash(fs.readFileSync(path.join(dir, 'frozen-inputs', p.path))) !== p.sha256) throw Error('Frozen input mismatch');
  if (JSON.stringify(m.settings) !== JSON.stringify(manifests[0].settings)) throw Error('Settings mismatch');
  for (const model of m.models) if (m.identities[model].tag.digest !== manifests[0].identities[model].tag.digest) throw Error('Model identity mismatch');
  const status = path.join(dir, 'status.json');
  const state = fs.existsSync(status) ? json(status) : {state: 'running'};
  statuses.push(state);
  const events = lines(path.join(dir, 'events.jsonl'));
  requests.push(...events.filter(e => e.type === 'request'));
  failures.push(...lines(path.join(dir, 'failures.jsonl')));
  if (state.active && state.state === 'stopped') {
    const job = expected.find(j => j.id === state.active);
    const start = events.find(e => e.type === 'request' && e.id === state.active);
    const stop = events.find(e => e.type === 'stopped');
    const atCampaignDeadline = Date.parse(stop.at) >= Date.parse(manifests[0].startedAt) + 5400000 - 100;
    failures.push({id: state.active, model: job.model, condition: job.condition, caseId: job.caseId,
      error: state.error, inputTokens: null, outputTokens: null, output: null,
      elapsedSeconds: (Date.parse(stop.at) - Date.parse(start.at)) / 1000,
      failureKind: atCampaignDeadline ? 'campaign_time_limit' : 'request_failure',
      reason: 'Retained stopped attempt; original output/usage unavailable; not retried'});
  }
  for (const r of lines(path.join(dir, 'records.jsonl'))) {
    const job = expected.find(j => j.id === r.id);
    const request = json(path.join(dir, r.id + '-request.json'));
    const response = json(path.join(dir, r.id + '-response.json'));
    if (!job || hash(r.output) !== r.outputHash || hash(JSON.stringify(request.messages)) !== job.payloadHash || r.payloadHash !== job.payloadHash) throw Error('Request/answer hash mismatch');
    if (response.message.content !== r.output || response.model !== r.model || request.model !== r.model || r.digest !== m.identities[r.model].tag.digest || response.done_reason !== r.finish_reason || response.prompt_eval_count !== r.inputTokens || response.eval_count !== r.outputTokens || JSON.stringify(request.options) !== JSON.stringify(m.settings) || request.stream !== false || request.think !== false || request.tools || request.messages.length !== 2) throw Error('Provider receipt mismatch');
    const event = requests.find(e => e.id === r.id);
    if (!event || event.requestHash !== hash(JSON.stringify(request))) throw Error('Request event mismatch');
    records.push(r);
  }
  const controller = path.join(dir, 'controller');
  if (fs.existsSync(controller)) for (const name of fs.readdirSync(controller).filter(n => /^review-\d+\.json$/.test(n))) reviews.push(...json(path.join(controller, name)).records);
  if (fs.existsSync(path.join(controller, 'review-corrections.json'))) corrections.push(...json(path.join(controller, 'review-corrections.json')).corrections);
  for (const name of fs.readdirSync(dir).filter(n => /^probes-\d+$/.test(n))) {
    const p = path.join(dir, name, 'results.json');
    if (fs.existsSync(p)) probes.push(...json(p).map(({recordId, status, sourceHash, reviewNote, blocks, sourceRange, stderr}) => {
      const text = stderr || '';
      const macro = /macro.*could not be found|malformed response/.test(text);
      const diagnostic = /failed to produce diagnostic/.test(text);
      const ordinary = text.split('\n').some(l => /:\d+:\d+: error:/.test(l) && !/macro|plugin|failed to produce diagnostic/i.test(l));
      const assessment = macro ? (ordinary ? 'type_errors_with_macro_infrastructure_failure' : 'macro_infrastructure_failure') :
        diagnostic ? (ordinary ? 'type_errors_with_compiler_diagnostic_failure' : 'compiler_diagnostic_failure') : status;
      return {recordId, status, assessment, compilerFlags: {macro, diagnostic, ordinary}, sourceHash, reviewNote, blocks, sourceRange};
    }));
  }
}
if (new Set(records.map(r => r.id)).size !== records.length || new Set(requests.map(r => r.id)).size !== requests.length || requests.length > 36) throw Error('Duplicate call or quota violation');
if (new Set(failures.map(r => r.id)).size !== failures.length || failures.some(f => records.some(r => r.id === f.id))) throw Error('Failure receipt mismatch');
for (const review of reviews) if (!records.some(r => r.id === review.id && r.outputHash === review.answerHash)) throw Error('Review/answer mismatch');
if (new Set(reviews.map(r => r.id)).size !== reviews.length) throw Error('Duplicate review');
for (const c of corrections) {
  const review = reviews.find(r => r.id === c.id), criterion = review?.criteria.find(r => r.index === c.criterion);
  if (!criterion) throw Error('Missing correction target');
  (review.calibrationCorrections ||= []).push({index: c.criterion, previous: {...criterion}, replacement: c.replacement});
  Object.assign(criterion, c.replacement);
}
const groups = [];
for (const model of manifests[0].models) for (const condition of ['C0', 'R', 'D5']) {
  const rs = records.filter(r => r.model === model && r.condition === condition);
  const failedRows = failures.filter(r => r.model === model && r.condition === condition);
  groups.push({model, condition, attempts: rs.length + failedRows.length, answers: rs.length, failures: failedRows.map(f => f.id), stop: rs.filter(r => r.finish_reason === 'stop').length,
    length: rs.filter(r => r.finish_reason === 'length').length,
    inputTokens: rs.reduce((s, r) => s + r.inputTokens, 0), outputTokens: rs.reduce((s, r) => s + r.outputTokens, 0),
    seconds: rs.reduce((s, r) => s + r.elapsedSeconds, 0),
    reviews: rs.map(r => ({id: r.id, contract: reviews.find(v => v.id === r.id)?.contract || 'pending',
      probes: probes.filter(p => p.recordId === r.id).map(p => p.assessment)}))});
}
const pairs = [];
for (const model of manifests[0].models) for (const caseId of manifests[0].selection) {
  const get = condition => records.find(r => r.model === model && r.caseId === caseId && r.condition === condition);
  const r = get('R'), d = get('D5');
  if (r && d) pairs.push({model, caseId, inputReductionPct: 100 * (r.inputTokens - d.inputTokens) / r.inputTokens,
    totalReductionPct: 100 * (r.inputTokens + r.outputTokens - d.inputTokens - d.outputTokens) / (r.inputTokens + r.outputTokens),
    releaseFinish: r.finish_reason, candidateFinish: d.finish_reason});
}
const outputTokens = records.reduce((s, r) => s + r.outputTokens, 0);
if (outputTokens > 55296) throw Error('Output quota exceeded');
const closed = statuses.at(-1).state !== 'running';
const complete = closed && requests.length === 36 && records.length + failures.length === 36;
const summary = {schema: 1, status: complete ? (failures.length ? 'executed_with_failures' : 'executed') : (closed ? 'bounded_partial' : 'in_progress'),
  qualification: 'Known development cases; one unblinded provisional reviewer; not independently accepted',
  reviewBasis: {packageReview: 'research/evaluation/independent-v2-review-20261107/REVIEW.md',
    status: 'Full-package eligibility held; selected action cases have an oracle ambiguity',
    boundary: 'Local observations accept stable current-owner dispatch and rely on independent API/integration/preservation evidence; this report does not close the hold'},
  integrity: {checks: 'Frozen pins, expanded requests, provider receipts, outputs, model identities, settings, call uniqueness and review hashes',
    planned: 36, dispatched: requests.length, answers: records.length, failures: failures.length, reviews: reviews.length,
    missingAnswers: expected.filter(j => !records.some(r => r.id === j.id)).map(j => j.id),
    unattempted: expected.filter(j => !requests.some(r => r.id === j.id)).map(j => j.id)},
  phases: phases.map((p, i) => ({directory: path.relative(process.cwd(), p), state: statuses[i].state})),
  sourceCommit: manifests[0].sourceCommit, settings: manifests[0].settings,
  limits: {calls: 36, outputTokens: 55296, aggregateSeconds: 5400},
  usage: {inputTokens: records.reduce((s, r) => s + r.inputTokens, 0), outputTokens,
    basis: 'Reported successful-response usage only; failures have unavailable usage, not zero',
    unreportedUsageAttempts: failures.length,
    responseSeconds: records.reduce((s, r) => s + r.elapsedSeconds, 0), failureSeconds: failures.reduce((s, r) => s + r.elapsedSeconds, 0)}, groups, pairs,
  tokenComparisons: manifests[0].models.map(model => ({model,
    pairedCases: pairs.filter(p => p.model === model).length,
    medianInputReductionPct: median(pairs.filter(p => p.model === model).map(p => p.inputReductionPct)),
    medianTotalReductionPct: median(pairs.filter(p => p.model === model).map(p => p.totalReductionPct))})),
  failures, reviews, probes};
fs.mkdirSync(out, {recursive: true});
fs.writeFileSync(path.join(out, 'summary.json'), JSON.stringify(summary, null, 2) + '\n');
console.log(JSON.stringify({status: summary.status, ...summary.integrity, usage: summary.usage}));

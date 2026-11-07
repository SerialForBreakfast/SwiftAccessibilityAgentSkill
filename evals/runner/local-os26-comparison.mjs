// Bounded, local-only comparison. No downloads, tools, retries or subscription calls.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {fileURLToPath} from 'node:url';
import {execFileSync} from 'node:child_process';
import {projectOutputPath} from './workspace-paths.mjs';

const repo = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '../..');
const hash = x => crypto.createHash('sha256').update(x).digest('hex');
const read = name => fs.readFileSync(path.join(repo, name), 'utf8');
const models = ['gemma4:12b', 'qwen2.5-coder:14b', 'qwen3.5:latest'];
const references = {
  'GP26-01': ['uikit/u-005-grouping-containment.md', 'uikit/u-007-accessibility-custom-actions.md'],
  'GP26-02': ['uikit/u-001-labels-meaningful-names.md', 'uikit/u-003-values-stateful-controls.md'],
  'GP26-03': ['uikit/u-010-dynamic-type-layout-resilience.md'],
  'GP26-04': ['swiftui/g-007-accessibility-actions.md', 'swiftui/g-008-custom-controls-representation.md'],
  'GP26-05': ['tvos/t-004-grouping-containment-shelves-grids.md', 'tvos/t-005-custom-actions-remote-first.md'],
  'GP26-06': ['swiftui/g-003-values-stateful-controls.md']
};
const promptFile = 'evals/os26/prompts.json';
const candidateFile = 'research/evaluation/failure-driven/compact-candidate-b/ENTRYPOINT.md';
const released = read('SKILL.md');
const metadata = released.match(/^---\n[\s\S]*?\n---/)?.[0];
const candidate = read(candidateFile).match(/<!-- SUBJECT START -->\n([\s\S]*?)<!-- SUBJECT END -->/)?.[1];
if (!metadata || !candidate) throw Error('Missing exact entrypoint boundaries');
const instructions = {F: released, BR: `${metadata}\n\n${candidate}`};
const catalog = JSON.parse(read(promptFile));
const pins = [promptFile, 'SKILL.md', candidateFile];
const cases = catalog.cases.map(c => {
  const refs = references[c.id].map(name => {
    const [domain, file] = name.split('/');
    const p = `references/${domain}/guidelines/${file}`;
    pins.push(p);
    return {path: p, text: read(p), sha256: hash(read(p))};
  });
  return {...c, refs};
});
if (cases.length !== 6) throw Error('Expected six frozen development cases');
const jobs = models.flatMap((model, mi) => cases.flatMap((c, ci) => {
  const order = (mi + ci) % 2 ? ['BR', 'F'] : ['F', 'BR'];
  return order.map(condition => {
    const system = `${instructions[condition]}\n\nRepository references below are supplied by this harness. No file lookup or other tools are available. Cite only evidence supplied here; distinguish proposed checks from checks actually run. Answer the user directly and keep the answer concise.\n\n${c.refs.map(r => `===== ${r.path} =====\n${r.text}`).join('\n\n')}`;
    const messages = [{role: 'system', content: system}, {role: 'user', content: c.prompt}];
    if (Buffer.byteLength(JSON.stringify(messages)) > 50000) throw Error('Input byte bound exceeded');
    return {id: `${model.replaceAll(/[^a-z0-9]+/gi, '_')}-${c.id}-${condition}`, model, condition,
      prompt: {id: c.id, family: c.family, platform: c.platform, framework: c.framework, prompt: c.prompt},
      references: c.refs.map(({path, sha256}) => ({path, sha256})), messages, payloadHash: hash(JSON.stringify(messages))};
  });
}));
const uniquePins = [...new Set(pins)].map(p => ({path: p, sha256: hash(read(p))}));
const manifest = {
  schema: 1, experiment: 'local-os26-released-vs-compact-b-20261106',
  sourceCommit: execFileSync('git', ['rev-parse', 'HEAD'], {cwd: repo, encoding: 'utf8'}).trim(),
  runnerHash: hash(fs.readFileSync(fileURLToPath(import.meta.url))), catalogRevision: catalog.revision,
  workspacePolicyHash: hash(fs.readFileSync(new URL('./workspace-paths.mjs', import.meta.url))),
  models, conditions: {F: 'released skill + current references', BR: 'compact B subject body + identical metadata/references'},
  pins: uniquePins, jobs: jobs.map(({messages, ...rest}) => ({...rest, inputBytes: Buffer.byteLength(JSON.stringify(messages))})),
  settings: {num_ctx: 16384, num_predict: 1024, temperature: 0, seed: 42, top_p: 1, top_k: 0},
  limits: {calls: 36, perRequestSeconds: 180, campaignSeconds: 3600, inputBytes: 50000, concurrency: 1, retries: 0},
  thinking: false, sessions: 'fresh independent chat per cell', retrieval: 'harness injection only',
  evaluation: 'six known development families; no release promotion; one unblinded reviewer',
  caveats: ['F differs from the earlier 900-token diagnostic in output cap and wrapper; compare within this run.',
    'B is a research draft with pending independent adjudication; owner authorized this local diagnostic.',
    'All subject payloads exclude rubrics, candidate notes, acceptance gates, fixtures and mutation sources.']
};
if (process.argv[2] !== '--execute') {
  await new Promise(resolve => process.stdout.write(JSON.stringify(manifest, null, 2) + '\n', resolve));
  process.exit(0);
}
const out = projectOutputPath(process.argv[3] || `evals/results/local-os26-${Date.now()}`);
if (fs.existsSync(out)) throw Error('New project-local output directory required');
fs.mkdirSync(out, {recursive: true, mode: 0o700});
fs.writeFileSync(path.join(out, 'manifest.json'), JSON.stringify(manifest, null, 2), {mode: 0o600});
fs.writeFileSync(path.join(out, 'payloads.json'), JSON.stringify(jobs, null, 2), {mode: 0o600});
const base = 'http://127.0.0.1:11434';
async function api(route, body, timeout = 180000) {
  const r = await fetch(base + route, {method: body ? 'POST' : 'GET', headers: {'content-type': 'application/json'},
    body: body ? JSON.stringify(body) : undefined, signal: AbortSignal.timeout(timeout)});
  if (!r.ok) throw Error(`Ollama ${route}: HTTP ${r.status}`);
  return r.json();
}
const completed = [];
let loaded = null;
const started = Date.now();
try {
  const inventory = await api('/api/tags');
  const identities = {};
  for (const model of models) {
    const entry = inventory.models.find(x => x.name === model);
    if (!entry?.digest) throw Error(`Missing installed model identity ${model}`);
    identities[model] = {tag: entry, show: await api('/api/show', {model})};
  }
  manifest.identities = identities;
  manifest.ollama = await api('/api/version');
  fs.writeFileSync(path.join(out, 'manifest.json'), JSON.stringify(manifest, null, 2));
  for (const job of jobs) {
    if (Date.now() - started > 3600000) throw Error('Campaign deadline reached');
    for (const p of uniquePins) if (hash(read(p.path)) !== p.sha256) throw Error('Changed input: ' + p.path);
    if (loaded && loaded !== job.model) await api('/api/generate', {model: loaded, keep_alive: 0}, 30000);
    loaded = job.model;
    fs.writeFileSync(path.join(out, 'active.json'), JSON.stringify({id: job.id, startedAt: new Date().toISOString()}));
    const t = Date.now();
    const data = await api('/api/chat', {model: job.model, messages: job.messages, stream: false, think: false,
      keep_alive: '5m', options: manifest.settings});
    if (data.model !== job.model || !data.done) throw Error('Model substitution or incomplete response');
    const after = (await api('/api/tags')).models.find(x => x.name === job.model);
    if (after?.digest !== identities[job.model].tag.digest) throw Error('Model digest changed');
    const output = data.message?.content || '';
    const r = {id: job.id, model: job.model, digest: after.digest, condition: job.condition, prompt: job.prompt,
      payloadHash: job.payloadHash, output, outputHash: hash(output), finish_reason: data.done_reason,
      inputTokens: data.prompt_eval_count, outputTokens: data.eval_count, elapsedSeconds: (Date.now() - t) / 1000,
      totalDuration: data.total_duration, loadDuration: data.load_duration, promptDuration: data.prompt_eval_duration,
      evalDuration: data.eval_duration, thinking: data.message?.thinking || null};
    if (typeof r.inputTokens !== 'number' || typeof r.outputTokens !== 'number') throw Error('Missing token accounting');
    fs.writeFileSync(path.join(out, job.id + '-response.json'), JSON.stringify(data, null, 2), {mode: 0o600});
    fs.appendFileSync(path.join(out, 'records.jsonl'), JSON.stringify(r) + '\n', {mode: 0o600});
    completed.push(r);
    console.log(JSON.stringify({completed: completed.length, total: jobs.length, id: job.id, finish: r.finish_reason,
      input: r.inputTokens, output: r.outputTokens, seconds: r.elapsedSeconds}));
  }
  fs.writeFileSync(path.join(out, 'status.json'), JSON.stringify({state: 'completed', completed: completed.length, total: jobs.length}));
} catch (e) {
  fs.writeFileSync(path.join(out, 'status.json'), JSON.stringify({state: 'stopped', completed: completed.length, total: jobs.length, error: e.message}));
  process.exitCode = 1;
  console.error(e.message);
} finally {
  if (loaded) {
    try { await api('/api/generate', {model: loaded, keep_alive: 0}, 30000); }
    catch (e) { console.error('Unload status unknown: ' + e.message); }
  }
  console.log(JSON.stringify({output: out, completed: completed.length}));
}

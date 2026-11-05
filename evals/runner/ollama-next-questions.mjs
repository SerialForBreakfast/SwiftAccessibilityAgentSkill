/** New development questions. Original benchmark artifacts remain unchanged. */
import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {repo, evaluate, fingerprint, hash, verifyBaseline, readReference} from './lib.mjs';
import {transport} from './ollama-development.mjs';
import {LOOKUP_INSTRUCTION} from './llamacpp-development.mjs';
import {protocol} from './protocol.mjs';

export const IDS = ['D04', 'D05', 'D06', 'D09', 'D11', 'D19', 'D24', 'D30'];
export function deployment(scenario) {
  const names = {uikit: 'iOS', swiftui: 'iOS', tvos: 'tvOS', macos: 'macOS'};
  const frameworks = {uikit: 'UIKit', swiftui: 'SwiftUI', tvos: 'UIKit', macos: 'AppKit'};
  if (!names[scenario.platform] || !scenario.os?.length) throw Error('Unsupported platform');
  return `${names[scenario.platform]} ${scenario.os[0]}; ${frameworks[scenario.platform]}`;
}
export function plan(scenarios) {
  return IDS.flatMap(id => {
    const s = scenarios.find(s => s.id === id);
    if (!s || s.split !== 'development' || s.turns.length !== 1 || !s.references.length) throw Error('Expected single-turn development case');
    const selected = {...s, os: [s.os[0]], turns: s.turns.map(t => `${t}\nDeployment context: ${deployment(s)}.`)};
    return ['C0', 'C2', 'C3-explicit'].map(arm => ({scenario: selected, arm, condition: arm.startsWith('C3') ? 'C3' : arm, outputLimit: 2048}));
  });
}
async function main() {
  verifyBaseline();
  const jobs = plan(JSON.parse(fs.readFileSync(path.join(repo, 'evals/scenarios.json'))));
  const pin = fingerprint(repo);
  const refs = [...new Set(jobs.flatMap(j => j.scenario.references))].map(name => {
    const r = readReference(repo, name); return {path: r.path, bytes: r.bytes, sha256: r.sha256};
  });
  const metadata = {alias: 'maxmini', model: 'qwen3.5:latest', revision: 'dec52a44569a2a25341c4e4d3fee25846eed4f6f0b936278e3a3c900bb99d37c', serving: 'Ollama 0.40.11 Metal', quantization: 'Q4_K_M', contextLimit: 16384, reasoning: 'off', sampling: {temperature: 0, seed: 42, top_p: 1, top_k: 0, presence_penalty: 0, repeat_penalty: 1}, concurrency: 1, maxTokens: 2048};
  const sourcePins = ['lib.mjs', 'protocol.mjs', 'ollama-development.mjs', 'llamacpp-development.mjs', 'ollama-next-questions.mjs'].map(name => ({path: `evals/runner/${name}`, sha256: hash(fs.readFileSync(path.join(repo, 'evals/runner', name)))}));
  const manifest = {experiment: 'maxmini-ollama-questions-v2', skillHash: pin, suiteHash: hash(fs.readFileSync(path.join(repo, 'evals/scenarios.json'))), sourcePins, references: refs, provider: metadata, jobs, maxGenerationRequests: 120, requestDeadlineSeconds: 120, cumulativeLimitSeconds: 5400, lookupInstruction: LOOKUP_INSTRUCTION, heldout: false, qualityGraded: false, limitations: ['New families and corrected platform wording; do not pool with development-v1.', 'No C3-original arm or 1024-token arm in this batch.', 'C2 is harness injection. Only successful C3 reads count as model retrieval.', 'Reported tokens and server logs are checked after generation; no qualified pre-generation tokenizer.', 'Execution and protocol measurements are not answer-quality grades.']};
  if (!process.argv.includes('--execute')) { console.log(JSON.stringify(manifest, null, 2)); return; }
  if (process.env.EVAL_ALLOW_NETWORK !== '1' || !process.env.EVAL_OUTPUT) throw Error('Explicit execution and a new output directory required');
  const out = process.env.EVAL_OUTPUT;
  fs.mkdirSync(out, {mode: 0o700});
  fs.writeFileSync(path.join(out, 'manifest.json'), JSON.stringify(manifest, null, 2));
  const counter = {calls: 0}, deadline = performance.now() + 5400000;
  let completed = 0, active = null;
  try {
    for (const j of jobs) {
      if (fingerprint(repo) !== pin) throw Error('Skill changed');
      for (const p of sourcePins) if (hash(fs.readFileSync(path.join(repo, p.path))) !== p.sha256) throw Error('Runner changed');
      active = `${j.scenario.id}-${j.scenario.os[0]}-2048-${j.arm}`;
      const exchanges = [], config = {url: 'http://127.0.0.1:11434/v1', model: metadata.model, maxTokens: 2048, extra: {temperature: 0, seed: 42}, metadata};
      const send = transport({out, arm: j.arm, caseId: active, counter, exchanges});
      const bounded = async (...args) => {
        if (counter.calls >= 120 || performance.now() > deadline) throw Error('Campaign budget exhausted');
        return send(...args);
      };
      const started = performance.now();
      const result = await evaluate({root: repo, condition: j.condition, scenario: j.scenario, config, fetcher: bounded});
      result.metadata.protocol = protocol(result, fs.readFileSync(path.join(repo, 'VERSION'), 'utf8').trim());
      fs.appendFileSync(path.join(out, 'records.jsonl'), JSON.stringify({case: active, arm: j.arm, outputLimit: 2048, scenario: j.scenario.id, os: j.scenario.os[0], question: j.scenario.turns, seconds: (performance.now() - started) / 1000, exchanges, ...result}) + '\n');
      completed++;
      console.log(JSON.stringify({case: active, completed, calls: counter.calls, reads: result.metadata.trace.length, truncated: exchanges.some(e => e.finishReason === 'length')}));
    }
    fs.writeFileSync(path.join(out, 'summary.json'), JSON.stringify({state: 'completed', completed, calls: counter.calls}));
  } catch (e) {
    fs.writeFileSync(path.join(out, 'summary.json'), JSON.stringify({state: 'stopped', completed, calls: counter.calls, active, error: e.message}));
    throw e;
  }
}
if (process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url)) main().catch(e => { console.error(e.message); process.exitCode = 1; });

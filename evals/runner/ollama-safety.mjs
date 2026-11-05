import fs from 'node:fs';
import path from 'node:path';

export function requestTimeout(deadlineEpochMs, now = Date.now()) {
  if (!Number.isSafeInteger(deadlineEpochMs)) throw Error('Recorded absolute deadline required');
  const remaining = deadlineEpochMs - now;
  if (remaining <= 0) throw Error('Campaign deadline exhausted');
  return Math.min(120000, remaining);
}

export function recordedDeadline(manifest) {
  requestTimeout(manifest.deadlineEpochMs);
  return manifest.deadlineEpochMs;
}

export function identityDigest(value) {
  if (!/^[a-f0-9]{64}$/.test(value || '')) throw Error('Verified Ollama manifest digest required (not a weights-layer hash)');
  return value;
}

export async function verifyIdentity({model, expectedDigest, deadlineEpochMs, fetcher = fetch}) {
  identityDigest(expectedDigest);
  const response = await fetcher('http://127.0.0.1:11434/api/tags', {
    redirect: 'error', signal: AbortSignal.timeout(requestTimeout(deadlineEpochMs))
  });
  if (!response.ok) throw Error('Model identity lookup failed');
  const data = await response.json();
  const matches = data.models?.filter(m => m.name === model || m.model === model) || [];
  if (matches.length !== 1 || matches[0].digest?.replace(/^sha256:/, '') !== expectedDigest) {
    throw Error('Model manifest identity changed');
  }
  requestTimeout(deadlineEpochMs);
  return {model, manifestDigest: expectedDigest, verifiedAt: new Date().toISOString()};
}

export function executionSafety(minutes) {
  // These historical adapters lack exact pre-generation tokenization and cannot qualify a portable pilot.
  if (process.env.EVAL_DIAGNOSTIC_ONLY !== '1') throw Error('Tokenizer unavailable: diagnostic-only approval required');
  return {expectedDigest: identityDigest(process.env.OLLAMA_MANIFEST_DIGEST),
    deadlineEpochMs: Date.now() + minutes * 60000, tokenFit: 'unqualified-diagnostic-only'};
}

export function saveFailure(out, id, status) {
  fs.writeFileSync(path.join(out, `failure-${id}.json`), JSON.stringify({
    status, retry: false, recordedAt: new Date().toISOString()
  }), {flag: 'wx', mode: 0o600});
}

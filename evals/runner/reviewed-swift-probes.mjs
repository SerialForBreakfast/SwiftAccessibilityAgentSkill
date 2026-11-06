// Type-check explicitly reviewed adaptations; never executes generated Swift.
// Raw answers, exact fences, scaffolds and diagnostics are retained privately.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {spawnSync} from 'node:child_process';
import {fileURLToPath} from 'node:url';

export const sha256 = b => crypto.createHash('sha256').update(b).digest('hex');
export function swiftBlocks(answer) {
  return [...answer.matchAll(/^```(?:swift|Swift)[ \t]*\r?\n([\s\S]*?)^```[ \t]*$/gm)].map(m => m[1]);
}
export function adapt(answer, adaptation) {
  const blocks = swiftBlocks(answer);
  if (!Array.isArray(adaptation.blocks) || !adaptation.blocks.length) throw Error('Explicit block indexes required');
  const selected = adaptation.blocks.map(i => {
    if (!Number.isInteger(i) || i < 0 || i >= blocks.length) throw Error('Invalid Swift fence index');
    return blocks[i];
  });
  // Imports may move to file scope; no other generated code is changed.
  const imports = [];
  const bodies = selected.map(b => b.replace(/^import [A-Za-z_][A-Za-z0-9_.]*[ \t]*\r?\n/gm, line => { imports.push(line.trim()); return ''; }));
  return {blocks, source: [...new Set(imports)].join('\n') + '\n' + (adaptation.prefix || '') + '\n' + bodies.join('\n') + '\n' + (adaptation.suffix || '')};
}
function command(command, args, timeout = 120000) {
  const r = spawnSync(command, args, {encoding: 'utf8', timeout, maxBuffer: 8 * 1024 * 1024});
  return {exitCode: r.status, signal: r.signal, error: r.error?.code || null, stdout: r.stdout || '', stderr: r.stderr || ''};
}
function main() {
  const [recordsFile, planFile, out] = process.argv.slice(2);
  if (!recordsFile || !planFile || !out || !path.isAbsolute(out) || fs.existsSync(out)) throw Error('Usage: node reviewed-swift-probes.mjs RECORDS REVIEWED_PLAN NEW_ABSOLUTE_DIRECTORY');
  const recordBytes = fs.readFileSync(recordsFile);
  const planBytes = fs.readFileSync(planFile);
  const records = recordBytes.toString('utf8').split('\n').filter(Boolean).map(JSON.parse);
  const plan = JSON.parse(planBytes);
  fs.mkdirSync(out, {mode: 0o700});
  fs.writeFileSync(path.join(out, 'records-snapshot.jsonl'), recordBytes, {mode: 0o600});
  fs.writeFileSync(path.join(out, 'reviewed-plan.json'), planBytes, {mode: 0o600});
  const sdks = {};
  for (const name of ['iphonesimulator', 'appletvsimulator']) {
    const r = command('xcrun', ['--sdk', name, '--show-sdk-path']);
    if (r.exitCode !== 0) throw Error('SDK unavailable: ' + name);
    sdks[name] = r.stdout.trim();
  }
  const results = [];
  for (const p of plan.probes) {
    if (!['iOS', 'iPadOS', 'tvOS'].includes(p.platform)) throw Error('Unsupported reviewed target: ' + p.platform);
    const record = records.find(r => r.id === p.recordId);
    if (!record || sha256(record.output) !== p.answerHash) throw Error('Missing/changed reviewed answer: ' + p.recordId);
    const row = {recordId: record.id, answerHash: p.answerHash, reviewNote: p.reviewNote, platform: p.platform};
    if (p.notApplicable || p.notAssessable) {
      results.push({...row, status: p.notApplicable ? 'not_applicable' : 'not_assessable', reason: p.notApplicable || p.notAssessable});
      continue;
    }
    const {blocks, source} = adapt(record.output, p);
    const stem = String(results.length).padStart(2, '0') + '-' + record.id.replaceAll(/[^a-zA-Z0-9_-]/g, '_');
    fs.writeFileSync(path.join(out, stem + '-answer.txt'), record.output, {mode: 0o600});
    blocks.forEach((b, i) => fs.writeFileSync(path.join(out, stem + `-block-${i}.swift`), b, {mode: 0o600}));
    const sourcePath = path.join(out, stem + '-probe.swift');
    fs.writeFileSync(sourcePath, source, {mode: 0o600});
    fs.writeFileSync(path.join(out, stem + '-adaptation.json'), JSON.stringify(p, null, 2), {mode: 0o600});
    const sdk = p.platform === 'tvOS' ? 'appletvsimulator' : 'iphonesimulator';
    const target = p.platform === 'tvOS' ? 'arm64-apple-tvos26.0-simulator' : 'arm64-apple-ios26.0-simulator';
    const args = ['swiftc', '-sdk', sdks[sdk], '-target', target, '-swift-version', '6', '-typecheck', '-parse-as-library', '-module-name', 'ReviewedProbe', sourcePath];
    const r = command('xcrun', args);
    const status = r.error || r.signal ? 'infrastructure_error' : r.exitCode === 0 ? 'typecheck_pass' : 'typecheck_failed';
    results.push({...row, status, blocks: p.blocks, sourceHash: sha256(source), command: ['xcrun', ...args], ...r});
    fs.writeFileSync(path.join(out, 'results.json'), JSON.stringify(results, null, 2));
    console.log(JSON.stringify({recordId: record.id, status}));
    if (status === 'infrastructure_error') break;
  }
  fs.writeFileSync(path.join(out, 'results.json'), JSON.stringify(results, null, 2));
  fs.writeFileSync(path.join(out, 'manifest.json'), JSON.stringify({runnerHash: sha256(fs.readFileSync(fileURLToPath(import.meta.url))), recordsHash: sha256(recordBytes), planHash: sha256(planBytes), sdks, compiler: command('xcrun', ['swiftc', '--version']), xcode: command('xcodebuild', ['-version'])}, null, 2));
}
if (process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url)) main();

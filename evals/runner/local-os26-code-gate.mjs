// Compile/API gate for locally generated answers to the six OS26 development prompts.
// This is diagnostic evidence, not a quality grade or gold-promotion receipt.
import fs from 'node:fs';
import path from 'node:path';
import {spawnSync} from 'node:child_process';
import {projectOutputPath, runEnvironment} from './workspace-paths.mjs';

const args = process.argv.slice(2);
const records = [];
let output = null;
for (let i = 0; i < args.length; i++) {
  if (args[i] === '--records') records.push(args[++i]);
  else if (args[i] === '--out') output = args[++i];
  else throw Error(`Unknown argument: ${args[i]}`);
}
if (!records.length) {
  throw Error('Usage: node evals/runner/local-os26-code-gate.mjs --records FILE [--records FILE...] [--out PROJECT_JSON]');
}
output = projectOutputPath(output || `evals/results/local-os26-code-gate-${Date.now()}.json`);
if (fs.existsSync(output)) throw Error('New project-local output file required');

const repo = path.resolve(path.dirname(new URL(import.meta.url).pathname), '../..');
const sdk = {
  iOS: '/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneSimulator.platform/Developer/SDKs/iPhoneSimulator27.0.sdk',
  tvOS: '/Applications/Xcode.app/Contents/Developer/Platforms/AppleTVSimulator.platform/Developer/SDKs/AppleTVSimulator27.0.sdk'
};
const target = {iOS: 'arm64-apple-ios26.0-simulator', tvOS: 'arm64-apple-tvos26.0-simulator'};
fs.mkdirSync(path.dirname(output), {recursive: true, mode: 0o700});
const sourceDir = fs.mkdtempSync(path.join(path.dirname(output), 'swift-accessibility-code-gate-'));
const env = runEnvironment(sourceDir);

function codeBlock(text) {
  return text.match(/```swift\n([\s\S]*?)```/)?.[1]?.trim() ?? '';
}
function readRecords(file) {
  return fs.readFileSync(file, 'utf8').split('\n').filter(Boolean).map(JSON.parse);
}
function wrapper(record, code) {
  const id = record.prompt.id;
  if (id === 'GP26-01') return `import UIKit\nfunc probe() {\n  let titleLabel = UILabel()\n  let downloadSwitch = UISwitch()\n  let helpButton = UIButton(type: .system)\n  ${code.includes('row =') ? '' : 'let row = UIStackView(arrangedSubviews: [titleLabel, downloadSwitch, helpButton])'}\n  ${code}\n}`;
  if (id === 'GP26-02') return `import UIKit\nstruct Order { let customer: String; let status: String; let isPriority: Bool }\n${code}`;
  if (id === 'GP26-03') return `import UIKit\nfunc probe() {\n  let totalLabel = UILabel()\n  let payButton = UIButton(type: .system)\n  let view = UIView()\n  let formattedTotal = "Total"\n  ${code}\n}`;
  if (id === 'GP26-04') return `import SwiftUI\nstruct Message: Identifiable { let id: UUID; let subject: String }\n${code}`;
  if (id === 'GP26-05') return `import SwiftUI\nstruct Movie: Identifiable { let id: UUID; let title: String; let posterName: String }\nstruct Probe: View {\n  let movies: [Movie]\n  let open: (Movie) -> Void\n  var body: some View {\n    ${code}\n  }\n}`;
  if (id === 'GP26-06') return `import SwiftUI\n${code}`;
  throw Error(`Unsupported prompt ${id}`);
}
function hazards(id, code) {
  const flags = [];
  if (id === 'GP26-01' && /accessibilityElementsHidden\s*=\s*true/.test(code)) flags.push('hides-descendants');
  if ((id === 'GP26-04' || id === 'GP26-05') && !/\bButton\s*\(/.test(code)) flags.push('no-native-button');
  if ((id === 'GP26-04' || id === 'GP26-05') && /\.onTapGesture\b/.test(code)) flags.push('gesture-activation');
  if ((id === 'GP26-04' || id === 'GP26-05') && /\.accessibilityAction\s*\(\s*"/.test(code)) flags.push('string-accessibility-action-overload');
  if (id === 'GP26-05' && /\.accessibilityTraits\s*\(/.test(code)) flags.push('legacy-accessibilityTraits-modifier');
  if (id === 'GP26-03' && /systemFont\s*\(\s*ofSize\s*:\s*17/.test(code)) flags.push('fixed-font-size');
  if (id === 'GP26-06' && /\.accessibilityValue\s*\(/.test(code)) flags.push('native-toggle-override');
  return flags;
}
function compile(source, platform, file) {
  const result = spawnSync('xcrun', ['swiftc', '-sdk', sdk[platform], '-target', target[platform], '-typecheck', '-parse-as-library', '-module-cache-path', env.SWIFT_MODULECACHE_PATH, '-module-name', 'GeneratedProbe', file], {encoding: 'utf8', timeout: 120000, env, maxBuffer: 8 * 1024 * 1024});
  return {ok: result.status === 0, exitCode: result.status, signal: result.signal ?? null, error: result.error?.code ?? null, diagnostics: `${result.stdout ?? ''}${result.stderr ?? ''}`.trim()};
}

const rows = [];
for (const file of records) for (const record of readRecords(file)) {
  const code = codeBlock(record.output || '');
  const row = {model: record.model, prompt: record.prompt.id, platform: record.prompt.platform, codeExtracted: Boolean(code), hazards: hazards(record.prompt.id, code)};
  if (!code) { row.compile = {ok: false, reason: 'no-swift-code-block'}; rows.push(row); continue; }
  const source = wrapper(record, code);
  const sourceFile = path.join(sourceDir, `${rows.length}-${record.model.replaceAll(/[^a-z0-9]+/gi, '_')}-${record.prompt.id}.swift`);
  fs.writeFileSync(sourceFile, source);
  row.compile = compile(source, record.prompt.platform === 'tvOS' ? 'tvOS' : 'iOS', sourceFile);
  rows.push(row);
}

const summary = {};
for (const model of [...new Set(rows.map(r => r.model))]) {
  const rs = rows.filter(r => r.model === model);
  summary[model] = {prompts: rs.length, codeBlocks: rs.filter(r => r.codeExtracted).length, compilePass: rs.filter(r => r.compile.ok).length, compileFail: rs.filter(r => !r.compile.ok).length, hazardCounts: Object.fromEntries([...new Set(rs.flatMap(r => r.hazards))].map(h => [h, rs.filter(r => r.hazards.includes(h)).length]))};
}
const result = {schema: 1, gate: 'local-os26-code-gate', note: 'Diagnostic compile/API evidence only; not a quality grade or gold-promotion receipt.', inputs: records, sdk: {iOS: sdk.iOS, tvOS: sdk.tvOS}, rows, summary};
fs.writeFileSync(output, JSON.stringify(result, null, 2), {mode: 0o600});
console.log(JSON.stringify({state: 'completed', output, summary}));

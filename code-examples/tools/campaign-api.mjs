// Compiler-resolved declaration inventory. Missing locators stay unresolved.
import fs from 'node:fs';
import path from 'node:path';
import {spawnSync} from 'node:child_process';
import {hash} from './contracts.mjs';
import {selectedPackages} from './campaign-core.mjs';
import {enclosingObjCScope} from './declaration-scope.mjs';

const [privateOutput, reportFile, ...packageDirectories] = process.argv.slice(2);
if (!privateOutput || !path.isAbsolute(privateOutput) || !reportFile) throw Error('Usage: campaign-api.mjs NEW_PRIVATE_OUTPUT NEW_REPORT');
fs.mkdirSync(privateOutput, {mode: 0o700});
const probe = args => {
  const r = spawnSync('xcrun', args, {encoding: 'utf8', timeout: 120000});
  if (r.status !== 0) throw Error('SDK probe failed');
  return r.stdout.trim();
};
const sdk = probe(['--sdk', 'iphonesimulator', '--show-sdk-path']);
const entries = new Map(), runs = [];
for (const [index, pkg] of (packageDirectories.length ? packageDirectories : selectedPackages(process.cwd())).entries()) {
  const manifest = JSON.parse(fs.readFileSync(pkg + '/manifest.json'));
  const sources = manifest.files.filter(f => f.path.startsWith('Sources/') && f.path.endsWith('.swift'));
  const command = ['swiftc', '-sdk', sdk, '-target', 'arm64-apple-ios26.0-simulator', '-typecheck', '-dump-ast',
    '-module-name', 'Audit', ...sources.map(f => pkg + '/' + f.path)];
  const r = spawnSync('xcrun', command, {encoding: 'utf8', timeout: 120000, maxBuffer: 64 * 1024 * 1024});
  const key = `p${index + 1}`;
  fs.writeFileSync(path.join(privateOutput, key + '.ast'), r.stdout ?? '', {flag: 'wx'});
  fs.writeFileSync(path.join(privateOutput, key + '.diagnostics'), r.stderr ?? '', {flag: 'wx'});
  fs.writeFileSync(path.join(privateOutput, key + '.command.json'), JSON.stringify(command), {flag: 'wx'});
  runs.push({package: pkg, exitCode: r.status, signal: r.signal, error: r.error?.code ?? null,
    sources, astHash: hash(r.stdout ?? ''), diagnosticsHash: hash(r.stderr ?? '')});
  if (r.status !== 0 || r.error || r.signal) continue;
  for (const match of r.stdout.matchAll(/(?:decl|override)="([^"\n]+)"/g)) {
    const value = match[1];
    const module = value.split('.')[0];
    if (['Audit', 'Swift', '_Concurrency', 'SwiftShims', 'Builtin'].includes(module) || !value.includes('(file)')) continue;
    const clean = value.replace(/ \[with .*$/, '');
    const symbol = clean.split('@')[0];
    const key = symbol;
    if (entries.has(key)) { entries.get(key).packages.add(pkg); continue; }
    const row = {symbol, module, packages: new Set([pkg]), status: 'unresolved-declaration-location',
      declaration: null, enclosingDeclaration: null, availability: [], introduction: null,
      note: 'Compiler accepted at deployment26 with this SDK; no introduction date inferred.'};
    const loc = clean.match(/@(.+):(\d+):(\d+)$/);
    if (loc && loc[1].startsWith(sdk + '/') && fs.existsSync(loc[1])) {
      const bytes = fs.readFileSync(loc[1]), lines = bytes.toString().split('\n'), line = Number(loc[2]);
      let start = line - 1;
      while (start > 0 && line - start < 8 && /^(\s|\/|\*|@available|API_|NS_|UIKIT_|AVF_|COREMEDIA_)/.test(lines[start - 1])) start--;
      let end = line;
      while (end < lines.length && end - line < 8 && !/[;{}]/.test(lines[end - 1])) end++;
      const context = lines.slice(start, end);
      const enclosing = enclosingObjCScope(lines, line);
      row.status = 'located-availability-context';
      row.declaration = {path: loc[1].slice(sdk.length + 1), line, column: Number(loc[3]),
        sha256: hash(bytes), contextStart: start + 1, context};
      row.enclosingDeclaration = enclosing;
      row.availability = [...context, ...(enclosing?.context ?? [])].filter(l => /API_AVAILABLE|API_DEPRECATED|API_UNAVAILABLE|@available|NS_AVAILABLE|NS_DEPRECATED/.test(l));
      row.note = row.availability.length ? 'Exact availability context retained; enclosing/renamed overlays require reviewer interpretation.' :
        'Declaration located; no explicit version annotation captured. Introduction remains unresolved.';
    }
    entries.set(key, row);
  }
}
const rows = [...entries.values()].map(r => ({...r, packages: [...r.packages]})).sort((a, b) => a.symbol.localeCompare(b.symbol));
const report = {schema: 1, scope: 'Compiler-resolved external member/override references in selected production source sets; excludes test/helper APIs, Swift standard library and transitive SDK internals. Type-only uses and synthesized/conformance requirements require separate source review.',
  status: 'inventory-with-explicit-unresolved-availability', sdkVersion: probe(['--sdk', 'iphonesimulator', '--show-sdk-version']),
  sdkBuild: probe(['--sdk', 'iphonesimulator', '--show-sdk-build-version']), target: 'arm64-apple-ios26.0-simulator', runs, rows};
fs.mkdirSync(path.dirname(reportFile), {recursive: true});
fs.writeFileSync(reportFile, JSON.stringify(report, null, 2) + '\n', {flag: 'wx'});
console.log(JSON.stringify({packages: runs.length, rows: rows.length, located: rows.filter(r => r.declaration).length,
  failedScans: runs.filter(r => r.exitCode !== 0).length}));

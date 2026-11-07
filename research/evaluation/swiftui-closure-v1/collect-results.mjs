// Preserve derived public receipts. Original bytes remain in private attempts/archive.
import fs from 'node:fs';
import path from 'node:path';
import {hash} from '../../../code-examples/tools/contracts.mjs';
const base = 'research/evaluation/swiftui-closure-v1';
const roots = process.argv.slice(2);
if (!roots.length || roots.some(p => !path.isAbsolute(p))) throw Error('Supply explicit private attempt roots');
const publicRoot = base + '/native-evidence';
fs.mkdirSync(publicRoot, {recursive: true});
const sanitize = s => s.replaceAll(process.cwd(), '<REPOSITORY>')
  .replaceAll(process.env.HOME, '<HOME>')
  .replaceAll('/private/tmp/', '<PRIVATE_TMP>/').replaceAll('/tmp/', '<PRIVATE_TMP>/')
  .replace(/\b[0-9A-F]{8}-[0-9A-F]{16}\b/g, '<HOST_DEVICE_ID>')
  .replace(/\b[0-9A-F]{8}-(?:[0-9A-F]{4}-){3}[0-9A-F]{12}\b/g, '<DEVICE_OR_RUN_UUID>');
const attempts = [];
for (const root of roots) {
  const rootId = path.basename(root);
  for (const name of fs.readdirSync(root).sort()) {
    const input = path.join(root, name), file = path.join(input, 'result.json');
    if (!fs.existsSync(file)) continue;
    const raw = fs.readFileSync(file), r = JSON.parse(raw);
    const target = publicRoot + '/' + rootId + '/' + name;
    fs.mkdirSync(target, {recursive: true});
    const artifacts = [];
    for (const entry of r.artifacts) {
      const original = fs.readFileSync(path.join(input, entry.path));
      if (hash(original) !== entry.sha256) throw Error('Original artifact drift: ' + entry.path);
      const bytes = entry.path.startsWith('inputs/') || entry.path.startsWith('adapter-') || entry.path === 'manifest.json'
        ? original : Buffer.from(sanitize(original.toString('utf8')));
      const output = target + '/' + entry.path;
      fs.mkdirSync(path.dirname(output), {recursive: true});
      // Idempotent collection is permitted only for byte-identical derived artifacts.
      if (fs.existsSync(output) && !fs.readFileSync(output).equals(bytes)) throw Error('Derived receipt changed: ' + output);
      if (!fs.existsSync(output)) fs.writeFileSync(output, bytes, {flag: 'wx'});
      artifacts.push({path: output, sha256: hash(bytes), originalSha256: entry.sha256,
        transformation: original.equals(bytes) ? 'none' : 'path-and-device-identifier-redaction'});
    }
    const manifest = JSON.parse(fs.readFileSync(input + '/manifest.json'));
    const derived = {attempt: rootId + '/' + name, package: manifest.id, revision: manifest.revision,
      checkId: r.checkId, originalResultHash: hash(raw), manifestHash: r.manifestHash,
      status: r.status, observed: r.observed, reason: r.reason ?? null,
      failureClassification: r.failureClassification ?? null, recordedAt: r.recordedAt,
      environment: r.environment ?? null, execution: r.execution ?? null,
      command: r.command ?? null, artifacts,
      provenance: 'derived public record; original result in private archive; redaction is not fresh execution'};
    const bytes = sanitize(JSON.stringify(derived, null, 2) + '\n');
    const output = target + '/derived-result.json';
    if (fs.existsSync(output) && fs.readFileSync(output, 'utf8') !== bytes) throw Error('Derived result changed');
    if (!fs.existsSync(output)) fs.writeFileSync(output, bytes, {flag: 'wx'});
    attempts.push({...JSON.parse(bytes), publicResult: {path: output, sha256: hash(bytes)}});
  }
}
const index = {schema: 1, scope: 'SwiftUI media code contracts; no model or generated-accessibility result', attempts};
fs.writeFileSync(base + '/results-index.json', JSON.stringify(index, null, 2) + '\n');
console.log(JSON.stringify({attempts: attempts.length, statuses: Object.fromEntries(
  [...new Set(attempts.map(a => a.status))].map(k => [k, attempts.filter(a => a.status === k).length]))}));

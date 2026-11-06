import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import assert from 'node:assert/strict';
import {fileURLToPath} from 'node:url';

const directory = path.dirname(fileURLToPath(import.meta.url));
const root = path.resolve(directory, '../../..');
const bytes = fs.readFileSync(path.join(directory, 'evidence.json'));
const record = JSON.parse(bytes);
const hash = value => crypto.createHash('sha256').update(value).digest('hex');
function source(relative) {
  const resolved = path.resolve(root, relative);
  assert.ok(resolved.startsWith(root + path.sep), 'Path must remain in repository');
  return fs.readFileSync(resolved);
}
for (const file of record.files) {
  assert.equal(hash(source(file.path)), file.sha256, `Pinned input drift: ${file.path}`);
}
const snippets = record.incidents.flatMap(c => [...c.before, ...c.after]);
snippets.push(record.supplemental.before, record.supplemental.after, record.supplemental.test);
for (const snippet of snippets) {
  const text = source(snippet.path).toString();
  assert.equal(hash(text), snippet.fileHash);
  const offset = text.indexOf(snippet.code);
  assert.ok(offset >= 0, `Excerpt differs: ${snippet.path}`);
  assert.equal(text.slice(0, offset).split('\n').length, snippet.startLine);
}
for (const report of record.publicReports) {
  assert.equal(hash(source(report.path)), report.sha256);
  assert.deepEqual(JSON.parse(source(report.path)), report.data);
}
for (const entry of record.current) {
  const manifest = JSON.parse(source(entry.manifest));
  const report = record.publicReports.find(r => r.path === entry.report).data;
  assert.equal(report.manifestHash, hash(source(entry.manifest)));
  for (const check of manifest.checks) {
    const row = report.rows.find(r => r.check === check.id);
    assert.equal(row?.status, 'passed', `${entry.id}/${check.id}`);
    assert.equal(row.expected, check.expected);
    assert.equal(row.observed, check.expected === 'success' ? 'success' : 'failure');
  }
}
for (const mutation of record.mutations) {
  assert.equal(hash(source(mutation.mutant)), mutation.mutantHash);
  assert.equal(mutation.status, 'passed');
  assert.equal(mutation.observed, 'failure');
}
for (const name of ['README.md', 'incidents.md', 'mutation-catalog.md']) {
  const text = fs.readFileSync(path.join(directory, name), 'utf8');
  for (const match of text.matchAll(/\]\(([^)\s]+)\)/g)) {
    if (/^https?:/.test(match[1])) continue;
    assert.ok(fs.existsSync(path.resolve(directory, match[1].split('#')[0])), `Broken link: ${match[1]}`);
  }
}
assert.ok(!/\/Users\/|\/private\/|\/tmp\//.test(bytes.toString()), 'Private path in evidence');
console.log(JSON.stringify({status: 'verified', nativeExecution: false,
  pinnedFiles: record.files.length, exactSnippets: snippets.length,
  publicReports: record.publicReports.length, incidents: record.incidents.length,
  deliberateMutations: record.mutations.length}, null, 2));

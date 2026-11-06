import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import {fileURLToPath} from 'node:url';
import {nativePlan} from './native-core.mjs';
import {hash} from './contracts.mjs';

const base = new URL('../pilots/uikit-media-metadata-v1/', import.meta.url);
const read = p => fs.readFileSync(new URL(p, base));
const manifest = JSON.parse(read('manifest.json'));

test('media metadata coverage binds seven methods and three mutants', () => {
  const coverage = JSON.parse(read('coverage.json'));
  const tests = manifest.checks.find(c => c.id === 'metadata-unit').testIds;
  assert.equal(tests.length, 7);
  assert.deepEqual(coverage.assertions.map(a => a.testId).sort(), [...tests].sort());
  for (const a of coverage.assertions) {
    assert.ok(manifest.claims.some(c => c.id === a.claimId));
    assert.deepEqual(a.guidelines, ['U-015']);
    assert.equal(a.promptStatus, 'draft-not-gold');
    assert.ok(read('Tests/MediaMetadataTests.swift').toString().includes('func ' + a.testId.split('/')[1] + '('));
  }
  assert.equal(manifest.checks.filter(c => c.expected === 'failure').length, 3);
  for (const c of manifest.checks) nativePlan(manifest, fileURLToPath(base), c.id);
});

test('metadata fixture payload hashes and media samples are preserved', () => {
  const swift = read('Tests/DescriptionFixture.swift').toString();
  const provenance = JSON.parse(read('fixture-provenance.json'));
  const payloads = {};
  for (const name of ['positive', 'control']) {
    const match = swift.match(new RegExp('private static let ' + name + ' = """\\n([\\s\\S]*?)"""'));
    const bytes = Buffer.from(match[1].replace(/\s/g, ''), 'base64');
    assert.equal(hash(bytes), provenance[name].sha256);
    assert.equal(bytes.length, provenance[name].bytes);
    const atoms = [];
    for (let p = 0; p < bytes.length;) {
      const size = bytes.readUInt32BE(p);
      assert.ok(size >= 8 && p + size <= bytes.length);
      atoms.push({type: bytes.toString('ascii', p + 4, p + 8), bytes: bytes.subarray(p, p + size)});
      p += size;
    }
    assert.equal(atoms.at(-1).type, 'moov');
    payloads[name] = atoms;
  }
  assert.deepEqual(payloads.positive.slice(0, -1), payloads.control.slice(0, -1));
  const tag = 'public.accessibility.describes-video';
  assert.equal(payloads.positive.at(-1).bytes.toString().split(tag).length - 1, 1);
  assert.equal(payloads.control.at(-1).bytes.includes(Buffer.from(tag)), false);
});

test('metadata subject prompt stays separate from pinned grading files', () => {
  const prompt = JSON.parse(read('evaluation/prompt.json'));
  assert.deepEqual(Object.keys(prompt).sort(), ['id', 'prompt', 'revision']);
  assert.ok(!/tagc|NegativeFixtures|testTagged|MM04/.test(prompt.prompt));
  const record = JSON.parse(read('evaluation/case.json'));
  assert.equal(record.status, 'draft-independent-review-pending');
  assert.equal(record.modelRuns, 0);
  assert.equal(record.split, 'development');
  assert.deepEqual(record.subjectFiles, ['evaluation/prompt.json']);
  for (const f of record.files) assert.equal(hash(read(f.path)), f.sha256, f.path);
});

test('metadata deprecation repair preserves first source and exact input hashes', () => {
  const old = JSON.parse(read('history/revision-1/manifest.json'));
  for (const f of old.files) assert.equal(hash(read('history/revision-1/' + f.path)), f.sha256);
  const source = read('history/revision-1/Sources/MediaMetadata.swift').toString();
  assert.equal(source.replace('option.locale?.languageCode', 'option.locale?.language.languageCode?.identifier'), read('Sources/MediaMetadata.swift').toString());
  assert.equal(old.revision, '1');
  assert.equal(manifest.revision, '2');
});

test('metadata reports bind first attempt and current native outcomes', () => {
  const first = JSON.parse(read('validation/revision-1.json'));
  assert.equal(first.manifestHash, hash(read('history/revision-1/manifest.json')));
  assert.equal(first.rows.length, 2);
  assert.ok(first.rows.find(r => r.lane === 'compile').excerpts.some(l => l.includes("'languageCode' was deprecated")));
  for (const row of first.rows) assert.equal(row.status, 'passed');
  const current = JSON.parse(read('validation/revision-2.json'));
  assert.equal(current.manifestHash, hash(read('manifest.json')));
  assert.equal(current.rows.length, manifest.checks.length);
  assert.equal(new Set(current.rows.map(r => r.check)).size, manifest.checks.length);
  for (const c of manifest.checks) {
    const row = current.rows.find(r => r.check === c.id);
    assert.equal(row.status, 'passed');
    assert.equal(row.observed, c.expected);
    assert.equal(row.execution.build, 'passed');
    assert.equal(row.execution.infrastructureError, null);
    assert.equal(row.execution.skippedTests, 0);
    assert.deepEqual([...row.execution.executedTestIds].sort(), [...c.testIds].sort());
    assert.deepEqual([...row.execution.failedTestIds].sort(), [...c.failureIds].sort());
  }
});

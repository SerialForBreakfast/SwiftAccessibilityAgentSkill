import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import {hash} from './contracts.mjs';

const root = new URL('../../', import.meta.url);
const base = new URL('../audits/availability-v1/', import.meta.url);
const read = p => fs.readFileSync(new URL(p, base));

test('availability sweep binds all current pilot sources and compile outcomes', () => {
  const inventory = JSON.parse(read('inventory.json'));
  const report = JSON.parse(read('compile-results.json'));
  assert.equal(report.inventoryHash, hash(read('inventory.json')));
  const pilots = fs.readdirSync(new URL('code-examples/pilots/', root)).filter(d =>
    fs.existsSync(new URL('code-examples/pilots/' + d + '/manifest.json', root))).sort();
  assert.deepEqual(inventory.entries.map(e => e.pilot).sort(), pilots);
  assert.equal(report.rows.length, pilots.length);
  assert.equal(new Set(report.rows.map(r => r.pilot)).size, pilots.length);
  for (const e of inventory.entries) {
    const bytes = fs.readFileSync(new URL(e.manifest, root));
    assert.equal(hash(bytes), e.manifestHash);
    const m = JSON.parse(bytes);
    assert.deepEqual(e.sources.map(f => f.path).sort(), m.files.filter(f => f.path.startsWith('Sources/')).map(f => f.path).sort());
    for (const f of e.sources) {
      const s = fs.readFileSync(new URL('code-examples/pilots/' + e.pilot + '/' + f.path, root));
      assert.equal(hash(s), f.sha256);
      assert.deepEqual(s.toString().split('\n').flatMap((text, i) => /#if|#available|@available/.test(text) ? [{line: i + 1, text}] : []), f.conditionalLines);
    }
    const r = report.rows.find(r => r.pilot === e.pilot);
    assert.equal(r.manifestHash, e.manifestHash);
    assert.equal(r.check, e.compileCheck);
    assert.equal(r.status, 'passed');
    assert.equal(r.observed, 'success');
    assert.equal(r.environment.deploymentTarget, '26.0');
    assert.equal(r.environment.runtimeVersion, null);
    assert.equal(r.execution.build, 'passed');
    assert.equal(r.execution.infrastructureError, null);
    assert.deepEqual([...r.sourcePaths].sort(), e.sources.map(f => f.path).sort());
  }
});

test('availability draft separates subject input from grading and audit evidence', () => {
  const c = JSON.parse(read('evaluation/case.json'));
  assert.equal(c.status, 'draft-independent-review-pending');
  assert.equal(c.split, 'development');
  assert.equal(c.modelRuns, 0);
  assert.deepEqual(c.subjectFiles, ['evaluation/prompt.json']);
  for (const f of c.files) assert.equal(hash(read(f.path)), f.sha256);
  assert.deepEqual(Object.keys(JSON.parse(read('evaluation/prompt.json'))).sort(), ['id', 'prompt', 'revision']);
});

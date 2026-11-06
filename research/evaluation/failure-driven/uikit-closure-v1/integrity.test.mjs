import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {hash, validateManifest} from '../../../../code-examples/tools/contracts.mjs';

const here = path.dirname(fileURLToPath(import.meta.url)), root = path.resolve(here, '../../../..');
const read = f => fs.readFileSync(path.join(here, f));
const json = f => JSON.parse(read(f));
const ledger = json('clause-ledger.json'), catalog = json('assertion-catalog.json').methods;
test('all bounded clauses and rules appear exactly once', () => {
  const inventory = JSON.parse(fs.readFileSync(path.join(root, ledger.inventoryFile)));
  assert.equal(hash(fs.readFileSync(path.join(root, ledger.inventoryFile))), ledger.inventoryHash);
  assert.equal(ledger.clauses.length, 209); assert.equal(ledger.rules.length, 15);
  assert.deepEqual(new Set(ledger.clauses.map(c => c.id)), new Set(inventory.documents.flatMap(d => d.clauses.map(c => c.id))));
  for (const row of [...ledger.clauses, ...ledger.rules]) {
    assert.ok(row.status && row.rationale && row.independentReview);
    assert.equal(hash(fs.readFileSync(path.join(root, row.guidelinePath))), row.guidelineHash);
  }
});
test('all bindings resolve to selected actual test methods', () => {
  for (const b of Object.values(ledger.bindings)) for (const key of b.tests) {
    const method = catalog.find(t => t.key === key);
    assert.ok(method, key); assert.ok(method.assertionCount > 0);
    assert.equal(hash(fs.readFileSync(path.join(root, method.testFile))), method.sourceHash);
  }
});
test('covered clauses require matching executed assertion evidence', () => {
  for (const row of ledger.clauses.filter(c => c.status === 'covered')) {
    assert.ok(row.bindingIds.length);
    for (const b of row.bindingIds) for (const key of ledger.bindings[b].tests) {
      const method = catalog.find(t => t.key === key);
      assert.ok(method.nativeEvidence.length, key);
      for (const e of method.nativeEvidence) {
        assert.equal(hash(fs.readFileSync(path.join(root, e.file))), e.fileHash);
        assert.ok(e.executedTestIds.includes(method.testId));
      }
    }
  }
});
test('new contract package is pinned and has independent payload separation', () => {
  const m = validateManifest(json('gap-contracts/manifest.json'), path.join(here, 'gap-contracts'));
  assert.equal(m.checks.filter(c => c.expected === 'success')[0].testIds.length, 17);
  assert.equal(m.checks.filter(c => c.expected === 'failure').length, 5);
  const prompts = json('gap-contracts/evaluation/prompts.json');
  assert.equal(prompts.cases.length, 3); assert.equal(prompts.holdout, false);
  const rubrics = read('gap-contracts/evaluation/RUBRICS.md').toString();
  for (const c of prompts.cases) {
    assert.ok(rubrics.includes(c.id));
    assert.doesNotMatch(c.prompt, /GAP-|ROUTING:|GapContractTests|NegativeFixtures/);
  }
});
test('availability preserves unresolved dates and source hashes', () => {
  const matrix = json('availability-matrix.json');
  for (const f of matrix.inputs) assert.equal(hash(read(f.file)), f.sha256);
  for (const row of matrix.rows) {
    assert.ok(row.independentReview && row.availabilityStatus);
    if (row.introduction) assert.ok(row.directDeclaration.includes('ios('));
    else assert.equal(row.availabilityStatus, 'unresolved-explicitly');
  }
});
test('declaration-scope first defect and correction remain traceable', () => {
  const incident = json('diagnostics/declaration-scope/record.json');
  assert.equal(hash(read('diagnostics/declaration-scope/first-scanner.mjs.txt')), incident.firstSourceHash);
  assert.equal(hash(read('api-declarations.json')), incident.firstInventoryHash);
  assert.equal(incident.differences.length, 4);
  const matrix = json('availability-matrix.json');
  for (const difference of incident.differences) {
    assert.equal(matrix.rows.find(r=>r.symbol===difference.symbol).enclosingDeclaration, null);
  }
});
test('type inventory binds current production source and explicit declaration status', () => {
  const inventory = json('type-declarations.json');
  assert.equal(inventory.rows.length,43);
  for (const row of inventory.rows) {
    assert.ok(row.status && row.independentReview && row.usages.length);
    for (const usage of row.usages) assert.equal(hash(fs.readFileSync(path.join(root,usage.path))),usage.sha256);
  }
});
test('quantity pre-execution coverage defect preserves first source and manifest', () => {
  const prefix='gap-contracts/history/revision-1/',r=json(prefix+'record.json');
  assert.equal(hash(read(prefix+'Sources/GapContracts.swift')),r.firstSourceHash);
  assert.equal(hash(read(prefix+'manifest.json')),r.firstManifestHash);
  validateManifest(json(prefix+'manifest.json'),path.join(here,prefix));
  assert.equal(json('gap-contracts/manifest.json').revision,'2');
});
test('completed campaign contains every selected check and current input hash', () => {
  const execution=json('execution.json');
  assert.equal(execution.rows.length,104);
  assert.equal(new Set(execution.rows.map(r=>r.campaign+':'+r.key)).size,104);
  assert.equal(execution.counts.uniquePositiveMethods,202);
  for (const campaign of execution.campaigns) {
    assert.equal(execution.rows.filter(r=>r.campaign===campaign.planHash).length,campaign.checks);
    for (const input of campaign.inputs) assert.equal(hash(fs.readFileSync(path.join(root,input.path))),input.sha256);
  }
});
test('positive and negative receipts match their intended native outcomes', () => {
  const execution=json('execution.json');
  for (const row of execution.rows) {
    const m=JSON.parse(fs.readFileSync(path.join(root,row.package,'manifest.json')));
    const c=m.checks.find(c=>c.id===row.check);
    assert.equal(hash(fs.readFileSync(path.join(root,row.package,'manifest.json'))),row.manifestHash);
    assert.equal(row.status,'passed');
    assert.match(row.originalRecordHash,/^[a-f0-9]{64}$/);
    if (row.expected==='failure') {
      assert.equal(row.observed,'failure');
      assert.deepEqual([...(row.lane==='unit'?row.execution.failedTestIds:row.execution.diagnosticIds)].sort(),[...c.failureIds].sort());
    } else assert.equal(row.observed,'success');
  }
});

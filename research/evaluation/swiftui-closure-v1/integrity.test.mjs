import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';
import {hash, validateManifest} from '../../../code-examples/tools/contracts.mjs';
import {classifyUnitFailure} from '../../../code-examples/tools/swiftui-media-diagnostics.mjs';
import {retrieve} from '../../../code-examples/tools/swiftui-media-retrieval.mjs';
const base = 'research/evaluation/swiftui-closure-v1';
const read = p => JSON.parse(fs.readFileSync(p));
const ledger = read(base + '/coverage-ledger.json'), pairs = read(base + '/prompt-records.json').cases;
const original = read('research/evaluation/swiftui-campaign-v1/clause-ledger.json');

test('all 217 original clauses and 15 rules retained without rewriting old dispositions', () => {
  assert.equal(ledger.clauses.length, 217); assert.equal(ledger.rules.length, 15);
  assert.deepEqual(ledger.clauses.map(r => r.id), original.clauses.map(r => r.id));
  assert.equal(Object.values(ledger.counts).reduce((a, b) => a + b, 0), 217);
  for (const row of ledger.clauses) {
    const prior = original.clauses.find(r => r.id === row.id);
    assert.equal(row.text, prior.text); assert.equal(row.originalDisposition, prior.disposition);
    assert.ok(row.rationale.length > 30); assert.equal(row.fullClauseProvenByUnits, false);
    assert.equal(row.independentReview, 'pending');
  }
});
test('all previously unresolved requirements have explicit reviewed scope and no silent full closure', () => {
  for (const prior of original.clauses.filter(r => r.disposition === 'unresolved')) {
    const row = ledger.clauses.find(r => r.id === prior.id);
    assert.notEqual(row.disposition, 'unresolved'); assert.notEqual(row.rationale, prior.rationale);
  }
  assert.equal(ledger.implementationQueue.length, 1);
  assert.equal(ledger.implementationQueue[0].status, 'unresolved');
});
for (const original of ledger.originals) test('original ledger pin: ' + original.path, () => {
  assert.equal(hash(fs.readFileSync(original.path)), original.sha256);
});
test('prior assertion bindings match actual passing execution records', () => {
  const receipts = read('research/evaluation/swiftui-campaign-v1/results-index.json').attempts;
  for (const row of ledger.clauses) for (const key of row.existingEvidence) {
    const binding = ledger.evidenceCatalog[key];
    const receipt = receipts.find(a => a.attempt === binding.execution.attempt);
    assert.ok(receipt); assert.equal(receipt.status, 'passed'); assert.equal(receipt.observed, 'success');
    assert.equal(receipt.originalResultHash, binding.execution.resultHash);
    assert.equal(receipt.manifestHash, binding.manifestHash);
    for (const id of binding.execution.testIds) assert.ok(receipt.execution.executedTestIds.includes(id));
  }
});
test('forwarding overlay pins match actual named unit executions', () => {
  const receipts = read('research/evaluation/swiftui-forwarding-v1/results-index.json').attempts;
  for (const row of ledger.clauses) for (const key of row.forwardingEvidence) {
    const binding = ledger.evidenceCatalog[key];
    const receipt = receipts.find(a => a.attempt === binding.receipt.attempt);
    assert.ok(receipt); assert.equal(receipt.status, 'passed');
    assert.equal(receipt.originalResultHash, binding.receipt.hash);
    assert.equal(hash(fs.readFileSync(binding.manifest)), binding.manifestHash);
    for (const id of binding.testIds) assert.ok(receipt.execution.executedTestIds.includes(id));
  }
});
for (const platform of ['iOS', 'macOS', 'tvOS']) test(platform + ' complete question inputs and disjoint assertion bindings', () => {
  const cases = pairs.filter(c => c.platform === platform); assert.equal(cases.length, 3);
  const manifest = read(cases[0].manifest); validateManifest(manifest, path.dirname(cases[0].manifest));
  const ids = cases.flatMap(c => c.testIds); assert.equal(new Set(ids).size, ids.length);
  assert.deepEqual(ids.sort(), [...manifest.checks.find(c => c.id === 'positive').testIds].sort());
  for (const c of cases) {
    assert.equal(c.framework, 'SwiftUI'); assert.equal(c.status, 'draft');
    assert.equal(hash(fs.readFileSync(c.subject.path)), c.subject.sha256);
    assert.equal(fs.readFileSync(c.subject.path, 'utf8'), c.subject.text);
    assert.equal(hash(fs.readFileSync(c.rubric.path)), c.rubric.sha256);
    assert.match(c.subject.text, /```swift/);
    assert.doesNotMatch(c.subject.text, /ROUTING:|NegativeFixtures|test[A-Z]|manifest\.json/);
    assert.deepEqual(c.outputs, {status: 'not-run', attempts: []});
    for (const id of c.testIds) assert.ok(fs.readFileSync(c.rubric.path, 'utf8').includes(id));
  }
});
for (const platform of ['iOS', 'macOS', 'tvOS']) for (const topic of ['selection', 'ownership', 'wiring']) {
  test(platform + '/' + topic + ' bounded progressive disclosure', () => {
    const q = {platform, framework: 'SwiftUI', topic};
    const g = retrieve(q), e = retrieve({...q, level: 'example'}), c = retrieve({...q, level: 'contract'});
    assert.equal(g.paths.length, 1); assert.equal(e.paths.length, 2); assert.equal(c.paths.length, 5);
    assert.ok(g.loadedBytes < e.loadedBytes && e.loadedBytes < c.loadedBytes); assert.equal(c.tokens, null);
    for (const t of c.trace) {
      assert.equal(hash(fs.readFileSync(t.path)), t.sha256);
      assert.doesNotMatch(t.path, /evaluation|NegativeFixtures|history|rubric/);
    }
  });
}
test('wrong framework and unknown platform never borrow these examples', () => {
  for (const framework of ['UIKit', 'AppKit', 'AVFoundation']) assert.equal(retrieve({platform: 'iOS', framework, topic: 'selection'}).loadedBytes, 0);
  assert.equal(retrieve({platform: 'watchOS', framework: 'SwiftUI', topic: 'selection'}).loadedBytes, 0);
  assert.throws(() => retrieve({platform: 'iOS', framework: 'SwiftUI', topic: 'selection', level: 'all'}));
});
test('test-source compile failure gets no mutant or unit credit', () => {
  const log = fs.readFileSync(base + '/history/revision-1/native.log', 'utf8');
  const diagnosis = classifyUnitFailure({status: 65}, log, {totalTestCount: 0});
  assert.equal(diagnosis.kind, 'test-source-compilation'); assert.equal(diagnosis.creditedTests, 0);
  assert.equal(diagnosis.diagnostics.length, 2);
});
test('Swift 6 isolation failure is retained as test compilation, not accessibility behavior', () => {
  const log = fs.readFileSync(base + '/history/revision-2/native.log', 'utf8');
  const diagnosis = classifyUnitFailure({status: 65}, log, {totalTestCount: 0});
  assert.equal(diagnosis.kind, 'test-source-compilation'); assert.equal(diagnosis.diagnostics.length, 4);
});
test('compiler-looking logs cannot hide timeouts or launched assertions', () => {
  const log = '/Tests/Test.swift:1:2: error: failed\nTesting cancelled because the build failed';
  assert.equal(classifyUnitFailure({status: 65, signal: 'SIGKILL'}, log, {totalTestCount: 0}).kind, 'infrastructure');
  assert.equal(classifyUnitFailure({status: 65, error: {}}, log, {totalTestCount: 0}).kind, 'infrastructure');
  assert.equal(classifyUnitFailure({status: 65}, log, {totalTestCount: 1}), null);
  assert.equal(classifyUnitFailure({status: 65}, log + "\nTest Case '-[A t]' failed", {totalTestCount: 0}), null);
  assert.equal(classifyUnitFailure({status: 0}, log, {totalTestCount: 0}), null);
});
test('native controls use tested selection binding and same player in actual view source', () => {
  const source = fs.readFileSync('code-examples/swiftui/media-shared-v1/MediaSelection.swift', 'utf8');
  assert.match(source, /VideoPlayer\(player: store\.player\)/);
  assert.match(source, /Picker\("Media options", selection: store\.selection\)/);
  assert.match(source, /\.onDisappear \{ store\.cancel\(\) \}/);
  assert.match(source, /Button\("Reload options"\)/);
  // This static wiring guard complements, but does not replace, Swift compilation.
});
test('additive adapters snapshot themselves and preserve historical adapters', () => {
  const runner = fs.readFileSync('code-examples/tools/swiftui-media-campaign.mjs', 'utf8');
  for (const name of ['swiftui-media-native.mjs', 'swiftui-media-platform-native.mjs']) {
    assert.ok(runner.includes(name));
    assert.ok(fs.readFileSync('code-examples/tools/' + name, 'utf8').includes("['" + name + "'"));
  }
});
test('all tracked checkpoint inputs outside permitted task notes remain byte-identical', () => {
  const pins = read(base + '/protected-inputs.json'); assert.equal(pins.baseCommit, '8e51ee9');
  for (const pin of pins.files) assert.equal(hash(fs.readFileSync(pin.path)), pin.sha256, pin.path);
});

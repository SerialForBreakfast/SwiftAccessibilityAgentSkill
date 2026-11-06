import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {validateManifest} from '../../../../code-examples/tools/contracts.mjs';

const root = path.dirname(fileURLToPath(import.meta.url));
const read = name => fs.readFileSync(path.join(root, name), 'utf8');
const manifest = JSON.parse(read('manifest.json'));

test('checkout contract source hashes and manifest validate', () => {
  validateManifest(manifest, root);
});
test('both deliberate mutants run the unchanged positive test selection', () => {
  for (const check of manifest.checks.slice(1)) {
    assert.deepEqual(check.testIds, manifest.checks[0].testIds);
    assert.equal(check.expected, 'failure');
    assert.equal(check.failureIds.length, 1);
  }
});
test('mutants contain exactly their single declared insertion', () => {
  const original = read('Sources/CheckoutSummary.swift');
  for (const [file, inserted] of [
    ['ChangedFont', 'payButton.titleLabel?.font = .preferredFont(forTextStyle: .headline)'],
    ['FixedHeight', 'heightAnchor.constraint(equalToConstant: 44).isActive = true']
  ]) assert.equal(read(`NegativeFixtures/${file}.swift`), original.replace('spacing = 8', `spacing = 8\n        ${inserted}`));
});
test('model-visible draft is distinct from controller evidence', () => {
  const prompt = JSON.parse(read('evaluation/prompt.json'));
  assert.equal(prompt.status, 'development-draft');
  assert.equal(prompt.id, 'UIKIT-CHECKOUT-PRESERVATION-D1');
  assert.doesNotMatch(prompt.prompt, /R16|ChangedFont|FixedHeight|testPreserves|ROUTING:/);
  assert.ok(fs.existsSync(path.join(root, 'evaluation/controller.md')));
});
test('first failed oracle is retained with an unchanged production source', () => {
  const history = path.join(root, 'history/revision-1');
  validateManifest(JSON.parse(fs.readFileSync(path.join(history, 'manifest.json'))), history);
  assert.equal(read('history/revision-1/Sources/CheckoutSummary.swift'), read('Sources/CheckoutSummary.swift'));
  assert.match(read('history/revision-1/Tests/CheckoutSummaryTests.swift'), /XCTAssertEqual\(button.configuration, configuration\)/);
  assert.doesNotMatch(read('Tests/CheckoutSummaryTests.swift'), /XCTAssertEqual\(button.configuration, configuration\)/);
  const oracle = JSON.parse(read('evaluation/oracle-prompt.json'));
  assert.equal(oracle.status, 'development-draft');
});

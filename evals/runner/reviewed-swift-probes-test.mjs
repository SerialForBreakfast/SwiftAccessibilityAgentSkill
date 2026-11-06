import test from 'node:test';
import assert from 'node:assert/strict';
import {adapt, swiftBlocks} from './reviewed-swift-probes.mjs';

test('retains all Swift fences and separates prose from candidate code', () => {
  const answer = 'Explanation\n```swift\nlet a = 1\n```\nAlternative\n```Swift\nlet b = 2\n```\n';
  assert.deepEqual(swiftBlocks(answer), ['let a = 1\n', 'let b = 2\n']);
  assert.equal(swiftBlocks('No changes are needed.').length, 0);
});

test('reviewed selection moves imports only, retaining invalid APIs verbatim', () => {
  const answer = '```swift\nimport SwiftUI\nButton { action() } label: { Text("Go") }\n.accessibilityTraits(.button)\n```';
  const r = adapt(answer, {blocks: [0], prefix: 'struct Probe {', suffix: '}'});
  assert.ok(r.source.startsWith('import SwiftUI\n'));
  assert.ok(r.source.includes('Button { action() } label: { Text("Go") }'));
  assert.ok(r.source.includes('.accessibilityTraits(.button)'));
  assert.equal(r.blocks[0], 'import SwiftUI\nButton { action() } label: { Text("Go") }\n.accessibilityTraits(.button)\n');
});

test('missing or out-of-range reviewed block choices fail closed', () => {
  assert.throws(() => adapt('No code', {blocks: [0]}), /Invalid Swift fence/);
  assert.throws(() => adapt('```swift\nlet a = 1\n```', {blocks: []}), /Explicit block/);
});

test('CRLF and full declarations can be extracted without forcing expression wrappers', () => {
  const answer = '```swift\r\nstruct Example: View {\r\n}\r\n```\r\n';
  const r = adapt(answer, {blocks: [0], prefix: 'import SwiftUI'});
  assert.ok(r.source.includes('struct Example: View {\r\n}\r\n'));
});

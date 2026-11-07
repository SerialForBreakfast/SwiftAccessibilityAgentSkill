import test from 'node:test';
import assert from 'node:assert/strict';
import {adapt, swiftBlocks, targetConfiguration} from './reviewed-swift-probes.mjs';

test('cross-platform compiler probes preserve the explicit deployment target', () => {
  assert.deepEqual(targetConfiguration('macOS'), {sdk: 'macosx', target: 'arm64-apple-macosx26.0'});
  assert.deepEqual(targetConfiguration('tvOS'), {sdk: 'appletvsimulator', target: 'arm64-apple-tvos26.0-simulator'});
  assert.deepEqual(targetConfiguration('iOS'), targetConfiguration('iPadOS'));
  assert.throws(() => targetConfiguration('SwiftUI'), /Unsupported reviewed target/);
});

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

test('reviewed source range retains complete bytes when only Markdown fence is cut', () => {
  const answer = 'Example\n```swift\nstruct Example {}\n';
  const start = answer.indexOf('struct');
  const r = adapt(answer, {sourceRange: {start, end: answer.length}});
  assert.deepEqual(r.blocks, ['struct Example {}\n']);
  assert.equal(r.source, '\n\nstruct Example {}\n\n');
  assert.throws(() => adapt(answer, {sourceRange: {start, end: answer.length + 1}}), /Invalid explicit source range/);
  assert.throws(() => adapt(answer, {blocks: [0], sourceRange: {start, end: answer.length}}), /Invalid explicit source range/);
});

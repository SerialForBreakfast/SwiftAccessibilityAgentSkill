import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import {route} from './route.mjs';
import {route as parentRoute} from '../0.3.0-dev.5/route.mjs';
import {hash} from '../../../../../code-examples/tools/contracts.mjs';
const base = 'research/evaluation/failure-driven/candidates/0.3.0-dev.6/';
const manifest = JSON.parse(fs.readFileSync(base + 'candidate.json'));
for (const platform of ['iOS', 'macOS', 'tvOS']) for (const concern of ['overview', 'selection', 'ownership', 'wiring']) {
  test(platform + '/' + concern + ' narrow read trace and on-demand complete contracts', () => {
    const q = {platform, framework: 'SwiftUI', topic: 'media', concern};
    const g = route(q), e = route({...q, level: 'example'}), c = route({...q, level: 'contract'});
    assert.equal(g.status, 'selected'); assert.equal(g.paths.length, 2);
    assert.equal(e.paths.length, 3); assert.equal(c.paths.length, 7);
    assert.equal(g.paths.filter(p => p.includes('media-' + concern)).length, 1);
    assert.ok(g.deliveredBytes < e.deliveredBytes && e.deliveredBytes < c.deliveredBytes);
    assert.equal(c.tokens, null);
    for (const r of [g, e, c]) for (const t of r.trace) {
      assert.equal(hash(fs.readFileSync(t.path)), t.sha256);
      assert.doesNotMatch(t.path, /\.prompt\.md|\.rubric|controller\.json|\/history\/|\/native-evidence\/|review\.json/);
    }
    assert.ok(c.paths.some(p => p.endsWith('/Tests/DescriptionFixture.swift')));
    assert.ok(c.paths.some(p => p.endsWith('/Tests/ReviewRegressionTests.swift')));
  });
}
test('unrelated routes remain inherited, not silently requalified', () => {
  for (const q of [{platform: 'iOS', framework: 'UIKit', topic: 'actions'}, {platform: 'macOS', framework: 'AppKit', topic: 'text'}]) {
    const r = route(q), previous = parentRoute(q);
    assert.deepEqual(r, {...previous, inheritedFrom: '0.3.0-dev.5'});
  }
});
test('mixed ownership and unsupported targets never borrow the media extension', () => {
  assert.equal(route({platform: 'iOS', framework: 'mixed', topic: 'media'}).status, 'needs-owner');
  assert.equal(route({platform: 'iOS', framework: 'mixed', ownerFramework: 'SwiftUI', topic: 'media'}).framework, 'SwiftUI');
  for (const platform of ['watchOS', 'visionOS', 'unknown']) assert.equal(route({platform, framework: 'SwiftUI', topic: 'media'}).deliveredBytes, 0);
  assert.equal(route({platform: 'iOS', framework: 'SwiftUI', topic: 'media', concern: '../../secret'}).status, 'unsupported');
});
test('byte budgets and level validation fail closed', () => {
  const q = {platform: 'iOS', framework: 'SwiftUI', topic: 'media'};
  const r = route({...q, maxBytes: 1}); assert.equal(r.status, 'budget-exceeded');
  assert.deepEqual(r.trace, []); assert.deepEqual(r.documents, []); assert.equal(r.deliveredBytes, 0);
  for (const maxBytes of [0, -1, Infinity, NaN, '1000']) assert.throws(() => route({...q, maxBytes}));
  assert.throws(() => route({...q, level: 'all'}));
});
test('candidate evidence and inherited sealed package remain unchanged', () => {
  for (const pin of [...manifest.assets, ...manifest.evidencePins, manifest.parentPins]) assert.equal(hash(fs.readFileSync(pin.path)), pin.sha256, pin.path);
  for (const pin of JSON.parse(fs.readFileSync(manifest.parentPins.path)).files) assert.equal(hash(fs.readFileSync(pin.path)), pin.sha256, pin.path);
  assert.equal(manifest.evaluationModelCalls, 0); assert.equal(manifest.releaseEligible, false);
  assert.equal(manifest.baselineEligible, false); assert.equal(manifest.liveRunsAuthorized, false);
  assert.equal(manifest.sourceReview.turns, 2); assert.ok(!fs.existsSync(base + 'SKILL.md'));
});

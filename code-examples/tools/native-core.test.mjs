import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import {createHash} from 'node:crypto';
import {fileURLToPath} from 'node:url';
import {nativePlan, selectDestination, compileOutcome, unitOutcome, packageSource} from './native-core.mjs';
const root = fileURLToPath(new URL('../pilots/uikit-v1/', import.meta.url));
const manifest = () => JSON.parse(fs.readFileSync(root + 'manifest.json'));
test('embedded media fixture matches its synthetic provenance', () => {
  const base = new URL('../pilots/uikit-media-v1/', import.meta.url);
  const provenance = JSON.parse(fs.readFileSync(new URL('fixture-provenance.json', base)));
  const source = fs.readFileSync(new URL('Tests/MediaFixture.swift', base), 'utf8');
  const payload = source.match(/private static let payload = """\n([\s\S]*?)\n"""/);
  assert.ok(payload, 'Embedded fixture payload is explicit');
  const bytes = Buffer.from(payload[1].replace(/\s/g, ''), 'base64');
  assert.equal(bytes.length, provenance.bytes);
  assert.equal(createHash('sha256').update(bytes).digest('hex'), provenance.sha256);
  assert.equal(bytes.toString('ascii', 4, 8), 'ftyp');
  assert.equal(provenance.kind, 'synthetic-media');
  const m = JSON.parse(fs.readFileSync(new URL('manifest.json', base)));
  assert.ok(m.files.some(f => f.path === 'Tests/MediaFixture.swift'));
});
const result = status => ({status, signal: null, error: null});
const destination = {uuid: 'synthetic', version: '26.5', build: 'synthetic'};
function unit(failed = false) {
  return {totalTestCount: 1, skippedTests: 0, passedTests: failed ? 0 : 1, failedTests: failed ? 1 : 0,
    devicesAndConfigurations: [{device: {deviceId: destination.uuid, osVersion: destination.version, osBuildNumber: destination.build, platform: 'iOS Simulator'}}],
    testFailures: failed ? [{failureText: 'XCTAssertEqual failed', testIdentifierString: 'Tests/testExample()'}] : []};
}
const check = {testIds: ['Tests/testExample']};
const log = failed => `Test Case '-[AccessibilityExamplesTests.Tests testExample]' ${failed ? 'failed' : 'passed'} (0.01 seconds).`;

test('all eight pilot checks plan offline with pinned source files', () => {
  const m = manifest(); assert.equal(m.checks.length, 8);
  for (const c of m.checks) assert.equal(nativePlan(m, root, c.id).execution, false);
});
test('on-demand index resolves sources and checks without runtime integration', () => {
  const index = JSON.parse(fs.readFileSync(new URL('../index.json', import.meta.url)));
  assert.equal(index.integration, 'offline-only'); assert.equal(index.examples.length, 11);
  for (const entry of index.examples) {
    const m = JSON.parse(fs.readFileSync(new URL('../' + entry.manifest, import.meta.url)));
    assert.equal(entry.status, 'pilot-not-promoted');
    assert.ok(fs.existsSync(new URL('../' + entry.source, import.meta.url)));
    assert.ok(entry.checks.every(id => m.checks.some(c => c.id === id)));
  }
});
test('UIKit expansion maps every selected test to a source claim and real test method', () => {
  const base = new URL('../pilots/uikit-semantics-v1/', import.meta.url);
  const m = JSON.parse(fs.readFileSync(new URL('manifest.json', base)));
  const coverage = JSON.parse(fs.readFileSync(new URL('coverage.json', base)));
  const source = fs.readFileSync(new URL('Tests/UIKitSemanticsTests.swift', base), 'utf8');
  assert.equal(coverage.scope, 'unit-only');
  const tests = m.checks.find(c => c.id === 'semantics-unit').testIds;
  assert.equal(new Set(coverage.assertions.map(a => a.testId)).size, 23);
  assert.deepEqual(coverage.assertions.map(a => a.testId).sort(), [...tests].sort());
  for (const a of coverage.assertions) {
    assert.ok(m.claims.some(c => c.id === a.claimId));
    assert.ok(source.includes('func ' + a.testId.split('/')[1] + '('));
    assert.ok(a.guidelines.every(g => /^U-\d{3}$/.test(g)));
  }
  for (const c of m.checks) nativePlan(m, fileURLToPath(base), c.id);
});
test('dynamic UIKit coverage resolves all 15 tests and isolated mutations', () => {
  const base = new URL('../pilots/uikit-dynamic-v1/', import.meta.url);
  const m = JSON.parse(fs.readFileSync(new URL('manifest.json', base)));
  const coverage = JSON.parse(fs.readFileSync(new URL('coverage.json', base)));
  const source = fs.readFileSync(new URL('Tests/DynamicUIKitTests.swift', base), 'utf8');
  const tests = m.checks.find(c => c.id === 'dynamic-unit').testIds;
  assert.equal(new Set(coverage.assertions.map(a => a.testId)).size, 15);
  assert.deepEqual(coverage.assertions.map(a => a.testId).sort(), [...tests].sort());
  for (const a of coverage.assertions) {
    assert.ok(m.claims.some(c => c.id === a.claimId));
    assert.ok(source.includes('func ' + a.testId.split('/')[1] + '('));
  }
  assert.equal(m.checks.filter(c => c.expected === 'failure').length, 4);
  for (const c of m.checks) nativePlan(m, fileURLToPath(base), c.id);
});
test('every indexed coverage map resolves exact native tests and source claims', () => {
  const index = JSON.parse(fs.readFileSync(new URL('../index.json', import.meta.url)));
  const seen = new Set();
  for (const entry of index.examples) {
    if (seen.has(entry.manifest)) continue;
    seen.add(entry.manifest);
    const url = new URL('../' + entry.manifest, import.meta.url);
    const m = JSON.parse(fs.readFileSync(url)), coverageURL = new URL('coverage.json', url);
    assert.ok(fs.existsSync(coverageURL), 'Every indexed package requires a coverage map');
    const coverage = JSON.parse(fs.readFileSync(coverageURL));
    const ids = coverage.assertions.map(a => a.testId);
    const positives = m.checks.filter(c => c.lane === 'unit' && c.expected === 'success').flatMap(c => c.testIds);
    assert.equal(new Set(ids).size, ids.length);
    assert.deepEqual([...ids].sort(), [...positives].sort());
    const source = m.files.filter(f => f.path.startsWith('Tests/')).map(f => fs.readFileSync(new URL(f.path, url), 'utf8')).join('\n');
    for (const a of coverage.assertions) {
      assert.ok(m.claims.some(c => c.id === a.claimId));
      assert.ok(source.includes('func ' + a.testId.split('/')[1] + '('));
      assert.ok(a.guidelines.length > 0 && a.guidelines.every(g => /^U-\d{3}$/.test(g)));
    }
    for (const check of m.checks) {
      if (check.lane === 'unit') assert.ok(check.testIds.every(id => positives.includes(id)));
      nativePlan(m, fileURLToPath(new URL('.', url)), check.id);
    }
  }
  assert.equal(seen.size, 9);
});
test('reject unsupported platform and unpinned replacement', () => {
  const m = manifest(); m.platform = 'tvOS'; assert.throws(() => nativePlan(m, root, m.checks[0].id));
  const n = manifest(); n.checks[2].replacement.source = '../../other.swift';
  assert.throws(() => nativePlan(n, root, n.checks[2].id));
});
test('destination resolves installed runtime, never a version flag', () => {
  const devices = {devices: {'com.apple.CoreSimulator.SimRuntime.iOS-26-5': [{udid: 'test', isAvailable: true}]}};
  const runtimes = {runtimes: [{identifier: 'com.apple.CoreSimulator.SimRuntime.iOS-26-5', version: '26.5', buildversion: 'actual-build', isAvailable: true}]};
  assert.equal(selectDestination(devices, runtimes, 'test', 26).build, 'actual-build');
  assert.throws(() => selectDestination(devices, runtimes, 'test', 27));
  assert.throws(() => selectDestination(devices, runtimes, 'missing', 26));
  runtimes.runtimes[0].isAvailable = false;
  assert.throws(() => selectDestination(devices, runtimes, 'test', 26));
});
test('compiler parser requires actual diagnostic line and preserves warnings in log', () => {
  const c = {diagnostics: [{id: 'type-error', contains: "cannot assign value of type 'Int'"}]};
  assert.deepEqual(compileOutcome(result(1), "a.swift:4:10: error: cannot assign value of type 'Int' to type 'String?'", c).diagnosticIds, ['type-error']);
  assert.throws(() => compileOutcome(result(1), "// error: cannot assign value of type 'Int'", c));
  assert.deepEqual(compileOutcome(result(1), 'a.swift:4:10: error: unrelated syntax', c).diagnosticIds, ['unmapped-compiler-error']);
  assert.equal(compileOutcome(result(0), 'a.swift:4:10: warning: deprecated', c).build, 'passed');
  assert.throws(() => compileOutcome({...result(null), signal: 'SIGKILL'}, '', c));
});
for (const failed of [false, true]) test('unit parser handles ' + (failed ? 'assertion failure' : 'pass'), () => {
  assert.equal(unitOutcome(result(failed ? 65 : 0), log(failed), unit(failed), check, destination).failedTestIds.length, failed ? 1 : 0);
});
for (const [label, mutate] of [
  ['zero tests', s => s.totalTestCount = 0], ['skip', s => s.skippedTests = 1],
  ['wrong count', s => s.passedTests = 2], ['wrong runtime', s => s.devicesAndConfigurations[0].device.osVersion = '27.0'],
  ['wrong platform', s => s.devicesAndConfigurations[0].device.platform = 'tvOS Simulator'],
  ['wrong destination', s => s.devicesAndConfigurations[0].device.deviceId = 'other'],
]) test('unit parser rejects ' + label, () => {
  const s = unit(); mutate(s); assert.throws(() => unitOutcome(result(0), log(false), s, check, destination));
});
test('unit parser rejects crashes, duplicate tests and unexpected test failures', () => {
  const s = unit(true); s.testFailures[0].failureText = 'Test crashed';
  assert.throws(() => unitOutcome(result(65), log(true), s, check, destination));
  s.testFailures[0].failureText = 'XCTAssertFalse failed'; s.testFailures[0].testIdentifierString = 'Other/test()';
  assert.throws(() => unitOutcome(result(65), log(true), s, check, destination));
  assert.throws(() => unitOutcome(result(0), log(false) + '\n' + log(false), unit(), check, destination));
});
test('generated package contains only library and unit target', () => {
  const source = packageSource('26.0');
  assert.ok(source.includes('.testTarget(')); assert.ok(!source.includes('UITest'));
  assert.ok(!source.includes('.package(')); assert.throws(() => packageSource('26.0"; injected'));
});

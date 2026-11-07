import {artifact, validateManifest} from './contracts.mjs';

export function nativePlan(manifest, root, checkId) {
  validateManifest(manifest, root);
  if (manifest.platform !== 'iOS') throw Error('Initial native adapter supports iOS only');
  const check = manifest.checks.find(c => c.id === checkId);
  if (!check) throw Error('Unknown native check');
  const inputs = manifest.files.filter(f => /^(Sources|Tests)\/[A-Za-z0-9_]+\.swift$/.test(f.path));
  if (!inputs.some(f => f.path.startsWith('Sources/')) || !inputs.some(f => f.path.startsWith('Tests/'))) throw Error('Missing package inputs');
  for (const input of inputs) artifact(root, input);
  if (check.replacement) {
    if (!inputs.some(f => f.path === check.replacement.target && f.path.startsWith('Sources/')) ||
        !manifest.files.some(f => f.path === check.replacement.source && f.path.startsWith('NegativeFixtures/'))) throw Error('Invalid mutation mapping');
  }
  if (check.compileSources && (!Array.isArray(check.compileSources) || !check.compileSources.length ||
      check.compileSources.some(p => !manifest.files.some(f => f.path === p && p.endsWith('.swift'))))) throw Error('Invalid compile inputs');
  if ((check.diagnostics ?? []).some(d => !check.failureIds.includes(d.id) || typeof d.contains !== 'string' || !d.contains)) throw Error('Invalid diagnostic mapping');
  if (check.lane === 'unit' && check.testIds.some(t => !/^[A-Za-z0-9_]+\/[A-Za-z0-9_]+$/.test(t))) throw Error('Unsupported XCTest selection');
  return {execution: false, check, inputs, deploymentTarget: manifest.deploymentTarget, runtimeMajor: manifest.runtimeMajor};
}

export function selectDestination(devices, runtimes, uuid, major) {
  const runtime = runtimes.runtimes.find(r => r.identifier.includes('.iOS-') &&
    Number(r.version.split('.')[0]) === major && r.isAvailable &&
    (devices.devices[r.identifier] ?? []).some(d => d.udid === uuid && d.isAvailable));
  if (!runtime) throw Error('Destination must be an available installed iOS runtime of the selected major');
  return {version: runtime.version, build: runtime.buildversion};
}

export function compileOutcome(result, log, check) {
  if (result.error || result.signal || ![0, 1].includes(result.status)) throw Error('Compiler infrastructure error');
  // Match complete diagnostic lines, never a substring echoed from source code.
  const errors = log.split('\n').filter(l => /^(?:.*:\d+:\d+: |<unknown>:\d+: )error: /.test(l));
  if (result.status === 0 && errors.length) throw Error('Compiler exit contradicts diagnostics');
  if (result.status !== 0 && !errors.length) throw Error('Unclassified compiler failure');
  const diagnosticIds = [...new Set(errors.map(line => {
    const message = line.slice(line.indexOf('error: ') + 7);
    const matches = (check.diagnostics ?? []).filter(d => message.includes(d.contains));
    return matches.length === 1 ? matches[0].id : 'unmapped-compiler-error';
  }))];
  return {exitCode: result.status, signal: null, infrastructureError: null,
    build: result.status === 0 ? 'passed' : 'failed', skippedTests: 0,
    executedTestIds: [], failedTestIds: [], diagnosticIds};
}

export function unitOutcome(result, log, summary, check, destination) {
  if (result.error || result.signal || ![0, 65].includes(result.status)) throw Error('Unit infrastructure error');
  const matches = [...log.matchAll(/Test Case '-\[AccessibilityExamplesTests\.(\w+) (\w+)\]' (passed|failed)/g)];
  const executedTestIds = matches.map(m => m[1] + '/' + m[2]);
  const failedTestIds = matches.filter(m => m[3] === 'failed').map(m => m[1] + '/' + m[2]);
  if (JSON.stringify([...executedTestIds].sort()) !== JSON.stringify([...check.testIds].sort()) ||
      summary?.totalTestCount !== executedTestIds.length || summary.skippedTests !== 0 ||
      summary.failedTests !== failedTestIds.length || summary.passedTests !== executedTestIds.length - failedTestIds.length) throw Error('Missing, skipped or inconsistent unit evidence');
  const configs = summary.devicesAndConfigurations;
  if (configs?.length !== 1 || configs[0].device.deviceId !== destination.uuid ||
      configs[0].device.osVersion !== destination.version || configs[0].device.osBuildNumber !== destination.build ||
      configs[0].device.platform !== 'iOS Simulator') throw Error('Result destination differs from preflight');
  if ((result.status === 0) !== (failedTestIds.length === 0)) throw Error('Unit exit contradicts test counts');
  if (failedTestIds.length) {
    const failures = summary.testFailures;
    if (!failures?.length || failures.some(f => !f.failureText?.startsWith('XCTAssert') ||
        !failedTestIds.includes(f.testIdentifierString?.replace(/\(\)$/, '')))) throw Error('Non-assertion or unrelated test failure');
  }
  return {exitCode: result.status, signal: null, infrastructureError: null, build: 'passed', skippedTests: 0,
    executedTestIds, failedTestIds, diagnosticIds: []};
}

export function packageSource(target) {
  if (!/^\d+\.\d+(\.\d+)?$/.test(target)) throw Error('Invalid deployment target');
  return `// swift-tools-version: 6.0\nimport PackageDescription\nlet package = Package(name: "AccessibilityExamples", platforms: [.iOS("${target}")], products: [.library(name: "AccessibilityExamples", targets: ["AccessibilityExamples"])], targets: [.target(name: "AccessibilityExamples"), .testTarget(name: "AccessibilityExamplesTests", dependencies: ["AccessibilityExamples"])])\n`;
}

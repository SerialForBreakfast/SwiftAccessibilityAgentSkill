import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {hash, validateManifest} from '../../../../code-examples/tools/contracts.mjs';
import {selectedPackages} from '../../../../code-examples/tools/campaign-core.mjs';
import {bindings, groups, gaps, directlyAsserted} from './review-spec.mjs';

const here = path.dirname(fileURLToPath(import.meta.url));
const root = path.resolve(here, '../../../..');
const relative = p => path.relative(root, p);
const read = p => fs.readFileSync(path.join(root, p));
const inventoryFile = 'code-examples/audits/requirements-v1/inventory.json';
const inventory = JSON.parse(read(inventoryFile));
const packages = [...selectedPackages(root), relative(path.join(here, 'gap-contracts'))];
const campaignFile = relative(path.join(here, 'execution.json'));
const campaign = fs.existsSync(path.join(root, campaignFile)) ? JSON.parse(read(campaignFile)) : null;
const catalog = [], packageMap = new Map();
for (const pkg of packages) {
  const bytes = read(pkg + '/manifest.json'), m = validateManifest(JSON.parse(bytes), path.join(root, pkg));
  const manifestHash = hash(bytes), evidence = [];
  const recordFiles = fs.existsSync(path.join(root, pkg, 'validation')) ?
    fs.readdirSync(path.join(root, pkg, 'validation')).filter(f => f.endsWith('.json')).map(f => pkg + '/validation/' + f) :
    fs.existsSync(path.join(root, pkg, 'validation.json')) ? [pkg + '/validation.json'] : [];
  for (const file of recordFiles) {
    const doc = JSON.parse(read(file));
    for (const row of doc.rows ?? []) if ((row.manifestHash ?? doc.manifestHash) === manifestHash && row.status === 'passed' && row.observed === 'success')
      evidence.push({file, fileHash: hash(read(file)), originalRecordHash: row.originalRecordHash,
        environment: row.environment, executedTestIds: row.execution?.executedTestIds ?? []});
  }
  if (campaign) for (const row of campaign.rows.filter(r => r.package === pkg && r.manifestHash === manifestHash && r.status === 'passed' && r.observed === 'success'))
    evidence.push({file: campaignFile, fileHash: hash(read(campaignFile)), originalRecordHash: row.originalRecordHash,
      environment: row.environment, executedTestIds: row.execution?.executedTestIds ?? []});
  packageMap.set(path.basename(pkg), {path: pkg, manifestHash, claims: m.claims, sources: m.files.filter(f => f.path.startsWith('Sources/'))});
  const selected = new Set(m.checks.filter(c => c.lane === 'unit' && c.expected === 'success').flatMap(c => c.testIds));
  for (const f of m.files.filter(f => f.path.startsWith('Tests/') && f.path.endsWith('.swift'))) {
    const text = read(pkg + '/' + f.path).toString();
    const className = text.match(/class\s+(\w+)\s*:\s*XCTestCase/)?.[1];
    if (!className) continue;
    for (const match of text.matchAll(/func\s+(test\w+)\s*\([^)]*\)[^{]*\{/g)) {
      const id = className + '/' + match[1];
      if (!selected.has(id)) continue;
      let end = match.index + match[0].length, depth = 1;
      for (; end < text.length && depth; end++) { if (text[end] === '{') depth++; if (text[end] === '}') depth--; }
      const body = text.slice(match.index, end);
      catalog.push({key: path.basename(pkg) + ':' + id, package: pkg, manifestHash, testId: id,
        testFile: pkg + '/' + f.path, sourceHash: f.sha256, line: text.slice(0, match.index).split('\n').length,
        bodyHash: hash(body), assertionCount: (body.match(/XCTAssert|XCTFail|XCTUnwrap/g) ?? []).length,
        nativeEvidence: evidence.filter(e => e.executedTestIds.includes(id))});
    }
  }
}
function resolve(name) {
  const b = bindings[name];
  if (!b) throw Error('Unknown binding: ' + name);
  return {name, scope: b.scope, tests: b.methods.map(method => {
    const found = catalog.filter(t => path.basename(t.package) === b.package && t.testId.endsWith('/' + method));
    if (found.length !== 1) throw Error('Unresolved/ambiguous reviewed method: ' + method);
    return found[0].key;
  }), sources: packageMap.get(b.package).claims};
}
const resolved = Object.fromEntries(Object.keys(bindings).map(k => [k, resolve(k)]));
const lookup = new Map(catalog.map(t => [t.key, t]));
const clauses = [], rules = [];
for (const d of inventory.documents) {
  if (hash(read(d.path)) !== d.sha256) throw Error('Guideline changed: ' + d.path);
  const sourceURLs = [...new Set(read(d.path).toString().match(/https:\/\/developer\.apple\.com\/[^\s)]+/g) ?? [])];
  const mapping = new Map();
  for (const [lines, names] of groups[d.guideline]) for (const line of lines.split(',')) mapping.set(d.guideline + '-L' + line, names.split(','));
  for (const c of d.clauses) {
    const names = [...(mapping.get(c.id) ?? [])];
    if (['U-014-L23', 'U-010-L25'].includes(c.id)) names.push('checkout');
    if (c.id === 'U-004-L24') names.push('quantityGap');
    const gapBinding = {'GAP-SUMMARY':'summaryGap', 'GAP-QUANTITY':'quantityGap', 'GAP-MOTION-FEEDBACK':'motionGap'}[gaps[c.id]?.id];
    if (gapBinding) names.push(gapBinding);
    let status, rationale;
    if (c.subsection === 'SwiftUI Interop Notes') {
      status = 'swiftui-deferred'; rationale = 'Cross-framework composition explicitly deferred. UIKit metadata is not evidence of hosted SwiftUI behavior.';
    } else if (c.subsection === 'VoiceOver Walkthrough') {
      status = 'documentation-supported/outside-unit-scope'; rationale = 'Actual speech, assistive input and navigation are outside compile/unit evidence. This introduces no manual or UI gate.';
    } else if (gaps[c.id]) {
      status = 'missing-testable-coverage'; rationale = gaps[c.id].reason;
      if (resolved[gapBinding].tests.every(k => lookup.get(k).nativeEvidence.length)) {
        status = 'partially-covered';
        rationale += ' Campaign closes the identified configuration/callback gap: ' + resolved[gapBinding].scope;
      }
    } else if (!names.length) {
      status = 'documentation-supported/outside-unit-scope'; rationale = 'Rendered geometry, reachability or perceptual clarity is not established by these configuration assertions. Apple guidance remains applicable.';
    } else {
      status = directlyAsserted.has(c.id) ? 'covered' : 'partially-covered';
      rationale = names.map(n => resolved[n].scope).join(' ');
      if (c.subsection === 'Optional XCUITest Hook') rationale += ' Only the metadata/state contract is translated; no XCUITest is added.';
      if (names.flatMap(n => resolved[n].tests).some(k => !lookup.get(k).nativeEvidence.length)) {
        status = 'partially-covered'; rationale += ' At least one selected assertion lacks matching current-manifest public native evidence; retain this gap until the campaign report binds it.';
      }
    }
    clauses.push({...c, status, rationale, bindingIds: names, gapId: gaps[c.id]?.id ?? null,
      gapDisposition: gapBinding ? (status === 'missing-testable-coverage' ? 'implemented-awaiting-validation' : 'implemented-validated-unit-scope') : null,
      sourceURLs, sourceScope: 'Guideline citations plus narrower source claims in bindings; citation presence is not fresh verification.',
      apiMatrix: 'availability-matrix.json',
      guidelinePath: d.path, guidelineHash: d.sha256, reviewer: 'local-author-source-and-assertion-review', independentReview: 'pending'});
  }
  rules.push({id: d.guideline + '-RULE', text: d.rule, guidelinePath: d.path, guidelineHash: d.sha256,
    sourceURLs, apiMatrix: 'availability-matrix.json',
    status: 'partially-covered', bindingIds: [...new Set(clauses.filter(c => c.guidelinePath === d.path).flatMap(c => c.bindingIds))],
    rationale: 'The rule is broader than its directly asserted example contracts. Metadata/callback evidence supports the listed portions; universal meaning, speech, navigation, visual quality and usability are not inferred.',
    independentReview: 'pending'});
}
const counts = Object.fromEntries([...new Set(clauses.map(c => c.status))].map(s => [s, clauses.filter(c => c.status === s).length]));
fs.writeFileSync(path.join(here, 'assertion-catalog.json'), JSON.stringify({schema: 1, methods: catalog}, null, 2) + '\n');
fs.writeFileSync(path.join(here, 'clause-ledger.json'), JSON.stringify({schema: 1, inventoryFile, inventoryHash: hash(read(inventoryFile)),
  status: 'author-reviewed-not-independent-acceptance', counts, bindings: resolved, rules, clauses}, null, 2) + '\n');
console.log(JSON.stringify({clauses: clauses.length, rules: rules.length, methods: catalog.length, counts,
  methodsWithoutHistoricalEvidence: catalog.filter(t => !t.nativeEvidence.length).length}));

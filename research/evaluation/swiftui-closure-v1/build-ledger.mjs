import fs from 'node:fs';
import {hash} from '../../../code-examples/tools/contracts.mjs';

const base = 'research/evaluation/swiftui-closure-v1';
const originalPath = 'research/evaluation/swiftui-campaign-v1/clause-ledger.json';
const forwardingPath = 'research/evaluation/swiftui-forwarding-v1/coverage-overlay.json';
const original = JSON.parse(fs.readFileSync(originalPath));
const forwarding = JSON.parse(fs.readFileSync(forwardingPath));
const forwarded = new Map(forwarding.rows.map(row => [row.id, row]));
const remaining = {
  'G-002-L31': 'Native hints can be cleared and replaced in existing forwarding units; whether a hint duplicates system speech is documentation-supported, outside unit scope.',
  'G-004-L31': 'Direct trait configuration is asserted in forwarding units. Generated traits across hosting containers are outside unit scope.',
  'G-005-L30': 'Explicit native children/order is tested. SwiftUI-generated flattening and discoverability are outside unit scope.',
  'G-006-L30': 'Actual spoken traversal through UIHostingController navigation stacks is outside unit scope; compile checks cannot settle it.',
  'G-009-L34': 'Native ownership and row action dispatch are tested. Generated mixed-stack containment and rotor destinations are outside unit scope.',
  'G-011-L31': 'Existing preference units assert non-color application cues. Rendered mixed-framework colors and contrast are outside unit scope.',
  'G-012-L30': 'Existing forwarding preference units assert final-state and animation-request policy. System preference propagation and rendered animation are outside unit scope.',
  'G-012-L31': 'Shared transition policy is already tested; consistency of rendered UIKit/SwiftUI animations is outside unit scope.',
  'G-013-L30': 'Existing lifecycle units assert request ownership and fallback target only. Delivered cross-framework focus is outside unit scope.',
  'G-014-L30': 'Native child/action configuration and SwiftUI List composition already have evidence. Generated table/collection cell semantics are outside unit scope.',
  'G-014-L31': 'Forwarding units assert same-instance name/value reset and callback invalidation. Actual SwiftUI-generated cell reuse is not directly controlled by these unit tests.',
  'G-015-L31': 'Existing native control configuration is separate from AVKit-generated accessible controls, which are documentation-supported outside unit scope.',
  'G-015-L32': 'New selection store owns item-bound media choices, native selection and stale completions. Supplemental live stream observation remains an explicitly separate unresolved implementation contract.',
  'G-015-L33': 'New composition keeps VideoPlayer and supplementary Picker as siblings. Source compilation is evidence of composition, not rendered overlap or duplicate generated accessibility controls.',
  'G-015-P79': 'OS27 generation/style/device/language behavior remains deferred from this OS26-targeted companion batch. Authored track selection is independently tested; system generation is not inferred.'
};
const notes = {
  selection: 'Real item/group selection, forced-only filtering, unrelated-group preservation and opaque snapshot IDs.',
  ownership: 'Generation and current-item checks, duplicate/late results and task cancellation are application policy.',
  wiring: 'Binding read/write, observation invalidation and same-player identity; the SwiftUI composition is compile-checked.'
};
const supplemental = {
  'G-003-L26': ['selection', 'wiring'], 'G-003-L52': ['selection', 'wiring'],
  'G-015-L25': ['selection'], 'G-015-L26': ['selection', 'ownership'],
  'G-015-L32': ['selection', 'ownership', 'wiring'], 'G-015-L33': ['wiring'],
  'G-015-L42': ['selection'], 'G-015-L52': ['selection']
};
const cases = JSON.parse(fs.readFileSync(base + '/prompt-records.json')).cases;
const evidenceCatalog = {};
function intern(value) {
  const key = hash(JSON.stringify(value));
  evidenceCatalog[key] = value;
  return key;
}
const rows = original.clauses.map(row => {
  const subset = forwarded.get(row.id);
  let disposition = row.disposition, rationale = row.rationale;
  if (subset) {
    disposition = 'partially-covered-native-subset';
    rationale = subset.scope + ' Broad hosting semantics remain outside unit scope; this is not whole-clause closure.';
  } else if (row.disposition === 'unresolved') {
    if (!remaining[row.id]) throw Error('Missing explicit disposition: ' + row.id);
    disposition = row.id === 'G-015-L32' ? 'partially-covered-testable-remainder' :
      row.id === 'G-015-P79' ? 'deferred-version-specific' : 'documentation-supported-outside-unit-scope';
    rationale = remaining[row.id];
  }
  const newEvidence = (supplemental[row.id] ?? []).flatMap(family => cases.filter(c => c.family === family).map(c => ({
    caseId: c.id, manifest: c.manifest, testIds: c.testIds, scope: notes[family],
    status: 'see-results-index-not-inferred-from-authorship'
  })));
  return {...row, originalDisposition: row.disposition, disposition, rationale,
    existingEvidence: row.bindingIds.map(id => {
      const binding = original.bindings.find(b => b.id === id);
      if (!binding) throw Error('Missing prior binding ' + id);
      return intern({bindingId: id, scope: 'Original author mapping; only named assertions, not whole prose.',
        manifest: binding.manifest, manifestHash: binding.manifestHash, execution: binding.execution});
    }), forwardingEvidence: (subset?.bindings ?? []).map(intern), newEvidence: newEvidence.map(intern),
    independentReview: 'pending', fullClauseProvenByUnits: false};
});
const result = {
  schema: 1, baseCommit: '8e51ee9', status: 'author-reconciled-independent-review-pending',
  originals: [originalPath, forwardingPath].map(path => ({path, sha256: hash(fs.readFileSync(path))})),
  rules: original.rules, clauses: rows, evidenceCatalog,
  counts: Object.fromEntries([...new Set(rows.map(r => r.disposition))].map(k => [k, rows.filter(r => r.disposition === k).length])),
  implementationQueue: [{id: 'live-stream-observation', clause: 'G-015-L32', status: 'unresolved',
    reason: 'A live-stream observer with teardown and item rebinding is not established by item media-selection units; retained as a named testable remainder, not relabeled outside scope.'}],
  nonGoals: ['UI tests', 'mandatory manual verification', 'system speech', 'delivered focus', 'generated semantics', 'OS27 promotion'],
  independentAcceptance: false
};
fs.writeFileSync(base + '/coverage-ledger.json', JSON.stringify(result, null, 2) + '\n');
console.log(JSON.stringify({clauses: rows.length, rules: result.rules.length, counts: result.counts}));

// Materialize private, hash-verified answers for the existing native adapter.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {fileURLToPath} from 'node:url';

const [input, output, ...extra] = process.argv.slice(2);
if (!input || !output || extra.length || !path.isAbsolute(input) || !path.isAbsolute(output)) {
  throw Error('Usage: node build-unit-packet.mjs ABS_FIRST_REVIEW ABS_NEW_PRIVATE_OUTPUT');
}
const hash = b => crypto.createHash('sha256').update(b).digest('hex');
const here = path.dirname(fileURLToPath(import.meta.url));
const results = JSON.parse(fs.readFileSync(path.join(here, 'results.json')));
const ids = ['R12', 'R13', 'R14', 'R16'];
// Verify every input before creating the destination. Never overwrite first attempts.
const sources = ids.map(id => {
  const bytes = fs.readFileSync(path.join(input, 'compile', id, 'Subject.swift'));
  const row = results.cases.find(c => c.review_id === id);
  if (row.exit_code !== 0 || hash(bytes) !== row.source_sha256) throw Error('Unexpected source: ' + id);
  const source = bytes.toString();
  if (source.split('final class CheckoutReviewHost:').length !== 2) throw Error('Ambiguous host');
  return {id, original: row.source_sha256,
    source: source.replace('final class CheckoutReviewHost:', `final class CheckoutReviewHost${id}:`)};
});
fs.mkdirSync(output, {mode: 0o700});
fs.mkdirSync(path.join(output, 'Sources'));
fs.mkdirSync(path.join(output, 'Tests'));
const files = [];
function save(name, text) {
  fs.writeFileSync(path.join(output, name), text, {flag: 'wx', mode: 0o600});
  files.push({path: name, sha256: hash(text)});
}
for (const item of sources) save(`Sources/Subject${item.id}.swift`, item.source);
const tests = ids.map(id => `
    func test${id}TextConfiguration() {
        let host = CheckoutReviewHost${id}()
        let total = "USD 123,456,789.00"
        host.configure(formattedTotal: total)
        XCTAssertEqual(host.totalLabel.text, total)
        XCTAssertEqual(host.totalLabel.numberOfLines, 0)
        XCTAssertTrue(host.totalLabel.adjustsFontForContentSizeCategory)
        XCTAssertNotNil(host.totalLabel.font.fontDescriptor.object(forKey: .textStyle))
    }

    func test${id}PreservesButtonTypography() throws {
        let host = CheckoutReviewHost${id}()
        let title = try XCTUnwrap(host.payButton.titleLabel)
        title.font = UIFont.systemFont(ofSize: 19, weight: .regular)
        title.adjustsFontForContentSizeCategory = false
        host.payButton.setTitle("Pay now", for: .normal)
        let before = try XCTUnwrap(title.font).fontDescriptor
        host.configure(formattedTotal: "USD 123,456,789.00")
        XCTAssertEqual(host.payButton.title(for: .normal), "Pay now")
        XCTAssertTrue(title.font.fontDescriptor.isEqual(before), "Existing button font descriptor changed")
        XCTAssertFalse(title.adjustsFontForContentSizeCategory, "Existing button scaling configuration changed")
    }
`).join('');
save('Tests/CheckoutAnswerTests.swift', `import XCTest
import UIKit
@testable import AccessibilityExamples

@MainActor
final class CheckoutAnswerTests: XCTestCase {
${tests}}
`);
const testIds = ids.flatMap(id => ['TextConfiguration', 'PreservesButtonTypography'].map(s => `CheckoutAnswerTests/test${id}${s}`));
const manifest = {schema: 1, id: 'checkout-answer-review', revision: '1', platform: 'iOS', deploymentTarget: '26.0', runtimeMajor: 26,
  limitations: 'Eight configuration-only tests; no layout, callback, input, speech or live-trait propagation assertions. Predicted R16 failure is an original answer defect, not a mutant.',
  claims: [{id: 'configuration', url: 'https://developer.apple.com/videos/play/wwdc2024/10074/', section: 'Scaled text; frozen GP26-03 preserve-button requirement',
    statement: 'Check explicit multiline/scaling text configuration and preservation of a synthetic preconfigured button font.', reviewedOn: '2026-11-06', availability: 'UIKit configuration properties, deployment iOS26.0.'}],
  files, checks: [{id: 'checkout-unit-first', lane: 'unit', expected: 'failure', claimIds: ['configuration'], testIds,
    failureIds: ['CheckoutAnswerTests/testR16PreservesButtonTypography']}]};
fs.writeFileSync(path.join(output, 'manifest.json'), JSON.stringify(manifest, null, 2) + '\n', {flag: 'wx', mode: 0o600});
fs.writeFileSync(path.join(output, 'adaptation.json'), JSON.stringify({
  changes: 'Only scaffold class names receive neutral-ID suffixes; original answer fence bodies unchanged. Tests set synthetic initial state externally. No action wiring, stack accessors, hierarchy attachment or lifecycle calls added.',
  sources: sources.map(({id, original, source}) => ({id, originalSourceHash: original, unitSourceHash: hash(source)})),
  expectedFailureMeaning: 'Prediction from source review, not a passing subject or deliberate mutation. Preserve actual first unit outcome even if prediction is wrong.'
}, null, 2) + '\n', {flag: 'wx', mode: 0o600});
console.log(JSON.stringify({output, answers: ids, testCount: testIds.length}));

import XCTest
import UIKit
@testable import AccessibilityExamples

@MainActor
final class EditedRotorUIKitTests: XCTestCase {
    private func search(_ reader: EditedMatchReader, current: UIAccessibilityCustomRotorItemResult? = nil,
                        direction: UIAccessibilityCustomRotor.Direction = .next,
                        rotor: UIAccessibilityCustomRotor? = nil) -> UIAccessibilityCustomRotorItemResult? {
        let predicate = UIAccessibilityCustomRotorSearchPredicate()
        if let current { predicate.currentItem = current }
        predicate.searchDirection = direction
        return (rotor ?? reader.textView.accessibilityCustomRotors?.first)?.itemSearchBlock(predicate)
    }

    private func location(_ item: UIAccessibilityCustomRotorItemResult?, in reader: EditedMatchReader) -> Int? {
        guard let range = item?.targetRange else { return nil }
        return reader.textView.offset(from: reader.textView.beginningOfDocument, to: range.start)
    }

    func testInitialDirectionAndBothBoundaries() throws {
        let reader = EditedMatchReader()
        reader.replace(text: "cat dog cat", query: "cat")
        let first = try XCTUnwrap(search(reader)), last = try XCTUnwrap(search(reader, direction: .previous))
        XCTAssertEqual(location(first, in: reader), 0)
        XCTAssertEqual(location(last, in: reader), 8)
        XCTAssertNil(search(reader, current: first, direction: .previous))
        XCTAssertNil(search(reader, current: last))
    }

    func testForwardAndBackwardUseFullCurrentRange() throws {
        let reader = EditedMatchReader()
        reader.replace(text: "cat dog cat", query: "cat")
        let first = try XCTUnwrap(search(reader)), second = try XCTUnwrap(search(reader, current: first))
        XCTAssertEqual(location(second, in: reader), 8)
        XCTAssertEqual(location(search(reader, current: second, direction: .previous), in: reader), 0)
        let end = try XCTUnwrap(reader.textView.position(from: reader.textView.beginningOfDocument, offset: 1))
        let partial = try XCTUnwrap(reader.textView.textRange(from: reader.textView.beginningOfDocument, to: end))
        let invalid = UIAccessibilityCustomRotorItemResult(targetElement: reader.textView, targetRange: partial)
        XCTAssertEqual(location(search(reader, current: invalid), in: reader), 0)
    }

    func testUnicodePrefixProducesCorrectNativeRange() {
        let reader = EditedMatchReader()
        reader.replace(text: "\u{1F600} e\u{301} target", query: "target")
        let item = search(reader)
        XCTAssertNotNil(item)
        XCTAssertEqual(location(item, in: reader), 6)
        if let range = item?.targetRange { XCTAssertEqual(reader.textView.text(in: range), "target") }
    }

    func testPartialGraphemeMatchesAreExcluded() {
        XCTAssertEqual(LiteralMatches.ranges(in: "e\u{301} e", query: "e", allowOverlaps: true),
                       [NSRange(location: 3, length: 1)])
        XCTAssertTrue(LiteralMatches.ranges(in: "\u{1F469}\u{200D}\u{1F4BB}", query: "\u{1F469}", allowOverlaps: true).isEmpty)
        XCTAssertEqual(LiteralMatches.ranges(in: "e\u{301}", query: "e\u{301}", allowOverlaps: false),
                       [NSRange(location: 0, length: 2)])
    }

    func testOverlapPolicyIsExplicit() {
        XCTAssertEqual(LiteralMatches.ranges(in: "banana", query: "ana", allowOverlaps: false),
                       [NSRange(location: 1, length: 3)])
        XCTAssertEqual(LiteralMatches.ranges(in: "banana", query: "ana", allowOverlaps: true),
                       [NSRange(location: 1, length: 3), NSRange(location: 3, length: 3)])
    }

    func testNewRevisionRestartsRetainedResult() throws {
        let reader = EditedMatchReader()
        reader.replace(text: "cat dog cat", query: "cat")
        let last = try XCTUnwrap(search(reader, direction: .previous))
        reader.replace(text: "cat dog cat", query: "cat")
        XCTAssertEqual(location(search(reader, current: last), in: reader), 0)
    }

    func testRetainedOldRotorIsInvalidAfterQueryChange() throws {
        let reader = EditedMatchReader()
        reader.replace(text: "cat dog cat", query: "cat")
        let old = try XCTUnwrap(reader.textView.accessibilityCustomRotors?.first)
        reader.replace(text: "cat dog cat", query: "dog")
        XCTAssertNil(search(reader, rotor: old))
        XCTAssertEqual(location(search(reader), in: reader), 4)
    }

    func testInsertionAndDeletionRebuildRanges() throws {
        let reader = EditedMatchReader()
        reader.replace(text: "cat", query: "cat")
        let old = try XCTUnwrap(search(reader))
        reader.replace(text: "\u{1F600} cat", query: "cat")
        XCTAssertEqual(location(search(reader, current: old), in: reader), 3)
        reader.replace(text: "dog", query: "cat")
        XCTAssertTrue(reader.matches.isEmpty)
        XCTAssertNil(search(reader, current: old))
        XCTAssertEqual(reader.textView.text, "dog")
    }

    func testEmptyQueryUpdatesOrdinaryDocumentWithoutRotor() {
        let reader = EditedMatchReader()
        reader.replace(text: "cat", query: "cat")
        reader.replace(text: "updated document", query: "")
        XCTAssertEqual(reader.textView.text, "updated document")
        XCTAssertTrue(reader.matches.isEmpty)
        XCTAssertTrue(reader.textView.accessibilityCustomRotors?.isEmpty == true)
        XCTAssertTrue(reader.textView.isAccessibilityElement)
        XCTAssertTrue(reader.textView.isSelectable)
        XCTAssertFalse(reader.textView.isEditable)
        XCTAssertFalse(reader.isAccessibilityElement)
    }

    func testUnannouncedTextChangeRejectsCachedSearch() {
        let reader = EditedMatchReader()
        reader.replace(text: "cat", query: "cat")
        reader.textView.text = "dog"
        XCTAssertNil(search(reader))
        XCTAssertEqual(reader.textView.text, "dog")
        reader.replace(text: "dog", query: "dog")
        XCTAssertEqual(location(search(reader), in: reader), 0)
    }

    func testForeignTextInputPositionsRestartSafely() throws {
        let reader = EditedMatchReader(), other = UITextView()
        reader.replace(text: "cat dog cat", query: "cat")
        _ = search(reader)
        other.text = "foreign"
        let range = try XCTUnwrap(other.textRange(from: other.beginningOfDocument, to: other.endOfDocument))
        let item = UIAccessibilityCustomRotorItemResult(targetElement: other, targetRange: range)
        XCTAssertEqual(location(search(reader, current: item), in: reader), 0)
    }

    func testNativeRangeCanBeUsedForOrdinaryTextSelection() throws {
        let reader = EditedMatchReader()
        reader.replace(text: "Read target normally", query: "target")
        let item = try XCTUnwrap(search(reader)), range = try XCTUnwrap(item.targetRange)
        XCTAssertTrue(item.targetElement === reader.textView)
        reader.textView.selectedTextRange = range
        XCTAssertEqual(reader.textView.text(in: try XCTUnwrap(reader.textView.selectedTextRange)), "target")
        XCTAssertEqual(reader.textView.text, "Read target normally")
    }
}

import XCTest
import AppKit
@testable import AccessibilityExamples

@MainActor
final class DesktopTextTests: XCTestCase {
    private func search(_ r: DesktopText, current: NSAccessibilityCustomRotor.ItemResult? = nil, direction: NSAccessibilityCustomRotor.SearchDirection = .next, filter: String = "", rotor: NSAccessibilityCustomRotor? = nil) -> NSAccessibilityCustomRotor.ItemResult? {
        let p = NSAccessibilityCustomRotor.SearchParameters(); p.currentItem = current; p.searchDirection = direction; p.filterString = filter
        guard let rotor = rotor ?? r.textView.accessibilityCustomRotors().first else { return nil }
        return rotor.itemSearchDelegate?.rotor(rotor, resultFor: p)
    }
    func testForwardBackwardAndBothBoundaries() throws {
        let r = DesktopText(); r.replace(text: "cat dog cat", query: "cat")
        let a = try XCTUnwrap(search(r)), b = try XCTUnwrap(search(r, current: a))
        XCTAssertEqual(a.targetRange, NSRange(location: 0, length: 3)); XCTAssertEqual(b.targetRange.location, 8)
        XCTAssertNil(search(r, current: b)); XCTAssertNil(search(r, current: a, direction: .previous))
        XCTAssertEqual(search(r, current: b, direction: .previous)?.targetRange.location, 0)
    }
    func testInitialPreviousStartsAtLast() {
        let r = DesktopText(); r.replace(text: "cat dog cat", query: "cat")
        XCTAssertEqual(search(r, direction: .previous)?.targetRange.location, 8)
    }
    func testUTF16RangeCanBeSelectedNormally() throws {
        let r = DesktopText(); r.replace(text: "\u{1F600} e\u{301} target", query: "target")
        let result = try XCTUnwrap(search(r)); XCTAssertEqual(result.targetRange, NSRange(location: 6, length: 6))
        r.textView.setSelectedRange(result.targetRange)
        XCTAssertEqual((r.textView.string as NSString).substring(with: r.textView.selectedRange()), "target")
        XCTAssertTrue(r.textView.isSelectable); XCTAssertFalse(r.textView.isEditable)
    }
    func testPartialGraphemesExcluded() {
        XCTAssertTrue(LiteralMatches.ranges(in: "e\u{301}", query: "e", allowOverlaps: false).isEmpty)
        XCTAssertTrue(LiteralMatches.ranges(in: "\u{1F469}\u{200D}\u{1F4BB}", query: "\u{1F469}", allowOverlaps: true).isEmpty)
    }
    func testExplicitOverlapPolicy() {
        let r = DesktopText(); r.replace(text: "banana", query: "ana", allowOverlaps: true)
        XCTAssertEqual(r.matches.map(\.location), [1,3]); r.replace(text: "banana", query: "ana")
        XCTAssertEqual(r.matches.map(\.location), [1])
    }
    func testOldRotorCannotSearchNewRevision() throws {
        let r = DesktopText(); r.replace(text: "cat dog", query: "cat")
        let old = try XCTUnwrap(r.textView.accessibilityCustomRotors().first)
        r.replace(text: "cat dog", query: "dog")
        XCTAssertNil(search(r, rotor: old)); XCTAssertEqual(search(r)?.targetRange.location, 4)
    }
    func testNewSessionRestartsOldResult() throws {
        let r = DesktopText(); r.replace(text: "cat dog cat", query: "cat")
        let last = try XCTUnwrap(search(r, direction: .previous)); r.replace(text: "cat dog cat", query: "cat")
        XCTAssertEqual(search(r, current: last)?.targetRange.location, 0)
    }
    func testUnannouncedEditRejectsCachedRange() {
        let r = DesktopText(); r.replace(text: "cat", query: "cat"); r.textView.string = "changed"
        XCTAssertNil(search(r))
    }
    func testEmptyQueryPreservesOrdinaryText() {
        let r = DesktopText(); r.replace(text: "updated", query: "")
        XCTAssertEqual(r.textView.string, "updated"); XCTAssertTrue(r.textView.accessibilityCustomRotors().isEmpty)
        XCTAssertTrue(r.textView.isSelectable)
    }
    func testFilterStringIsRespected() {
        let r = DesktopText(); r.replace(text: "Cat cat", query: "cat")
        XCTAssertNil(search(r, filter: "dog")); XCTAssertNotNil(search(r, filter: "CA"))
    }
    func testForeignAndPartialCurrentResultsRestart() throws {
        let r = DesktopText(); r.replace(text: "cat cat", query: "cat"); _ = search(r)
        let foreign = NSAccessibilityCustomRotor.ItemResult(targetElement: NSTextView()); foreign.targetRange = NSRange(location: 4, length: 3)
        XCTAssertEqual(search(r, current: foreign)?.targetRange.location, 0)
        let partial = NSAccessibilityCustomRotor.ItemResult(targetElement: r.textView); partial.targetRange = NSRange(location: 0, length: 1)
        XCTAssertEqual(search(r, current: partial)?.targetRange.location, 0)
    }
    func testRemovedMatchesClearRotor() {
        let r = DesktopText(); r.replace(text: "cat", query: "cat"); r.replace(text: "dog", query: "cat")
        XCTAssertTrue(r.matches.isEmpty); XCTAssertNil(search(r))
    }
}

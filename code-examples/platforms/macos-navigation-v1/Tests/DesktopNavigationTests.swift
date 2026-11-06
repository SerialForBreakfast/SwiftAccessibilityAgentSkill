import XCTest
import AppKit
@testable import AccessibilityExamples

@MainActor
final class DesktopNavigationTests: XCTestCase {
    private let a = DesktopResults.Item(id: "a", title: "Invoice")
    private let b = DesktopResults.Item(id: "b", title: "Invoice")
    private func results() -> DesktopResults { _ = NSApplication.shared; let r = DesktopResults(); r.apply([a,b]); return r }
    private func button() -> NSButton { _ = NSApplication.shared; return NSButton(title: "Action", target: nil, action: nil) }
    func testRowsAndVisibleValues() { let r = results(); XCTAssertEqual(r.table.numberOfRows, 2); XCTAssertEqual(r.tableView(r.table, objectValueFor: nil, row: 0) as? String, "Invoice") }
    func testSelectByIdentity() { let r = results(); r.select("b"); XCTAssertEqual(r.table.selectedRow, 1); XCTAssertEqual(r.selectedID, "b") }
    func testReorderPreservesIdentity() { let r = results(); r.select("b"); r.apply([b,a]); XCTAssertEqual(r.table.selectedRow, 0); XCTAssertEqual(r.selectedID, "b") }
    func testRemovedSelectionClears() { let r = results(); r.select("b"); r.apply([a]); XCTAssertNil(r.selectedID); XCTAssertEqual(r.table.selectedRow, -1) }
    func testUnknownSelectionClears() { let r = results(); r.select("a"); r.select("missing"); XCTAssertNil(r.selectedID) }
    func testDuplicateIDsRejectedAtomically() { let r = results(); r.select("b"); XCTAssertFalse(r.apply([a,a])); XCTAssertEqual(r.items, [a,b]); XCTAssertEqual(r.selectedID, "b") }
    func testEmptyResultsClearSelection() { let r = results(); r.select("a"); XCTAssertTrue(r.apply([])); XCTAssertEqual(r.table.numberOfRows, 0); XCTAssertNil(r.selectedID) }
    func testNoSelectionIsNotInvented() { let r = results(); r.apply([b,a]); XCTAssertEqual(r.table.selectedRow, -1) }
    func testExternalTableSelectionIsPreserved() { let r = results(); r.table.selectRowIndexes(IndexSet(integer: 1), byExtendingSelection: false); r.apply([b,a]); XCTAssertEqual(r.selectedID, "b") }
    func testRenamedItemKeepsIdentity() { let r = results(); r.select("a"); r.apply([.init(id: "a", title: "Renamed"), b]); XCTAssertEqual(r.selectedID, "a"); XCTAssertEqual(r.tableView(r.table, objectValueFor: nil, row: 0) as? String, "Renamed") }
    func testKeyCycleFollowsInputOrder() { let a = button(), b = button(), c = button(), order = DesktopKeyOrder(); order.apply([a,b,c]); XCTAssertTrue(a.nextKeyView === b); XCTAssertTrue(b.nextKeyView === c); XCTAssertTrue(c.nextKeyView === a) }
    func testDisabledKeyViewExcluded() { let a = button(), b = button(), c = button(), order = DesktopKeyOrder(); b.isEnabled = false; order.apply([a,b,c]); XCTAssertTrue(a.nextKeyView === c); XCTAssertNil(b.nextKeyView) }
    func testHiddenKeyViewExcluded() { let a = button(), b = button(), order = DesktopKeyOrder(); b.isHidden = true; order.apply([a,b]); XCTAssertTrue(a.nextKeyView === a); XCTAssertNil(b.nextKeyView) }
    func testRemovedKeyLinksCleared() { let a = button(), b = button(), order = DesktopKeyOrder(); order.apply([a,b]); order.apply([a]); XCTAssertNil(b.nextKeyView); XCTAssertTrue(a.nextKeyView === a) }
    func testDuplicateKeyInputDoesNotBreakCycle() { let a = button(), b = button(), order = DesktopKeyOrder(); order.apply([a,b,a]); XCTAssertTrue(a.nextKeyView === b); XCTAssertTrue(b.nextKeyView === a) }
    func testStopClearsOwnedLinks() { let a = button(), b = button(), order = DesktopKeyOrder(); order.apply([a,b]); order.stop(); XCTAssertNil(a.nextKeyView); XCTAssertNil(b.nextKeyView) }
    func testIncomingDisabledLinkCleared() { let a = button(), b = button(), order = DesktopKeyOrder(); b.nextKeyView = a; b.isEnabled = false; order.apply([a,b]); XCTAssertNil(b.nextKeyView) }
    func testEmptyKeyOrderClearsPriorLinks() { let a = button(), b = button(), order = DesktopKeyOrder(); order.apply([a,b]); order.apply([]); XCTAssertNil(a.nextKeyView); XCTAssertNil(b.nextKeyView) }
}

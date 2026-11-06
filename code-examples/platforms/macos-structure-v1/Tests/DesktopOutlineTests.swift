import XCTest
import AppKit
@testable import AccessibilityExamples

@MainActor
final class DesktopOutlineTests: XCTestCase {
    typealias Item = DesktopOutline.Item
    private func tree() -> [Item] { [Item(id: "g", title: "Group", children: [Item(id: "a", title: "Alpha"), Item(id: "b", title: "Beta")]), Item(id: "z", title: "Last")] }
    private func configured() -> DesktopOutline { let d = DesktopOutline(); XCTAssertTrue(d.apply(tree())); return d }
    func testColumnsHaveDistinctNamesAndOutlineOwnership() {
        let d = configured()
        XCTAssertEqual(d.outline.tableColumns.map(\.title), ["Name", "Kind"])
        XCTAssertTrue(d.outline.outlineTableColumn === d.outline.tableColumns[0])
        XCTAssertEqual(d.outline.accessibilityLabel(), "Library")
    }
    func testRootCountAndChildOrder() {
        let d = configured()
        XCTAssertEqual(d.outlineView(d.outline, numberOfChildrenOfItem: nil), 2)
        XCTAssertTrue(d.outlineView(d.outline, child: 0, ofItem: nil) as AnyObject === d.nodes["g"])
        XCTAssertTrue(d.outlineView(d.outline, child: 1, ofItem: nil) as AnyObject === d.nodes["z"])
    }
    func testNestedChildrenAndExpandableState() throws {
        let d = configured(), group = try XCTUnwrap(d.nodes["g"])
        XCTAssertEqual(d.outlineView(d.outline, numberOfChildrenOfItem: group), 2)
        XCTAssertTrue(d.outlineView(d.outline, child: 1, ofItem: group) as AnyObject === d.nodes["b"])
        XCTAssertTrue(d.outlineView(d.outline, isItemExpandable: group))
        XCTAssertFalse(d.outlineView(d.outline, isItemExpandable: try XCTUnwrap(d.nodes["a"])))
    }
    func testEachColumnUsesItsOwnValue() {
        let d = configured(), columns = d.outline.tableColumns
        XCTAssertEqual(d.outlineView(d.outline, objectValueFor: columns[0], byItem: d.nodes["g"]) as? String, "Group")
        XCTAssertEqual(d.outlineView(d.outline, objectValueFor: columns[1], byItem: d.nodes["g"]) as? String, "Group")
        XCTAssertEqual(d.outlineView(d.outline, objectValueFor: columns[1], byItem: d.nodes["a"]) as? String, "Item")
    }
    func testRenameRetainsStableNodeIdentity() throws {
        let d = configured(), original = try XCTUnwrap(d.nodes["a"])
        XCTAssertTrue(d.apply([Item(id: "a", title: "Renamed")]))
        XCTAssertTrue(d.nodes["a"] === original); XCTAssertEqual(original.title, "Renamed")
    }
    func testExpansionPersistsAcrossReload() throws {
        let d = configured(), group = try XCTUnwrap(d.nodes["g"])
        d.outline.expandItem(group)
        XCTAssertTrue(d.outline.isItemExpanded(group))
        XCTAssertTrue(d.apply(tree()))
        XCTAssertTrue(d.outline.isItemExpanded(group)); XCTAssertEqual(d.outline.numberOfRows, 4)
    }
    func testSelectedChildSurvivesSiblingReorder() throws {
        let d = configured(); d.outline.expandItem(try XCTUnwrap(d.nodes["g"])); d.select("b")
        XCTAssertEqual(d.selectedID, "b")
        XCTAssertTrue(d.apply([Item(id: "g", title: "Group", children: [Item(id: "b", title: "Beta"), Item(id: "a", title: "Alpha")])]))
        XCTAssertEqual(d.selectedID, "b")
    }
    func testRemovedSelectionClears() {
        let d = configured(); d.select("z")
        XCTAssertTrue(d.apply([Item(id: "only", title: "Only")]))
        XCTAssertNil(d.selectedID)
    }
    func testDuplicateRootsAreRejectedAtomically() {
        let d = configured(); d.select("z")
        XCTAssertFalse(d.apply([Item(id: "x", title: "One"), Item(id: "x", title: "Two")]))
        XCTAssertEqual(d.roots.map(\.id), ["g", "z"]); XCTAssertEqual(d.selectedID, "z")
    }
    func testDuplicateNestedIDsAreRejectedAtomically() {
        let d = configured()
        XCTAssertFalse(d.apply([Item(id: "x", title: "One", children: [Item(id: "x", title: "Child")])]))
        XCTAssertEqual(d.roots.map(\.id), ["g", "z"])
    }
    func testSameIDInDifferentBranchesIsRejected() {
        let d = configured()
        XCTAssertFalse(d.apply([Item(id: "x", title: "One", children: [Item(id: "same", title: "A")]), Item(id: "y", title: "Two", children: [Item(id: "same", title: "B")])]))
        XCTAssertEqual(d.nodes.count, 4)
    }
    func testRemovedNodeCannotSupplyStaleChildren() throws {
        let d = configured(), old = try XCTUnwrap(d.nodes["g"])
        XCTAssertTrue(d.apply([]))
        XCTAssertEqual(d.outlineView(d.outline, numberOfChildrenOfItem: old), 0)
        XCTAssertFalse(d.outlineView(d.outline, isItemExpandable: old))
    }
    func testUnknownColumnDoesNotInventAValue() {
        let d = configured(), unknown = NSTableColumn(identifier: NSUserInterfaceItemIdentifier("other"))
        XCTAssertNil(d.outlineView(d.outline, objectValueFor: unknown, byItem: d.nodes["a"]))
    }
    func testCollapsedChildCannotSelectWrongRow() {
        let d = configured(); d.select("a")
        XCTAssertNil(d.selectedID)
    }
    func testEmptyUpdateClearsRowsAndSelection() {
        let d = configured(); d.select("z"); XCTAssertTrue(d.apply([]))
        XCTAssertEqual(d.outline.numberOfRows, 0); XCTAssertNil(d.selectedID); XCTAssertTrue(d.nodes.isEmpty)
    }
    func testDeepNestedRelationshipsAreRetained() throws {
        let d = DesktopOutline()
        XCTAssertTrue(d.apply([Item(id: "p", title: "P", children: [Item(id: "q", title: "Q", children: [Item(id: "r", title: "R")])])]))
        let q = try XCTUnwrap(d.nodes["q"])
        XCTAssertEqual(d.outlineView(d.outline, numberOfChildrenOfItem: q), 1)
        XCTAssertTrue(d.outlineView(d.outline, child: 0, ofItem: q) as AnyObject === d.nodes["r"])
    }
}

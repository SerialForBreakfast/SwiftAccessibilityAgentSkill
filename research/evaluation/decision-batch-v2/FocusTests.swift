import XCTest
@testable import AccessibilityExamples
#if os(tvOS)
import UIKit

@MainActor final class ShelfChecks: XCTestCase {
    func testInstalledActionNeedsCurrentBindingAndEnabledButton() throws {
        let shelf = TelevisionResults()
        let item = TelevisionResults.Item(id: "x", title: "Same", actionName: "Play")
        func binding() throws -> (UIButton, UIAction) {
            let b = try XCTUnwrap(shelf.buttons.first)
            var installed: UIAction?
            b.enumerateEventHandlers { action, _, events, _ in
                if events.contains(.primaryActionTriggered) { installed = action }
            }
            return (b, try XCTUnwrap(installed))
        }
        XCTAssertTrue(shelf.apply([item]))
        let (old, retired) = try binding()
        XCTAssertTrue(shelf.apply([item]))
        let (current, active) = try binding()
        old.sendAction(retired)
        XCTAssertNil(shelf.selectedID, "retired binding selected the replacement")
        current.isEnabled = false
        current.sendAction(active)
        XCTAssertNil(shelf.selectedID, "disabled registration dispatched")
        current.isEnabled = true
        current.sendActions(for: .primaryActionTriggered)
        XCTAssertEqual(shelf.selectedID, "x")
    }
}
#elseif os(macOS)
import AppKit
@MainActor final class DesktopChecks: XCTestCase {
    func testIdenticalValueReplacementRetiresDelete() {
        let state = DocumentState(), item = Article(id: "x", title: "Same", important: true)
        var selected = [String](), deleted = [String]()
        state.chosen = { selected.append($0) }; state.deleted = { deleted.append($0) }
        XCTAssertTrue(state.replace([item]))
        let retired = state.action(for: item.id, remove: true)
        XCTAssertTrue(state.replace([item]))
        retired()
        XCTAssertEqual(state.entries, [item], "value equality did not retire old Delete")
        XCTAssertTrue(deleted.isEmpty)
        state.action(for: item.id)()
        state.action(for: item.id, remove: true)()
        XCTAssertEqual(selected, ["x"]); XCTAssertEqual(deleted, ["x"])
        XCTAssertTrue(state.entries.isEmpty)
    }
    func testConfiguredRowAndIndependentChild() {
        let row = DesktopRow()
        var opened = [String]()
        row.choose = { opened.append($0) }
        row.configure(id: "x", title: "Item", selected: true, expanded: true)
        XCTAssertTrue(row.isAccessibilityElement())
        XCTAssertEqual(row.accessibilityRole(), .row); XCTAssertTrue(row.isAccessibilitySelected())
        XCTAssertTrue((row.accessibilityChildren()?.first as? NSButton) === row.open)
        XCTAssertTrue(row.open.sendAction(row.open.action, to: row.open.target))
        XCTAssertEqual(opened, ["x"])
    }
    func testNativeSearchOwner() {
        let field = CatalogSearch.field()
        XCTAssertTrue(field.isEditable && field.isSelectable)
        XCTAssertEqual(field.accessibilityLabel(), "Catalog search")
        field.stringValue = "First"; field.stringValue = "Second"
        XCTAssertEqual(field.stringValue, "Second")
    }
}
#endif

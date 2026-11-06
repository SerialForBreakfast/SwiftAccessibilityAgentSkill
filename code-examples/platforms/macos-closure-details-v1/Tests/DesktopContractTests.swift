import XCTest
import AppKit
@testable import AccessibilityExamples

@MainActor
final class DesktopContractTests: XCTestCase {
    func testExplicitRowRoleAndChildSemantics() {
        let r = DesktopRow(); r.configure(id: "one", title: "Report", selected: true, expanded: true)
        XCTAssertEqual(r.accessibilityRole(), .row)
        XCTAssertEqual(r.accessibilityLabel(), "Report")
        XCTAssertTrue(r.isAccessibilitySelected()); XCTAssertTrue(r.isAccessibilityExpanded())
        XCTAssertTrue((r.accessibilityChildren()?.first as? NSButton) === r.open)
        XCTAssertEqual(r.open.accessibilityLabel(), "Open Report")
    }
    func testReconfigureClearsSelectionExpansionAndNames() {
        let r = DesktopRow(); r.configure(id: "one", title: "First", selected: true, expanded: true)
        r.configure(id: "two", title: "Second", selected: false, expanded: false)
        XCTAssertFalse(r.isAccessibilitySelected()); XCTAssertFalse(r.isAccessibilityExpanded())
        XCTAssertEqual(r.accessibilityLabel(), "Second"); XCTAssertEqual(r.open.accessibilityLabel(), "Open Second")
    }
    func testOrdinaryRowActionUsesCurrentIdentity() {
        let r = DesktopRow(); var chosen: [String] = []; r.choose = { chosen.append($0) }
        r.configure(id: "one", title: "First", selected: false, expanded: false)
        r.configure(id: "two", title: "Second", selected: false, expanded: false)
        r.open.performClick(nil); XCTAssertEqual(chosen, ["two"])
    }
    func testDisabledRowActionDoesNotChoose() {
        let r = DesktopRow(); var called = false; r.choose = { _ in called = true }
        r.open.isEnabled = false; r.activate(); XCTAssertFalse(called)
    }
    private func key(_ characters: String, code: UInt16) -> NSEvent {
        NSEvent.keyEvent(with: .keyDown, location: .zero, modifierFlags: [], timestamp: 0,
            windowNumber: 0, context: nil, characters: characters, charactersIgnoringModifiers: characters,
            isARepeat: false, keyCode: code)!
    }
    func testSpaceEventUsesOrdinaryToggleTransition() {
        let t = SemanticToggle(); var states: [Bool] = []; t.changed = { states.append($0) }
        t.keyDown(with: key(" ", code: 49)); XCTAssertEqual(states, [true]); XCTAssertEqual(t.status.stringValue, "On")
    }
    func testReturnEventUsesSameTransitionAsAccessibilityPress() {
        let t = SemanticToggle(); t.keyDown(with: key("\r", code: 36))
        XCTAssertTrue(t.on); XCTAssertTrue(t.accessibilityPerformPress()); XCTAssertFalse(t.on)
    }
    func testDisabledKeyboardEventCannotToggle() {
        let t = SemanticToggle(); t.isEnabled = false; var called = false; t.changed = { _ in called = true }
        t.keyDown(with: key(" ", code: 49)); XCTAssertFalse(t.on); XCTAssertFalse(called)
    }
}

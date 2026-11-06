import XCTest
import AppKit
import AVKit
@testable import AccessibilityExamples

@MainActor
final class StateContractTests: XCTestCase {
    func testRegionPreservesOrdinaryControlAndNamedBoundary() {
        let r = RegionState(); r.configure(name: "Open report", selected: false, reduceTransparency: false)
        XCTAssertTrue(r.button.superview === r)
        XCTAssertEqual(r.accessibilityLabel(), "Downloads")
        XCTAssertEqual(r.button.accessibilityLabel(), "Open report")
        XCTAssertEqual(r.accessibilityChildren()?.count, 2)
    }
    func testSelectedStateHasNonColorTextAndValue() {
        let r = RegionState(); r.configure(name: "Report", selected: true, reduceTransparency: false)
        XCTAssertEqual(r.status.stringValue, "Selected")
        XCTAssertEqual(r.button.accessibilityValue() as? String, "Selected")
    }
    func testReconfigureClearsStaleSelectionText() {
        let r = RegionState(); r.configure(name: "First", selected: true, reduceTransparency: false)
        r.configure(name: "Second", selected: false, reduceTransparency: false)
        XCTAssertEqual(r.button.accessibilityLabel(), "Second")
        XCTAssertEqual(r.status.stringValue, "Not selected")
    }
    func testReducedTransparencyDoesNotRemoveContent() {
        let r = RegionState(); r.configure(name: "Report", selected: false, reduceTransparency: true)
        XCTAssertTrue(r.backdrop.isHidden); XCTAssertFalse(r.button.isHidden); XCTAssertFalse(r.status.isHidden)
        r.configure(name: "Report", selected: false, reduceTransparency: false); XCTAssertFalse(r.backdrop.isHidden)
    }
    func testNativePlayerControlsAndPlayerArePreserved() {
        let p = AVPlayer(), view = RegionState.player(p)
        XCTAssertTrue(view.player === p)
        XCTAssertEqual(view.controlsStyle, .floating)
    }
    func testModalFlagRestoresOriginalFalse() {
        let view = NSView(), scope = ModalFlag(NSView())
        let s = ModalFlag(view); s.begin(); XCTAssertTrue(view.isAccessibilityModal())
        s.end(); XCTAssertFalse(view.isAccessibilityModal()); scope.end()
    }
    func testRepeatedModalBeginRestoresOriginalTrue() {
        let view = NSView(); view.setAccessibilityModal(true)
        let s = ModalFlag(view); s.begin(); s.begin(); s.end(); s.end()
        XCTAssertTrue(view.isAccessibilityModal())
    }
    func testCustomToggleRoleValueAndPressAgree() {
        let t = SemanticToggle(); XCTAssertEqual(t.accessibilityRole(), .checkBox)
        XCTAssertEqual(t.accessibilityValue() as? NSNumber, false)
        XCTAssertTrue(t.accessibilityPerformPress()); XCTAssertEqual(t.accessibilityValue() as? NSNumber, true)
        XCTAssertEqual(t.status.stringValue, "On")
    }
    func testDisabledCustomControlRejectsBothActionPaths() {
        let t = SemanticToggle(); t.isEnabled = false
        XCTAssertFalse(t.activate()); XCTAssertFalse(t.accessibilityPerformPress())
        XCTAssertFalse(t.isAccessibilityEnabled()); XCTAssertFalse(t.acceptsFirstResponder)
    }
    func testOrdinaryAndAccessibilityActionUseSameStateTransition() {
        let t = SemanticToggle(); var values: [Bool] = []; t.changed = { values.append($0) }
        XCTAssertTrue(t.activate()); XCTAssertTrue(t.accessibilityPerformPress())
        XCTAssertEqual(values, [true, false]); XCTAssertEqual(t.status.stringValue, "Off")
    }
}

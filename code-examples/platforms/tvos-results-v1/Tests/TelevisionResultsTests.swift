import XCTest
import UIKit
@testable import AccessibilityExamples

@MainActor
final class TelevisionResultsTests: XCTestCase {
    private let a = TelevisionResults.Item(id: "a", title: "Alpha", actionName: "Play Alpha")
    private let b = TelevisionResults.Item(id: "b", title: "Beta", actionName: "Play Beta")
    private func results() -> TelevisionResults { let r = TelevisionResults(); r.apply([a,b]); return r }
    func testVisibleAndAccessibleNames() { let r = results(); XCTAssertEqual(r.buttons[0].title(for: .normal), "Alpha"); XCTAssertEqual(r.buttons[0].accessibilityLabel, "Play Alpha") }
    func testPrimaryActionSelectsItem() { let r = results(); r.buttons[1].sendActions(for: .primaryActionTriggered); XCTAssertEqual(r.selectedID, "b") }
    func testReorderPreservesSelection() { let r = results(); r.select("b"); r.apply([b,a]); XCTAssertEqual(r.selectedID, "b"); XCTAssertTrue(r.buttons[0].accessibilityTraits.contains(.selected)) }
    func testFilterPreservesVisibleSelection() { let r = results(); r.select("b"); r.apply([a,b], query: "BETA"); XCTAssertEqual(r.visible, [b]); XCTAssertEqual(r.selectedID, "b") }
    func testFilteredSelectionClears() { let r = results(); r.select("a"); r.apply([a,b], query: "Beta"); XCTAssertNil(r.selectedID); XCTAssertFalse(r.buttons[0].accessibilityTraits.contains(.selected)) }
    func testStaleButtonDoesNotSelectReboundItem() { let r = results(); let old = r.buttons[0]; r.apply([a,b]); old.sendActions(for: .primaryActionTriggered); XCTAssertNil(r.selectedID) }
    func testDuplicateIDsRejectedAtomically() { let r = results(); let button = r.buttons[0]; r.select("b"); XCTAssertFalse(r.apply([a,a])); XCTAssertEqual(r.visible, [a,b]); XCTAssertTrue(r.buttons[0] === button); XCTAssertEqual(r.selectedID, "b") }
    func testEmptyResultsRemoveOldButtons() { let r = results(); let old = r.buttons[0]; r.select("a"); r.apply([]); XCTAssertTrue(r.buttons.isEmpty); XCTAssertNil(old.superview); XCTAssertNil(r.selectedID) }
    func testDisabledButtonCannotSelect() { let r = results(); r.buttons[0].isEnabled = false; r.buttons[0].sendActions(for: .primaryActionTriggered); XCTAssertNil(r.selectedID) }
    func testSelectionPreservesUnrelatedTraits() { let r = results(); r.buttons[0].accessibilityTraits = [.button, .startsMediaSession]; r.select("a"); r.select("b"); XCTAssertTrue(r.buttons[0].accessibilityTraits.contains(.startsMediaSession)); XCTAssertFalse(r.buttons[0].accessibilityTraits.contains(.selected)) }
    func testReducedMotionStillUpdatesContent() { var animations = 0; let s = TelevisionStatus(reduceMotion: {true}, animate: {animations += 1}); s.update("Ready"); XCTAssertEqual(s.label.text, "Ready"); XCTAssertEqual(s.label.accessibilityLabel, "Ready"); XCTAssertEqual(animations, 0) }
    func testNormalMotionAnimatesAfterContent() { var seen: String?; var s: TelevisionStatus!; s = TelevisionStatus(reduceMotion: {false}, animate: {seen = s.label.text}); s.update("Ready"); XCTAssertEqual(seen, "Ready"); s = nil }
    func testPreferenceReadOnEachChange() { var reduced = false, animations = 0; let s = TelevisionStatus(reduceMotion: {reduced}, animate: {animations += 1}); s.update("Loading"); reduced = true; s.update("Ready"); XCTAssertEqual(animations, 1); XCTAssertEqual(s.label.text, "Ready") }
    func testRepeatedStatusIsQuiet() { var animations = 0; let s = TelevisionStatus(reduceMotion: {false}, animate: {animations += 1}); s.update("Ready"); s.update("Ready"); XCTAssertEqual(animations, 1) }
    func testStatusRemainsAccessible() { let s = TelevisionStatus(reduceMotion: {true}, animate: {}); s.update("Failed"); XCTAssertTrue(s.label.isAccessibilityElement); XCTAssertEqual(s.label.accessibilityLabel, "Failed") }
    func testLocalizedStatusPreserved() { let s = TelevisionStatus(reduceMotion: {true}, animate: {}); s.update("Prêt à lire"); XCTAssertEqual(s.label.text, "Prêt à lire"); XCTAssertEqual(s.label.accessibilityLabel, "Prêt à lire") }
}

import XCTest
import UIKit
@testable import AccessibilityExamples

@MainActor
final class TelevisionActionsTests: XCTestCase {
    private func row(_ text: String = "Episode A", play: @escaping () -> Void = {}, details: @escaping () -> Void = {}) -> TelevisionActions {
        let row = TelevisionActions(); configure(row, text, play: play, details: details); return row
    }
    private func configure(_ r: TelevisionActions, _ text: String = "Episode A", play: @escaping () -> Void = {}, details: @escaping () -> Void = {}) {
        r.configure(title: text, playName: "Play \(text)", detailsName: "Details \(text)", onPlay: play, onDetails: details)
    }
    func testVisibleActionNames() { let r = row(); XCTAssertEqual(r.play.title(for: .normal), "Play Episode A"); XCTAssertEqual(r.details.title(for: .normal), "Details Episode A") }
    func testVisibleNamesRefresh() { let r = row(); configure(r, "B"); XCTAssertEqual(r.play.title(for: .normal), "Play B"); XCTAssertEqual(r.details.title(for: .normal), "Details B") }
    func testContextualNames() { let r = row(); XCTAssertEqual(r.play.accessibilityLabel, "Play Episode A"); XCTAssertEqual(r.details.accessibilityLabel, "Details Episode A") }
    func testContainerPreservesControls() { let r = row(); XCTAssertFalse(r.isAccessibilityElement); XCTAssertFalse(r.accessibilityElementsHidden); XCTAssertTrue(r.play.isAccessibilityElement); XCTAssertTrue(r.details.isAccessibilityElement) }
    func testOrdinaryPlay() { var p = 0, d = 0; let r = row(play: {p += 1}, details: {d += 1}); r.play.sendActions(for: .primaryActionTriggered); XCTAssertEqual(p, 1); XCTAssertEqual(d, 0) }
    func testOrdinaryDetails() { var d = 0; let r = row(details: {d += 1}); r.details.sendActions(for: .primaryActionTriggered); XCTAssertEqual(d, 1) }
    func testCustomDetails() { var d = 0; let r = row(details: {d += 1}); let a = r.play.accessibilityCustomActions!.first!; XCTAssertEqual(a.actionHandler?(a), true); XCTAssertEqual(d, 1) }
    func testStaleActionRejected() { let r = row(); let a = r.play.accessibilityCustomActions!.first!; var d = 0; configure(r, "B", details: {d += 1}); XCTAssertEqual(a.actionHandler?(a), false); XCTAssertEqual(d, 0) }
    func testReuseReplacesHandler() { var a = 0, b = 0; let r = row(details: {a += 1}); configure(r, "B", details: {b += 1}); r.details.sendActions(for: .primaryActionTriggered); XCTAssertEqual(a, 0); XCTAssertEqual(b, 1) }
    func testReuseNames() { let r = row(); configure(r, "B"); XCTAssertEqual(r.play.accessibilityLabel, "Play B"); XCTAssertEqual(r.details.accessibilityLabel, "Details B") }
    func testReuseClearsValue() { let r = row(); r.play.accessibilityValue = "old"; configure(r); XCTAssertNil(r.play.accessibilityValue) }
    func testDisabledOrdinaryAction() { var d = 0; let r = row(details: {d += 1}); r.details.isEnabled = false; r.details.sendActions(for: .primaryActionTriggered); XCTAssertEqual(d, 0) }
    func testDisabledCustomAction() { let r = row(); r.details.isEnabled = false; let a = r.play.accessibilityCustomActions!.first!; XCTAssertEqual(a.actionHandler?(a), false) }
    func testActionDoesNotRetainRow() { var r: TelevisionActions? = row(); weak var weakRow = r; let a = r!.play.accessibilityCustomActions!.first!; r = nil; XCTAssertNil(weakRow); XCTAssertEqual(a.actionHandler?(a), false) }
    func testSingleShortcutAfterReuse() { let r = row(); configure(r); configure(r); XCTAssertEqual(r.play.accessibilityCustomActions?.count, 1) }
    func testPreferredOrder() { let r = row(); XCTAssertEqual(r.preferredFocusEnvironments.count, 2); XCTAssertTrue(r.preferredFocusEnvironments.first === r.play) }
    func testDisabledPreferredTargetExcluded() { let r = row(); r.play.isEnabled = false; XCTAssertTrue(r.preferredFocusEnvironments.first === r.details) }
    func testRemovedPreferredTargetExcluded() { let r = row(); r.play.removeFromSuperview(); XCTAssertTrue(r.preferredFocusEnvironments.first === r.details) }
    func testHiddenPreferredTargetExcluded() { let r = row(); r.play.isHidden = true; XCTAssertTrue(r.preferredFocusEnvironments.first === r.details) }
    func testNoEligibleTarget() { let r = row(); r.play.isHidden = true; r.details.alpha = 0; XCTAssertTrue(r.preferredFocusEnvironments.isEmpty) }
    func testSelectedPreservesOtherTraits() { let r = row(); r.play.accessibilityTraits = [.button, .startsMediaSession]; r.setSelected(true); XCTAssertTrue(r.play.accessibilityTraits.contains(.button)); XCTAssertTrue(r.play.accessibilityTraits.contains(.startsMediaSession)); XCTAssertTrue(r.play.accessibilityTraits.contains(.selected)) }
    func testDeselectedPreservesOtherTraits() { let r = row(); r.play.accessibilityTraits = [.button, .selected]; r.setSelected(false); XCTAssertEqual(r.play.accessibilityTraits, .button) }
}

import XCTest
import UIKit
@testable import AccessibilityExamples

@MainActor
final class GapContractTests: XCTestCase {
    func testSummaryPreservesCompleteLocalizedName() {
        let card = SummaryCard()
        card.configure(title: "Hotel", subtitle: "Deux nuits", spokenSummary: "Deux nuits au Hotel")
        XCTAssertEqual(card.accessibilityLabel, "Deux nuits au Hotel")
        XCTAssertEqual(card.title.text, "Hotel")
        XCTAssertEqual(card.subtitle.text, "Deux nuits")
    }
    func testSummaryExposesOneNoninteractiveConcept() {
        let card = SummaryCard()
        card.configure(title: "Hotel", subtitle: "Two nights", spokenSummary: "Hotel, two nights")
        XCTAssertTrue(card.isAccessibilityElement)
        XCTAssertFalse(card.title.isAccessibilityElement)
        XCTAssertFalse(card.subtitle.isAccessibilityElement)
        XCTAssertTrue(card.accessibilityTraits.contains(.staticText))
        XCTAssertEqual(card.subviews.count, 2)
    }
    func testSummaryReuseReplacesOwnedTextAndClearsValue() {
        let card = SummaryCard()
        card.configure(title: "Old", subtitle: "Old detail", spokenSummary: "Old summary")
        card.accessibilityValue = "Stale"
        card.configure(title: "New", subtitle: "New detail", spokenSummary: "New summary")
        XCTAssertEqual(card.accessibilityLabel, "New summary")
        XCTAssertEqual(card.title.text, "New")
        XCTAssertEqual(card.subtitle.text, "New detail")
        XCTAssertNil(card.accessibilityValue)
    }
    func testSummaryPreservesUnrelatedTrait() {
        let card = SummaryCard()
        card.accessibilityTraits.insert(.updatesFrequently)
        card.configure(title: "A", subtitle: "B", spokenSummary: "A B")
        XCTAssertTrue(card.accessibilityTraits.contains(.updatesFrequently))
    }
    func testQuantityHasNamedAdjustableValueAndOrdinaryButtons() {
        let view = QuantityChoices(name: "Tickets")
        XCTAssertFalse(view.isAccessibilityElement)
        XCTAssertTrue(view.value.isAccessibilityElement)
        XCTAssertEqual(view.value.accessibilityLabel, "Tickets")
        XCTAssertTrue(view.value.accessibilityTraits.contains(.adjustable))
        XCTAssertEqual(view.value.accessibilityValue, "0")
        XCTAssertEqual(view.more.title(for: .normal), "Increase quantity")
        XCTAssertEqual(view.less.title(for: .normal), "Decrease quantity")
        XCTAssertEqual(view.arrangedSubviews.count, 3)
    }
    func testOrdinaryQuantityButtonsChangeSameState() {
        let view = QuantityChoices(name: "Tickets")
        var calls: [Int] = []
        view.onChange = { calls.append($0) }
        view.more.sendActions(for: .primaryActionTriggered)
        view.less.sendActions(for: .primaryActionTriggered)
        XCTAssertEqual(calls, [1, 0])
        XCTAssertEqual(view.quantity, 0)
    }
    func testAdjustableHooksSynchronizeBeforeCallback() {
        let view = QuantityChoices(name: "Tickets")
        var calls: [Int] = []
        view.onChange = { quantity in
            calls.append(quantity)
            XCTAssertEqual(view.value.text, String(quantity))
            XCTAssertEqual(view.value.accessibilityValue, String(quantity))
        }
        view.value.accessibilityIncrement()
        view.value.accessibilityDecrement()
        XCTAssertEqual(calls, [1, 0])
        view.onChange = { _ in }
    }
    func testDisabledQuantityRejectsBothDirectPaths() {
        let view = QuantityChoices(name: "Tickets")
        var calls = 0
        view.onChange = { _ in calls += 1 }
        view.enabled = false
        XCTAssertFalse(view.more.isEnabled)
        XCTAssertFalse(view.less.isEnabled)
        view.more.sendActions(for: .primaryActionTriggered)
        view.value.accessibilityIncrement()
        XCTAssertEqual(view.quantity, 0)
        XCTAssertEqual(calls, 0)
    }
    func testQuantityReenableRestoresBothPaths() {
        let view = QuantityChoices(name: "Tickets")
        view.enabled = false
        view.enabled = true
        XCTAssertTrue(view.more.isEnabled)
        view.more.sendActions(for: .primaryActionTriggered)
        view.value.accessibilityIncrement()
        XCTAssertEqual(view.quantity, 2)
    }
    func testQuantityBoundsSuppressRedundantEvents() {
        let view = QuantityChoices(name: "Tickets")
        var calls: [Int] = []
        view.onChange = { calls.append($0) }
        for _ in 0..<5 { view.value.accessibilityIncrement() }
        XCTAssertEqual(calls, [1, 2, 3])
        for _ in 0..<5 { view.value.accessibilityDecrement() }
        XCTAssertEqual(calls, [1, 2, 3, 2, 1, 0])
    }
    func testQuantityRetainedChildrenDoNotRetainOwner() {
        var view: QuantityChoices? = QuantityChoices(name: "Tickets")
        weak var owner = view
        let value = view!.value, button = view!.more
        view = nil
        XCTAssertNil(owner)
        value.accessibilityIncrement()
        button.sendActions(for: .primaryActionTriggered)
        XCTAssertNil(owner)
    }
    func testReducedMotionUpdatesTextWithoutAnimation() {
        let view = MotionStatus(readReduceMotion: { true })
        view.animate = { _ in XCTFail("Reduced motion should not request optional animation") }
        view.update(message: "Saved")
        XCTAssertEqual(view.label.text, "Saved")
        XCTAssertEqual(view.label.accessibilityLabel, "Saved")
    }
    func testMotionFeedbackPrecedesOptionalAnimation() {
        let view = MotionStatus(readReduceMotion: { false })
        var durations: [TimeInterval] = []
        view.animate = { duration in
            durations.append(duration)
            XCTAssertEqual(view.label.text, "Saved")
            XCTAssertEqual(view.label.accessibilityLabel, "Saved")
        }
        view.update(message: "Saved")
        XCTAssertEqual(durations, [0.25])
        view.animate = { _ in }
    }
    func testMotionPreferenceIsReadOnEachUpdate() {
        var reduced = false, reads = 0, animations = 0
        let view = MotionStatus(readReduceMotion: { reads += 1; return reduced })
        view.animate = { _ in animations += 1 }
        view.update(message: "Saving")
        reduced = true
        view.update(message: "Saved")
        XCTAssertEqual(reads, 2)
        XCTAssertEqual(animations, 1)
        XCTAssertEqual(view.label.text, "Saved")
    }
    func testMotionUpdatesReplaceErrorWithCompletion() {
        let view = MotionStatus(readReduceMotion: { true })
        view.update(message: "Try again")
        view.update(message: "Saved")
        XCTAssertEqual(view.label.accessibilityLabel, "Saved")
        XCTAssertEqual(view.label.text, "Saved")
    }
    func testMotionPreservesSuppliedLocalizedMessage() {
        let view = MotionStatus(readReduceMotion: { true })
        view.update(message: "Enregistrement termine")
        XCTAssertEqual(view.label.text, "Enregistrement termine")
        XCTAssertEqual(view.label.accessibilityLabel, "Enregistrement termine")
    }
}

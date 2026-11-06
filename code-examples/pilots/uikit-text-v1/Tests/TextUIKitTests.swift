import XCTest
import UIKit
@testable import AccessibilityExamples

@MainActor private final class ActionTarget: NSObject {
    @objc func perform(_ action: UIAccessibilityCustomAction) -> Bool { true }
}

final class TextUIKitTests: XCTestCase {
    @MainActor private func search(_ view: TextMatchRotor, current: UIAccessibilityCustomRotorItemResult? = nil, direction: UIAccessibilityCustomRotor.Direction = .next) -> UIAccessibilityCustomRotorItemResult? {
        let predicate = UIAccessibilityCustomRotorSearchPredicate()
        if let current { predicate.currentItem = current }
        predicate.searchDirection = direction
        return view.textView.accessibilityCustomRotors?.first?.itemSearchBlock(predicate)
    }
    @MainActor func testInitialRangeSelectsFirstOrLastMatch() throws {
        let view = TextMatchRotor(frame: .zero)
        view.replace(text: "cat dog cat", query: "cat")
        let first = try XCTUnwrap(search(view)), last = try XCTUnwrap(search(view, direction: .previous))
        XCTAssertTrue(first.targetElement === view.textView)
        XCTAssertEqual(view.textView.offset(from: view.textView.beginningOfDocument, to: try XCTUnwrap(first.targetRange).start), 0)
        XCTAssertEqual(view.textView.offset(from: view.textView.beginningOfDocument, to: try XCTUnwrap(last.targetRange).start), 8)
    }
    @MainActor func testRangeSearchMovesBothDirections() throws {
        let view = TextMatchRotor(frame: .zero)
        view.replace(text: "cat dog cat", query: "cat")
        let first = try XCTUnwrap(search(view)), next = try XCTUnwrap(search(view, current: first))
        let previous = try XCTUnwrap(search(view, current: next, direction: .previous))
        XCTAssertEqual(view.textView.text(in: try XCTUnwrap(next.targetRange)), "cat")
        XCTAssertEqual(view.textView.offset(from: view.textView.beginningOfDocument, to: try XCTUnwrap(previous.targetRange).start), 0)
    }
    @MainActor func testRangeBoundariesReturnNil() throws {
        let view = TextMatchRotor(frame: .zero)
        view.replace(text: "cat", query: "cat")
        let only = try XCTUnwrap(search(view))
        XCTAssertNil(search(view, current: only))
        XCTAssertNil(search(view, current: only, direction: .previous))
    }
    @MainActor func testUnicodePrefixProducesExactSelectedText() throws {
        let view = TextMatchRotor(frame: .zero)
        view.replace(text: "\u{1F600} cafe\u{301} target", query: "target")
        let result = try XCTUnwrap(search(view)), range = try XCTUnwrap(result.targetRange)
        XCTAssertEqual(view.textView.text(in: range), "target")
        XCTAssertEqual(view.textView.offset(from: range.start, to: range.end), 6)
    }
    @MainActor func testReplacingTextDiscardsOldMatches() {
        let view = TextMatchRotor(frame: .zero)
        view.replace(text: "target", query: "target")
        view.replace(text: "nothing", query: "target")
        XCTAssertNil(search(view))
        XCTAssertEqual(view.textView.text, "nothing")
    }
    @MainActor func testEmptyQueryRejectsWithoutChangingDocument() throws {
        let view = TextMatchRotor(frame: .zero)
        view.replace(text: "cat", query: "cat")
        XCTAssertFalse(view.replace(text: "replacement", query: ""))
        XCTAssertEqual(view.textView.text, "cat")
        XCTAssertEqual(view.textView.text(in: try XCTUnwrap(search(view)?.targetRange)), "cat")
    }
    @MainActor func testForeignElementRangeRestartsWithoutUsingForeignPositions() throws {
        let view = TextMatchRotor(frame: .zero), other = UITextView()
        view.replace(text: "cat dog cat", query: "cat")
        other.text = "foreign"
        let range = try XCTUnwrap(other.textRange(from: other.beginningOfDocument, to: other.endOfDocument))
        let foreign = UIAccessibilityCustomRotorItemResult(targetElement: other, targetRange: range)
        let result = try XCTUnwrap(search(view, current: foreign))
        XCTAssertTrue(result.targetElement === view.textView)
        XCTAssertEqual(view.textView.offset(from: view.textView.beginningOfDocument, to: try XCTUnwrap(result.targetRange).start), 0)
    }
    @MainActor func testAttributedActionNameRoundTrips() {
        let action = UIAccessibilityCustomAction(attributedName: NSAttributedString(string: "Edit item")) { _ in true }
        XCTAssertEqual(action.name, "Edit item")
        action.name = "Rename item"
        XCTAssertEqual(action.attributedName.string, "Rename item")
    }
    @MainActor func testEditCategoryConfigurationAndDefault() {
        let plain = UIAccessibilityCustomAction(name: "Plain") { _ in true }
        XCTAssertNil(plain.category)
        let edit = EditActionFactory.make(title: NSAttributedString(string: "Rename")) { _ in true }
        XCTAssertEqual(edit.category, UIAccessibilityCustomAction.editCategory)
        XCTAssertEqual(edit.name, "Rename")
    }
    @MainActor func testAttributedActionInvokesStoredHandlerOnce() {
        var count = 0
        let action = EditActionFactory.make(title: NSAttributedString(string: "Rename")) { _ in count += 1; return true }
        XCTAssertEqual(action.actionHandler?(action), true)
        XCTAssertEqual(count, 1)
    }
    @MainActor func testSelectorActionDoesNotRetainTarget() {
        var action: UIAccessibilityCustomAction?
        weak var weakTarget: ActionTarget?
        autoreleasepool {
            let target = ActionTarget()
            weakTarget = target
            action = UIAccessibilityCustomAction(name: "Perform", target: target, selector: #selector(ActionTarget.perform(_:)))
        }
        XCTAssertNotNil(action)
        XCTAssertNil(weakTarget)
        XCTAssertNil(action?.target)
    }
    @MainActor func testRotorResultDoesNotRetainTargetElement() {
        var result: UIAccessibilityCustomRotorItemResult?
        weak var target: NSObject?
        autoreleasepool {
            let element = NSObject()
            target = element
            result = UIAccessibilityCustomRotorItemResult(targetElement: element, targetRange: nil)
        }
        XCTAssertNotNil(result)
        XCTAssertNil(target)
    }
    @MainActor func testSliderClampsValuesToConfiguredBounds() {
        let slider = UISlider()
        slider.minimumValue = 10; slider.maximumValue = 20
        slider.value = 30
        XCTAssertEqual(slider.value, 20)
        slider.setValue(-10, animated: false)
        XCTAssertEqual(slider.value, 10)
    }
    @MainActor func testStepperDefaultsAndClamping() {
        let stepper = UIStepper()
        XCTAssertEqual(stepper.minimumValue, 0)
        XCTAssertEqual(stepper.maximumValue, 100)
        XCTAssertEqual(stepper.stepValue, 1)
        XCTAssertFalse(stepper.wraps)
        stepper.minimumValue = 2; stepper.maximumValue = 4
        stepper.value = 10; XCTAssertEqual(stepper.value, 4)
        stepper.value = -10; XCTAssertEqual(stepper.value, 2)
    }
    @MainActor func testSwitchExplicitDispatchReportsCurrentState() {
        let control = UISwitch()
        var events: [Bool] = []
        control.addAction(UIAction { [weak control] _ in
            if let control { events.append(control.isOn) }
        }, for: .valueChanged)
        control.setOn(true, animated: false)
        events.removeAll()
        control.sendActions(for: .valueChanged)
        XCTAssertEqual(events, [true])
        control.setOn(false, animated: false)
        events.removeAll()
        control.sendActions(for: .valueChanged)
        XCTAssertEqual(events, [false])
    }
    @MainActor func testBodyFontSizesAcrossContentSizeCategories() {
        let categories: [UIContentSizeCategory] = [.extraSmall, .small, .medium, .large, .extraLarge, .extraExtraLarge, .extraExtraExtraLarge, .accessibilityMedium, .accessibilityLarge, .accessibilityExtraLarge, .accessibilityExtraExtraLarge, .accessibilityExtraExtraExtraLarge]
        let sizes = categories.map { UIFont.preferredFont(forTextStyle: .body, compatibleWith: UITraitCollection(preferredContentSizeCategory: $0)).pointSize }
        XCTAssertLessThan(sizes[0], sizes[sizes.count - 1])
        for index in 1..<sizes.count { XCTAssertGreaterThanOrEqual(sizes[index], sizes[index - 1]) }
    }
}

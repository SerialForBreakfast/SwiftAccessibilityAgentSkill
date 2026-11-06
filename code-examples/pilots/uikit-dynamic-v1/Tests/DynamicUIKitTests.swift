import XCTest
import UIKit
@testable import AccessibilityExamples

final class DynamicUIKitTests: XCTestCase {
    @MainActor private func search(_ view: DynamicSections, from: UILabel?, direction: UIAccessibilityCustomRotor.Direction = .next) -> UIAccessibilityCustomRotorItemResult? {
        let predicate = UIAccessibilityCustomRotorSearchPredicate()
        if let from { predicate.currentItem = UIAccessibilityCustomRotorItemResult(targetElement: from, targetRange: nil) }
        predicate.searchDirection = direction
        return view.accessibilityCustomRotors?.first?.itemSearchBlock(predicate)
    }
    private var records: [SectionRecord] { [.init(id: "a", title: "Alpha"), .init(id: "b", title: "Beta"), .init(id: "c", title: "Gamma")] }

    @MainActor func testRotorInsertAndInitialSearch() {
        let view = DynamicSections(frame: .zero)
        XCTAssertTrue(view.replace(records))
        XCTAssertTrue(search(view, from: nil)?.targetElement === view.labels[0])
        XCTAssertTrue(search(view, from: nil, direction: .previous)?.targetElement === view.labels[2])
    }
    @MainActor func testReorderPreservesIdentityAndChangesSearchOrder() {
        let view = DynamicSections(frame: .zero)
        view.replace(records)
        let a = view.labels[0], b = view.labels[1], c = view.labels[2]
        view.replace([records[2], records[0], records[1]])
        XCTAssertTrue(view.labels[0] === c)
        XCTAssertTrue(view.labels[1] === a)
        XCTAssertTrue(search(view, from: c)?.targetElement === a)
        XCTAssertTrue(search(view, from: a)?.targetElement === b)
        XCTAssertTrue((view.accessibilityElements as? [UIView])?.first === c)
    }
    @MainActor func testRemovedCurrentItemUsesDeclaredBoundaryPolicy() {
        let view = DynamicSections(frame: .zero)
        view.replace(records)
        let old = view.labels[1]
        view.replace([records[0], records[2]])
        XCTAssertNil(old.superview)
        XCTAssertTrue(search(view, from: old)?.targetElement === view.labels[0])
        XCTAssertTrue(search(view, from: old, direction: .previous)?.targetElement === view.labels[1])
    }
    @MainActor func testEmptyReplacementClearsOrdinaryAndRotorContent() {
        let view = DynamicSections(frame: .zero)
        view.replace(records)
        view.replace([])
        XCTAssertTrue(view.labels.isEmpty)
        XCTAssertTrue(view.subviews.isEmpty)
        XCTAssertEqual(view.accessibilityElements?.count, 0)
        XCTAssertNil(search(view, from: nil))
    }
    @MainActor func testDuplicateIDsRejectWithoutPartialMutation() {
        let view = DynamicSections(frame: .zero)
        view.replace(records)
        let original = view.labels
        XCTAssertFalse(view.replace([records[0], records[0]]))
        XCTAssertEqual(view.labels.count, original.count)
        XCTAssertTrue(zip(view.labels, original).allSatisfy { $0 === $1 })
    }
    @MainActor func testRetitleUpdatesExistingElementWithoutLosingHeader() {
        let view = DynamicSections(frame: .zero)
        view.replace(records)
        let original = view.labels[0]
        view.replace([.init(id: "a", title: "Updated")])
        XCTAssertTrue(view.labels[0] === original)
        XCTAssertEqual(original.text, "Updated")
        XCTAssertEqual(original.accessibilityLabel, "Updated")
        XCTAssertTrue(original.accessibilityTraits.contains(.header))
    }
    @MainActor func testRemovedElementIsNotRetainedByIndexOrContainer() {
        let view = DynamicSections(frame: .zero)
        weak var removed: UILabel?
        // Observe persistent ownership after temporary Objective-C references drain.
        autoreleasepool {
            view.replace(records)
            removed = view.labels[0]
            view.replace([records[1]])
        }
        XCTAssertNil(removed)
    }
    @MainActor func testCustomActionsAreIndependentAndNamed() throws {
        var events: [String] = []
        let view = ReusableMessageActions { events.append($0 + ":" + $1.rawValue) }
        view.configure(id: "a", title: "Alpha", enabled: true)
        let actions = try XCTUnwrap(view.summary.accessibilityCustomActions)
        XCTAssertEqual(actions.map(\.name), ["Archive Alpha", "Delete Alpha"])
        XCTAssertEqual(actions[0].actionHandler?(actions[0]), true)
        XCTAssertEqual(actions[1].actionHandler?(actions[1]), true)
        XCTAssertEqual(events, ["a:archive", "a:delete"])
    }
    @MainActor func testOrdinaryButtonsUseCurrentItemAfterReuse() {
        var events: [String] = []
        let view = ReusableMessageActions { events.append($0 + ":" + $1.rawValue) }
        view.configure(id: "a", title: "Alpha", enabled: true)
        view.configure(id: "b", title: "Beta", enabled: true)
        view.archiveButton.sendActions(for: .touchUpInside)
        view.deleteButton.sendActions(for: .touchUpInside)
        XCTAssertEqual(events, ["b:archive", "b:delete"])
        XCTAssertEqual(view.archiveButton.accessibilityLabel, "Archive Beta")
        XCTAssertEqual(view.deleteButton.accessibilityLabel, "Delete Beta")
        XCTAssertFalse(view.isAccessibilityElement)
        XCTAssertFalse(view.accessibilityElementsHidden)
    }
    @MainActor func testRetainedOldActionCannotAffectReusedView() throws {
        var events: [String] = []
        let view = ReusableMessageActions { events.append($0 + ":" + $1.rawValue) }
        view.configure(id: "a", title: "Alpha", enabled: true)
        let old = try XCTUnwrap(view.summary.accessibilityCustomActions?.first)
        view.configure(id: "b", title: "Beta", enabled: true)
        XCTAssertEqual(old.actionHandler?(old), false)
        XCTAssertTrue(events.isEmpty)
    }
    @MainActor func testDisableAndReenableRefreshesBothActionPaths() throws {
        var count = 0
        let view = ReusableMessageActions { _, _ in count += 1 }
        view.configure(id: "a", title: "Alpha", enabled: false)
        let action = try XCTUnwrap(view.summary.accessibilityCustomActions?.first)
        XCTAssertFalse(view.archiveButton.isEnabled)
        XCTAssertFalse(view.deleteButton.isEnabled)
        XCTAssertEqual(action.actionHandler?(action), false)
        view.archiveButton.sendActions(for: .touchUpInside)
        XCTAssertEqual(count, 0)
        view.configure(id: "a", title: "Alpha", enabled: true)
        XCTAssertTrue(view.archiveButton.isEnabled)
        view.archiveButton.sendActions(for: .touchUpInside)
        XCTAssertEqual(count, 1)
    }
    @MainActor func testRetainedCustomActionDoesNotKeepViewAlive() throws {
        var view: ReusableMessageActions? = ReusableMessageActions { _, _ in }
        view?.configure(id: "a", title: "Alpha", enabled: true)
        weak var weakView = view
        let action = try XCTUnwrap(view?.summary.accessibilityCustomActions?.first)
        view = nil
        XCTAssertNil(weakView)
        XCTAssertEqual(action.actionHandler?(action), false)
    }
    @MainActor func testNativeControlFlagsAndSynthesizedState() {
        let button = UIButton(type: .system)
        XCTAssertTrue(button.isEnabled)
        XCTAssertFalse(button.isSelected)
        button.isEnabled = false
        button.isSelected = true
        XCTAssertTrue(button.state.contains(.disabled))
        XCTAssertTrue(button.state.contains(.selected))
        button.isEnabled = true
        button.isSelected = false
        XCTAssertFalse(button.state.contains(.disabled))
        XCTAssertFalse(button.state.contains(.selected))
    }
    @MainActor func testNativeActionIdentifierReplacesPreviousHandler() {
        let control = UIControl(), identifier = UIAction.Identifier("update")
        var events: [String] = []
        control.addAction(UIAction(identifier: identifier) { _ in events.append("old") }, for: .valueChanged)
        control.addAction(UIAction(identifier: identifier) { _ in events.append("new") }, for: .valueChanged)
        control.sendActions(for: .valueChanged)
        XCTAssertEqual(events, ["new"])
    }
    @MainActor func testNativeActionRemovalPreservesOtherIdentifier() {
        let control = UIControl(), first = UIAction.Identifier("first"), second = UIAction.Identifier("second")
        var events: [String] = []
        control.addAction(UIAction(identifier: first) { _ in events.append("first") }, for: .valueChanged)
        control.addAction(UIAction(identifier: second) { _ in events.append("second") }, for: .valueChanged)
        control.removeAction(identifiedBy: first, for: .valueChanged)
        control.sendActions(for: .valueChanged)
        XCTAssertEqual(events, ["second"])
    }
}

import XCTest
import UIKit
@testable import AccessibilityExamples

final class UIKitSemanticsTests: XCTestCase {
    @MainActor func testLabelValueAndHintAreSeparate() {
        let button = UIButton(type: .system)
        SemanticConfiguration.configure(button, selected: true, hint: "Saves for later")
        XCTAssertEqual(button.accessibilityLabel, "Bookmark")
        XCTAssertEqual(button.accessibilityValue, "Saved")
        XCTAssertEqual(button.accessibilityHint, "Saves for later")
    }
    @MainActor func testReconfigurationClearsStaleHintAndValue() {
        let button = UIButton(type: .system)
        SemanticConfiguration.configure(button, selected: true, hint: "Old hint")
        SemanticConfiguration.configure(button, selected: false, hint: nil)
        XCTAssertNil(button.accessibilityHint)
        XCTAssertEqual(button.accessibilityValue, "Not saved")
    }
    @MainActor func testSelectedTraitPreservesOtherTraits() {
        let button = UIButton(type: .system)
        button.accessibilityTraits.insert(.header)
        let original = button.accessibilityTraits
        SemanticConfiguration.configure(button, selected: true, hint: nil)
        XCTAssertEqual(button.accessibilityTraits, original.union(.selected))
        SemanticConfiguration.configure(button, selected: false, hint: nil)
        XCTAssertEqual(button.accessibilityTraits, original.subtracting(.selected))
    }
    @MainActor func testAttributedLabelAndPlainLabelStayLinked() {
        let element = UIAccessibilityElement(accessibilityContainer: UIView())
        element.accessibilityAttributedLabel = NSAttributedString(string: "Total")
        XCTAssertEqual(element.accessibilityLabel, "Total")
        element.accessibilityLabel = "Updated total"
        XCTAssertEqual(element.accessibilityAttributedLabel?.string, "Updated total")
    }
    @MainActor func testAttributedHintAndValueStayLinked() {
        let element = UIView()
        element.accessibilityAttributedHint = NSAttributedString(string: "Opens detail")
        element.accessibilityAttributedValue = NSAttributedString(string: "Pending")
        XCTAssertEqual(element.accessibilityHint, "Opens detail")
        XCTAssertEqual(element.accessibilityValue, "Pending")
        element.accessibilityHint = "Updated hint"
        element.accessibilityValue = "Ready"
        XCTAssertEqual(element.accessibilityAttributedHint?.string, "Updated hint")
        XCTAssertEqual(element.accessibilityAttributedValue?.string, "Ready")
    }
    @MainActor func testUserInputLabelsKeepPrimaryNameFirst() {
        let button = UIButton(type: .system)
        button.accessibilityUserInputLabels = ["Archive", "Save message"]
        XCTAssertEqual(button.accessibilityUserInputLabels, ["Archive", "Save message"])
    }
    @MainActor func testContainerRetainsExplicitOrderAndExposedChildren() {
        let first = UIButton(type: .system), second = UIButton(type: .system)
        let root = SemanticConfiguration.container(children: [second, first])
        XCTAssertFalse(root.isAccessibilityElement)
        XCTAssertFalse(root.accessibilityElementsHidden)
        XCTAssertTrue(root.shouldGroupAccessibilityChildren)
        let elements = root.accessibilityElements as? [UIView]
        XCTAssertEqual(elements?.count, 2)
        XCTAssertTrue(elements?.first === second)
        XCTAssertTrue(elements?.last === first)
        XCTAssertFalse(first.accessibilityElementsHidden)
    }
    @MainActor func testEmptyContainerHasEmptyElementList() {
        let root = SemanticConfiguration.container(children: [])
        XCTAssertEqual(root.accessibilityElements?.count, 0)
    }
    @MainActor func testVirtualElementRetainsContainerAndConfiguration() {
        let container = UIView()
        let element = UIAccessibilityElement(accessibilityContainer: container)
        element.accessibilityLabel = "Chart point"
        element.accessibilityValue = "42"
        element.accessibilityFrameInContainerSpace = CGRect(x: 10, y: 20, width: 30, height: 40)
        XCTAssertTrue(element.accessibilityContainer as? UIView === container)
        XCTAssertEqual(element.accessibilityLabel, "Chart point")
        XCTAssertEqual(element.accessibilityValue, "42")
        XCTAssertEqual(element.accessibilityFrameInContainerSpace, CGRect(x: 10, y: 20, width: 30, height: 40))
    }
    @MainActor func testModalConfigurationDoesNotHideOwnChildren() {
        let child = UIButton(type: .system), root = UIView()
        root.addSubview(child)
        root.accessibilityViewIsModal = true
        XCTAssertTrue(root.accessibilityViewIsModal)
        XCTAssertFalse(root.accessibilityElementsHidden)
        XCTAssertFalse(child.accessibilityElementsHidden)
        root.accessibilityViewIsModal = false
        XCTAssertFalse(root.accessibilityViewIsModal)
    }
    @MainActor func testAdjustableHooksSynchronizeValue() {
        let quantity = AdjustableQuantity(frame: .zero)
        XCTAssertTrue(quantity.accessibilityTraits.contains(.adjustable))
        quantity.accessibilityIncrement()
        XCTAssertEqual(quantity.quantity, 1)
        XCTAssertEqual(quantity.accessibilityValue, "1")
        quantity.accessibilityDecrement()
        XCTAssertEqual(quantity.accessibilityValue, "0")
    }
    @MainActor func testAdjustableBoundsDoNotOverflow() {
        let quantity = AdjustableQuantity(frame: .zero)
        for _ in 0..<10 { quantity.accessibilityDecrement() }
        XCTAssertEqual(quantity.quantity, 0)
        for _ in 0..<10 { quantity.accessibilityIncrement() }
        XCTAssertEqual(quantity.quantity, 3)
        XCTAssertEqual(quantity.accessibilityValue, "3")
    }
    @MainActor func testCustomActionHasNameAndInvokesOneCallback() throws {
        var calls = 0
        let control = ArchiveControl { calls += 1 }
        let action = try XCTUnwrap(control.button.accessibilityCustomActions?.first)
        XCTAssertEqual(action.name, "Archive message")
        XCTAssertEqual(action.actionHandler?(action), true)
        XCTAssertTrue(control.archived)
        XCTAssertEqual(calls, 1)
        XCTAssertEqual(action.actionHandler?(action), false)
        XCTAssertEqual(calls, 1)
    }
    @MainActor func testOrdinaryButtonRemainsAnIndependentPath() {
        var calls = 0
        let control = ArchiveControl { calls += 1 }
        XCTAssertEqual(control.button.title(for: .normal), "Archive")
        XCTAssertFalse(control.isAccessibilityElement)
        XCTAssertFalse(control.accessibilityElementsHidden)
        control.button.sendActions(for: .touchUpInside)
        XCTAssertTrue(control.archived)
        XCTAssertEqual(calls, 1)
    }
    @MainActor func testCustomActionDoesNotRetainOwner() throws {
        var control: ArchiveControl? = ArchiveControl {}
        weak var weakControl = control
        let action = try XCTUnwrap(control?.button.accessibilityCustomActions?.first)
        control = nil
        XCTAssertNil(weakControl)
        XCTAssertEqual(action.actionHandler?(action), false)
    }
    @MainActor private func search(_ root: SectionRotor, from element: NSObject, direction: UIAccessibilityCustomRotor.Direction) -> UIAccessibilityCustomRotorItemResult? {
        let predicate = UIAccessibilityCustomRotorSearchPredicate()
        predicate.currentItem = UIAccessibilityCustomRotorItemResult(targetElement: element, targetRange: nil)
        predicate.searchDirection = direction
        return root.accessibilityCustomRotors?.first?.itemSearchBlock(predicate)
    }
    @MainActor func testRotorNextAndPreviousReturnCorrectIdentity() {
        let root = SectionRotor(names: ["One", "Two", "Three"])
        XCTAssertTrue(search(root, from: root.sections[1], direction: .next)?.targetElement === root.sections[2])
        XCTAssertTrue(search(root, from: root.sections[1], direction: .previous)?.targetElement === root.sections[0])
    }
    @MainActor func testRotorBoundaryPolicyDoesNotWrap() {
        let root = SectionRotor(names: ["One", "Two"])
        XCTAssertNil(search(root, from: root.sections[1], direction: .next))
        XCTAssertNil(search(root, from: root.sections[0], direction: .previous))
    }
    @MainActor func testRotorInitialSearchReturnsFirstOrLast() throws {
        let root = SectionRotor(names: ["One", "Two"])
        let rotor = try XCTUnwrap(root.accessibilityCustomRotors?.first)
        let predicate = UIAccessibilityCustomRotorSearchPredicate()
        predicate.searchDirection = .next
        XCTAssertTrue(rotor.itemSearchBlock(predicate)?.targetElement === root.sections[0])
        predicate.searchDirection = .previous
        XCTAssertTrue(rotor.itemSearchBlock(predicate)?.targetElement === root.sections[1])
    }
    @MainActor func testRotorUnknownAnchorAndEmptyResults() {
        let root = SectionRotor(names: ["One", "Two"]), unknown = NSObject()
        XCTAssertTrue(search(root, from: unknown, direction: .next)?.targetElement === root.sections[0])
        XCTAssertTrue(search(root, from: unknown, direction: .previous)?.targetElement === root.sections[1])
        XCTAssertNil(search(SectionRotor(names: []), from: unknown, direction: .next))
    }
    @MainActor func testRotorKeepsOrdinaryElementsAndHeadingTraits() {
        let root = SectionRotor(names: ["One", "Two"])
        XCTAssertEqual(root.accessibilityCustomRotors?.first?.name, "Sections")
        XCTAssertFalse(root.isAccessibilityElement)
        XCTAssertFalse(root.accessibilityElementsHidden)
        XCTAssertEqual(root.accessibilityElements?.count, 2)
        XCTAssertTrue(root.sections.allSatisfy { $0.accessibilityTraits.contains(.header) })
    }
    @MainActor func testRotorDoesNotRetainOwner() throws {
        var root: SectionRotor? = SectionRotor(names: ["One"])
        weak var weakRoot = root
        let rotor = try XCTUnwrap(root?.accessibilityCustomRotors?.first)
        root = nil
        XCTAssertNil(weakRoot)
        XCTAssertNil(rotor.itemSearchBlock(UIAccessibilityCustomRotorSearchPredicate()))
    }
    @MainActor func testPreferredFontRespondsToExplicitContentSizeTraits() {
        let normal = UITraitCollection(preferredContentSizeCategory: .large)
        let large = UITraitCollection(preferredContentSizeCategory: .accessibilityExtraExtraExtraLarge)
        let a = UIFont.preferredFont(forTextStyle: .body, compatibleWith: normal)
        let b = UIFont.preferredFont(forTextStyle: .body, compatibleWith: large)
        XCTAssertGreaterThan(b.pointSize, a.pointSize)
    }
    @MainActor func testCustomFontMetricsScaleAndRespectMaximum() {
        let traits = UITraitCollection(preferredContentSizeCategory: .accessibilityExtraExtraExtraLarge)
        let base = UIFont.systemFont(ofSize: 17), metrics = UIFontMetrics(forTextStyle: .body)
        let scaled = metrics.scaledFont(for: base, compatibleWith: traits)
        let capped = metrics.scaledFont(for: base, maximumPointSize: 28, compatibleWith: traits)
        XCTAssertGreaterThan(scaled.pointSize, base.pointSize)
        XCTAssertLessThanOrEqual(capped.pointSize, 28)
        XCTAssertEqual(base.pointSize, 17)
    }
}

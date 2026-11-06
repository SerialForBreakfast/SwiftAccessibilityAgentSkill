import XCTest
import UIKit
@testable import AccessibilityExamples

@MainActor
final class ReuseUIKitTests: XCTestCase {
    func testReconfigureReplacesLanguageAndName() {
        let cell = SavedItemCell()
        cell.configure(id: "1", title: "Bonjour", saved: false, removable: true, language: "fr-FR")
        cell.configure(id: "2", title: "Hello", saved: false, removable: false, language: "en-US")
        XCTAssertEqual(cell.titleLabel.text, "Hello")
        XCTAssertEqual(cell.accessibilityLabel, "Hello")
        XCTAssertEqual(cell.accessibilityAttributedLabel?.attribute(.accessibilitySpeechLanguage, at: 0, effectiveRange: nil) as? String, "en-US")
    }

    func testReconfigureClearsSelectedStateWithoutLosingOtherTraits() {
        let cell = SavedItemCell()
        cell.accessibilityTraits.insert(.updatesFrequently)
        cell.configure(id: "1", title: "First", saved: true, removable: true, language: "en")
        XCTAssertTrue(cell.accessibilityTraits.contains(.selected))
        XCTAssertEqual(cell.accessibilityValue, "Saved")
        cell.configure(id: "2", title: "Second", saved: false, removable: false, language: "en")
        XCTAssertFalse(cell.accessibilityTraits.contains(.selected))
        XCTAssertTrue(cell.accessibilityTraits.contains(.updatesFrequently))
        XCTAssertEqual(cell.accessibilityValue, "Not saved")
        XCTAssertNil(cell.accessibilityHint)
        XCTAssertEqual(cell.accessibilityCustomActions?.count, 0)
    }

    func testRetainedActionRejectsReconfiguredIdentity() {
        let cell = SavedItemCell()
        var removed: [String] = []
        cell.onRemove = { removed.append($0) }
        cell.configure(id: "old", title: "Old", saved: true, removable: true, language: "en")
        let old = cell.accessibilityCustomActions![0]
        cell.configure(id: "new", title: "New", saved: true, removable: true, language: "en")
        XCTAssertFalse(old.actionHandler!(old))
        let current = cell.accessibilityCustomActions![0]
        XCTAssertTrue(current.actionHandler!(current))
        XCTAssertEqual(removed, ["new"])
    }

    func testPrepareForReuseClearsMetadataAndCallback() {
        let cell = SavedItemCell()
        cell.configure(id: "1", title: "First", saved: true, removable: true, language: "en")
        var calls = 0
        cell.onRemove = { _ in calls += 1 }
        let action = cell.accessibilityCustomActions![0]
        cell.prepareForReuse()
        XCTAssertNil(cell.titleLabel.text)
        XCTAssertNil(cell.accessibilityAttributedLabel)
        XCTAssertNil(cell.accessibilityValue)
        XCTAssertNil(cell.accessibilityHint)
        XCTAssertEqual(cell.accessibilityCustomActions?.count, 0)
        XCTAssertFalse(cell.accessibilityTraits.contains(.selected))
        XCTAssertNil(cell.onRemove)
        XCTAssertFalse(action.actionHandler!(action))
        XCTAssertEqual(calls, 0)
    }

    func testNewConfigurationAfterReuseUsesNewCallback() {
        let cell = SavedItemCell()
        cell.configure(id: "old", title: "Old", saved: false, removable: true, language: "en")
        cell.prepareForReuse()
        var removed: [String] = []
        cell.onRemove = { removed.append($0) }
        cell.configure(id: "new", title: "New", saved: false, removable: true, language: "en")
        let action = cell.accessibilityCustomActions![0]
        XCTAssertTrue(action.actionHandler!(action))
        XCTAssertEqual(removed, ["new"])
    }

    func testMissingHandlerReturnsFalse() {
        let cell = SavedItemCell()
        cell.configure(id: "1", title: "First", saved: false, removable: true, language: "en")
        let action = cell.accessibilityCustomActions![0]
        XCTAssertFalse(action.actionHandler!(action))
    }

    func testHeaderRoleTransitionPreservesOtherTraits() {
        let header = UILabel()
        header.accessibilityTraits.insert(.updatesFrequently)
        SectionConfiguration.configure(header, title: "Saved", isHeading: true)
        XCTAssertTrue(header.accessibilityTraits.contains(.header))
        SectionConfiguration.configure(header, title: "Summary", isHeading: false)
        XCTAssertFalse(header.accessibilityTraits.contains(.header))
        XCTAssertTrue(header.accessibilityTraits.contains(.updatesFrequently))
        XCTAssertEqual(header.accessibilityLabel, "Summary")
    }

    func testNestedSectionKeepsHeaderAndListSeparate() {
        let header = UILabel(), row = UIButton(type: .system)
        let section = SectionConfiguration.nested(header: header, rows: [row])
        XCTAssertFalse(section.isAccessibilityElement)
        XCTAssertEqual(section.accessibilityContainerType, .semanticGroup)
        XCTAssertEqual(section.accessibilityElements?.count, 2)
        XCTAssertTrue((section.accessibilityElements?[0] as? UILabel) === header)
        let list = section.accessibilityElements?[1] as? UIView
        XCTAssertEqual(list?.accessibilityContainerType, .list)
        XCTAssertEqual(list?.isAccessibilityElement, false)
        XCTAssertEqual(list?.accessibilityElements?.count, 1)
        XCTAssertTrue((list?.accessibilityElements?[0] as? UIButton) === row)
    }

    func testTypographyReconfigurationReplacesStyleAndSizePolicy() {
        let label = UILabel()
        for style: UIFont.TextStyle in [.headline, .caption1, .body] {
            for category: UIContentSizeCategory in [.large, .accessibilityExtraExtraExtraLarge, .small] {
                label.traitOverrides.preferredContentSizeCategory = category
                label.updateTraitsIfNeeded()
                let traits = label.traitCollection
                XCTAssertEqual(traits.preferredContentSizeCategory, category)
                label.numberOfLines = 1
                label.adjustsFontForContentSizeCategory = false
                ReusableTypography.configure(label, style: style)
                XCTAssertEqual(label.font.pointSize, UIFont.preferredFont(forTextStyle: style, compatibleWith: traits).pointSize)
                XCTAssertEqual(label.font.fontDescriptor.object(forKey: .textStyle) as? String, style.rawValue)
                XCTAssertTrue(label.adjustsFontForContentSizeCategory)
                XCTAssertEqual(label.numberOfLines, 0)
            }
        }
    }

    func testLayoutUpdatePreservesTargetIdentity() {
        let target = UIButton(type: .system)
        var calls = 0
        AccessibilityUpdate.layout(target: target).deliver { notification, argument in
            calls += 1
            XCTAssertEqual(notification, .layoutChanged)
            XCTAssertTrue((argument as? UIButton) === target)
        }
        XCTAssertEqual(calls, 1)
    }

    func testScreenUpdateAllowsNoTarget() {
        var calls = 0
        AccessibilityUpdate.screen(target: nil).deliver { notification, argument in
            calls += 1
            XCTAssertEqual(notification, .screenChanged)
            XCTAssertNil(argument)
        }
        XCTAssertEqual(calls, 1)
    }
}

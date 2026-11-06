import XCTest
import UIKit
@testable import AccessibilityExamples

@MainActor
final class ChoiceUIKitTests: XCTestCase {
    private func cell() -> AccessibleChoiceCell {
        AccessibleChoiceCell(style: .default, reuseIdentifier: "choice")
    }

    private func configure(_ cell: AccessibleChoiceCell, name: String = "Evening delivery", chosen: Bool = false) {
        cell.configure(name: name, chosen: chosen, selectedText: "Selected", unselectedText: "Not selected")
    }

    private func setSize(_ cell: AccessibleChoiceCell, _ size: UIContentSizeCategory) {
        for label in [cell.nameLabel, cell.stateLabel] {
            label.traitOverrides.preferredContentSizeCategory = size
            label.updateTraitsIfNeeded()
            XCTAssertEqual(label.traitCollection.preferredContentSizeCategory, size)
        }
    }

    func testLongLocalizedContentRemainsVerbatim() {
        let row = cell()
        let name = String(repeating: "Livraison du soir avec instructions detaillees. ", count: 12)
        setSize(row, .accessibilityExtraExtraExtraLarge)
        row.configure(name: name, chosen: true, selectedText: "Selectionnee", unselectedText: "Non selectionnee")
        XCTAssertEqual(row.nameLabel.text, name)
        XCTAssertEqual(row.accessibilityLabel, name)
        XCTAssertEqual(row.stateLabel.text, "Selectionnee")
        XCTAssertEqual(row.accessibilityValue, "Selectionnee")
    }

    func testMultilinePolicyReplacesShrinkToFit() {
        let row = cell()
        for label in [row.nameLabel, row.stateLabel] {
            label.numberOfLines = 1
            label.adjustsFontSizeToFitWidth = true
        }
        configure(row)
        for label in [row.nameLabel, row.stateLabel] {
            XCTAssertEqual(label.numberOfLines, 0)
            XCTAssertEqual(label.lineBreakMode, .byWordWrapping)
            XCTAssertFalse(label.adjustsFontSizeToFitWidth)
            XCTAssertTrue(label.adjustsFontForContentSizeCategory)
        }
    }

    func testFontsMatchEffectiveLargeTextEnvironment() {
        let row = cell()
        setSize(row, .accessibilityExtraExtraExtraLarge)
        configure(row)
        for label in [row.nameLabel, row.stateLabel] {
            let expected = UIFont.preferredFont(forTextStyle: .body, compatibleWith: label.traitCollection)
            XCTAssertEqual(label.font.pointSize, expected.pointSize, accuracy: 0.01)
            XCTAssertEqual(label.font.fontDescriptor.object(forKey: .textStyle) as? String, UIFont.TextStyle.body.rawValue)
        }
    }

    func testRepeatedSizeTransitionsDoNotAccumulateScaling() {
        let row = cell()
        for size: UIContentSizeCategory in [.large, .accessibilityExtraExtraExtraLarge, .small, .large] {
            setSize(row, size)
            configure(row)
            configure(row)
            for label in [row.nameLabel, row.stateLabel] {
                XCTAssertEqual(label.font.pointSize,
                               UIFont.preferredFont(forTextStyle: .body, compatibleWith: label.traitCollection).pointSize,
                               accuracy: 0.01)
            }
        }
    }

    func testSelectedStateHasTextSymbolAndMetadata() {
        let row = cell()
        configure(row, chosen: true)
        XCTAssertEqual(row.stateLabel.text, "Selected")
        XCTAssertEqual(row.accessibilityValue, "Selected")
        XCTAssertEqual(row.accessoryType, .checkmark)
        XCTAssertTrue(row.accessibilityTraits.contains(.selected))
    }

    func testDeselectionClearsEveryOwnedSelectionCue() {
        let row = cell()
        configure(row, chosen: true)
        configure(row, chosen: false)
        XCTAssertEqual(row.stateLabel.text, "Not selected")
        XCTAssertEqual(row.accessibilityValue, "Not selected")
        XCTAssertEqual(row.accessoryType, .none)
        XCTAssertFalse(row.accessibilityTraits.contains(.selected))
    }

    func testSelectionUpdatesPreserveUnrelatedTraits() {
        let row = cell()
        row.accessibilityTraits.insert(.updatesFrequently)
        for chosen in [true, false, true] {
            configure(row, chosen: chosen)
            XCTAssertTrue(row.accessibilityTraits.contains(.updatesFrequently))
            XCTAssertEqual(row.accessibilityTraits.contains(.selected), chosen)
        }
    }

    func testSameInstanceCanChangeNameAndSelectionWithoutReuse() {
        let row = cell()
        configure(row, name: "Evening", chosen: true)
        configure(row, name: "Morning", chosen: false)
        XCTAssertEqual(row.nameLabel.text, "Morning")
        XCTAssertEqual(row.accessibilityLabel, "Morning")
        XCTAssertEqual(row.accessibilityValue, "Not selected")
        XCTAssertFalse(row.accessibilityTraits.contains(.selected))
        XCTAssertTrue(row.isAccessibilityElement)
        XCTAssertFalse(row.nameLabel.isAccessibilityElement)
        XCTAssertFalse(row.stateLabel.isAccessibilityElement)
    }

    func testSelfSizingConfigurationAndVerticalConstraintChain() {
        let row = cell(), table = UITableView()
        table.rowHeight = 44
        AccessibleChoiceCell.configureSizing(table)
        XCTAssertEqual(table.rowHeight, UITableView.automaticDimension)
        XCTAssertGreaterThan(table.estimatedRowHeight, 0)
        XCTAssertEqual(row.textStack.axis, .vertical)
        let edges = row.contentView.constraints.filter {
            $0.isActive && ($0.firstItem as? UIView) === row.textStack &&
            ($0.secondItem as? UIView) === row.contentView && $0.relation == .equal
        }
        XCTAssertEqual(edges.filter { $0.firstAttribute == .top && $0.secondAttribute == .top }.count, 1)
        XCTAssertEqual(edges.filter { $0.firstAttribute == .bottom && $0.secondAttribute == .bottom }.count, 1)
        for view in [row, row.contentView, row.textStack, row.nameLabel, row.stateLabel] {
            let fixedHeights = view.constraints.filter {
                $0.isActive && $0.firstAttribute == .height && $0.relation == .equal && $0.secondItem == nil
            }
            XCTAssertTrue(fixedHeights.isEmpty)
        }
    }
}

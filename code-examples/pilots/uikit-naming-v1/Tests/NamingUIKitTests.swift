import XCTest
import UIKit
@testable import AccessibilityExamples

@MainActor
final class NamingUIKitTests: XCTestCase {
    private func configure(_ card: ItemActionCard, item: String = "Invoice A",
                           onOpen: @escaping () -> Void = {}, onSave: @escaping () -> Void = {}) {
        card.configure(title: item, openTitle: "Open", saveTitle: "Save",
                       openName: "Open \(item)", saveName: "Save \(item)",
                       onOpen: onOpen, onSave: onSave)
    }

    func testDecorationIsExplicitlyExcluded() {
        let card = ItemActionCard()
        card.decoration.isAccessibilityElement = true
        configure(card)
        XCTAssertFalse(card.decoration.isAccessibilityElement)
        XCTAssertTrue(card.titleLabel.isAccessibilityElement)
    }

    func testContainerPreservesIndependentControls() {
        let card = ItemActionCard()
        configure(card)
        XCTAssertFalse(card.isAccessibilityElement)
        XCTAssertFalse(card.accessibilityElementsHidden)
        XCTAssertTrue(card.openButton.isAccessibilityElement)
        XCTAssertTrue(card.saveButton.isAccessibilityElement)
        XCTAssertTrue(card.openButton.superview === card)
        XCTAssertTrue(card.saveButton.superview === card)
    }

    func testRepeatedVisibleTitlesHaveContextualNames() {
        let first = ItemActionCard(), second = ItemActionCard()
        configure(first)
        configure(second, item: "Invoice B")
        XCTAssertEqual(first.openButton.title(for: .normal), second.openButton.title(for: .normal))
        XCTAssertEqual(first.openButton.accessibilityLabel, "Open Invoice A")
        XCTAssertEqual(second.openButton.accessibilityLabel, "Open Invoice B")
        XCTAssertEqual(first.saveButton.accessibilityLabel, "Save Invoice A")
        XCTAssertEqual(second.saveButton.accessibilityLabel, "Save Invoice B")
    }

    func testReconfigurationReplacesNamesWithoutReuseCallback() {
        let card = ItemActionCard()
        configure(card)
        configure(card, item: "Invoice B")
        XCTAssertEqual(card.titleLabel.text, "Invoice B")
        XCTAssertEqual(card.openButton.accessibilityLabel, "Open Invoice B")
        XCTAssertEqual(card.saveButton.accessibilityLabel, "Save Invoice B")
        configure(card)
        XCTAssertEqual(card.openButton.accessibilityLabel, "Open Invoice A")
    }

    func testCompleteLocalizedNamesArePreserved() {
        let card = ItemActionCard()
        card.configure(title: "Facture A", openTitle: "Ouvrir", saveTitle: "Enregistrer",
                       openName: "Ouvrir la facture A", saveName: "Enregistrer la facture A",
                       onOpen: {}, onSave: {})
        XCTAssertEqual(card.openButton.accessibilityLabel, "Ouvrir la facture A")
        XCTAssertEqual(card.saveButton.accessibilityLabel, "Enregistrer la facture A")
        XCTAssertEqual(card.openButton.title(for: .normal), "Ouvrir")
    }

    func testOrdinaryActionsRemainIndependent() {
        let card = ItemActionCard()
        var opened = 0, saved = 0
        configure(card, onOpen: { opened += 1 }, onSave: { saved += 1 })
        card.openButton.sendActions(for: .touchUpInside)
        XCTAssertEqual(opened, 1)
        XCTAssertEqual(saved, 0)
        card.saveButton.sendActions(for: .touchUpInside)
        XCTAssertEqual(opened, 1)
        XCTAssertEqual(saved, 1)
    }

    func testReconfigurationReplacesHandlersWithoutDuplicates() {
        let card = ItemActionCard()
        var old = 0, current = 0
        configure(card, onOpen: { old += 1 })
        for _ in 0..<3 { configure(card, item: "Invoice B", onOpen: { current += 1 }) }
        card.openButton.sendActions(for: .touchUpInside)
        XCTAssertEqual(old, 0)
        XCTAssertEqual(current, 1)
    }

    func testReconfigurationResetsOwnedContainerState() {
        let card = ItemActionCard()
        configure(card)
        card.isAccessibilityElement = true
        card.accessibilityElementsHidden = true
        card.titleLabel.accessibilityLabel = "Stale"
        configure(card, item: "Invoice B")
        XCTAssertFalse(card.isAccessibilityElement)
        XCTAssertFalse(card.accessibilityElementsHidden)
        XCTAssertEqual(card.titleLabel.text, "Invoice B")
        // UILabel may derive a label from text; this check only rejects our stale override.
        XCTAssertNotEqual(card.titleLabel.accessibilityLabel, "Stale")
    }
}

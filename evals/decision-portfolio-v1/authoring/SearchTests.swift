import AppKit
import XCTest
@testable import Feature

@MainActor final class RecipientTests: XCTestCase {
    func testNativeSearchFieldAllowsSelection() {
        let field = RecipientField.makeField()
        XCTAssertTrue(field.isEditable && field.isSelectable)
        XCTAssertEqual(field.accessibilityLabel(), "Recipient")
    }
}

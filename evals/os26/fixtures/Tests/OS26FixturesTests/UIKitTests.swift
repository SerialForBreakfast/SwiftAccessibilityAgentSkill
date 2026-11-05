#if os(iOS)
import XCTest
import UIKit
@testable import OS26Fixtures
final class UIKitTests: XCTestCase {
    @MainActor func testSettingsCallbacksAndExposedControls() {
        var changes: [Bool] = []; var helpCount = 0
        let row = SettingsRow(onChange: { changes.append($0) }, onHelp: { helpCount += 1 })
        XCTAssertFalse(row.isAccessibilityElement)
        XCTAssertFalse(row.accessibilityElementsHidden)
        XCTAssertTrue(row.helpButton.isEnabled)
        row.downloadSwitch.isOn = true
        row.downloadSwitch.sendActions(for: .valueChanged)
        row.downloadSwitch.isOn = false
        row.downloadSwitch.sendActions(for: .valueChanged)
        row.helpButton.sendActions(for: .touchUpInside)
        XCTAssertEqual(changes, [true, false]); XCTAssertEqual(helpCount, 1)
    }
    @MainActor func testReconfigurationWithoutPrepareForReuse() {
        let cell = OrderCell(style: .default, reuseIdentifier: "order")
        let a = Order(customer: "Alice", status: "Shipped", isPriority: true)
        let b = Order(customer: "Bob", status: "Processing", isPriority: false)
        for order in [a, b, a, b] {
            cell.configure(order)
            let expected = order.isPriority ? "Priority order for Alice" : "Bob"
            XCTAssertEqual(cell.accessibilityLabel, expected)
            XCTAssertEqual(cell.accessibilityValue, order.status)
            XCTAssertEqual(cell.titleLabel.text, order.customer)
        }
    }
    @MainActor func testCheckoutCallbackAndResizePrerequisites() {
        var payments = 0
        let summary = CheckoutSummary(formattedTotal: "1.234.567,89 EUR", onPay: { payments += 1 })
        XCTAssertTrue(summary.totalLabel.adjustsFontForContentSizeCategory)
        XCTAssertEqual(summary.totalLabel.numberOfLines, 0)
        XCTAssertFalse(summary.constraints.contains { $0.isActive && $0.firstAttribute == .height && $0.relation == .equal && $0.secondItem == nil })
        XCTAssertEqual(summary.payButton.title(for: .normal), "Pay now")
        summary.payButton.sendActions(for: .touchUpInside)
        XCTAssertEqual(payments, 1)
        // These prerequisites do not establish actual layout at accessibility sizes.
    }
}
#endif

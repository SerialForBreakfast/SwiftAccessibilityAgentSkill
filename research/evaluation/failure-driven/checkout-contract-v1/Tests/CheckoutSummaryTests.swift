import UIKit
import XCTest
@testable import AccessibilityExamples

@MainActor
final class CheckoutSummaryTests: XCTestCase {
    func testPreservesExistingButtonIdentityTypographyAndTitle() throws {
        let button = UIButton(type: .system)
        button.setTitle("Pay securely", for: .normal)
        let title = try XCTUnwrap(button.titleLabel)
        title.font = .systemFont(ofSize: 19, weight: .semibold)
        title.adjustsFontForContentSizeCategory = false
        let descriptor = try XCTUnwrap(title.font).fontDescriptor
        let summary = CheckoutSummary(payButton: button)
        summary.update(total: "USD 1,234,567.89")
        XCTAssertTrue(summary.payButton === button)
        XCTAssertTrue(title.font.fontDescriptor.isEqual(descriptor))
        XCTAssertFalse(title.adjustsFontForContentSizeCategory)
        XCTAssertEqual(button.title(for: .normal), "Pay securely")
    }

    func testRepeatedUpdatesPreserveExistingActionExactlyOnce() {
        let button = UIButton(type: .system)
        var calls = 0
        button.addAction(UIAction { _ in calls += 1 }, for: .primaryActionTriggered)
        let summary = CheckoutSummary(payButton: button)
        for total in ["USD 0.00", "USD 123,456,789.00", "EUR 9,876.54"] {
            summary.update(total: total)
        }
        XCTAssertEqual(calls, 0)
        summary.payButton.sendActions(for: .primaryActionTriggered)
        XCTAssertEqual(calls, 1)
        summary.update(total: "USD 5.00")
        XCTAssertEqual(calls, 1)
        summary.payButton.sendActions(for: .primaryActionTriggered)
        XCTAssertEqual(calls, 2)
        XCTAssertEqual(summary.arrangedSubviews.count, 2)
    }

    func testFlexibleTextConfigurationAndNoFixedEnclosingHeight() {
        let summary = CheckoutSummary(payButton: UIButton(type: .system))
        summary.update(total: "USD 123,456,789,012.34")
        XCTAssertEqual(summary.totalLabel.text, "USD 123,456,789,012.34")
        XCTAssertEqual(summary.totalLabel.numberOfLines, 0)
        XCTAssertTrue(summary.totalLabel.adjustsFontForContentSizeCategory)
        XCTAssertNotNil(summary.totalLabel.font.fontDescriptor.object(forKey: .textStyle))
        XCTAssertFalse(summary.totalLabel.adjustsFontSizeToFitWidth)
        XCTAssertFalse(summary.constraints.contains {
            $0.isActive && $0.firstAttribute == .height && $0.relation == .equal && $0.secondItem == nil
        })
    }

    func testPreservesConfiguredButtonAndDisabledState() {
        let button = UIButton(type: .system)
        var configuration = UIButton.Configuration.filled()
        configuration.title = "Buy now"
        configuration.subtitle = "Secure checkout"
        configuration.buttonSize = .large
        configuration.cornerStyle = .capsule
        configuration.baseBackgroundColor = .systemOrange
        button.configuration = configuration
        button.isEnabled = false
        let summary = CheckoutSummary(payButton: button)
        summary.update(total: "USD 42.00")
        XCTAssertEqual(button.configuration?.title, configuration.title)
        XCTAssertEqual(button.configuration?.subtitle, configuration.subtitle)
        XCTAssertEqual(button.configuration?.buttonSize, configuration.buttonSize)
        XCTAssertEqual(button.configuration?.cornerStyle, configuration.cornerStyle)
        XCTAssertEqual(button.configuration?.baseBackgroundColor, configuration.baseBackgroundColor)
        XCTAssertFalse(button.isEnabled)
    }

    func testRetainedButtonDoesNotRetainSummary() {
        let button = UIButton(type: .system)
        weak var released: CheckoutSummary?
        autoreleasepool {
            let summary = CheckoutSummary(payButton: button)
            released = summary
            summary.update(total: "USD 1.00")
            XCTAssertNotNil(released)
        }
        XCTAssertNil(released)
    }
}

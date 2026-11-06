import XCTest
import UIKit
@testable import AccessibilityExamples

@MainActor
final class PreferenceUIKitTests: XCTestCase {
    func testReducedMotionUsesImmediateTransition() {
        XCTAssertEqual(MotionPolicy.duration(reduceMotion: true), 0)
    }

    func testOrdinaryMotionUsesBoundedDuration() {
        XCTAssertEqual(MotionPolicy.duration(reduceMotion: false), 0.25)
    }

    func testLivePreferenceMatchesPolicy() {
        XCTAssertEqual(MotionPolicy.currentDuration(), MotionPolicy.duration(reduceMotion: UIAccessibility.isReduceMotionEnabled))
    }

    func testErrorHasTextCueAndAccessibleName() {
        let view = ValidationStatus()
        view.configure(error: "Email is required")
        XCTAssertEqual(view.message.text, "Error: Email is required")
        XCTAssertEqual(view.message.accessibilityLabel, view.message.text)
        XCTAssertFalse(view.submit.isEnabled)
        XCTAssertEqual(view.submit.accessibilityHint, "Correct the error before submitting: Email is required")
    }

    func testRecoveryRemovesStaleErrorAndHint() {
        let view = ValidationStatus()
        view.configure(error: "Email is required")
        view.configure(error: nil)
        XCTAssertEqual(view.message.text, "Ready to submit")
        XCTAssertEqual(view.message.accessibilityLabel, "Ready to submit")
        XCTAssertTrue(view.submit.isEnabled)
        XCTAssertNil(view.submit.accessibilityHint)
    }

    func testReplacementErrorReplacesAllMetadata() {
        let view = ValidationStatus()
        view.configure(error: "Email is required")
        view.configure(error: "Address is incomplete")
        XCTAssertEqual(view.message.accessibilityLabel, "Error: Address is incomplete")
        XCTAssertEqual(view.submit.accessibilityHint, "Correct the error before submitting: Address is incomplete")
    }

    func testSemanticColorsResolveForExplicitAppearanceAndContrast() {
        let view = ValidationStatus()
        for style: UIUserInterfaceStyle in [.light, .dark] {
            for contrast: UIAccessibilityContrast in [.normal, .high] {
                let traits = UITraitCollection(traitsFrom: [UITraitCollection(userInterfaceStyle: style), UITraitCollection(accessibilityContrast: contrast)])
                XCTAssertEqual(view.message.textColor.resolvedColor(with: traits), UIColor.label.resolvedColor(with: traits))
                XCTAssertEqual(view.backgroundColor?.resolvedColor(with: traits), UIColor.systemBackground.resolvedColor(with: traits))
            }
        }
    }

    func testBorderReresolvesWhenAppearanceChanges() {
        let view = ValidationStatus()
        for style: UIUserInterfaceStyle in [.light, .dark, .light] {
            let traits = UITraitCollection(userInterfaceStyle: style)
            view.updateBorder(for: traits)
            XCTAssertEqual(view.layer.borderColor, UIColor.label.resolvedColor(with: traits).cgColor)
        }
    }
}

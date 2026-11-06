import XCTest
import UIKit
@testable import AccessibilityExamples

@MainActor
final class ContrastUIKitTests: XCTestCase {
    private func gray(_ value: Double) throws -> OpaqueSRGB {
        try OpaqueSRGB(red: value, green: value, blue: value)
    }

    private func traits(_ style: UIUserInterfaceStyle, _ contrast: UIAccessibilityContrast = .normal) -> UITraitCollection {
        UITraitCollection(traitsFrom: [UITraitCollection(userInterfaceStyle: style),
                                      UITraitCollection(accessibilityContrast: contrast)])
    }

    func testBlackWhiteAndIdenticalRatios() throws {
        let black = try gray(0), white = try gray(1)
        XCTAssertEqual(black.contrast(with: white), 21, accuracy: 1e-12)
        XCTAssertEqual(white.contrast(with: black), 21, accuracy: 1e-12)
        XCTAssertEqual(try gray(0.5).contrast(with: gray(0.5)), 1, accuracy: 1e-12)
    }

    func testPublishedLuminanceWeightsAndTransferBranches() throws {
        XCTAssertEqual(try OpaqueSRGB(red: 1, green: 0, blue: 0).luminance, 0.2126, accuracy: 1e-12)
        XCTAssertEqual(try OpaqueSRGB(red: 0, green: 1, blue: 0).luminance, 0.7152, accuracy: 1e-12)
        XCTAssertEqual(try OpaqueSRGB(red: 0, green: 0, blue: 1).luminance, 0.0722, accuracy: 1e-12)
        XCTAssertEqual(try gray(0.04).luminance, 0.0030959752321981426, accuracy: 1e-12)
        XCTAssertEqual(try gray(0.04045).luminance, 0.0031308049535603713, accuracy: 1e-12)
        XCTAssertEqual(try gray(0.5).luminance, 0.21404114048223255, accuracy: 1e-12)
    }

    func testNearThresholdIsNotRoundedToPassing() throws {
        let gray117 = try gray(117.0 / 255), gray119 = try gray(119.0 / 255), white = try gray(1)
        XCTAssertTrue(try gray117.meets(4.5, against: white))
        XCTAssertFalse(try gray119.meets(4.5, against: white))
        XCTAssertEqual(gray119.contrast(with: white), 4.478089453577214, accuracy: 1e-10)
    }

    func testInvalidComponentsAndThresholdsAreRejected() throws {
        for value in [Double.nan, Double.infinity, -0.01, 1.01] {
            XCTAssertThrowsError(try gray(value)) { XCTAssertEqual($0 as? ContrastError, .invalidComponent) }
        }
        let black = try gray(0), white = try gray(1)
        for threshold in [Double.nan, Double.infinity, 0, 22] {
            XCTAssertThrowsError(try black.meets(threshold, against: white)) {
                XCTAssertEqual($0 as? ContrastError, .invalidThreshold)
            }
        }
    }

    func testUIKitGrayConversionUsesLinearLuminance() throws {
        let color = UIColor(white: 0.5, alpha: 1)
        let resolved = try ConfiguredContrast.resolve(color, traits: traits(.light))
        XCTAssertEqual(resolved.luminance, 0.21404114048223255, accuracy: 0.00001)
        XCTAssertEqual(try ConfiguredContrast.ratio(foreground: color, background: .white, traits: traits(.light)),
                       3.976653024912438, accuracy: 0.0001)
    }

    func testLinearColorSpaceIsConvertedBeforeFormula() throws {
        let space = try XCTUnwrap(CGColorSpace(name: CGColorSpace.linearSRGB))
        let cg = try XCTUnwrap(CGColor(colorSpace: space, components: [0.21404114048223255, 0.21404114048223255, 0.21404114048223255, 1]))
        let resolved = try ConfiguredContrast.resolve(UIColor(cgColor: cg), traits: traits(.light))
        XCTAssertEqual(resolved.red, 0.5, accuracy: 0.0001)
        XCTAssertEqual(resolved.luminance, 0.21404114048223255, accuracy: 0.0001)
    }

    func testDynamicColorsUseExplicitStyleAndContrast() throws {
        let dynamic = UIColor { t in
            if t.accessibilityContrast == .high { return t.userInterfaceStyle == .dark ? .white : .black }
            return UIColor(white: t.userInterfaceStyle == .dark ? 0.8 : 0.2, alpha: 1)
        }
        for style: UIUserInterfaceStyle in [.light, .dark] {
            for contrast: UIAccessibilityContrast in [.normal, .high] {
                let result = try ConfiguredContrast.resolve(dynamic, traits: traits(style, contrast))
                let expected: Double = contrast == .high ? (style == .dark ? 1 : 0) : (style == .dark ? 0.8 : 0.2)
                XCTAssertEqual(result.red, expected, accuracy: 0.0001)
            }
        }
    }

    func testConfiguredSemanticPairAcrossFourTraitContexts() throws {
        for style: UIUserInterfaceStyle in [.light, .dark] {
            for contrast: UIAccessibilityContrast in [.normal, .high] {
                let ratio = try ConfiguredContrast.ratio(foreground: .label, background: .systemBackground,
                                                         traits: traits(style, contrast))
                XCTAssertTrue(ratio.isFinite)
                XCTAssertGreaterThanOrEqual(ratio, 4.5)
                XCTAssertLessThanOrEqual(ratio, 21.00001)
                print("CONFIGURED_CONTRAST style=\(style.rawValue) contrast=\(contrast.rawValue) ratio=\(ratio)")
            }
        }
    }

    func testTranslucentForegroundAndBackgroundAreRejected() throws {
        let t = traits(.light)
        XCTAssertThrowsError(try ConfiguredContrast.ratio(foreground: .black.withAlphaComponent(0.5), background: .white, traits: t)) {
            XCTAssertEqual($0 as? ContrastError, .translucent)
        }
        XCTAssertThrowsError(try ConfiguredContrast.ratio(foreground: .black, background: .white.withAlphaComponent(0.5), traits: t)) {
            XCTAssertEqual($0 as? ContrastError, .translucent)
        }
    }
}

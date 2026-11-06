import XCTest
import UIKit
@testable import AccessibilityExamples

@MainActor
final class PlaybackSpeedTests: XCTestCase {
    func testOrdinaryButtonsHaveDistinctNamesAndInitialSelection() {
        let view = PlaybackSpeedChoices()
        XCTAssertFalse(view.isAccessibilityElement)
        XCTAssertEqual(view.arrangedSubviews.count, 4)
        XCTAssertEqual(Set(view.buttons.compactMap(\.accessibilityLabel)).count, 4)
        XCTAssertTrue(view.buttons.allSatisfy { $0.accessibilityLabel?.contains("Playback speed") == true })
        XCTAssertTrue(view.buttons.allSatisfy { $0.accessibilityTraits.contains(.button) })
        XCTAssertEqual(view.buttons.map(\.isSelected), [false, true, false, false])
        XCTAssertEqual(view.buttons[1].accessibilityValue, "Current speed")
    }

    func testOrdinaryPrimaryActionUpdatesStateBeforeCallback() {
        let view = PlaybackSpeedChoices()
        var calls: [Float] = []
        view.onChange = { rate in
            calls.append(rate)
            XCTAssertEqual(view.selectedRate, rate)
            XCTAssertEqual(view.buttons[2].accessibilityValue, "Current speed")
        }
        view.buttons[2].sendActions(for: .primaryActionTriggered)
        XCTAssertEqual(calls, [1.5])
        XCTAssertEqual(view.selectedRate, 1.5)
    }

    func testOldSelectionClearsWithoutLosingUnrelatedTraits() {
        let view = PlaybackSpeedChoices()
        view.buttons[1].accessibilityTraits.insert(.updatesFrequently)
        XCTAssertTrue(view.select(2))
        XCTAssertEqual(view.buttons.map(\.isSelected), [false, false, false, true])
        XCTAssertEqual(view.buttons[1].accessibilityValue, "Not selected")
        XCTAssertFalse(view.buttons[1].accessibilityTraits.contains(.selected))
        XCTAssertTrue(view.buttons[1].accessibilityTraits.contains(.updatesFrequently))
        XCTAssertTrue(view.buttons[3].accessibilityTraits.contains(.selected))
    }

    func testRepeatedSelectionDoesNotEmitDuplicateChange() {
        let view = PlaybackSpeedChoices()
        var calls: [Float] = []
        view.onChange = { calls.append($0) }
        XCTAssertTrue(view.select(1))
        view.buttons[2].sendActions(for: .primaryActionTriggered)
        view.buttons[2].sendActions(for: .primaryActionTriggered)
        XCTAssertEqual(calls, [1.5])
    }

    func testInvalidRatesLeaveStateAndCallbackUntouched() {
        let view = PlaybackSpeedChoices()
        var calls = 0
        view.onChange = { _ in calls += 1 }
        for rate: Float in [.nan, .infinity, -.infinity, -1, 0, 1.25, .greatestFiniteMagnitude] {
            XCTAssertFalse(view.select(rate))
            XCTAssertEqual(view.selectedRate, 1)
        }
        XCTAssertEqual(calls, 0)
        XCTAssertEqual(view.buttons[1].accessibilityValue, "Current speed")
    }

    func testDisabledRequestsAreRejectedAndReenableRestoresOrdinaryPath() {
        let view = PlaybackSpeedChoices()
        var calls: [Float] = []
        view.onChange = { calls.append($0) }
        view.controlsEnabled = false
        XCTAssertTrue(view.buttons.allSatisfy { !$0.isEnabled })
        XCTAssertFalse(view.select(2))
        XCTAssertEqual(view.selectedRate, 1)
        XCTAssertTrue(calls.isEmpty)
        view.controlsEnabled = true
        view.buttons[3].sendActions(for: .primaryActionTriggered)
        XCTAssertEqual(calls, [2])
    }

    func testEverySupportedChoiceHasAnOrdinaryAction() {
        let view = PlaybackSpeedChoices()
        for (button, rate) in zip(view.buttons, PlaybackSpeedChoices.rates) {
            button.sendActions(for: .primaryActionTriggered)
            XCTAssertEqual(view.selectedRate, rate)
            XCTAssertTrue(button.isSelected)
        }
    }

    func testRetainedButtonDoesNotRetainOwner() {
        var owner: PlaybackSpeedChoices? = PlaybackSpeedChoices()
        weak var weakOwner = owner
        let button = owner!.buttons[0]
        owner = nil
        XCTAssertNil(weakOwner)
        button.sendActions(for: .primaryActionTriggered)
        XCTAssertNil(weakOwner)
    }
}

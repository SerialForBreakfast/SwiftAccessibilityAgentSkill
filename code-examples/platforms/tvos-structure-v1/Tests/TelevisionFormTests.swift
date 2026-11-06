import XCTest
import UIKit
@testable import AccessibilityExamples

@MainActor
final class TelevisionFormTests: XCTestCase {
    func testInitialIndependentControlsAndQuietError() {
        let f = TelevisionForm(validate: { _ in nil }, save: { _ in })
        XCTAssertTrue(f.field.superview === f)
        XCTAssertTrue(f.submitButton.superview === f)
        XCTAssertTrue(f.errorLabel.isHidden)
        XCTAssertEqual(f.subviews.count, 3)
        XCTAssertFalse(f.isAccessibilityElement)
    }
    func testInvalidInputShowsErrorWithoutSavingOrErasing() {
        var saved: [String] = []
        let f = TelevisionForm(validate: { _ in "Check address" }, save: { saved.append($0) })
        f.field.text = "bad input"; f.submit()
        XCTAssertEqual(f.field.text, "bad input")
        XCTAssertEqual(f.errorLabel.text, "Check address")
        XCTAssertFalse(f.errorLabel.isHidden)
        XCTAssertTrue(f.errorLabel.isAccessibilityElement)
        XCTAssertTrue(saved.isEmpty)
    }
    func testRepeatedErrorPreservesOriginalHelpWithoutAppending() {
        let f = TelevisionForm(hint: "Work address", validate: { _ in "Check address" }, save: { _ in })
        f.submit(); f.submit()
        XCTAssertEqual(f.field.accessibilityHint, "Work address. Check address")
    }
    func testEditingClearsErrorRestoresHelpAndPreservesInput() {
        let f = TelevisionForm(hint: "Work address", validate: { _ in "Check address" }, save: { _ in })
        f.submit(); f.field.text = "new value"
        f.field.sendActions(for: .editingChanged)
        XCTAssertTrue(f.errorLabel.isHidden)
        XCTAssertFalse(f.errorLabel.isAccessibilityElement)
        XCTAssertEqual(f.errorLabel.text, "")
        XCTAssertEqual(f.field.accessibilityHint, "Work address")
        XCTAssertEqual(f.field.text, "new value")
    }
    func testCorrectionRecoversAndAllowsOrdinarySubmission() {
        var saved: [String] = []
        let f = TelevisionForm(validate: { $0 == "valid" ? nil : "Check address" }, save: { saved.append($0) })
        f.field.text = "bad"; f.submit()
        f.field.text = "valid"; f.field.sendActions(for: .editingChanged)
        f.submitButton.sendActions(for: .primaryActionTriggered)
        XCTAssertEqual(saved, ["valid"])
        XCTAssertTrue(f.errorLabel.isHidden)
    }
    func testValidInputIsNotSilentlyTrimmed() {
        var saved = ""
        let f = TelevisionForm(validate: { _ in nil }, save: { saved = $0 })
        f.field.text = "  a@b  "; f.submit()
        XCTAssertEqual(saved, "  a@b  ")
        XCTAssertEqual(f.field.text, "  a@b  ")
    }
    func testDisabledSubmissionDoesNotValidateOrSave() {
        var calls = 0
        let f = TelevisionForm(validate: { _ in calls += 1; return nil }, save: { _ in calls += 1 })
        f.submitButton.isEnabled = false; f.submit()
        XCTAssertEqual(calls, 0)
    }
    func testReentrantSaveDoesNotSubmitTwice() {
        var calls = 0
        var f: TelevisionForm!
        f = TelevisionForm(validate: { _ in nil }, save: { _ in
            calls += 1
            if calls == 1 { f.submit() }
        })
        f.submit()
        XCTAssertEqual(calls, 1)
        f = nil
    }
    func testAbsentHelpReturnsToNilAfterEditing() {
        let f = TelevisionForm(validate: { _ in "Check address" }, save: { _ in })
        f.submit(); f.field.sendActions(for: .editingChanged)
        XCTAssertNil(f.field.accessibilityHint)
    }
    func testValidationKeepsExistingControlIdentity() {
        let f = TelevisionForm(validate: { _ in "Check address" }, save: { _ in })
        let field = f.field, button = f.submitButton
        f.submit(); f.field.sendActions(for: .editingChanged); f.submit()
        XCTAssertTrue(f.field === field); XCTAssertTrue(f.submitButton === button)
        XCTAssertEqual(f.subviews.count, 3)
    }
    func testEditingDoesNotValidateOrSave() {
        var calls = 0
        let f = TelevisionForm(validate: { _ in calls += 1; return nil }, save: { _ in calls += 1 })
        f.field.text = "editing"; f.field.sendActions(for: .editingChanged)
        XCTAssertEqual(calls, 0)
    }
    func testSubmissionPassesInputSnapshotToCallback() {
        var saved = ""
        var f: TelevisionForm!
        f = TelevisionForm(validate: { _ in nil }, save: { input in
            f.field.text = "later"; saved = input
        })
        f.field.text = "original"; f.submit()
        XCTAssertEqual(saved, "original"); XCTAssertEqual(f.field.text, "later")
        f = nil
    }
}

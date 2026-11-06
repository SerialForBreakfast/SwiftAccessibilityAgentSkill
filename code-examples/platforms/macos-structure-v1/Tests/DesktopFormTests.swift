import XCTest
import AppKit
@testable import AccessibilityExamples

@MainActor
final class DesktopFormTests: XCTestCase {
    func testInitialIndependentControlsAndQuietError() {
        let f = DesktopForm(validate: { _ in nil }, save: { _ in })
        XCTAssertTrue(f.field.superview === f)
        XCTAssertTrue(f.submitButton.superview === f)
        XCTAssertTrue(f.errorLabel.isHidden)
        XCTAssertEqual(f.subviews.count, 3)
        XCTAssertFalse(f.isAccessibilityElement())
    }
    func testInvalidInputShowsErrorWithoutSavingOrErasing() {
        var saved: [String] = []
        let f = DesktopForm(validate: { _ in "Check address" }, save: { saved.append($0) })
        f.field.stringValue = "bad input"; f.submit()
        XCTAssertEqual(f.field.stringValue, "bad input")
        XCTAssertEqual(f.errorLabel.stringValue, "Check address")
        XCTAssertFalse(f.errorLabel.isHidden)
        XCTAssertTrue(f.errorLabel.isAccessibilityElement())
        XCTAssertTrue(saved.isEmpty)
    }
    func testRepeatedErrorPreservesOriginalHelpWithoutAppending() {
        let f = DesktopForm(help: "Work address", validate: { _ in "Check address" }, save: { _ in })
        f.submit(); f.submit()
        XCTAssertEqual(f.field.accessibilityHelp(), "Work address. Check address")
    }
    func testEditingClearsErrorRestoresHelpAndPreservesInput() {
        let f = DesktopForm(help: "Work address", validate: { _ in "Check address" }, save: { _ in })
        f.submit(); f.field.stringValue = "new value"
        f.controlTextDidChange(Notification(name: NSControl.textDidChangeNotification, object: f.field))
        XCTAssertTrue(f.errorLabel.isHidden)
        XCTAssertFalse(f.errorLabel.isAccessibilityElement())
        XCTAssertEqual(f.errorLabel.stringValue, "")
        XCTAssertEqual(f.field.accessibilityHelp(), "Work address")
        XCTAssertEqual(f.field.stringValue, "new value")
    }
    func testCorrectionRecoversAndAllowsOrdinarySubmission() {
        var saved: [String] = []
        let f = DesktopForm(validate: { $0 == "valid" ? nil : "Check address" }, save: { saved.append($0) })
        f.field.stringValue = "bad"; f.submit()
        f.field.stringValue = "valid"; f.controlTextDidChange(Notification(name: NSControl.textDidChangeNotification, object: f.field))
        f.submitButton.performClick(nil)
        XCTAssertEqual(saved, ["valid"])
        XCTAssertTrue(f.errorLabel.isHidden)
    }
    func testValidInputIsNotSilentlyTrimmed() {
        var saved = ""
        let f = DesktopForm(validate: { _ in nil }, save: { saved = $0 })
        f.field.stringValue = "  a@b  "; f.submit()
        XCTAssertEqual(saved, "  a@b  ")
        XCTAssertEqual(f.field.stringValue, "  a@b  ")
    }
    func testDisabledSubmissionDoesNotValidateOrSave() {
        var calls = 0
        let f = DesktopForm(validate: { _ in calls += 1; return nil }, save: { _ in calls += 1 })
        f.submitButton.isEnabled = false; f.submit()
        XCTAssertEqual(calls, 0)
    }
    func testReentrantSaveDoesNotSubmitTwice() {
        var calls = 0
        var f: DesktopForm!
        f = DesktopForm(validate: { _ in nil }, save: { _ in
            calls += 1
            if calls == 1 { f.submit() }
        })
        f.submit()
        XCTAssertEqual(calls, 1)
        f = nil
    }
    func testAbsentHelpReturnsToNilAfterEditing() {
        let f = DesktopForm(validate: { _ in "Check address" }, save: { _ in })
        f.submit(); f.controlTextDidChange(Notification(name: NSControl.textDidChangeNotification, object: f.field))
        XCTAssertNil(f.field.accessibilityHelp())
    }
    func testValidationKeepsExistingControlIdentity() {
        let f = DesktopForm(validate: { _ in "Check address" }, save: { _ in })
        let field = f.field, button = f.submitButton
        f.submit(); f.controlTextDidChange(Notification(name: NSControl.textDidChangeNotification, object: f.field)); f.submit()
        XCTAssertTrue(f.field === field); XCTAssertTrue(f.submitButton === button)
        XCTAssertEqual(f.subviews.count, 3)
    }
    func testEditingDoesNotValidateOrSave() {
        var calls = 0
        let f = DesktopForm(validate: { _ in calls += 1; return nil }, save: { _ in calls += 1 })
        f.field.stringValue = "editing"; f.controlTextDidChange(Notification(name: NSControl.textDidChangeNotification, object: f.field))
        XCTAssertEqual(calls, 0)
    }
    func testSubmissionPassesInputSnapshotToCallback() {
        var saved = ""
        var f: DesktopForm!
        f = DesktopForm(validate: { _ in nil }, save: { input in
            f.field.stringValue = "later"; saved = input
        })
        f.field.stringValue = "original"; f.submit()
        XCTAssertEqual(saved, "original"); XCTAssertEqual(f.field.stringValue, "later")
        f = nil
    }
}

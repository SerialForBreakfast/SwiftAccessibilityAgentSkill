# AppKit/macOS: form-recovery

Status: draft; independent oracle/question review pending. Not baseline-eligible.
Classification: Shared validation policy demonstrated through platform-specific native controls.

Preserve entered text and existing field/button identity. Keep an ordinary Save action and visible error text, rather than an error conveyed only by color or an accessibility shortcut. Append transient help without accumulation and restore the original optional help on edit; clear stale error state and leave field value alone. Editing must not validate/save in this task. Respect disabled state and avoid duplicate submission from the reentrant save callback. Capture input before the callback. Accept other native composition/delegate/action designs, injected validators and equivalent reentrancy guards. Exact English sample strings and helper names are not required. No claim of announcements, keyboard presentation or focus delivery from stored values.

Score correctness, preservation, practical usefulness and unsupported certainty separately. Invented APIs, lost ordinary actions, erased user input and stale cross-item actions are critical. Accept alternatives satisfying the contract; no requirement for test/helper names. These are known-development cases, not holdouts.

## Traceability

- [Source claims and check IDs](../manifest.json)
- [Implementation](../Sources/DesktopForm.swift)
- [Unit assertions](../Tests/DesktopFormTests.swift)
- Methods: `DesktopFormTests/testInitialIndependentControlsAndQuietError`, `DesktopFormTests/testInvalidInputShowsErrorWithoutSavingOrErasing`, `DesktopFormTests/testRepeatedErrorPreservesOriginalHelpWithoutAppending`, `DesktopFormTests/testEditingClearsErrorRestoresHelpAndPreservesInput`, `DesktopFormTests/testCorrectionRecoversAndAllowsOrdinarySubmission`, `DesktopFormTests/testValidInputIsNotSilentlyTrimmed`, `DesktopFormTests/testDisabledSubmissionDoesNotValidateOrSave`, `DesktopFormTests/testReentrantSaveDoesNotSubmitTwice`, `DesktopFormTests/testAbsentHelpReturnsToNilAfterEditing`, `DesktopFormTests/testValidationKeepsExistingControlIdentity`, `DesktopFormTests/testEditingDoesNotValidateOrSave`, `DesktopFormTests/testSubmissionPassesInputSnapshotToCallback`.
- Negative checks: `invalidsave`, `stalemessage`, `reentrant`.
- [Execution and difficulty record](../../../../research/evaluation/platform-structure-v1/README.md)

Subject input is the separate .prompt.md plus approved condition material. Do not inject the rubric, assertions, negative fixtures or incident narrative.

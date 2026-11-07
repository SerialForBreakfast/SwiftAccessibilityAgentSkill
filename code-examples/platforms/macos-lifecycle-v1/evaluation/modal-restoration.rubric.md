# AppKit/macOS: modal-restoration

Status: draft; independent review and baseline qualification pending.
Classification: AppKit/macOS-specific request contract.

Resolve eligibility at completion, preserve current hierarchy ownership, reject disabled/hidden candidates and use an eligible fallback. Check acceptsFirstResponder before a native request. makeFirstResponder returning true is not proof that the named button became first responder; the window may become first responder. Reject stale/duplicate/cancelled completions and consume the current session before invoking a potentially reentrant requester. Report request rejection distinctly. Accept equivalent leases, completion guards or lifecycle ownership rather than requiring the example helper names or exact control subclasses.

Score correctness, preservation, usefulness and unsupported certainty separately. Invented APIs, stale cross-modal actions, lost ordinary controls and unsupported availability are critical errors. Accept valid alternatives; unit results establish stored state, callback/request behavior and ownership rather than delivered focus/speech or rendered appearance.

## Traceability

- [Source claims and negative IDs](../manifest.json)
- [Implementation](../Sources/DesktopLifecycle.swift)
- [Assertions](../Tests/DesktopLifecycleTests.swift)
- Methods: `DesktopLifecycleTests/testRefusingOriginalUsesFallback`, `DesktopLifecycleTests/testBeginDoesNotRequestFocus`, `DesktopLifecycleTests/testCompletedModalRequestsOriginal`, `DesktopLifecycleTests/testRemovedOriginalUsesFallback`, `DesktopLifecycleTests/testHiddenAncestorUsesFallback`, `DesktopLifecycleTests/testDisabledOriginalUsesFallback`, `DesktopLifecycleTests/testForeignOriginalUsesFallback`, `DesktopLifecycleTests/testOldCompletionCannotConsumeNewSession`, `DesktopLifecycleTests/testDuplicateCompletionIsQuiet`, `DesktopLifecycleTests/testCancellationRejectsLateCompletion`, `DesktopLifecycleTests/testOldCancellationPreservesCurrentSession`, `DesktopLifecycleTests/testNoEligibleTargetDoesNotRequest`, `DesktopLifecycleTests/testRequestRejectionIsReturned`, `DesktopLifecycleTests/testReentrantRequestPreservesNewSession`, `DesktopLifecycleTests/testHiddenRootPreventsRequest`, `DesktopLifecycleTests/testDefaultRequestWithoutWindowReturnsFalse`.
- Negative checks: `foreigntarget`, `stalecompletion`, `original-responder-check`.
- [Execution, original source and analysis](../../../../research/evaluation/platform-lifecycle-v1/README.md)

Subject payload is the matching .prompt.md plus explicitly approved condition material. Keep this rubric, source solutions, assertions, negative fixtures and incident history out of subject context. These are development cases, not holdouts.

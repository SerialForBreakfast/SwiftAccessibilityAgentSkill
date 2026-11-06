# UIKit/tvOS: modal-restoration

Status: draft; independent review and baseline qualification pending.
Classification: UIKit/tvOS-specific request contract.

Resolve eligibility at completion, preserve current hierarchy ownership, reject disabled/hidden candidates and use an eligible fallback. Respect ancestor visibility/interaction eligibility, update the preferred target and request a focus update on an appropriate owning environment. Apple requires the environment to contain the currently focused view for setNeedsFocusUpdate to have effect; a unit request spy does not establish that condition. Reject stale/duplicate/cancelled completions and consume the current session before invoking a potentially reentrant requester. Report request rejection distinctly. Accept equivalent leases, completion guards or lifecycle ownership rather than requiring the example helper names or exact control subclasses.

Score correctness, preservation, usefulness and unsupported certainty separately. Invented APIs, stale cross-modal actions, lost ordinary controls and unsupported availability are critical errors. Accept valid alternatives; unit results establish stored state, callback/request behavior and ownership rather than delivered focus/speech or rendered appearance.

## Traceability

- [Source claims and negative IDs](../manifest.json)
- [Implementation](../Sources/TelevisionLifecycle.swift)
- [Assertions](../Tests/TelevisionLifecycleTests.swift)
- Methods: `TelevisionLifecycleTests/testBeginDoesNotRequestFocus`, `TelevisionLifecycleTests/testCompletedModalRequestsOriginal`, `TelevisionLifecycleTests/testRemovedOriginalUsesFallback`, `TelevisionLifecycleTests/testHiddenAncestorUsesFallback`, `TelevisionLifecycleTests/testDisabledOriginalUsesFallback`, `TelevisionLifecycleTests/testForeignOriginalUsesFallback`, `TelevisionLifecycleTests/testOldCompletionCannotConsumeNewSession`, `TelevisionLifecycleTests/testDuplicateCompletionIsQuiet`, `TelevisionLifecycleTests/testCancellationRejectsLateCompletion`, `TelevisionLifecycleTests/testOldCancellationPreservesCurrentSession`, `TelevisionLifecycleTests/testNoEligibleTargetDoesNotRequest`, `TelevisionLifecycleTests/testRequestRejectionIsReturned`, `TelevisionLifecycleTests/testReentrantRequestPreservesNewSession`, `TelevisionLifecycleTests/testHiddenRootPreventsRequest`, `TelevisionLifecycleTests/testTransparentAncestorUsesFallback`, `TelevisionLifecycleTests/testDefaultRequestUpdatesPreferredTarget`, `TelevisionLifecycleTests/testPreferredTargetRevalidatedAfterRemoval`.
- Negative checks: `foreigntarget`, `stalecompletion`.
- [Execution, original source and analysis](../../../../research/evaluation/platform-lifecycle-v1/README.md)

Subject payload is the matching .prompt.md plus explicitly approved condition material. Keep this rubric, source solutions, assertions, negative fixtures and incident history out of subject context. These are development cases, not holdouts.

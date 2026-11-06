# macOS/AppKit: validation-ownership

Status: draft, independent review pending, not baseline eligible. Development case, not holdout.
Classification: Shared ownership principle demonstrated through platform-native objects.

Only the current request and unchanged input snapshot can apply. Consume a completion before external callbacks; support synchronous and reentrant callbacks, cancellation, duplicate delivery, and owner deallocation. Preserve field identity and raw input. Use declared field order, not dictionary iteration, for the requested invalid target. Distinguish unavailable/invalid service responses from success. Accept task tokens, generations, equivalent identity guards, or structured-concurrency adapters that meet the supplied callback contract. Do not require transport cancellation or claim delivered focus.

## Grading
Score correctness, behavior preservation, practical usefulness and unsupported certainty independently. Critical: stale cross-item writes, lost ordinary actions or input, invented APIs, unsupported availability. Accept valid alternatives; sample names and English strings are not required. Missing executable inputs are ungradable, not a model failure.

## Evidence
- [Source claims and negatives](../manifest.json), claim async; negative checks: validation-generation, validation-snapshot.
- [Implementation](../Sources/AsyncOwnership.swift); [assertions](../Tests/AsyncOwnershipTests.swift).
- Exact methods: `AsyncOwnershipTests/testPendingStateAndSnapshotPreserveInput`, `AsyncOwnershipTests/testOutOfOrderReplyCannotReplaceLatestErrors`, `AsyncOwnershipTests/testEditInvalidatesInFlightResult`, `AsyncOwnershipTests/testCancelRejectsLateReply`, `AsyncOwnershipTests/testNativeFieldMutationCannotApplyOldSnapshot`, `AsyncOwnershipTests/testFirstInvalidUsesDeclaredFieldOrder`, `AsyncOwnershipTests/testDuplicateReplyCannotAcceptTwice`, `AsyncOwnershipTests/testUnknownFieldAndEmptyErrorAreNotSuccess`, `AsyncOwnershipTests/testSynchronousCompletionWorks`, `AsyncOwnershipTests/testReentrantAcceptancePreservesNewRequest`, `AsyncOwnershipTests/testRetainedReplyDoesNotRetainForm`, `AsyncOwnershipTests/testSuccessRecoversAfterErrorAndKeepsFieldIdentity`.
- Execution: research/evaluation/cross-platform-closure-v1/results-index.json, matching manifest hash.

Inject only the separate subject question and approved condition content. Keep rubric, negative fixtures, solution, routes and incident diagnostics controller-only. No model answer has been generated or graded.

# macOS/AppKit: media-load-ownership

Status: draft, independent review pending, not baseline eligible. Development case, not holdout.
Classification: Shared ownership principle demonstrated through platform-native objects.

Check both request ownership and actual AVPlayer.currentItem identity; item identity alone fails same-item refresh. Invalidate cancelled requests, handle nil without loading, consume duplicate completion, distinguish loader failure from absent metadata, preserve player preferences and avoid retaining the owner. Accept equivalent weak ownership and cancellation designs. Fixture callbacks prove state ownership, not real asset loading, audio-description detection, or presentation.

## Grading
Score correctness, behavior preservation, practical usefulness and unsupported certainty independently. Critical: stale cross-item writes, lost ordinary actions or input, invented APIs, unsupported availability. Accept valid alternatives; sample names and English strings are not required. Missing executable inputs are ungradable, not a model failure.

## Evidence
- [Source claims and negatives](../manifest.json), claim media; negative checks: media-identity, media-duplicate.
- [Implementation](../Sources/AsyncOwnership.swift); [assertions](../Tests/AsyncOwnershipTests.swift).
- Exact methods: `MediaLoadOwnerTests/testNilItemDoesNotInvokeLoader`, `MediaLoadOwnerTests/testReplacementRejectsOldItemCompletion`, `MediaLoadOwnerTests/testSameItemNewRequestRejectsOldGeneration`, `MediaLoadOwnerTests/testExternalReplacementRejectsOldResult`, `MediaLoadOwnerTests/testCancellationRejectsLateSuccess`, `MediaLoadOwnerTests/testErrorIsNotMissingOrSuccessfulMetadata`, `MediaLoadOwnerTests/testDuplicateCallbackCannotOverwriteFirstResult`, `MediaLoadOwnerTests/testInspectionDoesNotChangePlayerPreferences`, `MediaLoadOwnerTests/testRetainedLoaderReplyDoesNotRetainOwner`.
- Execution: research/evaluation/cross-platform-closure-v1/results-index.json, matching manifest hash.

Inject only the separate subject question and approved condition content. Keep rubric, negative fixtures, solution, routes and incident diagnostics controller-only. No model answer has been generated or graded.

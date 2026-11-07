# tvOS/UIKit: text-rotor

Status: draft, independent review pending, not baseline eligible. Development case, not holdout.
Classification: UIKit-specific contract.

Use real framework rotor APIs and UTF-16 NSRange coordinates with composed-character boundary validation. Match entire current ranges and target identity, handle invalid/foreign results, ends, empty query, changed text and stale sessions. Keep native text selection available. Explicit overlap policy and stable source revision are application policies. Accept equivalent indexing/session designs. AppKit uses imported nested SearchParameters/ItemResult types and requires safe actor isolation for delegate calls; UIKit uses a search block. Do not transplant unavailable platform members. Unit callbacks do not establish rotor discoverability or spoken navigation.

## Grading
Score correctness, behavior preservation, practical usefulness and unsupported certainty independently. Critical: stale cross-item writes, lost ordinary actions or input, invented APIs, unsupported availability. Accept valid alternatives; sample names and English strings are not required. Missing executable inputs are ungradable, not a model failure.

## Evidence
- [Source claims and negatives](../manifest.json), claim text; negative checks: text-boundary, text-stale.
- [Implementation](../Sources/EditedRotorUIKit.swift); [assertions](../Tests/EditedRotorUIKitTests.swift).
- Exact methods: `EditedRotorUIKitTests/testInitialDirectionAndBothBoundaries`, `EditedRotorUIKitTests/testForwardAndBackwardUseFullCurrentRange`, `EditedRotorUIKitTests/testUnicodePrefixProducesCorrectNativeRange`, `EditedRotorUIKitTests/testPartialGraphemeMatchesAreExcluded`, `EditedRotorUIKitTests/testOverlapPolicyIsExplicit`, `EditedRotorUIKitTests/testNewRevisionRestartsRetainedResult`, `EditedRotorUIKitTests/testRetainedOldRotorIsInvalidAfterQueryChange`, `EditedRotorUIKitTests/testInsertionAndDeletionRebuildRanges`, `EditedRotorUIKitTests/testEmptyQueryUpdatesOrdinaryDocumentWithoutRotor`, `EditedRotorUIKitTests/testUnannouncedTextChangeRejectsCachedSearch`, `EditedRotorUIKitTests/testForeignTextInputPositionsRestartSafely`, `EditedRotorUIKitTests/testNativeRangeCanBeUsedForOrdinaryTextSelection`.
- Execution: research/evaluation/cross-platform-closure-v1/results-index.json, matching manifest hash.

Inject only the separate subject question and approved condition content. Keep rubric, negative fixtures, solution, routes and incident diagnostics controller-only. No model answer has been generated or graded.

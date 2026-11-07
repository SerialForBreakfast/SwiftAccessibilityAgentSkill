# Controller-only rubric: macOS/ownership

Draft, separate-context source review informed. Known development family, not a holdout.

1. Old callbacks, including an Off/nil request, cannot alter a newer item or completed snapshot.
2. Old or duplicate success/error results cannot replace current state.
3. Reject cancelled results; explain whether cancellation cleanup is cooperative or immediately owner-invalidated. Either is valid when the contract is explicit.
4. State how item changes trigger reload or explicit invalidation; do not claim automatic external observation from a getter.

Answer correctness and controller execution evidence are separate scores. The request
explicitly asks for tests; accept any focused executable tests of the contract, not
these exact IDs, ticket scheme, strings, IDs, view type or architecture. Harmless
extra invalidation is valid when state remains correct. Task cancellation need not
be synchronously delivered unless the answer promises it.

Narrow example assertion leads:
- `MediaSelectionTests/testLoadingDoesNotChangeNativeChoice`
- `MediaSelectionTests/testOldOptionIDCannotSelectAfterReload`
- `MediaSelectionTests/testDuplicateCompletionCannotOverwriteSuccess`
- `MediaSelectionTests/testOldCompletionCannotOverwriteNewLoad`
- `MediaSelectionTests/testOldErrorCannotOverwriteNewSuccess`
- `MediaSelectionTests/testCancelRejectsLateCompletion`
- `MediaSelectionTests/testCancelDoesNotClearNativeSelection`
- `MediaSelectionTests/testReplacedItemRejectsOldChoice`
- `MediaSelectionTests/testReplacedItemRejectsOldCompletion`
- `MediaSelectionTests/testCapturedBindingRejectsAfterCancellation`
- `MediaSelectionTests/testCancelledOldTaskCannotCancelNewerLoad`
- `MediaSelectionTests/testCancelledCurrentTaskDoesNotPublishResult`
- `MediaSelectionTests/testAlreadyCancelledTaskCannotStartLoad`
- `ReviewRegressionTests/testStaleOffCannotClearReloadedSelection`
- `ReviewRegressionTests/testStaleOffCannotClearReplacementSelection`
- `ReviewRegressionTests/testOldCompletionLeavesLoadingOnItemChange`

Insufficient evidence for controller validation is not automatically an incorrect
answer. Source compilation does not establish speech, layout or delivered focus.

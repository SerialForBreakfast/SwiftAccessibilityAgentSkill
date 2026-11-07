# Controller-only rubric: macOS / ownership

Draft, independent review pending. Accept alternate observable stores, typed IDs,
async tasks or callbacks and suitable native selection APIs that preserve the same
contract. Do not require this example's architecture, strings or UUID format.

Pass: current-item selection and observable state follow the requested behavior.
Gap: selection is simulated, stale operations affect newer work, or required inputs
are missing. Insufficient evidence: prose or view construction without executable
assertions. API compilation does not prove speech, rendered captions or focus.

Assertion bindings (narrow observations, not whole-prose coverage):
- `MediaSelectionTests/testLoadingDoesNotChangeNativeChoice`
- `MediaSelectionTests/testDuplicateCompletionCannotOverwriteSuccess`
- `MediaSelectionTests/testOldCompletionCannotOverwriteNewLoad`
- `MediaSelectionTests/testCancelRejectsLateCompletion`
- `MediaSelectionTests/testCancelDoesNotClearNativeSelection`
- `MediaSelectionTests/testReplacedItemRejectsOldChoice`
- `MediaSelectionTests/testReplacedItemRejectsOldCompletion`
- `MediaSelectionTests/testCancelledOldTaskCannotCancelNewerLoad`
- `MediaSelectionTests/testCancelledCurrentTaskDoesNotPublishResult`
- `MediaSelectionTests/testAlreadyCancelledTaskCannotStartLoad`

Use real local media groups for selection claims. Distinguish app policy (forced-only
filtering, snapshot IDs and generations) from Apple API contracts. Synthetic content
does not prove production stream metadata or narration quality.

## Criterion-Level Review

1. Ignore old success/error results after a newer request or item replacement.
2. Duplicate completions cannot overwrite a committed result.
3. Cancellation invalidates only work owned by that request, not a newer operation.
4. Already-cancelled tasks do not start new work.
5. Preserve valid native selection when old callbacks are rejected.

Accept equivalent native APIs, state architectures and visible selection controls.
These are task contracts; the supplied test identifiers prove only named narrow
observations and are not an instruction to reproduce this exact implementation.

# filtered-results: controller rubric

Status: draft, not independently reviewed or baseline-eligible.
Classification: UIKit-specific on tvOS.

Preserve visible titles and accessible names, use ordinary primary actions, reconcile selection by stable ID and filtered membership, atomically reject duplicate IDs, remove obsolete views, prevent stale/disabled dispatch, and preserve unrelated trait bits. Accept collection-backed rendering, target/action, different stale-action ownership strategies and equivalent filtering consistent with the prompt. Direct sendActions tests do not simulate remote events or actual focus.

Grade correctness, preservation, practical usefulness and unsupported certainty separately. Hidden ordinary actions, wrong-item dispatch and invented availability are critical errors. Do not penalize valid implementation alternatives simply for differing from the reference.

## Traceability

- [Apple claims and check IDs](../manifest.json)
- [Example](../Sources/TelevisionResults.swift)
- [Unit assertions](../Tests/TelevisionResultsTests.swift)
- Methods: `TelevisionResultsTests/testVisibleAndAccessibleNames`, `TelevisionResultsTests/testPrimaryActionSelectsItem`, `TelevisionResultsTests/testReorderPreservesSelection`, `TelevisionResultsTests/testFilterPreservesVisibleSelection`, `TelevisionResultsTests/testFilteredSelectionClears`, `TelevisionResultsTests/testStaleButtonDoesNotSelectReboundItem`, `TelevisionResultsTests/testDuplicateIDsRejectedAtomically`, `TelevisionResultsTests/testEmptyResultsRemoveOldButtons`, `TelevisionResultsTests/testDisabledButtonCannotSelect`, `TelevisionResultsTests/testSelectionPreservesUnrelatedTraits`.
- Negative checks: `stalebutton`, `clobberedtraits`.
- [Execution and first failures](../../../../research/evaluation/platform-navigation-v1/README.md)

Subject input is the matching .prompt.md only plus approved evaluation-condition material. Keep this rubric, solutions, tests, routes and incident history out of subject inputs. These are development cases, not fresh holdouts.

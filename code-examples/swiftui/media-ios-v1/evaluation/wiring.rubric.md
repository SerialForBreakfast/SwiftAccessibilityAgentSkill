# Controller-only rubric: iOS / wiring

Draft, independent review pending. Accept alternate observable stores, typed IDs,
async tasks or callbacks and suitable native selection APIs that preserve the same
contract. Do not require this example's architecture, strings or UUID format.

Pass: current-item selection and observable state follow the requested behavior.
Gap: selection is simulated, stale operations affect newer work, or required inputs
are missing. Insufficient evidence: prose or view construction without executable
assertions. API compilation does not prove speech, rendered captions or focus.

Assertion bindings (narrow observations, not whole-prose coverage):
- `MediaSelectionTests/testNativeRefreshLoadsActualGroup`
- `MediaSelectionTests/testOldErrorCannotOverwriteNewSuccess`
- `MediaSelectionTests/testNoItemIsNotAbsentGroup`
- `MediaSelectionTests/testAbsentGroupIsNotFailure`
- `MediaSelectionTests/testLoadFailureIsNotEmptySuccess`
- `MediaSelectionTests/testViewRetainsSameStoreAndPlayer`
- `MediaSelectionTests/testActualRefreshPassesItemAndCharacteristicToLoader`
- `MediaSelectionTests/testActualRefreshErrorSetsFailedPhase`
- `MediaSelectionTests/testActualRefreshAbsentSetsAbsentPhase`
- `MediaSelectionTests/testInvalidChoiceDoesNotInvalidateObservableSelection`

Use real local media groups for selection claims. Distinguish app policy (forced-only
filtering, snapshot IDs and generations) from Apple API contracts. Synthetic content
does not prove production stream metadata or narration quality.

## Criterion-Level Review

1. Visible selection controls and VideoPlayer use the same underlying store/player.
2. Selection binding invokes actual native operations and reads actual selection.
3. Store-owned native writes trigger observable invalidation; automatic external native observation is a separate contract.
4. Distinguish no item, loading, absent group and load failure; provide a usable retry path.
5. Keep ordinary player controls; compile actual view composition without claiming speech, layout or delivered focus.

Accept equivalent native APIs, state architectures and visible selection controls.
These are task contracts; the supplied test identifiers prove only named narrow
observations and are not an instruction to reproduce this exact implementation.

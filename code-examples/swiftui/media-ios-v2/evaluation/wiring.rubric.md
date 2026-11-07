# Controller-only rubric: iOS/wiring

Draft, separate-context source review informed. Known development family, not a holdout.

1. The visible controls and native player share selection ownership.
2. Selection writes affect the real item and the app reports its own native writes observably, using any valid state mechanism.
3. Distinguish missing item, loading, absent group and errors and offer retry.
4. Keep ordinary player controls and distinguish compiled composition from generated semantics or delivered focus.

Answer correctness and controller execution evidence are separate scores. The request
explicitly asks for tests; accept any focused executable tests of the contract, not
these exact IDs, ticket scheme, strings, IDs, view type or architecture. Harmless
extra invalidation is valid when state remains correct. Task cancellation need not
be synchronously delivered unless the answer promises it.

Narrow example assertion leads:
- `MediaSelectionTests/testNativeRefreshLoadsActualGroup`
- `MediaSelectionTests/testNoItemIsNotAbsentGroup`
- `MediaSelectionTests/testAbsentGroupIsNotFailure`
- `MediaSelectionTests/testLoadFailureIsNotEmptySuccess`
- `MediaSelectionTests/testViewRetainsSameStoreAndPlayer`
- `MediaSelectionTests/testActualRefreshPassesItemAndCharacteristicToLoader`
- `MediaSelectionTests/testActualRefreshErrorSetsFailedPhase`
- `MediaSelectionTests/testActualRefreshAbsentSetsAbsentPhase`

Insufficient evidence for controller validation is not automatically an incorrect
answer. Source compilation does not establish speech, layout or delivered focus.

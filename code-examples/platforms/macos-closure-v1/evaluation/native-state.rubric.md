# macOS/AppKit: native-state

Status: draft, independent review pending, not baseline eligible. Development case, not holdout.
Classification: AppKit-specific contract.

Preserve independent controls, names, current state and non-color text. Restore the prior modal flag, including an initially true flag, without replacing controls. Keep native AVKit player identity and controls enabled. Accept equivalent native composition and explicit semantics. AppKit custom role/value/action and disabled state must agree; TV traits must retain unrelated bits and state must not accumulate. Assert only metadata/configuration and invoked action behavior, not actual modal focus containment, speech, visual contrast, or TV27 runtime text scaling.

## Grading
Score correctness, behavior preservation, practical usefulness and unsupported certainty independently. Critical: stale cross-item writes, lost ordinary actions or input, invented APIs, unsupported availability. Accept valid alternatives; sample names and English strings are not required. Missing executable inputs are ungradable, not a model failure.

## Evidence
- [Source claims and negatives](../manifest.json), claim state; negative checks: state-text, modal-restore.
- [Implementation](../Sources/StateContracts.swift); [assertions](../Tests/StateContractTests.swift).
- Exact methods: `StateContractTests/testRegionPreservesOrdinaryControlAndNamedBoundary`, `StateContractTests/testSelectedStateHasNonColorTextAndValue`, `StateContractTests/testReconfigureClearsStaleSelectionText`, `StateContractTests/testReducedTransparencyDoesNotRemoveContent`, `StateContractTests/testNativePlayerControlsAndPlayerArePreserved`, `StateContractTests/testModalFlagRestoresOriginalFalse`, `StateContractTests/testRepeatedModalBeginRestoresOriginalTrue`, `StateContractTests/testCustomToggleRoleValueAndPressAgree`, `StateContractTests/testDisabledCustomControlRejectsBothActionPaths`, `StateContractTests/testOrdinaryAndAccessibilityActionUseSameStateTransition`.
- Execution: research/evaluation/cross-platform-closure-v1/results-index.json, matching manifest hash.

Inject only the separate subject question and approved condition content. Keep rubric, negative fixtures, solution, routes and incident diagnostics controller-only. No model answer has been generated or graded.

# UIKit/tvOS state-transition recovery

Draft development case; independent review pending; not a holdout. Complete starter source is included in the separate question.

Keep visible status and effective accessibility label aligned across search -> selection and repeated alternating updates. Clear an obsolete owned override or update it consistently; accept either solution. Preserve control identity, unrelated traits, normal controls, transparency adaptation, player identity and prior modal flag. Do not prescribe replacing a native control or adding an announcement to hide stale metadata. Critical: stale output, erased ordinary actions, invented APIs.

Grade correctness, preservation, practical usefulness and unsupported certainty separately. Exact helper names and English strings are not required. Getter/fallback assertions establish metadata consistency, not speech.

[Source and deliberate controls](../manifest.json); [assertions](../Tests/StateContractTests.swift).

- `StateContractTests/testSearchThenSelectionDoesNotLeaveStaleLabel`
- `StateContractTests/testRepeatedSearchAndSelectionKeepCurrentStatus`
- `StateContractTests/testRegionPreservesOrdinaryControlAndNamedBoundary`
- `StateContractTests/testSelectedStateHasNonColorTextAndValue`
- `StateContractTests/testReconfigureClearsStaleSelectionText`
- `StateContractTests/testReducedTransparencyDoesNotRemoveContent`
- `StateContractTests/testNativePlayerControlsAndPlayerArePreserved`
- `StateContractTests/testModalFlagRestoresOriginalFalse`
- `StateContractTests/testRepeatedModalBeginRestoresOriginalTrue`
- `StateContractTests/testSearchQueryAndResultCountRemainVisible`
- `StateContractTests/testSelectionPreservesUnrelatedTraits`
- `StateContractTests/testTextUsesFlexibleSemanticConfigurationWithoutOS27Claim`

The first failing native output and repaired revision remain separate in the campaign results. No independent model answer has been generated. Never inject this rubric, negative fixture or incident analysis into subject context.

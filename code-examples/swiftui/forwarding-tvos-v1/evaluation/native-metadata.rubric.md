# tvOS native-metadata

Draft development case, independent review pending; not a holdout.

Verify explicit native getters after both directions of reconfiguration, nil/empty help/status, Unicode names, disabled state, child identity/order and native heading/selected metadata. Accept equivalent native composition. Compile real representable update calls but do not infer automatic hosting propagation or SwiftUI generated semantics.

Grade correctness, preservation, usefulness and unsupported certainty separately. No exact English strings, helper names or single layout oracle is required. Invented APIs, lost ordinary actions and stale cross-item callbacks are critical when established.

[Claims and source checks](../manifest.json); [source](../Sources/NativeSurface.swift).

- `ForwardingTests/testInitialExplicitName`
- `ForwardingTests/testNamesRefreshWithoutReconstruction`
- `ForwardingTests/testValueMatchesVisibleState`
- `ForwardingTests/testBothSelectionTransitionsClearOldValue`
- `ForwardingTests/testNilStatusDoesNotLeaveOldText`
- `ForwardingTests/testEmptyStatusDoesNotAddSpuriousSeparator`
- `ForwardingTests/testHintCanBeSet`
- `ForwardingTests/testNilHintClearsOldHelp`
- `ForwardingTests/testChangedHintReplacesRatherThanAppends`
- `ForwardingTests/testDisabledStateForwardedToBothControls`
- `ForwardingTests/testReenableRestoresBothControls`
- `ForwardingTests/testControlIdentityPreservedAcrossUpdates`
- `ForwardingTests/testNamedContainerPreservesOrderedChildren`
- `ForwardingTests/testHeadingIsAddedAndRemoved`
- `ForwardingTests/testUnrelatedNativeTraitsSurviveSelection`
- `ForwardingTests/testTextConfigurationUsesScalableNativeFont`
- `ForwardingTests/testLocalizedAndUnicodeNamesPreserved`
- `ForwardingTests/testReconfigureDoesNotAccumulateChildren`

Do not inject rubric, mutants or first-failure history into the subject. Independent subject outputs are not run.

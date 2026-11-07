# Criterion-by-criterion review

Author-bound development overlay; not independent gold acceptance. Open the linked
methods for setup and exact assertion expressions. Bindings are narrow observations;
the JSON retains remaining gaps, source pins, claim leads and matching execution.
Unbound criteria are visible rather than credited through a nearby package pass.

## ios-swiftui-semantics

| Criterion | Disposition | Exact method evidence |
| --- | --- | --- |
| 1. Does not invent a defect solely from missing overrides. | unit-evidence-not-bound | Source/answer review or missing suitable assertion |
| 2. Preserves native control and its existing state binding. | unit-subset-bound | [SemanticsTests/testBindingReadsCurrentNativeToggleState](../../../code-examples/swiftui/ios-v1/Tests/SwiftUIContractsTests.swift#L7); [SemanticsTests/testBothToggleTransitionsRefreshValue](../../../code-examples/swiftui/ios-v1/Tests/SwiftUIContractsTests.swift#L10) |
| 3. Distinguishes meaningful visible naming from implementation identifiers. | unit-evidence-not-bound | Source/answer review or missing suitable assertion |

## ios-swiftui-state

| Criterion | Disposition | Exact method evidence |
| --- | --- | --- |
| 1. Clears obsolete optional metadata on the same instance. | unit-subset-bound | [SemanticsTests/testConfigureClearsPriorStatusAndPriorityWithoutReuse](../../../code-examples/swiftui/ios-v1/Tests/SwiftUIContractsTests.swift#L11); [SemanticsTests/testHintTracksCurrentAvailability](../../../code-examples/swiftui/ios-v1/Tests/SwiftUIContractsTests.swift#L18) |
| 2. Checks current item plus request identity before accepting results. | unit-subset-bound | [FormsMediaTests/testStaleTrackLoadIsIgnored](../../../code-examples/swiftui/ios-v1/Tests/SwiftUIContractsTests.swift#L68); [FormsMediaTests/testDirectEditRejectsOldSnapshot](../../../code-examples/swiftui/ios-v1/Tests/SwiftUIContractsTests.swift#L60) |
| 3. Preserves unrelated state and the ordinary Open action. | unit-subset-bound | [DocumentTests/testOrdinarySelectionUsesCurrentItem](../../../code-examples/swiftui/ios-v1/Tests/SwiftUIContractsTests.swift#L28) |

## ios-swiftui-actions

| Criterion | Disposition | Exact method evidence |
| --- | --- | --- |
| 1. Preserves independent visible ordinary actions. | unit-subset-bound | [DocumentTests/testOrdinarySelectionUsesCurrentItem](../../../code-examples/swiftui/ios-v1/Tests/SwiftUIContractsTests.swift#L28); [DocumentTests/testDeleteCurrentItemOnceAndClearSelection](../../../code-examples/swiftui/ios-v1/Tests/SwiftUIContractsTests.swift#L29) |
| 2. Shortcut uses the current file and respects enabled state. | unit-subset-bound | [DocumentTests/testOldActionDoesNotTargetReboundRow](../../../code-examples/swiftui/ios-v1/Tests/SwiftUIContractsTests.swift#L27) |
| 3. Repeated updates do not accumulate handlers or retain obsolete owners. | unit-subset-bound | [InteropTests/testCoordinatorReplacesOldCallback](../../../code-examples/swiftui/ios-v1/Tests/InteropTests.swift#L26); [InteropTests/testOldNativeViewCannotDispatchAfterRebind](../../../code-examples/swiftui/ios-v1/Tests/InteropTests.swift#L35) |

## ios-swiftui-structure

| Criterion | Disposition | Exact method evidence |
| --- | --- | --- |
| 1. Does not merge away independent controls. | unit-evidence-not-bound | Source/answer review or missing suitable assertion |
| 2. Keeps ordinary navigation and stable current item identity. | unit-subset-bound | [DocumentTests/testLandmarksAreSubsetNotEveryRow](../../../code-examples/swiftui/ios-v1/Tests/SwiftUIContractsTests.swift#L23); [DocumentTests/testSelectionSurvivesReorder](../../../code-examples/swiftui/ios-v1/Tests/SwiftUIContractsTests.swift#L25); [DocumentTests/testRemovedSelectionClears](../../../code-examples/swiftui/ios-v1/Tests/SwiftUIContractsTests.swift#L26) |
| 3. Does not claim generated tree or rotor discoverability from configuration-only units. | unit-evidence-not-bound | Source/answer review or missing suitable assertion |

## ios-swiftui-text

| Criterion | Disposition | Exact method evidence |
| --- | --- | --- |
| 1. Addresses scalable text and live integration as distinct concerns. | unit-evidence-not-bound | Source/answer review or missing suitable assertion |
| 2. Preserves Pay behavior and accepts valid layout alternatives. | unit-evidence-not-bound | Source/answer review or missing suitable assertion |
| 3. Checks platform/OS availability rather than borrowing another target’s text behavior. | unit-evidence-not-bound | Source/answer review or missing suitable assertion |
| 4. Does not equate wrapping or modifier compilation with rendered layout success. | unit-evidence-not-bound | Source/answer review or missing suitable assertion |

## ios-swiftui-lifecycle

| Criterion | Disposition | Exact method evidence |
| --- | --- | --- |
| 1. Resolves a current valid anchor at completion time. | unit-subset-bound | [LifecycleTests/testDismissResolvesCurrentOrigin](../../../code-examples/swiftui/ios-v1/Tests/SwiftUIContractsTests.swift#L46); [LifecycleTests/testEligibleListIsEvaluatedAtCompletion](../../../code-examples/swiftui/ios-v1/Tests/SwiftUIContractsTests.swift#L52); [LifecycleTests/testRemovedOriginUsesFallback](../../../code-examples/swiftui/ios-v1/Tests/SwiftUIContractsTests.swift#L47) |
| 2. Rejects stale or duplicate completion and consumes ownership before external callbacks. | unit-subset-bound | [LifecycleTests/testOldDismissalCannotConsumeNewSession](../../../code-examples/swiftui/ios-v1/Tests/SwiftUIContractsTests.swift#L48); [LifecycleTests/testRepeatedDismissIsQuiet](../../../code-examples/swiftui/ios-v1/Tests/SwiftUIContractsTests.swift#L49); [LifecycleTests/testReentrantRequestPreservesNewPresentation](../../../code-examples/swiftui/ios-v1/Tests/SwiftUIContractsTests.swift#L51) |
| 3. Distinguishes requesting restoration from proving delivered focus. | unit-evidence-not-bound | Source/answer review or missing suitable assertion |

## ios-swiftui-media

| Criterion | Disposition | Exact method evidence |
| --- | --- | --- |
| 1. Keeps loading, empty/missing, error and positive metadata distinct. | unit-subset-bound | [FormsMediaTests/testMissingAndEmptyMediaAreDifferentStates](../../../code-examples/swiftui/ios-v1/Tests/SwiftUIContractsTests.swift#L65) |
| 2. Rejects results for an obsolete player item/request. | unit-subset-bound | [FormsMediaTests/testStaleTrackLoadIsIgnored](../../../code-examples/swiftui/ios-v1/Tests/SwiftUIContractsTests.swift#L68) |
| 3. Does not change selected media options as a side effect of inspection. | unit-subset-bound | [FormsMediaTests/testMediaSelectionSurvivesReorder](../../../code-examples/swiftui/ios-v1/Tests/SwiftUIContractsTests.swift#L66); [FormsMediaTests/testMetadataChoiceDoesNotMutatePlayerPreferences](../../../code-examples/swiftui/ios-v1/Tests/SwiftUIContractsTests.swift#L70) |
| 4. Does not infer spoken description quality or complete caption support from a metadata flag. | unit-evidence-not-bound | Source/answer review or missing suitable assertion |

## ios-swiftui-testing

| Criterion | Disposition | Exact method evidence |
| --- | --- | --- |
| 1. Limits conclusions to actual assertions and compilation. | answer-protocol-or-source-review | Source/answer review or missing suitable assertion |
| 2. Keeps exact first failures separate from repairs and deliberate mutants. | answer-protocol-or-source-review | Source/answer review or missing suitable assertion |
| 3. Checks imported API names and availability on the real selected target. | answer-protocol-or-source-review | Source/answer review or missing suitable assertion |
| 4. Does not add mandatory manual verification or UI tests. | answer-protocol-or-source-review | Source/answer review or missing suitable assertion |

## macos-swiftui-semantics

| Criterion | Disposition | Exact method evidence |
| --- | --- | --- |
| 1. Does not invent a defect solely from missing overrides. | unit-evidence-not-bound | Source/answer review or missing suitable assertion |
| 2. Preserves native control and its existing state binding. | unit-subset-bound | [SemanticsTests/testBindingReadsCurrentNativeToggleState](../../../code-examples/swiftui/macos-v1/Tests/SwiftUIContractsTests.swift#L7); [SemanticsTests/testBothToggleTransitionsRefreshValue](../../../code-examples/swiftui/macos-v1/Tests/SwiftUIContractsTests.swift#L10) |
| 3. Distinguishes meaningful visible naming from implementation identifiers. | unit-evidence-not-bound | Source/answer review or missing suitable assertion |

## macos-swiftui-state

| Criterion | Disposition | Exact method evidence |
| --- | --- | --- |
| 1. Clears obsolete optional metadata on the same instance. | unit-subset-bound | [SemanticsTests/testConfigureClearsPriorStatusAndPriorityWithoutReuse](../../../code-examples/swiftui/macos-v1/Tests/SwiftUIContractsTests.swift#L11); [SemanticsTests/testHintTracksCurrentAvailability](../../../code-examples/swiftui/macos-v1/Tests/SwiftUIContractsTests.swift#L18) |
| 2. Checks current item plus request identity before accepting results. | unit-subset-bound | [FormsMediaTests/testStaleTrackLoadIsIgnored](../../../code-examples/swiftui/macos-v1/Tests/SwiftUIContractsTests.swift#L68); [FormsMediaTests/testDirectEditRejectsOldSnapshot](../../../code-examples/swiftui/macos-v1/Tests/SwiftUIContractsTests.swift#L60) |
| 3. Preserves unrelated state and the ordinary Open action. | unit-subset-bound | [DocumentTests/testOrdinarySelectionUsesCurrentItem](../../../code-examples/swiftui/macos-v1/Tests/SwiftUIContractsTests.swift#L28) |

## macos-swiftui-actions

| Criterion | Disposition | Exact method evidence |
| --- | --- | --- |
| 1. Preserves independent visible ordinary actions. | unit-subset-bound | [DocumentTests/testOrdinarySelectionUsesCurrentItem](../../../code-examples/swiftui/macos-v1/Tests/SwiftUIContractsTests.swift#L28); [DocumentTests/testDeleteCurrentItemOnceAndClearSelection](../../../code-examples/swiftui/macos-v1/Tests/SwiftUIContractsTests.swift#L29) |
| 2. Shortcut uses the current file and respects enabled state. | unit-subset-bound | [DocumentTests/testOldActionDoesNotTargetReboundRow](../../../code-examples/swiftui/macos-v1/Tests/SwiftUIContractsTests.swift#L27) |
| 3. Repeated updates do not accumulate handlers or retain obsolete owners. | unit-subset-bound | [InteropTests/testCoordinatorReplacesOldCallback](../../../code-examples/swiftui/macos-v1/Tests/InteropTests.swift#L26); [InteropTests/testOldNativeViewCannotDispatchAfterRebind](../../../code-examples/swiftui/macos-v1/Tests/InteropTests.swift#L35) |

## macos-swiftui-structure

| Criterion | Disposition | Exact method evidence |
| --- | --- | --- |
| 1. Does not merge away independent controls. | unit-evidence-not-bound | Source/answer review or missing suitable assertion |
| 2. Keeps ordinary navigation and stable current item identity. | unit-subset-bound | [DocumentTests/testLandmarksAreSubsetNotEveryRow](../../../code-examples/swiftui/macos-v1/Tests/SwiftUIContractsTests.swift#L23); [DocumentTests/testSelectionSurvivesReorder](../../../code-examples/swiftui/macos-v1/Tests/SwiftUIContractsTests.swift#L25); [DocumentTests/testRemovedSelectionClears](../../../code-examples/swiftui/macos-v1/Tests/SwiftUIContractsTests.swift#L26) |
| 3. Does not claim generated tree or rotor discoverability from configuration-only units. | unit-evidence-not-bound | Source/answer review or missing suitable assertion |

## macos-swiftui-text

| Criterion | Disposition | Exact method evidence |
| --- | --- | --- |
| 1. Addresses scalable text and live integration as distinct concerns. | unit-evidence-not-bound | Source/answer review or missing suitable assertion |
| 2. Preserves Pay behavior and accepts valid layout alternatives. | unit-evidence-not-bound | Source/answer review or missing suitable assertion |
| 3. Checks platform/OS availability rather than borrowing another target’s text behavior. | unit-evidence-not-bound | Source/answer review or missing suitable assertion |
| 4. Does not equate wrapping or modifier compilation with rendered layout success. | unit-evidence-not-bound | Source/answer review or missing suitable assertion |

## macos-swiftui-lifecycle

| Criterion | Disposition | Exact method evidence |
| --- | --- | --- |
| 1. Resolves a current valid anchor at completion time. | unit-subset-bound | [LifecycleTests/testDismissResolvesCurrentOrigin](../../../code-examples/swiftui/macos-v1/Tests/SwiftUIContractsTests.swift#L46); [LifecycleTests/testEligibleListIsEvaluatedAtCompletion](../../../code-examples/swiftui/macos-v1/Tests/SwiftUIContractsTests.swift#L52); [LifecycleTests/testRemovedOriginUsesFallback](../../../code-examples/swiftui/macos-v1/Tests/SwiftUIContractsTests.swift#L47) |
| 2. Rejects stale or duplicate completion and consumes ownership before external callbacks. | unit-subset-bound | [LifecycleTests/testOldDismissalCannotConsumeNewSession](../../../code-examples/swiftui/macos-v1/Tests/SwiftUIContractsTests.swift#L48); [LifecycleTests/testRepeatedDismissIsQuiet](../../../code-examples/swiftui/macos-v1/Tests/SwiftUIContractsTests.swift#L49); [LifecycleTests/testReentrantRequestPreservesNewPresentation](../../../code-examples/swiftui/macos-v1/Tests/SwiftUIContractsTests.swift#L51) |
| 3. Distinguishes requesting restoration from proving delivered focus. | unit-evidence-not-bound | Source/answer review or missing suitable assertion |

## macos-swiftui-media

| Criterion | Disposition | Exact method evidence |
| --- | --- | --- |
| 1. Keeps loading, empty/missing, error and positive metadata distinct. | unit-subset-bound | [FormsMediaTests/testMissingAndEmptyMediaAreDifferentStates](../../../code-examples/swiftui/macos-v1/Tests/SwiftUIContractsTests.swift#L65) |
| 2. Rejects results for an obsolete player item/request. | unit-subset-bound | [FormsMediaTests/testStaleTrackLoadIsIgnored](../../../code-examples/swiftui/macos-v1/Tests/SwiftUIContractsTests.swift#L68) |
| 3. Does not change selected media options as a side effect of inspection. | unit-subset-bound | [FormsMediaTests/testMediaSelectionSurvivesReorder](../../../code-examples/swiftui/macos-v1/Tests/SwiftUIContractsTests.swift#L66); [FormsMediaTests/testMetadataChoiceDoesNotMutatePlayerPreferences](../../../code-examples/swiftui/macos-v1/Tests/SwiftUIContractsTests.swift#L70) |
| 4. Does not infer spoken description quality or complete caption support from a metadata flag. | unit-evidence-not-bound | Source/answer review or missing suitable assertion |

## macos-swiftui-testing

| Criterion | Disposition | Exact method evidence |
| --- | --- | --- |
| 1. Limits conclusions to actual assertions and compilation. | answer-protocol-or-source-review | Source/answer review or missing suitable assertion |
| 2. Keeps exact first failures separate from repairs and deliberate mutants. | answer-protocol-or-source-review | Source/answer review or missing suitable assertion |
| 3. Checks imported API names and availability on the real selected target. | answer-protocol-or-source-review | Source/answer review or missing suitable assertion |
| 4. Does not add mandatory manual verification or UI tests. | answer-protocol-or-source-review | Source/answer review or missing suitable assertion |

## tvos-swiftui-semantics

| Criterion | Disposition | Exact method evidence |
| --- | --- | --- |
| 1. Does not invent a defect solely from missing overrides. | unit-evidence-not-bound | Source/answer review or missing suitable assertion |
| 2. Preserves native control and its existing state binding. | unit-subset-bound | [SemanticsTests/testBindingReadsCurrentNativeToggleState](../../../code-examples/swiftui/tvos-v1/Tests/SwiftUIContractsTests.swift#L7); [SemanticsTests/testBothToggleTransitionsRefreshValue](../../../code-examples/swiftui/tvos-v1/Tests/SwiftUIContractsTests.swift#L10) |
| 3. Distinguishes meaningful visible naming from implementation identifiers. | unit-evidence-not-bound | Source/answer review or missing suitable assertion |

## tvos-swiftui-state

| Criterion | Disposition | Exact method evidence |
| --- | --- | --- |
| 1. Clears obsolete optional metadata on the same instance. | unit-subset-bound | [SemanticsTests/testConfigureClearsPriorStatusAndPriorityWithoutReuse](../../../code-examples/swiftui/tvos-v1/Tests/SwiftUIContractsTests.swift#L11); [SemanticsTests/testHintTracksCurrentAvailability](../../../code-examples/swiftui/tvos-v1/Tests/SwiftUIContractsTests.swift#L18) |
| 2. Checks current item plus request identity before accepting results. | unit-subset-bound | [FormsMediaTests/testStaleTrackLoadIsIgnored](../../../code-examples/swiftui/tvos-v1/Tests/SwiftUIContractsTests.swift#L68); [FormsMediaTests/testDirectEditRejectsOldSnapshot](../../../code-examples/swiftui/tvos-v1/Tests/SwiftUIContractsTests.swift#L60) |
| 3. Preserves unrelated state and the ordinary Open action. | unit-subset-bound | [DocumentTests/testOrdinarySelectionUsesCurrentItem](../../../code-examples/swiftui/tvos-v1/Tests/SwiftUIContractsTests.swift#L28) |

## tvos-swiftui-actions

| Criterion | Disposition | Exact method evidence |
| --- | --- | --- |
| 1. Preserves independent visible ordinary actions. | unit-subset-bound | [DocumentTests/testOrdinarySelectionUsesCurrentItem](../../../code-examples/swiftui/tvos-v1/Tests/SwiftUIContractsTests.swift#L28); [DocumentTests/testDeleteCurrentItemOnceAndClearSelection](../../../code-examples/swiftui/tvos-v1/Tests/SwiftUIContractsTests.swift#L29) |
| 2. Shortcut uses the current file and respects enabled state. | unit-subset-bound | [DocumentTests/testOldActionDoesNotTargetReboundRow](../../../code-examples/swiftui/tvos-v1/Tests/SwiftUIContractsTests.swift#L27) |
| 3. Repeated updates do not accumulate handlers or retain obsolete owners. | unit-subset-bound | [InteropTests/testCoordinatorReplacesOldCallback](../../../code-examples/swiftui/tvos-v1/Tests/InteropTests.swift#L26); [InteropTests/testOldNativeViewCannotDispatchAfterRebind](../../../code-examples/swiftui/tvos-v1/Tests/InteropTests.swift#L35) |

## tvos-swiftui-structure

| Criterion | Disposition | Exact method evidence |
| --- | --- | --- |
| 1. Does not merge away independent controls. | unit-evidence-not-bound | Source/answer review or missing suitable assertion |
| 2. Keeps ordinary navigation and stable current item identity. | unit-subset-bound | [DocumentTests/testLandmarksAreSubsetNotEveryRow](../../../code-examples/swiftui/tvos-v1/Tests/SwiftUIContractsTests.swift#L23); [DocumentTests/testSelectionSurvivesReorder](../../../code-examples/swiftui/tvos-v1/Tests/SwiftUIContractsTests.swift#L25); [DocumentTests/testRemovedSelectionClears](../../../code-examples/swiftui/tvos-v1/Tests/SwiftUIContractsTests.swift#L26) |
| 3. Does not claim generated tree or rotor discoverability from configuration-only units. | unit-evidence-not-bound | Source/answer review or missing suitable assertion |

## tvos-swiftui-text

| Criterion | Disposition | Exact method evidence |
| --- | --- | --- |
| 1. Addresses scalable text and live integration as distinct concerns. | unit-evidence-not-bound | Source/answer review or missing suitable assertion |
| 2. Preserves Pay behavior and accepts valid layout alternatives. | unit-evidence-not-bound | Source/answer review or missing suitable assertion |
| 3. Checks platform/OS availability rather than borrowing another target’s text behavior. | unit-evidence-not-bound | Source/answer review or missing suitable assertion |
| 4. Does not equate wrapping or modifier compilation with rendered layout success. | unit-evidence-not-bound | Source/answer review or missing suitable assertion |

## tvos-swiftui-lifecycle

| Criterion | Disposition | Exact method evidence |
| --- | --- | --- |
| 1. Resolves a current valid anchor at completion time. | unit-subset-bound | [LifecycleTests/testDismissResolvesCurrentOrigin](../../../code-examples/swiftui/tvos-v1/Tests/SwiftUIContractsTests.swift#L46); [LifecycleTests/testEligibleListIsEvaluatedAtCompletion](../../../code-examples/swiftui/tvos-v1/Tests/SwiftUIContractsTests.swift#L52); [LifecycleTests/testRemovedOriginUsesFallback](../../../code-examples/swiftui/tvos-v1/Tests/SwiftUIContractsTests.swift#L47) |
| 2. Rejects stale or duplicate completion and consumes ownership before external callbacks. | unit-subset-bound | [LifecycleTests/testOldDismissalCannotConsumeNewSession](../../../code-examples/swiftui/tvos-v1/Tests/SwiftUIContractsTests.swift#L48); [LifecycleTests/testRepeatedDismissIsQuiet](../../../code-examples/swiftui/tvos-v1/Tests/SwiftUIContractsTests.swift#L49); [LifecycleTests/testReentrantRequestPreservesNewPresentation](../../../code-examples/swiftui/tvos-v1/Tests/SwiftUIContractsTests.swift#L51) |
| 3. Distinguishes requesting restoration from proving delivered focus. | unit-evidence-not-bound | Source/answer review or missing suitable assertion |

## tvos-swiftui-media

| Criterion | Disposition | Exact method evidence |
| --- | --- | --- |
| 1. Keeps loading, empty/missing, error and positive metadata distinct. | unit-subset-bound | [FormsMediaTests/testMissingAndEmptyMediaAreDifferentStates](../../../code-examples/swiftui/tvos-v1/Tests/SwiftUIContractsTests.swift#L65) |
| 2. Rejects results for an obsolete player item/request. | unit-subset-bound | [FormsMediaTests/testStaleTrackLoadIsIgnored](../../../code-examples/swiftui/tvos-v1/Tests/SwiftUIContractsTests.swift#L68) |
| 3. Does not change selected media options as a side effect of inspection. | unit-subset-bound | [FormsMediaTests/testMediaSelectionSurvivesReorder](../../../code-examples/swiftui/tvos-v1/Tests/SwiftUIContractsTests.swift#L66); [FormsMediaTests/testMetadataChoiceDoesNotMutatePlayerPreferences](../../../code-examples/swiftui/tvos-v1/Tests/SwiftUIContractsTests.swift#L70) |
| 4. Does not infer spoken description quality or complete caption support from a metadata flag. | unit-evidence-not-bound | Source/answer review or missing suitable assertion |

## tvos-swiftui-testing

| Criterion | Disposition | Exact method evidence |
| --- | --- | --- |
| 1. Limits conclusions to actual assertions and compilation. | answer-protocol-or-source-review | Source/answer review or missing suitable assertion |
| 2. Keeps exact first failures separate from repairs and deliberate mutants. | answer-protocol-or-source-review | Source/answer review or missing suitable assertion |
| 3. Checks imported API names and availability on the real selected target. | answer-protocol-or-source-review | Source/answer review or missing suitable assertion |
| 4. Does not add mandatory manual verification or UI tests. | answer-protocol-or-source-review | Source/answer review or missing suitable assertion |

## ios-uikit-semantics

| Criterion | Disposition | Exact method evidence |
| --- | --- | --- |
| 1. Does not invent a defect solely from missing overrides. | unit-evidence-not-bound | Source/answer review or missing suitable assertion |
| 2. Preserves native control and its existing state binding. | unit-evidence-not-bound | Source/answer review or missing suitable assertion |
| 3. Distinguishes meaningful visible naming from implementation identifiers. | unit-evidence-not-bound | Source/answer review or missing suitable assertion |

## ios-uikit-state

| Criterion | Disposition | Exact method evidence |
| --- | --- | --- |
| 1. Clears obsolete optional metadata on the same instance. | unit-subset-bound | [UIKitSemanticsTests/testReconfigurationClearsStaleHintAndValue](../../../code-examples/pilots/uikit-semantics-v1/Tests/UIKitSemanticsTests.swift#L13) |
| 2. Checks current item plus request identity before accepting results. | unit-subset-bound | [MediaLoadOwnerTests/testReplacementRejectsOldItemCompletion](../../../code-examples/platforms/ios-closure-v1/Tests/AsyncOwnershipTests.swift#L84); [MediaLoadOwnerTests/testSameItemNewRequestRejectsOldGeneration](../../../code-examples/platforms/ios-closure-v1/Tests/AsyncOwnershipTests.swift#L89); [MediaLoadOwnerTests/testExternalReplacementRejectsOldResult](../../../code-examples/platforms/ios-closure-v1/Tests/AsyncOwnershipTests.swift#L95) |
| 3. Preserves unrelated state and the ordinary Open action. | unit-subset-bound | [DynamicUIKitTests/testOrdinaryButtonsUseCurrentItemAfterReuse](../../../code-examples/pilots/uikit-dynamic-v1/Tests/DynamicUIKitTests.swift#L88) |

## ios-uikit-actions

| Criterion | Disposition | Exact method evidence |
| --- | --- | --- |
| 1. Preserves independent visible ordinary actions. | unit-subset-bound | [DynamicUIKitTests/testOrdinaryButtonsUseCurrentItemAfterReuse](../../../code-examples/pilots/uikit-dynamic-v1/Tests/DynamicUIKitTests.swift#L88) |
| 2. Shortcut uses the current file and respects enabled state. | unit-subset-bound | [DynamicUIKitTests/testRetainedOldActionCannotAffectReusedView](../../../code-examples/pilots/uikit-dynamic-v1/Tests/DynamicUIKitTests.swift#L101); [DynamicUIKitTests/testDisableAndReenableRefreshesBothActionPaths](../../../code-examples/pilots/uikit-dynamic-v1/Tests/DynamicUIKitTests.swift#L110) |
| 3. Repeated updates do not accumulate handlers or retain obsolete owners. | unit-subset-bound | [DynamicUIKitTests/testRetainedCustomActionDoesNotKeepViewAlive](../../../code-examples/pilots/uikit-dynamic-v1/Tests/DynamicUIKitTests.swift#L125); [DynamicUIKitTests/testNativeActionIdentifierReplacesPreviousHandler](../../../code-examples/pilots/uikit-dynamic-v1/Tests/DynamicUIKitTests.swift#L147) |

## ios-uikit-structure

| Criterion | Disposition | Exact method evidence |
| --- | --- | --- |
| 1. Does not merge away independent controls. | unit-subset-bound | [NamingUIKitTests/testContainerPreservesIndependentControls](../../../code-examples/pilots/uikit-naming-v1/Tests/NamingUIKitTests.swift#L22) |
| 2. Keeps ordinary navigation and stable current item identity. | unit-subset-bound | [DynamicUIKitTests/testReorderPreservesIdentityAndChangesSearchOrder](../../../code-examples/pilots/uikit-dynamic-v1/Tests/DynamicUIKitTests.swift#L20); [DynamicUIKitTests/testRemovedCurrentItemUsesDeclaredBoundaryPolicy](../../../code-examples/pilots/uikit-dynamic-v1/Tests/DynamicUIKitTests.swift#L31) |
| 3. Does not claim generated tree or rotor discoverability from configuration-only units. | unit-evidence-not-bound | Source/answer review or missing suitable assertion |

## ios-uikit-text

| Criterion | Disposition | Exact method evidence |
| --- | --- | --- |
| 1. Addresses scalable text and live integration as distinct concerns. | unit-subset-bound | [ChoiceUIKitTests/testFontsMatchEffectiveLargeTextEnvironment](../../../code-examples/pilots/uikit-choice-v1/Tests/ChoiceUIKitTests.swift#L49); [ChoiceUIKitTests/testRepeatedSizeTransitionsDoNotAccumulateScaling](../../../code-examples/pilots/uikit-choice-v1/Tests/ChoiceUIKitTests.swift#L60) |
| 2. Preserves Pay behavior and accepts valid layout alternatives. | unit-subset-bound | [ChoiceUIKitTests/testLongLocalizedContentRemainsVerbatim](../../../code-examples/pilots/uikit-choice-v1/Tests/ChoiceUIKitTests.swift#L23); [ChoiceUIKitTests/testSelfSizingConfigurationAndVerticalConstraintChain](../../../code-examples/pilots/uikit-choice-v1/Tests/ChoiceUIKitTests.swift#L116) |
| 3. Checks platform/OS availability rather than borrowing another target’s text behavior. | unit-evidence-not-bound | Source/answer review or missing suitable assertion |
| 4. Does not equate wrapping or modifier compilation with rendered layout success. | unit-evidence-not-bound | Source/answer review or missing suitable assertion |

## ios-uikit-lifecycle

| Criterion | Disposition | Exact method evidence |
| --- | --- | --- |
| 1. Resolves a current valid anchor at completion time. | unit-subset-bound | [ModalUIKitTests/testNotificationWaitsForCompletionAndUsesCurrentTarget](../../../code-examples/pilots/uikit-modal-v1/Tests/ModalUIKitTests.swift#L49); [ModalUIKitTests/testRetainedButRemovedTargetPostsNil](../../../code-examples/pilots/uikit-modal-v1/Tests/ModalUIKitTests.swift#L173) |
| 2. Rejects stale or duplicate completion and consumes ownership before external callbacks. | unit-subset-bound | [ModalUIKitTests/testOldCompletionCannotCloseReopenedPanel](../../../code-examples/pilots/uikit-modal-v1/Tests/ModalUIKitTests.swift#L135); [ModalUIKitTests/testOrdinaryCloseAndEscapeShareDismissalGuard](../../../code-examples/pilots/uikit-modal-v1/Tests/ModalUIKitTests.swift#L74) |
| 3. Distinguishes requesting restoration from proving delivered focus. | unit-evidence-not-bound | Source/answer review or missing suitable assertion |

## ios-uikit-media

| Criterion | Disposition | Exact method evidence |
| --- | --- | --- |
| 1. Keeps loading, empty/missing, error and positive metadata distinct. | unit-subset-bound | [MediaLoadOwnerTests/testNilItemDoesNotInvokeLoader](../../../code-examples/platforms/ios-closure-v1/Tests/AsyncOwnershipTests.swift#L80); [MediaLoadOwnerTests/testErrorIsNotMissingOrSuccessfulMetadata](../../../code-examples/platforms/ios-closure-v1/Tests/AsyncOwnershipTests.swift#L105); [MediaLoadOwnerTests/testSameItemNewRequestRejectsOldGeneration](../../../code-examples/platforms/ios-closure-v1/Tests/AsyncOwnershipTests.swift#L89); [MediaMetadataTests/testKnownMissingGroupIsAbsent](../../../code-examples/pilots/uikit-media-metadata-v1/Tests/MediaMetadataTests.swift#L73); [MediaMetadataTests/testMissingItemIsUnavailableRatherThanAbsent](../../../code-examples/pilots/uikit-media-metadata-v1/Tests/MediaMetadataTests.swift#L66) |
| 2. Rejects results for an obsolete player item/request. | unit-subset-bound | [MediaLoadOwnerTests/testReplacementRejectsOldItemCompletion](../../../code-examples/platforms/ios-closure-v1/Tests/AsyncOwnershipTests.swift#L84); [MediaLoadOwnerTests/testExternalReplacementRejectsOldResult](../../../code-examples/platforms/ios-closure-v1/Tests/AsyncOwnershipTests.swift#L95) |
| 3. Does not change selected media options as a side effect of inspection. | unit-subset-bound | [MediaMetadataTests/testInspectionPreservesChosenAudioAndSubtitleOff](../../../code-examples/pilots/uikit-media-metadata-v1/Tests/MediaMetadataTests.swift#L32) |
| 4. Does not infer spoken description quality or complete caption support from a metadata flag. | unit-evidence-not-bound | Source/answer review or missing suitable assertion |

## ios-uikit-testing

| Criterion | Disposition | Exact method evidence |
| --- | --- | --- |
| 1. Limits conclusions to actual assertions and compilation. | answer-protocol-or-source-review | Source/answer review or missing suitable assertion |
| 2. Keeps exact first failures separate from repairs and deliberate mutants. | answer-protocol-or-source-review | Source/answer review or missing suitable assertion |
| 3. Checks imported API names and availability on the real selected target. | answer-protocol-or-source-review | Source/answer review or missing suitable assertion |
| 4. Does not add mandatory manual verification or UI tests. | answer-protocol-or-source-review | Source/answer review or missing suitable assertion |

## tvos-uikit-semantics

| Criterion | Disposition | Exact method evidence |
| --- | --- | --- |
| 1. Does not invent a defect solely from missing overrides. | unit-evidence-not-bound | Source/answer review or missing suitable assertion |
| 2. Preserves native control and its existing state binding. | unit-evidence-not-bound | Source/answer review or missing suitable assertion |
| 3. Distinguishes meaningful visible naming from implementation identifiers. | unit-evidence-not-bound | Source/answer review or missing suitable assertion |

## tvos-uikit-state

| Criterion | Disposition | Exact method evidence |
| --- | --- | --- |
| 1. Clears obsolete optional metadata on the same instance. | unit-subset-bound | [StateContractTests/testReconfigureClearsStaleSelectionText](../../../code-examples/platforms/tvos-state-recovery-v1/Tests/StateContractTests.swift#L33) |
| 2. Checks current item plus request identity before accepting results. | unit-subset-bound | [MediaLoadOwnerTests/testReplacementRejectsOldItemCompletion](../../../code-examples/platforms/tvos-closure-v1/Tests/AsyncOwnershipTests.swift#L84); [MediaLoadOwnerTests/testSameItemNewRequestRejectsOldGeneration](../../../code-examples/platforms/tvos-closure-v1/Tests/AsyncOwnershipTests.swift#L89); [MediaLoadOwnerTests/testExternalReplacementRejectsOldResult](../../../code-examples/platforms/tvos-closure-v1/Tests/AsyncOwnershipTests.swift#L95) |
| 3. Preserves unrelated state and the ordinary Open action. | unit-subset-bound | [TelevisionActionsTests/testOrdinaryPlay](../../../code-examples/platforms/tvos-uikit-v1/Tests/TelevisionActionsTests.swift#L17); [TelevisionActionsTests/testOrdinaryDetails](../../../code-examples/platforms/tvos-uikit-v1/Tests/TelevisionActionsTests.swift#L18) |

## tvos-uikit-actions

| Criterion | Disposition | Exact method evidence |
| --- | --- | --- |
| 1. Preserves independent visible ordinary actions. | unit-subset-bound | [TelevisionActionsTests/testOrdinaryPlay](../../../code-examples/platforms/tvos-uikit-v1/Tests/TelevisionActionsTests.swift#L17); [TelevisionActionsTests/testOrdinaryDetails](../../../code-examples/platforms/tvos-uikit-v1/Tests/TelevisionActionsTests.swift#L18) |
| 2. Shortcut uses the current file and respects enabled state. | unit-subset-bound | [TelevisionActionsTests/testStaleActionRejected](../../../code-examples/platforms/tvos-uikit-v1/Tests/TelevisionActionsTests.swift#L20); [TelevisionActionsTests/testDisabledOrdinaryAction](../../../code-examples/platforms/tvos-uikit-v1/Tests/TelevisionActionsTests.swift#L24); [TelevisionActionsTests/testDisabledCustomAction](../../../code-examples/platforms/tvos-uikit-v1/Tests/TelevisionActionsTests.swift#L25) |
| 3. Repeated updates do not accumulate handlers or retain obsolete owners. | unit-subset-bound | [TelevisionActionsTests/testSingleShortcutAfterReuse](../../../code-examples/platforms/tvos-uikit-v1/Tests/TelevisionActionsTests.swift#L27); [TelevisionActionsTests/testActionDoesNotRetainRow](../../../code-examples/platforms/tvos-uikit-v1/Tests/TelevisionActionsTests.swift#L26) |

## tvos-uikit-structure

| Criterion | Disposition | Exact method evidence |
| --- | --- | --- |
| 1. Does not merge away independent controls. | unit-subset-bound | [TelevisionActionsTests/testContainerPreservesControls](../../../code-examples/platforms/tvos-uikit-v1/Tests/TelevisionActionsTests.swift#L16) |
| 2. Keeps ordinary navigation and stable current item identity. | unit-subset-bound | [EditedRotorUIKitTests/testNewRevisionRestartsRetainedResult](../../../code-examples/platforms/tvos-closure-v1/Tests/EditedRotorUIKitTests.swift#L67); [EditedRotorUIKitTests/testEmptyQueryUpdatesOrdinaryDocumentWithoutRotor](../../../code-examples/platforms/tvos-closure-v1/Tests/EditedRotorUIKitTests.swift#L96) |
| 3. Does not claim generated tree or rotor discoverability from configuration-only units. | unit-evidence-not-bound | Source/answer review or missing suitable assertion |

## tvos-uikit-text

| Criterion | Disposition | Exact method evidence |
| --- | --- | --- |
| 1. Addresses scalable text and live integration as distinct concerns. | unit-subset-bound | [StateContractTests/testTextUsesFlexibleSemanticConfigurationWithoutOS27Claim](../../../code-examples/platforms/tvos-closure-v1/Tests/StateContractTests.swift#L57) |
| 2. Preserves Pay behavior and accepts valid layout alternatives. | unit-evidence-not-bound | Source/answer review or missing suitable assertion |
| 3. Checks platform/OS availability rather than borrowing another target’s text behavior. | unit-evidence-not-bound | Source/answer review or missing suitable assertion |
| 4. Does not equate wrapping or modifier compilation with rendered layout success. | unit-evidence-not-bound | Source/answer review or missing suitable assertion |

## tvos-uikit-lifecycle

| Criterion | Disposition | Exact method evidence |
| --- | --- | --- |
| 1. Resolves a current valid anchor at completion time. | unit-subset-bound | [TelevisionLifecycleTests/testCompletedModalRequestsOriginal](../../../code-examples/platforms/tvos-lifecycle-v1/Tests/TelevisionLifecycleTests.swift#L42); [TelevisionLifecycleTests/testRemovedOriginalUsesFallback](../../../code-examples/platforms/tvos-lifecycle-v1/Tests/TelevisionLifecycleTests.swift#L43) |
| 2. Rejects stale or duplicate completion and consumes ownership before external callbacks. | unit-subset-bound | [TelevisionLifecycleTests/testOldCompletionCannotConsumeNewSession](../../../code-examples/platforms/tvos-lifecycle-v1/Tests/TelevisionLifecycleTests.swift#L47); [TelevisionLifecycleTests/testDuplicateCompletionIsQuiet](../../../code-examples/platforms/tvos-lifecycle-v1/Tests/TelevisionLifecycleTests.swift#L48); [TelevisionLifecycleTests/testReentrantRequestPreservesNewSession](../../../code-examples/platforms/tvos-lifecycle-v1/Tests/TelevisionLifecycleTests.swift#L53) |
| 3. Distinguishes requesting restoration from proving delivered focus. | unit-evidence-not-bound | Source/answer review or missing suitable assertion |

## tvos-uikit-media

| Criterion | Disposition | Exact method evidence |
| --- | --- | --- |
| 1. Keeps loading, empty/missing, error and positive metadata distinct. | unit-subset-bound | [MediaLoadOwnerTests/testNilItemDoesNotInvokeLoader](../../../code-examples/platforms/tvos-closure-v1/Tests/AsyncOwnershipTests.swift#L80); [MediaLoadOwnerTests/testErrorIsNotMissingOrSuccessfulMetadata](../../../code-examples/platforms/tvos-closure-v1/Tests/AsyncOwnershipTests.swift#L105); [MediaLoadOwnerTests/testSameItemNewRequestRejectsOldGeneration](../../../code-examples/platforms/tvos-closure-v1/Tests/AsyncOwnershipTests.swift#L89); [MediaMetadataTests/testKnownMissingGroupIsAbsent](../../../code-examples/platforms/tvos-media-v1/Tests/MediaMetadataTests.swift#L73); [MediaMetadataTests/testMissingItemIsUnavailableRatherThanAbsent](../../../code-examples/platforms/tvos-media-v1/Tests/MediaMetadataTests.swift#L66) |
| 2. Rejects results for an obsolete player item/request. | unit-subset-bound | [MediaLoadOwnerTests/testReplacementRejectsOldItemCompletion](../../../code-examples/platforms/tvos-closure-v1/Tests/AsyncOwnershipTests.swift#L84); [MediaLoadOwnerTests/testExternalReplacementRejectsOldResult](../../../code-examples/platforms/tvos-closure-v1/Tests/AsyncOwnershipTests.swift#L95) |
| 3. Does not change selected media options as a side effect of inspection. | unit-subset-bound | [MediaMetadataTests/testInspectionPreservesChosenAudioAndSubtitleOff](../../../code-examples/platforms/tvos-media-v1/Tests/MediaMetadataTests.swift#L32) |
| 4. Does not infer spoken description quality or complete caption support from a metadata flag. | unit-evidence-not-bound | Source/answer review or missing suitable assertion |

## tvos-uikit-testing

| Criterion | Disposition | Exact method evidence |
| --- | --- | --- |
| 1. Limits conclusions to actual assertions and compilation. | answer-protocol-or-source-review | Source/answer review or missing suitable assertion |
| 2. Keeps exact first failures separate from repairs and deliberate mutants. | answer-protocol-or-source-review | Source/answer review or missing suitable assertion |
| 3. Checks imported API names and availability on the real selected target. | answer-protocol-or-source-review | Source/answer review or missing suitable assertion |
| 4. Does not add mandatory manual verification or UI tests. | answer-protocol-or-source-review | Source/answer review or missing suitable assertion |

## macos-appkit-semantics

| Criterion | Disposition | Exact method evidence |
| --- | --- | --- |
| 1. Does not invent a defect solely from missing overrides. | unit-evidence-not-bound | Source/answer review or missing suitable assertion |
| 2. Preserves native control and its existing state binding. | unit-evidence-not-bound | Source/answer review or missing suitable assertion |
| 3. Distinguishes meaningful visible naming from implementation identifiers. | unit-evidence-not-bound | Source/answer review or missing suitable assertion |

## macos-appkit-state

| Criterion | Disposition | Exact method evidence |
| --- | --- | --- |
| 1. Clears obsolete optional metadata on the same instance. | unit-subset-bound | [DesktopActionsTests/testReuseClearsOwnedValue](../../../code-examples/platforms/macos-appkit-v1/Tests/DesktopActionsTests.swift#L28) |
| 2. Checks current item plus request identity before accepting results. | unit-subset-bound | [MediaLoadOwnerTests/testReplacementRejectsOldItemCompletion](../../../code-examples/platforms/macos-closure-v1/Tests/AsyncOwnershipTests.swift#L84); [MediaLoadOwnerTests/testSameItemNewRequestRejectsOldGeneration](../../../code-examples/platforms/macos-closure-v1/Tests/AsyncOwnershipTests.swift#L89); [MediaLoadOwnerTests/testExternalReplacementRejectsOldResult](../../../code-examples/platforms/macos-closure-v1/Tests/AsyncOwnershipTests.swift#L95) |
| 3. Preserves unrelated state and the ordinary Open action. | unit-subset-bound | [DesktopActionsTests/testOrdinaryOpenOnly](../../../code-examples/platforms/macos-appkit-v1/Tests/DesktopActionsTests.swift#L21); [DesktopActionsTests/testOrdinarySaveOnly](../../../code-examples/platforms/macos-appkit-v1/Tests/DesktopActionsTests.swift#L22) |

## macos-appkit-actions

| Criterion | Disposition | Exact method evidence |
| --- | --- | --- |
| 1. Preserves independent visible ordinary actions. | unit-subset-bound | [DesktopActionsTests/testOrdinaryOpenOnly](../../../code-examples/platforms/macos-appkit-v1/Tests/DesktopActionsTests.swift#L21); [DesktopActionsTests/testOrdinarySaveOnly](../../../code-examples/platforms/macos-appkit-v1/Tests/DesktopActionsTests.swift#L22) |
| 2. Shortcut uses the current file and respects enabled state. | unit-subset-bound | [DesktopActionsTests/testStaleShortcutRejected](../../../code-examples/platforms/macos-appkit-v1/Tests/DesktopActionsTests.swift#L25); [DesktopActionsTests/testDisabledOrdinarySave](../../../code-examples/platforms/macos-appkit-v1/Tests/DesktopActionsTests.swift#L29); [DesktopActionsTests/testDisabledShortcut](../../../code-examples/platforms/macos-appkit-v1/Tests/DesktopActionsTests.swift#L30) |
| 3. Repeated updates do not accumulate handlers or retain obsolete owners. | unit-subset-bound | [DesktopActionsTests/testRepeatedConfigurationDoesNotDuplicateActions](../../../code-examples/platforms/macos-appkit-v1/Tests/DesktopActionsTests.swift#L33); [DesktopActionsTests/testShortcutDoesNotRetainRow](../../../code-examples/platforms/macos-appkit-v1/Tests/DesktopActionsTests.swift#L32) |

## macos-appkit-structure

| Criterion | Disposition | Exact method evidence |
| --- | --- | --- |
| 1. Does not merge away independent controls. | unit-subset-bound | [DesktopActionsTests/testContainerDoesNotReplaceControls](../../../code-examples/platforms/macos-appkit-v1/Tests/DesktopActionsTests.swift#L19) |
| 2. Keeps ordinary navigation and stable current item identity. | unit-subset-bound | [DesktopOutlineTests/testSelectedChildSurvivesSiblingReorder](../../../code-examples/platforms/macos-structure-v1/Tests/DesktopOutlineTests.swift#L47); [DesktopOutlineTests/testRemovedSelectionClears](../../../code-examples/platforms/macos-structure-v1/Tests/DesktopOutlineTests.swift#L53) |
| 3. Does not claim generated tree or rotor discoverability from configuration-only units. | unit-evidence-not-bound | Source/answer review or missing suitable assertion |

## macos-appkit-text

| Criterion | Disposition | Exact method evidence |
| --- | --- | --- |
| 1. Addresses scalable text and live integration as distinct concerns. | unit-evidence-not-bound | Source/answer review or missing suitable assertion |
| 2. Preserves Pay behavior and accepts valid layout alternatives. | unit-evidence-not-bound | Source/answer review or missing suitable assertion |
| 3. Checks platform/OS availability rather than borrowing another target’s text behavior. | unit-evidence-not-bound | Source/answer review or missing suitable assertion |
| 4. Does not equate wrapping or modifier compilation with rendered layout success. | unit-evidence-not-bound | Source/answer review or missing suitable assertion |

## macos-appkit-lifecycle

| Criterion | Disposition | Exact method evidence |
| --- | --- | --- |
| 1. Resolves a current valid anchor at completion time. | unit-subset-bound | [DesktopLifecycleTests/testCompletedModalRequestsOriginal](../../../code-examples/platforms/macos-lifecycle-v1/Tests/DesktopLifecycleTests.swift#L43); [DesktopLifecycleTests/testRemovedOriginalUsesFallback](../../../code-examples/platforms/macos-lifecycle-v1/Tests/DesktopLifecycleTests.swift#L44) |
| 2. Rejects stale or duplicate completion and consumes ownership before external callbacks. | unit-subset-bound | [DesktopLifecycleTests/testOldCompletionCannotConsumeNewSession](../../../code-examples/platforms/macos-lifecycle-v1/Tests/DesktopLifecycleTests.swift#L48); [DesktopLifecycleTests/testDuplicateCompletionIsQuiet](../../../code-examples/platforms/macos-lifecycle-v1/Tests/DesktopLifecycleTests.swift#L49); [DesktopLifecycleTests/testReentrantRequestPreservesNewSession](../../../code-examples/platforms/macos-lifecycle-v1/Tests/DesktopLifecycleTests.swift#L54) |
| 3. Distinguishes requesting restoration from proving delivered focus. | unit-evidence-not-bound | Source/answer review or missing suitable assertion |

## macos-appkit-media

| Criterion | Disposition | Exact method evidence |
| --- | --- | --- |
| 1. Keeps loading, empty/missing, error and positive metadata distinct. | unit-subset-bound | [MediaLoadOwnerTests/testNilItemDoesNotInvokeLoader](../../../code-examples/platforms/macos-closure-v1/Tests/AsyncOwnershipTests.swift#L80); [MediaLoadOwnerTests/testErrorIsNotMissingOrSuccessfulMetadata](../../../code-examples/platforms/macos-closure-v1/Tests/AsyncOwnershipTests.swift#L105); [MediaLoadOwnerTests/testSameItemNewRequestRejectsOldGeneration](../../../code-examples/platforms/macos-closure-v1/Tests/AsyncOwnershipTests.swift#L89); [MediaMetadataTests/testKnownMissingGroupIsAbsent](../../../code-examples/platforms/macos-media-v1/Tests/MediaMetadataTests.swift#L73); [MediaMetadataTests/testMissingItemIsUnavailableRatherThanAbsent](../../../code-examples/platforms/macos-media-v1/Tests/MediaMetadataTests.swift#L66) |
| 2. Rejects results for an obsolete player item/request. | unit-subset-bound | [MediaLoadOwnerTests/testReplacementRejectsOldItemCompletion](../../../code-examples/platforms/macos-closure-v1/Tests/AsyncOwnershipTests.swift#L84); [MediaLoadOwnerTests/testExternalReplacementRejectsOldResult](../../../code-examples/platforms/macos-closure-v1/Tests/AsyncOwnershipTests.swift#L95) |
| 3. Does not change selected media options as a side effect of inspection. | unit-subset-bound | [MediaMetadataTests/testInspectionPreservesChosenAudioAndSubtitleOff](../../../code-examples/platforms/macos-media-v1/Tests/MediaMetadataTests.swift#L32) |
| 4. Does not infer spoken description quality or complete caption support from a metadata flag. | unit-evidence-not-bound | Source/answer review or missing suitable assertion |

## macos-appkit-testing

| Criterion | Disposition | Exact method evidence |
| --- | --- | --- |
| 1. Limits conclusions to actual assertions and compilation. | answer-protocol-or-source-review | Source/answer review or missing suitable assertion |
| 2. Keeps exact first failures separate from repairs and deliberate mutants. | answer-protocol-or-source-review | Source/answer review or missing suitable assertion |
| 3. Checks imported API names and availability on the real selected target. | answer-protocol-or-source-review | Source/answer review or missing suitable assertion |
| 4. Does not add mandatory manual verification or UI tests. | answer-protocol-or-source-review | Source/answer review or missing suitable assertion |

## ios-uikit-no-change

| Criterion | Disposition | Exact method evidence |
| --- | --- | --- |
| 1. Does not transfer defaults, support or runtime evidence across targets. | answer-protocol-or-source-review | Source/answer review or missing suitable assertion |
| 2. Preserves the valid existing native control without inventing a defect. | answer-protocol-or-source-review | Source/answer review or missing suitable assertion |
| 3. Does not claim a document was read merely because its name is known. | answer-protocol-or-source-review | Source/answer review or missing suitable assertion |

## ios-swiftui-no-change

| Criterion | Disposition | Exact method evidence |
| --- | --- | --- |
| 1. Does not transfer defaults, support or runtime evidence across targets. | answer-protocol-or-source-review | Source/answer review or missing suitable assertion |
| 2. Preserves the valid existing native control without inventing a defect. | answer-protocol-or-source-review | Source/answer review or missing suitable assertion |
| 3. Does not claim a document was read merely because its name is known. | answer-protocol-or-source-review | Source/answer review or missing suitable assertion |

## macos-appkit-no-change

| Criterion | Disposition | Exact method evidence |
| --- | --- | --- |
| 1. Does not transfer defaults, support or runtime evidence across targets. | answer-protocol-or-source-review | Source/answer review or missing suitable assertion |
| 2. Preserves the valid existing native control without inventing a defect. | answer-protocol-or-source-review | Source/answer review or missing suitable assertion |
| 3. Does not claim a document was read merely because its name is known. | answer-protocol-or-source-review | Source/answer review or missing suitable assertion |

## tvos-uikit-no-change

| Criterion | Disposition | Exact method evidence |
| --- | --- | --- |
| 1. Does not transfer defaults, support or runtime evidence across targets. | answer-protocol-or-source-review | Source/answer review or missing suitable assertion |
| 2. Preserves the valid existing native control without inventing a defect. | answer-protocol-or-source-review | Source/answer review or missing suitable assertion |
| 3. Does not claim a document was read merely because its name is known. | answer-protocol-or-source-review | Source/answer review or missing suitable assertion |

## mixed-ios-owner

| Criterion | Disposition | Exact method evidence |
| --- | --- | --- |
| 1. Clarifies actual ownership before selecting API-specific guidance. | answer-protocol-or-source-review | Source/answer review or missing suitable assertion |
| 2. States the missing evidence or boundary honestly. | answer-protocol-or-source-review | Source/answer review or missing suitable assertion |
| 3. Does not claim a document was read merely because its name is known. | answer-protocol-or-source-review | Source/answer review or missing suitable assertion |

## mixed-macos-owner

| Criterion | Disposition | Exact method evidence |
| --- | --- | --- |
| 1. Clarifies actual ownership before selecting API-specific guidance. | answer-protocol-or-source-review | Source/answer review or missing suitable assertion |
| 2. States the missing evidence or boundary honestly. | answer-protocol-or-source-review | Source/answer review or missing suitable assertion |
| 3. Does not claim a document was read merely because its name is known. | answer-protocol-or-source-review | Source/answer review or missing suitable assertion |

## mixed-tvos-owner

| Criterion | Disposition | Exact method evidence |
| --- | --- | --- |
| 1. Clarifies actual ownership before selecting API-specific guidance. | answer-protocol-or-source-review | Source/answer review or missing suitable assertion |
| 2. States the missing evidence or boundary honestly. | answer-protocol-or-source-review | Source/answer review or missing suitable assertion |
| 3. Does not claim a document was read merely because its name is known. | answer-protocol-or-source-review | Source/answer review or missing suitable assertion |

## watchos-scope

| Criterion | Disposition | Exact method evidence |
| --- | --- | --- |
| 1. Does not transfer defaults, support or runtime evidence across targets. | answer-protocol-or-source-review | Source/answer review or missing suitable assertion |
| 2. States the missing evidence or boundary honestly. | answer-protocol-or-source-review | Source/answer review or missing suitable assertion |
| 3. Does not claim a document was read merely because its name is known. | answer-protocol-or-source-review | Source/answer review or missing suitable assertion |

## visionos-scope

| Criterion | Disposition | Exact method evidence |
| --- | --- | --- |
| 1. Does not transfer defaults, support or runtime evidence across targets. | answer-protocol-or-source-review | Source/answer review or missing suitable assertion |
| 2. States the missing evidence or boundary honestly. | answer-protocol-or-source-review | Source/answer review or missing suitable assertion |
| 3. Does not claim a document was read merely because its name is known. | answer-protocol-or-source-review | Source/answer review or missing suitable assertion |

## ios-missing-reference

| Criterion | Disposition | Exact method evidence |
| --- | --- | --- |
| 1. Does not transfer defaults, support or runtime evidence across targets. | answer-protocol-or-source-review | Source/answer review or missing suitable assertion |
| 2. States the missing evidence or boundary honestly. | answer-protocol-or-source-review | Source/answer review or missing suitable assertion |
| 3. Does not claim a document was read merely because its name is known. | answer-protocol-or-source-review | Source/answer review or missing suitable assertion |

## macos-version-boundary

| Criterion | Disposition | Exact method evidence |
| --- | --- | --- |
| 1. Does not transfer defaults, support or runtime evidence across targets. | answer-protocol-or-source-review | Source/answer review or missing suitable assertion |
| 2. States the missing evidence or boundary honestly. | answer-protocol-or-source-review | Source/answer review or missing suitable assertion |
| 3. Does not claim a document was read merely because its name is known. | answer-protocol-or-source-review | Source/answer review or missing suitable assertion |

## tvos-version-boundary

| Criterion | Disposition | Exact method evidence |
| --- | --- | --- |
| 1. Does not transfer defaults, support or runtime evidence across targets. | answer-protocol-or-source-review | Source/answer review or missing suitable assertion |
| 2. States the missing evidence or boundary honestly. | answer-protocol-or-source-review | Source/answer review or missing suitable assertion |
| 3. Does not claim a document was read merely because its name is known. | answer-protocol-or-source-review | Source/answer review or missing suitable assertion |


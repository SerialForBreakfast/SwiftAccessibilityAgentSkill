// Author-reviewed assertion bindings, after reading the current test bodies and sources.
// Syntax: package slug, method names, directly supported configuration/behavior.
const B = (pkg, names, scope) => ({package: pkg, methods: names.split(' '), scope});
export const bindings = {
 checkout: B('checkout-contract-v1', 'testPreservesExistingButtonIdentityTypographyAndTitle testPreservesConfiguredButtonAndDisabledState testRepeatedUpdatesPreserveExistingActionExactlyOnce testFlexibleTextConfigurationAndNoFixedEnclosingHeight testRetainedButtonDoesNotRetainSummary', 'Supplied UIButton identity, explicitly configured fields, state and existing action remain intact. Oracle revision 1 is preserved separately; this does not prove rendered layout or speech.'),
 summaryGap: B('gap-contracts', 'testSummaryPreservesCompleteLocalizedName testSummaryExposesOneNoninteractiveConcept testSummaryReuseReplacesOwnedTextAndClearsValue testSummaryPreservesUnrelatedTrait', 'Supplied complete summary, explicit grouping flags and reuse metadata; not actual navigation or semantic quality of arbitrary prose.'),
 quantityGap: B('gap-contracts', 'testQuantityHasNamedAdjustableValueAndOrdinaryButtons testOrdinaryQuantityButtonsChangeSameState testAdjustableHooksSynchronizeBeforeCallback testDisabledQuantityRejectsBothDirectPaths testQuantityReenableRestoresBothPaths testQuantityDisabledTraitTransitionsPreserveUnrelatedTraits testQuantityBoundsSuppressRedundantEvents testQuantityRetainedChildrenDoNotRetainOwner', 'Named adjustable metadata and independently wired ordinary controls share application-defined range, state and callback rules; not assistive dispatch.'),
 motionGap: B('gap-contracts', 'testReducedMotionUpdatesTextWithoutAnimation testMotionFeedbackPrecedesOptionalAnimation testMotionPreferenceIsReadOnEachUpdate testMotionUpdatesReplaceErrorWithCompletion testMotionPreservesSuppliedLocalizedMessage', 'Final text/metadata update independently of optional animation, using current injected preference. Actual animation, rendering and announcement are outside the unit assertion.'),
 names: B('uikit-naming-v1', 'testRepeatedVisibleTitlesHaveContextualNames testCompleteLocalizedNamesArePreserved testReconfigurationReplacesNamesWithoutReuseCallback', 'Explicit contextual names and complete caller-supplied localized strings; usefulness of arbitrary wording is not computed.'),
 decoration: B('uikit-naming-v1', 'testDecorationIsExplicitlyExcluded testContainerPreservesIndependentControls', 'Explicit exclusion flags and separate child controls; not actual focus delivery.'),
 native: B('uikit-v1', 'testSettingsCallbacksAndExposedControls', 'Ordinary UISwitch and UIButton remain configured and independently dispatch callbacks; native speech/default getters are not inferred.'),
 hints: B('uikit-semantics-v1', 'testLabelValueAndHintAreSeparate testReconfigurationClearsStaleHintAndValue', 'Chosen distinct label/value/hint fields and clearing stale hints; appropriateness of arbitrary prose remains documentation-supported.'),
 values: B('uikit-reuse-v1', 'testReconfigureClearsSelectedStateWithoutLosingOtherTraits testPrepareForReuseClearsMetadataAndCallback', 'Selected/value state transitions and reuse resets are explicit; no spoken output assertion.'),
 choice: B('uikit-choice-v1', 'testSelectedStateHasTextSymbolAndMetadata testDeselectionClearsEveryOwnedSelectionCue testSelectionUpdatesPreserveUnrelatedTraits', 'Configured text, symbol and selected trait transition together without losing unrelated traits.'),
 traits: B('uikit-semantics-v1', 'testSelectedTraitPreservesOtherTraits testAdjustableHooksSynchronizeValue testAdjustableBoundsDoNotOverflow', 'Explicit selected/adjustable traits and bounded custom values; native semantic equivalence is not fully observed.'),
 headings: B('uikit-reuse-v1', 'testHeaderRoleTransitionPreservesOtherTraits testNestedSectionKeepsHeaderAndListSeparate', 'Heading flags added/removed and explicit semantic group/list hierarchy; rotor navigation delivery not observed.'),
 grouped: B('uikit-semantics-v1', 'testContainerRetainsExplicitOrderAndExposedChildren testEmptyContainerHasEmptyElementList', 'Explicit stored child order/grouping and empty list; task coherence and traversal are separate.'),
 independent: B('uikit-naming-v1', 'testOrdinaryActionsRemainIndependent testReconfigurationReplacesHandlersWithoutDuplicates', 'Independent direct button events and replaced callbacks without duplicate dispatch.'),
 ordered: B('uikit-dynamic-v1', 'testReorderPreservesIdentityAndChangesSearchOrder testRemovedCurrentItemUsesDeclaredBoundaryPolicy testEmptyReplacementClearsOrdinaryAndRotorContent', 'Stored order, identity, rotor search results and removal policy; no observed reading order.'),
 actions: B('uikit-dynamic-v1', 'testCustomActionsAreIndependentAndNamed testOrdinaryButtonsUseCurrentItemAfterReuse testRetainedOldActionCannotAffectReusedView', 'Named custom actions and ordinary buttons use current IDs, while stale custom callbacks reject.'),
 actionstate: B('uikit-semantics-v1', 'testCustomActionHasNameAndInvokesOneCallback testOrdinaryButtonRemainsAnIndependentPath', 'Custom handler changes archived state and callback count; ordinary button remains available. No announcement delivery.'),
 custom: B('uikit-containers-v1', 'testActivationReturnsHandlerSuccessAndFailure testDisabledActivationDoesNotInvokeHandler testHeaderMetadataAndVirtualContainerIdentity', 'Configured custom role, activation result/guard and virtual metadata; not all native-control equivalents.'),
 rotor: B('uikit-semantics-v1', 'testRotorKeepsOrdinaryElementsAndHeadingTraits testRotorNextAndPreviousReturnCorrectIdentity testRotorInitialSearchReturnsFirstOrLast', 'Ordinary element list and heading flags retained alongside direct rotor search identity; not actual user navigation.'),
 fonts: B('uikit-reuse-v1', 'testTypographyReconfigurationReplacesStyleAndSizePolicy', 'Effective trait overrides, font style and multiline/scaling policy across repeated configurations.'),
 longtext: B('uikit-choice-v1', 'testLongLocalizedContentRemainsVerbatim testMultilinePolicyReplacesShrinkToFit testFontsMatchEffectiveLargeTextEnvironment testRepeatedSizeTransitionsDoNotAccumulateScaling testSelfSizingConfigurationAndVerticalConstraintChain', 'Long string retention, scalable wrapping metadata, self-sizing and vertical constraint prerequisites; no rendered clipping claim.'),
 colors: B('uikit-preferences-v1', 'testSemanticColorsResolveForExplicitAppearanceAndContrast testBorderReresolvesWhenAppearanceChanges', 'Configured semantic colors and border conversion under selected trait values, not rendered pixels.'),
 contrast: B('uikit-contrast-v1', 'testConfiguredSemanticPairAcrossFourTraitContexts testLinearColorSpaceIsConvertedBeforeFormula testNearThresholdIsNotRoundedToPassing', 'Opaque configured-color numeric contrast, explicit conversion and selected appearance/contrast contexts; W3C formula provenance stays separate from Apple claims.'),
 errors: B('uikit-preferences-v1', 'testErrorHasTextCueAndAccessibleName testRecoveryRemovesStaleErrorAndHint testReplacementErrorReplacesAllMetadata', 'Explicit error/completion text and metadata replace old state; not spoken output.'),
 motion: B('uikit-preferences-v1', 'testReducedMotionUsesImmediateTransition testOrdinaryMotionUsesBoundedDuration testLivePreferenceMatchesPolicy', 'Preference-dependent duration policy and current preference read; final visible feedback was not coupled to this policy in this pilot.'),
 observers: B('uikit-lifecycle-v1', 'testInitialMotionReadAndNotificationRefresh testStopRemovesObserverAndRestartRefreshes testRepeatedStartDoesNotDuplicateRegistration', 'Injected preference read, private notification refresh, stop/restart and duplicate registration control; not system notification delivery.'),
 modal: B('uikit-modal-v1', 'testOpenExposesHeadingAndIndependentButtons testBackgroundRestoresBothOriginalValues testOrdinaryCloseAndEscapeShareDismissalGuard', 'Configured title/actions, background-hidden snapshot and ordinary/escape callbacks; not actual modal focus.'),
 restoration: B('uikit-modal-v1', 'testNotificationWaitsForCompletionAndUsesCurrentTarget testRetainedButRemovedTargetPostsNil testPreviouslyHiddenBackgroundDoesNotReceiveTargetRequest', 'Captured restoration notification kind/argument after completion and invalid target rejection; no focus delivery assertion.'),
 cells: B('uikit-reuse-v1', 'testReconfigureReplacesLanguageAndName testPrepareForReuseClearsMetadataAndCallback testRetainedActionRejectsReconfiguredIdentity', 'Collection-cell naming/state reset and stale identity checks on direct custom callbacks.'),
 controls: B('uikit-text-v1', 'testSliderClampsValuesToConfiguredBounds testStepperDefaultsAndClamping testSwitchExplicitDispatchReportsCurrentState', 'Configured native bounds/defaults and explicit switch event dispatch; not VoiceOver announcements.'),
 media: B('uikit-media-v1', 'testNativeControllerPreservesControlsAndAutomaticSelection testPlayPauseControlMetadataTransitions testTimelineValueAndBounds testUnavailableTimelineResetsPreviousState', 'Native-controls retention flag, play/pause/timeline metadata and unavailable-state reset.'),
 captions: B('uikit-media-v1', 'testSubtitleOptionsExposeBothAuthoredLanguages testSubtitleSelectionAndOffState testMissingSubtitleLanguagePreservesSelection testAlternateAudioDoesNotReplaceSubtitleSelection', 'Local synthetic options/selection and independent audio/text preservation; no caption quality or input navigation.'),
 speed: B('uikit-speed-v1', 'testOrdinaryButtonsHaveDistinctNamesAndInitialSelection testOrdinaryPrimaryActionUpdatesStateBeforeCallback testEverySupportedChoiceHasAnOrdinaryAction', 'Ordinary speed buttons, named state and direct event dispatch; requested speed is not effective playback.'),
 inspection: B('uikit-media-inspection-v1', 'testDurationCategoriesRemainDistinct testLoadedRangesDoNotAuthorizeSeeking testDiscontinuousRangesPreserveGapsAndHalfOpenEnds testWaitingStatusDoesNotBecomePlayingFromRate testEmptyNativePlayerCaptureAndControlMetadataRemainUnchanged', 'Duration/range distinctions and selected native player fields; no live stream inference from duration.'),
 metadata: B('uikit-media-metadata-v1', 'testTaggedOptionIsRecognizedWithoutInferringOtherAudio testInspectionPreservesChosenAudioAndSubtitleOff testLoadedItemDurationAndSubtitleVariants testKnownMissingGroupIsAbsent testUnreadableLocalAssetPropagatesError', 'Tagged asset metadata, existing selection, loaded duration and missing/error distinction; not narration/content quality.')
};
// Every eligible clause gets an explicit binding; broad clauses remain partial.
export const groups = {
 'U-001': [['23','native'],['24,26,37,38,49,53,54','names'],['25,39','decoration'],['48','native']],
 'U-002': [['23,24,25,26,37,38,47,51,52','hints']],
 'U-003': [['23,24,26,37,38,47,51','values'],['25,52','choice']],
 'U-004': [['23,52','native'],['24,26,37,39,48,53','traits,custom'],['25,38','headings']],
 'U-005': [['23,37','grouped'],['24,52','grouped'],['25,38,44,48,53','independent,decoration'],['26,39','decoration']],
 'U-006': [['23,24,26,37,39,48,52,53','ordered,grouped'],['25,38','modal']],
 'U-007': [['23,24,36,37,50','actions'],['25,46','actionstate'],['51','independent,actions']],
 'U-008': [['23','native'],['24,44,45,54,59','custom,traits'],['25,58','traits']],
 'U-009': [['23,28,39,56,58','headings'],['24,40,52','headings,grouped'],['25,27,59','rotor,independent'],['26,41,57','actions']],
 'U-010': [['23,24','fonts'],['25,26,47,51,52','longtext']],
 'U-011': [['23,25,38,46,50,51','choice,errors'],['24','colors'],['26,37','contrast']],
 'U-012': [['23','motion,observers'],['24,50','motion'],['25,36,37,46,51','errors,motion']],
 'U-013': [['23,24,25,37,38,47,51,52','modal'],['26','restoration']],
 'U-014': [['23,39','native,controls'],['24,38,52,53','grouped,independent'],['25','actions'],['26,37,48','cells,values']],
 'U-015': [['23,24,39,40,51,56','media,speed'],['25,41','captions,metadata'],['26,42,52','inspection,metadata'],['27,57','media,speed']]
};
// Missing compositions identified by reading actual tests, not by test-name matching.
export const gaps = {
 'U-005-L24': {id:'GAP-SUMMARY', reason:'Stored child order is covered, but no explicit supplied title/subtitle summary contract asserts removal of duplicate text stops.'},
 'U-005-L52': {id:'GAP-SUMMARY', reason:'Add a text-only composed concept; retain independently actionable rows as separate examples.'},
 'U-008-L24': {id:'GAP-QUANTITY', reason:'Existing custom quantity tests assert value/traits but not a complete named adjustable value with ordinary increase/decrease controls sharing guards.'},
 'U-009-L27': {id:'GAP-QUANTITY', reason:'Ordinary archive/media paths exist; extend the custom adjustable example so its core change operation also has ordinary controls.'},
 'U-012-L25': {id:'GAP-MOTION-FEEDBACK', reason:'Duration policy and error labels are tested separately, not final-state feedback independent of optional animation.'},
 'U-012-L46': {id:'GAP-MOTION-FEEDBACK', reason:'Translate final-state code contract to a unit assertion without a UI smoke test.'},
 'U-012-L51': {id:'GAP-MOTION-FEEDBACK', reason:'Assert text/metadata update before optional animation and when motion is suppressed.'}
};
// Covered refers only to the literal stored/configured portion stated in scope.
export const directlyAsserted = new Set([
 'U-001-L24','U-001-L25','U-001-L26','U-002-L26','U-002-L38','U-002-L52',
 'U-003-L26','U-003-L38','U-004-L25','U-005-L23','U-006-L26','U-007-L36',
 'U-007-L37','U-009-L23','U-009-L39','U-010-L23','U-010-L24','U-011-L24',
 'U-014-L26','U-015-L26','U-015-L42','U-015-L52'
]);

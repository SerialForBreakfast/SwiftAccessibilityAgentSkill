# Controller-only rubric: macOS/selection

Draft, separate-context source review informed. Known development family, not a holdout.

1. Apply an explicit choice to the current item's actual media-selection group; a display string alone is insufficient.
2. Preserve unrelated groups, player settings and existing native choices.
3. When full captions are requested, distinguish forced-only options without resetting an existing filtered choice.
4. Represent an existing unmapped choice separately from Off; Off follows the group's actual permission.

Answer correctness and controller execution evidence are separate scores. The request
explicitly asks for tests; accept any focused executable tests of the contract, not
these exact IDs, ticket scheme, strings, IDs, view type or architecture. Harmless
extra invalidation is valid when state remains correct. Task cancellation need not
be synchronously delivered unless the answer promises it.

Narrow example assertion leads:
- `MediaSelectionTests/testFullSubtitleChoicesExcludeForcedOnly`
- `MediaSelectionTests/testBindingWritesNativeSelection`
- `MediaSelectionTests/testBindingReadsExternalSelection`
- `MediaSelectionTests/testUnknownChoicePreservesSelection`
- `MediaSelectionTests/testOffClearsOnlyPermittedGroup`
- `MediaSelectionTests/testSubtitleChangePreservesDescriptiveAudio`
- `MediaSelectionTests/testOffPreservesAudio`
- `MediaSelectionTests/testAudioStoreReadsDescriptionTag`
- `MediaSelectionTests/testAudioOffMatchesActualGroupPermission`
- `MediaSelectionTests/testReloadRecoversNativeChoiceWithNewIDs`
- `MediaSelectionTests/testErrorThenReloadRecovers`
- `MediaSelectionTests/testSelectionPreservesPlayerSettingsAndIdentity`
- `MediaSelectionTests/testChoiceIDsUniqueWithinSnapshot`
- `MediaSelectionTests/testBindingWriteInvalidatesObservableSelection`
- `ReviewRegressionTests/testForcedSelectionIsNotOff`
- `ReviewRegressionTests/testUnlistedChoicePreservesNativeSelection`
- `ReviewRegressionTests/testExplicitOffIsDistinctFromUnlistedSelection`

Insufficient evidence for controller validation is not automatically an incorrect
answer. Source compilation does not establish speech, layout or delivered focus.

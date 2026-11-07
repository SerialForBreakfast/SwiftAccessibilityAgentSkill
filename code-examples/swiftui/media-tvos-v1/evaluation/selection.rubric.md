# Controller-only rubric: tvOS / selection

Draft, independent review pending. Accept alternate observable stores, typed IDs,
async tasks or callbacks and suitable native selection APIs that preserve the same
contract. Do not require this example's architecture, strings or UUID format.

Pass: current-item selection and observable state follow the requested behavior.
Gap: selection is simulated, stale operations affect newer work, or required inputs
are missing. Insufficient evidence: prose or view construction without executable
assertions. API compilation does not prove speech, rendered captions or focus.

Assertion bindings (narrow observations, not whole-prose coverage):
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
- `MediaSelectionTests/testOldOptionIDCannotSelectAfterReload`
- `MediaSelectionTests/testErrorThenReloadRecovers`
- `MediaSelectionTests/testSelectionPreservesPlayerSettingsAndIdentity`
- `MediaSelectionTests/testChoiceIDsUniqueWithinSnapshot`
- `MediaSelectionTests/testCapturedBindingRejectsAfterCancellation`
- `MediaSelectionTests/testBindingWriteInvalidatesObservableSelection`

Use real local media groups for selection claims. Distinguish app policy (forced-only
filtering, snapshot IDs and generations) from Apple API contracts. Synthetic content
does not prove production stream metadata or narration quality.

## Criterion-Level Review

1. Apply an explicit choice to the current item's actual media-selection group, not only a display string.
2. Preserve unrelated audio/subtitle selection and do not reset the player.
3. Unknown or stale choices leave the current selection unchanged.
4. Off follows the actual group permission.
5. For the requested full-caption UI, distinguish forced-only tracks from full subtitle options; accept explicit alternate policy if the UI offers a separate forced-track choice.

Accept equivalent native APIs, state architectures and visible selection controls.
These are task contracts; the supplied test identifiers prove only named narrow
observations and are not an instruction to reproduce this exact implementation.

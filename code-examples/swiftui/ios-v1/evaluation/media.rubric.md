# iOS/SwiftUI media

Draft development case; independent review pending; not baseline eligible or a holdout.

Actual VideoPlayer composition preserves player identity. Option-list state and generation ownership are application policy. Distinguish unavailable/empty, stable selection and stale callbacks; do not claim real caption selection, AVAsset extraction, audio-description quality or rendered accessibility from synthetic choices.

Grade correctness, ordinary-behavior preservation, practical usefulness and unsupported certainty separately. Critical errors require concrete evidence: invented APIs, lost ordinary actions, stale cross-item dispatch, unsupported availability. Accept equivalent valid implementations and native no-change reasoning. Exact helper names and English sample strings are not required. Missing integration/context is ungradable, not automatically an answer failure.

[Source claims and checks](../manifest.json); [example](../Sources/FormsMedia.swift). Guidelines: G-015.

Exact assertions:
- `FormsMediaTests/testMissingAndEmptyMediaAreDifferentStates`
- `FormsMediaTests/testMediaSelectionSurvivesReorder`
- `FormsMediaTests/testRemovedTrackSelectionClears`
- `FormsMediaTests/testStaleTrackLoadIsIgnored`
- `FormsMediaTests/testUnknownTrackCannotChangeSelection`
- `FormsMediaTests/testMetadataChoiceDoesNotMutatePlayerPreferences`
- `FormsMediaTests/testDuplicateTrackIDsAreNotAccepted`

Sources and negative controls remain controller-only; inject only the subject and approved condition material. No independent subject answer exists yet. Native model-policy units are not tests of generated SwiftUI semantics.

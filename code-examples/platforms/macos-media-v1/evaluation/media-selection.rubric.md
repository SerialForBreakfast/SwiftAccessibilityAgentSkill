# macOS: media-selection

Status: draft, independently unreviewed, not baseline-eligible.
Classification: shared AVFoundation contract demonstrated on macOS; not framework UI semantics.

Use current group options and locale language metadata; exclude forced-only options for full-subtitle requests, require the describes-video characteristic when requested. Missing matches must not clear or replace selection. Off requires allowsEmptySelection. Respect the supplied current-item group precondition. Preserve other groups. Accept equivalent AVFoundation option filtering; no required helper names. Returning a request result is not proof of audible output or rendered subtitles.

Score correctness, preservation, usefulness and unsupported certainty separately. Invented APIs, unsupported availability and unrequested selection/playback mutation are critical. Accept alternative implementations satisfying the contract. Synthetic silent fixtures do not establish accessibility interaction or narration quality.

## Traceability

- [Claims and checks](../manifest.json)
- [Source](../Sources/MediaChoice.swift)
- [Unit assertions](../Tests/MediaChoiceTests.swift)
- Methods: `MediaChoiceTests/testSelectFullEnglishSubtitle`, `MediaChoiceTests/testMissingLanguagePreservesChoice`, `MediaChoiceTests/testDescriptionSelectsTaggedAudio`, `MediaChoiceTests/testDescriptionUnavailablePreservesChoice`, `MediaChoiceTests/testSubtitleOffWhenAllowed`, `MediaChoiceTests/testAudioOffFollowsNativePermission`, `MediaChoiceTests/testOffPolicyRejectsWithoutCallingClear`, `MediaChoiceTests/testOffPolicyAllowsOneClear`, `MediaChoiceTests/testSubtitleChoiceLeavesAudioUntouched`.
- Negative checks: `forced`, `missing`, `description`, `offpermission`.
- [Evidence, provenance and difficulties](../../../../research/evaluation/platform-media-v1/README.md)

Subject input is only the separate .prompt.md and approved condition material. Keep this rubric, tests, fixtures and incident analysis outside subject context. Known-development cases, not holdouts.

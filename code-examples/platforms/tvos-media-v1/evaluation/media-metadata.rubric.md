# tvOS: media-metadata

Status: draft, independently unreviewed, not baseline-eligible.
Classification: shared AVFoundation contract demonstrated on tvOS; not framework UI semantics.

Query the actual media characteristics rather than infer description from alternate language or option name. Preserve existing audio and subtitle-off selection. Load duration/group asynchronously, retain unavailable versus absent and propagate errors. Metadata loading is not readyToPlay or narration quality. Accept typed result errors or throwing APIs; no requirement for the example enum names.

Score correctness, preservation, usefulness and unsupported certainty separately. Invented APIs, unsupported availability and unrequested selection/playback mutation are critical. Accept alternative implementations satisfying the contract. Synthetic silent fixtures do not establish accessibility interaction or narration quality.

## Traceability

- [Claims and checks](../manifest.json)
- [Source](../Sources/MediaMetadata.swift)
- [Unit assertions](../Tests/MediaMetadataTests.swift)
- Methods: `MediaMetadataTests/testTaggedOptionIsRecognizedWithoutInferringOtherAudio`, `MediaMetadataTests/testUntaggedAlternateAudioIsNotDescription`, `MediaMetadataTests/testInspectionPreservesChosenAudioAndSubtitleOff`, `MediaMetadataTests/testLoadedItemDurationAndSubtitleVariants`, `MediaMetadataTests/testMissingItemIsUnavailableRatherThanAbsent`, `MediaMetadataTests/testKnownMissingGroupIsAbsent`, `MediaMetadataTests/testUnreadableLocalAssetPropagatesError`.
- Negative checks: `described`, `unavailable`.
- [Evidence, provenance and difficulties](../../../../research/evaluation/platform-media-v1/README.md)

Subject input is only the separate .prompt.md and approved condition material. Keep this rubric, tests, fixtures and incident analysis outside subject context. Known-development cases, not holdouts.

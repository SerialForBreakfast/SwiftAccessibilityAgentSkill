# macOS: media-inspection

Status: draft, independently unreviewed, not baseline-eligible.
Classification: shared AVFoundation contract demonstrated on macOS; not framework UI semantics.

Keep unavailable, invalid, indefinite, infinite and finite duration evidence distinct. Unknown stream classification remains unknown: indefinite is not proof of live. Loaded ranges do not substitute for seekable ranges; preserve discontinuities and half-open time membership. Preserve buffer flags independently, rate separately from timeControlStatus and arbitrary waiting reasons. No playback mutation. Accept equivalent typed states and representations. Snapshot membership is not proof a future seek succeeds.

Score correctness, preservation, usefulness and unsupported certainty separately. Invented APIs, unsupported availability and unrequested selection/playback mutation are critical. Accept alternative implementations satisfying the contract. Synthetic silent fixtures do not establish accessibility interaction or narration quality.

## Traceability

- [Claims and checks](../manifest.json)
- [Source](../Sources/MediaInspection.swift)
- [Unit assertions](../Tests/MediaInspectionTests.swift)
- Methods: `MediaInspectionTests/testDurationCategoriesRemainDistinct`, `MediaInspectionTests/testIndefiniteDoesNotInventLiveClassification`, `MediaInspectionTests/testLoadedRangesDoNotAuthorizeSeeking`, `MediaInspectionTests/testDiscontinuousRangesPreserveGapsAndHalfOpenEnds`, `MediaInspectionTests/testUnavailableAndEmptyRangesDiffer`, `MediaInspectionTests/testFullBufferDoesNotImplyLikelyToKeepUp`, `MediaInspectionTests/testWaitingStatusDoesNotBecomePlayingFromRate`, `MediaInspectionTests/testWaitingReasonAndIndependentFlagsArePreserved`, `MediaInspectionTests/testEmptyNativePlayerCaptureRemainsUnavailable`.
- Negative checks: `ranges`.
- [Evidence, provenance and difficulties](../../../../research/evaluation/platform-media-v1/README.md)

Subject input is only the separate .prompt.md and approved condition material. Keep this rubric, tests, fixtures and incident analysis outside subject context. Known-development cases, not holdouts.

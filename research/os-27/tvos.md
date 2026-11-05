# tvOS 27 changes

Research only; reviewed 2026-11-05. Tier-1 source: [27.0 release notes](https://developer.apple.com/documentation/tvos-release-notes/tvos-27-release-notes), [27.2](https://developer.apple.com/documentation/tvos-release-notes/tvos-27_2-release-notes), [27.3 beta](https://developer.apple.com/documentation/tvos-release-notes/tvos-27_3-release-notes). Section names and issue IDs below locate the supporting passage; fingerprints are in [sources](sources.md). Symbol minimum versions remain pending DocC availability extraction unless expressly stated. A release-note appearance alone is not an API introduction date.

| Claim ID | Documented change | Release/type | Supporting section / issue | Research implication (inference) |
| --- | --- | --- | --- | --- |
| TV-01 | System-wide Larger Text is introduced on tvOS 27. | 27 system feature | [WWDC26/221](https://developer.apple.com/videos/play/wwdc2026/221/), Introduction | Review scaled fonts, layouts, grids and carousels. |
| TV-02 | Tab-style pickers announce tab semantics. | 27 feature | SwiftUI / 173211711 | Confirm platform-specific style behavior in symbol docs. |
| TV-03 | Apple TV app sidebar highlight rendering is corrected. | 27 resolved | Apple TV / 177389941 | Do not generalize to app focus restoration. |
| TV-04 | Generated English subtitles support tvOS 27. | 27 media feature | [WWDC26/256](https://developer.apple.com/videos/play/wwdc2026/256/), 3:03 | Preserve caption controls and authored tracks. |

## Follow-up

WWDC26/221 chapters: common issues 2:46, layout 6:13. Separate text scaling from remote focus, selection and scroll reachability. Research exact hardware constraints and font API declarations. 27.2/27.3 retrieved notes focus on StoreKit testing; the coverage inventory records that narrow scope.

[Full topic inventory](coverage.md) · [Cross-platform evidence](cross-platform.md) · [Research method](README.md)

# visionOS 27 changes

Research only; reviewed 2026-11-05. Tier-1 source: [27.0 release notes](https://developer.apple.com/documentation/visionos-release-notes/visionos-27-release-notes), [27.2](https://developer.apple.com/documentation/visionos-release-notes/visionos-27_2-release-notes), [27.3 beta](https://developer.apple.com/documentation/visionos-release-notes/visionos-27_3-release-notes). Section names and issue IDs below locate the supporting passage; fingerprints are in [sources](sources.md). Symbol minimum versions remain pending DocC availability extraction unless expressly stated. A release-note appearance alone is not an API introduction date.

| Claim ID | Documented change | Release/type | Supporting section / issue | Research implication (inference) |
| --- | --- | --- | --- | --- |
| VISION-01 | Eye Setup performed on betas 1–4 can impair tracking; Apple specifies setup again on beta 5 or later. | historical beta known issue | Eye Setup / 175305506 | Do not label all stable 27 devices affected. |
| VISION-02 | Quick Look annotation buttons losing focus on first pinch receive a fix. | 27 resolved | Quick Look / 172214657 | Keep app-specific and input-specific scope. |
| VISION-03 | Safari-opened 3D objects may reposition when moved. | 27.2 known | Quick Look / 187035825 | Investigate spatial interaction interruption. |
| VISION-04 | Generated English subtitles support visionOS 27. | 27 media feature | [WWDC26/256](https://developer.apple.com/videos/play/wwdc2026/256/), 3:03 | Check custom-player affordances. |

## Follow-up

Announcement-level visionOS features are recorded centrally. Confirm shipping status, device support and exact input APIs before recommending integration. Distinguish gaze, hand pinch, Dwell Control and external assistive input.

[Full topic inventory](coverage.md) · [Cross-platform evidence](cross-platform.md) · [Research method](README.md)

## Second-pass shipping evidence

VISION-05: [SHIP-03](shipping-constraints.md) records released-system documentation for Look to Drive and eye-confirmed Dwell Control. VISION-06: [SHIP-04](shipping-constraints.md) records FaceTime interpreter/live-captioner support in 27.2. Both come from Apple Support rather than announcement inference. Developer API integration remains a separate task.

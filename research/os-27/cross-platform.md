# Cross-platform accessibility research

Reviewed 2026-11-05. These records distinguish new behavior from established techniques
revisited at WWDC. Platform-specific symbol minima remain an explicit follow-up.

## Tier-1 developer evidence

| ID | Supported finding | Source locator | Scope / next research |
| --- | --- | --- | --- |
| CROSS-01 | iOS 27 lets linked SwiftUI text elements participate in cross-element text navigation. | [WWDC26/219](https://developer.apple.com/videos/play/wwdc2026/219/), Standard views, 3:45 onward | Behavior introduction, not proof the modifier is new; retrieve its declaration history. |
| CROSS-02 | The reading session demonstrates page-turn traits with scrolling and edit-category actions for selected text. | [WWDC26/219](https://developer.apple.com/videos/play/wwdc2026/219/), Standard views | Keep ordinary selection/actions usable alongside rotor shortcuts; API minima need symbol review. |
| CROSS-03 | Custom controls need meaningful actions and feedback across assistive input methods. | [WWDC26/220](https://developer.apple.com/videos/play/wwdc2026/220/), Guiding principles 1:02; Complex controls 8:41 | Updated implementation guidance; do not classify every technique as OS-27-only. |
| CROSS-04 | English audio transcription is supported on iOS, macOS, tvOS and visionOS 27; subtitle translation is described for iOS/macOS. Authored subtitles retain priority. | [WWDC26/256](https://developer.apple.com/videos/play/wwdc2026/256/), 2:14 and 3:03 | Audit hardware and language constraints; avoid extrapolating translation to every platform. |
| CROSS-05 | System players provide subtitle selection/style preview; custom players have integration options. | [WWDC26/256](https://developer.apple.com/videos/play/wwdc2026/256/), 4:31 and 5:39 | Investigate AVKit versus AVPlayerLayer behavior and exact symbol availability. |

## Tier-1 announced system features

Source for ANN-01 through ANN-07: [Apple announcement, May 19, 2026](https://www.apple.com/newsroom/2026/05/apple-unveils-new-accessibility-features-and-updates-with-apple-intelligence/).
These records preserve announcement scope; shipping versions and footnote constraints
must be reconciled with current Support/API documentation before implementation advice.

| ID | Announced change | Supporting section | Research task |
| --- | --- | --- | --- |
| ANN-01 | VoiceOver image exploration and Magnifier gain AI-assisted descriptions. | VoiceOver and Magnifier Can Explore More | Check supported hardware, privacy and semantic-label interaction. |
| ANN-02 | Natural-language Voice Control navigation on iPhone/iPad. | Voice Control Gets Natural Language | Study ambiguous controls without abandoning stable accessible names. |
| ANN-03 | Accessibility Reader expands complex-document handling, summaries and translation. | Accessibility Reader Adapts Even More | Separate content structure from generated interpretation. |
| ANN-04 | Vision Pro gains wheelchair-control capability; motion cues, face gestures and Dwell Control changes are announced. | Wheelchair feature; Additional Updates | Resolve hardware, safety constraints and API boundaries. |
| ANN-05 | Touch Accommodations setup and hearing-aid pairing/handoff improvements. | Additional Updates | Collect user-facing support guides. |
| ANN-06 | Name Recognition language expansion and a FaceTime interpreter integration API. | Additional Updates | Find exact API and language/device support. |
| ANN-07 | Sony Access controller support on iOS/iPadOS/macOS. | Additional Updates | Distinguish controller support from universal alternative-input accessibility. |

## Toolchain track

[Xcode 27.3 beta notes](https://developer.apple.com/documentation/xcode-release-notes/xcode-27_3-release-notes)
list Swift 6.4 and OS-27.3 SDKs, coding-assistant and Device Hub changes. This is a
beta tooling track, not a claim that a particular assistant discovers this skill.
Research inspector, simulator accessibility, SDK availability diagnostics and native
agent integration separately. Preserve the approved frontier evaluation strategy.

## Second-pass reconciliation

Use [API-01 and API-03](api-availability.md) for the older linked-group and edit-category introduction versions. [Shipping constraints](shipping-constraints.md) promotes the Dwell Control/wheelchair portions of ANN-04 and the visionOS FaceTime portion of ANN-06 to shipping evidence while preserving their remaining API/hardware questions.

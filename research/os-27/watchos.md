# watchOS 27 changes

Research only; reviewed 2026-11-05. Tier-1 source: [27.0 release notes](https://developer.apple.com/documentation/watchos-release-notes/watchos-27-release-notes), [27.2](https://developer.apple.com/documentation/watchos-release-notes/watchos-27_2-release-notes), [27.3 beta](https://developer.apple.com/documentation/watchos-release-notes/watchos-27_3-release-notes). Section names and issue IDs below locate the supporting passage; fingerprints are in [sources](sources.md). Symbol minimum versions remain pending DocC availability extraction unless expressly stated. A release-note appearance alone is not an API introduction date.

| Claim ID | Documented change | Release/type | Supporting section / issue | Research implication (inference) |
| --- | --- | --- | --- | --- |
| WATCH-01 | Release notes describe NSTextTable-related types for UIKit clients. | 27 shared framework note | TextKit / 159870239 | Do not infer a WatchKit integration from a shared note. |
| WATCH-02 | SwiftUI changes and resolved issues are listed in the platform notes. | 27 framework inventory | SwiftUI | Perform per-symbol watchOS availability audit. |

## Follow-up

This platform needs deeper user-facing accessibility research: VoiceOver, Digital Crown, AssistiveTouch, haptics, text size and complications. Current entries are a scoped starting point, not an exhaustive watchOS feature list. Review WatchKit deprecations and independent watchOS user reports; classify framework-shared text before making claims.

[Full topic inventory](coverage.md) · [Cross-platform evidence](cross-platform.md) · [Research method](README.md)

## Second-pass findings

WATCH-03: Apple's [watchOS 27 guide](https://support.apple.com/en-us/guide/watch/apdb93ea3872/27/watchos/27), Convenience and productivity, identifies Sound Recognition on Series 12 and Ultra 4. [SHIP-05](shipping-constraints.md) records setup and safety scope. This is stronger user-facing coverage than the shared-framework notes alone.

WATCH-04: The [feature-availability table](https://www.apple.com/watchos/feature-availability/) distinguishes Live Captions for Live Listen from VoiceOver/Live Speech language support. Search-index reviewed in this pass; full table reconciliation remains pending. Listing a feature here establishes current support scope, not that it was introduced in 27.

[API-02](api-availability.md) lists no watchOS entry for TabsPickerStyle. Keep watchOS implementation recommendations separate from other SwiftUI platforms.

# iOS 27 changes

Research only; reviewed 2026-11-05. Tier-1 source: [27.0 release notes](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-27-release-notes), [27.2](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-27_2-release-notes), [27.3 beta](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-27_3-release-notes). Section names and issue IDs below locate the supporting passage; fingerprints are in [sources](sources.md). Symbol minimum versions remain pending DocC availability extraction unless expressly stated. A release-note appearance alone is not an API introduction date.

| Claim ID | Documented change | Release/type | Supporting section / issue | Research implication (inference) |
| --- | --- | --- | --- | --- |
| IOS-01 | Tab-style pickers convey tab semantics to VoiceOver. | 27.0 feature | SwiftUI / 173211711 | Compare navigation with value selection. |
| IOS-02 | Background-to-foreground scene restoration can be extended/completed. | 27 SDK-linked | UIKit / 161843040 | Distinguish scene state from accessibility focus. |
| IOS-03 | Presented-controller trait inheritance follows the superview chain. | 27 SDK-linked | UIKit / 170005251 | Investigate custom presentation and text-size propagation. |
| IOS-04 | Default UIView margins become zero starting in 27.1; controller system margins remain. | 27.1 behavior, documented in 27.2 | 27.2 UIKit / 186294594 | Check readable layout without assuming an accessibility regression. |
| IOS-05 | Soft scroll edges for iOS-26-SDK apps receive a rendering correction. | 27.3 beta resolved | 27.3 SwiftUI / 188312290 | Separate runtime and linked SDK. |
| IOS-06 | UIKit clients gain NSTextTable-related types. | 27 feature | TextKit / 159870239 | Review table semantics separately from text layout. |

## Follow-up

Connect reading, rotor actions and alternative input to [cross-platform claims](cross-platform.md). API availability and per-device/language constraints need symbol/support-page review. CarPlay ETA-panel focus fix 177508893 belongs in a later CarPlay extension, not a generalized UIKit focus rule.

[Full topic inventory](coverage.md) · [Cross-platform evidence](cross-platform.md) · [Research method](README.md)

## Second-pass constraints

[API-01/02/03](api-availability.md) distinguish existing linked-group/edit-category symbols from the new tab-picker style. [SHIP-01](shipping-constraints.md) adds actual iPhone model and language constraints for generated subtitles. [SHIP-06](shipping-constraints.md) adds supervised-device policy scope.

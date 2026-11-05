# iPadOS 27 changes

Research only; reviewed 2026-11-05. Tier-1 source: [27.0 release notes](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-27-release-notes), [27.2](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-27_2-release-notes), [27.3 beta](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-27_3-release-notes). Section names and issue IDs below locate the supporting passage; fingerprints are in [sources](sources.md). Symbol minimum versions remain pending DocC availability extraction unless expressly stated. A release-note appearance alone is not an API introduction date.

| Claim ID | Documented change | Release/type | Supporting section / issue | Research implication (inference) |
| --- | --- | --- | --- | --- |
| IPAD-01 | Menu imagery defaults are reduced; explicit image visibility controls are available. | 27 behavior | UIKit / 170479084; SwiftUI / 170480710 | Review meaning conveyed by labels rather than icons alone. |
| IPAD-02 | Orientation declarations cease to be a condition for continuous resizability. | 27 resolved | UIKit / 166422120 | Investigate reflow during window resizing. |
| IPAD-03 | Launch-screen declarations are required for apps built with the 27 SDK. | 27 SDK-linked requirement | UIKit / 168247372 | Track migration separately from accessibility semantics. |

## Follow-up

iOS and iPadOS share release notes; shared documentation is not proof of identical input or window behavior. Follow iPad keyboard, pointer, multiwindow and Voice Control user tasks independently. IOS-04 is worded as iOS in Apple notes; confirm iPad scope before asserting it.

[Full topic inventory](coverage.md) · [Cross-platform evidence](cross-platform.md) · [Research method](README.md)

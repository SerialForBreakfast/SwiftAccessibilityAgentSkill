# Apple sources and version boundaries

[Source evidence](source-evidence.json) records retrieved document hashes and exact
installed SDK header excerpts. Source tiers are unchanged. Apple API contracts and
application policy remain separate.

| Contract | Tier 1 reference | Version evidence |
| --- | --- | --- |
| AppKit custom rotor | [NSAccessibilityCustomRotor](https://developer.apple.com/documentation/appkit/nsaccessibilitycustomrotor) | macOS10.13 declaration; SDK27 Swift import uses nested SearchParameters/ItemResult; weak search delegate needs retained session ownership |
| UIKit custom rotor | [UIAccessibilityCustomRotor](https://developer.apple.com/documentation/uikit/uiaccessibilitycustomrotor) | SDK27 TV target26 compile; do not infer TV introduction from an iOS-only annotation |
| Native selectable text | [NSTextView](https://developer.apple.com/documentation/appkit/nstextview), [UITextView](https://developer.apple.com/documentation/uikit/uitextview) | TV UITextView editable property is unavailable; class availability does not imply member availability |
| Row, value, selected, expanded, modal metadata | [NSAccessibilityProtocol](https://developer.apple.com/documentation/appkit/nsaccessibilityprotocol) | Targeted properties have macOS10.10 annotations in installed declarations; exact getters asserted separately |
| Keyboard entry point | [NSResponder.keyDown](https://developer.apple.com/documentation/appkit/nsresponder/keydown(with:)) | Synthetic NSEvent direct-call units; not event-loop delivery |
| Current media item | [AVPlayer.currentItem](https://developer.apple.com/documentation/avfoundation/avplayer/currentitem) | Native identity getter plus application request generation policy |
| Isolation | [MainActor](https://developer.apple.com/documentation/swift/mainactor) | Main-actor callbacks and isolated rotor delegate conformance compiled on the recorded Swift toolchain |

Latest-request-wins, overlap policy, form field ordering and invalid-service-response
handling are example policies, not rules attributed to Apple. Unicode matching
returns UTF16 ranges and verifies character boundaries; this does not assert every
possible search or localization policy.

Compile success establishes syntax/type availability for the selected SDK and
deployment target. Runtime receipts establish the directly asserted observations on
the actual host/simulator. Neither establishes the first OS release of a behavior.
A complete new AppKit/tvOS member-level availability matrix remains separate work;
unresolved earliest annotations must not be guessed from successful compilation.

# API availability: second-pass review

Reviewed 2026-11-05. Tier-1 Apple DocC JSON, specifically `metadata.platforms`.
[Retrieval fingerprints](pass-2-sources.md) identify the reviewed responses. These
are symbol-introduction versions, distinct from SDK-linked behavior and hardware
support. The table records published metadata, not compiler validation.

| ID | Symbol / Apple source | Introduced platforms | Interpretation |
| --- | --- | --- | --- |
| API-01 | [accessibilityLinkedGroup(id:in:)](https://developer.apple.com/documentation/swiftui/view/accessibilitylinkedgroup(id:in:)) | iOS/iPadOS/Catalyst/tvOS 14; macOS 11; watchOS 7; visionOS 1 | Existing symbol. CROSS-01 describes new iOS-27 reading behavior, not API introduction. |
| API-02 | [TabsPickerStyle](https://developer.apple.com/documentation/swiftui/tabspickerstyle) | iOS/iPadOS/Catalyst/macOS/tvOS/visionOS 27 | New symbol. watchOS is not listed in this response; do not infer support from generic SwiftUI notes. |
| API-03 | [UIAccessibilityCustomAction.editCategory](https://developer.apple.com/documentation/uikit/uiaccessibilitycustomaction/editcategory) | iOS/iPadOS/Catalyst/tvOS 18; visionOS 2 | Predates 27. UIKit edit-category guidance at WWDC26 is adoption guidance, not a new OS-27-only rotor API. |
| API-04 | [NSTextSelectionManager](https://developer.apple.com/documentation/appkit/nstextselectionmanager) | macOS 27 | New AppKit text-interaction abstraction; does not itself establish every accessibility behavior. |
| API-05 | [NSToolbarItemGroup.role](https://developer.apple.com/documentation/appkit/nstoolbaritemgroup/role-swift.property) | macOS/Catalyst 27; response also lists iOS/iPadOS 13 | macOS 27 matches AppKit release notes. Investigate unexpected mobile-platform metadata before making a mobile API recommendation. |

## Symbol-specific follow-up

- API-05: compare platform SDK declarations and DocC variants; preserve the metadata
  as received rather than replacing it with an assumed platform list.
- Retrieve `NSSegmentedControl.role`, scene-restoration methods, text-table types,
  media-selection/preview APIs, and UIKit text-navigation declarations next.
- Capture deprecation/unavailability and linked-SDK behavior separately. No minimum
  deployment target is inferred merely from the SDK used to build an app.
- Research remains outside skill guidance and evaluation inputs. Optional compiler
  checks can resolve declaration questions after the source review, without treating
  them as a requirement to trust Apple's documented behavior.

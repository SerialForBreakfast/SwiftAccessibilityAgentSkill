# iPadOS 27 changes

Third pass, 2026-11-05. Research only. iOS and iPadOS share one Apple release-notes
document; shared documentation is not proof of identical input or window behavior. This page
lists entries the notes classified as iPad-specific (IPAD-101 to IPAD-112) and iPadOS Support
items (IPAD-113 to IPAD-117). Shared entries are on [ios.md](ios.md); the full inventory is
[inventory/ios-ipados.md](inventory/ios-ipados.md). No iPadOS 27.1 exists. Column key as on
[ios.md](ios.md).

## Menus

| ID | Change | Release / status | SDK-linked | Tier | Source and locator | Older ID |
| --- | --- | --- | --- | --- | --- | --- |
| IPAD-104 | On iPadOS 27.0 (and macOS 27.0) the menu bar and context menus show a reduced set of menu-item images; SwiftUI hides symbol images by default; use `.labelStyle(.titleAndIcon)` to keep one. | 27.0 New Feature + behavior change | Not stated (C-18) | Tier-1, release note | [27.0 RN][r0] § SwiftUI, 170480710 | IPAD-01 |
| IPAD-106 | UIKit: same reduction; new `UIMenuElement.preferredImageVisibility` (symbol availability pending). | 27.0 New Feature + behavior change | Not stated (C-18) | Tier-1, release note | [27.0 RN][r0] § UIKit, 170479084 | IPAD-01 |

## Window resizing and orientation (all "built with the iOS 27 SDK")

| ID | Change | Release / status | SDK-linked | Tier | Source and locator | Older ID |
| --- | --- | --- | --- | --- | --- | --- |
| IPAD-107 | Supported interface orientations are no longer a condition for continuous resizability. | 27.0 Resolved | Yes | Tier-1, release note | [27.0 RN][r0] § UIKit, 166422120 | IPAD-02 |
| IPAD-108 | With `UIRequiresFullScreen`, `UIScreen.main` bounds stay fixed. | 27.0 Resolved | Yes | Tier-1, release note | [27.0 RN][r0] § UIKit, 178559386 | |
| IPAD-109 | With `UIRequiresFullScreen`, resizes arrive as discrete `UIScreen` changes. | 27.0 Resolved | Yes | Tier-1, release note | [27.0 RN][r0] § UIKit, 178560235 | |
| IPAD-110 | An iPhone-only app ignores supported orientations after the first resize. | 27.0 Resolved | Yes | Tier-1, release note | [27.0 RN][r0] § UIKit, 178561952 | IPAD-116 |
| IPAD-111 | An iPhone-only app with `UIRequiresFullScreen` gets discrete resizes. | 27.0 Resolved | Yes | Tier-1, release note | [27.0 RN][r0] § UIKit, 178562971 | IPAD-116 |
| IPAD-112 | An iPhone-only app supporting only portrait or only landscape had broken layout in unsupported orientations. | 27.0 Resolved | Yes | Tier-1, release note | [27.0 RN][r0] § UIKit, 178573319 | IPAD-116 |
| IOS-359 | Launch-screen key required for apps built with the 27.0 SDK. | 27.0 behavior change | Yes | Tier-1, release note | [27.0 RN][r0] § UIKit, 168247372 | IPAD-03 |

## External display, Siri and app defects

| ID | Change | Release / status | SDK-linked | Tier | Source and locator |
| --- | --- | --- | --- | --- | --- |
| IPAD-105 | Fixed: with Siri off and an iPad extended to an external display showing Spotlight, disconnecting might crash the system. | 27.0 Resolved | No | Tier-1, release note | [27.0 RN][r0] § System Experience, 176281601 |
| IPAD-101 | Fixed: Photos single-photo viewer blank when opened from Siri search results. | 27.0 Resolved | No | Tier-1, release note | [27.0 RN][r0] § Photos, 169236746 |
| IPAD-103 | Fixed: Siri orb waveform and "Hey Siri" on some older iPads with Camera open. | 27.0 Resolved | No | Tier-1, release note | [27.0 RN][r0] § Siri, 180751246 |
| IPAD-102 | Fixed: Safari tab-organize tip might not appear. | 27.0 Resolved | No | Tier-1, release note | [27.0 RN][r0] § Safari, 178280800 |

## User-facing features (Apple Support, "About iPadOS 27 Updates")

| ID | Change | Release / status | Tier | Source and locator | Older ID |
| --- | --- | --- | --- | --- | --- |
| IPAD-113 | VoiceOver image-understanding bullet as on iOS, but without the Action button integration. Magnifier, Accessibility Reader and Voice Control bullets parallel iOS (per notes' comparison). | 27.0 shipped | Tier-1, Support release note | [149075](https://support.apple.com/en-us/149075) | ANN-01; SHIP-101 |
| IPAD-114 | Write with Siri works when hovering a trackpad over a text selection or empty line, and with handwritten text selected in Notes. | 27.0 shipped | Tier-1, Support release note | [149075](https://support.apple.com/en-us/149075) | |
| IPAD-115 | "Side-by-side multitasking is easier to set up", with a second-app choice when tiling. | 27.2 shipped | Tier-1, Support release note | [149075](https://support.apple.com/en-us/149075) § 27.2 | |
| IPAD-116 | Resize iPhone apps running on iPad. Developer counterparts IPAD-110 to IPAD-112. | 27.0 shipped | Tier-1, Support release note | [149075](https://support.apple.com/en-us/149075) | |
| IPAD-117 | App names in the status bar. | 27.0 shipped | Tier-1, Support release note | [149075](https://support.apple.com/en-us/149075) | |
| — | Visual Intelligence with Apple Pencil highlighting; Spotlight-integrated Siri by swiping down from the top edge. 27.0.1 note says only "bug fixes for your iPad". | 27.0 / 27.0.1 | Tier-1, Support release note | [149075](https://support.apple.com/en-us/149075) | |
| — | On-device voice and dictation models require M4 or later with at least 12GB unified memory. | 27.0 | Tier-1, Support release note | [149075](https://support.apple.com/en-us/149075) | IOS-415 |

Shipping evidence on iPadOS for VoiceOver AI descriptions, Voice Control natural language and
Accessibility Reader is limited to this updates page; no iPad user-guide page was retrieved
(SHIP-101 to SHIP-105 gaps). Device list for iPadOS 27: see [releases.md](releases.md).

## Research inference (not Apple-stated)

- The menu-image reduction (IPAD-104/106) could remove icon cues that some users, for
  example people with cognitive disabilities, rely on. Review whether labels carry meaning.
- IPAD-107 to IPAD-112 change resize and orientation behavior; investigate reflow and
  focus retention during window resizing.
- IOS-398 (zero `UIView` margins) is worded for iOS; iPad scope is unconfirmed (C-08).
- Follow iPad keyboard, pointer, multiwindow and Voice Control tasks independently of iPhone.

[r0]: https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-27-release-notes

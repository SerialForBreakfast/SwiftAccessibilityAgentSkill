# OS 27 release, build and date map

Third pass, 2026-11-05. Research only. Every value carries its source. Tier labels follow
the [README](README.md). Values from non-Apple sources are flagged **non-Apple** and must
not be cited as Apple-confirmed builds. Betas are listed separately from shipped releases.

## The 27.1 question

Apple shipped **27.1 only as iOS 27.1 for iPhone Duo (23 Oct 2026) and Xcode 27.1
(27A9275, 15 Oct 2026)**, plus Safari 27.1 notes scoped to iOS 27.1. There is no 27.1 for
iPadOS, macOS, tvOS, watchOS or visionOS:

- Apple's security-releases table lists "iOS 27.1", device iPhone Duo, 23 Oct 2026, with no
  published CVE entries, and no other 27.1 row. Tier-1, Support.
  [Apple security releases](https://support.apple.com/en-us/100100) (IOS notes KQ2; MAC-398; VISION-319; REL-2)
- Every platform release-notes index lists only the 27, 27.2 and 27.3 pages, and every
  `*-27_1-release-notes.md` URL returned HTTP 404 (15,639-byte error shell, SHA-256
  `c8a4f47291ff4563e78e90f4326f3d457661a44a8041d823b1c21b325eb7c510`). Tier-1, negative evidence.
  (MAC-397; VISION-272; REL-3)
- The only Apple text describing a 27.1 platform behavior is the 27.2 UIKit note that
  `UIView` default layout margins are zero "On iOS 27.1 and later" (IOS-398, issue 186294594;
  pass-2 IOS-04). See [conflicts.md](conflicts.md) C-08 for the scope dispute.
- The "About iOS 27 Updates" page has sections for 27, 27.0.1 and 27.2 and none for 27.1.
  [149076](https://support.apple.com/en-us/149076)

Research inference (not Apple-stated): 27.1 was a device-enablement branch for iPhone Duo
whose work was folded into 27.2.

## Stable releases

| Platform | Version | Date | Build | Source for date | Source for build | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| iOS / iPadOS | 27.0 | 14 Sep 2026 | **24A435 (non-Apple, Tier-2)**: RC build, not Apple-confirmed as public | [Security releases](https://support.apple.com/en-us/100100); [149034](https://support.apple.com/en-us/149034) header | [The Mac Observer](https://www.macobserver.com/news/ios-27-release-candidate-build-24a435-explained/) | Apple pages fetched give no public 27.0 build. Devices: iPhone 11 and later; iPad Pro 12.9-inch 4th gen and later, iPad Pro 11-inch 2nd gen and later, iPad Air 4th gen and later, iPad 9th gen and later, iPad mini 6th gen and later. |
| iOS / iPadOS | 27.0.1 | 28 Sep 2026 | 24A446 | Security releases | [Developer Releases](https://developer.apple.com/news/releases/) | No published CVE entries. |
| iOS (iPhone Duo only) | 27.1 | 23 Oct 2026 | **24A94425 (non-Apple, Tier-2)**, day-one update; **24A94232 (non-Apple, Tier-3)**, reported factory build from a reader comment | Security releases | [MacRumors 23 Oct](https://macrumors.com/2026/10/23/apple-releases-ios-27-1/); [MacRumors 13 Oct](https://macrumors.com/2026/10/13/iphone-duo-day-one-update) | No Apple-stated build. Reports disagree on whether 24A94425 appeared 13 or 22 Oct. No iPadOS 27.1. |
| iOS / iPadOS | 27.2 | 26 Oct 2026 | 24B119 (iOS and iPadOS); 24B91020 (iOS only) | Security releases; content page [149230](https://support.apple.com/en-us/149230) | Developer Releases | Apple gives no reason for two iOS builds. Inference (unverified): 24B91020 may be the iPhone Duo variant. |
| macOS | 27.0 "Golden Gate" | 14 Sep 2026 | pending (not in Developer Releases window) | Security releases (MAC-404); Eclectic Light, Tier-2, agrees | — | Supported: MacBook Neo (2026) and Apple-silicon MacBook Air, MacBook Pro, iMac, Mac mini, Mac Studio, Mac Pro. |
| macOS | 27.0.1 | 28 Sep 2026 | 26A434 | Developer Releases (MAC-402) | Developer Releases | No published CVE entries; no developer release notes. Build prefix "26" follows Darwin numbering; copy as shown. |
| macOS | 27.2 | 26 Oct 2026 | 26B123 | Developer Releases (MAC-402) | Developer Releases | |
| tvOS | 27.0 | 14 Sep 2026 | 24J361 | [Releases RSS](https://developer.apple.com/news/releases/rss/releases.rss) (REL-1) | Releases RSS | Hardware: Apple TV 4K (2nd generation and later) (TV-183). tvOS 26.x included Apple TV HD. |
| tvOS | 27.2 | 26 Oct 2026 | 24K122 | Releases RSS ([item](https://developer.apple.com/news/releases/?id=10262026e)) | Releases RSS | No tvOS 27.0.1 is recorded in the notes (pending). |
| watchOS | 27.0 | 14 Sep 2026 | 24R364 | Releases RSS (REL-1) | Releases RSS | Hardware: Apple Watch Series 9 and later (WATCH-183); watchOS 26.x covered Series 6 and later. |
| watchOS | 27.0.1 | 28 Sep 2026 | 24R365 | Releases RSS ([item](https://developer.apple.com/news/releases/?id=09282026e)) | Releases RSS | The security-releases extraction did not surface a watchOS 27.0.1 row (REL-2). |
| watchOS | 27.2 | 26 Oct 2026 | 24S118 | Releases RSS ([item](https://developer.apple.com/news/releases/?id=10262026g)) | Releases RSS | |
| visionOS | 27.0 | 14 Sep 2026 | pending | Security releases; [149038](https://support.apple.com/en-us/149038) header | — | RC about 9 Sep per iClarified (non-Apple, Tier-3, search snippet). Devices: Apple Vision Pro (all models). |
| visionOS | 27.0.1 | 28 Sep 2026 | 24M372 | Releases RSS ([item](https://developer.apple.com/news/releases/?id=09282026d)) (VISION-321) | Releases RSS | "security fixes" per [149067](https://support.apple.com/en-us/149067). |
| visionOS | 27.2 | 26 Oct 2026 | 24N120 | Releases RSS; [149526](https://support.apple.com/en-us/149526) header | Releases RSS | |
| Safari | 27.0 | 14 Sep 2026 | 20625.1.29 | [Safari release-notes index](https://developer.apple.com/tutorials/data/documentation/safari-release-notes.json) | Index JSON | |
| Safari | 27.1 | 23 Oct 2026 | not recorded in notes | Index JSON | — | Available for iOS 27.1 only (WEB-144). |
| Safari | 27.2 | 26 Oct 2026 | 20625.2.8 | Index JSON | Index JSON | |
| Xcode | 27.0 | 14 Sep 2026 | 27A266a | Developer Releases (MAC-402; VISION-321) | Developer Releases | Includes Swift 6.4 and the 27 SDKs; requires macOS Tahoe 26.6 or later. |
| Xcode | 27.1 | 15 Oct 2026 | 27A9275 | Developer Releases (MAC-399) | Developer Releases | 27.1 beta (27A9269) on 18 Sep 2026. |
| Xcode | 27.2 | 29 Oct 2026 | 27B52 | Developer Releases (MAC-402) | Developer Releases | Ships three days after the OS 27.2 releases. |

## Betas (not shipped)

| Platform | Version | Date | Build | Source |
| --- | --- | --- | --- | --- |
| iOS / iPadOS | 27.3 beta | 3 Nov 2026 | 24C5037i | [Developer Releases](https://developer.apple.com/news/releases/) |
| macOS | 27.3 beta | 3 Nov 2026 | 26C5035r | Developer Releases (MAC-403) |
| tvOS | 27.3 beta | 3 Nov 2026 | 24K5286g | Releases RSS (REL-1) |
| watchOS | 27.3 beta | 3 Nov 2026 | 24S5284h | Releases RSS (REL-1) |
| visionOS | 27.3 beta | 3 Nov 2026 | 24N5286r | Releases RSS ([item](https://developer.apple.com/news/releases/?id=11032026e)) |
| Safari | 27.3 beta | 3 Nov 2026 | 20626.1.12 | Safari index JSON |
| Xcode | 27.3 beta | 3 Nov 2026 | 27C5020n | Developer Releases (MAC-403) |
| tvOS (historical) | 27.2 beta 3 | 5 Oct 2026 | 24K5103f | Releases RSS (REL-1) |
| watchOS (historical) | 27.0 beta 1 | 8 Jun 2026 | 24R5289n | [Releases RSS item](https://developer.apple.com/news/releases/?id=06082026g) |

Apple's beta titles carry no beta number for 27.3; whether earlier 27.3 betas exist is
unestablished. MacRumors (non-Apple) calls the 3 Nov watchOS seed "beta 1".
[MacRumors](https://www.macrumors.com/2026/11/03/apple-watchos-27-3-beta-1/)

## Gaps

- Public 27.0 builds for iOS/iPadOS, macOS and visionOS are not Apple-sourced here.
- No Apple statement of iOS 27.1 builds or of the reason for two iOS 27.2 builds.
- Safari 27.1 build was not recorded. tvOS 27.0.1 existence is unrecorded.
- See [backlog.md](backlog.md) items R-1 to R-4.

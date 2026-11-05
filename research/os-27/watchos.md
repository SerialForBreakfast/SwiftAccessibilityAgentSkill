# watchOS 27 changes

Third pass, 2026-11-05. Research only. watchOS release notes hold 73 entries (27.0: 67; 27.2:
4; 27.3 beta: 2), all in [inventory/watchos.md](inventory/watchos.md). 27.2 and the 27.3
beta contain only StoreKit Testing entries. No watchOS 27.1 exists. watchOS 27 requires
Apple Watch Series 9 and later (watchOS 26 covered Series 6 and later; WATCH-183). Builds:
[releases.md](releases.md). Column key as on [ios.md](ios.md).

## User-facing accessibility and gestures (Apple Support)

| ID | Change | Release / status | Tier | Source and locator | Older ID |
| --- | --- | --- | --- | --- | --- |
| WATCH-174 | Series 12 and Ultra 4 "can continuously listen for certain sounds" such as a doorbell, siren or crying baby, and notify you. | watchOS 27 shipped | Tier-1, support guide | [What's new in watchOS 27](https://support.apple.com/guide/watch/whats-new-apdb93ea3872/watchos), "Sound Recognition in Accessibility" | WATCH-03; SHIP-05; SHIP-112 |
| WATCH-175 | Sound Recognition setup on iPhone: Settings > Accessibility > Sound & Name Recognition > Sound Recognition; turn off with "Detect using Apple Watch"; not for high-risk or emergency situations. | watchOS 27 | Tier-1, support guide | [Use Sound Recognition](https://support.apple.com/guide/watch/use-sound-recognition-ay39m4y6riek/watchos) | SHIP-05 |
| WATCH-176 | New single tap gesture selects a widget in the Smart Stack. | watchOS 27 shipped | Tier-1, support guide | [What's new in watchOS 27](https://support.apple.com/guide/watch/whats-new-apdb93ea3872/watchos), Smart Stack bullet | |
| WATCH-177 | Single tap is index finger and thumb together; double tap is unsupported with Low Power Mode, Sleep Focus, wrist down, locked watch, family setup, or when "Accessibility features that use hand gestures are turned on". Settings: Playback, Ignore Tap Gestures with Vision Pro, Off. | watchOS 27 | Tier-1, support guide | [Use tap gestures](https://support.apple.com/guide/watch/use-tap-gestures-apdabb7b275c/watchos) | |
| WATCH-178 | Wrist flick and Cover to Mute (palm 3 s, haptic confirmation) documented; not marked new. | existing | Tier-1, support guide | [Gestures for notifications](https://support.apple.com/guide/watch/use-gestures-for-notifications-and-alerts-apd8bcbaa778/watchos) | |
| WATCH-179 | Text size in Control Center via Digital Crown; Settings > Accessibility lists On/Off Labels, Reduce Transparency, Increase Contrast, Show Borders, Color Filters, Minimum Brightness, Text Size, Bold Text. Nothing marked new. | existing | Tier-1, support guide | [Text and display settings](https://support.apple.com/guide/watch/adjust-text-and-display-settings-apd766b7bd85/watchos) | |
| WATCH-180 | watchOS 27 guide accessibility TOC: VoiceOver (braille display, Bluetooth keyboard), Apple Watch Mirroring, AssistiveTouch, RTT, Live Listen, Sound Recognition, Type to speak, haptic time. | watchOS 27 guide | Tier-1, support guide | [User Guide TOC](https://support.apple.com/guide/watch/whats-new-apdb93ea3872/watchos) | |
| WATCH-181 | Interaction-relevant: dynamic app grid with Siri app centered; Siri Modular face; Steps complication and Shazam in Smart Stack (Series 12, Ultra 4); Workout Buddy without iPhone. | watchOS 27 | Tier-1, support guide | [What's new in watchOS 27](https://support.apple.com/guide/watch/whats-new-apdb93ea3872/watchos) | |
| WATCH-182 | Siri AI (beta): Series 9 and later, Ultra 2 and later, SE 3; needs an Apple Intelligence iPhone (15 Pro or later); not initially in the EU; not under 13. | watchOS 27 | Tier-1, support guide | same | C-25 |
| WATCH-04 | Feature-availability table distinguishes Live Captions for Live Listen from VoiceOver/Live Speech languages (pass-2 search-index review; full reconciliation pending). | availability | Tier-1, feature-availability table | [watchOS feature availability](https://www.apple.com/watchos/feature-availability/) | WATCH-04 |

"About watchOS 27 Updates" ([149077](https://support.apple.com/en-us/149077)) labels no item
as accessibility (C-31).

## Developer-relevant interaction entries (release notes)

| ID | Change | Release / status | SDK-linked | Tier | Source and locator | Older ID |
| --- | --- | --- | --- | --- | --- | --- |
| WATCH-156 | Fixed: in apps built with the watchOS 27.0 SDK, `TabView.selection` updated only after scrolling or rotating the Digital Crown past 50%; now updates as the offset begins to change. watchOS-only. | 27.0 Resolved | Yes | Tier-1, release note | [27.0 RN][w0] § SwiftUI, 163517317 | |
| WATCH-106 | Fixed: some complications missing in the Watch app's Face Gallery. | 27.0 Resolved | No | Tier-1, release note | [27.0 RN][w0] § Complications, 177840928 | |
| WATCH-164 | Fixed: `WCSession.transferCurrentComplicationUserInfo` did not work with WidgetKit complications. | 27.0 Resolved | No | Tier-1, release note | [27.0 RN][w0] § Watch Connectivity, 113202790 | |
| WATCH-127 | Fixed: tapping the Now Playing Suggestions widget in Smart Stack did not start playback. | 27.0 Resolved | No | Tier-1, release note | [27.0 RN][w0] § Smart Stack, 178464737 | |
| WATCH-128 | Fixed: Always On status-bar time might not update. | 27.0 Resolved | No | Tier-1, release note | [27.0 RN][w0] § Status Bar, 178633015 | |
| WATCH-115 | While a third-party heart-rate monitor is active, the watch pauses background heart-rate measurements and notifications (behavior statement under Resolved). | 27.0 Resolved (behavior; C-21) | No | Tier-1, release note | [27.0 RN][w0] § Health, 162788761 | |
| WATCH-167 | Fixed: Workout Alerts and Workout Buddy might fail to deliver audio announcements in standalone mode with Siri AI on iPhone. | 27.0 Resolved | No | Tier-1, release note | [27.0 RN][w0] § Workout, 181296052 | |
| WATCH-123 | Siri may appear to be listening when it is not after long silence. No workaround. | 27.0 Known Issue | No | Tier-1, release note | [27.0 RN][w0] § Siri, 180434572 | |
| WATCH-165 | `WKExtension` and `WKExtensionDelegate` deprecated for minimum deployment watchOS 9.2 or later. | 27.0 Deprecation | No | Tier-1, release note | [27.0 RN][w0] § WatchKit, 70031637 | |
| WATCH-114 | arm64e.x1 and CPA2 on Apple Watch with S11 or later. | 27.0 New Feature (hardware-gated) | Build setting | Tier-1, release note | [27.0 RN][w0] § Hardware Security, 152103975 | |
| WATCH-149 | `TextInputBorderShape`; DocC watchOS 27.0. | 27.0 New Feature | No | Tier-1, release note + API declaration | [27.0 RN][w0] § SwiftUI, 173362083 | API-143 |
| WATCH-163 | `NSTextTable` available to "UIKit clients" (text copied into watchOS notes). | 27.0 New Feature | No | Tier-1, release note | [27.0 RN][w0] § TextKit, 159870239 | WATCH-01; IOS-06 |
| XCODE-113 / XCODE-119c | Xcode agents verify watchOS apps through the Digital Crown and buttons (181147968); XCTest `.rotateDigitalCrown` fixed in Xcode 27.2 (188422137). | Xcode 27.0 / 27.2 | n/a | Tier-1, release note | [xcode-tooling.md](xcode-tooling.md) | |

**`TabsPickerStyle` (173211711) is not in the watchOS notes and DocC lists no watchOS
entry** (API-117). Pass-2 WATCH-02 ("SwiftUI changes listed") is now resolved entry by entry
in the inventory.

## Not found in Apple sources

No Apple source describes watchOS 27 changes to VoiceOver, AssistiveTouch, haptics,
notifications or Digital Crown accessibility beyond WATCH-156. Apple does not state a model
list for the single-tap gesture. No dedicated watchOS accessibility session exists at WWDC26;
the watchOS Group Lab (8014) was not reviewed. The Newsroom announcement had no
watchOS-specific feature (WATCH-184).

## Community evidence

WATCH-186: AppleVis reports a new VoiceOver "Tap to Wake" toggle (Tier-3, search snippet,
HTTP 403; no Apple confirmation). WATCH-187: press model lists conflict with Apple (C-25).
See [community.md](community.md).

## Research inference (not Apple-stated)

- Sound Recognition on the watch is gated to Series 12 and Ultra 4; older watches presumably
  keep iPhone-side Sound Recognition.
- The single tap likely needs double-tap-capable hardware (Series 9 and later, Ultra 2 and
  later); test Smart Stack widget selection by single tap.
- WATCH-163 is probably irrelevant to third-party watchOS apps. Keep watchOS
  recommendations separate from other SwiftUI platforms.

[w0]: https://developer.apple.com/documentation/watchos-release-notes/watchos-27-release-notes

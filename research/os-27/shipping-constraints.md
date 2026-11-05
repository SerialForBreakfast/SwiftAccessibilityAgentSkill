# Announced versus shipped, with deployment constraints

Second pass (SHIP-01 to SHIP-06) and third pass (SHIP-101 to SHIP-116, PEND-01 to PEND-04),
2026-11-05. Research only.

Evidence types: an Apple Newsroom post supports **announced** only. An Apple Support "About
… 27 Updates" page, a version-27 User Guide page or the apple.com feature-availability table
supports **shipped**. All are Tier-1 under the [README](README.md); the third-pass
shipped-features notes used T1 to T4 and are remapped here. Third-pass Support quotes in
SHIP-101 to SHIP-116 were read through a summarizing fetch tool: **quote needs verification
against live page**. The visionOS Support claims (VISION-283 to VISION-304) were fetched
directly with curl.

Announcement source for every ANN record:
[Apple Newsroom, 19 May 2026](https://www.apple.com/newsroom/2026/05/apple-unveils-new-accessibility-features-and-updates-with-apple-intelligence/),
which says the features are "coming later this year". Announced constraints (footnotes 1–6):
Apple Intelligence beta in 16 languages; Voice Control natural language in English (U.S.,
Canada, UK, Australia); generated subtitles in English (U.S., Canada); wired wheelchair
connection needs the Apple Vision Pro Developer Strap; wheelchair control for controlled
environments.

## Status matrix

| Announced feature (pass-2 ID) | Shipped evidence | First version | Platforms with shipping evidence | Hardware / language / region limits | Status |
| --- | --- | --- | --- | --- | --- |
| VoiceOver AI image descriptions and conversational questions (ANN-01) | SHIP-101; IOS-411 | iOS 27.0 | iOS (iPad bullet omits the Action button, IPAD-113) | iPhone 16 models and later, iPhone 15 Pro/Pro Max; locales in SHIP-103 | Shipped (iOS). iPadOS/macOS evidence pending. |
| Magnifier conversational help (ANN-01) | SHIP-102; IOS-412 | iOS 27.0 | iOS | Same as SHIP-101 | Shipped (iOS) |
| Voice Control natural language / Flexible item names (ANN-02) | SHIP-104; IOS-414; developer fix IOS-379 | iOS 27.0 | iOS | English (AU, CA, UK, US) only; Apple Intelligence device floor | Shipped (iOS). iPadOS-specific page pending. |
| Accessibility Reader expansion (ANN-03) | SHIP-105; IOS-413 | iOS 27.0 | iOS; not on the macOS updates page | Locales as SHIP-103 | Shipped (iOS) |
| Generated subtitles (CROSS-04) | SHIP-01; SHIP-02; SHIP-106 | iOS 27; macOS 27 | iPhone, Mac | iPhone 15 Pro/Pro Max or iPhone 16 and later; Mac M1 or later; English (locale: see [conflicts.md](conflicts.md) C-10) | Shipped (iPhone, Mac). tvOS and visionOS: **PEND-04** |
| Vision Pro wheelchair control (ANN-04) | SHIP-03; SHIP-107; VISION-283, 289–292 | visionOS 27.0 | visionOS | U.S. and U.S. territories; TOLT (Developer Strap, USB-C) or LUCI (Bluetooth); requires Dwell Control, Switch Control or AssistiveTouch on; adult supporter; controlled environments; not on wall power; unavailable at 10% battery or below | Shipped |
| Dwell Control eye-glance confirmation (ANN-04) | SHIP-03; SHIP-108; VISION-284, 293 | visionOS 27.0 | visionOS | none stated | Shipped |
| Face gestures (ANN-04) | SHIP-109; VISION-294 (User Guide only) | 27.x; not itemized in update notes (inferred 27.0) | visionOS | none stated | Shipped per guide; first version unverified (C-24) |
| Vehicle Motion Cues on visionOS (ANN-04) | SHIP-110; VISION-295 (User Guide only) | 27.x; not itemized (inferred 27.0) | visionOS | Travel Mode must be on; not for safety-critical situations | Shipped per guide; first version unverified (C-24) |
| Touch Accommodations setup (ANN-05) | none; WWDC26-8005 29:48–30:05 describes "a new setup flow for iOS 27" | — | — | — | **PEND-01** |
| MFi hearing-aid pairing, handoff, setup (ANN-05) | none; VISION-302 hearing-devices page not marked new | — | — | — | **PEND-02** |
| Name Recognition in 50+ languages (ANN-06, language half) | SHIP-113 (feature-availability table, about 55 locales) | not stated | iOS | listed locales | Shipped (availability table); not in update notes |
| FaceTime sign-language interpreter / live captioner (ANN-06, API half) | SHIP-04; SHIP-115; IOS-418; VISION-285 | **27.2** | iOS, macOS, visionOS | none stated | System feature shipped in 27.2. **No public API** (API-131; WWDC-133). See C-23. |
| Sony Access controller (ANN-07) | none from Apple; beta-era MacG snippet (Tier-3) | — | — | — | **PEND-03** |
| tvOS Larger Text | SHIP-111; TV-181; TV-182 | tvOS 27 (first version per notes; no "About tvOS 27 Updates" page found) | tvOS | Apple TV 4K (2nd generation and later) is the tvOS 27 floor; no feature-specific hardware limit stated | Shipped; scope wording conflict C-01 |
| watchOS Sound Recognition (not in May announcement) | SHIP-05; SHIP-112; WATCH-174/175 | watchOS 27 | watchOS | Series 12 and Ultra 4 only; set up on paired iPhone; not for emergencies | Shipped |

## Pass-2 records (preserved)

| ID | Feature and supported constraint | Source section | Pass-3 cross-ref |
| --- | --- | --- | --- |
| SHIP-01 | iPhone generated subtitles require iOS 27 on iPhone 15 Pro/Pro Max or iPhone 16 and later; English US/Canada when absent from content. | [iPhone subtitles guide](https://support.apple.com/en-us/guide/iphone/iph3e2e23d1/27/ios/27), introductory note | SHIP-106; C-10 |
| SHIP-02 | Mac generated subtitles require macOS 27 and M1 or later; English US/Canada. | [Mac captions guide](https://support.apple.com/en-us/guide/mac-help/mchlc1cb8d54/27/mac/27), introductory note | SHIP-106 |
| SHIP-03 | visionOS 27 includes Look to Drive and eye-confirmed Dwell Control. | [visionOS updates](https://support.apple.com/en-us/149067), visionOS 27 › Accessibility | SHIP-107/108; VISION-283/284 |
| SHIP-04 | visionOS 27.2 supports a third-party interpreter or live captioner in FaceTime. | [visionOS updates](https://support.apple.com/en-us/149067), visionOS 27.2 › Other | SHIP-115; VISION-285 |
| SHIP-05 | Watch Sound Recognition on Series 12 and Ultra 4; setup via paired iPhone. | [Watch Sound Recognition](https://support.apple.com/guide/watch/use-sound-recognition-ay39m4y6riek/27/watchos/27) | SHIP-112; WATCH-174/175 |
| SHIP-06 | Managed Accessibility configuration controls Live Recognition on supervised iOS/iPadOS/macOS/visionOS 27 devices (ADE). | [Deployment guide](https://support.apple.com/en-us/guide/deployment/depdc9488053/web) | SHIP-116 |

## Pass-3 records

| ID | Claim | Release / status | Tier / evidence type | Source and locator |
| --- | --- | --- | --- | --- |
| SHIP-101 | VoiceOver gains detailed, context-aware descriptions of photos, charts and screenshots, conversational questions, and an Action button shortcut. Apple Intelligence footnote: all iPhone 16 models and later, iPhone 15 Pro, iPhone 15 Pro Max. | 27.0 shipped | Tier-1, Support release note; quote needs verification | [149076](https://support.apple.com/en-us/149076), Apple Intelligence across apps › Accessibility |
| SHIP-102 | Magnifier gains conversational visual help, a high-contrast interface and natural-language controls. | 27.0 shipped | Tier-1, Support release note | [149076](https://support.apple.com/en-us/149076), same section |
| SHIP-103 | "Ask questions, detailed image and scene descriptions in VoiceOver and Magnifier" available in about 35 locales; separate entries for on-device image descriptions (21 locales) and Magnifier text detection. | 27 availability | Tier-1, feature-availability table | [iOS feature availability](https://www.apple.com/ios/feature-availability/), Accessibility entries |
| SHIP-104 | Voice Control Flexible item names: English (Australia, Canada, UK, US) only. | 27.0 shipped | Tier-1, Support release note + availability table | [149076](https://support.apple.com/en-us/149076); [feature availability](https://www.apple.com/ios/feature-availability/) |
| SHIP-105 | Accessibility Reader content cleanup and summaries; same locales as SHIP-103. Not listed on the macOS updates page. | 27.0 shipped (iOS) | Tier-1, Support release note + availability table | [149076](https://support.apple.com/en-us/149076); [127257](https://support.apple.com/en-us/127257) |
| SHIP-106 | iPhone generated subtitles: Settings > Accessibility > Subtitles & Captioning > Automatic Subtitles; iOS 27, iPhone 15 Pro or iPhone 16 and later, English (U.S.). Pass 3 saw this only in a search snippet; the page fetch was truncated. | 27.0 shipped | Tier-3 for the pass-3 snippet; SHIP-01 remains the Tier-1 record | [iPhone guide](https://support.apple.com/guide/iphone/display-subtitles-and-captions-iph3e2e23d1/ios) |
| SHIP-107 | Look to Drive: TOLT or LUCI; U.S. and territories; not at 10 percent battery or below; not on wall power; Settings > Accessibility > Wheelchair. | 27.0 shipped | Tier-1, Support release note + User Guide | [149067](https://support.apple.com/en-us/149067); [Look to Drive guide](https://support.apple.com/en-al/guide/apple-vision-pro/tan5f0e3ad72/27/visionos/27) |
| SHIP-108 | Updated Dwell Control: confirm by glancing at a selection marker above the dwell pointer. | 27.0 shipped | Tier-1, Support release note | [149067](https://support.apple.com/en-us/149067), visionOS 27 › Accessibility |
| SHIP-109 | Face Gestures: Settings > Accessibility > Interaction > Face Gestures; Slight, Default or Exaggerated sensitivity. Not in release notes; may be a carried-forward feature. | 27.x guide | Tier-1, User Guide | [Vision Pro guide](https://support.apple.com/en-al/guide/apple-vision-pro/tan6a3f9c0e3/27/visionos/27) |
| SHIP-110 | Vehicle Motion Cues listed in the visionOS 27 guide navigation (pass-3 shipped-features notes did not open the page; visionOS notes did, VISION-295). | 27.x guide | Tier-1, User Guide | [nav link](https://support.apple.com/en-al/guide/apple-vision-pro/tan6a3f9c0e5/27/visionos/27) |
| SHIP-111 | tvOS Text Size: Accessibility > Display slider on Apple TV 4K. Press reports nine levels on Apple TV 4K 2nd and 3rd generation (Tier-2, beta era). | tvOS 27 | Tier-1, User Guide (version not stated on page) | [Apple TV guide](https://support.apple.com/en-nz/guide/tv/atvb0222141c/tvos); [iDownloadBlog](https://www.idownloadblog.com/2026/07/02/increase-text-size-apple-tv/) |
| SHIP-112 | watchOS Sound Recognition on Series 12 and Ultra 4; "About watchOS 27 Updates" labels no accessibility item. | watchOS 27 | Tier-1, User Guide | [Watch guide](https://support.apple.com/guide/watch/use-sound-recognition-ay39m4y6riek/27/watchos/27); [149077](https://support.apple.com/en-us/149077) |
| SHIP-113 | Name Recognition about 55 locales. | 27 availability | Tier-1, feature-availability table | [feature availability](https://www.apple.com/ios/feature-availability/), Name Recognition |
| SHIP-114 | Availability (not change) entries: Personal Voice 3 locales; Live Captions 18 locales; Voice Control 20 locales; VoiceOver/Live Speech/Read & Speak 70+ locales. | availability only | Tier-1, feature-availability table | [feature availability](https://www.apple.com/ios/feature-availability/) |
| SHIP-115 | FaceTime supports adding a third-party sign-language interpreter or live captioner; listed under "Other" in each 27.2 updates page. | 27.2 shipped | Tier-1, Support release note | iOS [149076](https://support.apple.com/en-us/149076); macOS [127257](https://support.apple.com/en-us/127257); visionOS [149067](https://support.apple.com/en-us/149067) |
| SHIP-116 | macOS 27: applying the deprecated PPPC Accessibility key triggers a one-time user notification per app, and users can disable device-management-granted accessibility permissions in System Settings. | 27.0 shipped | Tier-1, Support (enterprise) | [What's new for enterprise in macOS Golden Gate 27](https://support.apple.com/en-us/148830), Device management; conflict C-07 |

## Pending (announced, no shipping evidence)

| ID | Feature | Announcement locator | Search result | Pass-2 ID |
| --- | --- | --- | --- | --- |
| PEND-01 | Touch Accommodations setup (iOS, iPadOS) | Newsroom, Additional Updates | No Support or release-note entry. WWDC26-8005 (29:48–30:05) mentions a new iOS 27 setup flow (Tier-1 transcript, informal). | ANN-05 |
| PEND-02 | MFi hearing-aid pairing, handoff and setup (iOS, iPadOS, macOS, visionOS) | Newsroom, Additional Updates | No Support or release-note entry; preview press only. | ANN-05 |
| PEND-03 | Sony Access controller (iOS, iPadOS, macOS) | Newsroom, Additional Updates | No Apple setup page; MacG beta-era snippet only. | ANN-07 |
| PEND-04 | Generated subtitles on Apple TV and Apple Vision Pro | Newsroom, Generated Subtitles; WWDC26-256 says tvOS and visionOS 27 support transcription | No Support evidence; the visionOS Subtitles page (VISION-300) does not mention generated subtitles. | CROSS-04 |

## Other user-facing items with interaction relevance (Tier-1, Support)

| ID | Item | Release | Source |
| --- | --- | --- | --- |
| IOS-415 | On-device dictation on iPhone Air and iPhone 17 Pro and later (developer counterpart IOS-147). iPad on-device voice and dictation models need M4 or later with 12GB unified memory. | 27.0 | [149076](https://support.apple.com/en-us/149076); [149075](https://support.apple.com/en-us/149075) |
| IOS-416 | Liquid Glass readability refinements; Settings slider from ultra-clear to fully tinted (also on macOS). | 27.0 | [149076](https://support.apple.com/en-us/149076); [127257](https://support.apple.com/en-us/127257) |
| IOS-417 | 27.0.1 fixes touchscreen becoming unresponsive when Notification Center and Control Center open simultaneously. | 27.0.1 | [149076](https://support.apple.com/en-us/149076) |
| IOS-419 | 27.2 granular text selection in Siri responses. | 27.2 | [149076](https://support.apple.com/en-us/149076) |
| VISION-286 | Look-to-talk Siri; Siri AI on Apple Vision Pro with M2 and later. | 27.0 | [149067](https://support.apple.com/en-us/149067) |
| VISION-287 | Look to see notifications. | 27.0 | [149067](https://support.apple.com/en-us/149067) |
| WATCH-176 | Single tap gesture selects a Smart Stack widget. | watchOS 27 | [What's new in watchOS 27](https://support.apple.com/guide/watch/whats-new-apdb93ea3872/watchos) |
| WATCH-182 | Siri AI (beta) on Series 9 and later, Ultra 2 and later, SE 3; needs an Apple Intelligence iPhone; not initially in the EU; not under 13. | watchOS 27 | same |
| — | tvOS 27.2 reportedly added ASL/BSL versions of some Apple TV app titles (content, not a setting). | 27.2 | Tier-3 snippet: [Thurrott](https://www.thurrott.com/apple/343252/apple-releases-version-27-2-of-ios-ipados-macos-watchos-and-tvos) |

## Research inference

Ask which device, OS, language, region, account and management policy the person uses
before promising an AI-assisted accessibility feature. The iPhone device floor applies to
SHIP-101, 102, 104 and 105 because the updates page lists them under one Apple
Intelligence footnote. A feature missing from an "About updates" page does not prove it did
not ship: generated subtitles, Face Gestures, Vehicle Motion Cues, tvOS Text Size and Sound
Recognition are guide-documented but not itemized there. Look to Drive is an add-on to
Dwell Control, Switch Control or AssistiveTouch, not a standalone input mode. Live Captions
on visionOS blocks recording and mirroring (VISION-299).

# OS 27 accessibility features: what was announced and what shipped (snapshot 2026-11-05)

Method and caveats:
- Pages were read with WebFetch, which returns a summary from a small model and not the raw text. A quote in quotation marks is that summary's quotation of the page. Before publishing, check each quote against the live page.
- Evidence tiers:
  - **T1:** an Apple Support release-notes page ("About … 27 Updates") or an Apple Support user-guide page for version 27. This is shipping evidence.
  - **T2:** Apple's iOS 27 feature-availability page. This is shipping evidence for language and region.
  - **T3:** the Apple Newsroom announcement. It proves only that a feature was announced.
  - **T4:** third-party press or community coverage. It supports a claim but proves nothing on its own.
  - **T4-snippet:** the claim comes only from a search-result snippet; no page was read.
- Release timeline (T4): the OS 27 family was released September 14, 2026 ([MacDailyNews](https://macdailynews.com/2026/09/14/apple-releases-ios-27-ipados-27-macos-27-watchos-27-visionos-27-and-tvos-27/)). Version 27.2 was released around October 26, 2026. Every Apple "About … 27 Updates" page shows a Published Date of October 26, 2026 ([iOS](https://support.apple.com/en-us/149076)). Betas of 27.3 started November 3, 2026 ([MacRumors](https://www.macrumors.com/2026/11/03/apple-watchos-27-3-beta-1/)). None of the release-notes pages I read lists a 27.1 release.
- Earlier claim IDs: this pass maps to SHIP-01..06 and ANN-01..07 in `os-27/shipping-constraints.md` and `os-27/cross-platform.md`. Each claim below notes its match.
- I did not retrieve the WWDC June 2026 platform press releases (see Gaps).

## Q1. For each feature: announcement, shipping evidence, platforms, first version, devices, languages and settings path

### Takeaway
The OS 27.0 Apple Support release notes confirm these features shipped:
- AI-assisted VoiceOver, Magnifier, Accessibility Reader and natural-language Voice Control on iOS. Device floor: iPhone 15 Pro or iPhone 16 and later.
- Look to Drive and the updated Dwell Control on visionOS 27.

The FaceTime third-party interpreter/live-captioner shipped in 27.2 on iOS, macOS and visionOS.

User guides for version 27 also document these features:
- Generated subtitles on iPhone and Mac.
- Text Size on tvOS.
- Face Gestures and Vehicle Motion Cues on visionOS.
- Sound Recognition on watchOS.

None of the release notes I read mentions these announced features:
- Touch Accommodations setup.
- Hearing-aid pairing and handoff.
- Sony Access controller support.
- The Name Recognition language expansion. Only the feature-availability page covers it.

### Cited Findings

**Announcement baseline (T3)**
- **ANN-baseline.** The Newsroom release of May 19, 2026 says the features are "coming later this year." It has these sections:
  - VoiceOver and Magnifier Can Explore More
  - Voice Control Gets Natural Language
  - Accessibility Reader Adapts Even More
  - Generated Subtitles for Video
  - A Powerful Wheelchair Control Feature for Apple Vision Pro
  - Hikawa Adaptive MagSafe Accessory Now Widely Available
  - Additional Updates

  Source: [Newsroom](https://www.apple.com/newsroom/2026/05/apple-unveils-new-accessibility-features-and-updates-with-apple-intelligence/), headings and intro.
- The "Additional Updates" section lists these items, with no timing given:
  - Vehicle Motion Cues (visionOS)
  - Face gestures and Dwell Control (visionOS)
  - Touch Accommodations setup (iOS, iPadOS)
  - Made for iPhone hearing aids pairing, handoff and setup (iOS, iPadOS, macOS, visionOS)
  - Larger Text (tvOS)
  - Name Recognition in "more than 50 languages"
  - The FaceTime sign-language interpreter API
  - Sony Access controller support (iOS, iPadOS, macOS), with a thumbstick, nine buttons, up to four extra buttons or switches, and two controllers combined

  Source: [Newsroom](https://www.apple.com/newsroom/2026/05/apple-unveils-new-accessibility-features-and-updates-with-apple-intelligence/), Additional Updates.
- Announced constraints (T3), from the same [Newsroom](https://www.apple.com/newsroom/2026/05/apple-unveils-new-accessibility-features-and-updates-with-apple-intelligence/) page, footnotes 1–6:
  - Apple Intelligence beta languages: English, Danish, Dutch, French, German, Italian, Norwegian, Portuguese, Spanish, Swedish, Turkish, Vietnamese, Chinese (Simplified and Traditional), Japanese and Korean. The footnote says there are 16.
  - Voice Control natural language: English in the U.S., Canada, the UK and Australia.
  - Generated subtitles: English in the U.S. and Canada.
  - The wired wheelchair connection requires the Apple Vision Pro Developer Strap.
  - Wheelchair control is intended for controlled environments.
- The Hikawa Grip & Stand was available at announcement in 20 countries and regions. It is hardware, not part of OS 27. Source: [Newsroom](https://www.apple.com/newsroom/2026/05/apple-unveils-new-accessibility-features-and-updates-with-apple-intelligence/), Hikawa section.

**Shipped in OS 27.0**

- **SHIP-101: VoiceOver AI image descriptions and conversational questions (iOS 27.0). Tier T1. Matches ANN-01.**
  - Evidence: the "About iOS 27 Updates" page, under "Apple Intelligence across apps → Accessibility". VoiceOver gains detailed, context-aware descriptions of photos, charts and screenshots. You can ask conversational questions about the screen or your surroundings, and there is an Action button shortcut.
  - Devices: Apple Intelligence features require "All iPhone 16 models and later, iPhone 15 Pro, iPhone 15 Pro Max" (page footnote).
  - Source: [support.apple.com/en-us/149076](https://support.apple.com/en-us/149076)
  - iPad and Mac shipping evidence for this feature was not retrieved.
- **SHIP-102: Magnifier conversational visual help (iOS 27.0). Tier T1. Matches ANN-01.**
  - Evidence: the same section of the [iOS updates page](https://support.apple.com/en-us/149076) lists conversational visual help, a high-contrast interface and natural-language zoom controls. The device floor is the same as SHIP-101.
- **SHIP-103: Languages for the Ask / AI description features in VoiceOver and Magnifier. Tier T2.**
  - Evidence: the feature-availability page entry "Accessibility: Ask questions, detailed image and scene descriptions in VoiceOver and Magnifier."
  - Locales: Chinese (Simplified, not in mainland China), Chinese (Traditional), Danish, Dutch, Norwegian, Swedish, Turkish, Vietnamese, Japanese and Korean. Also English (AU, CA, IN, IE, NZ, SG, ZA, UK, US), French (BE, CA, FR, CH), German (AT, DE, CH), Italian (IT, CH), Portuguese (BR, PT) and Spanish (CL, Latin America, MX, ES, US).
  - The page also has separate entries for "On-device image and scene descriptions" (21 locales, including Arabic, Hindi, Polish, Russian, Thai and Ukrainian) and "On-device text detection in Magnifier."
  - Source: [apple.com/ios/feature-availability](https://www.apple.com/ios/feature-availability/), Accessibility entries.
- **SHIP-104: Voice Control natural language / "Flexible item names" (iOS 27.0). Tier T1 + T2. Matches ANN-02.**
  - Release notes: the [iOS updates page](https://support.apple.com/en-us/149076) says you can describe onscreen elements in your own words, for example "tap the gear."
  - Languages: the feature-availability entry "Accessibility: Voice Control: Flexible item names" lists English (Australia), English (Canada), English (UK) and English (US) only ([feature availability](https://www.apple.com/ios/feature-availability/)). This matches the announcement.
  - The device floor is the Apple Intelligence list in SHIP-101.
  - The announcement covered iPhone and iPad. I did not find an iPadOS-specific release-notes page.
- **SHIP-105: Accessibility Reader cleanup, images and tables, summaries and translation (iOS 27.0). Tier T1 + T2. Matches ANN-03.**
  - Release notes: the [iOS updates page](https://support.apple.com/en-us/149076), Accessibility section.
  - Languages: the feature-availability entry "Accessibility Reader: Content cleanup and summaries" uses the same locale list as SHIP-103 ([feature availability](https://www.apple.com/ios/feature-availability/)).
  - The macOS 27 updates page does not list Accessibility Reader ([macOS updates](https://support.apple.com/en-us/127257)).
- **SHIP-106: Generated subtitles. Tier T1 (from the earlier pass) and T4-snippet (this pass). Matches SHIP-01 and SHIP-02.**
  - iPhone:
    - Apple's iPhone guide, "Display subtitles and captions on iPhone", says generated subtitles require iOS 27 on iPhone 15 Pro/Pro Max or iPhone 16 and later, in English (U.S.). The setting is Settings > Accessibility > Subtitles & Captioning > Automatic Subtitles. Source: [iPhone guide](https://support.apple.com/guide/iphone/display-subtitles-and-captions-iph3e2e23d1/ios).
    - This pass saw those details only in a search snippet; the page fetch came back truncated.
    - The earlier pass (SHIP-01) recorded English US/Canada. Check the locale.
  - Mac: the earlier pass (SHIP-02) recorded macOS 27 on M1 or later.
  - Developers: the WWDC26 session "Discover generated subtitles and subtitle styles" describes generation from English audio starting in iOS 27 ([WWDC26 #256](https://developer.apple.com/videos/play/wwdc2026/256/)).
  - Other platforms: tvOS and visionOS shipping evidence was not found. The tvOS Text Size page does not mention generated subtitles.
  - The feature-availability page has no subtitles entry ([feature availability](https://www.apple.com/ios/feature-availability/), second half).
- **SHIP-107: Look to Drive, Apple Vision Pro wheelchair control (visionOS 27.0). Tier T1. Matches SHIP-03 and ANN-04.**
  - Release notes: the "About visionOS 27 Updates" page, visionOS 27 → Accessibility: "control a compatible powered wheelchair with your eyes" ([support.apple.com/en-us/149067](https://support.apple.com/en-us/149067)).
  - User guide constraints:
    - Works with TOLT Technologies or LUCI controllers.
    - Only available "for compatible wheelchair control systems in the U.S. and U.S. territories."
    - TOLT connects over USB-C through the Developer Strap; LUCI connects over Bluetooth.
    - "not available when the Apple Vision Pro battery level is at 10 percent or below."
    - Do not use it on wall power.
    - Settings path: Settings > Accessibility > Wheelchair.

    Source: [Vision Pro guide: Look to Drive](https://support.apple.com/en-al/guide/apple-vision-pro/tan5f0e3ad72/27/visionos/27), requirements and setup. The en-al locale was the one indexed. The release notes give no chip floor for this feature.
- **SHIP-108: Updated Dwell Control with an eye-glance selection marker (visionOS 27.0). Tier T1. Matches SHIP-03 and ANN-04.**
  - Evidence: confirm by "glancing at a selection marker above the dwell pointer" instead of waiting for a timer.
  - Source: [visionOS updates](https://support.apple.com/en-us/149067), visionOS 27 → Accessibility.
- **SHIP-109: Face Gestures on Apple Vision Pro. Tier T1 (user guide). Matches ANN-04.**
  - Evidence: the visionOS 27 guide page "Use Face Gestures to perform actions on Apple Vision Pro".
  - Settings path: Settings > Accessibility > Interaction > Face Gestures. You assign each gesture an action, "such as a tap or a custom command," and set its sensitivity to Slight, Default or Exaggerated.
  - Source: [Vision Pro guide](https://support.apple.com/en-al/guide/apple-vision-pro/tan6a3f9c0e3/27/visionos/27)
  - Caveats: the visionOS 27 release notes do not list face gestures. The guide may document an existing feature that was carried forward, so I cannot confirm the first version.
- **SHIP-110: Vehicle Motion Cues on Apple Vision Pro. Tier T1-weak.**
  - Evidence: only the visionOS 27 guide navigation lists a "Use Vehicle Motion Cues" page ([nav link](https://support.apple.com/en-al/guide/apple-vision-pro/tan6a3f9c0e5/27/visionos/27)). I did not open that page.
  - The release notes do not list it ([visionOS updates](https://support.apple.com/en-us/149067)).
  - The first version and requirements are unverified.
- **SHIP-111: tvOS Text Size ("Larger Text"). Tier T1-weak + T4.**
  - Evidence: the Apple TV guide page "Display bold text or change the text size on Apple TV 4K" says "Go to Accessibility > Display" and adjust the slider. Its version selector includes tvOS 27, but the page does not say which version it shows.
  - Source: [Apple TV guide](https://support.apple.com/en-nz/guide/tv/atvb0222141c/tvos)
  - Press reports describe a systemwide setting with nine levels on Apple TV 4K (2nd and 3rd generation) ([iDownloadBlog](https://www.idownloadblog.com/2026/07/02/increase-text-size-apple-tv/), [TechRadar](https://www.techradar.com/televisions/streaming-devices/apple-is-introducing-useful-accessibility-features-in-tvos-27-for-apple-tv-4k-that-will-appeal-to-everyone-including-larger-text-and-auto-generated-subtitles-but-some-major-streaming-apps-dont-use-apples-own-app-tech-that-enables-them)). These are mostly beta-era reports.
  - I did not retrieve a tvOS 27 release-notes page.
- **SHIP-112: watchOS Sound Recognition. Tier T1 (from the earlier pass). Matches SHIP-05.**
  - Evidence: the watchOS 27 guide documents Sound Recognition on Series 12 and Ultra 4, set up through the paired iPhone ([Watch guide](https://support.apple.com/guide/watch/use-sound-recognition-ay39m4y6riek/27/watchos/27)).
  - The "About watchOS 27 Updates" page labels no item as accessibility ([support.apple.com/en-us/149077](https://support.apple.com/en-us/149077)). I did not re-verify the guide in this pass.
- **SHIP-113: Name Recognition locales. Tier T2. Matches ANN-06 (language half).**
  - Evidence: the feature-availability entry "Accessibility: Name Recognition" lists about 55 locales, from Arabic (Saudi Arabia) to Vietnamese. Examples include Catalan, Croatian, Czech, Greek, Hebrew, Hindi, Malay, Romanian, Slovak and Thai.
  - Source: [feature availability](https://www.apple.com/ios/feature-availability/), Name Recognition.
  - This is consistent with the announced "more than 50 languages." The iOS 27 release notes do not mention it.
- **SHIP-114: Other Accessibility entries on the iOS 27 feature-availability page (T2).**
  - Personal Voice: English (US), Mandarin Chinese (China mainland) and Spanish (Mexico).
  - Live Captions: 18 locales, including Cantonese, English (AU, CA, IN, SG, UK, US), French (CA, FR), German, Japanese, Korean, Mandarin and Spanish (MX, ES, US).
  - Voice Control (base): 20 locales.
  - VoiceOver / Live Speech / Read & Speak: more than 70 locales.

  Source: [feature availability](https://www.apple.com/ios/feature-availability/). These entries show that the features are available on iOS 27. They do not show that anything changed in 27.

**Shipped in 27.2**
- **SHIP-115: FaceTime third-party sign-language interpreter or live captioner. Tier T1. Matches SHIP-04 and ANN-06 (API half).**
  - Release notes: each 27.2 notes page lists, under "Other," that FaceTime "supports adding a third-party sign language interpreter or live captioner to a call."
    - iOS: [149076](https://support.apple.com/en-us/149076)
    - macOS: [127257](https://support.apple.com/en-us/127257)
    - visionOS: [149067](https://support.apple.com/en-us/149067)
  - First version: 27.2 on all three platforms. The announcement described it as a developer API.
  - I did not retrieve the API name or entitlement.
- tvOS 27.2 reportedly added ASL and BSL sign-language versions of some Apple TV app titles. This is T4 only, from [Thurrott](https://www.thurrott.com/apple/343252/apple-releases-version-27-2-of-ios-ipados-macos-watchos-and-tvos) via a snippet. It is content, not a setting.

**Not accessibility-labeled, but adjacent (T1)**
- Liquid Glass refinements "improve readability," and a slider adjusts the effect from clear to tinted ([iOS](https://support.apple.com/en-us/149076), [macOS](https://support.apple.com/en-us/127257)).
- watchOS has a single-handed tap gesture (index finger and thumb) for selecting a Smart Stack widget ([watchOS](https://support.apple.com/en-us/149077), Smart Stack).

### Inferences
- The iPhone device floor (iPhone 15 Pro and later) applies to SHIP-101, 102, 104 and 105. This follows from the release notes placing these items under "Apple Intelligence across apps," which has a single device footnote.
- The language and region scope that shipped matches the announced scope for Voice Control and Name Recognition. Accessibility Reader and the VoiceOver/Magnifier "Ask" features shipped in about 35 locales, more than the announcement's 16-language Apple Intelligence footnote.

### Gaps
- iPadOS and macOS shipping evidence for SHIP-101..105 is missing. I did not open an iPadOS or Mac user-guide page for these features.
- The tvOS 27 release-notes page and the first tvOS version for Text Size are missing.
- The first version and requirements for Vehicle Motion Cues are not verified.
- I did not retrieve the WWDC June 2026 platform press releases. The beta-era feature list is therefore not reconciled.

## Q2. Which announced features have no shipping evidence yet?

### Takeaway
I found no Apple Support or release-notes evidence for these features:
- The Touch Accommodations setup change.
- MFi hearing-aid pairing, handoff and setup.
- Sony Access controller support.
- The generated-subtitles portion for tvOS and visionOS.

The VoiceOver Live Recognition "Ask" via the Action button is covered by SHIP-101/103. I found nothing new in 27 for Braille Access, Live Listen, Vocal Shortcuts, Eye Tracking, Music Haptics or the Accessibility Nutrition Labels. Those features were not in the May 2026 announcement either.

### Cited Findings
- **PEND-01 (Touch Accommodations) and PEND-02 (hearing aids). Matches ANN-05.** Both are announced only ([Newsroom](https://www.apple.com/newsroom/2026/05/apple-unveils-new-accessibility-features-and-updates-with-apple-intelligence/), Additional Updates). Search returned only preview coverage, such as [The Mac Observer](https://www.macobserver.com/news/hearing-aids-pairing-handoff-iphone-ipad-mac/). The iOS, macOS and visionOS 27 release notes do not list either feature ([149076](https://support.apple.com/en-us/149076), [127257](https://support.apple.com/en-us/127257), [149067](https://support.apple.com/en-us/149067)). Tier: T3/T4.
- **PEND-03 (Sony Access controller). Matches ANN-07.**
  - I found no Apple Support setup page.
  - The macOS 27 release notes do not list it ([127257](https://support.apple.com/en-us/127257)).
  - Press coverage describes it as coming ([Mac Observer](https://www.macobserver.com/news/sony-access-controller-support-iphone-ipad-mac/), [heise](https://heise.de/-11304058)). A June 2026 MacG article says macOS 27 lets you configure the controller ([MacG](https://www.macg.co/materiel/2026/06/macos-27-permet-de-configurer-la-manette-playstation-access-pour-les-joueurs-en-situation-de-handicap-309147)). That article is beta-era; I saw only the snippet.
  - Status: beta-reported but not confirmed as shipped. Tier: T4.
- **PEND-04 (generated subtitles on Apple TV and Vision Pro).** These platforms were announced ([Newsroom](https://www.apple.com/newsroom/2026/05/apple-unveils-new-accessibility-features-and-updates-with-apple-intelligence/), Generated Subtitles). Beyond beta-era press such as [TechRadar](https://www.techradar.com/televisions/streaming-devices/apple-is-introducing-useful-accessibility-features-in-tvos-27-for-apple-tv-4k-that-will-appeal-to-everyone-including-larger-text-and-auto-generated-subtitles-but-some-major-streaming-apps-dont-use-apples-own-app-tech-that-enables-them), I found no T1 evidence. The visionOS guide has a "Subtitles and captions" page in its navigation, but I did not open it.
- **Beta-only or community-reported items (T4).**
  - AppleVis reports these VoiceOver changes in iOS 27: finer control over reading during Explore by Touch, an adjustable delay before hints, and Live Recognition "Ask," which needs Apple Intelligence and so excludes iPhone 15 and earlier ([AppleVis](https://applevis.com/comment/215522)).
  - AppleVis also reports a 27.2 bug fix that reverts VoiceOver audio-profile changes ([AppleVis 27.2](https://www.applevis.com/blog/apple-releases-ios-272-ipados-272-expanded-language-support-siri-ai-profiles-tv-app-bug-fixes)).
  - A fan wiki claims Reduce Motion moved to Settings > Appearance. That is unreliable and unverified ([apple.fandom](https://apple.fandom.com/wiki/IOS_27)).

### Inferences
- These "Additional Updates" items may still have shipped as changes inside existing settings that release notes do not list. The way to resolve this is to check the version-27 user-guide pages for Touch Accommodations, Hearing Devices and Game Controllers.

### Gaps
- I did not search for Braille Access, Live Listen, Live Captions changes, Personal Voice, Vocal Shortcuts, Eye Tracking or Music Haptics changes in 27 beyond the feature-availability entries. No 27 announcement mentioned them, and I found nothing new.
- I did not research Accessibility Nutrition Labels changes for 27. A WWDC26 tvOS session reportedly advises flagging Larger Text support in tvOS nutrition labels; this is T4-snippet via the [nonstrict WWDC index](https://nonstrict.eu/wwdcindex/wwdc2026/221/).

## Q3. Managed-device and MDM accessibility policy changes in 27

### Takeaway
Yes, two changes apply in 27:
- **macOS 27 privacy grants:** an Accessibility grant from the deprecated PPPC Accessibility key now triggers a user notification, and users can turn off accessibility permissions that device management granted.
- **Live Recognition control:** a managed Accessibility configuration can control Live Recognition on supervised devices. This comes from the earlier pass, SHIP-06.

### Cited Findings
- **SHIP-116 (macOS 27).** Tier T1. Source: Apple's "What's new for enterprise in macOS Golden Gate 27," macOS Golden Gate 27 → Device management ([support.apple.com/en-us/148830](https://support.apple.com/en-us/148830)).
  - "When applying the deprecated Accessibility key in the Privacy Preferences Policy Control payload," the user sees a notification once for each configured app.
  - "the user can disable accessibility permissions granted by device management in System Settings."
- **Matches SHIP-06.** A managed Accessibility configuration controls Live Recognition on supervised iOS, iPadOS, macOS and visionOS 27 devices enrolled through Automated Device Enrollment ([Deployment guide](https://support.apple.com/en-us/guide/deployment/depdc9488053/web)). ManageEngine also lists Live Recognition as restrictable through DDM ([ManageEngine](https://www.manageengine.com/mobile-device-management/articles/wwdc-2026-apple-admins-mdm-changes.html), T4). I did not re-fetch the guide in this pass.
- **Conflicting third-party claim.** One blog says MDM can no longer silently grant Accessibility on macOS 27 ([mdm.tools](https://mdm.tools/blog/macos-27-accessibility-grant-removed/), T4). Apple's enterprise page instead describes the deprecated key still working, with a notification. Prefer Apple's account.

### Inferences
- Admins who rely on a PPPC Accessibility grant for monitoring agents should expect user-visible notifications and possible revocation on macOS 27.

### Gaps
- I did not verify enterprise "What's new" pages for iOS 27 or visionOS 27. I also did not read the full Accessibility payload section of the Platform Deployment guide.

## Q4. Apple Support "What's new / About … 27 Updates" pages

### Takeaway
These pages exist for iOS, macOS, watchOS and visionOS. All carry a Published Date of October 26, 2026 and cover the .0, .0.1 and .2 releases. Accessibility items appear only in the iOS 27 and visionOS 27 sections, and in the 27.2 FaceTime item.

### Cited Findings
- **iOS:** "About iOS 27 Updates." Accessibility appears under Apple Intelligence across apps (VoiceOver, Magnifier, Accessibility Reader, Voice Control). In 27.2, the FaceTime interpreter item appears under "Other." 27.0.1 has no accessibility items. Source: [support.apple.com/en-us/149076](https://support.apple.com/en-us/149076). T1.
- **macOS:** "What's new in the updates for macOS 27 Golden Gate." There is no labeled accessibility item in 27.0, and the 27.2 FaceTime interpreter item is listed. Source: [support.apple.com/en-us/127257](https://support.apple.com/en-us/127257). T1.
- **visionOS:** "About visionOS 27 Updates." The Accessibility section lists Look to Drive and Dwell Control, and the 27.2 FaceTime item is listed. Apple Intelligence requires M2 or later. Source: [support.apple.com/en-us/149067](https://support.apple.com/en-us/149067). T1.
- **watchOS:** "About watchOS 27 Updates." No item is labeled accessibility. Source: [support.apple.com/en-us/149077](https://support.apple.com/en-us/149077). T1.
- **tvOS:** I found no "About tvOS 27 Updates" page. Search returned only press coverage, such as [MacRumors](https://www.macrumors.com/2026/10/19/watchos-27-2-release-candidate/).
- **iPadOS:** I found no separate page. The iOS page is titled for iOS only.

### Inferences
- The release-notes pages leave out many guide-documented features: generated subtitles, Face Gestures, Vehicle Motion Cues, tvOS Text Size and Sound Recognition. A feature missing from the release notes therefore does not prove it did not ship. User-guide pages for version 27 are the stronger test.

### Gaps
- The tvOS 27 updates page and an iPadOS 27 updates page are missing.
- I did not check whether any 27.1 releases occurred. None of the pages lists one.

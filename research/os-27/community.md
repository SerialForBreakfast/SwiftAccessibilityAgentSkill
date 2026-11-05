# User experience and commentary sources

Research date: 2026-11-05 (second and third passes). Research only. Editorial reports and
individual observations complement Apple platform evidence. **None of these items is a
platform contract.** They do not establish API behavior, universal bug ranges or fix
versions. Tier-2 is editorial with a named author and testing; Tier-3 is forums (including
Apple Developer Forums) and reader comments. "Tier-1 match" names the Apple claim an item
corroborates; where a match is given it was not independently re-verified in the community
pass.

Retrieval note: www.applevis.com returned HTTP 403 to automated fetches. Third-pass AppleVis
articles were read through the mirror host mail.applevis.com, and those URLs are cited. The
AppleVis bug tracker "fixed" pages could not be fetched.

## AppleVis features, iOS/iPadOS 27.0 (Tier-2, Scott Davert, 13 Sep 2026)

Source: [AppleVis, Davert](https://mail.applevis.com/comment/215301). Supported devices per
the article: iPhone SE 2nd generation and later, iPhone 11 and later (see
[conflicts.md](conflicts.md) C-26).

| ID | Report | Tier-1 match |
| --- | --- | --- |
| COMM-101 | VoiceOver hint delay configurable from 0.05 to 2.0 s (default 0.8); hints set to all, app-specific or none. | Apple's accessibility announcement (not checked against release notes) |
| COMM-102 | Text Exploration (Explore by Touch by paragraph, line or sentence) and Text Navigation (one-finger swipe by line, sentence, paragraph or element). | none found |
| COMM-103 | Pronunciation dictionaries importable or shareable; VoiceOver cursor shown, hidden, or hidden during screen sharing; Bluetooth keyboard function keys run VoiceOver commands without the modifier. | none found |
| COMM-104 | Apple Intelligence image recognition overhaul: Describe, Ask About and Explore for an image, item or screen, plus a customizable rotor list; Live Recognition gains Ask and an Action button shortcut; not on iPhone 15 and earlier. | ANN-01; SHIP-101; WWDC26-8005 |
| COMM-105 | Braille: Braille Screen Input predictive gestures, emoji search, hold-dots entry; "Snap To Print Text Cursor" default with contracted braille; persistent text-field labels; Braille Access plain-text and PDF files; Perkins-style commands for Ask and Intelligent Description. Editing and routing problems from iOS 26 "improved significantly". | none found (pass-2 lead on persistent labels and Braille Access files) |
| COMM-106 | Limits found in testing: Braille Access PDFs lose headings and formatting; a 15 MB PDF failed to load; only Image/Item Description maps to Perkins keys; Auto-Caption output not in braille. | none found |
| COMM-107 | Reader comments (Tier-3, Zoe Victoria): paragraph navigation skips link announcements and some buttons; bold and italic no longer announced separately; Alex voice sounds rushed. | none |

## AppleVis editorial bug summary, iOS/iPadOS 27.0 (Tier-2, 14 Sep 2026)

Source: [AppleVis Editorial Team](https://mail.applevis.com/comment/215423), "iOS 27 and iPadOS 27: A Summary of VoiceOver and Braille Issues and Improvements". 26 VoiceOver bugs; most give no device or build.

| ID | Severity | Report |
| --- | --- | --- |
| COMM-108 | Serious | Changed states and screen updates not announced; VoiceOver may speak old text or the last wake time. No workaround. |
| COMM-109 | Serious | Per-voice Equalizer has no effect; Pronunciation Dictionary often ignores entries. AppleVis advises dependent users not to upgrade. |
| COMM-110 | Serious | With an external audio device, VoiceOver silent during Safari audio playback; speech intermittently stops mid-sentence. |
| COMM-111 | Serious | Diagnostics Mode in the new Recovery Menu gives no speech; device restarts after about 5–10 minutes idle. |
| COMM-112 | Moderate | Sound Curtain and Touch Curtain fail on some devices. |
| COMM-113 | Moderate | Lock Screen swipe focus lands on or loops through status bar items; text field to combo box auto-opens the menu; "Show Notifications" sometimes cannot reach notifications; Quick Settings Direct Touch fails; Screen Recognition missing from Quick Settings. |
| COMM-114 | Moderate | Safari Start Page buttons do not update content; Phone All/Missed switchers fail in Classic View; Siri "Open in App" does nothing; Camera shows edit elements outside Edit Mode; Copy Speech includes markup and hints. |
| COMM-115 | Minor | Notification Center clear-all rotor action fails; mislabeled call button; duplicate rotor "Delete"; top-of-hour misspoken in 24-hour time; custom gesture replacement fails; Safari "Show Bookmarks" labeled "Bookmark"; Camera focus wraps. |
| COMM-116 | Not counted | VoiceOver on the internal speaker has less bass than iOS 26; not all devices affected. |

## Forum reports (Tier-3)

| ID | Report | Context | Source |
| --- | --- | --- | --- |
| COMM-117 | VoiceOver timbre and sentence-pause settings have no effect (FB24536499); voice falls back to default during third-party dictation insertion (FB24536545); double-tapping the status bar no longer scrolls to top. | Apple-fan01, 28 Aug 2026, iPhone 17 Pro, iOS 27 beta 7 | [AppleVis forum](https://mail.applevis.com/forum/apple-beta-releases/bugs-voiceover-ios-27) |
| COMM-118 | VoiceOver prepends unrelated words to focused elements; traced to corrupted Custom Labels; deleting them is a user workaround. | LUCA, 18 Sep 2026, iPhone 16 Pro and 13 mini, iOS 27.0 | [AppleVis forum](https://mail.applevis.com/forum/ios-ipados/help-needed-voiceover-issue-ios-27) |
| COMM-119 | Siri AI bubble stays after Voice Control activates and cannot be dismissed hands-free. Only Voice Control item found; no Switch Control items. | iOS 27 | [Developer Forums 847214](https://developer.apple.com/forums/thread/847214) |
| COMM-121 | Zero vertical layout margins on iPhone Duo simulator; an Apple Frameworks Engineer replied that zero is intended, applies to iPhone Duo in 27.1 and all devices in 27.2. Reporter says `preservesSuperviewLayoutMargins` does not restore vertical spacing (unanswered). No accessibility mention. | reed.1325, early Oct 2026, iOS 27.1 RC, FB25097501 | [Developer Forums 849929](https://developer.apple.com/forums/thread/849929) |
| COMM-123 | VoiceOver skips Unicode fraction glyphs and fraction text in SwiftUI, UIKit and WKWebView. No replies. | Oct 2026, iOS 27 | [Developer Forums 849493](https://developer.apple.com/forums/thread/849493) |
| COMM-124 | When Shift+Tab moves focus to a focusable parent, the VoiceOver cursor stays on the descendant; NVDA correct. FB25212861. | late Oct 2026, macOS 27.0.1, Safari 27.0.1, Chrome, Firefox | [Developer Forums 851810](https://developer.apple.com/forums/thread/851810) |
| COMM-125 | Accessibility Inspector Element Detection fails only while a SwiftUI `.sheet` is presented ("Potentially inaccessible text", nil element); contrast failures at maximum Dynamic Type. | about 30 Oct 2026, Xcode 27.1, iPadOS 27.0 Simulator | [Developer Forums 854036](https://developer.apple.com/forums/thread/854036) |
| COMM-126 | macOS 27 PPPC Accessibility reported deprecated or removed; App Settings grant user-editable (850583); vendors want a non-consent path (836770, FB23531820, 13 replies); PPPC profile not applied on a 27.0 beta (839536). | enterprise / MDM | [850583](https://developer.apple.com/forums/thread/850583); [836770](https://developer.apple.com/forums/thread/836770); [839536](https://developer.apple.com/forums/thread/839536) |
| COMM-132 | Commenters (14–15 Sep) plan to wait for 27.1 fixes; one Feedback marked "potential fix in a future update". None confirms a fix. | AppleVis comments | [AppleVis Editorial comments](https://mail.applevis.com/comment/215423) |
| COMM-133 | Still open at snapshot: COMM-124, COMM-125, and the COMM-121 margin objection. | late Oct 2026 | threads above |

## Practitioner and press (Tier-2)

| ID | Report | Source |
| --- | --- | --- |
| COMM-120 | iOS 27 SwiftUI `accessibilityLinkedGroup` lets VoiceOver keep reading across separate text elements; described as the SwiftUI counterpart of iOS 18 text-navigation APIs. No regressions reported. Tier-1 match: WWDC26-219 (WWDC-107; API-101). | [Blake Crosley, 8 Jun 2026](https://blakecrosley.com/blog/accessibility-ios-27) |
| COMM-122 | Quotes the 27.2 margin note (186294594); his probe saw the change only when linking the 27.1+ SDK; says 27.1 shipped 23 Oct for iPhone Duo only (his inference) and 27.2 as 24B119. Conflict C-08. | [Blake Crosley, 26 Oct 2026](https://blakecrosley.com/blog/ios-27-2-release-notes) |
| COMM-127 | iOS 27 replaces the transparency toggle with a slider; blur keeps text legible at maximum glass; no legibility problems found. Tier-1 match: IOS-416. | [Ben Lovejoy, 9to5Mac, 12 Jun 2026](https://9to5mac.com/2026/06/12/ios-27-fixes-liquid-glass-and-not-just-with-a-slider/) |
| COMM-128 | Excluded: uncredited blog claims of an "intermediate" higher-contrast Liquid Glass mode and Xcode 27 "deferral flags" removal. | [noqta.tn](https://www.noqta.tn/en/blog/apple-liquid-glass-ios-27-developer-adoption-guide-2026); [ecorpit.com](https://ecorpit.com/ios-27-liquid-glass-xcode-27-migration-guide-2026/) |
| COMM-130 | Crosley's 27.2 summary lists no accessibility fixes; it does not cover VoiceOver, so this means none listed, not none exist. | [blakecrosley.com 27.2](https://blakecrosley.com/blog/ios-27-2-release-notes) |
| COMM-131 | Unretrieved forum results mention issues "finally being addressed in iOS 27.2". Unverified. | [AppleVis forum search result](https://applevis.com/forum/apple-beta-releases/bugs-voiceover-ios-27) |

## Corroboration map (COMM-129)

COMM-120 corroborates WWDC26-219 and 220. COMM-104 corroborates the 8005 lab and Apple's
May preview. COMM-121 and COMM-122 corroborate release note 186294594 (IOS-398; pass-2
IOS-04). COMM-123, COMM-124 and COMM-125 have no matching Apple-acknowledged issue. No
AppleVis bug item has a confirmed fix in a later point release in the sources found.

## Other third-pass community and editorial items by platform

| Platform | Item | Tier | Source |
| --- | --- | --- | --- |
| tvOS | Some major streaming apps do not use Apple's UI frameworks, so they may not respond to Larger Text (TV-185). | Tier-2 | [TechRadar](https://www.techradar.com/televisions/streaming-devices/apple-is-introducing-useful-accessibility-features-in-tvos-27-for-apple-tv-4k-that-will-appeal-to-everyone-including-larger-text-and-auto-generated-subtitles-but-some-major-streaming-apps-dont-use-apples-own-app-tech-that-enables-them); [MacRumors](https://macrumors.com/2026/05/20/apple-previews-new-tvos-27-feature/); [9to5Mac](https://9to5mac.com/2026/05/20/tvos-27-will-give-apple-tv-4k-a-useful-new-display-setting/) |
| tvOS | AppleVis: tvOS 27 shipped 14 Sep with larger accessibility text sizes (TV-186). Search snippet only, HTTP 403. | Tier-3 (snippet) | [AppleVis](https://applevis.com/blog/apple-releases-tvos-27) |
| watchOS | AppleVis: new VoiceOver "Tap to Wake" toggle (WATCH-186). Search snippet only, HTTP 403. No Apple confirmation. | Tier-3 (snippet) | [AppleVis](https://applevis.com/comment/215526) |
| iOS | AppleVis: finer Explore-by-Touch reading control, adjustable hint delay, Live Recognition Ask needs Apple Intelligence. | Tier-2 | [AppleVis](https://applevis.com/comment/215522) |
| iOS | AppleVis 27.2: fix reverting VoiceOver audio-profile changes. | Tier-2 | [AppleVis 27.2](https://www.applevis.com/blog/apple-releases-ios-272-ipados-272-expanded-language-support-siri-ai-profiles-tv-app-bug-fixes) |
| iOS | Fan wiki claims Reduce Motion moved to Settings > Appearance. Unreliable, unverified. | Tier-3 | [apple.fandom](https://apple.fandom.com/wiki/IOS_27) |

## Pass-2 leads (preserved)

- [AppleVis iOS/iPadOS 27 VoiceOver and braille review](https://server.applevis.com/blog/ios-27-ipados-27-summary-voiceover-braille-issues-improvements?page=4), 14 Sep 2026. Now reviewed through the mirror as COMM-108 to COMM-116.
- [AppleVis feature discussion](https://server.applevis.com/comment/215624): persistent braille text-field labels and Braille Access files. Now corroborated by COMM-105.
- [AppleVis bug tracker](https://www.applevis.com/bugs): discovery index; fixed pages returned 403.
- [AppleVis 27.2 RC discussion](https://mail.applevis.com/comment/219125): differing passcode speech across devices. Lead only.
- [Hacking with Swift forum index](https://www.hackingwithswift.com/forums/100-days-of-swiftui/) and [NSHipster archive](https://nshipster.com/authors/mattt): no OS-27 change evidence.

## Research inference

The serious AppleVis items are speech-pipeline and announcement-timing failures, not
new-feature failures; COMM-108 overlaps COMM-117's beta speech-settings reports. COMM-117's
status-bar double-tap report sits beside Apple's 27.0 note that status-bar tap scroll-to-top
now updates a bound `scrollPosition` (IOS-337); the relation is untested. AppleVis covered
VoiceOver on iPhone only: low vision, Voice Control and Switch Control are effectively
unreviewed, and no macOS, watchOS, tvOS or visionOS 27 AppleVis editorial was found. No
Deque, TPGi/Vispero or Level Access posts on iOS 27 were found.

## Extraction checklist

For every user-impact report, record author and editorial status, date, OS build, device,
assistive technology and settings, task, symptom, workaround, claimed fix version and
corroboration. Preserve differences between observations. Prioritize braille, VoiceOver,
ordinary navigation, Switch Control, Voice Control, keyboard-only use, low vision, hearing
access and cognitive load.

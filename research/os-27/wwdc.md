# WWDC26 session index

Third pass, 2026-11-05. Research only. Base URL: `https://developer.apple.com/videos/play/wwdc2026/<id>/`.
Timestamps are the transcript `data-start` values (m:ss), accurate to the sentence. All
session transcripts are **Tier-1, evidence type transcript** under the [README](README.md).
Group-lab answers (8004, 8005) are Apple staff speaking informally: Tier-1 transcript, but
treat them as weaker than release notes or DocC. Some notes rated transcripts T2 and lab
answers T2 or T3; they are normalized here. A WWDC demonstration does not establish that an
API is new: check [api-availability.md](api-availability.md).

The notes ranked all 138 WWDC26 transcripts by accessibility keywords. Hit counts:
8005 (210), 219 (81), 256 (74), 220 (51), 221 (38), 230 (16), 212 (14), 102 (9); 269, 272
and 278 had none and 289 had one (WWDC-103). There is no "What's new in Accessibility",
"What's new in UIKit" or "What's new in AppKit" session (WWDC-102). The catalog's topic
tags put 219 and 220 under SwiftUI and UI frameworks and 221 under audio and video, so a
topic filter for accessibility misses them (WWDC-104).

## Dedicated accessibility sessions

| Session | Title (length) | Timestamped claims | Claim IDs | New in 27 or revisited |
| --- | --- | --- | --- | --- |
| [219](https://developer.apple.com/videos/play/wwdc2026/219/) | Enhance the accessibility of your reading app (20:00) | 4:12 `UIAccessibilityReadingContent` as existing technique; 4:44, 14:57 `UITextInput`; 7:00 "iOS 18 introduced the text navigation APIs"; 7:17 `accessibilityNextTextNavigationElement`; 7:59–8:06 SwiftUI `accessibilityLinkedGroup` achieves the same "starting in iOS 27"; 8:27 AppKit `accessibilitySharedTextUIElements`; 9:55 `causesPageTurn` with `accessibilityScroll`; 11:46–11:50 edit-rotor custom action via edit category; 13:31 Accessibility Reader "Since iOS 26"; 19:23 audit with VoiceOver read-all. Chapters: Characteristics 1:26, Standard views 3:45, Custom text 14:05. | WWDC-105–111; VISION-315; XCODE-125; CROSS-01/02; API-101–105 | One 27 behavior (linked-group text navigation); rest revisited |
| [220](https://developer.apple.com/videos/play/wwdc2026/220/) | Refine accessibility for custom controls (16:25) | 1:02 Guiding principles; 3:41 purpose, value, actions, feedback; 5:10 slider as element with `accessibilityLabel`; 5:37–5:47 `.adjustable` trait and `accessibilityAdjustableAction`; 6:38–6:49 passthrough gesture from `accessibilityActivationPoint`; 7:27 announcements throttled to about 0.3 s; 8:41 Complex controls; ~9:53–10:18 four named custom actions; ~12:52–14:16 `accessibilityDirectTouch` with `.requiresActivation` / `.silentOnTouch`; 15:43 manual VoiceOver testing; 16:06 Switch Control and Voice Control. | WWDC-112/113; VISION-314; XCODE-126; MAC-411; CROSS-03 | Revisited; nothing described as new. Code-sample typo: C-06 |
| [221](https://developer.apple.com/videos/play/wwdc2026/221/) | Prepare your tvOS apps for Dynamic Type | 0:12–0:20 Large Text "now available" system-wide; 0:40–0:43 and 9:46–9:48 Accessibility Nutrition Labels for tvOS; 1:21–1:30 "Dynamic Type works the same way on tvOS"; 1:30–1:49 Settings > Accessibility > Display > Text Size, Large to Accessibility XXXL; 2:31–2:43 standard components automatic, update custom elements; 2:46 Identify common issues; 2:54–3:15 avoid fixed sizes; 4:56–5:24 `.caption` and `.frame(maxWidth: .infinity)`; 5:55–6:08 `preferredFont(forTextStyle:)` and `adjustsFontForContentSizeCategory`; 6:13 Adapt your layout; 6:25–7:26 grid columns by `isAccessibilitySize`, marquee for long titles; 8:03–8:49 `AnyLayout` and `UIStackView.axis` flip. | WWDC-114–116; TV-171–180; TV-01 | New platform feature; existing APIs. Timestamp variants: C-28. Scope wording: C-01 |
| [256](https://developer.apple.com/videos/play/wwdc2026/256/) | Discover generated subtitles and subtitle styles | 2:14 two generation sources (speech transcription, translation of authored subtitles); 3:03 "you don't need to implement anything"; 4:11 English subtitles from English audio on iOS and macOS 27; 4:18 also tvOS and visionOS 27; ~4:22 translation iOS/macOS only; 4:31, 5:01, 5:39 player integration; 5:54 Settings styling "for many years"; 7:10 `AVLegibleMediaOptionsMenuController`; 7:25 `AVPlayerLayer`; 7:32 `AVCaptionRenderer`; 7:43 profile IDs; 9:24 generated tracks marked with a sparkle and "Translated". | WWDC-117–120; CROSS-04/05; TV-04; VISION-04 | System feature new; preview APIs are 26.4 (C-13) |
| [8005](https://developer.apple.com/videos/play/wwdc2026/8005/) | Accessibility Technologies Group Lab (60:41) | 2:46–3:01 feature list (image descriptions, Live Recognition, Accessibility Reader, Voice Control, automatic subtitles in personal videos); 3:43–3:48 Vehicle Motion Cues to visionOS; ~5:02 Accessibility Inspector and Device Hub; 16:44 "I don't think there's new API" for text-to-speech; 22:26–22:29 new XCTest API to test VoiceOver from a Mac; 29:48–30:05 new iOS 27 Touch Accommodations setup flow; 34:57 reorder-modifier VoiceOver support unknown in beta; 36:07–36:13 FaceTime interpreter feature "not quite available in the iOS 27 beta"; ~36:38 stable identifiers; ~52:26–53:30 XCUITest relies on the accessibility hierarchy; 57:32–58:14 Pointer Control as gaze alternative; 58:39–58:47 RealityKit accessibility covered in an earlier session. | WWDC-130–135; XCODE-127; VISION-316; COMM-104 | Informal; about 40% of transcript reviewed |

## Adjacent sessions with accessibility content

| Session | Title | Timestamped claims | Claim IDs |
| --- | --- | --- | --- |
| [102](https://developer.apple.com/videos/play/wwdc2026/102/) (ASL: [112](https://developer.apple.com/videos/play/wwdc2026/112/)) | Platforms State of the Union | 23:25 macOS 27 supports the "show borders" environment value; Liquid Glass adapts to Reduce Transparency and Increase Contrast; 46:58 previews show accessibility sizes; 56:10–56:21 Xcode ships an accessibility specialist. | WWDC-121/122; XCODE-123; API-111 |
| [203](https://developer.apple.com/videos/play/wwdc2026/203/) | PencilKit handwriting | 8:14 VoiceOver can speak handwriting; 8:23 search lets assistive features navigate to words. | WWDC-125; API-123 |
| [204](https://developer.apple.com/videos/play/wwdc2026/204/) | What's new in WebKit for Safari 27 (16:32) | 1:07 "A year of quality improvements", accessibility focus ~4:35; 10:06 Customizable Select; ~10:19 "great accessibility automatically". | WEB-171; WWDC-127 |
| [212](https://developer.apple.com/videos/play/wwdc2026/212/) | CarPlay | 7:08 Voice Control template for all CarPlay app categories from iOS 27 (not the assistive feature). | WWDC-124; API-132 |
| [230](https://developer.apple.com/videos/play/wwdc2026/230/) | What's new in assessment on macOS | 3:00–3:30 managing accessibility features during exams; Menu Bar and Dock hidden by default; ~4:13 a true property does not enable the feature; 4:27 Switch Control quits if disallowed. | WWDC-123; MAC-409; API-120 |
| [250](https://developer.apple.com/videos/play/wwdc2026/250/) | Principles of great design | 10:22 single accessibility mention. | WWDC-104 |
| [251](https://developer.apple.com/videos/play/wwdc2026/251/) | (design, Dynamic Type) | 12:20–13:04 brand-font example; standard tab labels grow at accessibility sizes. | WWDC-129 |
| [258](https://developer.apple.com/videos/play/wwdc2026/258/) | What's new in Xcode 27 (28:00) | 9:37 Device Hub chapter; 10:36–10:43 increase contrast and choose a larger Dynamic Type size. | XCODE-121; WWDC-128 |
| [259](https://developer.apple.com/videos/play/wwdc2026/259/) | Xcode, agents, and you (24:03) | 18:25 Orchestrate; 19:56–20:00 agent adds VoiceOver labels and identifiers; 21:13–21:32 VoiceOver verification. | XCODE-124; WWDC-122 |
| [260](https://developer.apple.com/videos/play/wwdc2026/260/) | Get the most out of Device Hub (17:09) | 6:04 Configure; 8:08 Reproducing a bug; 13:53 accessibility settings that affect UI; 14:39–15:06 reproduce a large-text bug; 15:52 devicectl. | XCODE-122 |
| [269](https://developer.apple.com/videos/play/wwdc2026/269/) | What's new in SwiftUI | 2:35–2:47 interactive Liquid Glass tuned for the pointer on macOS; 3:24 `appearsActive`; 3:32–3:46 Mac menu bars show a minimal set of icons by default; use `labelStyle(.titleAndIcon)`. | MAC-410 |
| [272](https://developer.apple.com/videos/play/wwdc2026/272/) | Use SwiftUI with AppKit and UIKit | 9:29–10:05 keyboard shortcut in an NSMenu; 11:42 menu bar extra in an AppKit app. | MAC-411 |
| [285](https://developer.apple.com/videos/play/wwdc2026/285/) | (USD) | 10:15 accessibility metadata standardized in USD; `applyAPISchema("AccessibilityAPI", …)` with label and description. | WWDC-126 |
| [289](https://developer.apple.com/videos/play/wwdc2026/289/) | Modernize your AppKit app | 3:52–4:13 `NSTextSelectionManager` "new API in macOS 27"; 5:51–6:29 key view loop, `.autorecalculatesKeyViewLoop`; 6:34–8:22 menu bar and status-item keyboard navigation, expanded interface session; 14:31–14:56 scroll edge style, semibold sidebar selection; 15:01–15:24 glass bounce on click. | MAC-408; API-133; API-141 |
| [315](https://developer.apple.com/videos/play/wwdc2026/315/) | Rediscover the HTML Select Element | 0:29, 1:19 customizable select accessibility. | WEB-172; WWDC-127 |
| [8004](https://developer.apple.com/videos/play/wwdc2026/8004/) | visionOS Group Lab (63:26) | 32:04, 33:19 gaze and pinch, look to scroll; 53:36–54:29 accessibility-focused telepresence, no future plans; 54:48–55:12 wheelchair control is part of visionOS 27. | VISION-317 |

## Sessions checked with no substantive accessibility content

278 Modernize your UIKit app; 226 Create live communication experiences (no interpreter,
caption or translation mentions); 287 Build next-generation experiences with visionOS 27
(32:35); 279 Explore advances in RealityKit (23:51); 234 Design immersive environments (one
incidental "accessible" at 3:13). Sources: VISION-318; WWDC notes gaps.

## Not reviewed

370 Elevate your app's text experience with TextKit (listed in MAC-411); 282, 283, 284, 286,
320, 338, 393 (visionOS); 8013 Xcode Tips and Tricks Group Lab; 8014 watchOS Group Lab;
8015 Safari and Web Technologies Group Lab; ASL duplicates 111 and 112 separately; the
remaining 60% of 8005. No WWDC26 session names `XCUIVoiceOverService` or
`performAccessibilityAudit` in its transcript, and none covers Web Inspector accessibility
tooling or `ariaNotify`. No dedicated watchOS or visionOS accessibility session exists.
See [backlog.md](backlog.md).

# OS 27 family: community and editorial evidence on accessibility (Tier-2 / Tier-3)

Snapshot date: 2026-11-05. Tier-2 = editorial with named author and testing (AppleVis editorial, 9to5Mac hands-on, named practitioner blogs). Tier-3 = forum posts, including Apple Developer Forums, and reader comments. None of these items is a platform contract. "Tier-1 match" names the Apple-documented claim an item corroborates or conflicts with, where one was found. Unless a match is marked otherwise, it was not independently checked against Apple's release notes in this pass.

Method note: www.applevis.com returned HTTP 403 to automated fetches. The same articles were read through the mirror host mail.applevis.com, and those are the URLs cited. The AppleVis bug-tracker "fixed" pages could not be fetched, which is a gap.

## Q1. What does AppleVis report as new, changed, fixed or broken for VoiceOver, braille, Voice Control, Switch Control and low vision in each 27.x release?

### Takeaway
AppleVis covers iOS/iPadOS 27.0 in depth: one feature article (Scott Davert, 13 Sep 2026) and one editorial bug summary (AppleVis Editorial Team, 14 Sep 2026) with 26 VoiceOver bugs in Serious, Moderate and Minor tiers. Neither has braille-specific bugs beyond the feature limits Davert notes, and neither covers Voice Control, Switch Control or low vision. I found no AppleVis editorial on 27.1 or 27.2, and no AppleVis coverage of macOS, watchOS, tvOS or visionOS 27.

### Cited Findings
**Features (Tier-2: Scott Davert, AppleVis, 13 Sep 2026, iOS 27.0; supported devices iPhone SE 2nd gen and later, iPhone 11 and later)**
- COMM-101. VoiceOver hint delay is now configurable from 0.05 to 2.0 seconds (default 0.8), and hints can be set to all, app-specific or none. Tier-1 match: Apple's iOS 27 accessibility feature announcement (not checked against Apple's release notes here). — [AppleVis, Davert](https://mail.applevis.com/comment/215301)
- COMM-102. New Text Exploration (Explore by Touch reads by Paragraph, Line or Sentence) and Text Navigation (one-finger swipe moves by Line, Sentence, Paragraph or Element). — [AppleVis, Davert](https://mail.applevis.com/comment/215301)
- COMM-103. Pronunciation dictionaries can be imported or shared. The VoiceOver cursor can be shown, always hidden, or hidden during screen sharing. Bluetooth keyboard function keys run VoiceOver commands without the modifier. — [AppleVis, Davert](https://mail.applevis.com/comment/215301)
- COMM-104. Davert calls the Apple Intelligence Image Recognition overhaul the largest VoiceOver and braille upgrade. It adds Describe, Ask About, and Explore for an image, an item or the screen, plus a customizable rotor list. Live Recognition gains "Ask" and an Action Button shortcut. Per the article, iPhone 15 and earlier do not get these features. Tier-1 match: Apple's May 2026 accessibility preview ([MacRumors coverage](https://macrumors.com/2026/05/19/new-accessibility-features-with-apple-intelligence/)) and the WWDC26 Accessibility Technologies Group Lab ([WWDC26 8005](https://developer.apple.com/videos/play/wwdc2026/8005/)). — [AppleVis, Davert](https://mail.applevis.com/comment/215301)
- COMM-105. Braille changes:
  - Braille Screen Input gets predictive-text gestures, emoji search, and hold-dots character entry.
  - "Snap To Print Text Cursor" is the default with contracted braille.
  - Text field labels stay visible.
  - Braille Access adds plain-text and PDF files.
  - Perkins-style commands are added for Ask and Intelligent Description.

  Davert also says braille text editing and cursor routing problems from iOS 26 "improved significantly." — [AppleVis, Davert](https://mail.applevis.com/comment/215301)
- COMM-106. Braille limitations Davert found while testing 27.0:
  - Braille Access PDFs lose headings and formatting.
  - A 15 MB PDF with images failed to load; Davert suspects a size limit.
  - Only Image/Item Description can be mapped to Perkins-style keys.
  - Auto-Caption output is not available in braille.

  — [AppleVis, Davert](https://mail.applevis.com/comment/215301)
- COMM-107. Reader comments under the same article (Tier-3, Zoe Victoria):
  - Paragraph navigation does not announce links and sometimes skips buttons.
  - Bold and italic are no longer announced separately when swiping.
  - The Alex voice sounds rushed, with shorter pauses between element announcements.

  — [AppleVis comments](https://mail.applevis.com/comment/215301)

**Bugs (Tier-2: AppleVis Editorial Team, "iOS 27 and iPadOS 27: A Summary of VoiceOver and Braille Issues and Improvements," 14 Sep 2026, iOS/iPadOS 27.0, public release 14 Sep 2026)**
- COMM-108 (Serious). Changed states and screen updates are not announced. VoiceOver may speak old text, or the last wake time instead of the current time. No workaround; focus off and back on eventually helps. — [AppleVis Editorial](https://mail.applevis.com/comment/215423)
- COMM-109 (Serious). The per-voice Equalizer has no effect. The Pronunciation Dictionary often ignores custom entries. AppleVis advises users who rely on either not to upgrade. — [AppleVis Editorial](https://mail.applevis.com/comment/215423)
- COMM-110 (Serious). With an external audio device connected, VoiceOver is silent during Safari audio playback (workaround: pause the audio). Speech also intermittently stops mid-sentence (workaround: touch or swipe, then refocus). — [AppleVis Editorial](https://mail.applevis.com/comment/215423)
- COMM-111 (Serious). Diagnostics Mode in the new Recovery Menu gives no spoken feedback. The device restarts after roughly 5–10 minutes of inactivity. — [AppleVis Editorial](https://mail.applevis.com/comment/215423)
- COMM-112 (Moderate). Sound Curtain and Touch Curtain do not work "on some devices." Workarounds: set volume to 0% for Sound Curtain, or use Quick Settings; there is no workaround for Touch Curtain. — [AppleVis Editorial](https://mail.applevis.com/comment/215423)
- COMM-113 (Moderate, focus and navigation):
  - Lock Screen swipe focus lands on status bar items (Clock, Battery) or loops.
  - Focus on the battery indicator blocks swiping to other status bar items.
  - Moving from a text field to a combo box auto-opens its menu; a commenter says pop-up buttons are also affected.
  - "Show Notifications" sometimes cannot reach visible notifications.
  - Direct Touch in VoiceOver Quick Settings does not work.
  - Screen Recognition is missing from Quick Settings.

  — [AppleVis Editorial](https://mail.applevis.com/comment/215423)
- COMM-114 (Moderate, app-level):
  - Safari Start Page, Reading List, History and Bookmarks buttons select but do not update content.
  - Phone "All/Missed" switchers fail in Classic View.
  - Siri "Open in App" does nothing.
  - Camera shows Camera Controls edit elements outside Edit Mode.
  - Copy Speech includes markup and hints.

  — [AppleVis Editorial](https://mail.applevis.com/comment/215423)
- COMM-115 (Minor):
  - Notification Center "clear all" rotor action fails.
  - Phone keypad call button is mislabeled.
  - Siri Actions rotor shows duplicate "Delete."
  - In 24-hour time, the top of the hour is misspoken.
  - Replacing a custom gesture command sometimes does not overwrite the old one.
  - Safari bottom toolbar "Show Bookmarks" is labeled "Bookmark."
  - Camera focus wraps at the first and last elements.

  — [AppleVis Editorial](https://mail.applevis.com/comment/215423)
- COMM-116 (Not counted as a bug). VoiceOver on the internal speaker has noticeably less bass than in iOS 26, especially at low volume. AppleVis is unsure it is unintended, and a commenter says not all devices are affected. — [AppleVis Editorial](https://mail.applevis.com/comment/215423)

**Forum reports (Tier-3)**
- COMM-117. Apple-fan01, 28 Aug 2026, iPhone 17 Pro, iOS 27 beta 7:
  - VoiceOver timbre and sentence-pause settings have no effect (FB24536499).
  - VoiceOver falls back to the default voice (Daniel) during quick text insertion from a third-party dictation keyboard (FB24536545).
  - Double-tapping the status bar no longer scrolls to the top, which worked in iOS 26 (not filed).

  — [AppleVis forum](https://mail.applevis.com/forum/apple-beta-releases/bugs-voiceover-ios-27)
- COMM-118. LUCA, 18 Sep 2026, iPhone 16 Pro and iPhone 13 mini, iOS 27.0: VoiceOver prepends unrelated words ("back," "Search") to focused elements, and the problem survives a VoiceOver reset. Jellibubi traced it to corrupted Custom Labels. Deleting them fixed it as a user workaround, not a system fix. — [AppleVis forum](https://mail.applevis.com/forum/ios-ipados/help-needed-voiceover-issue-ios-27)
- COMM-119. Developer Forums, iOS 27: the Siri AI bubble stays on screen after Voice Control activates, and the user cannot dismiss it hands-free. This is the only Voice Control item found. No Switch Control items were found. — [Apple Developer Forums 847214](https://developer.apple.com/forums/thread/847214)

### Inferences
- The serious AppleVis items are audio, speech pipeline and announcement-timing failures (COMM-108–111), not new-feature failures. COMM-108 overlaps COMM-117's beta-era speech-settings reports.
- The editorial is VoiceOver on iPhone. "Braille" in its title refers to improvements, not bugs. Low vision, Voice Control and Switch Control are effectively unreviewed by AppleVis for 27.

### Gaps
- No AppleVis editorial or bug-tracker data for 27.0.1, 27.1 or 27.2 could be retrieved; the bug-tracker "fixed" pages returned 403.
- The articles give no device or build for most editorial bugs.
- No macOS 27, watchOS 27, tvOS 27 or visionOS 27 AppleVis coverage was found.
- No low-vision (Zoom, Magnifier, Accessibility Reader) user-reported bugs were found.

## Q2. Which developer-facing accessibility regressions in 27 do credible practitioners discuss?

### Takeaway
Practitioner evidence is thin. The best-documented developer change is the UIView default layout margin going to zero: iPhone Duo in 27.1, all devices in 27.2. It is discussed with an Apple engineer on the Developer Forums, but no source ties it to accessibility. Other developer reports are single Tier-3 forum posts: fractions skipped, the VoiceOver cursor not following Shift+Tab on macOS, and Accessibility Inspector contrast failures with sheets.

### Cited Findings
- COMM-120. Blake Crosley, 8 Jun 2026, Tier-2 practitioner: iOS 27 adds SwiftUI `accessibilityLinkedGroup` so VoiceOver continues reading across separate text elements. He describes it as the SwiftUI counterpart of iOS 18's next/previous text navigation element APIs. The post reports no regressions. Tier-1 match: WWDC26 sessions [219](https://developer.apple.com/videos/play/wwdc2026/219/) and [220](https://developer.apple.com/videos/play/wwdc2026/220/). — [blakecrosley.com](https://blakecrosley.com/blog/accessibility-ios-27)
- COMM-121. UIView layout margins, Apple Developer Forums thread 849929 (Tier-3, reed.1325, about early Oct 2026, iPhone Duo simulator, iOS 27.1 RC, FB25097501):
  - The reporter saw zero vertical margins in UIKit and SwiftUI.
  - A Frameworks Engineer replied that the zero default is intended, applies to iPhone Duo in 27.1 and to all devices in 27.2, and is documented in the 27.2 release notes.
  - The reporter says `preservesSuperviewLayoutMargins` does not restore vertical spacing. That objection is unanswered, and the thread is not marked resolved.
  - No accessibility or Dynamic Type mention.

  — [Developer Forums 849929](https://developer.apple.com/forums/thread/849929)
- COMM-122. Blake Crosley, 26 Oct 2026, Tier-2: he quotes the release note "On iOS 27.1 and later, the default layout margins for a UIView are zero" (issue 186294594). His probe found the change only when the app links the 27.1+ SDK. He says 27.1 shipped 23 Oct for iPhone Duo only (his inference), and 27.2 shipped 26 Oct as build 24B119. Tier-1 match: 27.2 release notes issue 186294594 (secondhand here). — [blakecrosley.com 27.2](https://blakecrosley.com/blog/ios-27-2-release-notes)
- COMM-123. Developer Forums 849493 (Tier-3, Oct 2026, iOS 27): VoiceOver skips Unicode fraction glyphs and fraction text ("½", "1/2") in SwiftUI, UIKit and WKWebView. No replies at capture. — [Developer Forums 849493](https://developer.apple.com/forums/thread/849493)
- COMM-124. Developer Forums 851810 (Tier-3, about late Oct 2026, macOS 27.0.1, Safari 27.0.1, Chrome, Firefox): when Shift+Tab moves keyboard focus to a focusable parent, the VoiceOver cursor stays on the descendant. NVDA works correctly. Filed as FB25212861. — [Developer Forums 851810](https://developer.apple.com/forums/thread/851810)
- COMM-125. Developer Forums 854036 (Tier-3, about 30 Oct 2026, Xcode 27.1, iPadOS 27.0 Simulator): Accessibility Inspector Element Detection fails only while a SwiftUI `.sheet` is presented, reporting "Potentially inaccessible text" with a nil element. The poster also reports contrast failures at maximum Dynamic Type. — [Developer Forums 854036](https://developer.apple.com/forums/thread/854036)
- COMM-126. macOS 27 managed Accessibility permission (Tier-3, enterprise and MDM):
  - PPPC Accessibility is reported deprecated or removed.
  - An App Settings grant remains user-editable (thread 850583).
  - Vendors ask for a non-consent provisioning path (thread 836770, FB23531820, 13 replies).
  - A PPPC profile was not applied on a 27.0 beta (thread 839536).

  — [Developer Forums 850583](https://developer.apple.com/forums/thread/850583); [836770](https://developer.apple.com/forums/thread/836770); [839536](https://developer.apple.com/forums/thread/839536)
- COMM-127. Liquid Glass (Tier-2, Ben Lovejoy, 9to5Mac, 12 Jun 2026, hands-on with an unnamed developer beta): iOS 27 replaces the transparency toggle with a slider, and blurring keeps text legible at maximum glass. Lovejoy reports no legibility problems. No contrast-setting change is described. — [9to5Mac](https://9to5mac.com/2026/06/12/ios-27-fixes-liquid-glass-and-not-just-with-a-slider/)
- COMM-128. Further Liquid Glass claims (an "intermediate" higher-contrast mode, Xcode 27 "deferral flags" removal) come from uncredited SEO and migration-guide blogs and were not corroborated. They are excluded as evidence. — [noqta.tn](https://www.noqta.tn/en/blog/apple-liquid-glass-ios-27-developer-adoption-guide-2026); [ecorpit.com](https://ecorpit.com/ios-27-liquid-glass-xcode-27-migration-guide-2026/)

### Inferences
- The margin change is a documented behavior change, not a regression, per the Apple engineer reply. Its accessibility impact (tighter touch spacing, Dynamic Type layouts) is plausible but unreported by any practitioner found.
- The fraction-skipping (COMM-123) and focus-desync (COMM-124) reports are the clearest candidate developer-facing AT regressions. Each rests on one post.

### Gaps
- No Deque, TPGi/Vispero or Level Access posts on iOS 27 were found.
- No practitioner reports were found on:
  - rotor changes
  - tab or picker semantics
  - Dynamic Type layout regressions
  - visionOS, watchOS or tvOS 27 accessibility
- No accessibility podcasts or newsletters with written notes were found.

## Q3. Which Apple-documented claim does each report corroborate or conflict with, and is it resolved in a later point release?

### Takeaway
Only COMM-121/122 maps to an Apple issue number: 186294594, a documented intended change, so it corroborates rather than conflicts. The feature items (COMM-101–105, 120, 127) corroborate Apple's May 2026 preview and WWDC26 sessions. None of the AppleVis bug items has a confirmed fix in a later point release in the sources found.

### Cited Findings
- COMM-129. Mapping:
  - COMM-120 corroborates WWDC26 219/220.
  - COMM-104 corroborates the WWDC26 Group Lab 8005 and Apple's May preview.
  - COMM-121/122 corroborate the 27.2 release note 186294594.
  - COMM-123/124/125 have no matching Apple-acknowledged issue found and are open FB reports.

  — [Developer Forums 849929](https://developer.apple.com/forums/thread/849929); [blakecrosley.com 27.2](https://blakecrosley.com/blog/ios-27-2-release-notes); [WWDC26 8005](https://developer.apple.com/videos/play/wwdc2026/8005/)
- COMM-130. Crosley's 27.2 summary lists no accessibility fixes in 27.2. Its listed known issues cover Nearby Interaction, Health, Shortcuts, the Simulator and StoreKit. Crosley does not cover VoiceOver, so "no fixes" means "none listed in this source," not "none exist." — [blakecrosley.com 27.2](https://blakecrosley.com/blog/ios-27-2-release-notes)
- COMM-131. Some forum results mention that issues were "finally being addressed in iOS 27.2" and an iOS 27.2 developer beta. I could not retrieve those posts, so this is unverified. — [AppleVis forum search result](https://applevis.com/forum/apple-beta-releases/bugs-voiceover-ios-27)

### Inferences
- If Crosley's account of 27.1 holds (iPhone Duo only), 27.1 was not a general fix release for existing devices. Users waiting for "27.1" fixes (COMM-132) would have had to wait for 27.2 (26 Oct).

### Gaps
- Apple's iOS 27.2 release notes were not directly fetched to check for VoiceOver fixes.
- AppleVis "Fixed iOS & iPadOS Bugs" was not accessible (403).

## Q4. Which known 27.0 issues are users still reporting after 27.1 or 27.2?

### Takeaway
No source in this pass shows an explicit post-27.1 or post-27.2 user report of a 27.0 AppleVis bug persisting, or of one being fixed. The newest evidence is late-October Developer Forums posts on 27.0.1 (macOS) and 27.1 (Xcode/iPadOS Simulator). They show some issues still open but are not re-reports of the AppleVis list.

### Cited Findings
- COMM-132. On 14–15 Sep 2026, AppleVis commenters (Pilgrim Pete, Singer Girl, Justin, Nikola Jovic) say they will wait for 27.1 for fixes. Nikola Jovic says his Feedback on a language-detection voice issue is marked "potential fix in a future update." None confirms a fix. — [AppleVis Editorial comments](https://mail.applevis.com/comment/215423)
- COMM-133. Still open at snapshot, Tier-3:
  - macOS 27.0.1 VoiceOver cursor and focus desync (COMM-124).
  - Xcode 27.1 Accessibility Inspector sheet detection (COMM-125).
  - The UIView margin objection in thread 849929 (COMM-121), unanswered at capture.

  — [851810](https://developer.apple.com/forums/thread/851810); [854036](https://developer.apple.com/forums/thread/854036); [849929](https://developer.apple.com/forums/thread/849929)

### Inferences
- Because 27.1 appears to have shipped only for iPhone Duo (Crosley's inference), "still reported after 27.1" is largely untestable for existing iPhones. The relevant point release is 27.2 (24B119, 26 Oct), and community follow-up on it was not found within ten days of release.

### Gaps
- No post-27.2 AppleVis user reports were retrieved.
- Persistence of the Serious items (COMM-108–111) and the Curtain bug (COMM-112) after 27.2 is unknown.

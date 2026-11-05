# iOS 27 changes

Third pass, 2026-11-05. Research only. This page curates the accessibility and
interaction-relevant claims. The full 322-entry release-note inventory (iOS and iPadOS share
one Apple document) is in [inventory/ios-ipados.md](inventory/ios-ipados.md); iPad-specific
claims are on [ipados.md](ipados.md). Releases and builds: [releases.md](releases.md). No
iOS 27.1 release notes exist; 27.1 shipped only for iPhone Duo.

Column key. **Release / status** uses Apple's heading (New Feature, Resolved, Known Issue,
Deprecation) plus "behavior change" where the entry changes existing behavior.
**SDK-linked** is "Yes" only when Apple's text gates the behavior on building or linking
with the 27 SDK. **Tier** follows the [README](README.md) with the evidence type after it.
Symbol availability is pending unless [api-availability.md](api-availability.md) records it.
Quotes are 25 words or fewer. Locator = section and Apple issue number, or timestamp.

## Assistive technology named by Apple

| ID | Change | Release / status | SDK-linked | Tier | Source and locator | Older ID |
| --- | --- | --- | --- | --- | --- | --- |
| IOS-323 | New `TabsPickerStyle` resembles `.segmented` "but VoiceOver reads it as 'tabs'"; for tab navigation, not value selection. DocC: 27.0, no watchOS (API-117). | 27.0 New Feature | No | Tier-1, release note + API declaration | [27.0 RN][r0] § SwiftUI › New Features, 173211711 | IOS-01; API-02 |
| IOS-181 | Fixed: with VoiceOver on and one image in the gallery, Image Playground's prompt input might not appear. | 27.0 Resolved | No | Tier-1, release note | [27.0 RN][r0] § Image Playground, 175357842 | |
| IOS-379 | Fixed: Voice Control might not respond when using Flexible Item Names to describe on-screen items. Developer counterpart of IOS-414. | 27.0 Resolved | No | Tier-1, release note | [27.0 RN][r0] § Voice Control, 184088006 | ANN-02 |
| IOS-176 | Fixed: visual feedback might not appear when tapping to indicate a heard tone in Hearing Test. | 27.0 Resolved | No | Tier-1, release note | [27.0 RN][r0] § Hearing Test, 176360906 | |
| IOS-274 | Fixed: Report a Concern attachment text from Siri "might be difficult to read while in Dark Mode". | 27.0 Resolved | No | Tier-1, release note | [27.0 RN][r0] § Siri, 178381615 | |

## User-facing accessibility features (Apple Support)

| ID | Change | Release / status | SDK-linked | Tier | Source and locator | Older ID |
| --- | --- | --- | --- | --- | --- | --- |
| IOS-411 | VoiceOver: detailed image understanding for photos, charts and screenshots; conversational questions about screen or surroundings; Action button integration (iPhone only). Device floor iPhone 15 Pro / iPhone 16 and later. | 27.0 shipped | n/a | Tier-1, Support release note | [149076](https://support.apple.com/en-us/149076) § iOS 27 › Accessibility | ANN-01; SHIP-101 |
| IOS-412 | Magnifier: conversational visual assistance, high-contrast interface, natural-language app controls. | 27.0 shipped | n/a | Tier-1, Support release note | [149076](https://support.apple.com/en-us/149076) | ANN-01; SHIP-102 |
| IOS-413 | Accessibility Reader: smarter cleanup and formatting, images and tables, on-demand summaries, translation. | 27.0 shipped | n/a | Tier-1, Support release note | [149076](https://support.apple.com/en-us/149076) | ANN-03; SHIP-105 |
| IOS-414 | "Voice Control flexible inputs" describe on-screen elements, e.g. "tap the gear". English (AU, CA, UK, US) only. | 27.0 shipped | n/a | Tier-1, Support release note + availability table | [149076](https://support.apple.com/en-us/149076); [feature availability](https://www.apple.com/ios/feature-availability/) | ANN-02; SHIP-104 |
| IOS-415 | Dictation more accurate with an on-device model on iPhone Air and iPhone 17 Pro and later. | 27.0 shipped | n/a | Tier-1, Support release note | [149076](https://support.apple.com/en-us/149076) | |
| IOS-416 | "Liquid Glass refinements improve overall readability"; Settings slider from ultra-clear to fully tinted. | 27.0 shipped | n/a | Tier-1, Support release note | [149076](https://support.apple.com/en-us/149076) § System Improvements | |
| IOS-417 | 27.0.1 fixes the touchscreen becoming unresponsive when Notification Center and Control Center open simultaneously. | 27.0.1 shipped | n/a | Tier-1, Support release note | [149076](https://support.apple.com/en-us/149076) § 27.0.1 | |
| IOS-418 | FaceTime supports adding a third-party sign-language interpreter or live captioner. No public API found. | 27.2 shipped | n/a | Tier-1, Support release note | [149076](https://support.apple.com/en-us/149076) § 27.2 | ANN-06; SHIP-04; SHIP-115 |
| IOS-419 | Granular text selection in Siri responses. | 27.2 shipped | n/a | Tier-1, Support release note | [149076](https://support.apple.com/en-us/149076) § 27.2 | |
| SHIP-01 | Generated subtitles on iPhone 15 Pro or iPhone 16 and later; English. | 27.0 shipped | n/a | Tier-1, support guide | [iPhone subtitles guide](https://support.apple.com/en-us/guide/iphone/iph3e2e23d1/27/ios/27) | CROSS-04; C-10 |

## Focus, keyboard and CarPlay

| ID | Change | Release / status | SDK-linked | Tier | Source and locator | Older ID |
| --- | --- | --- | --- | --- | --- | --- |
| IOS-119 | Fixed: `CPNavigationSession` ETA Tray panel items might not receive focus. Only CarPlay focus entry. | 27.0 Resolved | No | Tier-1, release note | [27.0 RN][r0] § CarPlay, 177508893 | pass-2 iOS follow-up |
| IOS-120–123 | CarPlay panel fixes: `panelDidHide(_:)` not called (177590525); `CPMapPanel` close button (177592347); symbol-button handler (177595560); steering-wheel track buttons (177832695). | 27.0 Resolved | No | Tier-1, release note | [27.0 RN][r0] § CarPlay | |
| IOS-345 | Fixed: with `fullScreenCover`, a zoom navigation transition and `@FocusState` set in `onAppear`, the keyboard waited for the transition. | 27.0 Resolved | No | Tier-1, release note | [27.0 RN][r0] § SwiftUI, 178421089 | |
| IOS-188 | Fixed: unlocalized text for paste candidates. | 27.0 Resolved | No | Tier-1, release note | [27.0 RN][r0] § Keyboard, 180881635 | |
| WWDC-124 | CarPlay Voice Control template available to all CarPlay app categories from iOS 27 (a Siri-style template, not the assistive feature). | 27.0 | n/a | Tier-1, transcript | [WWDC26-212](https://developer.apple.com/videos/play/wwdc2026/212/) 7:08 | API-132 |

## Scenes, windows and external displays

| ID | Change | Release / status | SDK-linked | Tier | Source and locator | Older ID |
| --- | --- | --- | --- | --- | --- | --- |
| IOS-358 | `UIScene.extendStateRestoration` / `completeStateRestoration` extend state restoration across background-to-foreground transitions when linked on the 27 SDK. DocC lists iOS 15.0 (C-04). | 27.0 New Feature | Yes | Tier-1, release note | [27.0 RN][r0] § UIKit › New Features, 161843040 | IOS-02; API-145 |
| IOS-373 | Apps built with the latest SDK "must adopt the scene-based life cycle or they fail to launch". | 27.0 Deprecation + behavior change | Yes | Tier-1, release note | [27.0 RN][r0] § UIKit › Deprecations, 141837548 | |
| IOS-359 | Apps built with the 27.0 SDK must include a launch screen key or face App Store rejection. | 27.0 behavior change | Yes | Tier-1, release note | [27.0 RN][r0] § UIKit, 168247372 | IPAD-03 |
| IOS-363 / IOS-325 | `windowExternalDisplayNonInteractive` scenes no longer offered automatically; use `UISceneAccessory.externalNonInteractive` or SwiftUI `.sceneAccessory`. | 27.0 behavior change | Yes | Tier-1, release note | [27.0 RN][r0] § UIKit 177015874; § SwiftUI 175548901 | |
| IOS-367 | Fixed: `UISceneClosureConfirmation` did not present a dialog. | 27.0 Resolved | No | Tier-1, release note | [27.0 RN][r0] § UIKit, 169108042 | |
| IOS-370–372 | iPhone Mirroring: honors orientations until resize (178555304); `UIRequiresFullScreen` resizes are discrete `UIScreen` changes (178558224); scene starts on `UIScreen.main` (178558897). | 27.0 Resolved | Yes | Tier-1, release note | [27.0 RN][r0] § UIKit | |
| IOS-185–187 | Further iPhone Mirroring fixes (180961142, 181023494, 181057810). | 27.0 Resolved | No | Tier-1, release note | [27.0 RN][r0] § iPhone Mirroring | |
| IOS-354 | Fixed: black pill on the CarPlay screen after iPhone Mirroring. | 27.0 Resolved | No | Tier-1, release note | [27.0 RN][r0] § System Experience, 177893758 | |

## Traits, layout, navigation, toolbars and status bar

| ID | Change | Release / status | SDK-linked | Tier | Source and locator | Older ID |
| --- | --- | --- | --- | --- | --- | --- |
| IOS-361 | A presented view controller inherits traits by walking its superview chain, not from the presentation controller; custom `UIPresentationController` subclasses may need updates. | 27.0 behavior change | Yes | Tier-1, release note | [27.0 RN][r0] § UIKit, 170005251 | IOS-03 |
| IOS-398 | "On iOS 27.1 and later, the default layout margins for a `UIView` are zero"; view controllers still supply `systemMinimumLayoutMargins`; use `preservesSuperviewLayoutMargins`. | 27.2 New Feature + behavior change (documents 27.1) | Not stated (C-08) | Tier-1, release note | [27.2 RN][r2] § UIKit › New Features, 186294594 | IOS-04; COMM-121/122 |
| IOS-364 / IOS-331 | `UINavigationItem.navigationBarMinimization` replaces `barMinimizeBehavior`; SwiftUI `toolbarMinimizationBehavior` replaces `toolbarMinimizeBehavior`. | 27.0 New Feature | No | Tier-1, release note | [27.0 RN][r0] § UIKit 177953926; § SwiftUI 177954148 | |
| IOS-362 | With center search-bar placement, the `UISearchController` scope bar sits inline on the search-field row. | 27.0 behavior change | Yes | Tier-1, release note | [27.0 RN][r0] § UIKit, 173860616 | |
| IOS-365 | A `UIScrollEdgeElementContainerInteraction` container view may contribute to the scroll-edge-effect shape. | 27.0 New Feature | No | Tier-1, release note | [27.0 RN][r0] § UIKit, 179191941 | |
| IOS-410 | iOS-26-SDK apps rendered a fully transparent soft scroll edge above `safeAreaBar(edge:)` on iOS 27; in 27.3 they get the iOS 27 soft edge. | **27.3 beta** Resolved (behavior statement) | Yes (iOS 26 SDK apps) | Tier-1, release note | [27.3 beta RN][r3] § SwiftUI, 188312290 | IOS-05 |
| IOS-340 | `containerRelativeFrame` accounts for safe-area insets on a ScrollView's non-scrollable axis. | 27.0 Resolved | Yes | Tier-1, release note | [27.0 RN][r0] § SwiftUI, 165913417 | |
| IOS-342 | `controlSize`, `buttonSizing`, `buttonRepeatBehavior`, `menuIndicatorVisibility`, `ButtonBorderShape` reset to defaults in sheets and popovers. | 27.0 behavior change | Yes | Tier-1, release note | [27.0 RN][r0] § SwiftUI, 167448274 | |
| IOS-321 | A `TabView` enforces a visible selection and "might crash" if set to a hidden or unavailable tab. | 27.0 behavior change | Yes | Tier-1, release note | [27.0 RN][r0] § SwiftUI, 164516837 | |
| IOS-315 / IOS-322 | `.toolbarColorScheme(_, for: .statusBar)` (55162154) and `.toolbarVisibility(…, for: .statusBar)` (165329279). | 27.0 New Feature | No | Tier-1, release note | [27.0 RN][r0] § SwiftUI | |
| IOS-366 | Deprecated `UIApplication` status-bar accessors might return NaN or null. | 27.0 Resolved (behavior) | Yes | Tier-1, release note | [27.0 RN][r0] § UIKit, 162044221 | |
| IOS-337 | Status-bar tap scroll-to-top now updates a bound `scrollPosition` ("2027 SDKs"). | 27.0 Resolved | Yes | Tier-1, release note | [27.0 RN][r0] § SwiftUI, 111501113 | COMM-117 (inference) |
| IOS-293 | Fixed: status bar might appear blurred. | 27.0 Resolved | No | Tier-1, release note | [27.0 RN][r0] § Status Bar, 179470940 | |
| IOS-344 / IOS-328 | Button icon/title spacing in List section headers (175681345); `GeometryProxy.concentricCornerRadii` (177185166). | 27.0 | No | Tier-1, release note | [27.0 RN][r0] § SwiftUI | |

## Menus

| ID | Change | Release / status | SDK-linked | Tier | Source and locator | Older ID |
| --- | --- | --- | --- | --- | --- | --- |
| IOS-326 | `LabeledContent` inside a `Menu` maps its value to the menu-item subtitle. | 27.0 behavior change | Yes | Tier-1, release note | [27.0 RN][r0] § SwiftUI, 175594929 | |
| IOS-343 | "Fixed:" Menu labels cannot contain controls, gesture views or representables with gesture recognizers. | 27.0 Resolved (rule statement; C-21) | No | Tier-1, release note | [27.0 RN][r0] § SwiftUI, 169091260 | |
| IOS-368 | Fixed: `UIMenuLeaf` lacked `subtitle`. | 27.0 Resolved | No | Tier-1, release note | [27.0 RN][r0] § UIKit, 173271862 | |

Menu-image reduction (iPadOS and macOS) is on [ipados.md](ipados.md) and [macos.md](macos.md).

## Text and text input

| ID | Change | Release / status | SDK-linked | Tier | Source and locator | Older ID |
| --- | --- | --- | --- | --- | --- | --- |
| IOS-317 | Selectable `Text` uses the system text-selection UI and "might include additional gestures"; use `.highPriorityGesture()` for custom gestures that should win. | 27.0 behavior change | Yes | Tier-1, release note | [27.0 RN][r0] § SwiftUI, 79770704 | |
| IOS-319 / IOS-338 | Selectable `Text` supports `TextRenderer` (158160386); custom renderer dropped on selectable text fixed (151015350). | 27.0 | Yes (319) | Tier-1, release note | [27.0 RN][r0] § SwiftUI | |
| IOS-324 | `TextInputBorderShape` and `textInputBorderShape(_:)`; `.squareBorder` and `.roundedBorder` soft-deprecated for `.bordered`. DocC 27.0 (API-143). | 27.0 New Feature | No | Tier-1, release note + API declaration | [27.0 RN][r0] § SwiftUI, 173362083 | |
| IOS-356 | "`NSTextTable` and its related objects and types are available to UIKit clients starting with OS 27 releases." Symbol availability pending. | 27.0 New Feature | No | Tier-1, release note | [27.0 RN][r0] § TextKit, 159870239 | IOS-06 |
| IOS-383 | Writing Tools unresponsive after the Plus button; workaround: force quit Messages. No later fix listed. | 27.0 Known Issue | No | Tier-1, release note | [27.0 RN][r0] § Writing Tools, 177097101 | |
| CROSS-01 / WWDC-107 | Starting in iOS 27, SwiftUI `accessibilityLinkedGroup` also links cross-element text navigation. Symbol is iOS 14.0 (API-101). | 27.0 behavior | n/a | Tier-1, transcript | [WWDC26-219](https://developer.apple.com/videos/play/wwdc2026/219/) 7:59–8:06 | CROSS-01; API-01; COMM-120 |
| CROSS-02 | Page-turn traits with scrolling and edit-category custom actions demonstrated; both predate 27 (API-102, API-103). | revisited | n/a | Tier-1, transcript | [WWDC26-219](https://developer.apple.com/videos/play/wwdc2026/219/) 9:55, 11:46 | CROSS-02; API-03 |

## Voice input and speech output

| ID | Change | Release / status | SDK-linked | Tier | Source and locator | Older ID |
| --- | --- | --- | --- | --- | --- | --- |
| IOS-147 | New on-device Dictation model via Keyboard settings > Dictation > "Advanced Dictation Preview". | 27.0 New Feature | No | Tier-1, release note | [27.0 RN][r0] § Dictation, 178444388 | IOS-415 |
| IOS-148–151 | Dictation fixes: "New Line"/"All Caps" (177959708); spoken punctuation word inserted (178078177); contact names (178079519); extra words (178269104). | 27.0 Resolved | No | Tier-1, release note | [27.0 RN][r0] § Dictation | |
| IOS-152 | Voice Editing commands ("Change X to Y", "Delete X", Undo/Redo) "might not work reliably"; no workaround; no later fix listed. | 27.0 Known Issue | No | Tier-1, release note | [27.0 RN][r0] § Dictation, 173448573 | |
| IOS-261 | Fixed: answering Announce Notifications by voice or head gesture prompted unlock instead of reading the message. | 27.0 Resolved | No | Tier-1, release note | [27.0 RN][r0] § Siri, 177733317 | |
| IOS-262 / IOS-266 | Fixed: new voices fell back to legacy voices in Low Power Mode or when hot (177742977); Pace/Expressiveness could not be changed (177969955). | 27.0 Resolved | No | Tier-1, release note | [27.0 RN][r0] § Siri | |
| IOS-290 | Siri might cut off word endings during navigation; workaround: reduce expressivity or turn off expressive voices. | 27.0 Known Issue | No | Tier-1, release note | [27.0 RN][r0] § Siri, 181266301 | |
| IOS-283–288 | Siri voice-command known issues: no way to say "photo one" (176812955); "Send these" may apply to all results (171728298); "read my last message" may read an unknown sender (178049066); wrong photo count (177376984); Maps snippets incomplete (177116121). | 27.0 Known Issue | No | Tier-1, release note | [27.0 RN][r0] § Siri | |
| IOS-360 | Siri can load resources through `UIDragInteractionDelegate` without a drag gesture; avoid animations or modal UI in `sessionWillBegin`. | 27.0 behavior change | No | Tier-1, release note | [27.0 RN][r0] § UIKit, 168884200 | |

## Media and audio

| ID | Change | Release / status | SDK-linked | Tier | Source and locator | Older ID |
| --- | --- | --- | --- | --- | --- | --- |
| IOS-216 / IOS-217 | `RemoteMediaSession` always provisions production APNs tokens (Known, 186036238); foreground session missing from Control Center (Resolved, 183641494). | 27.0 | No | Tier-1, release note | [27.0 RN][r0] § Now Playing | |
| IOS-115 | AudioAccessoryKit lets third-party headphones supply info for fixed spatial audio; developer testing now, EU customers "in a future iOS 27" release. | 27.0 New Feature | No | Tier-1, release note | [27.0 RN][r0] § AudioAccessoryKit, 178275661 | |
| IOS-101 / IOS-124 | AirPlay to Home Theaters with PIN fixed (176462871); CarPlay stereo silent after Spatial Audio fixed (178189709). | 27.0 Resolved | No | Tier-1, release note | [27.0 RN][r0] | |
| CROSS-04 / WWDC-117/118 | Generated English subtitles from English audio on iOS 27; no implementation needed; authored subtitles keep priority; translation on iOS and macOS. | 27.0 system feature | n/a | Tier-1, transcript | [WWDC26-256](https://developer.apple.com/videos/play/wwdc2026/256/) 2:14, 3:03, 4:11 | CROSS-04 |
| CROSS-05 | System players offer subtitle selection and style preview; preview APIs are 26.4 (API-112–115; C-13). | 26.4 APIs, showcased | n/a | Tier-1, transcript + API declaration | [WWDC26-256](https://developer.apple.com/videos/play/wwdc2026/256/) 4:31, 5:39, 7:10–7:43 | CROSS-05 |
| API-117b | AVKit `AVPlaybackUserInterfaceMediaSelectionControllable` legible options. | 27.0 new symbol (iOS, iPadOS, Catalyst) | n/a | Tier-1, API declaration | [api-availability.md](api-availability.md) | |

## Visual legibility and other UI defects

| ID | Change | Release / status | Tier | Source and locator |
| --- | --- | --- | --- | --- |
| IOS-129 | "Add a Control" button small and clipped (170774279). | 27.0 Resolved | Tier-1, release note | [27.0 RN][r0] § Control Center |
| IOS-159 | Fitness+ duplicate title text in landscape on larger iPhones (177964121). | 27.0 Resolved | Tier-1, release note | [27.0 RN][r0] § Fitness+ |
| IOS-190 | Lock Screen grabber in wrong location or orientation (178174745). | 27.0 Resolved | Tier-1, release note | [27.0 RN][r0] § Lock Screen |
| IOS-126 | Ringing alarm could not be stopped from the Lock Screen without unlocking (177728602). | 27.0 Resolved | Tier-1, release note | [27.0 RN][r0] § Clock |
| IOS-313 | Swift Charts conditionals warned or crashed below a 27.0 deployment target (174168981). | 27.0 Resolved | Tier-1, release note | [27.0 RN][r0] § Swift Charts |

## Accessibility API additions relevant to iOS

New 27.0 symbols (all Tier-1, API declaration; details in [api-availability.md](api-availability.md)):
API-118 `AccessibilitySettings.isApplicationAccessibilityEnabled`; API-119
`AXSpeechAttributeSSML`; API-116 `MACaptionAppearanceDomain.videoConferencing`; API-120
assessment toggles (`allowsAccessibilityVoiceOver`, `…SpokenContent` on iOS); API-121
`GestureInputKinds`; API-122 `XCUIVoiceOverService`; API-123 `PKStrokeRecognizer`. New in
27.1: API-117a sign-language media characteristic. Deprecated at 27.3: API-127
`ContentSizeCategory`, API-128 legacy `accessibility(label:)` modifiers.

## Negative findings

Searches of the 27.0, 27.2 and 27.3 beta Markdown for "accessib", "Dynamic Type", "Switch
Control", "Full Keyboard", "haptic" and "caption" return zero hits. The developer notes carry
no `UIAccessibility` API entries; consumer features appear only on Support pages.

## Community evidence

User reports are on [community.md](community.md): AppleVis feature and bug summaries for
iOS 27.0 (COMM-101 to COMM-116), forum reports (COMM-117 to COMM-125). None is a platform
contract.

## Research inference (not Apple-stated)

- SDK-linked entries carry the most regression risk when an app moves to the 27 SDK:
  selectable-text gestures (IOS-317), TabView selection crash (IOS-321), trait propagation
  (IOS-361), control-size reset in sheets (IOS-342), scope-bar placement (IOS-362),
  external-display scenes (IOS-363), scene life cycle (IOS-373), launch screen (IOS-359),
  status-bar accessors (IOS-366).
- IOS-361 likely affects Dynamic Type and content-size propagation into custom
  presentations; Apple does not say so.
- IOS-398 margins may affect touch spacing and large-text layouts; no source reports this.
- Most 27.0 "Resolved" rows are beta-cycle fixes; several name betas in their text. Exceptions
  carry older FB numbers (e.g. IOS-337, FB12477370).
- Of 27.0 known issues, only two StoreKit Testing items (184155259, 184255116) are listed as
  fixed in 27.2. None of the accessibility-adjacent known issues (IOS-152, IOS-290, IOS-283–288,
  IOS-383) has a later fix entry; absence is not evidence either way.

[r0]: https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-27-release-notes
[r2]: https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-27_2-release-notes
[r3]: https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-27_3-release-notes

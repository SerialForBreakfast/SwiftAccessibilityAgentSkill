# iOS & iPadOS 27 (27.0, 27.0.1, 27.1, 27.2, 27.3 beta): exhaustive release-note claim inventory (research pass 3)

Snapshot date: 2026-11-05. The 27.3 beta is kept separate from stable releases throughout: release column = `27.3 beta`.

Retrieval log (curl, 2026-11-05):

| Source | URL | HTTP | Bytes | SHA-256 |
|---|---|---|---|---|
| iOS & iPadOS 27 Release Notes (.md) | https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-27-release-notes.md | 200 | 68,415 | c544e3d8fee60d339135a0f53a4910d43e5255a62bb2ef066c73d9b36f5f05f3 |
| iOS & iPadOS 27.2 Release Notes (.md) | https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-27_2-release-notes.md | 200 | 4,276 | 7a9757f67c75e62434b8868de53d598ba757b8742ae4dd5200626f77048c2a11 |
| iOS & iPadOS 27.3 Beta Release Notes (.md) | https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-27_3-release-notes.md | 200 | 5,111 | eec301ea75e066f62988e7d768821b3825ebce0de15d7e006b85de45e1dbcfa5 |
| Inferred 27.1 URL (.md) | https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-27_1-release-notes.md | 404 (HTML error shell) | 15,639 | c8a4f47291ff4563e78e90f4326f3d457661a44a8041d823b1c21b325eb7c510 |
| Release-notes index (.md) | https://developer.apple.com/documentation/ios-ipados-release-notes.md | 200 | 13,373 | 8f895d6ac4b571f0d26210a710538acc6495f9fa1e7a2958dbc61eb701569605 |
| Release-notes index (DocC JSON) | https://developer.apple.com/tutorials/data/documentation/ios-ipados-release-notes.json | 200 | 46,438 | 77a2216e3386100f1e684cbc0abd7673578362bab0884ed80a3fe9337604bc33 |
| About iOS 27 Updates (HTML) | https://support.apple.com/en-us/149076 | 200 | (HTML) | 3109438f3d9179984e10e569967ee9d4c1d149929f7d41c21132dc4192fefeaf |
| About iPadOS 27 Updates (HTML) | https://support.apple.com/en-us/149075 | 200 | (HTML) | 094a127ea73550b1ce0e009fa76391a36c1e9fa3043b02e884069029f02d5ff2 |
| Apple security releases | https://support.apple.com/en-us/100100 | 200 | 324,687 | (not hashed; dynamic page) |
| Apple Developer News – Releases (HTML + RSS) | https://developer.apple.com/news/releases/ ; https://developer.apple.com/news/releases/rss/releases.rss | 200 | 237,420 / 25,253 | (not hashed; dynamic page) |

Parsing method: every `- ` bullet under a `###` section and `####` status heading in the three Markdown files was extracted by script. Result: **322 release-note entries** (27.0: 296; 27.2: 14; 27.3 beta: 12). By status: 27.0 has 65 New Features, 197 Resolved, 23 Known Issues, and 11 Deprecations. 27.2 has 2 New Features, 5 Resolved, and 7 Known Issues. 27.3 beta has 3 New Features, 3 Resolved, 2 Known Issues, and 4 Deprecations. **92 entries** are flagged as relevant to accessibility or adjacent interaction. **12 entries** are iPad-specific (IPAD-101..112).

Legend for the inventory tables:
- **Status** uses Apple's section heading: New Features → New Feature, Resolved Issues → Resolved, Known Issues → Known Issue, Deprecations → Deprecation. "+ Behavior change" is my classification. It marks an entry that changes runtime or build behavior for existing code rather than only adding API. "(no Fixed: prefix)" marks an entry that sits under Resolved Issues but reads as a behavior statement.
- **SDK** = "Yes" when the entry text gates the behavior on building or linking with the 27 SDK (or says "Recompile").
- **Quote** = Apple's text, truncated at 22 words (an ellipsis marks truncation). Workaround text is truncated at 18 words.
- All inventory rows are **Tier-1** (Apple Developer release notes). The locator is release-notes URL + `###` section + issue number.
- Symbol availability for any API named in these notes is **pending declaration review**. No DocC availability JSON was checked, and release notes are not used to infer introduction versions.

## Key question 1: Entry-by-entry inventory of the iOS & iPadOS 27 release notes, with accessibility and adjacent-interaction flags

### Takeaway
The 27.0 notes hold 296 entries in about 85 sections, 27.2 adds 14, and the 27.3 beta adds 12, for 322 atomic Tier-1 claims. Of these, 92 bear on accessibility or adjacent interaction. Only three name an assistive technology outright: VoiceOver in IOS-323 (`TabsPickerStyle`, 173211711) and IOS-181 (Image Playground, 175357842), and Voice Control in IOS-379 (184088006). Most of the relevant surface is UIKit/SwiftUI behavior tied to the 27 SDK: scenes and windows, menus, text selection, trait propagation, status bar, margins, navigation and toolbar minimization, and the iPad resize model. The developer notes contain no explicit Switch Control, Full Keyboard Access, Dynamic Type, captions, or haptics entries. Those features appear only in the consumer "About iOS 27 Updates" pages (Key question 2).

### Cited Findings

#### A. Accessibility-named entries (Tier-1)
- IOS-323: SwiftUI New Feature (173211711). The new `TabsPickerStyle` resembles `.segmented`, "but VoiceOver reads it as 'tabs'". It is meant for pickers that represent tab-based navigation, not value selection. Not SDK-gated in the text. **Matches IOS-01.** Symbol availability is pending declaration review. — [iOS & iPadOS 27 Release Notes, SwiftUI › New Features, 173211711](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-27-release-notes)
- IOS-181: Image Playground Resolved (175357842). Fixed: "When VoiceOver is enabled and the gallery contains only one image, the prompt input UI might not appear." — [27.0 RN, Image Playground › Resolved Issues, 175357842](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-27-release-notes)
- IOS-379: Voice Control Resolved (184088006). Fixed: Voice Control "might not respond when using Flexible Item Names to describe items on the screen." This is the developer-side counterpart of the consumer feature "Voice Control flexible inputs". — [27.0 RN, Voice Control › Resolved Issues, 184088006](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-27-release-notes)
- IOS-176: Hearing Test Resolved (176360906). Visual feedback might not appear when you tap the screen to indicate you heard a tone. This touches non-auditory feedback for a hearing-health flow. — [27.0 RN, Hearing Test, 176360906](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-27-release-notes)
- IOS-274: Siri Resolved (178381615). In Report a Concern flows started with Siri, attachment text "might be difficult to read while in Dark Mode" (a contrast defect). — [27.0 RN, Siri, 178381615](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-27-release-notes)

#### B. Focus, keyboard, and CarPlay focus (Tier-1)
- IOS-119: CarPlay Resolved (177508893). "`CPNavigationSession` ETA Tray panel items might not receive focus." This is the only CarPlay focus entry. — [27.0 RN, CarPlay, 177508893](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-27-release-notes)
- IOS-120/121/122: CarPlay Resolved. `panelDidHide(_:)` might not be called (177590525). `CPMapPanel` might not dismiss on close-button tap (177592347). The `CPMapPanelButtonConfiguration` symbol-button handler might not be called (177595560). IOS-123: steering-wheel next/previous track buttons might not work (177832695). — [27.0 RN, CarPlay](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-27-release-notes)
- IOS-345: SwiftUI Resolved (178421089). With `fullScreenCover` + `.navigationTransition(_:)` and `@FocusState` set to true in `.onAppear`, the keyboard waited for the zoom transition to finish before animating. — [27.0 RN, SwiftUI › Resolved, 178421089](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-27-release-notes)
- IOS-188: Keyboard Resolved (180881635). Unlocalized text could appear for paste candidates. — [27.0 RN, Keyboard, 180881635](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-27-release-notes)

#### C. Scenes, windows, external displays, iPad resizing (Tier-1)
- IOS-358: UIKit New Feature (161843040). When linked on the iOS 27 SDK, `UIScene.extendStateRestoration`/`completeStateRestoration` extend state restoration across background→foreground transitions. SDK-linked. **Matches IOS-02.** — [27.0 RN, UIKit › New Features, 161843040](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-27-release-notes)
- IOS-373: UIKit Deprecation + behavior change (141837548). "Apps built with the latest SDK must adopt the scene-based life cycle or they fail to launch." SDK-linked. — [27.0 RN, UIKit › Deprecations, 141837548](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-27-release-notes)
- IOS-359: UIKit (168247372). Apps built with the 27.0 SDK must include a launch screen (`UILaunchStoryboardName`, `UILaunchStoryboards`, `UILaunchScreen`, or `UILaunchScreens`). Otherwise they are rejected once the App Store accepts 27.0-SDK builds. — [27.0 RN, UIKit, 168247372](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-27-release-notes)
- IOS-363 (UIKit, 177015874) and IOS-325 (SwiftUI, 175548901): with the 27.0 SDK, `windowExternalDisplayNonInteractive` scenes are no longer offered automatically. Use `registerSceneAccessory(_:)` with `UISceneAccessory.externalNonInteractive`, or SwiftUI `.sceneAccessory` with `ExternalNonInteractiveAccessory`. Both are SDK-linked. — [27.0 RN, UIKit/SwiftUI](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-27-release-notes)
- IOS-367: UIKit Resolved (169108042). `UISceneClosureConfirmation` did not present a confirmation dialog. — [27.0 RN, UIKit, 169108042](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-27-release-notes)
- iPhone Mirroring scene fixes, all SDK-linked: IOS-370 (178555304) honors supported orientations until the user resizes. IOS-371 (178558224) makes `UIRequiresFullScreen` resizes discrete `UIScreen` changes. IOS-372 (178558897) starts the scene on `UIScreen.main`. Non-SDK mirroring fixes are IOS-185/186/187 (180961142, 181023494, 181057810). — [27.0 RN, UIKit / iPhone Mirroring](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-27-release-notes)
- **iPad-specific (IPAD-107..112), UIKit Resolved, all SDK-linked "built with the iOS 27 SDK":**
  - IPAD-107 (166422120): supported interface orientations should no longer be a condition for continuous resizability.
  - IPAD-108 (178559386): with `UIRequiresFullScreen`, `UIScreen.main` bounds should stay fixed.
  - IPAD-109 (178560235): resizes should arrive as discrete `UIScreen` changes.
  - IPAD-110 (178561952): an iPhone-only app should ignore supported orientations after the first resize.
  - IPAD-111 (178562971): an iPhone-only app with `UIRequiresFullScreen` gets discrete resizes.
  - IPAD-112 (178573319): an iPhone-only app supporting only portrait or only landscape had layout break in unsupported orientations.
  - Source: [27.0 RN, UIKit › Resolved Issues](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-27-release-notes)
- IPAD-105: System Experience Resolved (176281601). With Siri off and an iPad extended to an external display showing Spotlight, disconnecting the display might crash the system. IOS-354 (177893758): a black pill might appear on the CarPlay screen after iPhone Mirroring. — [27.0 RN, System Experience](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-27-release-notes)

#### D. Traits, layout, margins, navigation and toolbars, status bar (Tier-1)
- IOS-361: UIKit (170005251). With the iOS 27.0 SDK, a presented view controller inherits its trait collection by walking its superview chain rather than taking it directly from the presentation controller. Custom `UIPresentationController` subclasses may need updates. SDK-linked. This is relevant to Dynamic Type and content-size-category propagation. **Matches IOS-03.** — [27.0 RN, UIKit, 170005251](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-27-release-notes)
- IOS-398: 27.2 UIKit New Feature (186294594). "On iOS 27.1 and later, the default layout margins for a `UIView` are zero." View controllers still supply `systemMinimumLayoutMargins`. To inherit them, set `preservesSuperviewLayoutMargins = true`. The text does not say this is SDK-gated. **Matches IOS-04.** — [iOS & iPadOS 27.2 RN, UIKit › New Features, 186294594](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-27_2-release-notes)
- IOS-364: UIKit (177953926). `UINavigationItem.navigationBarMinimization` replaces `barMinimizeBehavior` and `barMinimizationSafeAreaAdjustment`. IOS-331 (SwiftUI, 177954148): `toolbarMinimizationBehavior` replaces `toolbarMinimizeBehavior`. — [27.0 RN, UIKit/SwiftUI](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-27-release-notes)
- IOS-362: UIKit (173860616). With the 27.0 SDK and center search-bar placement, the `UISearchController` scope bar sits inline on the search-field row, including inside navigation bars. SDK-linked. — [27.0 RN, UIKit, 173860616](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-27-release-notes)
- IOS-365: UIKit (179191941, FB23027596). A `UIScrollEdgeElementContainerInteraction` container view may contribute to the scroll edge effect shape. IOS-410 (27.3 beta SwiftUI, 188312290): iOS-26-SDK apps rendered a fully transparent `ScrollEdgeEffectStyle.soft` edge above `safeAreaBar(edge:)` on iOS 27; in 27.3 and later they get the iOS 27 soft edge. **Matches IOS-05.** — [27.0 RN UIKit](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-27-release-notes); [27.3 Beta RN SwiftUI › Resolved, 188312290](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-27_3-release-notes)
- IOS-340: SwiftUI Resolved (165913417). With the 27.0 SDKs, `containerRelativeFrame` correctly accounts for safe-area insets on a `ScrollView`'s non-scrollable axis. SDK-linked. IOS-342 (167448274): `controlSize`, `buttonSizing`, `buttonRepeatBehavior`, `menuIndicatorVisibility`, and `ButtonBorderShape` now reset to defaults inside sheets and popovers (SDK-linked). IOS-344 (175681345): icon/title spacing of a Button in a List section header or footer. IOS-328 (177185166): `GeometryProxy.concentricCornerRadii`. — [27.0 RN, SwiftUI](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-27-release-notes)
- Status bar:
  - IOS-315 (55162154/FB7234376): `.toolbarColorScheme(_, for: .statusBar)`.
  - IOS-322 (165329279): `.toolbarVisibility(..., for: .statusBar)`.
  - IOS-366 (162044221): deprecated `UIApplication` status-bar accessors might return NaN or null with the 27 SDK (SDK-linked).
  - IOS-337 (111501113/FB12477370): status-bar tap scroll-to-top now updates a bound `scrollPosition` (SDK-linked, "2027 SDKs").
  - IOS-293 (179470940): status bar might appear blurred.
  - Source: [27.0 RN, SwiftUI/UIKit/Status Bar](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-27-release-notes)
- IOS-321: SwiftUI (164516837). With the 27.0 SDKs, a `TabView` enforces that its selection is a visible tab. It "might crash" when selection is set to a hidden or unavailable tab. SDK-linked. — [27.0 RN, SwiftUI, 164516837](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-27-release-notes)

#### E. Menus (Tier-1)
- IPAD-104 (SwiftUI, 170480710) and IPAD-106 (UIKit, 170479084): on iPadOS 27.0 (and macOS 27.0), the menu bar and context menus show a reduced set of menu item images. SwiftUI hides symbol images by default; use `.labelStyle(.titleAndIcon)` to keep one. UIKit adds `UIMenuElement.preferredImageVisibility`. The text does not say this is SDK-gated. — [27.0 RN, SwiftUI/UIKit](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-27-release-notes)
- IOS-326 (175594929): with the 27.0 SDKs, `LabeledContent` inside a `Menu` maps its value to the menu item subtitle. IOS-343 (169091260): Menu labels cannot contain controls, gesture views, or representables with gesture recognizers. The "Fixed:" framing suggests this is now enforced or documented. IOS-368 (173271862): `UIMenuLeaf` lacked the `subtitle` property. — [27.0 RN](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-27-release-notes)

#### F. Text, TextKit, text input (Tier-1)
- IOS-317: SwiftUI (79770704/FB9208920). With the iOS/iPadOS 27.0 SDKs, `Text` with `.textSelection(.enabled)` uses the system text-selection UI instead of a callout menu and "might include additional gestures". Apple advises `.highPriorityGesture()` for custom gestures that should win. SDK-linked. — [27.0 RN, SwiftUI, 79770704](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-27-release-notes)
- IOS-319 (158160386): selectable `Text` supports `TextRenderer` (SDK-linked). IOS-338 (151015350): a custom `TextRenderer` was dropped on selectable text. IOS-324 (173362083): `TextInputBorderShape` and `textInputBorderShape(_:)`; `.squareBorder` and `.roundedBorder` are soft-deprecated in favor of `.bordered`. — [27.0 RN, SwiftUI](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-27-release-notes)
- IOS-356: TextKit (159870239). "`NSTextTable` and its related objects and types are available to UIKit clients starting with OS 27 releases." **Matches IOS-06.** — [27.0 RN, TextKit, 159870239](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-27-release-notes)
- IOS-383: Writing Tools Known Issue (177097101). Writing Tools becomes unresponsive when you interact with the Plus button. Workaround: force quit Messages. — [27.0 RN, Writing Tools](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-27-release-notes)

#### G. Voice input and speech output: Dictation and Siri (Tier-1)
- IOS-147: Dictation New Feature (178444388). A new on-device model, enabled via Keyboard settings > Dictation > "Advanced Dictation Preview". Resolved:
  - IOS-148 (177959708): "New Line"/"All Caps" commands.
  - IOS-149 (178078177): the spoken punctuation word was inserted along with the punctuation.
  - IOS-150 (178079519): contact names not recognized.
  - IOS-151 (178269104): extra words inserted.
  - Known Issue IOS-152 (173448573): Voice Editing commands ("Change X to Y", "Delete X", "Undo/Redo") "might not work reliably". No workaround.
  - Source: [27.0 RN, Dictation](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-27-release-notes)
- Siri voice and speech:
  - IOS-261 (177733317): Announce Notifications "yes" by voice or head gesture prompted unlock instead of reading the full message.
  - IOS-262 (177742977): new voices 6/7 fell back to legacy voices in Low Power Mode or when overheated.
  - IOS-266 (177969955): Pace/Expressiveness could not be changed.
  - Known IOS-290 (181266301): Siri might cut off word endings during navigation. Workaround: reduce voice expressivity from the fastest pace, or turn off expressive voices.
  - Known IOS-284 (176812955): no voice commands to refer to specific photos ("photo one"). Workaround: tap or use the picker.
  - Known IOS-283 (171728298): "Send these" may apply to all search results rather than the selected ones.
  - Known IOS-288 (178049066): "read my last message" may read an unknown-sender message.
  - Known IOS-286 (177376984): the spoken or displayed count of photos added may be wrong.
  - Known IOS-285 (177116121): Maps snippets incomplete or misformatted.
  - Source: [27.0 RN, Siri](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-27-release-notes)

#### H. Gestures and drag (Tier-1)
- IOS-360: UIKit (168884200). On iOS/iPadOS 27.0, Siri can load resources through `UIDragInteractionDelegate` without a user drag gesture, for example when Apple Intelligence is invoked from a context menu. Avoid animations or modal UI in `dragInteraction(_:sessionWillBegin:)`; use `sessionDidMove` instead. — [27.0 RN, UIKit, 168884200](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-27-release-notes)
- **Haptics:** no entry in any of the three release notes mentions haptics. Searching the 27.0, 27.2, and 27.3 Markdown for "haptic" returns nothing. — [27.0 RN](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-27-release-notes)

#### I. Media, Now Playing, audio (Tier-1)
- IOS-216: Now Playing Known Issue (186036238). `RemoteMediaSession`/`RemoteMediaSessionRepresentable` always provision production APNs push tokens. Workaround: use production for testing. IOS-217 (183641494): a new `RemoteMediaSession` created in the foreground was not visible in Control Center. IOS-101 AirPlay (176462871): AirPlay to Home Theaters failed when a PIN or password was required. IOS-124 (178189709): CarPlay stereo audio was silent after Spatial Audio. IOS-115 AudioAccessoryKit (178275661): third-party headphone info for fixed spatial audio, developer testing only for now, with EU customer availability "in a future iOS 27 and iPadOS 27 release". — [27.0 RN](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-27-release-notes)
- **Captions:** no developer release-note entry mentions captions or subtitles. Caption features appear only in the Support pages (Key question 2).

#### J. Other visual-legibility and UI defects of adjacent interest (Tier-1)
- IOS-129 (170774279): "Add a Control" button small and clipped. IOS-159 (177964121): Fitness+ duplicate title text in landscape on larger iPhones. IOS-190 (178174745): Lock Screen grabber in the wrong location or orientation. IOS-126 (177728602): a ringing alarm could not be stopped from the Lock Screen without unlocking. IOS-313 (174168981): Swift Charts conditionals in `Chart` warned or crashed below a 27.0 deployment target. IPAD-101 (169236746): the Photos single-photo viewer was blank from Siri search on iPadOS. IPAD-103 (180751246): Siri orb and "Hey Siri" on older iPads with Camera open. IPAD-102 (178280800): iPad Safari tab-organize tip. — [27.0 RN](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-27-release-notes)

#### K. Notable non-accessibility deprecations and behavior changes (Tier-1, for completeness)
- IOS-374 UIKit (179874781): `canOpenURL:` is deprecated.
- IOS-218 (170066290): On Demand Resources / `NSBundleResourceRequest` deprecated; use Background Assets.
- IOS-351 (178776840): `FileDocument` deprecated. IOS-329 (177458781): `Document` protocol; `ReferenceFileDocument` and `FileDocument` are described as deprecated.
- IOS-318 (105893279): `@State` is now macro-based, back-deploys to iOS 17-aligned OSes, with several source-compatibility exceptions.
- IOS-213 (176055825): stricter TLS for MDM, DDM, ADE, profile install, app install, and software update processes; TLS 1.2 minimum.
- IOS-131 (174796039) and Core AI 179282606: background Neural Engine access is restricted and needs a new entitlement.
- IOS-160 (75545872): `volumeAvailableCapacityKey` truncated to 3 significant digits.
- IOS-103 (158364073): AirPort Utility is no longer available for new downloads.
- 27.3 beta: Live Caller ID Lookup and NEURLFilter PIR shard counts must be powers of two (191651833, 191651462). NEURLFilter drops user tiers (191651440). NEURLFilter URLs must be declared in Info.plist `NSPIRConfiguration` (191651632).
- Sources: [27.0 RN](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-27-release-notes); [27.3 Beta RN](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-27_3-release-notes)

#### L. Full atomic inventory (all 322 entries, Tier-1, Apple Developer release notes)
URL for each row by release column:
- 27.0: https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-27-release-notes
- 27.2: https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-27_2-release-notes
- 27.3 beta: https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-27_3-release-notes

Locator = section + issue number. Evidence tier = Tier-1 for every row. The A11y/adjacent column is blank for unflagged rows.

| Claim ID | Release | Section | Status | Issue (FB) | SDK-linked | iPad-specific | A11y / adjacent flag | Apple text (≤22 words) | Workaround (≤18 words) |
|---|---|---|---|---|---|---|---|---|---|
| IOS-101 | 27.0 | AirPlay | Resolved | 176462871 |  |  | AirPlay media | "Fixed: AirPlay to Home Theaters fails when a PIN or password is required." |  |
| IOS-102 | 27.0 | AirPods Max 2 | Resolved | 178280323 |  |  |  | "Fixed: You cannot update AirPods Max 2 firmware beta in iOS 27 Beta 1 and macOS 27 Beta 1. AirPods Max 2 …" |  |
| IOS-103 | 27.0 | AirPort Utility | Deprecation | 158364073 |  |  |  | "AirPort Utility will no longer be available for new downloads from the App Store. If you previously downloaded the app, you can …" |  |
| IOS-104 | 27.0 | App Intents | New Feature | 173431080 |  |  |  | "You can now pass a name parameter of type `AttributedString` to the `notes.createNote` and `notes.updateNote` schemas." |  |
| IOS-105 | 27.0 | App Intents | Resolved | 175031314 |  |  |  | "Fixed: Non-SF Symbol custom images for app entities might not always appear in Siri." |  |
| IOS-106 | 27.0 | App Intents | Resolved | 175534195 |  |  |  | "Fixed: Default values from schemas might not be applied for parameters that are of “Set” type." |  |
| IOS-107 | 27.0 | App Intents | Resolved | 177996973 |  |  |  | "Fixed: Entities you register using `RelevantEntities` for the workout audio context might not appear as suggestions in Fitness media picker." |  |
| IOS-108 | 27.0 | App Intents | Resolved | 181212609 (FB23526663) |  |  |  | "Fixed: Requests that should result in an app’s `reminders.updateReminder`-conforming intent to be called might fail with “<App> cannot be used for this …" |  |
| IOS-109 | 27.0 | App Intents | Resolved | 181763422 |  |  |  | "Fixed: AppEntity instances have a cumulative size limit of 10MB, including all child properties and their values. Your app might crash if …" |  |
| IOS-110 | 27.0 | App Intents | Resolved | 182532125 |  |  |  | "Fixed: The notes.appendText schema erroneously disappeared from the SDK." |  |
| IOS-111 | 27.0 | App Intents | Known Issue | 181800016 (FB23652582) | Yes |  |  | "Existing entities that conformed to @AppEntity(schema: .photos.asset) in prior releases might no longer compile in the 27 SDKs because new properties were …" | To continue conforming to the schema, adopt the additional properties and move the code behind an availability check. |
| IOS-112 | 27.0 | App Intents | Deprecation | 176751155 |  |  |  | "The `calendar.deleteEvents` schema has been renamed to `calendar.deleteEvent`." |  |
| IOS-113 | 27.0 | Apple Intelligence Report | Resolved | 176056930 |  |  |  | "Fixed: When you view Apple Intelligence Report entries for Home Intelligence, some data that was sent to Private Cloud Compute won’t appear …" |  |
| IOS-114 | 27.0 | Apple Wallet | Resolved | 182055786 |  |  |  | "Fixed: Updating to iOS 27.0 Beta 3 or 4 might cause Digital ID to expire and become unavailable for presentation affecting any …" |  |
| IOS-115 | 27.0 | AudioAccessoryKit | New Feature | 178275661 |  |  | audio accessory | "AudioAccessoryKit now allows third-party audio accessory manufacturers to provide headphone information to the system to support fixed spatial audio. It is only …" |  |
| IOS-116 | 27.0 | Background Assets | New Feature | 163944365 |  |  |  | "You can reduce your app’s storage usage with localized asset packs. The system delivers the appropriately localized asset packs based on the …" |  |
| IOS-117 | 27.0 | Battery / Power Management | Resolved | 177346712 |  |  |  | "Fixed: Devices with a deeply discharged battery might fail to boot into the OS and remain stuck on the red dead battery …" |  |
| IOS-118 | 27.0 | Camera | Resolved | 177335723 |  |  |  | "Fixed: In the Camera app, Portrait mode blur effect might render incorrectly for photos." |  |
| IOS-119 | 27.0 | CarPlay | Resolved | 177508893 |  |  | CarPlay focus | "Fixed: `CPNavigationSession` ETA Tray panel items might not receive focus." |  |
| IOS-120 | 27.0 | CarPlay | Resolved | 177590525 |  |  | CarPlay panels | "Fixed: The panel delegate method `panelDidHide(_ panel: CPMapPanel)` might not be called." |  |
| IOS-121 | 27.0 | CarPlay | Resolved | 177592347 |  |  | CarPlay panels | "Fixed: Under certain configurations, `CPMapPanel` might not dismiss when you tap the close button." |  |
| IOS-122 | 27.0 | CarPlay | Resolved | 177595560 |  |  | CarPlay buttons | "Fixed: The symbol button handler of `CPMapPanelButtonConfiguration` might not be called." |  |
| IOS-123 | 27.0 | CarPlay | Resolved | 177832695 |  |  | CarPlay input | "Fixed: Your vehicle’s next and previous track steering wheel buttons might not function correctly in CarPlay." |  |
| IOS-124 | 27.0 | CarPlay | Resolved | 178189709 |  |  | CarPlay audio | "Fixed: In CarPlay, playback of stereo music content might be silent after playback of Spatial Audio content." |  |
| IOS-125 | 27.0 | CarPlay | Known Issue | 178952858 |  |  |  | "Siri might respond more slowly than expected in CarPlay, particularly under higher device temperatures or poor network conditions." | Try the request again after the device has cooled down or once you are in an area with … |
| IOS-126 | 27.0 | Clock | Resolved | 177728602 |  |  | alarm control | "Fixed: You might be unable to stop a ringing alarm from the lock screen without unlocking your device." |  |
| IOS-127 | 27.0 | CloudKit | Resolved | 177621316 |  |  |  | "Fixed: Saving a `CKShare` in which an administrator participant has changed their own role to `CKShareParticipantRole.privateUser` (self-demotion) has no effect." |  |
| IOS-128 | 27.0 | Communication Safety | Resolved | 183962032 |  |  |  | "Fixed: Sensitive QRCode detected as non-sensitive, preventing 3rd party developers from testing API functionality." |  |
| IOS-129 | 27.0 | Control Center | Resolved | 170774279 |  |  | control clipping | "Fixed: The “Add a Control” button in edit mode might appear small and clipped." |  |
| IOS-130 | 27.0 | Control Center | Known Issue | 184729556 |  |  |  | "Gathering `PowerProfiler` and `Lookback` traces through the `Performance Trace` Control Center widget might fail to produce traces." | Gather traces on iOS 27.0 beta 1 or earlier. |
| IOS-131 | 27.0 | Core AI | New Feature + Behavior change | 174796039 |  |  |  | "iOS 27 includes Neural Engine improvements for Apple Intelligence capable devices. The system now restricts background access to the Neural Engine, similar …" |  |
| IOS-132 | 27.0 | Core AI | New Feature | 179282606 |  |  |  | "Access to the Neural engine when your app is in the background requires the new entitlement: “com.apple.developer.background-tasks.continued-processing.inference”." |  |
| IOS-133 | 27.0 | Core AI | Resolved | 169746264 |  |  |  | "Fixed: `AIModelCache` entries might not honor the cache policy you provide, causing re-specialization to occur more often than expected." |  |
| IOS-134 | 27.0 | Core AI | Resolved | 175789258 |  |  |  | "Fixed: When inference runs on the GPU, `InferenceFunction.encode` blocks until all compute is complete instead of returning as soon as encoding is …" |  |
| IOS-135 | 27.0 | Core AI | Resolved | 176210080 |  |  |  | "Fixed: Certain weight and activation configurations may not run on the Neural Engine, such as FP8-quantized weights and activations, palettized weights with …" |  |
| IOS-136 | 27.0 | Core AI | Resolved | 176807213 |  |  |  | "Fixed: When you run `InferenceFunction.run` on functions with both state arguments and outputs with dynamic shapes, the framework might be unable to …" |  |
| IOS-137 | 27.0 | Core AI | Resolved | 177008303 |  |  |  | "Fixed: On-device specialization fails when loading an `.aimodel` converted with `coreai-torch` v0.4.0." |  |
| IOS-138 | 27.0 | Core AI | Resolved | 177354777 |  |  |  | "Fixed: Inference might fail or crash for models with control flow over dynamic-shape tensors (for example, linear-attention LLMs such as Qwen3.5/3.6)." |  |
| IOS-139 | 27.0 | Core AI | Resolved | 177729331 |  |  |  | "Fixed: Ahead-of-time (AOT) compilation might fail unexpectedly for certain models." |  |
| IOS-140 | 27.0 | Core AI | Resolved | 177991751 |  |  |  | "Fixed: When Metal API Validation is enabled, CoreAI models might fail to execute." |  |
| IOS-141 | 27.0 | Core AI | Resolved | 178056451 |  |  |  | "Fixed: Models with custom Metal kernels will fail to load." |  |
| IOS-142 | 27.0 | Core AI | Resolved | 179732320 |  |  |  | "Fixed: App-group support might not work as expected on certain model types." |  |
| IOS-143 | 27.0 | Core AI | Resolved | 181264112 |  |  |  | "Fixed: On-device specialization might fail when loading an `.aimodelc` compiled ahead of time using Xcode 27 Beta 2 or earlier." |  |
| IOS-144 | 27.0 | Core Bluetooth | Resolved | 178333845 |  |  |  | "Fixed: The Channel Sounding API in Core Bluetooth is not returning ranging results." |  |
| IOS-145 | 27.0 | Core Spotlight | Known Issue | 183770678 |  |  |  | "Creating a SpotlightSearchTool without a configuration and using it with a LanguageModelSession backed by the on-device system language model fails with an …" | Configure the tool with a focused guide, which uses a compact schema sized for the on-device model: ``` … |
| IOS-146 | 27.0 | Developer Settings | Resolved | 178063365 |  |  |  | "Fixed: Deep links into Settings > Developer > Paired Macs might silently fail to navigate to the target Mac computer. The Paired …" |  |
| IOS-147 | 27.0 | Dictation | New Feature | 178444388 |  |  | dictation input | "Dictation can now be powered by a new on-device model that boosts accuracy. To enable this, go to Keyboard settings > Dictation …" |  |
| IOS-148 | 27.0 | Dictation | Resolved | 177959708 |  |  | dictation input | "Fixed: The “New Line” and “All Caps” formatting commands might not work reliably in the dictation UI." |  |
| IOS-149 | 27.0 | Dictation | Resolved | 178078177 |  |  | dictation input | "Fixed: When you explicitly dictate punctuation— such as “Period” or “Colon” — both the spoken command word and the punctuation character might …" |  |
| IOS-150 | 27.0 | Dictation | Resolved | 178079519 |  |  | dictation input | "Fixed: Dictation might not recognize names from your contacts." |  |
| IOS-151 | 27.0 | Dictation | Resolved | 178269104 |  |  | dictation input | "Fixed: Dictation might insert extra words at the end of a dictated passage that you did not speak." |  |
| IOS-152 | 27.0 | Dictation | Known Issue | 173448573 |  |  | voice editing input | "Voice Editing commands such as “Change X to Y”, “Delete X”, and “Undo/Redo” might not work reliably." |  |
| IOS-153 | 27.0 | Family Settings | Resolved | 178546389 |  |  |  | "Fixed: Family member’s Ask To Buy, Apple Cash, Purchases, Subscription rows cannot be accessed." |  |
| IOS-154 | 27.0 | Files | Resolved | 179787658 |  |  |  | "Fixed: Deleting files from Recently Deleted might fail with an error or experience significant delays." |  |
| IOS-155 | 27.0 | Files | Resolved | 181179631 |  |  |  | "Fixed: Users might be unable to delete or open a file whose name contains certain Unicode characters if the name was created …" |  |
| IOS-156 | 27.0 | Finder | Resolved | 178093786 |  |  |  | "Fixed: Suggested names for a file or folder might be more generic than its contents. For example, a folder containing only bird …" |  |
| IOS-157 | 27.0 | FindMy | Resolved | 178384345 |  |  |  | "Fixed: Siri might not be able to find some of the people sharing location with you in FindMy." |  |
| IOS-158 | 27.0 | First-Party App Search | Resolved | 178186226 |  |  |  | "Fixed: Search assets might download slowly for languages and regions other than English and the United States, causing degraded search experiences for …" |  |
| IOS-159 | 27.0 | Fitness+ | Resolved | 177964121 |  |  | duplicate UI text (landscape) | "Fixed: On larger iPhones in landscape orientation, the Workout Detail view may display duplicate title text and action buttons when browsing workouts …" |  |
| IOS-160 | 27.0 | Foundation | New Feature + Behavior change | 75545872 |  |  |  | "`volumeAvailableCapacityKey` is truncated to 3 significant decimal digits at the block count level (e.g., 123,456,789 blocks becomes 123,000,000 blocks)." |  |
| IOS-161 | 27.0 | Foundation | Resolved | 161588649 (FB20439045) |  |  |  | "Fixed: `+[NSURL URLWithString:]` no longer double-encodes the `%` of valid percent-escape sequences when encoding other invalid characters." |  |
| IOS-162 | 27.0 | Foundation Models | Resolved | 177684296 |  |  |  | "Fixed: Private Cloud Compute might not work when you use simulators." |  |
| IOS-163 | 27.0 | Foundation Models | Resolved | 177748926 |  |  |  | "Fixed: When using the on-device Apple Foundation Model for both tool calling and guided generation, some prompts might cause the model to …" |  |
| IOS-164 | 27.0 | Foundation Models | Resolved | 177899620 |  |  |  | "Fixed: `@Generable` on an `enum` produces a deprecation warning about `GenerationError` that cannot be silenced." |  |
| IOS-165 | 27.0 | Foundation Models | Resolved | 177901494 |  |  |  | "Fixed: Truncating transcript history in the `onPrompt` modifier might cause an unexpected runtime error." |  |
| IOS-166 | 27.0 | Foundation Models | Resolved | 177902488 |  |  |  | "Fixed: `onPrompt` might not be called when applied to a `Profile` without instructions." |  |
| IOS-167 | 27.0 | Foundation Models | Resolved | 178181782 |  |  |  | "Fixed: `PrivateCloudComputeLanguageModel` always uses greedy decoding." |  |
| IOS-168 | 27.0 | Game Center | Resolved | 172683368 |  |  |  | "Fixed: When you trigger the Access Point, its completion handler is never invoked." |  |
| IOS-169 | 27.0 | Game Controller | New Feature | 168071382 |  |  | adaptive game controller input | "The PlayStation® Access™ controller is now supported on macOS, iPadOS, and iOS. You can create custom input profiles in game controller settings …" |  |
| IOS-170 | 27.0 | Gaussian Splats | Resolved | 183538823 |  |  |  | "Fixed: When 3DGS content rendered by a GaussianSplatComponent is moved offscreen and then returns to the visible area, some splats might be …" |  |
| IOS-171 | 27.0 | Hardware Security | New Feature | 152103975 |  |  |  | "arm64e.x1 introduces additional hardware security and performance instructions, including CPA2 for stronger MIE protection. Devices with support for arm64e.x1 include iPhone models …" |  |
| IOS-172 | 27.0 | HealthKit | New Feature | 135746152 |  |  |  | "HealthKit now supports heart rate and cycling power zones." |  |
| IOS-173 | 27.0 | HealthKit | New Feature | 172310874 |  |  |  | "Updated HealthKit permissions flow now lets users grant apps access to limited history or full history." |  |
| IOS-174 | 27.0 | HealthKit | New Feature | 178532053 |  |  |  | "HealthKit adds support for tracking menopausal state and bleeding after menopause; two new sample types are available. `HKCategoryTypeIdentifierMenopausalState` records a person’s current …" |  |
| IOS-175 | 27.0 | HealthKit | Resolved | 171273931 (FB22066297) |  |  |  | "Fixed: null unit might incorrectly convert to count and percent units." |  |
| IOS-176 | 27.0 | Hearing Test | Resolved | 176360906 |  |  | visual feedback (Hearing Test) | "Fixed: During a Hearing Test, visual feedback might not appear when you tap the screen to indicate a tone was heard." |  |
| IOS-177 | 27.0 | Home Screen | Resolved | 178435221 |  |  |  | "Fixed: Switching between many different posters with different icon tints may cause system sluggishness." |  |
| IOS-178 | 27.0 | Home Screen | Resolved | 178576719 |  |  |  | "Fixed: The Home Screen Customization on a newly setup device might not save." |  |
| IOS-179 | 27.0 | HomeKit | New Feature | 178858470 |  |  |  | "When Apple Intelligence in the Home app is enabled, your HomeKit Secure Video recordings are processed on-device and through Private Cloud Compute …" |  |
| IOS-180 | 27.0 | HomeKit | New Feature | 181282161 |  |  |  | "Apple Intelligence for Home requires an iCloud+ subscription starting at 2TB." |  |
| IOS-181 | 27.0 | Image Playground | Resolved | 175357842 |  |  | VoiceOver | "Fixed: When VoiceOver is enabled and the gallery contains only one image, the prompt input UI might not appear." |  |
| IOS-182 | 27.0 | Image Playground | Resolved | 177710762 |  |  |  | "Fixed: When Image Wand encounters an error — such as an unsupported flow or unsafe output — you might see the misleading …" |  |
| IOS-183 | 27.0 | Image Playground | Resolved | 177833994 |  |  |  | "Fixed: If required models are downloading, you might see an error message instead of download progress information." |  |
| IOS-184 | 27.0 | Image Playground | Resolved | 178256174 |  |  |  | "Fixed: In the Image Playground photo picker, the All and Suggested tabs are missing, which might limit the number of photos available …" |  |
| IOS-185 | 27.0 | iPhone Mirroring | Resolved | 180961142 |  |  | mirroring windows | "Fixed: In rare cases, iPhone Mirroring may not resize correctly even after pressing the home button in the mirroring app." |  |
| IOS-186 | 27.0 | iPhone Mirroring | Resolved | 181023494 |  |  | mirroring windows | "Fixed: Restarting an app while iPhone Mirroring is active can result in the screen appearing to freeze and resizing being disabled." |  |
| IOS-187 | 27.0 | iPhone Mirroring | Resolved | 181057810 |  |  | mirroring windows | "Fixed: iPhone Mini does not resize properly during iPhone Mirroring." |  |
| IOS-188 | 27.0 | Keyboard | Resolved | 180881635 |  |  | keyboard | "Fixed: Unlocalized text can appear for paste candidates." |  |
| IOS-189 | 27.0 | LDCM | Resolved | 175484509 |  |  |  | "Fixed: When your device’s charging port is wet but empty, you might see a dialog instructing you to unplug a charger or …" |  |
| IOS-190 | 27.0 | Lock Screen | Resolved | 178174745 |  |  | Lock Screen orientation | "Fixed: After dismissing Lock Screen, the Lock Screen grabber might appear in the incorrect location or orientation." |  |
| IOS-191 | 27.0 | Lock Screen | Resolved | 178283603 |  |  |  | "Fixed: Siri and Search may still be available when locked even if they are disabled under “Allow Access When Locked” in Settings." |  |
| IOS-192 | 27.0 | Lock Screen | Resolved | 181621150 |  |  |  | "Fixed: Portions of Depth Effect–enabled wallpapers might appear earlier than expected while pulling down Notification Center." |  |
| IOS-193 | 27.0 | Lock Screen | Known Issue | 178200601 |  |  |  | "Starting a Vision Pro Guest Mode session might result in two Live Activities on screen at the same time." | Dismiss the Lock Screen and re-lock the device. |
| IOS-194 | 27.0 | Mail | Resolved | 169101671 |  |  |  | "Fixed: Emails might display content that doesn’t match their subject line." |  |
| IOS-195 | 27.0 | Mail Banners | Resolved | 173869986 |  |  |  | "Fixed: Mail banners for early flights will show the flight status as delayed." |  |
| IOS-196 | 27.0 | Media Sharing Extensions | New Feature | 168722808 |  |  |  | "New frameworks allow you to add media sharing protocols through extension at the system level and enable media apps to use these …" |  |
| IOS-197 | 27.0 | Media Sharing Extensions | Resolved | 178179521 |  |  |  | "Fixed: Due to a mismatch in runtime checks with the mandatory entitlement for `MediaSharingExtensions`, extensions using the new `MediaDeviceExtension` framework can build …" |  |
| IOS-198 | 27.0 | Messages | Resolved | 177453147 |  |  |  | "Fixed: Stickers attached to a message from an unknown sender do not appear." |  |
| IOS-199 | 27.0 | Messages | Resolved | 177657977 |  |  |  | "Fixed: GIFs and pasted images might render as the incorrect size." |  |
| IOS-200 | 27.0 | Messages | Resolved | 180859837 |  |  |  | "Fixed: HDR screenshots might appear garbled when sent in Messages." |  |
| IOS-201 | 27.0 | Metal | Resolved | 172520325 |  |  |  | "Fixed: When you use a sampler to read from a texture with clamp-to-edge addressing mode, the result might be clamped to zero." |  |
| IOS-202 | 27.0 | Metal | Resolved | 177318505 |  |  |  | "Fixed: On devices in the Apple 10 GPU family, using a sampler to read from a texture with clamp-to-edge addressing mode might …" |  |
| IOS-203 | 27.0 | MetricKit | New Feature | 96078210 (FB10494149) |  |  |  | "`CrashDiagnostic` now includes a `terminationCategory` that maps to the corresponding case in `ForegroundTerminationMetric` and `BackgroundTerminationMetric`." |  |
| IOS-204 | 27.0 | MetricKit | New Feature | 159889985 |  |  |  | "Apps that emit developer-defined states through the `StateReporting` framework now receive metrics and diagnostics in the context of those states." |  |
| IOS-205 | 27.0 | MetricKit | New Feature | 159890067 |  |  |  | "`MemoryExceptionDiagnostic` are available when your app or app extension is terminated for exceeding its memory limit." |  |
| IOS-206 | 27.0 | MetricKit | New Feature | 159890165 |  |  |  | "A new application-level `MetalFrameRateMetric` is available for Metal frame pacing rendering insights per `CAMetalLayer`." |  |
| IOS-207 | 27.0 | MetricKit | New Feature | 164439529 |  |  |  | "A new Swift-first `MetricManager` API enables your app to receive `MetricReport` and `DiagnosticReport` objects through `AsyncStream`. `MetricReport` contains a daily aggregated entry …" |  |
| IOS-208 | 27.0 | MetricKit | New Feature | 170513251 |  |  |  | "`LocationActivityTimeMetric` now includes a `reducedAccuracy` property that reports the time your app spent tracking location using reduced accuracy (`kCLLocationAccuracyReduced`). Xcode’s simulated metric …" |  |
| IOS-209 | 27.0 | MetricKit | New Feature | 180024784 (FB23242495) | Yes |  |  | "`HitchTimeMetric.ratio` and `SignpostIntervalMetric.hitchTimeRatio` now use the new `HitchTimeRatio` type, a `Dimension` subclass that expresses hitch time as a ratio of milliseconds hitching …" |  |
| IOS-210 | 27.0 | MetricKit | Deprecation | 174892111 |  |  |  | "The original MetricKit APIs — including `MXMetricManager`, `MXMetricManagerSubscriber`, `MXMetricPayload`, and `MXDiagnosticPayload` — are no longer recommended for new adoption. Use `MetricManager` instead." |  |
| IOS-211 | 27.0 | MetricKit | Deprecation | 180455992 | Yes |  |  | "The `scrollHitchTime(_:)` case of `MetricResult` and the `ScrollHitchTimeMetric` type are no longer part of the new Swift MetricKit API, and `MetricReport` values …" |  |
| IOS-212 | 27.0 | Nearby Interaction | Resolved | 178073051 |  |  |  | "Fixed: The Channel Sounding API in Nearby Interaction does not return ranging results." |  |
| IOS-213 | 27.0 | Network Security | New Feature + Behavior change | 176055825 |  |  |  | "Starting in 27.0 operating systems, select system processes now enforce stricter network security (TLS) requirements. These new requirements might cause connections to …" |  |
| IOS-214 | 27.0 | NetworkExtension | Resolved | 176839377 |  |  |  | "Fixed: When an active VPN configuration sets `includeAllNetworks` to true, `excludeLocalNetworks` fails to exclude wired connections to CarPlay." |  |
| IOS-215 | 27.0 | Notifications | Resolved | 179179362 |  |  |  | "Fixed: Critical alerts are automatically turned on for any apps that request your permission to enable notifications." |  |
| IOS-216 | 27.0 | Now Playing | Known Issue | 186036238 |  |  | Now Playing media | "`RemoteMediaSession` and `RemoteMediaSessionRepresentable` always provision Now Playing start and update push tokens for the `production` APNs environment, even if the `aps-environment` configuration …" | Use the `production` environment for testing and validation. |
| IOS-217 | 27.0 | NowPlaying | Resolved | 183641494 |  |  | Now Playing media | "Fixed: Newly created RemoteMediaSession won’t be visible in control center if created while the app is open in the foreground." |  |
| IOS-218 | 27.0 | On Demand Resources | Deprecation | 170066290 |  |  |  | "On Demand Resources and the `NSBundleResourceRequest` API are deprecated. Use Background Assets instead." |  |
| IOS-219 | 27.0 | PencilKit | Deprecation | 176410709 |  |  |  | "`__PKStrokeRenderState` has been renamed to `PKStrokeRenderStateReference`, with `PKStrokeRenderStateReference.init(…)` replacing `PKStrokeRenderState.asObjCRenderState()`." |  |
| IOS-220 | 27.0 | PhotoKit | Resolved | 175050631 |  |  |  | "Fixed: The `addedDate` property on `PHAsset` might return `nil` even though it’s marked as non-nullable." |  |
| IOS-221 | 27.0 | PhotoKit | Deprecation | 175412725 (FB22589474) |  |  |  | "The `originalFilename` property on `PHAssetResource` is incorrectly marked as non-nullable, which misrepresents the property value; a new, nullable `filename` property is available …" |  |
| IPAD-101 | 27.0 | Photos | Resolved | 169236746 |  | Yes | iPad blank viewer | "Fixed: When opened from a grid of Photos search results in Siri on iPadOS, the single-photo viewer might appear blank." |  |
| IOS-222 | 27.0 | Photos | Resolved | 176384327 |  |  |  | "Fixed: You might see a slight shift in color hues after applying Spatial Reframing to photos." |  |
| IOS-223 | 27.0 | Photos | Resolved | 178093956 |  |  |  | "Fixed: When sharing a Live Photo from the Photos app, you might not be able to disable the Live Photo effect prior …" |  |
| IOS-224 | 27.0 | Photos | Resolved | 178164434 |  |  |  | "Fixed: Photos app might quit unexpectedly when you re-enter the Extend tool on a photo that has already been extended." |  |
| IOS-225 | 27.0 | Photos Edit | Resolved | 178183850 |  |  |  | "Fixed: A thin white line might be visible in photos that have had Spatial Reframing applied." |  |
| IOS-226 | 27.0 | Podcasts | Resolved | 175524004 |  |  |  | "Fixed: On first launch after updating, you might experience longer-than-expected library migration times, which might last several minutes." |  |
| IOS-227 | 27.0 | RealityKit | New Feature | 178061856 |  |  |  | "The Gaussian Splat Component API in RealityKit will be available in an upcoming release." |  |
| IOS-228 | 27.0 | RealityKit | Resolved | 172875414 |  |  |  | "Fixed: Some MaterialX 1.39 nodes are not supported." |  |
| IOS-229 | 27.0 | RealityKit | Resolved | 177674901 |  |  |  | "Fixed: `ComputeGraphComponents` stored in a Reality file do not render when loaded." |  |
| IOS-230 | 27.0 | RealityKit | Resolved | 177976245 |  |  |  | "Fixed: When `OpacityComponent` is applied to an entity with opaque materials, `RealityRenderer` renders the opaque materials with transparency, revealing interior surfaces. Only …" |  |
| IOS-231 | 27.0 | Related Receipts | Known Issue | 178202101 |  |  |  | "The disclaimer “Siri found in Mail or Photos. Not shared with card issuer” does not appear below displayed transaction related receipts in …" |  |
| IOS-232 | 27.0 | Reminders | Known Issue | 180040003 |  |  |  | "After you tap “Add to Reminders” in Messages, the “New Reminder” interface presents the reminder with an empty title field." | Tap “Add to Reminders” in the “New Reminder” interface to create the reminder, then edit the title in … |
| IOS-233 | 27.0 | Safari | Resolved | 177812052 |  |  |  | "Fixed: The Safari tab bar might enter a state where it does not appear on screen." |  |
| IOS-234 | 27.0 | Safari | Resolved | 178099724 |  |  |  | "Fixed: Safari Intelligence features might appear as available before assets are fully downloaded. If you use the feature before assets are available, …" |  |
| IPAD-102 | 27.0 | Safari | Resolved | 178280800 |  | Yes | iPad Safari tip | "Fixed: On iPad, the tip prompting users to automatically organize their tabs might not appear in Safari." |  |
| IOS-235 | 27.0 | Safari Extensions | Resolved | 179293939 |  |  |  | "Fixed: Turning on or off Safari extensions created via the “Describe an Extension” feature might not take effect until Safari is relaunched." |  |
| IOS-236 | 27.0 | Screen Time | Resolved | 175437403 |  |  |  | "Fixed: Screen Time restrictions might not apply to child accounts despite being configured." |  |
| IOS-237 | 27.0 | Security | Resolved | 183456836 |  |  |  | "Fixed: Obtaining new certificates via ACME fails. New MDM enrollments using Managed Device Attestation fail." |  |
| IOS-238 | 27.0 | SensorKit | Resolved | 178275291 |  |  |  | "Fixed: PPG sensor reader might return no samples when attempting to fetch data." |  |
| IOS-239 | 27.0 | ShaderGraph | Resolved | 177976666 | Yes |  |  | "Fixed: The `realitykit_hair_surfaceshader` node does not support `DiffuseLightProbeGroupComponent`. Materials built with this node might not respond to diffuse light probe group lighting." |  |
| IOS-240 | 27.0 | Shortcuts | Resolved | 179514725 |  |  |  | "Fixed: Focus automations migrated from iOS 26 to iOS 27 do not work." |  |
| IOS-241 | 27.0 | Shortcuts | Resolved | 179846468 |  |  |  | "Fixed: Writing Tools actions are unavailable in Shortcuts." |  |
| IOS-242 | 27.0 | Shortcuts | Resolved | 181071784 |  |  |  | "Fixed: The Use Model action might fail to run when using the On-Device option for some output types." |  |
| IOS-243 | 27.0 | Shortcuts | Resolved | 182745894 |  |  |  | "Fixed: Shortcuts containing the Send Message action might fail to import or share." |  |
| IOS-244 | 27.0 | Shortcuts | Known Issue | 166068090 |  |  |  | "If an app intent uses Duration or `LPLinkMetadata`, creating a shortcut with that intent and then attempting to edit it with “Describe …" | If the model discards the action, press “Undo” to recover the unsupported intent. |
| IOS-245 | 27.0 | Shortcuts | Known Issue | 168315587 |  |  |  | "When an app intent defines a `UnionValue` parameter with two number-related types (for example, both Int and Double), the number option appears …" | Define only one number-related type in the `UnionValue` parameter (for example, use only Int or only Double, not … |
| IOS-246 | 27.0 | Siri | Resolved | 175230813 |  |  |  | "Fixed: Siri ignores custom values for navigation preferences, transport, and incident types in apps that use `maps.startNavigation` or `maps.reportIncident` intent schemas." |  |
| IOS-247 | 27.0 | Siri | Resolved | 175380461 |  |  |  | "Fixed: When location data is unavailable or only coarse-accuracy location data is available, Maps searches initiated through Siri might return empty or …" |  |
| IOS-248 | 27.0 | Siri | Resolved | 175884006 |  |  |  | "Fixed: When you turn off Siri, some photo-related questions might return web search results instead of prompting you to share the photo …" |  |
| IOS-249 | 27.0 | Siri | Resolved | 176400964 |  |  |  | "Fixed: When you ask Siri to work with reminder lists, you might need to use the exact list name. Siri might not …" |  |
| IOS-250 | 27.0 | Siri | Resolved | 176844035 |  |  |  | "Fixed: App Intents with `@UnionValue` types that accept a `PlaceDescriptorEntity` and a `String` always receive `String` values instead of `PlaceDescriptorEntity` entities." |  |
| IOS-251 | 27.0 | Siri | Resolved | 177190637 |  |  |  | "Fixed: Starting a call with Siri might fail with an error in apps that adopt CallKit and the `phone.startCall` AppSchema." |  |
| IOS-252 | 27.0 | Siri | Resolved | 177356158 |  |  |  | "Fixed: When you ask Siri to send a message to a contact that doesn’t exist on your device, Siri might draft a …" |  |
| IOS-253 | 27.0 | Siri | Resolved | 177416168 |  |  |  | "Fixed: You might not see names and images of email senders in the Siri email list UI." |  |
| IOS-254 | 27.0 | Siri | Resolved | 177464215 |  |  |  | "Fixed: Siri might not resolve some entity types when your app has provided only an `EntityStringQuery` for the entity type." |  |
| IOS-255 | 27.0 | Siri | Resolved | 177476889 |  |  |  | "Fixed: Siri functionality during software updates is limited, including calls to emergency services." |  |
| IOS-256 | 27.0 | Siri | Resolved | 177545828 |  |  |  | "Fixed: Asking Siri to call short phone numbers, such as “Call 17”, might fail." |  |
| IOS-257 | 27.0 | Siri | Resolved | 177593534 |  |  |  | "Fixed: Search results from third-party apps may not be tappable." |  |
| IOS-258 | 27.0 | Siri | Resolved | 177649865 |  |  |  | "Fixed: Disabling Siri might not delete your Siri and Dictation interaction history from your device." |  |
| IOS-259 | 27.0 | Siri | Resolved | 177679168 |  |  |  | "Fixed: Siri might not find app-specific contacts that are only indexed in Spotlight and do not appear in the Contacts app." |  |
| IOS-260 | 27.0 | Siri | Resolved | 177722240 |  |  |  | "Fixed: Siri cannot create a recurring reminder or update an existing reminder to be reoccurring." |  |
| IOS-261 | 27.0 | Siri | Resolved | 177733317 |  |  | Announce Notifications/head gesture | "Fixed: With AirPods connected to iPhone and Announce Notifications enabled, responding “yes” by voice or head gesture to a long incoming notification …" |  |
| IOS-262 | 27.0 | Siri | Resolved | 177742977 |  |  | speech voices | "Fixed: New American English Siri voices 6 and 7 might default to legacy US voices when your device is overheated or in …" |  |
| IOS-263 | 27.0 | Siri | Resolved | 177755742 |  |  |  | "Fixed: When you use ChatGPT with Apple Intelligence, some responses used in follow-up queries or when you resume a chat might be …" |  |
| IOS-264 | 27.0 | Siri | Resolved | 177762533 |  |  | Siri snippet/color | "Fixed: When you ask Siri to find, search, or read reminders, Siri might list or read the reminders instead of showing a …" |  |
| IOS-265 | 27.0 | Siri | Resolved | 177942110 |  |  |  | "Fixed: Mail older than 6 months might not be searchable by body content, but is still searchable by sender and subject." |  |
| IOS-266 | 27.0 | Siri | Resolved | 177969955 |  |  | speech pace | "Fixed: After enabling Expressive Voices, you are not able to modify Pace or Expressiveness in the Settings pane." |  |
| IOS-267 | 27.0 | Siri | Resolved | 177992979 |  |  |  | "Fixed: Siri might run the incorrect `OpenIntent` or `system.open` intent when multiple intents targeting different entity types are available in your app." |  |
| IOS-268 | 27.0 | Siri | Resolved | 177998395 |  |  |  | "Fixed: After creating a list through Siri, tapping the list icon might result in an error instead of opening the list in …" |  |
| IOS-269 | 27.0 | Siri | Resolved | 178025056 |  |  |  | "Fixed: When you tap the Send button in the Siri message confirmation flow, the message might fail to send." |  |
| IOS-270 | 27.0 | Siri | Resolved | 178163636 |  |  |  | "Fixed: When you ask Siri to open a URL from the Siri App, Safari might launch to a blank screen." |  |
| IOS-271 | 27.0 | Siri | Resolved | 178247289 |  |  |  | "Fixed: On CarPlay with Apple Intelligence and the ChatGPT extension enabled, asking ChatGPT a question through Siri might not produce a spoken …" |  |
| IOS-272 | 27.0 | Siri | Resolved | 178276448 |  |  |  | "Fixed: You might encounter build failures when attempting to implement a Transferable `IntentValueRepresentation` for `PHAsset`." |  |
| IOS-273 | 27.0 | Siri | Resolved | 178379209 |  |  |  | "Fixed: When asking Siri to call, message, or email a contact, Siri might fail to resolve the correct person — particularly when …" |  |
| IOS-274 | 27.0 | Siri | Resolved | 178381615 |  |  | contrast/readability (Dark Mode) | "Fixed: For Report a Concern flows started with Siri, the text in attachments might be difficult to read while in Dark Mode." |  |
| IOS-275 | 27.0 | Siri | Resolved | 178384054 |  |  |  | "Fixed: Businesses with overnight hours might display as “Closed till [next day]” even during open hours." |  |
| IOS-276 | 27.0 | Siri | Resolved | 178459481 |  |  |  | "Fixed: In CarPlay, when Apple Intelligence enabled, Siri requests for directions in Maps might fail to start navigation." |  |
| IOS-277 | 27.0 | Siri | Resolved | 178489724 |  |  |  | "Fixed: Siri might not respond to your voice correctly." |  |
| IOS-278 | 27.0 | Siri | Resolved | 178560562 |  |  |  | "Fixed: In the Siri app, conversations might be deleted a few minutes after receiving streaming responses." |  |
| IOS-279 | 27.0 | Siri | Resolved | 179195692 |  |  |  | "Fixed: When you say “Save Parking Location,” the parking location information displays with reduced detail compared to Beta 1." |  |
| IOS-280 | 27.0 | Siri | Resolved | 180333394 |  |  |  | "Fixed: On macOS, Siri AI cannot search within specific folders such as Desktop or Documents. File searches might return results from unintended …" |  |
| IPAD-103 | 27.0 | Siri | Resolved | 180751246 |  | Yes | iPad Siri | "Fixed: When the Camera app is open, the Siri “orb” waveform will not animate correctly on some older iPads and “Hey Siri” …" |  |
| IOS-281 | 27.0 | Siri | Resolved | 181041601 |  |  |  | "Fixed: Siri encounters an error when asked to compose emails if the Mail app is not open in the background." |  |
| IOS-282 | 27.0 | Siri | Resolved (no "Fixed:" prefix; behavior statement) + Behavior change | 182145010 |  |  |  | "As of beta 5, Siri AI conversation history no longer syncs to devices running a prior beta. iCloud sync works between devices …" |  |
| IOS-283 | 27.0 | Siri | Known Issue | 171728298 |  |  | voice commands/selection | "After Siri returns photo search results and you select photos, Siri might not detect which photos are selected on screen. Commands like …" | Open Photos, select the photos you want to act on, then perform the action using Siri — for … |
| IOS-284 | 27.0 | Siri | Known Issue | 176812955 |  |  | voice commands | "Siri doesn’t support voice commands to interact with specific photos. For example, you can’t refer to photos by number, such as “photo …" | Use the photo picker to select the photo you want, or tap to select photos directly. |
| IOS-285 | 27.0 | Siri | Known Issue | 177116121 |  |  | Siri snippet formatting | "When you ask Siri for Maps information, the response snippets might appear incomplete or display formatting issues." | Ask Siri to repeat the information, or open Maps directly for complete details. |
| IOS-286 | 27.0 | Siri | Known Issue | 177376984 |  |  | spoken response accuracy | "When you ask Siri to add photos to an album, the confirmation prompt and spoken response might report or display more photos …" | Add photos to the album manually in the Photos app: tap Select, tap the photos you want to … |
| IOS-287 | 27.0 | Siri | Known Issue | 177984074 |  |  |  | "Non-SF Symbol custom images for entities might not appear in Siri results for third-party apps." |  |
| IOS-288 | 27.0 | Siri | Known Issue | 178049066 |  |  | spoken message reading | "When you ask Siri to read your last message, Siri might read an unread message from an unknown sender, such as spam, …" | Name the sender in your request – for example, “Read my last message from <name>.” |
| IOS-289 | 27.0 | Siri | Known Issue | 178274714 |  |  |  | "Siri might respond more slowly than expected in CarPlay, particularly under higher device temperatures or poor network conditions." | Try the request again after the device has cooled down or once you are in an area with … |
| IOS-290 | 27.0 | Siri | Known Issue | 181266301 |  |  | speech output | "Siri might cut off the end of words during navigation." | Reduce voice expressivity from the fastest pace, or turn off expressive voices. |
| IOS-291 | 27.0 | Sleep Focus | Resolved | 179960164 |  |  |  | "Fixed: Sleep Focus may not automatically toggle on/off after a reboot or update until the user unlocks the device." |  |
| IOS-292 | 27.0 | StandBy | Resolved | 178061326 |  |  |  | "Fixed: StandBy Clocks may be missing." |  |
| IOS-293 | 27.0 | Status Bar | Resolved | 179470940 |  |  | status bar legibility | "Fixed: Status bar might appear blurred while apps are in the foreground." |  |
| IOS-294 | 27.0 | StoreKit | New Feature | 141012819 |  |  |  | "Offer code redemption APIs now return a `VerificationResult` when redemption completes. If a redemption succeeds, your app receives a `VerificationResult` that contains …" |  |
| IOS-295 | 27.0 | StoreKit | New Feature | 156749517 |  |  |  | "StoreKit now includes the `Transaction.OwnershipType.assigned` and `Transaction.RevocationType.assignmentRevoked` enum values to support volume purchases. `Transaction` query methods now additionally return transactions assigned to …" |  |
| IOS-296 | 27.0 | StoreKit | New Feature | 160501742 |  |  |  | "New `Product.ProductType` APIs represent subscription Bundles and subscription Suites. New APIs in `Product.SubscriptionInfo.BundledSubscription` let you fetch merchandising data about subscriptions contained in …" |  |
| IOS-297 | 27.0 | StoreKit | New Feature | 167808780 |  |  |  | "`partnerName` and `partnerId` properties for Advanced Commerce API are available in [`Transaction.AdvancedCommerceInfo`](https://developer.apple.com/documentation/storekit/transaction/advancedcommerceinfo-swift.struct) and [`RenewalInfo.AdvancedCommerceInfo`](https://developer.apple.com/documentation/storekit/product/subscriptioninfo/renewalinfo/advancedcommerceinfo-swift.struct)." |  |
| IOS-298 | 27.0 | StoreKit | Resolved | 180999342 (FB23487953) |  |  |  | "Fixed: The refund request, offer code redemption, and manage subscriptions sheets might fail to present in TestFlight." |  |
| IOS-299 | 27.0 | StoreKit | Resolved | 181766819 (FB23646993) |  |  |  | "Fixed: `Storefront` API might return incorrect metadata when running in the TestFlight environment." |  |
| IOS-300 | 27.0 | StoreKit | Resolved | 181842500 |  |  |  | "Fixed: Purchases of non-subscription In-App Purchases made using the SKTestSession.buyProduct() method might fail with an invalid product error. The billingPlanType(_:) PurchaseOption isn’t …" |  |
| IOS-301 | 27.0 | StoreKit | Resolved | 183165269 |  |  |  | "Fixed: Transactions fail to finish." |  |
| IOS-302 | 27.0 | StoreKit Testing in Xcode | Resolved | 102093015 (FB11767567) |  |  |  | "Fixed: The unified app receipt is not updated after forcing a subscription expiration with `SKTestSession`." |  |
| IOS-303 | 27.0 | StoreKit Testing in Xcode | Resolved | 154390284 (FB18403150) |  |  |  | "Fixed: The `SKTestSession` `disableDialogs` setting is not always respected for all system dialogs." |  |
| IOS-304 | 27.0 | StoreKit Testing in Xcode | Resolved | 160698598 (FB20269723) |  |  |  | "Fixed: Subscription upgrades performed with the Xcode Transaction Manager are not reported in `Transaction.updates`." |  |
| IOS-305 | 27.0 | StoreKit Testing in Xcode | Resolved | 162014134 (FB20537538) |  |  |  | "Fixed: The renewal behavior preference is not respected when using the `purchaseDate(_:renewalBehavior:)` purchase option to make purchases using `SKTestSession`." |  |
| IOS-306 | 27.0 | StoreKit Testing in Xcode | Resolved | 174560379 (FB22475017) |  |  |  | "Fixed: Re-purchasing a previously refunded non-consumable fails with an already owned error when using StoreKit Testing in Xcode." |  |
| IOS-307 | 27.0 | StoreKit Testing in Xcode | Resolved | 177942756 |  |  |  | "Fixed: Using `pricingTerms.commitmentInfo.price` in StoreKit Testing in Xcode returns an incorrect price for monthly subscriptions with a 12-month commitment." |  |
| IOS-308 | 27.0 | StoreKit Testing in Xcode | Resolved | 178441109 |  |  |  | "Fixed: Transactions for upgraded subscriptions are immediately marked as expired when using StoreKit Testing in Xcode." |  |
| IOS-309 | 27.0 | StoreKit Testing in Xcode | Resolved | 183933307 (FB24137836) |  |  |  | "Fixed: Intro offer eligibility does not reset immediately after calling `SKTestSession.clearTransactions()`." |  |
| IOS-310 | 27.0 | StoreKit Testing in Xcode | Known Issue | 184155259 |  |  |  | "Changing the storefront or locale using `SKTestSession` doesn’t propagate through `Storefront.updates`." |  |
| IOS-311 | 27.0 | StoreKit Testing in Xcode | Known Issue | 184255116 |  |  |  | "Failed purchases using `SKTestSession` might display error dialogs even when `dialogsDisabled` is set to true." |  |
| IOS-312 | 27.0 | Suggestions in Messages | Resolved | 178193147 |  |  |  | "Fixed: The app icon shown for navigation suggestions is always the Apple Maps icon. If the suggestion is selected, the user’s preferred …" |  |
| IOS-313 | 27.0 | Swift Charts | Resolved | 174168981 |  |  | charts | "Fixed: When your project has a minimum deployment target lower than 27.0, using conditionals inside a `Chart` closure produces the warning “Conformance …" |  |
| IOS-314 | 27.0 | SwiftData | Resolved | 178113288 |  |  |  | "Fixed: You might experience a deadlock for @Query when saving a ModelContext on a background actor while scheduling new async tasks for …" |  |
| IOS-315 | 27.0 | SwiftUI | New Feature | 55162154 (FB7234376) |  |  | status bar | "You can now use `.toolbarColorScheme(colorScheme, for: .statusBar)` to set a preferred status bar color scheme." |  |
| IOS-316 | 27.0 | SwiftUI | New Feature | 78212597 |  |  |  | "`AsyncImage` now automatically caches downloaded images using HTTP caching protocols, allowing servers to control caching behavior via standard headers. You can customize …" |  |
| IOS-317 | 27.0 | SwiftUI | New Feature + Behavior change | 79770704 (FB9208920) | Yes |  | text selection/gestures | "In apps built with the iOS 27.0 and iPadOS 27.0 SDKs, a `Text` view with `.textSelection(.enabled)` applied now supports user-interactive selection using …" |  |
| IOS-318 | 27.0 | SwiftUI | New Feature + Behavior change | 105893279 |  |  |  | "A `@State` declared with an expression as its initial value used to evaluate the expression each time the view struct re-instantiates. In …" |  |
| IOS-319 | 27.0 | SwiftUI | New Feature | 158160386 (FB19589465) | Yes |  | text rendering | "In apps built with the iOS 27.0 and macOS 27.0 SDKs, selectable `Text` views now support `TextRenderer`." |  |
| IOS-320 | 27.0 | SwiftUI | New Feature | 158441552 | Yes |  |  | "In apps built with the 27.0 SDKs, the new `ReadableDocument` and `WritableDocument` protocols support asynchronous reading and writing, progress reporting, and direct …" |  |
| IOS-321 | 27.0 | SwiftUI | New Feature + Behavior change | 164516837 | Yes |  | tab navigation | "In apps built with the iOS 27.0 and iPadOS 27.0 SDKs, a `TabView` enforces that its selection is set to a visible …" |  |
| IOS-322 | 27.0 | SwiftUI | New Feature | 165329279 |  |  | status bar | "You can use `.toolbarVisibility(hideStatusBar ? .hidden : .automatic, for: .statusBar)` to conditionally hide the status bar." |  |
| IPAD-104 | 27.0 | SwiftUI | New Feature + Behavior change | 170480710 |  | Yes | menu icons | "The menu bar on iPadOS 27.0 and macOS 27.0, as well as context menus on macOS 27.0, present a reduced set of …" |  |
| IOS-323 | 27.0 | SwiftUI | New Feature | 173211711 |  |  | VoiceOver (tabs trait); matches IOS-01 | "The `TabsPickerStyle` style is now available for pickers that represent tab-based navigation and content selection. This style is similar to the `.segmented` …" |  |
| IOS-324 | 27.0 | SwiftUI | New Feature | 173362083 |  |  | text input visuals | "You can now use the `TextInputBorderShape` type to customize the border shape of text input controls like `TextField` with the `textInputBorderShape(_:)` view …" |  |
| IOS-325 | 27.0 | SwiftUI | New Feature | 175548901 | Yes |  | external display scenes | "In apps built with the iOS 27.0 SDK, you can display non-interactive content on external display scenes using the `.sceneAccessory` view modifier …" |  |
| IOS-326 | 27.0 | SwiftUI | New Feature + Behavior change | 175594929 | Yes |  | menu subtitles | "In apps built with the 27.0 SDKs, a `LabeledContent` view used inside a `Menu` maps its value to the platform menu item’s …" |  |
| IOS-327 | 27.0 | SwiftUI | New Feature | 175902616 |  |  |  | "The @Entry macro now warns of potential issues if you store default class instances or closures in the environment. The SwiftUI Specialist …" |  |
| IOS-328 | 27.0 | SwiftUI | New Feature | 177185166 |  |  | layout geometry | "You can now access `concentricCornerRadii` and `concentricCornerRadii(in:)` on `GeometryProxy`. These APIs return the corner radii that are concentric with the view’s container …" |  |
| IOS-329 | 27.0 | SwiftUI | New Feature | 177458781 |  |  |  | "You can now use the `Document` protocol for representing documents in `DocumentGroup`. This protocol combines `ReadableDocument` and `WritableDocument` for common read-and-write cases. …" |  |
| IOS-330 | 27.0 | SwiftUI | New Feature | 177526032 |  |  |  | "`@ContentBuilder` type checking performance is further improved for valid code compared to Beta 1." |  |
| IOS-331 | 27.0 | SwiftUI | New Feature + Behavior change | 177954148 |  |  | toolbar/navigation | "You can use `toolbarMinimizationBehavior` to control bar minimization behavior. This modifier replaces `toolbarMinimizeBehavior`." |  |
| IOS-332 | 27.0 | SwiftUI | New Feature | 179388848 |  |  |  | "The new data item or error object based `alert` and `confirmationDialog` modifiers can now be used by projects targeting iOS 15.0, macOS …" |  |
| IOS-333 | 27.0 | SwiftUI | New Feature | 180300890 | Yes |  |  | "In macOS apps built with the macOS 27 SDK, the action retrieved from the `\.newDocument` environment value accepts an in-memory `ReadableDocument` produced …" |  |
| IOS-334 | 27.0 | SwiftUI | New Feature | 180301165 |  |  |  | "A new `fileExporter(isPresented:documents:contentTypes:onCompletion:onCancellation:)` modifier exports a collection of values that conform to `WritableDocument` whose `Writer.Destination` is `URL`. The system presents a single …" |  |
| IOS-335 | 27.0 | SwiftUI | New Feature + Behavior change | 180301399 |  |  |  | "The `makeFileWrapper` closure of `FileWrapperDocumentWriter` now receives a second argument, `previous: FileWrapper?`, holding the `FileWrapper` from the document’s most recent read or …" |  |
| IOS-336 | 27.0 | SwiftUI | New Feature + Behavior change | 180301692 |  |  |  | "`DocumentReader.Source` and `DocumentWriter.Destination` now default to `URL`. Conforming types that read from or write to a file URL no longer need to …" |  |
| IOS-337 | 27.0 | SwiftUI | Resolved | 111501113 (FB12477370) | Yes |  | status-bar scroll-to-top | "Fixed: In apps built with the 2027 SDKs, tapping the status bar to scroll a `ScrollView` to its top correctly updates a …" |  |
| IOS-338 | 27.0 | SwiftUI | Resolved | 151015350 |  |  | text rendering | "Fixed: A custom `TextRenderer` applied via `.textRenderer(_:)` now takes effect on a `Text` view that also has `.textSelection(.enabled)` applied. Previously, the custom …" |  |
| IOS-339 | 27.0 | SwiftUI | Resolved | 154080867 |  |  |  | "Fixed: When you apply both `.fileExporter(_:...)` and `.fileMover(_:...)` modifiers to a view, some dialogs might not present correctly." |  |
| IOS-340 | 27.0 | SwiftUI | Resolved + Behavior change | 165913417 | Yes |  | layout/safe area | "Fixed: In apps built with the 27.0 SDKs, `containerRelativeFrame(_:alignment:)` incorrectly accounts for safe-area insets on a `ScrollView`’s non-scrollable axis, causing the calculated …" |  |
| IOS-341 | 27.0 | SwiftUI | Resolved | 167443223 |  |  |  | "Fixed: Retroactive conformances of SwiftUI types to Equatable are not consulted when SwiftUI compares their values." |  |
| IOS-342 | 27.0 | SwiftUI | Resolved + Behavior change | 167448274 | Yes |  | control size in sheets | "Fixed: Certain control-related view modifiers unexpectedly affect sheet and popover content. In apps built with the 27.0 SDKs, the `controlSize`, `buttonSizing`, `buttonRepeatBehavior`, …" |  |
| IOS-343 | 27.0 | SwiftUI | Resolved | 169091260 |  |  | menu labels/gestures | "Fixed: `Menu` labels cannot contain controls, views with gestures, or view representables with gesture recognizers." |  |
| IOS-344 | 27.0 | SwiftUI | Resolved | 175681345 |  |  | layout spacing | "Fixed: A Button containing both an icon and a title placed inside a `List` `Section` header or footer has incorrect spacing between …" |  |
| IOS-345 | 27.0 | SwiftUI | Resolved | 178421089 |  |  | focus/keyboard | "Fixed: When you present a `fullScreenCover` with a `.navigationTransition(_:)` and set `@FocusState` to `true` via `.onAppear`, the keyboard does not animate concurrently …" |  |
| IOS-346 | 27.0 | SwiftUI | Resolved | 179149051 (FB23015259) |  |  |  | "Fixed: `@State` variable named using a raw identifier fails to compile." |  |
| IOS-347 | 27.0 | SwiftUI | Resolved (no "Fixed:" prefix; behavior statement) + Behavior change | 180302015 |  |  |  | "The `read(from:progress:)` and `write(content:to:previous:progress:)` requirements of `DocumentReader` and `DocumentWriter` are declared with `@concurrent` instead of `nonisolated`. With approachable-concurrency defaults that infer `MainActor` …" |  |
| IOS-348 | 27.0 | SwiftUI | Resolved (no "Fixed:" prefix; behavior statement) + Behavior change | 180302065 |  |  |  | "The `makeDocument:` and `makeReadableDocument:` closures passed to `DocumentGroup` initializers are now `@MainActor`-isolated. SwiftUI invokes these factories on the main actor when constructing …" |  |
| IOS-349 | 27.0 | SwiftUI | Resolved (no "Fixed:" prefix; behavior statement) + Behavior change | 180302075 |  |  |  | "`URLDocumentConfiguration` is a `@MainActor`-isolated `@Observable` reference type and no longer conforms to `Sendable`. Code that captured a configuration in a `Sendable` closure …" |  |
| IOS-350 | 27.0 | SwiftUI | Known Issue | 158441261 |  |  |  | "Progress reported in `DocumentReader.read(from:progress:)` and `DocumentWriter.write(snapshot:to:previous:progress:)` might not be presented." |  |
| IOS-351 | 27.0 | SwiftUI | Deprecation | 178776840 |  |  |  | "The `FileDocument` protocol is deprecated. Use `ReadableDocument` for read-only documents or `Document` for documents that support reading and writing." |  |
| IOS-352 | 27.0 | System | New Feature | 160612181 |  |  |  | "System now provides Swift APIs for the C `stat`, `lstat`, `fstat`, and `fstatat` system calls. This includes a new `Stat` type with …" |  |
| IOS-353 | 27.0 | System | Resolved | 177911316 |  |  |  | "Fixed: Custom `FilePath` or `FileDescriptor` extensions that make unqualified calls to `stat()` or `stat(_)` (without the `Darwin.` qualification) might conflict with the …" |  |
| IPAD-105 | 27.0 | System Experience | Resolved | 176281601 |  | Yes | iPad external display | "Fixed: When Siri is off and your iPad is extended to an external display where Spotlight is on screen, disconnecting the display …" |  |
| IOS-354 | 27.0 | System Experience | Resolved | 177893758 |  |  | CarPlay screen | "Fixed: After using iPhone Mirroring or other non-main display experiences, a black pill may appear on the CarPlay screen." |  |
| IOS-355 | 27.0 | System Stability | Resolved | 178343305 |  |  |  | "Fixed: Devices might freeze or panic when idle." |  |
| IOS-356 | 27.0 | TextKit | New Feature | 159870239 |  |  | TextKit tables; matches IOS-06 | "`NSTextTable` and its related objects and types are available to UIKit clients starting with OS 27 releases." |  |
| IOS-357 | 27.0 | Trust Insights | New Feature | 154949256 |  |  |  | "You can now use the TrustInsights framework in your apps by declaring the TrustInsights capability on your app target in Xcode. The …" |  |
| IOS-358 | 27.0 | UIKit | New Feature | 161843040 | Yes |  | scenes; matches IOS-02 | "When linked on iOS 27, tvOS 27, macCatalyst 27, or visionOS 27 SDKs, you can use `UIScene.extendStateRestoration` and `UIScene.completeStateRestoration` to extend state …" |  |
| IOS-359 | 27.0 | UIKit | New Feature + Behavior change | 168247372 | Yes |  | launch/scenes | "iOS and iPadOS apps built with the 27.0 SDK or later are required to include a launch screen. Your app’s `Info.plist` must …" |  |
| IOS-360 | 27.0 | UIKit | New Feature + Behavior change | 168884200 |  |  | drag interaction/gestures | "On iOS 27.0 and iPadOS 27.0, Siri can load resources from drag interactions installed in your app’s interface. For example, when Apple …" |  |
| IOS-361 | 27.0 | UIKit | New Feature + Behavior change | 170005251 | Yes |  | trait propagation (Dynamic Type); matches IOS-03 | "In apps built with the iOS 27.0 SDK, a presented view controller inherits its trait collection by walking up its view’s superview …" |  |
| IPAD-106 | 27.0 | UIKit | New Feature + Behavior change | 170479084 |  | Yes | menu icons | "On iPadOS 27.0 and macOS 27.0, the menu bar and context menus present a reduced set of menu item images and do …" |  |
| IOS-362 | 27.0 | UIKit | New Feature + Behavior change | 173860616 | Yes |  | search/navigation layout | "In apps built with the iOS 27.0 SDK, when `UISearchController` uses center search-bar placement, the scope bar appears inline on the same …" |  |
| IOS-363 | 27.0 | UIKit | New Feature + Behavior change | 177015874 | Yes |  | external display scenes | "In apps built with the iOS 27.0 SDK, `windowExternalDisplayNonInteractive` scenes are no longer offered automatically by the system. Use `UIViewController.registerSceneAccessory(_:)` with a …" |  |
| IOS-364 | 27.0 | UIKit | New Feature + Behavior change | 177953926 |  |  | navigation bar | "Use `UINavigationItem.navigationBarMinimization` to control navigation bar minimization behavior. This property replaces `UINavigationItem.barMinimizeBehavior` and `UINavigationItem.barMinimizationSafeAreaAdjustment`." |  |
| IOS-365 | 27.0 | UIKit | New Feature + Behavior change | 179191941 (FB23027596) |  |  | scroll edge layout | "The container view of a `UIScrollEdgeElementContainerInteraction` may contribute its size and position to the overall shape of the scroll edge effect." |  |
| IOS-366 | 27.0 | UIKit | Resolved | 162044221 | Yes |  | status bar | "Fixed: In apps built with the iOS 27.0 SDK, the deprecated status bar accessors on `UIApplication` — including `statusBarFrame`, `statusBarOrientation`, `statusBarStyle`, and …" |  |
| IPAD-107 | 27.0 | UIKit | Resolved | 166422120 | Yes | Yes | iPad windows | "Fixed: On iPad, if your iPad app is built with the iOS 27 SDK and its `UISupportedInterfaceOrientations` doesn’t include all four interface …" |  |
| IOS-367 | 27.0 | UIKit | Resolved | 169108042 |  |  | scene closure | "Fixed: The `UISceneClosureConfirmation` API does not present a confirmation dialog." |  |
| IOS-368 | 27.0 | UIKit | Resolved | 173271862 |  |  | menu subtitle | "Fixed: The `UIMenuLeaf` protocol is missing the subtitle property introduced in iOS 16.0." |  |
| IOS-369 | 27.0 | UIKit | Resolved | 174773785 |  |  | toolbar | "Fixed: The background might not appear on a bottom toolbar when you use `UIBarButtonItem.hidesSharedBackground` to hide a toolbar item’s glass background." |  |
| IOS-370 | 27.0 | UIKit | Resolved | 178555304 | Yes |  | scenes/orientation | "Fixed: In iPhone Mirroring, if your app is built with the iOS 27 SDK its scene will support all interface orientations regardless …" |  |
| IOS-371 | 27.0 | UIKit | Resolved | 178558224 | Yes |  | scenes/resize | "Fixed: In iPhone Mirroring, if your app is built with the iOS 27 SDK and sets `UIRequiresFullScreen`, its scene receives continuous resize …" |  |
| IOS-372 | 27.0 | UIKit | Resolved | 178558897 | Yes |  | scenes/screen | "Fixed: In iPhone Mirroring if your app is built with the iOS 27 SDK, its scene is initially connected to a `UIScreen` …" |  |
| IPAD-108 | 27.0 | UIKit | Resolved | 178559386 | Yes | Yes | iPad windows | "Fixed: On iPad, if your iPad app is built with the iOS 27 SDK and sets `UIRequiresFullScreen`, the bounds of `UIScreen.main` changes …" |  |
| IPAD-109 | 27.0 | UIKit | Resolved | 178560235 | Yes | Yes | iPad windows | "Fixed: On iPad, if your iPad app is built with the iOS 27 SDK and sets `UIRequiresFullScreen`, its scene receives continuous resize …" |  |
| IPAD-110 | 27.0 | UIKit | Resolved | 178561952 | Yes | Yes | iPad windows | "Fixed: On iPad, if your iPhone-only app is built with the iOS 27 SDK its scene continues to honor supported interface orientations …" |  |
| IPAD-111 | 27.0 | UIKit | Resolved | 178562971 | Yes | Yes | iPad windows | "Fixed: On iPad, if your iPhone-only app is built with the iOS 27 SDK and sets `UIRequiresFullScreen`, its scene receives continuous resize …" |  |
| IPAD-112 | 27.0 | UIKit | Resolved | 178573319 | Yes | Yes | iPad layout/orientation | "Fixed: On iPad, if your iPhone-only app is built with the iOS 27 SDK and supports only portrait or only landscape interface …" |  |
| IOS-373 | 27.0 | UIKit | Deprecation + Behavior change | 141837548 | Yes |  | scene life cycle | "Apps built with the latest SDK must adopt the scene-based life cycle or they fail to launch. For migration guidance, see [Transitioning …" |  |
| IOS-374 | 27.0 | UIKit | Deprecation + Behavior change | 179874781 |  |  |  | "`canOpenURL:` is deprecated. Attempt to open the URL and handle any failure instead of validating it first. Using universal links instead of …" |  |
| IOS-375 | 27.0 | USDKit | Resolved | 170653056 |  |  |  | "Fixed: Some types of USD attributes cannot be read or modified." |  |
| IOS-376 | 27.0 | USDKit | Resolved | 178071414 |  |  |  | "Fixed: Array, vector, matrix, and quaternion types cannot be authored using USDKit." |  |
| IOS-377 | 27.0 | VideoToolbox | New Feature | 177635243 |  |  |  | "`VTLowLatencySuperResolutionScalerConfiguration` now supports a 1.5x scale factor. Call `+supportedScaleFactorsForFrameWidth:frameHeight:` to discover the scale factors available for your source dimensions." |  |
| IOS-378 | 27.0 | VideoToolbox | New Feature | 179040806 |  |  |  | "`VTLowLatencyFrameInterpolationConfiguration` now supports arbitrary source dimensions up to 1080p." |  |
| IOS-379 | 27.0 | Voice Control | Resolved | 184088006 |  |  | Voice Control | "Fixed: Voice Control might not respond when using Flexible Item Names to describe items on the screen." |  |
| IOS-380 | 27.0 | Watch Connectivity | Resolved | 113202790 (FB12819178) |  |  |  | "Fixed: The `WCSession.transferCurrentComplicationUserInfo` method does not work with complications built using WidgetKit on watchOS." |  |
| IOS-381 | 27.0 | Weather Highlights | Deprecation | 164408676 |  |  |  | "Weather Highlights is currently only available in US English." |  |
| IOS-382 | 27.0 | WidgetKit | Resolved | 177493357 |  |  |  | "Fixed: Your widget extension might not render its timeline when it uses an App Intent with a `@UnionValue` parameter, and content such …" |  |
| IOS-383 | 27.0 | Writing Tools | Known Issue | 177097101 |  |  | Writing Tools input | "Writing Tools becomes unresponsive when you interact with the Plus button while Writing Tools is in use." | Force quit Messages to resolve the issue. |
| IOS-384 | 27.0 | Xcode | Resolved | 179746601 |  |  |  | "Fixed: The Simulator might display a black wallpaper and blank app icons temporarily during first boot." |  |
| IOS-385 | 27.2 | App Tracking Transparency | New Feature | 179504171 |  |  |  | "`AppTrackingTransparency` ([ATT](https://developer.apple.com/documentation/apptrackingtransparency)) now supports an alternative expanded prompt and reprompting on a yearly basis for EU users. The alternative prompt is required …" |  |
| IOS-386 | 27.2 | App Tracking Transparency | Resolved | 187149729 |  |  |  | "Fixed: The new `requestTrackingAuthorization(usingExpandedInterface:additionalInformationAction:completionHandler:)` API is renamed to `requestTrackingAuthorization(preferExpandedInterface:...)`." |  |
| IOS-387 | 27.2 | App Tracking Transparency | Resolved | 187610745 |  |  |  | "Fixed: The new `requestTrackingAuthorizationPreferExpandedInterface:...` API is renamed to `requestTrackingAuthorizationPreferringExpandedInterface:...`." |  |
| IOS-388 | 27.2 | Health | Known Issue | 186964423 |  |  |  | "Personalized summaries might not generate as expected in the Insights tab." |  |
| IOS-389 | 27.2 | Health | Known Issue | 188843443 |  |  |  | "The redesigned Health app is not included in this beta and was available in the previous beta for testing purposes only. If …" |  |
| IOS-390 | 27.2 | Nearby Interaction | Known Issue | 189664070 |  |  |  | "An `NISession` running with a DL-TDoA configuration in a foreground app might be invalidated unexpectedly with a resource timeout error (`NIErrorCodeResourceUsageTimeout`)." | Run a new `NISession` with the same DL-TDoA configuration. |
| IOS-391 | 27.2 | Quest Lab Appointments | Known Issue | 184530996 |  |  |  | "If you have an upcoming lab appointment, wait to update iOS versions until you receive your results. Contact [Quest](https://support.exp.questdiagnostics.com) directly to reschedule …" | Lab results are also available under Browse > Lab Results. |
| IOS-392 | 27.2 | Shortcuts | Known Issue | 187499433 |  |  |  | "Describe a Shortcut might fail with the error “Something went wrong. Try again later.”" |  |
| IOS-393 | 27.2 | Simulator | Known Issue | 188407822 (FB24939277) |  |  |  | "Cloning a simulator device running runtime 27.2 might fail due to incorrect file permissions." | `find ~/Library/Developer/CoreSimulator/Devices/<SOURCE_UDID>/data -name '*.sb-????????-??????' -delete` |
| IOS-394 | 27.2 | StoreKit Testing in Xcode | Resolved | 183933307 (FB24137836) |  |  |  | "Fixed: Intro offer eligibility does not reset immediately after calling `SKTestSession.clearTransactions()`." |  |
| IOS-395 | 27.2 | StoreKit Testing in Xcode | Resolved | 184155259 |  |  |  | "Fixed: Changing the storefront or locale using `SKTestSession` doesn’t propagate through `Storefront.updates`." |  |
| IOS-396 | 27.2 | StoreKit Testing in Xcode | Resolved | 184255116 |  |  |  | "Fixed: Failed purchases using `SKTestSession` might display error dialogs even when `dialogsDisabled` is set to `true`." |  |
| IOS-397 | 27.2 | StoreKit Testing in Xcode | Known Issue | 186018916 |  |  |  | "Making a purchase in-app for a subscription that is a member of a subscription bundle incorrectly allows the user to unbundle instead …" |  |
| IOS-398 | 27.2 | UIKit | New Feature + Behavior change | 186294594 |  |  | layout margins; matches IOS-04 | "On iOS 27.1 and later, the default layout margins for a `UIView` are zero. A view controller continues to provide its view …" |  |
| IOS-399 | 27.3 beta | App Intents | Known Issue | 190573761 |  |  |  | "If you define `authenticationPolicy` on an `AppEntity` or `AppEntity` property that requires unlock, Siri AI might not request an unlock before it …" |  |
| IOS-400 | 27.3 beta | Live Caller ID Lookup | New Feature | 187726157 |  |  |  | "The system now keeps a set of unused evaluation keys uploaded to your Live Caller ID Lookup service, and when it runs …" |  |
| IOS-401 | 27.3 beta | Live Caller ID Lookup | Deprecation | 191651833 |  |  |  | "Live Caller ID Lookup now requires the shard count in a service’s PIR configuration to be a power of two, for example …" |  |
| IOS-402 | 27.3 beta | NEURLFilter | New Feature | 187726173 |  |  |  | "The system now keeps a set of unused evaluation keys uploaded to your NEURLFilter PIR service, and when it runs out of …" |  |
| IOS-403 | 27.3 beta | NEURLFilter | Deprecation | 191651440 |  |  |  | "NEURLFilter no longer supports user tiers. The system no longer calls your service’s `/token-key-for-user-token` endpoint and instead uses the first valid public …" |  |
| IOS-404 | 27.3 beta | NEURLFilter | Deprecation | 191651462 |  |  |  | "NEURLFilter now limits a service’s PIR configuration to at most 65,536 shards and requires the shard count to be a power of …" |  |
| IOS-405 | 27.3 beta | NEURLFilter | Deprecation | 191651632 |  |  |  | "Your NEURLFilter service URL and Privacy Pass issuer URL must now be declared statically in your app’s Info.plist, and providing them only …" |  |
| IOS-406 | 27.3 beta | StoreKit | New Feature | 164581840 |  |  |  | "Multiseat subscriptions let a customer purchase multiple seats for an auto-renewable subscription and invite others to join it. Check whether a subscription …" |  |
| IOS-407 | 27.3 beta | StoreKit | Resolved | 190639717 |  |  |  | "Fixed: If you test Ask to Buy in the Sandbox environment while signed in to an iCloud account that is a member …" |  |
| IOS-408 | 27.3 beta | StoreKit Testing in Xcode | Resolved | 186018916 |  |  |  | "Fixed: Making an in-app purchase for a subscription that is a member of a subscription bundle incorrectly allows the user to unbundle …" |  |
| IOS-409 | 27.3 beta | StoreKit Testing in Xcode | Known Issue | 186670057 (FB24651858) |  |  |  | "When you launch an app that uses `SKTestSession` for the first time, some StoreKit Test API calls might hang." | Set a StoreKit configuration file in your scheme’s run options, then rerun the tests. |
| IOS-410 | 27.3 beta | SwiftUI | Resolved (no "Fixed:" prefix; behavior statement) + Behavior change | 188312290 | Yes |  | scroll edge visuals; matches IOS-05 | "In apps built with the iOS 26 SDK,`ScrollEdgeEffectStyle.soft` rendered a fully transparent edge above a `safeAreaBar(edge:)` when running on iOS 27. In …" |  |

### Inferences
- **Release coverage gap:** 27.0, 27.2, and 27.3 beta each have one release-notes page; 27.1 has none. The only release-note evidence of a 27.1 platform behavior change is the 27.2 margin entry IOS-398 ("On iOS 27.1 and later"). This is consistent with 27.1 being an iPhone Duo-only build (Key question 2).
- **Resolved items in the 27.0 notes are mostly beta-cycle regressions.** Several explicitly name betas: IOS-102 (178280323, "Beta 1"/"Beta 2"), Apple Wallet 182055786 ("Beta 3 or 4"), Control Center 184729556 workaround ("beta 1 or earlier"), Siri 182145010 ("As of beta 5"), and SwiftUI 177526032 ("compared to Beta 1"). Treat most 27.0 "Resolved" rows as fixed before GM, not as fixes of iOS 26 shipping behavior. Exceptions carry FB numbers from earlier cycles, for example 111501113/FB12477370 and 102093015/FB11767567.
- **CarPlay and Siri duplicate known issue:** the identical Known Issue text "Siri might respond more slowly than expected in CarPlay…" appears twice with different issue numbers. It is 178952858 under CarPlay (IOS-125) and 178274714 under Siri (IOS-289).
- For accessibility auditing, the SDK-linked entries carry the most regression risk when an app moves to the 27 SDK:
  - selectable-Text gestures (79770704)
  - TabView selection crash (164516837)
  - trait propagation (170005251)
  - control-size reset in sheets (167448274)
  - search scope-bar placement (173860616)
  - external-display scenes (177015874)
  - scene life-cycle requirement (141837548)
  - launch screen requirement (168247372)
  - status-bar accessor NaNs (162044221)
  - the iPad resize and orientation model (IPAD-107..112)

  The zero default `UIView` margins (186294594) are an OS-version behavior "On iOS 27.1 and later". The text does not gate it on the SDK, so it may affect existing binaries. Verify this before relying on it.
- The menu-image reduction on iPadOS (IPAD-104/106) could remove icon cues that some users (for example, users with cognitive disabilities) rely on. This is my inference; Apple does not state it.

### Gaps
- No developer release-note entries cover Switch Control, Full Keyboard Access, Dynamic Type, captions, haptics, or `UIAccessibility` API changes. Searches of all three Markdown files for "accessib", "Dynamic Type", "Switch Control", "Full Keyboard", "haptic", and "caption" return zero hits. API-level accessibility changes would need the DocC API diff or framework documentation, which this pass did not check.
- Symbol availability for every named API is **pending declaration review**. DocC availability JSON was not fetched.
- Apple sometimes edits release notes after publication. The SHA-256 hashes above pin the 2026-11-05 snapshot only.

## Key question 2: What did 27.1 change (and what do the Apple Support "About iOS/iPadOS 27 Updates" pages say)?

### Takeaway
No iOS & iPadOS 27.1 developer release notes exist. Apple's index lists only 27, 27.2, and the 27.3 beta. On Apple's security-releases page, 27.1 is an **iOS-only, iPhone Duo-only** update with no published CVE entries, dated 23 Oct 2026. The only Tier-1 evidence of a 27.1 platform change is the 27.2 note that `UIView` default layout margins are zero "on iOS 27.1 and later". The consumer "About iOS 27 Updates" page (published October 26, 2026) has sections for 27, 27.0.1, and 27.2 but none for 27.1. Its 27.2 section adds one accessibility-adjacent item: FaceTime support for third-party sign language interpreters and live captioners.

### Cited Findings
- The DocC index JSON and Markdown index list only "iOS & iPadOS 27.3 Beta Release Notes", "iOS & iPadOS 27.2 Release Notes", and "iOS & iPadOS 27 Release Notes" under "iOS & iPadOS 27". There is no 27.1 child page. By contrast, the 26 cycle lists 26, 26_1 … 26_6. (Tier-1) — [iOS & iPadOS Release Notes index](https://developer.apple.com/documentation/ios-ipados-release-notes); [index JSON](https://developer.apple.com/tutorials/data/documentation/ios-ipados-release-notes.json)
- Direct probes of `.../ios-ipados-27_1-release-notes.md` and the JSON variants `ios-ipados-27_1-release-notes`, `ios-ipados-27_0_1-release-notes`, and `ios-ipados-27_1-beta-release-notes` all returned HTTP 404 on 2026-11-05. (Tier-1, negative evidence) — [developer.apple.com](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-27_1-release-notes.md)
- Apple security releases list "iOS 27.1 — This update has no published CVE entries." with device "iPhone Duo" and date 23 Oct 2026. There is no iPadOS 27.1 row. (Tier-1) — [Apple security releases](https://support.apple.com/en-us/100100)
- IOS-398 / 186294594: "On iOS 27.1 and later, the default layout margins for a `UIView` are zero." This is published in the 27.2 notes, UIKit › New Features. (Tier-1) **Matches IOS-04.** — [27.2 RN](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-27_2-release-notes)
- MacRumors reports that iOS 27.1 was released only for iPhone Duo. The device shipped with build 24A94232 and got a day-one update to build 24A94425. Apple's update text reportedly says only "bug fixes for your iPhone". (Tier-2; the 24A94232 number comes from a reader comment cited by the fetch, so treat it as Tier-3.) — [MacRumors, Oct 23 2026](https://macrumors.com/2026/10/23/apple-releases-ios-27-1/); [MacRumors, Oct 13 2026](https://macrumors.com/2026/10/13/iphone-duo-day-one-update)
- **About iOS 27 Updates** (published October 26, 2026) lists sections for iOS 27, 27.0.1, and 27.2, with no 27.1 section. (Tier-1) — [About iOS 27 Updates](https://support.apple.com/en-us/149076)
  - **27.0 Accessibility section (consumer features):**
    - VoiceOver: more detailed image understanding for photos, charts, and screenshots; a conversational experience for asking about the screen or surroundings; and "a new way to get answers fast with an Action button integration" (iPhone only).
    - Magnifier: enhanced, with conversational visual assistance, a high-contrast interface, and natural-language app controls.
    - Accessibility Reader: smarter text cleanup and formatting, images and tables, on-demand summaries, and translation.
    - "Voice Control flexible inputs" let you describe on-screen elements, for example "tap the gear".
    - Dictation: more accurate, using an on-device model on iPhone Air and iPhone 17 Pro and later.
  - **27.0 System Improvements:** "Liquid Glass refinements improve overall readability", with a new Settings slider "from ultra-clear to fully tinted". Also independent volume settings for Alarms and Timers.
  - **27.0.1:** fixes an iPhone 18 Pro/Pro Max restart on Face ID failure, a 2x photo color artifact, and an issue where opening Notification Center and Control Center simultaneously "may cause the touchscreen to become unresponsive".
  - **27.2:** Siri AI memory and wider personal context, Excluded Apps, granular text selection in Siri responses, Siri AI in French, Japanese, Korean, Portuguese, and Spanish, and Suggestions in Messages. Also "FaceTime supports adding a third party sign language interpreter or live captioner to a call".
- **About iPadOS 27 Updates** (Tier-1) — [About iPadOS 27 Updates](https://support.apple.com/en-us/149075). Differences from the iOS page:
  - The VoiceOver bullet omits the Action-button integration.
  - Write with Siri works when hovering a trackpad over a text selection or empty line, and with handwritten text selected in Notes.
  - 27.2 adds "Side-by-side multitasking is easier to set up", with a second-app choice when tiling apps left or right via window controls or the menu bar.
  - 27.0 adds Visual Intelligence with Apple Pencil highlighting, Spotlight-integrated Siri by swiping down from the top edge, app names in the status bar, and the ability to resize iPhone apps running on iPad.
  - The iPadOS 27.0.1 note says only "bug fixes for your iPad".
  - On-device voice and dictation models require M4 or later with at least 12GB of unified memory.
- Claim IDs for Support-page items, all Tier-1 consumer-feature claims and not API claims:
  - IOS-411: VoiceOver image understanding, conversational Q&A, and Action button
  - IOS-412: Magnifier
  - IOS-413: Accessibility Reader
  - IOS-414: Voice Control flexible inputs (developer counterpart IOS-379)
  - IOS-415: on-device dictation (developer counterpart IOS-147)
  - IOS-416: Liquid Glass readability slider
  - IOS-417: 27.0.1 touchscreen-unresponsive fix
  - IOS-418: 27.2 FaceTime sign language interpreter or live captioner
  - IOS-419: 27.2 Siri granular text selection
  - IPAD-113: iPadOS VoiceOver bullet without Action button
  - IPAD-114: trackpad hover for Write with Siri
  - IPAD-115: 27.2 side-by-side tiling second-app choice
  - IPAD-116: resizing iPhone apps on iPad (developer counterpart IPAD-110..112)
  - IPAD-117: app names in the status bar
  - Sources: [149076](https://support.apple.com/en-us/149076); [149075](https://support.apple.com/en-us/149075)

### Inferences
- 27.1 was most likely a device-enablement branch for iPhone Duo that Apple folded into 27.2. The 27.2 notes document the 27.1 margin change, and 27.2 shipped two iOS builds on the same day (Key question 3). This is not confirmed by Apple text.
- A missing 27.1 notes page does **not** mean nothing changed. At least one UIKit layout behavior (186294594) is dated to 27.1.

### Gaps
- No Apple text describes any other 27.1 changes, and no Apple page states the 27.1 build numbers. Builds come from Tier-2 and Tier-3 reporting only.
- The Support pages do not say whether the VoiceOver, Magnifier, or Accessibility Reader features expose new developer APIs. This pass found no developer release-note entry for them.
- An India-region copy of 149076 (support.apple.com/en-in/149076) was surfaced by search but not fetched. The search summary claimed it differs from the US copy, but I did not verify that.

## Key question 3: Exact release dates and build numbers (27.0, 27.0.x, 27.1, 27.2, 27.3 beta)

### Takeaway
Apple Tier-1 sources give these dates:
- iOS/iPadOS 27: 14 Sep 2026
- 27.0.1: 28 Sep 2026, build 24A446
- iOS 27.1 (iPhone Duo only): 23 Oct 2026
- 27.2: 26 Oct 2026, build 24B119, plus a second iOS-only build 24B91020
- 27.3 beta (stable releases are listed separately above): 3 Nov 2026, build 24C5037i

The 27.0 GM/RC build (24A435) and the 27.1 builds come only from Tier-2 and Tier-3 sources.

### Cited Findings
- Security releases: "iOS 27 and iPadOS 27", 14 Sep 2026, with content at support.apple.com/en-us/149034. "iOS 27.0.1 and iPadOS 27.0.1 — no published CVE entries", 28 Sep 2026. "iOS 27.1 — no published CVE entries", iPhone Duo, 23 Oct 2026. "iOS 27.2 and iPadOS 27.2", 26 Oct 2026, with content at 149230. Device list for 27/27.0.1/27.2: iPhone 11 and later, iPad Pro 12.9-inch 4th gen and later, iPad Pro 11-inch 2nd gen and later, iPad Air 4th gen and later, iPad 9th gen and later, and iPad mini 6th gen and later. (Tier-1) — [Apple security releases](https://support.apple.com/en-us/100100)
- The 149034 security page header reads "Released September 14, 2026". (Tier-1) — [About the security content of iOS 27 and iPadOS 27](https://support.apple.com/en-us/149034)
- Apple Developer News releases list these builds (Tier-1) — [Apple Developer Releases](https://developer.apple.com/news/releases/); [Releases RSS](https://developer.apple.com/news/releases/rss/releases.rss):
  - "iOS 27.3 beta (24C5037i)" and "iPadOS 27.3 beta (24C5037i)", November 3, 2026
  - "iOS 27.2 (24B91020)", "iOS 27.2 (24B119)", and "iPadOS 27.2 (24B119)", October 26, 2026
  - "iOS 27.0.1 (24A446)" and "iPadOS 27.0.1 (24A446)", September 28, 2026
  - The page as fetched did not include the iOS 27.0 (Sep 14) or iOS 27.1 entries. The fetched list appears truncated to recent items, and `?page=2/3` returned nothing parseable.
- The iOS 27 release candidate build was 24A435, issued to developers around September 9. The source notes that Apple had not confirmed it as the public build. (Tier-2) — [The Mac Observer](https://www.macobserver.com/news/ios-27-release-candidate-build-24a435-explained/)
- iOS 27.1 for iPhone Duo: build 24A94425 was the day-one update (IPSW), and the factory build was reportedly 24A94232. Reports disagree on whether the newer build appeared on Oct 13 or Oct 22. (Tier-2/Tier-3) — [MacRumors](https://macrumors.com/2026/10/23/apple-releases-ios-27-1/); [MacRumors](https://macrumors.com/2026/10/13/iphone-duo-day-one-update)

### Inferences
- The 24B91020 iOS 27.2 build is probably the iPhone Duo variant of 27.2, given the 27.1 Duo-only branch and its "24A94xxx" style build numbers. Apple does not say this; it is unverified.
- The 27.3 beta build suffix "i" is unusual for a first beta. I did not check whether this is beta 1 or later. Apple's release title does not include a beta number.

### Gaps
- Apple Tier-1 pages fetched here do not give the iOS 27.0 public build number. 24A435 is Tier-2 only.
- I found no Tier-1 statement of 27.1 build numbers, and no Tier-1 explanation for the two 27.2 builds.
- 27.3 beta number and date ordering: only one 27.3 beta entry (Nov 3) was visible. Whether earlier 27.3 betas exist is not established.

## Key question 4: Which 27.0 known issues were resolved in 27.1, 27.2, or 27.3 (matched by issue number)?

### Takeaway
Exact issue-number matches show only **two 27.0 Known Issues resolved later**. Both are StoreKit Testing issues fixed in 27.2: 184155259 and 184255116. One 27.2 Known Issue (186018916) is resolved in the **27.3 beta** (not yet stable). No 27.0 accessibility-relevant Known Issue appears as resolved in any later notes. That includes Dictation Voice Editing 173448573, the Siri speech and voice-command issues, Now Playing 186036238, and Writing Tools 177097101.

### Cited Findings
- 184155259: 27.0 Known Issue (IOS-310), "Changing the storefront or locale using `SKTestSession` doesn't propagate through `Storefront.updates`." Listed as Fixed in 27.2 StoreKit Testing in Xcode › Resolved (IOS-395). (Tier-1) — [27.0 RN](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-27-release-notes); [27.2 RN](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-27_2-release-notes)
- 184255116: 27.0 Known Issue (IOS-311), failed `SKTestSession` purchases might show error dialogs even with dialogs disabled. Fixed in 27.2 (IOS-396). (Tier-1) — [27.0 RN](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-27-release-notes); [27.2 RN](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-27_2-release-notes)
- 183933307 (intro offer eligibility after `clearTransactions()`) is listed as **Resolved in both** 27.0 (IOS-309) and 27.2 (IOS-394). This is a duplicate fixed-listing, not a Known→Resolved transition. (Tier-1) — same sources
- 186018916: 27.2 Known Issue (IOS-397), an in-app purchase of a subscription-bundle member allows unbundling instead of throwing. Fixed in **27.3 beta** (IOS-408). Beta only, not stable. (Tier-1) — [27.2 RN](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-27_2-release-notes); [27.3 Beta RN](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-27_3-release-notes)
- These 27.0 Known Issues have **no** later resolution entry (matched by issue number across the 27.2 and 27.3 beta notes):
  - 181800016 (App Intents photos schema)
  - 178952858 (CarPlay Siri slowness)
  - 184729556 (Performance Trace control)
  - 183770678 (SpotlightSearchTool context size)
  - 173448573 (Dictation Voice Editing)
  - 178200601 (Vision Pro Guest Mode Live Activities)
  - 186036238 (Now Playing APNs)
  - 178202101 (Related Receipts disclaimer)
  - 180040003 (Reminders empty title)
  - 166068090 and 168315587 (Shortcuts)
  - 171728298, 176812955, 177116121, 177376984, 177984074, 178049066, 178274714, 181266301 (Siri)
  - 158441261 (SwiftUI document progress)
  - 177097101 (Writing Tools)
  - Source: [27.0 RN](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-27-release-notes); [27.2 RN](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-27_2-release-notes); [27.3 Beta RN](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-27_3-release-notes)
- New Known Issues in 27.2:
  - 186964423: Health Insights summaries
  - 188843443: redesigned Health app pulled from the beta
  - 189664070: DL-TDoA `NISession` timeout. Workaround: run a new session.
  - 184530996: Quest lab appointments. Workaround: Browse > Lab Results.
  - 187499433: Describe a Shortcut error
  - 188407822 / FB24939277: simulator clone permissions, with a `find … -delete` workaround

  The 27.2 Health known issue references "this beta", so it is apparently left over from beta notes.
- New Known Issues in 27.3 beta: 190573761 (App Intents `authenticationPolicy`; Siri AI might not request unlock before showing entities) and 186670057 / FB24651858 (`SKTestSession` hangs on first launch; workaround: set a StoreKit configuration file in the scheme).
- Sources: [27.2 RN](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-27_2-release-notes); [27.3 Beta RN](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-27_3-release-notes)
- 27.2 also renamed two new ATT APIs. 187149729 renamed `requestTrackingAuthorization(usingExpandedInterface:…)` to `…(preferExpandedInterface:…)`. 187610745 renamed the ObjC selector to `requestTrackingAuthorizationPreferringExpandedInterface:…`. Both relate to the 27.2 ATT expanded prompt for EU users (179504171). (Tier-1) — [27.2 RN](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-27_2-release-notes)

### Inferences
- Known Issues absent from later notes may be fixed silently, still open, or not carried forward. Apple's point-release notes list only items new to that release, so absence is not evidence either way.
- Because no 27.1 notes exist, no 27.1 resolutions can be matched.

### Gaps
- No Tier-1 confirmation of the status of the accessibility-adjacent 27.0 Known Issues after 27.0: Dictation Voice Editing 173448573, Siri speech truncation 181266301, Siri voice-command photo selection 171728298/176812955, and Writing Tools 177097101.
- Matching was by Apple issue number only. No Feedback Assistant or Tier-2/3 verification was done.

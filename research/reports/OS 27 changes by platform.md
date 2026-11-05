# OS 27 reshapes accessibility through semantics

Apple's OS 27 family documents **927 developer release-note entries** across iOS/iPadOS (322), macOS (296), visionOS (168), watchOS (73) and tvOS (68) for 27.0, 27.2 and the 27.3 beta. Read entry by entry, these releases change accessibility mainly through semantics, layout and input behavior that ships with the 27 SDKs, not through new accessibility APIs. Examples include a `tabs` role that VoiceOver announces, reduced menu imagery, gesture-based text selection, new resize rules and SwiftUI controls that no longer wrap AppKit. User-facing accessibility features shipped mostly outside the developer notes: AI-assisted VoiceOver, Magnifier, Voice Control and Accessibility Reader on iOS 27.0; Look to Drive and the updated Dwell Control on visionOS 27.0; tvOS Larger Text; watch-side Sound Recognition; and a FaceTime interpreter and live-captioner option in 27.2. A DocC scan of 2,518 accessibility-related symbols finds **no new traits, rotors, `UIAccessibility` or `NSAccessibility` members**. The genuinely new surface is narrow: a VoiceOver UI-testing service, an app-accessibility-enabled query, an SSML speech key, exam-mode toggles, caption and sign-language media hooks, and a `TabsPickerStyle` that VoiceOver reads as "tabs". The version labeled "27.1" exists only as iOS for iPhone Duo and as Xcode 27.1. Four announced features still lack shipping evidence, and the corpus keeps 33 conflicts open rather than resolving them. Everything below is backed by the third-pass corpus in [../os-27/README.md](../os-27/README.md). That corpus is research only and stays isolated from skill guidance until benchmark baselines exist.

## Five inventories cover 927 Apple entries, and 27.1 barely exists

The third pass turns the earlier topic index into row-per-entry inventories, transferred mechanically from the notes and with 27.3 beta rows kept in their own sections. Coverage is complete for every retrieved OS release-note document. Safari and Xcode are covered only for the accessibility subset, and their full inventories are backlog item T-1.

| Platform | 27.0 | 27.2 | 27.3 beta | Total | Accessibility or interaction subset | Corpus files |
| --- | ---: | ---: | ---: | ---: | --- | --- |
| iOS and iPadOS | 296 | 14 | 12 | 322 | 92 flagged; 12 iPad-specific | [ios](../os-27/ios.md), [ipados](../os-27/ipados.md), [inventory](../os-27/inventory/ios-ipados.md) |
| macOS | 272 | 9 | 15 | 296 | 48 starred high-priority | [macos](../os-27/macos.md), [inventory](../os-27/inventory/macos.md) |
| visionOS | 160 | 6 | 2 | 168 | 9 flagged | [visionos](../os-27/visionos.md), [inventory](../os-27/inventory/visionos.md) |
| watchOS | 67 | 4 | 2 | 73 | 6 named in notes | [watchos](../os-27/watchos.md), [inventory](../os-27/inventory/watchos.md) |
| tvOS | 62 | 4 | 2 | 68 | 4 named in notes | [tvos](../os-27/tvos.md), [inventory](../os-27/inventory/tvos.md) |
| Safari | 62 rows | 3 | 30 | 96 rows (+1 in 27.1) | accessibility-scoped | [safari-webkit](../os-27/safari-webkit.md), [inventory](../os-27/inventory/safari.md) |
| Xcode | 29 rows | 10 | 9 | 51 rows (+3 in 27.1) | tooling-scoped | [xcode-tooling](../os-27/xcode-tooling.md), [inventory](../os-27/inventory/xcode.md) |

The point releases are thin. The 27.2 and 27.3-beta notes for tvOS, watchOS and visionOS are almost entirely StoreKit Testing. **Only two 27.0 known issues were explicitly fixed later**, both StoreKit Testing items, and none of the accessibility-adjacent known issues (Dictation Voice Editing, Siri speech truncation, photo voice commands, Writing Tools) has a later fix entry ([iOS 27.2 notes](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-27_2-release-notes)). Every `*-27_1-release-notes` URL returns HTTP 404. Apple's security table lists only "iOS 27.1" for iPhone Duo on 23 October 2026 ([Apple security releases](https://support.apple.com/en-us/100100)), and the developer feed shows Xcode 27.1 (27A9275) on 15 October ([Developer Releases](https://developer.apple.com/news/releases/)). The only Apple text describing 27.1 behavior is the 27.2 note that `UIView` default margins are zero "On iOS 27.1 and later." Apple-sourced builds are mapped in [../os-27/releases.md](../os-27/releases.md), for example 27.2 as iOS 24B119 plus an unexplained 24B91020, macOS 26B123, tvOS 24K122, watchOS 24S118 and visionOS 24N120. Builds that come only from press, such as the iOS 27.0 RC 24A435 and the iPhone Duo builds, are flagged as non-Apple.

## Semantics, menus and input carry the platform changes

On **iOS**, the only developer entries that name an assistive technology are `TabsPickerStyle` (IOS-323, pass-2 IOS-01), an Image Playground VoiceOver fix and a Voice Control Flexible Item Names fix ([iOS 27 notes](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-27-release-notes)). The larger risk sits in SDK-linked behavior:
- Presented controllers now inherit traits through the superview chain (IOS-361), which matters for content-size propagation.
- Selectable `Text` gains system selection gestures (IOS-317).
- A `TabView` crashes on a hidden selection (IOS-321).
- Apps built with the latest SDK must adopt the scene life cycle or fail to launch (IOS-373).

Apple's Support page carries the user-facing features: richer VoiceOver image descriptions with conversational questions, Magnifier conversation, an expanded Accessibility Reader, and natural-language Voice Control. All four require iPhone 15 Pro or iPhone 16 and later ([About iOS 27 Updates](https://support.apple.com/en-us/149076)). **iPadOS** adds reduced menu-item imagery (IPAD-104/106) and six SDK-linked resize and orientation rules (IPAD-107 to 112), and its VoiceOver bullet omits the Action button ([About iPadOS 27 Updates](https://support.apple.com/en-us/149075)).

**macOS** has the richest semantic changes:
- `NSSegmentedControl` and `NSToolbarItemGroup` gain roles, including `tabs`, which VoiceOver reads as "tabs" (MAC-118).
- Open/save panel tab-order and keyboard-loop fixes (MAC-124, MAC-133).
- A SwiftUI `Menu` that exposed AXDescription instead of AXTitle is fixed (MAC-330).
- Grouped forms now honor Show borders (MAC-325) ([macOS 27 notes](https://developer.apple.com/documentation/macos-release-notes/macos-27-release-notes)).

The likeliest regressions come from two other changes. On the 27 SDK, image-only `NSMenuItem`s lose their images (MAC-140). SwiftUI `Slider`, `Menu` and `Picker` also stop wrapping `NSSlider` and `NSPopUpButton` (MAC-301, MAC-311), so their inherited accessibility behavior needs re-auditing. That re-audit need is a research inference; Apple's notes say nothing about accessibility impact.

**tvOS 27** brings system Text Size from Large to Accessibility XXXL. Standard UIKit and SwiftUI components scale automatically, and custom text must adopt text styles ([WWDC26-221](https://developer.apple.com/videos/play/wwdc2026/221/)). tvOS 27 runs only on Apple TV 4K (2nd generation and later). **watchOS 27** documents Sound Recognition on Series 12 and Ultra 4 only ([Apple Watch guide](https://support.apple.com/guide/watch/use-sound-recognition-ay39m4y6riek/watchos)), a new single-tap Smart Stack gesture, and an SDK-linked Digital Crown `TabView` selection fix (WATCH-156). `TabsPickerStyle` is absent from watchOS. **visionOS** release notes contain no user-facing accessibility feature. Look to Drive and the glance-to-confirm Dwell Control appear only on Support ([About visionOS 27 Updates](https://support.apple.com/en-us/149067)). Look to Drive comes with heavy restrictions:
- TOLT or LUCI controllers only.
- U.S. and U.S. territories only.
- An adult supporter must be present.
- Not usable on wall power or at 10% battery or below.

**Safari 27.0** adds `ariaNotify` and 32 accessibility fixes, mostly accessible-name computation and VoiceOver navigation. Safari 27.2 stops VoiceOver from repeating re-rendered live regions ([Safari 27.2 notes](https://developer.apple.com/documentation/safari-release-notes/safari-27_2-release-notes)). The 27.3 beta changes the events that VoiceOver activation dispatches. **Xcode 27** adds `XCUIVoiceOverService`, an accessibility specialist for agents, and Contrast and Control Borders preview overrides, and it fixes Accessibility Inspector in simulators ([Xcode 27 notes](https://developer.apple.com/documentation/xcode-release-notes/xcode-27-release-notes)).

## Only a handful of accessibility symbols are new in 27

The DocC review in [../os-27/api-availability.md](../os-27/api-availability.md) separates four groups:
- **New in 27.** Nine symbol families qualify:
  - `AccessibilitySettings.isApplicationAccessibilityEnabled` and its change notification.
  - `AXSpeechAttributeSSML`.
  - `MACaptionAppearanceDomain.videoConferencing`.
  - AVKit legible-option controls.
  - `AEAssessmentConfiguration` toggles for VoiceOver, Switch Control, Voice Control, Zoom and others (most macOS-only).
  - SwiftUI `GestureInputKinds`.
  - `XCUIVoiceOverService`.
  - PencilKit `PKStrokeRecognizer`.
  - `TabsPickerStyle`, with no watchOS entry ([TabsPickerStyle JSON](https://developer.apple.com/tutorials/data/documentation/swiftui/tabspickerstyle.json)).

  AppKit adds input and semantics symbols: `NSTextSelectionManager`, the segmented and toolbar roles, `preferredImageVisibility`, the gesture-relationship APIs and `NSStatusItem.expandedInterfaceSession`. `AVMediaCharacteristic.signLanguageInterpretationForAccessibility` is dated 27.1.
- **Older symbols with changed behavior in 27.** These are where WWDC most often misleads:
  - `accessibilityLinkedGroup` dates to iOS 14 but now links text navigation in iOS 27 ([WWDC26-219](https://developer.apple.com/videos/play/wwdc2026/219/), 7:59).
  - The tvOS Dynamic Type APIs date to tvOS 10 to 15 but now respond to a system setting.
  - `accessibilityShowBorders` has listed macOS 11 since its introduction, yet macOS 27 only now "also supports" it.
- **Added in 26.x.** The subtitle-preview APIs that session 256 presents as new shipped in 26.4.
- **Deprecated.** The caption adaptors and `allowsAccessibilitySpeech` are deprecated at 27.0. At **27.3**, SwiftUI's `ContentSizeCategory` and the legacy `.accessibility(label:)` modifier family are deprecated ([ContentSizeCategory JSON](https://developer.apple.com/tutorials/data/documentation/swiftui/contentsizecategory.json)).

**Apple's curated Accessibility updates page has no 2026 section** ([Accessibility updates](https://developer.apple.com/documentation/updates/accessibility)), so this delta is discoverable only symbol by symbol.

## Shipped features outrun the notes; four announcements stay pending

The matrix in [../os-27/shipping-constraints.md](../os-27/shipping-constraints.md) compares the May 19 announcement with Support evidence ([Apple Newsroom](https://www.apple.com/newsroom/2026/05/apple-unveils-new-accessibility-features-and-updates-with-apple-intelligence/)). Shipped:
- iOS 27.0 AI-assisted VoiceOver, Magnifier, Voice Control (English in the US, Canada, UK and Australia) and Accessibility Reader.
- Generated subtitles on iPhone and Mac. iPhone needs iPhone 15 Pro or later; Mac needs M1 or later.
- Look to Drive and the updated Dwell Control on visionOS 27.0.
- Face Gestures and Vehicle Motion Cues, documented only in the visionOS User Guide with an undated first version.
- Name Recognition in about 55 locales.
- tvOS Text Size.
- **The FaceTime third-party sign-language interpreter or live captioner, in 27.2 on iOS, macOS and visionOS.** It shipped as a system feature, not as the announced developer API. No interpreter symbol exists, and Apple staff said at WWDC that it was "not quite available in the iOS 27 beta" ([WWDC26-8005](https://developer.apple.com/videos/play/wwdc2026/8005/), 36:07).

**Still pending:**
- Touch Accommodations setup (PEND-01).
- MFi hearing-aid pairing and handoff (PEND-02).
- Sony Access controller support (PEND-03).
- Generated subtitles on Apple TV and Vision Pro (PEND-04), even though session 256 says tvOS and visionOS 27 support them.

Managed devices add a separate constraint. On macOS 27 the deprecated PPPC Accessibility key now notifies the user, and users can revoke management-granted accessibility permission ([macOS enterprise](https://support.apple.com/en-us/148830)).

Community evidence in [../os-27/community.md](../os-27/community.md) is never treated as contract. AppleVis's 27.0 editorial lists 26 VoiceOver bugs and calls four of them serious: stale announcements, ignored pronunciation entries, silence during Safari audio and silent Recovery diagnostics ([AppleVis editorial](https://mail.applevis.com/comment/215423)). No report confirms that any of them was fixed in 27.2.

## Thirty-three conflicts stay open, led by scope wording

[../os-27/conflicts.md](../os-27/conflicts.md) keeps every discrepancy rather than resolving it. The most consequential:
- **tvOS Larger Text scope.** The session promises scaling for "every app on the platform," while Support says only apps that support Dynamic Type adjust ([Apple TV guide](https://support.apple.com/guide/tv/display-bold-text-or-change-the-text-size-atvb0222141c/tvos)).
- **Zero `UIView` margins.** An Apple engineer's forum reply limits the change to iPhone Duo in 27.1 and all devices in 27.2. A practitioner saw it only when linking the 27.1 SDK, and the release note states no SDK gate ([forum 849929](https://developer.apple.com/forums/thread/849929)).
- **Radar 186015032.** WebKit's post lists it under Safari 27.2, while Apple places it in the 27.3 beta ([WebKit 27.2](https://webkit.org/blog/18515/webkit-features-for-safari-27-2/)).
- **`UIScene.extendStateRestoration`.** DocC lists tvOS 15.0, against a release note that frames the behavior as linked on the 27 SDK.
- **AVKit subtitles-on-mute.** The tvOS entry is labeled "Fixed:" yet says the logic "has not yet been updated."
- **Release-note names differ from DocC** for two AppKit gesture APIs.
- **Session 220's code sample** contains a typo.
- **The PPPC key.** Apple's account conflicts with an MDM blog's claim that the grant was removed.

The largest gaps are in [../os-27/backlog.md](../os-27/backlog.md):
- Apple-sourced public 27.0 builds.
- Verification of quotes that came through a summarizing fetch tool.
- iPadOS and macOS shipping evidence for the AI features.
- Full Safari and Xcode inventories.
- An `NSAccessibility` symbol diff.
- watchOS VoiceOver and haptics changes.
- About ten unreviewed WWDC transcripts, listed in [../os-27/wwdc.md](../os-27/wwdc.md).

## Conclusion

For accessibility, the main OS 27 story is the 27 SDKs. Moving an app to them silently changes trait propagation, menu imagery, text selection, window resizing and control implementations. Most adopted accessibility behavior therefore comes from rebuilding, not from new APIs, and a rebuild is the moment to audit. The AI-assisted features are real but gated by hardware, language and region, so guidance must still assume a user who has none of them and relies on good labels and ordinary navigation.

The evidence also shows which sources to trust for what. Apple's release notes undercount user-facing features, WWDC sessions overstate newness, and the curated updates pages omit the API delta. Only cross-checking DocC metadata, release notes and Support pages, with conflicts kept rather than resolved, produces claims safe to promote into guidance once baselines exist.

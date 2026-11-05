# macOS 27 changes

Third pass, 2026-11-05. Research only. macOS 27 "Golden Gate" release notes hold 296
entries (27.0: 272; 27.2: 9; 27.3 beta: 15), all in
[inventory/macos.md](inventory/macos.md). This page curates the accessibility and
interaction-relevant subset. No macOS 27.1 exists; the sequence is 27.0, 27.0.1 (26A434),
27.2 (26B123), 27.3 beta (26C5035r). See [releases.md](releases.md). Column key as on
[ios.md](ios.md).

## VoiceOver semantics and roles

| ID | Change | Release / status | SDK-linked | Tier | Source and locator | Older ID |
| --- | --- | --- | --- | --- | --- | --- |
| MAC-118 | New `NSToolbarItemGroup.role` and `NSSegmentedControl.role`, including `tabs`; such controls "are read by VoiceOver as 'tabs' and have a distinct visual appearance". DocC 27.0 (API-134/135). | 27.0 New Feature | No | Tier-1, release note + API declaration | [27.0 RN][m0] § AppKit, 162577742 | MAC-01; API-05; C-12 |
| MAC-309 | `TabsPickerStyle`: like `.segmented` "but VoiceOver reads it as 'tabs'"; distinct look on macOS. | 27.0 New Feature | No | Tier-1, release note + API declaration | [27.0 RN][m0] § SwiftUI, 173211711 | API-02; API-117 |
| MAC-307 | A `TabView` in an inspector looks like one in a sidebar; both use the `.tabs` picker style automatically. | 27.0 behavior change | Yes ("latest SDKs") | Tier-1, release note | [27.0 RN][m0] § SwiftUI, 170678002 | |
| MAC-330 | Fixed: a `Menu` with `.plain` or custom button style exposed AXDescription instead of AXTitle. | 27.0 Resolved | No | Tier-1, release note | [27.0 RN][m0] § SwiftUI, 171831601 | MAC-04 |
| MAC-325 | Fixed: `.grouped` form section backgrounds showed no border with the Show borders setting on. | 27.0 Resolved | No | Tier-1, release note | [27.0 RN][m0] § SwiftUI, 155906280 | MAC-04 |
| WWDC-121 | macOS 27 "also supports the 'show borders' environment value, just like iOS"; Liquid Glass adapts to Reduce Transparency and Increase Contrast. | 27.0 | n/a | Tier-1, transcript | [WWDC26-102](https://developer.apple.com/videos/play/wwdc2026/102/) 23:25 | API-111; C-14 |

## Keyboard navigation and focus

| ID | Change | Release / status | SDK-linked | Tier | Source and locator | Older ID |
| --- | --- | --- | --- | --- | --- | --- |
| MAC-124 | Fixed: open/save panel focus and tab order might skip fields, including the accessory view. | 27.0 Resolved | No | Tier-1, release note | [27.0 RN][m0] § AppKit, 43112307 | MAC-03 |
| MAC-133 | Fixed: "When full keyboard navigation is off, the keyboard loop might not traverse the correct fields and controls." | 27.0 Resolved | No | Tier-1, release note | [27.0 RN][m0] § AppKit, 169837566 | MAC-03 |
| MAC-115 | Recents list in open/save panels reachable with Command-Shift-F. | 27.0 New Feature | No | Tier-1, release note | [27.0 RN][m0] § AppKit, 120442314 | |
| MAC-116 | Window › Move & Resize and Full Screen Tile menus work on non-sheet open/save panels. | 27.0 New Feature | No | Tier-1, release note | [27.0 RN][m0] § AppKit, 150791154 | |
| MAC-331 / MAC-336 | Fixed: disabled default-action buttons stayed tinted (174278196); destructive default-action buttons in sheet toolbars did not look destructive (178957869). | 27.0 Resolved | No | Tier-1, release note | [27.0 RN][m0] § SwiftUI | |
| MAC-209 | Only the first hit-tested view hierarchy activates gesture recognizers; opt out with `NSView.exclusiveGestureBehavior` or `NSViewGestureRecognizerIsExclusive`; new key `NSGestureRecognizerSuppressesMainMenuActions` (wording differs from the AppKit updates page, C-19). | 27.0 New Feature + behavior change | No | Tier-1, release note | [27.0 RN][m0] § NSGestureRecognizer, 173551081 | API-140 |
| MAC-408 | Key view loop "to enable speed and accessibility": enable `.autorecalculatesKeyViewLoop` or maintain the loop yourself; keyboard navigation reaches the menu bar and status items; custom status-item windows should use the expanded interface session "so that keyboard focus can behave correctly". | 27.0 | n/a | Tier-1, transcript | [WWDC26-289](https://developer.apple.com/videos/play/wwdc2026/289/) 5:51–6:29, 6:34–8:22 | API-141 |

## Menus (behavior depends on the linked SDK)

| ID | Change | Release / status | SDK-linked | Tier | Source and locator | Older ID |
| --- | --- | --- | --- | --- | --- | --- |
| MAC-120 | Menu bar and context menus show a reduced set of item images; `NSMenu` hides symbol images by default; applies to apps linked on the macOS 26.0 SDK or later; new `NSMenuItem.preferredImageVisibility` (DocC 27.0). | 27.0 New Feature + behavior change | Yes | Tier-1, release note | [27.0 RN][m0] § AppKit, 170477566 | API-136; C-18 |
| MAC-139 | On the macOS 27 SDK both symbol and non-symbol images are hidden; earlier SDKs keep non-symbol images. | 27.0 Resolved | Yes | Tier-1, release note | [27.0 RN][m0] § AppKit, 179374305 | C-18 |
| MAC-140 | On the 27 SDK, images on items with empty title and attributed title are hidden; image-only items need `preferredImageVisibility`. | 27.0 Resolved | Yes | Tier-1, release note | [27.0 RN][m0] § AppKit, 179936632 | C-18 |
| MAC-306 | SwiftUI hides menu symbol images in most contexts; `.labelStyle(.titleAndIcon)` forces an icon. Also stated in WWDC26-269 3:32–3:46. | 27.0 New Feature + behavior change | Not stated | Tier-1, release note + transcript | [27.0 RN][m0] § SwiftUI, 170480710 | IPAD-01; MAC-410 |
| MAC-352 | Catalyst/iPadOS: menu elements show no images by default; new `UIMenuElement.preferredImageVisibility`. | 27.0 New Feature | Not stated | Tier-1, release note | [27.0 RN][m0] § UIKit, 170479084 | IPAD-01 |
| MAC-121 | NSTextView context menu moves Layout Orientation into the Font submenu. | 27.0 behavior change | Yes | Tier-1, release note | [27.0 RN][m0] § AppKit, 177605020 | |
| MAC-312 | `LabeledContent` in a `Menu` maps its value to the item subtitle. | 27.0 behavior change | Yes | Tier-1, release note | [27.0 RN][m0] § SwiftUI, 175594929 | |
| MAC-138 / MAC-333 / MAC-334 | Fixed: `highlightedItem` and other NSMenu APIs in context menus (178288949); "Settings…" icon (175053352); toolbar overflow crash with `NSHostingMenu` (177616606). | 27.0 Resolved | No | Tier-1, release note | [27.0 RN][m0] | |
| MAC-268 | "Ask Siri" might appear in context menus even when Siri is disabled. No workaround. | 27.0 Known Issue | No | Tier-1, release note | [27.0 RN][m0] § Siri, 176299524 | |

## Toolbars, windows and sheets

| ID | Change | Release / status | SDK-linked | Tier | Source and locator |
| --- | --- | --- | --- | --- | --- |
| MAC-122 | `NSTitlebarAccessoryViewController` may draw outside its bounds by default; may be clipped during reveal. | 27.0 behavior change | Yes | Tier-1, release note | [27.0 RN][m0] § AppKit, 180962967 |
| MAC-328 | `controlSize` and related environment values reset to defaults in sheets and popovers. | 27.0 behavior change | Yes | Tier-1, release note | [27.0 RN][m0] § SwiftUI, 167448274 |
| MAC-193 / MAC-195 | Catalyst app with no windows no longer creates one on switch (69906818); missing show/hide sidebar buttons fixed (176879915). | 27.0 | No | Tier-1, release note | [27.0 RN][m0] § Mac Catalyst |
| MAC-369 / MAC-164 | Fixed: window lost exiting full screen through Mission Control (177660206); Dock persisted in full screen (174992242). | 27.0 Resolved | No | Tier-1, release note | [27.0 RN][m0] |
| MAC-198 | Fixed: window controls in TV, Podcasts and Music stopped responding after dragging the playhead. | 27.0 Resolved | No | Tier-1, release note | [27.0 RN][m0] § Media Playback, 177984877 |
| MAC-207 | New `.disableScreenCornerInteractions` presentation option disables Hot Corners. | 27.0 New Feature | No | Tier-1, release note + API declaration | [27.0 RN][m0] § NSApplication, 168692527 |
| MAC-375 | External display settings might not be restored; arrangement may change. | 27.2 Known Issue | No | Tier-1, release note | [27.2 RN][m2] § Display Settings, 188643179 |
| MAC-376 | Clean installs might not prompt for notifications for some apps; workaround: System Settings > Notifications. | 27.2 Known Issue | No | Tier-1, release note | [27.2 RN][m2] § Notifications, 187312007 |

MAC-375 is pass-2 MAC-05.

## Text system

| ID | Change | Release / status | SDK-linked | Tier | Source and locator | Older ID |
| --- | --- | --- | --- | --- | --- | --- |
| MAC-119 | `NSTextSelectionManager` provides click, drag, shift-click and multi-click selection using gesture recognizers; `NSTextView` uses it; `mouseDown:` overrides keep working via a fallback. DocC 27.0. WWDC26-289 3:52–4:13 calls it "a new API in macOS 27". | 27.0 New Feature | No | Tier-1, release note + API declaration + transcript | [27.0 RN][m0] § AppKit, 163365571 | MAC-02; API-04; API-133 |
| MAC-127 / MAC-135 / MAC-126 | Fixed: selectable non-editable `NSTextField` drew outside bounds when truncating (118196071); `textColor = nil` color inconsistency (175095850); `NSTextContentManager` subclass instantiation (115247760). | 27.0 Resolved | No | Tier-1, release note | [27.0 RN][m0] § AppKit | |
| MAC-304 / MAC-323 | Selectable `Text` supports `TextRenderer` (158160386, 151015350). | 27.0 | Yes | Tier-1, release note | [27.0 RN][m0] § SwiftUI | |
| MAC-310 | `TextInputBorderShape`; `.squareBorder`/`.roundedBorder` soft-deprecated. | 27.0 New Feature | No | Tier-1, release note + API declaration | [27.0 RN][m0] § SwiftUI, 173362083 | API-143 |
| MAC-322 | `TextField` honors custom font and color on its prompt. | 27.0 Resolved | Yes | Tier-1, release note | [27.0 RN][m0] § SwiftUI, 86580365 | |

## SwiftUI controls no longer built on AppKit controls

| ID | Change | Release / status | SDK-linked | Tier | Source and locator |
| --- | --- | --- | --- | --- | --- |
| MAC-301 | Bordered `Menu` and `Picker` "no longer use `NSPopUpButton` in their implementation". | 27.0 behavior change | Not stated | Tier-1, release note | [27.0 RN][m0] § SwiftUI, 68559433 |
| MAC-311 | "On macOS, the `Slider` implementation no longer uses `NSSlider`." | 27.0 behavior change | Not stated | Tier-1, release note | [27.0 RN][m0] § SwiftUI, 173990195 |
| MAC-308 | Disabled `.checkbox` toggles no longer tinted, easier to tell from enabled. | 27.0 behavior change | Not stated | Tier-1, release note | [27.0 RN][m0] § SwiftUI, 172689844 |
| MAC-326 / MAC-335 | Fixed: glass buttons lacked hover outside toolbars (158800693); dragging a `Slider` could move the window (177790490). | 27.0 Resolved | No | Tier-1, release note | [27.0 RN][m0] § SwiftUI |
| MAC-332 | `List` accepts drops the same way as iOS. | 27.0 behavior change | Yes | Tier-1, release note | [27.0 RN][m0] § SwiftUI, 174628712 |

## Pointer, trackpad and gestures

| ID | Change | Release / status | SDK-linked | Tier | Source and locator | Older ID |
| --- | --- | --- | --- | --- | --- | --- |
| MAC-117 | `NSRefreshController` pull-to-refresh via `NSScrollView.refreshController`. | 27.0 New Feature | No | Tier-1, release note + API declaration | [27.0 RN][m0] § AppKit, 160867808 | API-137 |
| MAC-208 | Notes name `cancellableByScrollGesture`; DocC symbol is `isCancellableByScrollGesture`. | 27.0 New Feature | No | Tier-1, release note + API declaration | [27.0 RN][m0] § NSGestureRecognizer, 165650612 | API-139; C-02 |
| MAC-212 | Notes name `scrollGestureForFailureRelationship`; DocC is `scrollGestureForRelationships`, with min/max touches for scrolling. | 27.0 New Feature | No | Tier-1, release note + API declaration | [27.0 RN][m0] § NSScrollView, 164924201 | API-138; C-02 |
| MAC-210 / MAC-211 | Stuck gestures auto-cancel after input ends for a few seconds (175705302); diagnostic defaults (176396492). | 27.0 New Feature | No | Tier-1, release note | [27.0 RN][m0] § NSGestureRecognizer | |
| MAC-134 | `NSClickGestureRecognizer` with click count above 1 sends its action before the multi-click timeout (behavior wording under Resolved). | 27.0 Resolved (behavior; C-21) | No | Tier-1, release note | [27.0 RN][m0] § AppKit, 173975472 | |
| MAC-137 | Base `NSGestureRecognizer.locationInView:` returns `NSZeroPoint` and logs; subclasses must override. | 27.0 Resolved (behavior) | No | Tier-1, release note | [27.0 RN][m0] § AppKit, 176395420 | |
| MAC-355 | Fixed: Catalyst views with drag and context-menu interactions could not activate both by touch. | 27.0 Resolved | No | Tier-1, release note | [27.0 RN][m0] § UIKit, 175048540 | |
| MAC-406 | AppKit updates (June 2026): `NSControl` `Events` type, `beginDraggingSession(items:gesture:source:)`, Sidecar iPad touch recognizers (TN3212), `GestureInputKinds`, Info.plist keys `NSViewGestureRecognizerIsExclusive`, `NSIsTouchNative`, `NSGestureRecognizerSuppressesMainMenuActions`. Availability pending for three symbols. | 27.0 | n/a | Tier-1, API documentation (updates page) | [AppKit updates](https://developer.apple.com/documentation/updates/appkit) | API-121 |
| API-124 | Direct-touch system-gesture opt-outs for Mac touch input. | **27.3 beta** DocC | n/a | Tier-1, API declaration | [api-availability.md](api-availability.md) | |

## Assessment, managed devices and media

| ID | Change | Release / status | Tier | Source and locator | Older ID |
| --- | --- | --- | --- | --- | --- |
| MAC-143 | Finer-grained Automatic Assessment Configuration, with controls for the Dock, Menu Bar and accessibility settings. | 27.0 New Feature | Tier-1, release note | [27.0 RN][m0] § Automatic Assessment Configuration, 158132137 | API-120 |
| MAC-409 / WWDC-123 | Exams can manage accessibility-feature availability; Menu Bar and Dock hidden by default; a true property does not enable the feature; Switch Control quits if disallowed. | 27.0 | Tier-1, transcript | [WWDC26-230](https://developer.apple.com/videos/play/wwdc2026/230/) 3:00–4:27 | API-120 |
| SHIP-116 | Deprecated PPPC Accessibility key triggers a one-time notification per app; users can disable management-granted accessibility permissions. | 27.0 | Tier-1, Support (enterprise); quote needs verification | [148830](https://support.apple.com/en-us/148830) § Device management | C-07; COMM-126 |
| SHIP-06 | Managed Accessibility configuration controls Live Recognition on supervised devices. | 27 | Tier-1, support guide | [Deployment guide](https://support.apple.com/en-us/guide/deployment/depdc9488053/web) | SHIP-06 |
| SHIP-02 | Generated subtitles need macOS 27 and M1 or later; English. | 27.0 | Tier-1, support guide | [Mac captions guide](https://support.apple.com/en-us/guide/mac-help/mchlc1cb8d54/27/mac/27) | CROSS-04 |
| SHIP-115 | FaceTime third-party sign-language interpreter or live captioner. | 27.2 shipped | Tier-1, Support release note | [127257](https://support.apple.com/en-us/127257) § 27.2 › Other | SHIP-04 |
| IOS-416 (macOS) | Liquid Glass readability slider also listed for macOS. | 27.0 | Tier-1, Support release note | [127257](https://support.apple.com/en-us/127257) | |
| MAC-393 | Fixed: `CaptureInputSequenceProvider` assertion in a "Mac (Designed for iPad)" target. | **27.3 beta** Resolved | Tier-1, release note | [27.3 beta RN][m3] § Speech, 187921017 | MAC-06 |
| MAC-269 / MAC-255 | Siri cannot act on "photo one" by voice (Known, 176812955; workaround: picker or tap); fixed: disabling Siri might not have deleted Siri and Dictation history (Resolved, 177649865). | 27.0 | Tier-1, release note | [27.0 RN][m0] § Siri | |

## Liquid Glass and appearance

MAC-130 (`NSScrollView` scroll edge effect without visible scrollers, 159019809), MAC-131
(`NSSegmentedCell` placement under Liquid Glass, 168066807) and MAC-125 (Web Safe Colors in
right-to-left layouts, 107870015) are 27.0 Resolved, Tier-1 release notes. WWDC26-289
14:31–15:24 covers automatic hard scroll edges behind free-floating text, semibold sidebar
selection and a glass bounce-on-click effect for controls (MAC-408). WWDC26-269 2:35–3:24
covers pointer-tuned interactive glass and `appearsActive` (MAC-410).

## Negative findings

No release-note entries cover VoiceOver, Voice Control, Zoom, Full Keyboard Access, captions,
Increase Contrast or Reduce Transparency as features. No new `NSAccessibility` symbols were
found (API-130); Apple's Accessibility updates page has no 2026 section (MAC-407). WWDC26 has
no "What's new in AppKit" session. The macOS updates page lists no labeled accessibility item
for 27.0 (shipped-features notes; C-30 records the page-location discrepancy).

## Community evidence

COMM-124 (VoiceOver cursor not following Shift+Tab, macOS 27.0.1) and COMM-126 (PPPC forum
reports) are Tier-3 on [community.md](community.md). No AppleVis macOS 27 editorial was found.

## Research inference (not Apple-stated)

- The menu-image change is the likeliest macOS accessibility regression source: an
  image-only `NSMenuItem` with no title may leave VoiceOver users an empty item unless it
  has an accessibility label.
- SwiftUI `Slider`, bordered `Menu` and `Picker` no longer inherit AppKit AX roles, actions
  and keyboard handling (MAC-301, MAC-311); re-audit with VoiceOver, Full Keyboard Access and
  Voice Control.
- Gesture-based text selection (MAC-119) and exclusive hit-testing (MAC-209) may change how
  assistive pointer input such as Voice Control clicks and Dwell interacts with custom views.
- Most macOS 27 accessibility-relevant API work is semantic (tabs roles) or input-related,
  not new `NSAccessibility` members. A full symbol diff is pending.

[m0]: https://developer.apple.com/documentation/macos-release-notes/macos-27-release-notes
[m2]: https://developer.apple.com/documentation/macos-release-notes/macos-27_2-release-notes
[m3]: https://developer.apple.com/documentation/macos-release-notes/macos-27_3-release-notes

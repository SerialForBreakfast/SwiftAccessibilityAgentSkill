# tvOS 27 changes

Third pass, 2026-11-05. Research only. tvOS release notes hold 68 entries (27.0: 62; 27.2: 4;
27.3 beta: 2), all in [inventory/tvos.md](inventory/tvos.md). 27.2 and the 27.3 beta contain
only StoreKit Testing entries. No tvOS 27.1 exists. tvOS 27 runs on Apple TV 4K (2nd
generation and later); tvOS 26 also supported Apple TV HD (TV-183). Builds:
[releases.md](releases.md). Column key as on [ios.md](ios.md).

## Larger Text (system Text Size)

| ID | Change | Release / status | SDK-linked | Tier | Source and locator | Older ID |
| --- | --- | --- | --- | --- | --- | --- |
| TV-169 | Announced: "Larger Text support is coming to tvOS" for viewers with low vision. | announced 19 May 2026 | n/a | Tier-1, announcement | [Newsroom](https://www.apple.com/newsroom/2026/05/apple-unveils-new-accessibility-features-and-updates-with-apple-intelligence/) tvOS paragraph | TV-01 |
| TV-171 | Large Text is "now available, bringing system-wide text scaling to every app on the platform". | 27.0 | n/a | Tier-1, transcript | [WWDC26-221](https://developer.apple.com/videos/play/wwdc2026/221/) 0:12–0:20 | TV-01; C-01 |
| TV-172 | Developers can indicate Larger Text support in Accessibility Nutrition Labels for tvOS. | 27.0 | n/a | Tier-1, transcript | WWDC26-221 0:40–0:43, 9:46 | WWDC-115 |
| TV-173 / TV-174 | "Dynamic Type works the same way on tvOS"; Settings > Accessibility > Display > Text Size; sizes from Large (default) up to Accessibility XXXL. | 27.0 | n/a | Tier-1, transcript | WWDC26-221 1:21–1:49 | WWDC-116; C-28; C-29 |
| TV-175 | Standard UIKit and SwiftUI components (labels, buttons, navigation and tab bars) scale automatically; custom elements need updating. | 27.0 | n/a | Tier-1, transcript | WWDC26-221 2:31–2:43 | |
| TV-176 / TV-177 | Avoid fixed font sizes and hard-coded frames; use `.caption` and `.frame(maxWidth: .infinity)`; UIKit `preferredFont(forTextStyle: .headline)` with `adjustsFontForContentSizeCategory = true`. | 27.0 | n/a | Tier-1, transcript | WWDC26-221 2:54–3:15, 4:56–5:24, 5:55–6:08 | API-110 |
| TV-178 / TV-179 | Grids switch column count on `dynamicTypeSize.isAccessibilitySize` with `containerRelativeFrame`; consider a marquee for long titles; cards flip axis with `AnyLayout` or `UIStackView.axis` on `isAccessibilityCategory`. | 27.0 | n/a | Tier-1, transcript | WWDC26-221 6:25–7:26, 8:03–8:49 | API-110 |
| TV-180 | Chapters 0:01, 2:46, 6:13; resources "Applying custom fonts to text" and "Scaling fonts automatically"; `UIFontMetrics` not named (DocC tvOS 11.0). | 27.0 | n/a | Tier-1, transcript | WWDC26-221 metadata | API-146 |
| TV-181 | Settings > Accessibility > Display has Bold Text and Text Size; "Apps that support Dynamic Type automatically adjust to the Text Size setting." | tvOS 27 | n/a | Tier-1, support guide | [Text size guide](https://support.apple.com/guide/tv/display-bold-text-or-change-the-text-size-atvb0222141c/tvos) | SHIP-111; C-01 |
| TV-182 | "You can now adjust the text size across all apps that support Dynamic Text on Apple TV 4K." Also redesigned Podcasts and Music apps. | tvOS 27 | n/a | Tier-1, support guide | [What's new in tvOS 27](https://support.apple.com/guide/tv/whats-new-in-tvos-27-atvb457e13ae/27/tvos/27) | C-01; C-29 |
| TV-184 | Pre-existing text aids remain: Hover Text, Zoom, subtitle settings, closed captions/SDH, VoiceOver settings. | existing | n/a | Tier-1, support guide | [Apple TV 4K User Guide TOC](https://support.apple.com/guide/tv/welcome/tvos) | |

## Focus, controls and VoiceOver semantics

| ID | Change | Release / status | SDK-linked | Tier | Source and locator | Older ID |
| --- | --- | --- | --- | --- | --- | --- |
| TV-102 | Fixed: Apple TV app sidebar focus highlight briefly appeared flat on the right side. Only focus-engine entry. | 27.0 Resolved | No | Tier-1, release note | [27.0 RN][t0] § Apple TV, 177389941 | TV-03 |
| TV-140 | `TabsPickerStyle` "similar to the `.segmented` style, but VoiceOver reads it as 'tabs'". DocC tvOS 27.0. | 27.0 New Feature | No | Tier-1, release note + API declaration | [27.0 RN][t0] § SwiftUI, 173211711 | TV-02; API-02; API-117 |
| TV-151 | Buttons no longer automatically use the asset-catalog accent color as label tint when building against the tvOS 27 SDK. | 27.0 Resolved (behavior) | Yes | Tier-1, release note | [27.0 RN][t0] § SwiftUI, 171830912 | |
| TV-150 | "Fixed:" Menu labels cannot contain controls, gesture views or representables with gesture recognizers. | 27.0 Resolved (rule; C-21) | No | Tier-1, release note | [27.0 RN][t0] § SwiftUI, 169091260 | |
| TV-148 | `containerRelativeFrame` safe-area insets on a ScrollView's non-scrollable axis fixed. Used by the WWDC26-221 grid technique. | 27.0 Resolved | Yes | Tier-1, release note | [27.0 RN][t0] § SwiftUI, 165913417 | |
| TV-149 | Control environment values reset to defaults in sheets and popovers. | 27.0 Resolved (behavior) | Yes | Tier-1, release note | [27.0 RN][t0] § SwiftUI, 167448274 | |
| TV-142 | `LabeledContent` in a `Menu` maps its value to the menu-item subtitle. | 27.0 New Feature | Yes | Tier-1, release note | [27.0 RN][t0] § SwiftUI, 175594929 | |
| TV-141 | `TextInputBorderShape`; DocC tvOS 27.0. | 27.0 New Feature | No | Tier-1, release note + API declaration | [27.0 RN][t0] § SwiftUI, 173362083 | API-143 |
| TV-146 | Data-item and error-based `alert` and `confirmationDialog` back-deploy to tvOS 15.0. | 27.0 New Feature | No | Tier-1, release note | [27.0 RN][t0] § SwiftUI, 179388848 | |
| XCODE-113 | Xcode agents can verify tvOS apps by moving focus with the Siri Remote. | Xcode 27.0 | n/a | Tier-1, release note | [Xcode 27 RN](https://developer.apple.com/documentation/xcode-release-notes/xcode-27-release-notes) § Coding Intelligence, 183317784 | |

## Media and captions

| ID | Change | Release / status | SDK-linked | Tier | Source and locator | Older ID |
| --- | --- | --- | --- | --- | --- | --- |
| TV-103 | Listed as Fixed: subtitles may not enable or disable as expected when muting or unmuting; the same text says the logic "has not yet been updated to account for the new system behavior". | 27.0 Resolved (wording conflict) | No | Tier-1, release note | [27.0 RN][t0] § AVKit Video Playback, 177086166 | C-05 |
| TV-170 | Announced: generated subtitles appear automatically for uncaptioned video on Apple TV, among others; English U.S./Canada footnote. | announced | n/a | Tier-1, announcement | [Newsroom](https://www.apple.com/newsroom/2026/05/apple-unveils-new-accessibility-features-and-updates-with-apple-intelligence/) | TV-04 |
| WWDC-118 | English subtitles from English audio "also supported on tvOS and visionOS 27"; translation iOS/macOS only. | 27.0 (WWDC claim) | n/a | Tier-1, transcript | [WWDC26-256](https://developer.apple.com/videos/play/wwdc2026/256/) 4:18 | TV-04; CROSS-04; C-11; PEND-04 |
| API-113 / API-114 | `AVLegibleMediaOptionsMenuController` has no tvOS entry; `AVCaptionRenderer` is tvOS 26.4. | 26.4 APIs | n/a | Tier-1, API declaration | [api-availability.md](api-availability.md) | C-13 |
| TV-161 / TV-162 | VideoToolbox low-latency scaler 1.5x and frame interpolation up to 1080p. | 27.0 New Feature | No | Tier-1, release note | [27.0 RN][t0] § VideoToolbox | |

## Scenes and life cycle

| ID | Change | Release / status | SDK-linked | Tier | Source and locator | Older ID |
| --- | --- | --- | --- | --- | --- | --- |
| TV-157 | "When linked on iOS 27, tvOS 27, …" `UIScene.extendStateRestoration` / `completeStateRestoration` extend restoration across background-to-foreground transitions. DocC lists tvOS 15.0. | 27.0 New Feature | Yes | Tier-1, release note | [27.0 RN][t0] § UIKit, 161843040 | IOS-02; API-145; C-04 |
| TV-158 | Apps built with the latest SDK "must adopt the scene-based life cycle or they fail to launch". | 27.0 Deprecation + behavior change | Yes | Tier-1, release note | [27.0 RN][t0] § UIKit, 141837548 | |

## Not found in Apple sources

No WWDC26 tvOS focus-engine or Siri Remote input changes; no tvOS VoiceOver changes; no
Apple statement on whether `AVPlayerViewController` panels scale with Text Size or whether
caption size follows it; no "About tvOS 27 Updates" page; no tvOS-specific hardware limit for
Larger Text beyond the tvOS 27 floor. tvOS 27.2 reportedly added ASL and BSL versions of some
Apple TV app titles (Tier-3 snippet, content not a setting).

## Community evidence

TV-185 (Tier-2: some major streaming apps do not use Apple's UI frameworks and may not
respond to Larger Text) and TV-186 (Tier-3 snippet: AppleVis release post). See
[community.md](community.md).

## Research inference (not Apple-stated)

- Treat Larger Text as automatic for system UI and standard components, adoption-dependent
  for custom text (C-01). Because sizes start at the default Large, layout testing should
  focus on `isAccessibilitySize`.
- TV-151 (button tint) and TV-148 (`containerRelativeFrame`) interact with Larger Text grids
  and focus visuals in 27-SDK builds; re-check focus-state contrast.
- The scene-life-cycle mandate (TV-158) is the highest-impact UIKit change for tvOS apps.
- Separate text scaling from remote focus, selection and scroll reachability.

[t0]: https://developer.apple.com/documentation/tvos-release-notes/tvos-27-release-notes

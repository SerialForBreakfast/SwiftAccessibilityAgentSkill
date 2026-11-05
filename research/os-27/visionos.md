# visionOS 27 changes

Third pass, 2026-11-05. Research only. visionOS release notes hold 168 entries (27.0: 160 in
53 sections; 27.2: 6; 27.3 beta: 2), all in [inventory/visionos.md](inventory/visionos.md).
None describes a user-facing accessibility feature; those are documented only on Apple
Support. No visionOS 27.1 exists. Builds: 27.0.1 24M372, 27.2 24N120, 27.3 beta 24N5286r
([releases.md](releases.md)). Devices: Apple Vision Pro (all models). The visionOS notes
used their own tier scheme (Newsroom and WWDC as T2); here Newsroom is Tier-1 announcement
and WWDC is Tier-1 transcript. Column key as on [ios.md](ios.md).

## Alternative input and gaze (Apple Support, shipped)

| ID | Change | Release / status | Tier | Source and locator | Older ID |
| --- | --- | --- | --- | --- | --- |
| VISION-283 | Look to Drive "enables you to control a compatible powered wheelchair with your eyes". | 27.0 shipped | Tier-1, Support release note | [149067](https://support.apple.com/en-us/149067) § visionOS 27 › Accessibility | VISION-05; SHIP-03; SHIP-107; ANN-04 |
| VISION-289 | Look to Drive works with a TOLT Technologies or LUCI controller, only for compatible systems in the U.S. and U.S. territories; Guest User sessions supported. | 27.0 | Tier-1, support guide | [Use Look to Drive](https://support.apple.com/guide/apple-vision-pro/use-look-to-drive-tan5f0e3ad72/visionos) intro | SHIP-107 |
| VISION-290 | TOLT via Developer Strap (USB-C), LUCI via Bluetooth; requires Dwell Control, Switch Control or AssistiveTouch on; Settings > Accessibility > Wheelchair (control row position; logging 1 hour, 24 hours, never). | 27.0 | Tier-1, support guide | same, § Set up Look to Drive | |
| VISION-291 | Controlled environments only, never near traffic; "An adult trusted supporter should be present and attentive during each session"; not on wall power; unavailable at 10% battery or below. | 27.0 | Tier-1, support guide | same, § Important / Before you begin | VISION-304 |
| VISION-292 | Eyes only (pinches do not start or stop motion); stop by looking at Stop, Pause or Exit or closing eyes longer than a blink; no emergency calls; auto-stops on disconnect, removal, low charge, power loss or malfunction. | 27.0 | Tier-1, support guide | same, § driving controls | |
| VISION-284 | Updated Dwell Control: glance at a selection marker above the dwell pointer to confirm instead of waiting for a timer. | 27.0 shipped | Tier-1, Support release note | [149067](https://support.apple.com/en-us/149067) § visionOS 27 › Accessibility | SHIP-03; SHIP-108; ANN-04 |
| VISION-293 | Dwell Control options: Long Look to Tap and Glance Up to Tap; plus Highlight Control, Keyboard, Pause During Media Playback, Show Scroll Controls, Menu Follow. | 27.0 | Tier-1, support guide | [Perform actions with your eyes](https://support.apple.com/guide/apple-vision-pro/perform-actions-with-your-eyes-tan0ba69a1f1/visionos) | |
| VISION-294 | Face Gestures: a facial expression such as a smile or raised eyebrows performs a tap or custom command; Slight, Default or Exaggerated; usable as a Switch Control switch. | 27.x guide; first version inferred 27.0 | Tier-1, support guide | [Face gestures](https://support.apple.com/guide/apple-vision-pro/perform-actions-with-face-gestures-tan6a3f9c0e3/visionos) | SHIP-109; C-24 |
| VISION-295 | Vehicle Motion Cues: animated edge dots only when vehicle motion is detected and Travel Mode is on; not for situations requiring attention to safety. | 27.x guide; first version inferred 27.0 | Tier-1, support guide | [Vehicle Motion Cues](https://support.apple.com/guide/apple-vision-pro/use-vehicle-motion-cues-tan6a3f9c0e5/visionos) | SHIP-110; C-24 |
| VISION-296 / VISION-297 | Pointer Control lets you "use your eyes, head, wrist, or finger as a pointer"; Eye Input can be both eyes, left only or right only. | existing; newness unknown | Tier-1, support guide | [Pointer Control](https://support.apple.com/guide/apple-vision-pro/use-a-pointer-to-navigate-tan3869c8a85/visionos); [Eye Input](https://support.apple.com/guide/apple-vision-pro/eye-input-tan88016cfa4/visionos) | |
| VISION-286 | Look-to-talk Siri ("Just look at Siri and start speaking"); Siri AI requires Apple Vision Pro with M2 and later. | 27.0 shipped | Tier-1, Support release note | [149067](https://support.apple.com/en-us/149067) § Siri AI | |
| VISION-287 | "Look to see notifications": glance at a notification to expand it. | 27.0 shipped | Tier-1, Support release note | [149067](https://support.apple.com/en-us/149067) § System Improvements | |

## Hearing, captions and communication

| ID | Change | Release / status | Tier | Source and locator | Older ID |
| --- | --- | --- | --- | --- | --- |
| VISION-285 | "FaceTime supports adding a third party sign language interpreter or live captioner to a call." Not in the 27.2 developer notes. | 27.2 shipped | Tier-1, Support release note | [149067](https://support.apple.com/en-us/149067) § visionOS 27.2 › Other | VISION-06; SHIP-04; SHIP-115; C-22; C-23 |
| VISION-299 | Live Captions transcribe app audio and nearby conversation; "you can't record or mirror your view" while on; not all languages or regions. | existing | Tier-1, support guide | [Live captions](https://support.apple.com/guide/apple-vision-pro/live-captions-tan0b3d5c0c9/visionos) | |
| VISION-300 | Subtitles & Captioning covers Closed Captions + SDH and Style; no mention of generated subtitles. | visionOS 27 guide | Tier-1, support guide | [Subtitles and captions](https://support.apple.com/guide/apple-vision-pro/subtitles-and-captions-tan0201bdfb1/visionos) | VISION-04; PEND-04; C-11 |
| VISION-280 | Announced: generated subtitles on Apple Vision Pro; English U.S./Canada footnote. | announced | Tier-1, announcement | [Newsroom](https://www.apple.com/newsroom/2026/05/apple-unveils-new-accessibility-features-and-updates-with-apple-intelligence/) | VISION-04 |
| VISION-302 | MFi hearing aids pair from Settings > Accessibility > Hearing Devices with automatic switching; page not marked new. | existing | Tier-1, support guide | [Hearing devices](https://support.apple.com/guide/apple-vision-pro/use-hearing-devices-tan0654b02b7/visionos) | PEND-02 |
| VISION-160 | Fixed: subtitles might be clipped when resizing Multiview tiles in the TV app. | 27.0 Resolved | Tier-1, release note | [27.0 RN][v0] § RealityKit, 181267166 | |

## Vision and VoiceOver (Apple Support)

| ID | Change | Release / status | Tier | Source and locator |
| --- | --- | --- | --- | --- |
| VISION-301 | VoiceOver Image Explorer describes people, objects, text and tables with finger-pinch gestures; Live Recognition describes scenes with an "Ask" question and outputs speech, braille or sounds. Newness in 27 not dated. | visionOS 27 guide | Tier-1, support guide | [VoiceOver for images](https://support.apple.com/guide/apple-vision-pro/use-voiceover-for-images-and-videos-tan37e18e5f9/visionos); [Live Recognition](https://support.apple.com/guide/apple-vision-pro/get-live-descriptions-with-live-recognition-tanb4e29f7a1/visionos) |
| VISION-298 | Zoom: Full Screen or Window Zoom; include apps, surroundings or both; works with VoiceOver. | existing | Tier-1, support guide | [Zoom](https://support.apple.com/guide/apple-vision-pro/zoom-tan563db5e24/visionos) |
| VISION-303 | Accessibility TOC lists Vehicle Motion Cues, face gestures, Look to Drive, Pointer Control, Live captions, Digital Prism Correction. | visionOS 27 guide | Tier-1, support guide | [Accessibility TOC](https://support.apple.com/guide/apple-vision-pro/get-started-with-accessibility-features-tan426c48bdc/visionos) |
| VISION-320 | visionOS 27 security notes acknowledge a VoiceOver report (Hariji Vivek Pandey). | 27.0 | Tier-1, Support (security) | [149038](https://support.apple.com/en-us/149038) § Additional recognition |

## Developer release-note entries

| ID | Change | Release / status | SDK-linked | Tier | Source and locator | Older ID |
| --- | --- | --- | --- | --- | --- | --- |
| VISION-114 | Eye tracking may degrade after Eye Setup on 27.0 Beta 1–4; redo eye and hand setup on Beta 5 or later. | 27.0 Known Issue (historical beta) | No | Tier-1, release note | [27.0 RN][v0] § Eye Setup, 175305506 | VISION-01; VISION-273 |
| VISION-140 | Fixed: annotation-window buttons in Quick Look might lose focus and become unresponsive on the first pinch. | 27.0 Resolved | No | Tier-1, release note | [27.0 RN][v0] § Quick Look, 172214657 | VISION-02 |
| VISION-147 | Fixed: `.highlight` hover effect highlighted the whole entity hierarchy during direct interactions. | 27.0 Resolved | No | Tier-1, release note | [27.0 RN][v0] § RealityKit, 158462269 | VISION-275 |
| VISION-169 | Activate Siri by looking at the Siri orb and speaking (enabled in Beta 2). Known-issue workaround for Environments commands: "Use gaze and pinch" (178082773). | 27.0 New Feature | No | Tier-1, release note | [27.0 RN][v0] § Siri, 177137200 | VISION-276 |
| VISION-172 / VISION-183 | Fixed: Type to Siri image drag-and-drop (176312944); search field keeps keyboard focus after back navigation (178191950). | 27.0 Resolved | No | Tier-1, release note | [27.0 RN][v0] § Siri | |
| VISION-223 | `TabsPickerStyle`, "similar to the `.segmented` style, but VoiceOver reads it as 'tabs'". DocC visionOS 27.0. | 27.0 New Feature | No | Tier-1, release note + API declaration | [27.0 RN][v0] § SwiftUI, 173211711 | VISION-274; VISION-310; API-117 |
| VISION-225 | `LabeledContent` in a `Menu` maps its value to the menu-item subtitle. | 27.0 New Feature | Yes | Tier-1, release note | [27.0 RN][v0] § SwiftUI, 175594929 | |
| VISION-236 / VISION-237 | `containerRelativeFrame` safe-area fix (165913417); control modifiers reset in sheets and popovers (167448274). | 27.0 Resolved | Yes | Tier-1, release note | [27.0 RN][v0] § SwiftUI | |
| VISION-248 | `UIScene.extendStateRestoration` / `completeStateRestoration` when linked on visionOS 27. | 27.0 New Feature | Yes | Tier-1, release note | [27.0 RN][v0] § UIKit, 161843040 | IOS-02; C-04 |
| VISION-251 | Apps built with the latest SDK must adopt the scene-based life cycle "or they fail to launch". | 27.0 Deprecation | Yes | Tier-1, release note | [27.0 RN][v0] § UIKit, 141837548 | |
| VISION-261 | 3D objects opened from Safari might reposition unexpectedly when moved. | 27.2 Known Issue | No | Tier-1, release note | [27.2 RN][v2] § Quick Look, 187035825 | VISION-03 |
| VISION-262 | Siri might become unresponsive when asking ChatGPT with ChatGPT off; workaround: force quit Siri, turn on ChatGPT. | 27.2 Known Issue | No | Tier-1, release note | [27.2 RN][v2] § Siri AI, 189382856 | |
| VISION-257–259 | WebKit `<model>` fixes: off-center or hidden models, darker in Dark Mode, cross-platform rendering differences. | 27.0 Resolved | No | Tier-1, release note | [27.0 RN][v0] § WebKit | |

The remaining SDK-linked 27.0 entries (VISION-151, 218, 221, 222, 230, 231) and behavior notes
under Resolved (VISION-146, 151, 159, 188, 240, 241, 242; C-21) are in the inventory.

## Spatial accessibility APIs

No new spatial-accessibility API was found in 27 (VISION Q3). RealityKit
`AccessibilityComponent` lists visionOS with no `introducedAt` (pending; API-148);
`HoverEffectComponent` and `InputTargetComponent` are visionOS 1.0 (API-149); SwiftUI hover
and accessibility modifiers are visionOS 1.0 (API-150). New 27.0 symbols on visionOS:
`TabsPickerStyle` and `textInputBorderShape(_:)` (VISION-310). There is no public API to
detect Look to Drive, Glance Up to Tap or Face Gestures. HIG: visionOS default control size
60×60 pt, minimum 28×28 pt (VISION-311); immersive-space guidance warns that head-anchored
content prevents use of Pointer Control (VISION-312); the HIG accessibility change log ends
9 June 2025 (VISION-313).

## WWDC26

No dedicated visionOS accessibility session. VISION-316 (8005 lab, 57:32–58:14): Pointer
Control as the gaze alternative. VISION-317 (8004 lab, 54:48–55:12): wheelchair control is
part of visionOS 27. Sessions 287, 279 and 234 had no substantive accessibility content
(VISION-318). Index: [wwdc.md](wwdc.md).

## Research inference (not Apple-stated)

- Look to Drive is a layer over Dwell Control, Switch Control or AssistiveTouch, not a
  standalone input mode.
- Live Captions blocks recording and mirroring, so it cannot be combined with the 27.0
  High Quality Recording feature.
- Standard labels, actions and hover effects remain the developer's main lever, because the
  new input features run through the system accessibility layer.
- The "earlier session" in VISION-316 is likely WWDC23 "Create accessible spatial
  experiences"; unverified.

[v0]: https://developer.apple.com/documentation/visionos-release-notes/visionos-27-release-notes
[v2]: https://developer.apple.com/documentation/visionos-release-notes/visionos-27_2-release-notes

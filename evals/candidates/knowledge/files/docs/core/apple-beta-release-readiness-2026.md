# Apple Beta and Release Readiness Notes

Refresh note (2026-11-04): historical discovery notes are preserved below. Consult [the source refresh ledger](source-refresh-2026-11.md) for claim-level review status and stable/beta distinctions before using these notes as current guidance.

Last updated: 2026-09-01

Status: Release-readiness planning artifact.

Purpose: Summarize what current Apple beta release notes, WWDC26 sessions, and changelog-style materials suggest Swift Accessibility Agent should anticipate for upcoming platform releases.

## Source Posture

This document is for planning and evaluation. Convert items into accepted implementation guidance only after the relevant Apple release notes, API documentation, or WWDC sessions are stable enough to cite from the source registry.

Use `Freshness: MEDIUM` when answering from this document unless the specific claim is also supported by a finalized guideline or current Apple documentation.

## Near-Term Signals

| Area | Source Signal | What We Can Anticipate | Agent Implication |
| --- | --- | --- | --- |
| tvOS Dynamic Type / Larger Text | WWDC26 has a dedicated "Prepare your tvOS apps for Dynamic Type" session. tvOS 27 adds system-wide Larger Text support with sizes from Large through Accessibility XXXL. | tvOS accessibility guidance needs first-class text scaling coverage, not just focus/navigation coverage. | Add a tvOS Larger Text guideline and promptfoo cases. Review for hard-coded fonts, fixed widths/heights, shelf/card truncation, and layouts that need fewer visible columns at large sizes. |
| Accessibility Nutrition Labels | tvOS 26 and visionOS 26 release notes add an App Store accessibility section for apps and games. | Teams will need help making support claims that map to real app behavior and evidence. | Add release-readiness guidance that connects labels to evidence, without encouraging unsupported marketing claims. |
| Generated subtitles and subtitle styles | WWDC26 covers generated subtitles, subtitle translation, authored subtitles, AVKit / AVPlayerLayer / Media Accessibility integration, and subtitle style preview. | Media accessibility guidance needs to distinguish authored captions from generated subtitles and style preview. | Update media guidelines so authored subtitles remain preferred where available, generated subtitles fill gaps, and custom players expose selection plus style preview where appropriate. |
| Custom controls | WWDC26 "Refine accessibility for custom controls" emphasizes labels, values, traits, actions, feedback, direct touch, passthrough gestures, and multiple input methods. | Custom controls need stronger guidance across SwiftUI/UIKit/AppKit, especially around direct-touch surfaces and alternate actions. | Strengthen custom-control docs and rotor/action guidance. Add prompts that ask in user language about draggable, gesture-heavy, or playful controls. |
| Reading apps and custom text | WWDC26 "Enhance the accessibility of your reading app" emphasizes standard text views, text selection, edit rotor custom actions, Accessibility Reader, and `UITextInput` for custom-rendered text. | Reading/document apps need deeper coverage than generic labels and Dynamic Type. | Add a reading/content topic for standard text views, custom text rendering, text selection, edit rotor actions, and Accessibility Reader compatibility. |
| TextKit directionality and text tables | iOS/iPadOS/tvOS/visionOS/macOS 26 and 27 release notes include TextKit changes around natural alignment, base writing direction, indentation directionality, and `NSTextTable` availability for UIKit clients. | Internationalization and rich text behavior can affect accessibility reading order, layout, tables, and bidirectional text. | Add source-registry tracking and promptfoo cases for RTL/natural alignment, text tables, and custom text layout. |
| SwiftUI tabs and menus | iOS/iPadOS 27 release notes add `TabsPickerStyle`, with VoiceOver reading it as tabs, and adjust default menu icon visibility. | Role accuracy and menu semantics are shifting in ways agents should know. | Add SwiftUI/UIKit guidance for navigation vs value-selection pickers, menu image visibility, and accessible meaning when icons are hidden. |
| iPad continuous resizing | iOS/iPadOS 27 release notes include several iPad resize/orientation known issues and behavior changes. | iPad accessibility testing should include resizable windows, orientation, and clipped/truncated large-text states. | Expand testing matrix prompts and ViewLens runtime-evidence scenarios for resizing and orientation. |
| UIKit scene lifecycle and state restoration | iOS/tvOS/visionOS 27 release notes add `UIScene.extendStateRestoration` and `UIScene.completeStateRestoration`; latest SDKs require scene-based lifecycle. | Focus restoration and modal/state continuity become more important in scene transitions. | Add regression-triage prompts for scene restoration, background/foreground transitions, modal focus restoration, and assistive-technology continuity. |
| Xcode 27 agent support | Xcode 27 beta notes include plugin skills, MCP support, Agent Client protocol, first-class planning artifacts, Preview Snapshot MCP variants, specialist skills, and coding-agent filesystem controls. | This skill should remain installer-neutral but be ready for Xcode agent/plugin workflows. | Keep `npx skills` first-class, maintain Xcode compatibility docs, and consider an optional Xcode plugin packaging path when the release stabilizes. |
| Xcode Preview Snapshot variants | Xcode 27 beta notes say Preview Snapshot MCP can render variants such as light/dark, orientation, and type-size overrides; later notes add platform/device/OS metadata. | Agent evaluations can ask Xcode/ViewLens for richer UI evidence without screenshot-only assumptions. | Add optional C3-style evals later for preview snapshot/type-size evidence and make provenance visible in answers. |
| Xcode Device Hub limitations | Xcode beta notes mention VoiceOver toggles and larger text UI limitations in Device Hub/appearance inspector. | Automated beta testing may need workarounds and should not assume toggles always reflect runtime assistive-tech state. | Track known tool limitations in regression guidance; prefer explicit device/simulator setting evidence where possible. |
| Xcode Coding Assistant accessibility fixes | Xcode 26/27 notes include fixes for Coding Assistant button labels and VoiceOver trapping. | The agent ecosystem itself is an accessibility surface. | Add user-experience evals for whether installed skills and agent outputs are usable with VoiceOver, keyboard, and readable routing/source paths. |

## What To Do Next

1. Create a tvOS Larger Text guideline.
2. Update media guidance for generated subtitles, subtitle selection UI, authored subtitle preference, and subtitle style preview.
3. Add custom-control guidance for direct touch, passthrough gestures, custom actions, and feedback.
4. Add a reading-app/content guideline covering standard text views, custom-rendered text, text selection, edit rotor actions, and Accessibility Reader.
5. Add source-registry entries for the specific WWDC26 sessions and release-note pages.
6. Add promptfoo gold prompts for tvOS Larger Text, generated subtitles, custom controls, reading apps, scene restoration, and Xcode agent/plugin usage.
7. Add ViewLens/evidence prompts for preview snapshots, Dynamic Type matrices, focus graphs, and before/after verification.

## Promptfoo Candidates

- "My Apple TV app uses fixed-size title labels and movie poster cards. What will break with the new Larger Text support?"
- "If Apple can generate subtitles automatically, should my app still ship authored captions?"
- "My custom game control works by dragging and pinching. How should VoiceOver or Switch Control users operate it?"
- "My reading app renders pages as images for typography. How do I make the text accessible?"
- "What should I check when a menu icon disappears but the command still needs to be understandable?"
- "A scene restores after backgrounding, but VoiceOver focus lands in the wrong place. What should I test?"
- "Can Xcode Preview Snapshot type-size variants replace runtime accessibility testing?"
- "How should this skill work inside Xcode now that Xcode supports plugins, skills, and MCP?"

## Agent Answering Policy

When using this document:

- Say whether the claim comes from beta release notes, WWDC sessions, or accepted repo guidance.
- Use assumptions for beta behavior, preview-only APIs, and tool limitations.
- Do not claim final API behavior until release notes/API docs stabilize.
- Do not treat generated subtitles, visual intelligence, or preview snapshots as substitutes for app-owned semantics and captions.
- Prefer action-oriented recommendations that developers can test before the final OS release.

## Sources

- tvOS 27 release notes: https://developer.apple.com/documentation/tvos-release-notes/tvos-27-release-notes
- iOS & iPadOS 27 release notes: https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-27-release-notes
- macOS 27 release notes: https://developer.apple.com/documentation/macos-release-notes/macos-27-release-notes
- visionOS 27 release notes: https://developer.apple.com/documentation/visionos-release-notes/visionos-27-release-notes
- Xcode 27 release notes: https://developer.apple.com/documentation/xcode-release-notes/xcode-27-release-notes
- Xcode 26.6 release notes: https://developer.apple.com/documentation/xcode-release-notes/xcode-26_6-release-notes
- WWDC26: Prepare your tvOS apps for Dynamic Type: https://developer.apple.com/videos/play/wwdc2026/221/
- WWDC26: Discover generated subtitles and subtitle styles: https://developer.apple.com/videos/play/wwdc2026/256/
- WWDC26: Refine accessibility for custom controls: https://developer.apple.com/videos/play/wwdc2026/220/
- WWDC26: Enhance the accessibility of your reading app: https://developer.apple.com/videos/play/wwdc2026/219/
- WWDC26 video index: https://developer.apple.com/videos/wwdc2026/

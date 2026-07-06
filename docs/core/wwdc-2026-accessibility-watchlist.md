# WWDC 2026 Accessibility Feature Watchlist

Last updated: 2026-07-06

Status: Watchlist, not accepted implementation guidance.

Purpose: Track newly previewed Apple accessibility features that may affect Swift Accessibility Agent routing, guidelines, testing, and promptfoo evaluation.

## Source Posture

Use this document as a discovery and planning artifact. Prefer Apple developer documentation and release notes before turning any item here into prescriptive implementation guidance.

Current source confidence:

- High for feature existence where Apple Newsroom announced the capability.
- Medium for developer impact where public API behavior, framework integration, or third-party adoption details are not yet documented.
- Medium for community analysis from press coverage. Use commentary to identify questions, not to override Apple documentation.

When an agent relies on this watchlist before a dedicated guideline exists, it should include an `Assumptions:` line naming the unresolved API, availability, or platform-support detail.

## Feature Watchlist

| Feature | Platforms | User Need | Agent Implication | Repo Action | Evidence Status |
| --- | --- | --- | --- | --- | --- |
| tvOS Larger Text / Dynamic Type-like scaling | tvOS / Apple TV | Low-vision users need readable text at TV distance and across changing screen sizes. | Treat tvOS text scaling as first-class, not iOS-only. Review tvOS UI for scalable text, focus-ring layout resilience, shelf/card truncation, and large-text menu states. | Add or update a tvOS guideline focused on Larger Text layout resilience. Add promptfoo coverage for Apple TV text scaling. | Apple announced Larger Text support for tvOS; developer integration details need Apple docs. |
| Generated subtitles for uncaptioned video | iPhone, iPad, Mac, Apple TV, Apple Vision Pro | Deaf and hard-of-hearing users need spoken dialogue access when captions are missing. | Do not treat system-generated subtitles as a substitute for author-provided captions when captions can be shipped. Inspect media controls, caption affordances, language availability, and custom player integration. | Update media guidance across UIKit, SwiftUI, tvOS, macOS, and visionOS. Add tests for caption/subtitle discoverability and fallback behavior. | Apple announced on-device generated subtitles; availability and language limits are noted by Apple. |
| Apple Intelligence-enhanced VoiceOver image exploration | iOS, iPadOS, macOS, likely systemwide supported contexts | Blind and low-vision users need richer descriptions for images and documents. | Keep requiring semantic labels, values, alt text, and accessible custom views. AI descriptions improve exploration, but do not replace app-owned semantics or deterministic labels. | Strengthen image/custom-view guidance and negative-case evals for "AI can describe it, so can I skip labels?" | Apple announced Image Explorer improvements; safety notes say users should not rely on these features in high-risk contexts. |
| Magnifier Live Recognition and spoken control | iPhone, iPad, supported Apple Intelligence devices | Low-vision users need fast environmental and document understanding. | Keep app guidance focused on high-contrast UI, explicit controls, readable text, and semantic structure. Do not assume external Magnifier workflows compensate for inaccessible app UI. | Add user-research prompts around low-vision workflows and app handoff points. | Apple announced Magnifier updates; developer obligations remain inference until API docs are available. |
| Voice Control natural language navigation | iPhone and iPad, initially limited by language/region | Users with motor disabilities need robust voice navigation without memorizing exact control names. | Emphasize unique visible names, accessible names, unambiguous control labels, and duplicate-label detection. Natural language support makes ambiguous UI more visible, not less important. | Extend Voice Control naming guidance beyond macOS into UIKit and SwiftUI review checklists. Add promptfoo prompts using user language like "tap the purple folder." | Apple announced natural-language Voice Control with availability limits. |
| Accessibility Reader with summaries, translation, and complex-layout handling | Apple platforms where Accessibility Reader is available | Users with dyslexia, low vision, and cognitive accessibility needs benefit from reformatted text, summaries, and readable layouts. | Review app text hierarchy, headings, document structure, localization, selectable text, and custom rendering. Avoid flattening text into inaccessible images or canvases. | Add guidance for readable long-form content, tables, multi-column layouts, and document previews. | Apple announced expanded Accessibility Reader support. Developer integration details need Apple docs. |
| Apple Vision Pro wheelchair control and Dwell Control improvements | visionOS / Apple Vision Pro | Some wheelchair users need alternate drive controls and reliable eye-driven interaction. | Treat visionOS accessibility as more than VoiceOver. Include eye, dwell, face gesture, motion sensitivity, and controlled-environment assumptions in architecture guidance. | Expand visionOS backlog with eye/dwell interaction, motion cues, and mobility-assistive-device interoperability topics. | Apple announced the feature and controlled-environment constraints. |
| Vehicle Motion Cues on visionOS | visionOS / Apple Vision Pro | Users may experience motion sickness while using Vision Pro in moving vehicles. | Review immersive experiences for motion sensitivity, comfort settings, reduced motion, and environmental assumptions. | Add visionOS reduced-motion and comfort guidance when the visionOS track moves beyond scaffold. | Apple announced Vehicle Motion Cues for visionOS. |
| Made for iPhone hearing aid setup and handoff improvements | iOS, iPadOS, macOS, visionOS | Hearing-aid users need reliable audio routing between devices. | Review media apps for explicit audio-route state, caption affordances, and non-audio alternatives. Avoid assuming routing is invisible or always correct. | Add media/audio-route checks to testing guidance. | Apple announced setup and handoff improvements. |
| Name Recognition language expansion | Apple ecosystem feature | Deaf and hard-of-hearing users may rely on name detection in more languages. | Consider notification, transcription, and alert design from a multi-language accessibility standpoint. App guidance should still provide visible, haptic, and captioned alternatives where relevant. | Track under hearing/deaf media and notification guidance. | Apple announced expanded language coverage. |
| FaceTime sign-language interpreter API | FaceTime / communication apps | Deaf and hard-of-hearing users may need interpreter access during calls. | Track API documentation before making implementation recommendations. For now, guide communication apps to preserve video layout, focus, captions, and interpreter visibility. | Add source-registry entry and communication-app guideline once Apple developer docs are available. | Apple announced a new API, but public implementation details need follow-up. |
| Sony Access controller support | iOS, iPadOS, macOS | Users with motor disabilities need customizable game and app input. | Treat hardware controller support as an accessibility affordance. Review focus systems, remapping assumptions, switch access, and non-touch input parity. | Consider a cross-platform alternate-input guideline for games and interactive apps. | Apple announced controller support. |

## Architecture Implications

These features should influence the agent architecture in three ways:

1. Keep watchlist items outside the always-loaded runtime path until there is accepted guidance.
2. Add feature-specific routing only after the repo has stable guidelines or backlog entries.
3. Make evals verify user-impact reasoning, not just framework vocabulary.

The agent should avoid answers that imply platform AI features absolve app teams from accessibility work. New system capabilities are useful user tools, but app semantics, labels, focus behavior, captions, scalable layout, and input alternatives remain app responsibilities.

## Promptfoo Coverage Candidates

Use user-like prompts, not repo-internal terminology:

- "My Apple TV app text is too small for people sitting across the room. What should I check?"
- "Can I rely on Apple's automatic subtitles instead of shipping captions?"
- "If VoiceOver can describe images with AI now, do I still need accessibility labels?"
- "Voice Control can understand natural language now. Do duplicate button names still matter?"
- "My app uses a custom video player. What should I verify for captions and subtitles?"
- "How should a visionOS app think about users who rely on eye control or dwell interactions?"
- "What should I check if a user controls my iPad app with a game controller or adaptive controller?"
- "How should long articles, tables, or document previews be structured for Accessibility Reader?"

Expected eval behavior:

- Route to the relevant platform or media guidance if it exists.
- Name this watchlist only when the answer depends on previewed 2026 features.
- Include assumptions when public developer docs or API details are not yet available.
- Avoid claiming generated subtitles, AI image descriptions, or natural-language Voice Control replace semantic accessibility work.

## Recommended Repo Actions

1. Add a tvOS Larger Text guideline or extend the existing tvOS Dynamic Type/layout-resilience coverage.
2. Update media guidelines so generated subtitles are treated as a fallback and not a replacement for captions.
3. Add Voice Control naming and duplicate-label checks to UIKit and SwiftUI guidance.
4. Expand the visionOS backlog for eye, dwell, face gesture, wheelchair-control context, and motion-comfort topics.
5. Add promptfoo gold prompts for the coverage candidates above.
6. Add source-registry entries when Apple developer documentation or release notes are published.
7. Re-check community analysis from Hacking With Swift, NSHipster, Swiftjective-C, and other Apple-platform commentators during the next source refresh.

## Commentary Coverage Notes

The July 6, 2026 search pass found useful coverage from Apple Newsroom, The Verge, TechRadar, Tom's Guide, and T3. Targeted searches did not find accessibility-specific WWDC 2026 analysis from Hacking With Swift, NSHipster, or Swiftjective-C in this pass. Re-check those sources before converting this watchlist into accepted guidance.

## Sources

- Apple Newsroom: https://www.apple.com/newsroom/2026/05/apple-unveils-new-accessibility-features-and-updates-with-apple-intelligence/
- The Verge: https://www.theverge.com/tech/933420/apple-iphone-mac-vision-pro-accessibility-2026-apple-intelligence
- TechRadar: https://www.techradar.com/televisions/streaming-devices/apple-is-introducing-useful-accessibility-features-in-tvos-27-for-apple-tv-4k-that-will-appeal-to-everyone-including-larger-text-and-auto-generated-subtitles-but-some-major-streaming-apps-dont-use-apples-own-app-tech-that-enables-them
- Tom's Guide: https://www.tomsguide.com/phones/iphones/apple-announces-new-accessibility-features-powered-by-ai-for-your-iphone-what-you-need-to-know
- T3: https://www.t3.com/tech/tvs/apple-tv-getting-a-small-feature-update-that-could-make-a-big-difference-to-millions-of-users-literally

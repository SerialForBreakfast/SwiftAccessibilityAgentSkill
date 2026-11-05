# Sources of Truth Registry

Last updated: 2026-11-04
Owner: SwiftUI Accessibility Agent project

## Registry Format

Each source entry must include:

- `source_id`: Stable short ID (for citations in guideline docs).
- `title`: Human-readable title.
- `url`: Canonical URL.
- `authority_tier`: Tier-1, Tier-2, or Tier-3.
- `last_reviewed`: Date reviewed for freshness.
- `scope`: What this source is used to validate.
- `notes`: Caveats, version context, or follow-ups.

## Authority Tiers

- Tier-1: Apple platform truth. Use as the baseline source for rules.
- Tier-2: High-quality community sources. Use for implementation practice and examples.
- Tier-3: Reference-only sources. Use with caution and always cross-check.

## Tier-1 Sources (Reviewed Scope Recorded in Audit)

| source_id | title | url | authority_tier | last_reviewed | scope | notes |
|---|---|---|---|---|---|---|
| APPLE-SWIFTUI-ACCESSIBILITY | SwiftUI: Accessibility | https://developer.apple.com/documentation/swiftui/view-accessibility | Tier-1 | 2026-03-07 | SwiftUI accessibility APIs and modifiers | Old DocC URL returns 404; replaced with reviewed View accessibility modifier page. Prior review date retained. |
| APPLE-VIEW-ACCESSIBILITY | Accessibility Modifiers (View Accessibility) | https://developer.apple.com/documentation/swiftui/view-accessibility | Tier-1 | 2026-11-04 | Modifier-level behavior for SwiftUI view semantics | Overview and modifier categories: native semantics plus selective customization. |
| APPLE-ACCESSIBILITY-ELEMENT-CHILDREN | accessibilityElement(children:) | https://developer.apple.com/documentation/swiftui/view/accessibilityelement%28children%3A%29 | Tier-1 | 2026-11-04 | SwiftUI grouping behavior (`combine`/`contain`/`ignore`) | Declaration and discussion: child behavior defaults to ignore; choose grouping deliberately. |
| APPLE-ACCESSIBILITY-CHILDREN | accessibilityChildren(children:) | https://developer.apple.com/documentation/swiftui/view/accessibilitychildren%28children%3A%29 | Tier-1 | 2026-11-04 | Synthetic accessibility child elements for complex visuals | Discussion: synthetic children replace existing children and provide nonvisual structure. |
| APPLE-ACCESSIBILITY-REPRESENTATION | accessibilityRepresentation(representation:) | https://developer.apple.com/documentation/swiftui/view/accessibilityrepresentation%28representation%3A%29 | Tier-1 | 2026-11-04 | Alternate semantic representations for non-standard UI | Discussion: replacement representation; styled native controls can retain native semantics. |
| APPLE-CREATING-ACCESSIBLE-VIEWS | Enhancing the Accessibility of Your SwiftUI App | https://developer.apple.com/documentation/accessibility/enhancing-the-accessibility-of-your-swiftui-app | Tier-1 | 2026-11-04 | End-to-end SwiftUI accessibility implementation guidance | WWDC24 sample project and setup; sample companion, not a comprehensive API contract. |
| APPLE-HIG-ACCESSIBILITY | Apple Human Interface Guidelines: Accessibility | https://developer.apple.com/design/human-interface-guidelines/accessibility | Tier-1 | 2026-11-04 | Product-level accessibility behavior expectations | HIG vision, mobility, hearing, cognition and platform comfort guidance. |
| APPLE-AX-HUB | Accessibility Documentation Hub | https://developer.apple.com/documentation/accessibility | Tier-1 | 2026-11-04 | Assistive technologies, testing resources, and broad guidance | Accessibility topic index; resolve specific API or testing pages for normative details. |
| APPLE-AX-INSPECTOR | Accessibility Inspector | https://developer.apple.com/documentation/accessibility/accessibility-inspector | Tier-1 | 2026-11-04 | Tooling workflows and audit checks | Overview: semantic inspection and audit support; complements app-level accessibility testing. |
| APPLE-AX-TESTING | Performing Accessibility Testing for Your App | https://developer.apple.com/documentation/accessibility/performing-accessibility-testing-for-your-app | Tier-1 | 2026-11-04 | Manual and tool-assisted accessibility testing guidance | Overview and testing matrix: common tasks, settings and assistive technologies. |
| APPLE-WWDC-AX-INDEX | WWDC Accessibility and Inclusion Sessions | https://developer.apple.com/videos/accessibility-inclusion/ | Tier-1 | 2026-03-07 | Session-driven updates and platform changes | Discovery index or background resource; use a specific reviewed source for implementation claims. Prior review date retained. |
| APPLE-WWDC24-SWIFTUI | Catch Up on Accessibility in SwiftUI (WWDC24) | https://developer.apple.com/videos/play/wwdc2024/10073/ | Tier-1 | 2026-11-04 | SwiftUI semantics, modifiers, and interaction updates | Transcript: reducing navigation overhead while preserving meaningful semantic attributes and actions. |
| APPLE-WWDC21-SWIFTUI-BEYOND | SwiftUI Accessibility: Beyond the Basics (WWDC21) | https://developer.apple.com/videos/play/wwdc2021/10119/ | Tier-1 | 2026-11-04 | Advanced SwiftUI grouping, representation, and interaction patterns | Transcript: synthetic children and representations for custom graphics and controls. |
| APPLE-WWDC23-SWIFTUI-UIKIT | Build Accessible Apps with SwiftUI and UIKit (WWDC23) | https://developer.apple.com/videos/play/wwdc2023/10036/ | Tier-1 | 2026-11-04 | Interop guidance for mixed SwiftUI/UIKit apps | Transcript: interaction and announcement refinements across SwiftUI/UIKit. |
| APPLE-WWDC23-AUDITS | Perform Accessibility Audits for Your App (WWDC23) | https://developer.apple.com/videos/play/wwdc2023/10035/ | Tier-1 | 2026-11-04 | Practical auditing approach and tooling | Transcript: automated audits find categories of issues; app/user-task evaluation remains separate. |
| APPLE-UIKIT-ACCESSIBILITY | Accessibility for UIKit | https://developer.apple.com/documentation/uikit/accessibility-for-uikit | Tier-1 | 2026-11-04 | UIKit accessibility API guidance for iOS/tvOS | Overview: built-in UIKit semantics and customization; custom elements and containers. |
| APPLE-TVOS-FOCUS | About Focus Interactions for Apple TV | https://developer.apple.com/documentation/uikit/about-focus-interactions-for-apple-tv | Tier-1 | 2026-11-04 | tvOS focus engine behavior and navigation expectations | Overview and focus engine: indirect input, preferred environments, user-controlled navigation. |
| APPLE-MACOS-NSACCESSIBILITY | NSAccessibilityProtocol | https://developer.apple.com/documentation/appkit/nsaccessibilityprotocol | Tier-1 | 2026-11-04 | AppKit accessibility protocol and role/value/action contracts | Protocol overview: informational properties, action methods and notifications. |
| APPLE-WWDC25-MAC-ACCESSIBILITY | Make your Mac app more accessible to everyone (WWDC25) | https://developer.apple.com/videos/play/wwdc2025/229/ | Tier-1 | 2026-11-04 | macOS-specific patterns and modern platform recommendations | Transcript: Mac container navigation and keyboard interaction differ from iOS. |
| APPLE-IOS18-RELEASE-NOTES | iOS/iPadOS 18 Release Notes | https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-18-release-notes | Tier-1 | 2026-03-07 | Official release-note signal for accessibility fixes/regressions | Archived release-line reference retained for older OS context; not evidence of current OS behavior. Prior review date retained. |
| APPLE-MACOS15-RELEASE-NOTES | macOS 15 Release Notes | https://developer.apple.com/documentation/macos-release-notes/macos-15-release-notes | Tier-1 | 2026-03-07 | Official release-note signal for platform regressions and fixes | Archived release-line reference retained for older OS context; not evidence of current OS behavior. Prior review date retained. |
| APPLE-SAFARI18-RELEASE-NOTES | Safari 18 Release Notes | https://developer.apple.com/documentation/safari-release-notes/safari-18-release-notes | Tier-1 | 2026-03-07 | VoiceOver and web accessibility change tracking | Archived release-line reference retained for older OS context; not evidence of current OS behavior. Prior review date retained. |
| APPLE-VOICEOVER-RECOGNITION-SUPPORT | Use VoiceOver Recognition on iPhone/iPad | https://support.apple.com/en-us/111799 | Tier-1 | 2026-11-04 | System behavior for image/text recognition and related announcements | VoiceOver Recognition settings support image/text recognition; retain app-owned semantics. |
| ADA-2025-WINNERS | Apple Design Awards 2025 Winners and Finalists | https://www.apple.com/newsroom/2025/06/apple-unveils-winners-and-finalists-of-the-2025-apple-design-awards/ | Tier-1 | 2026-03-07 | Apple-recognized inclusive product exemplars | Historical product exemplar; not an implementation or current-version contract. Prior review date retained. |
| ADA-2024-WINNERS | Apple Design Awards 2024 Winners and Finalists | https://developer.apple.com/design/awards/2024/ | Tier-1 | 2026-03-07 | Apple-recognized inclusive product exemplars | Historical product exemplar; not an implementation or current-version contract. Prior review date retained. |
| ADA-2023-WINNERS | Apple Design Awards 2023 Winners and Finalists | https://developer.apple.com/design/awards/2023/ | Tier-1 | 2026-03-07 | Apple-recognized inclusive product exemplars | Historical product exemplar; not an implementation or current-version contract. Prior review date retained. |
| ASC-ANL-OVERVIEW | App Store Connect: Overview of Accessibility Nutrition Labels | https://developer.apple.com/help/app-store-connect/manage-app-accessibility/overview-of-accessibility-nutrition-labels/ | Tier-1 | 2026-11-04 | Label feature definitions and policy framing | Feature definitions, OS 26+ display scope, common-task/device evaluation, and compatible-app handling. |
| ASC-ANL-MANAGE | App Store Connect: Manage Accessibility Nutrition Labels | https://developer.apple.com/help/app-store-connect/manage-app-accessibility/manage-accessibility-nutrition-labels/ | Tier-1 | 2026-11-04 | Operational guidance for declaring accessibility support | Device-specific answers, draft/publish workflow, update support responses as app behavior changes. |

## Tier-2 Sources (Seed)

| source_id | title | url | authority_tier | last_reviewed | scope | notes |
|---|---|---|---|---|---|---|
| SWIFTLEE-A11Y | SwiftLee Accessibility Articles | https://www.avanderlee.com | Tier-2 | 2026-03-07 | Pragmatic Swift/SwiftUI techniques | Discovery index or background resource; use a specific reviewed source for implementation claims. Prior review date retained. |
| HWS-SWIFTUI-A11Y | Hacking with Swift: SwiftUI Accessibility | https://www.hackingwithswift.com | Tier-2 | 2026-03-07 | Practical examples and beginner-to-mid workflows | Response blocked or empty; retained for discovery/history, excluded as refreshed normative evidence. Prior review date retained. |
| MAJID-A11Y | Swift with Majid: Accessibility Topics | https://swiftwithmajid.com | Tier-2 | 2026-03-07 | Advanced SwiftUI patterns (e.g., representations/rotors) | Discovery index or background resource; use a specific reviewed source for implementation claims. Prior review date retained. |
| USEYOURLOAF-A11Y | Use Your Loaf: Accessibility Updates | https://useyourloaf.com | Tier-2 | 2026-03-07 | API changes and migration notes | Discovery index or background resource; use a specific reviewed source for implementation claims. Prior review date retained. |
| CVS-SWIFTUI-A11Y-TECHNIQUES | CVS Health iOS SwiftUI Accessibility Techniques | https://github.com/cvs-health/ios-swiftui-accessibility-techniques | Tier-2 | 2026-03-07 | Open-source technique examples | Discovery index or background resource; use a specific reviewed source for implementation claims. Prior review date retained. |
| CVS-COMBINING-FOCUS | CVS Health: Combining Focus Example | https://github.com/cvs-health/ios-swiftui-accessibility-techniques/blob/main/iOSswiftUIa11yTechniques/Documentation/CombiningFocus.md | Tier-2 | 2026-11-04 | Concrete grouping/focus example for compound elements | Combining Focus example: implementation illustration, anchored to Apple grouping contract. |
| SWIFTLEE-SWIFTUI-UIKIT-A11Y | SwiftLee: Accessibility in SwiftUI for UIKit Developers | https://www.avanderlee.com/swiftui/accessibility-uikit-developers/ | Tier-2 | 2026-11-04 | Interop-oriented SwiftUI/UIKit implementation patterns | Interop article: practical trait/modifier mapping; current Apple documentation controls availability. |
| CASHAPP-ACCESSIBILITYSNAPSHOT | AccessibilitySnapshot (Cash App) | https://github.com/cashapp/AccessibilitySnapshot | Tier-2 | 2026-03-07 | Snapshot-style accessibility regression testing techniques | Discovery index or background resource; use a specific reviewed source for implementation claims. Prior review date retained. |
| APPLE-FORUMS-ACCESSIBILITY-TAG | Apple Developer Forums: Accessibility Tag | https://developer.apple.com/forums/tags/accessibility | Tier-2 | 2026-03-07 | Discovery index for emerging accessibility regressions | Discovery index or background resource; use a specific reviewed source for implementation claims. Prior review date retained. |
| APPLE-FORUMS-SWIFTUI-TAG | Apple Developer Forums: SwiftUI Tag | https://developer.apple.com/forums/tags/swiftui | Tier-2 | 2026-03-07 | Discovery index for SwiftUI accessibility regressions | Discovery index or background resource; use a specific reviewed source for implementation claims. Prior review date retained. |
| APPLE-FORUMS-A11Y-INCLUSION-HUB | Apple Developer Forums: Accessibility and Inclusion Topic | https://developer.apple.com/forums/forums/topics/accessibility-and-inclusion | Tier-2 | 2026-03-07 | Official forum hub for platform accessibility bug discussions | Discovery index or background resource; use a specific reviewed source for implementation claims. Prior review date retained. |
| APPLE-FORUMS-THREAD-100449 | VoiceOver Focus Trapped in Container View (Forum Thread) | https://developer.apple.com/forums/thread/100449 | Tier-2 | 2026-11-04 | UIKit container focus-trap symptom and mitigation discussion | 2018/2020 iOS container report; does not establish current OS or tvOS impact. |
| APPLE-FORUMS-THREAD-750508 | SwiftUI Link Trait Behavior (Forum Thread) | https://developer.apple.com/forums/thread/750508 | Tier-2 | 2026-11-04 | Role/trait mismatch symptom report | April 2024/June 2025 reports of combined link/button traits; thread does not establish an OS range or confirmed defect. |
| APPLE-FORUMS-THREAD-804448 | VoiceOver Reads Text Inside Image (Forum Thread) | https://developer.apple.com/forums/thread/804448 | Tier-2 | 2026-11-04 | OCR-style extra announcement symptom | Accepted user answer identifies Text Recognition setting; preserve user recognition preference and image semantics. |
| APPLE-FORUMS-THREAD-814208 | SwiftUI Lazy Stack Hang with Accessibility Tools (Forum Thread) | https://developer.apple.com/forums/thread/814208 | Tier-2 | 2026-11-04 | Accessibility-enabled hang/performance regression with nested lazy stacks | DTS confirms state mutation during lazy allocation; later replies report improved reproduction on 26.5/27 beta, without a universal fixed-version guarantee. |
| APPLE-FORUMS-THREAD-725486 | SwiftUI List Reorder Announcement Regression (Forum Thread) | https://developer.apple.com/forums/thread/725486 | Tier-2 | 2026-11-04 | Reorder announcement context loss symptom | February/March 2023 reorder report acknowledged by Apple; exact minor versions/fix not established. |
| AXE-CON-SUPPORT | axe-con Accessibility Conference Support Page | https://www.deque.com/axe-con/support/ | Tier-2 | 2026-03-07 | Conference accessibility details and session resource entry point | Discovery index or background resource; use a specific reviewed source for implementation claims. Prior review date retained. |
| A11YSIG-RECORDINGS | A11ySIG/A11yNYC Recording Archive Example | https://www.a11ysig.org/recording-a11ynyc-digital-accessibilitys-gap-ai-to-bridge-mobile-and-web-barriers-michael-bervell-jason-tan/ | Tier-2 | 2026-03-07 | Community practitioner session archive signal | Discovery index or background resource; use a specific reviewed source for implementation claims. Prior review date retained. |

## Tier-3 Sources (Seed)

| source_id | title | url | authority_tier | last_reviewed | scope | notes |
|---|---|---|---|---|---|---|
| COMMUNITY-CONFERENCE-SLIDES | Conference Slide Decks | N/A | Tier-3 | 2026-03-07 | Background context only | Do not cite as sole source for any rule. |
| COMMUNITY-VENDOR-BLOGS | Vendor Blogs | N/A | Tier-3 | 2026-03-07 | Supplemental examples | Require Tier-1 corroboration before adoption. |
| COMMUNITY-FORUM-POSTS | Community Posts/Threads | N/A | Tier-3 | 2026-03-07 | Edge-case discovery | Treat as anecdotal until validated. |
| APPLEVIS-IOS18-VOICEOVER-BRAILLE | AppleVis: iOS 18/iPadOS 18 VoiceOver and Braille Summary | https://www.applevis.com/blog/ios-18-ipados-18-accessibility-summary-voiceover-braille-issues-improvements | Tier-3 | 2026-03-07 | Community trend/impact reporting for OS-level regressions | Response blocked or empty; retained for discovery/history, excluded as refreshed normative evidence. Prior review date retained. |
| APPLEVIS-RC-THREAD | AppleVis Beta/RC Accessibility Threads | https://www.applevis.com/forum/apple-beta-releases/release-candidates-ios-ipados-182-macos-sequoia-152-tvos-182-visionos-22 | Tier-3 | 2026-03-07 | Early signal for release-cycle regression patterns | Response blocked or empty; retained for discovery/history, excluded as refreshed normative evidence. Prior review date retained. |
| APPLEVIS-HOF | AppleVis App Hall of Fame | https://www.applevis.com/applevis-ios-ipados-app-hall-fame | Tier-3 | 2026-03-07 | Community-recognized examples of sustained accessibility quality | Response blocked or empty; retained for discovery/history, excluded as refreshed normative evidence. Prior review date retained. |
| STACKOVERFLOW-VO-FOCUS-RESET | VoiceOver Focus Reset Discussion (Stack Overflow) | https://stackoverflow.com/questions/79860389/voiceover-focus-does-not-reset-to-top-when-navigating-between-screens-in-swiftui | Tier-3 | 2026-03-07 | Supplemental symptom report for navigation focus behavior | Response blocked or empty; retained for discovery/history, excluded as refreshed normative evidence. Prior review date retained. |

## Tiering Policy Notes

- Open-source repos can be Tier-2 when maintained and consistent with Apple guidance.
- Any repo-derived technique must map to at least one Tier-1 Apple source before it becomes a project rule.
- When Tier-1 and Tier-2 conflict, Tier-1 wins.

## Freshness Policy

- Apple docs: review quarterly and at each major OS release (iOS, tvOS, macOS).
- WWDC sources: review annually after WWDC season.
- Community sources: review annually and downgrade if stale.

## Stale-Source Downgrade Rules (Actionable)

Apply these rules during freshness review:

1. Trigger conditions:
   - `last_reviewed` exceeds freshness interval for source tier/type.
   - Link is dead, redirected to unrelated content, or materially changed.
   - Guidance conflicts with current Tier-1 Apple documentation.
2. Required actions:
   - Mark source notes with stale/conflict reason and review date.
   - Remove source from new guideline citations until revalidated.
   - If source is Tier-2 and remains stale after one review cycle, downgrade to Tier-3.
   - If source is irrecoverably outdated or unavailable, remove from registry.
3. Guideline impact handling:
   - For each guideline citing a downgraded/removed source, open a follow-up to replace citation.
   - Do not keep a guideline in `Accepted` status if its required Tier-1 citation is invalid.
4. Completion criteria:
   - Registry entry updated (`last_reviewed`, notes, tier if changed).
   - Affected guideline files updated or follow-up issues recorded.

## November 2026 Refresh

Claim-level availability and pending audit work: [refresh ledger](../source-refresh-2026-11.md).

| source_id | title | url | authority_tier | last_reviewed | scope | notes |
|---|---|---|---|---|---|---|
| APPLE-WWDC26-TVOS-TEXT | tvOS Larger Text | https://developer.apple.com/videos/play/wwdc2026/221/ | Tier-1 | 2026-11-04 | tvOS | Transcript reviewed: Overview; layout adaptation; see claim-level ledger. |
| APPLE-WWDC26-READING | Accessible reading | https://developer.apple.com/videos/play/wwdc2026/219/ | Tier-1 | 2026-11-04 | iOS, macOS | Transcript reviewed: Standard views; Custom text; see claim-level ledger. |
| APPLE-WWDC26-SUBTITLES | Generated subtitles | https://developer.apple.com/videos/play/wwdc2026/256/ | Tier-1 | 2026-11-04 | iOS, macOS, tvOS, visionOS | Transcript reviewed: Availability and support; Style preview; see claim-level ledger. |
| APPLE-WWDC26-CONTROLS | Accessible custom controls | https://developer.apple.com/videos/play/wwdc2026/220/ | Tier-1 | 2026-11-04 | iOS, SwiftUI | Transcript reviewed: Guiding principles; Complex controls; see claim-level ledger. |

## Audit Dispositions

The machine-readable [source audit](../../../evals/evidence/registry-audit.json) distinguishes scoped content review, historical references, discovery indexes, replaced URLs, and access-limited resources. Reachability alone does not establish claim freshness. Access-limited community pages remain research pointers; current platform rules use reviewed Apple sources.

## Refreshed Release and Symbol Sources

| source_id | title | url | authority_tier | last_reviewed | scope | notes |
|---|---|---|---|---|---|---|
| APPLE-IOS26-RELEASE-NOTES | iOS/iPadOS 26 release notes | https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-26-release-notes | Tier-1 | 2026-11-04 | TextKit natural alignment and SDK-linked directionality | Scoped review; retrieval fingerprint in source audit. |
| APPLE-TVOS26-RELEASE-NOTES | tvOS 26 release notes | https://developer.apple.com/documentation/tvos-release-notes/tvos-26-release-notes | Tier-1 | 2026-11-04 | App Store accessibility labels and TextKit | Scoped review; retrieval fingerprint in source audit. |
| APPLE-IOS27-RELEASE-NOTES | iOS/iPadOS 27 release notes | https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-27-release-notes | Tier-1 | 2026-11-04 | SwiftUI, TextKit and UIKit changes | Scoped review; retrieval fingerprint in source audit. |
| APPLE-TVOS27-RELEASE-NOTES | tvOS 27 release notes | https://developer.apple.com/documentation/tvos-release-notes/tvos-27-release-notes | Tier-1 | 2026-11-04 | Platform-specific SDK and behavior changes | Scoped review; retrieval fingerprint in source audit. |
| APPLE-MACOS27-RELEASE-NOTES | macOS 27 release notes | https://developer.apple.com/documentation/macos-release-notes/macos-27-release-notes | Tier-1 | 2026-11-04 | AppKit tab role and SwiftUI navigation semantics | Scoped review; retrieval fingerprint in source audit. |
| APPLE-VISIONOS27-RELEASE-NOTES | visionOS 27 release notes | https://developer.apple.com/documentation/visionos-release-notes/visionos-27-release-notes | Tier-1 | 2026-11-04 | SwiftUI, UIKit and TextKit scope | Scoped review; retrieval fingerprint in source audit. |
| APPLE-XCODE27-RELEASE-NOTES | Xcode 27 release notes | https://developer.apple.com/documentation/xcode-release-notes/xcode-27-release-notes | Tier-1 | 2026-11-04 | Coding Intelligence and Device Hub | Scoped review; retrieval fingerprint in source audit. |
| APPLE-XCODE266-RELEASE-NOTES | Xcode 26.6 release notes | https://developer.apple.com/documentation/xcode-release-notes/xcode-26_6-release-notes | Tier-1 | 2026-11-04 | ACP, Preview Snapshot variants and assistant accessibility fixes | Scoped review; retrieval fingerprint in source audit. |
| APPLE-NEWSROOM-2026-ACCESSIBILITY | 2026 accessibility announcements | https://www.apple.com/newsroom/2026/05/apple-unveils-new-accessibility-features-and-updates-with-apple-intelligence/ | Tier-1 | 2026-11-04 | Announcement-level feature and availability context | Scoped review; retrieval fingerprint in source audit. |
| APPLE-LINKED-GROUP | accessibilityLinkedGroup(id:in:) | https://developer.apple.com/documentation/swiftui/view/accessibilitylinkedgroup(id:in:) | Tier-1 | 2026-11-04 | Symbol availability and linked text discussion | Scoped review; retrieval fingerprint in source audit. |
| APPLE-ADJUSTABLE-ACTION | accessibilityAdjustableAction(_:) | https://developer.apple.com/documentation/swiftui/view/accessibilityadjustableaction(_:) | Tier-1 | 2026-11-04 | Adjustable action declaration and availability | Scoped review; retrieval fingerprint in source audit. |
| APPLE-DIRECT-TOUCH | accessibilityDirectTouch(_:options:) | https://developer.apple.com/documentation/swiftui/view/accessibilitydirecttouch(_:options:) | Tier-1 | 2026-11-04 | Direct-touch declaration and availability | Scoped review; retrieval fingerprint in source audit. |
| APPLE-CATEGORIZED-ACTIONS | accessibilityActions(category:_:) | https://developer.apple.com/documentation/swiftui/view/accessibilityactions(category:_:) | Tier-1 | 2026-11-04 | Categorized action declaration and availability | Scoped review; retrieval fingerprint in source audit. |

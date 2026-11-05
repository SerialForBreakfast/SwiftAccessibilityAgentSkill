# U-008: Custom Controls and Semantic Equivalence

## Title

When building custom controls, provide semantic accessibility equivalent to standard controls.

## Problem Statement

Custom UI can appear visually correct but announce as generic views, hiding role, state, and action context.

## Rule

Any custom interactive UIKit component must expose equivalent semantics (role, label, value, actions) to the native control it replaces.

## Rationale

Assistive technologies depend on semantics, not visuals. Semantic equivalence preserves predictable interaction behavior.

## How To Implement

### UIKit

- Prefer native controls whenever possible.
- For custom controls, set `isAccessibilityElement`, label, value, traits, and custom actions explicitly.
- Keep semantic state synchronized with visual state transitions.

### SwiftUI Interop Notes

- Ensure representable boundaries preserve custom control semantics.
- Validate parent container behavior does not mask child custom-control traits.

## Interaction Refinement (Source Review: 2026-11-04)

Expose purpose, current value, equivalent actions, and meaningful feedback. For continuous controls, provide adjustable increment/decrement behavior before adding precision gestures. Direct touch and passthrough gestures are additional interaction options, not substitutes for discoverable actions. Keep ordinary navigation usable for people who do not use rotor shortcuts.

In SwiftUI, `accessibilityAdjustableAction` is available from iOS/tvOS 13 and macOS 10.15; `accessibilityDirectTouch` from iOS/tvOS 17 and macOS 14. Both are available on visionOS 1. Check the exact platform target before generating code. Keep value-change announcements useful rather than speaking every intermediate update.

Sources: [APPLE-WWDC26-CONTROLS], [APPLE-ADJUSTABLE-ACTION], [APPLE-DIRECT-TOUCH].

## How To Test

### Accessibility Inspector

- Confirm custom controls are exposed as intended semantic types.
- Confirm label/value/traits/actions are present and consistent.

### VoiceOver Walkthrough

- Focus custom control and verify announcement matches role/state intent.
- Trigger interactions and confirm updated state feedback.

### Optional XCUITest Hook

- Assert critical custom control states via labels/values/identifiers.

## Do / Don't

- Do: model custom steppers as adjustable controls with clear increment/decrement behavior.
- Don't: ship custom tappable views with no semantic role.

## Citations

- [APPLE-AX-HUB] https://developer.apple.com/documentation/accessibility
- [APPLE-HIG-ACCESSIBILITY] https://developer.apple.com/design/human-interface-guidelines/accessibility
- [APPLE-WWDC23-SWIFTUI-UIKIT] https://developer.apple.com/videos/play/wwdc2023/10036/

## Quote Snippets (Optional)

- None included in this draft.

## Metadata

- Status: Accepted
- Last Reviewed: 2026-03-07
- Last Verified: 2026-03-07
- Platforms: iOS, iPadOS
- Confidence: Medium

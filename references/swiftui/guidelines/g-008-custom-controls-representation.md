# G-008: Custom Controls and Accessibility Representation

## Title

When building custom controls, provide a semantic accessibility representation equivalent to standard controls.

## Problem Statement

Custom UI patterns often look correct visually but announce as generic views, leaving users without role, state, or action context.

## Rule

Any custom interactive component must expose equivalent accessibility semantics (role, label, value, actions) to the native control it replaces.

## Rationale

Assistive technologies depend on semantic structure rather than visuals. Equivalent semantic representation preserves predictable interaction behavior.

## How To Implement

### SwiftUI

- Prefer native controls first; custom controls are a fallback.
- If using a custom control, explicitly provide label, value, traits/role, and actions.
- Use accessibility representation techniques to map complex visuals to clear semantic elements.
- Keep semantic behavior synchronized with custom visual state transitions.

### UIKit Interop Notes

- In UIKit-backed custom views, set `isAccessibilityElement`, `accessibilityLabel`, `accessibilityValue`, and traits explicitly.
- In representables, verify semantic fields update when SwiftUI bindings change.

## Interaction Refinement (Source Review: 2026-11-04)

Expose purpose, current value, equivalent actions, and meaningful feedback. For continuous controls, provide adjustable increment/decrement behavior before adding precision gestures. Direct touch and passthrough gestures are additional interaction options, not substitutes for discoverable actions. Keep ordinary navigation usable for people who do not use rotor shortcuts.

In SwiftUI, `accessibilityAdjustableAction` is available from iOS/tvOS 13 and macOS 10.15; `accessibilityDirectTouch` from iOS/tvOS 17 and macOS 14. Both are available on visionOS 1. Check the exact platform target before generating code. Keep value-change announcements useful rather than speaking every intermediate update.

Sources: [APPLE-WWDC26-CONTROLS], [APPLE-ADJUSTABLE-ACTION], [APPLE-DIRECT-TOUCH].

## How To Test

### Accessibility Inspector

- Confirm custom controls are exposed as the intended semantic type, not generic containers.
- Confirm label/value/traits/actions are all present and consistent.

### VoiceOver Walkthrough

- Focus custom control and verify announcement matches expected role/state.
- Trigger interaction and confirm updated state and action feedback.

### Optional XCUITest Hook

- Assert critical custom control states via accessibility labels/values/identifiers.

## Do / Don't

- Do: model a custom stepper as an adjustable control with clear increment/decrement behavior.
- Don't: ship custom tappable views with only visual affordances and no semantic role.

## Citations

- [APPLE-SWIFTUI-ACCESSIBILITY] https://developer.apple.com/documentation/swiftui/view-accessibility
- [APPLE-CREATING-ACCESSIBLE-VIEWS] https://developer.apple.com/documentation/accessibility/enhancing-the-accessibility-of-your-swiftui-app
- [APPLE-WWDC23-SWIFTUI-UIKIT] https://developer.apple.com/videos/play/wwdc2023/10036/

## Quote Snippets (Optional)

- None included in this draft.

## Metadata

- Status: Accepted
- Last Reviewed: 2026-03-07
- Last Verified: 2026-03-07
- Platforms: iOS, iPadOS
- Confidence: Medium

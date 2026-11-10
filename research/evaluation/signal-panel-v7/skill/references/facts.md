# Platform facts

## Leave working native controls alone

Before proposing a change, show the defect from the supplied code. A different style or an alternative is not a defect.

- **SwiftUI `Slider`** already exposes its value and adjustment. If the binding, range, step and label work, keep it. Do not call its value wrong without evidence, and do not replace it with a custom adjustable element.
- **Reduce Motion:** if the code already checks `accessibilityReduceMotion` and uses no animation or a non-moving transition, keep it. Do not claim movement that the transaction excludes.
- **Editable search or text field on macOS SwiftUI:**
  - keep one editable owner (the `NSSearchField` or `TextField`);
  - to remove a duplicate announcement, remove the *extra* label or wrapper semantics only;
  - never hide or replace the representable people type into; hiding neighbouring decoration is fine.
- **AppKit rows:** a row role and independently operable child controls can coexist. Inspect what people operate before flattening a row.

## Distinctions

- **UIKit button:** `accessibilityIdentifier` is for tests. It does not set the visible title. Check the displayed title (`title(for: .normal)` or `configuration?.title`) for each state.
- **State across updates:**
  - apply both inputs in succession to the same view;
  - check visible wording, accessibility value and the `.selected` trait separately;
  - a reconfigure must remove a stale `.selected` trait without dropping the others: `traits.remove(.selected)` / `traits.insert(.selected)`.
- **Optional help:** clear AppKit help with `setAccessibilityHelp(nil)`; an empty string is a different value.
- **UIKit edit grouping:** assign `action.category = grouped ? UIAccessibilityCustomAction.editCategory : nil`. The category is a `String?`, not an enum with an `.edit` case. Test both settings on the returned action. Keep the caller's established default.
- **AppKit accessibility members are methods, not assignable properties:**
  - `button.setAccessibilityLabel("Save")`, `button.accessibilityLabel()`;
  - `view.setAccessibilityCustomActions([NSAccessibilityCustomAction(name: "Archive") { archive(); return true }])`;
  - `NSAccessibilityCustomAction(name:target:selector:)` also exists.
  - Do not write UIKit-style `button.accessibilityLabel = …` on AppKit.
- **tvOS:**
  - Larger Text in tvOS settings is a tvOS 27 feature (WWDC26 session 221). On tvOS 26, keep layout readable and controls reachable without promising that preference.
  - Gate any newer API by its own availability.
- **Versions:** separate the build SDK, the deployment target and the tested runtime.

# Hidden code-contract rubric v1

Two development tasks per platform/framework combination. Grade the observable behavior described in the exported question, not the spelling used in the reference. The source package ID on each task is a related historical example, not a claim that a generated solution passed that entire package. App policy (duplication, clamping, fallback order, status wording or preference mapping) is not an Apple mandate.

| Task | Required observation | Accepted alternative in pilot | Deliberate defect |
|---|---|---|---|
| iOS UIKit checkout-font | Caller-supplied design font and scaled size survive two trait configurations; description wraps and keeps text. | Compute the scaled font first and assign the configuration together. | Replace typeface with preferred system font. |
| iOS UIKit switch-preservation | Return the original switch with its new name and unchanged value, traits and hint across reuse. | Only write a changed label; a working implementation may be kept. | Return another switch. |
| iOS SwiftUI toggle-binding | Read current state; forward changed, unlocked writes exactly once. | Delegate setter to a guarded commit function. | Return the unguarded binding. |
| iOS SwiftUI adjustable-volume | Both adjustment directions change by five within bounds. | Compute a signed delta then clamp. | Allow overshoot at endpoints. |
| macOS AppKit ordinary-buttons | Both existing buttons dispatch their distinct selectors to the current owner before and after rebinding. | Configure pairs in a loop. | Wire Save only. |
| macOS AppKit status-change | Publish the new field string before notifying, once per transition including clearing. | Compare saved old and updated new values. | Notify for duplicates. |
| macOS SwiftUI landmark-identity | Preserve order and stable IDs of important entries through replacement/removal. | Build with a reducing accumulator. | Return indices as IDs. |
| macOS SwiftUI checkout-layout | Distinguish ordinary and accessibility values of a supplied size environment. | Compare the enum to the accessibility threshold. | Recognize only the first accessibility size. |
| tvOS UIKit restoration-eligibility | Prefer eligible enabled opener, then enabled fallback, then no request. | Filter current candidates first and search the result. | Treat a present but disabled opener as eligible. |
| tvOS UIKit row-traits | Repeated selection updates preserve the button's unrelated traits. | Nonmutating union/subtraction. | Replace all traits. |
| tvOS SwiftUI motion-policy | Reduce Motion suppresses an optional existing effect; otherwise preserve it, including nil. | Guard and return the original animation. | Always animate when given an effect. |
| tvOS SwiftUI stale-media-reply | A write must match both current item and request; reject stale replies without writing. | Compare each component separately. | Compare only item identity. |

The tasks intentionally test different layers. Direct AppKit selector dispatch checks wiring, not mouse or assistive navigation. Binding tests observe writes, not SwiftUI view installation. The rotor task tests identity policy, not system rotor discovery. Font configuration and focus-target selection do not establish rendered fit or delivered focus. For explanation questions, integration outside the submitted seam, or a disputed oracle, retain source review rather than awarding an automatic pass.

No quality lift, native skill activation or model cost was measured. These known development cases cannot become held-out merely by hiding their tests.

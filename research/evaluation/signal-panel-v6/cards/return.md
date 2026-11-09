A close request, cancellation and completed dismissal are different events. Keep the origin independently of the presented content. Only the presentation that owns a dismissal may complete it; record that it completed so a repeat does nothing, then resolve the destination against what is eligible at that moment.

For a sheet, the presentation carries its own owner: use `sheet(item:)` with the token in the item, or capture the token when the sheet opens. Compare the captured owner with current state; do not use current state to infer which presentation called back. A late A must not close B, change B's focus or request restoration; B's own completion still restores once. Take the ordinary Close path before completing it, and contrast an origin that survives with one that disappears. For proof, exercise the installed closures: finish A late, then B twice. Handing a helper the right ticket does not exercise the installed callback.

For overlapping UIKit panels, restore or transfer the original background snapshot before the next panel captures it. Finish the replacement too: suppression while it is open says nothing about the final state. Preserve an initially hidden background and every ordinary control, including one that applies and closes.

For AppKit, check ownership by the originating window. Eligibility and refusal are separate rules:
- An absent origin, or an attached one that cannot become first responder, is ineligible: request the fallback.
- An eligible origin can still refuse `makeFirstResponder(_:)`; when it returns false, request the fallback too.
A detached-origin test covers neither attached case. Report requests, not delivered assistive focus.

[Implementation excerpts](examples/return.md)

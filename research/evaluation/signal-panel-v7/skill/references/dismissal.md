# Dismissal, focus return and fallback

## Decide

- **Three different events:** a close request, a cancellation, and a *completed* dismissal. Restore focus only on the completed dismissal of the presentation that owns it. Record that it completed, so a repeat does nothing. Resolve the return target against what still exists at that moment.
- **The callback must know which presentation it belongs to.**
  - Late arrivals: SwiftUI can call presentation A's dismissal after B has opened.
  - The wrong design: a closure that reads shared state at callback time (`currentTicket`, `activeSheet`, `lastOrigin`) cannot tell A from B.
  - The right design: build each presentation's dismissal closure when that presentation opens, capturing its own token and origin. Then the late A compares *its* token with the current one and does nothing.
  - Neither `onDisappear` of the sheet content nor a binding setter is the dismissal completion.

```swift
@MainActor final class ReturnCoordinator {
    private var active: UUID?
    let restore: (String) -> Void
    init(restore: @escaping (String) -> Void) { self.restore = restore }

    /// Call when a sheet opens; attach the returned closure to that presentation only.
    func open(origin: String) -> () -> Void {
        let token = UUID()
        active = token
        return { [weak self] in
            guard let self, self.active == token else { return }   // late A, or a repeat
            self.active = nil
            self.restore(origin)
        }
    }
}
// In the view: keep the closure with its presentation, e.g. in the `sheet(item:)` item or a per-presentation modifier.
```

- **UIKit overlapping panels:**
  - restore or hand over the original background's hidden state before the next panel captures it;
  - check the final state after the replacement closes too;
  - keep every ordinary control, including one that applies and closes.
- **AppKit focus return:** eligibility and refusal are separate rules.
  - The origin must still be in the *origin window*: `origin.window === originWindow`. Being attached to some window, or held weakly, is not enough.
  - An absent origin, a detached one, or an attached one with `acceptsFirstResponder == false` is ineligible: use the fallback.
  - An eligible origin can still refuse: when `window.makeFirstResponder(origin)` returns `false`, request the fallback too.
  - Report focus *requests*, not delivered assistive focus.

## Test: fire the old presentation's own callback late

**The wrong test:** call a helper with the right old ticket, such as `coordinator.complete(ticket: a)`. It passes even when the installed closure reads shared state, because the test supplied the identity the closure never had.

```swift
@MainActor func testLateFirstDismissalDoesNotRestoreSecond() {
    var restored: [String] = []
    let coordinator = ReturnCoordinator { restored.append($0) }
    let dismissA = coordinator.open(origin: "rowA")      // the closure attached to sheet A
    let dismissB = coordinator.open(origin: "rowB")      // B opens before A's completion arrives
    dismissA()                                           // late A
    XCTAssertEqual(restored, [])
    dismissB()
    dismissB()                                           // repeat completion
    XCTAssertEqual(restored, ["rowB"])
}
// Without the token comparison: late A restores "rowA" while B is showing → ["rowA", "rowB", "rowB"].
```

**AppKit cases, each with its own assertion:**

1. **Attached but refusing:** subclass the control and override `acceptsFirstResponder` to return `false`. Expect the fallback.
2. **Detached:** `removeFromSuperview()`. Expect the fallback.
3. **In another window:** move the origin to a second `NSWindow`. Expect the fallback.
4. **Eligible:** expect the origin itself.

A detached-only test passes even when the code ignores refusal. Assert the list of requested targets.

**Ordinary path:** opening, then Close, then completion restores once. Escape or cancel follows the same path.

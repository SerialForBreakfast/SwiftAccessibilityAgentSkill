# Callbacks after reuse, update and teardown

## Decide

- **Configure replaces; it never adds.** UIKit can reuse a cell or view without calling `prepareForReuse()`, and a SwiftUI representable calls `update…View` many times on the same view. Each configure must replace the title, value and callback: remove the earlier action by identifier, or reassign `target`/`action`, before installing the new one. Otherwise one press fires twice.
- **An old callback must do nothing.** A callback created for earlier content survives in many places: in another view that was reused, in a custom action someone retained, in a closure SwiftUI kept. It must not act after the control was reconfigured, moved to another view, stopped or dismantled.
  - Guard it with a token captured *when the callback is created*, and compare it with current state *when it runs*:
    ```swift
    let token = generation                 // captured at creation
    return { [weak owner = self] in
        guard let owner, owner.generation == token else { return }
        …
    }
    ```
  - Reading "the latest ID" or taking a new token at invoke time cannot detect an old callback.
- **Enablement:** a disabled control or action rejects dispatch. Ordinary buttons stay connected after a fix.
- **Shortcuts belong to an element people reach.** Put `accessibilityCustomActions` on an element with `isAccessibilityElement = true`, or on a child that is one. A container with `isAccessibilityElement = false` exposes its children, not its own actions. Making a row one element hides its nested buttons unless you re-expose them as custom actions.
- **Reloaded outlines and lists:**
  - keep node identity stable across rename and reorder;
  - restore selection by ID, not row number, and keep surviving expansion;
  - clear selection when its node is gone; a removed node's handle stops serving data.
- **Saved state is separate.** A "Saved" or "Selected" product state is model state, not the collection's transient selection. Changing one must not rewrite the other. Reconfiguring a cell clears a stale selected trait without dropping its other traits.

## Fix pattern

```swift
func configure(_ button: UIButton, for item: Item) {
    generation += 1
    let callback = makeCallback()              // captures the new generation
    button.removeAction(identifiedBy: .init("primary"), for: .primaryActionTriggered)
    button.addAction(UIAction(identifier: .init("primary")) { _ in callback() }, for: .primaryActionTriggered)
}
func stop() { generation += 1 }                 // dismantle/teardown retires everything
```

AppKit target/action: reassign `target` and `action` on each configure, and clear them on the old control when the owner moves to a new one. For `NSAccessibilityCustomAction(name:handler:)`, the handler closure carries the same token check.

## Test: keep the old callback, then call it

**The wrong test:** configure A, reconfigure B, then press the current control. Reconfiguring replaced the control's action, so the old callback never runs. That test passes even when the token guard is deleted.

**Right:** obtain the old callback *before* reconfiguring, then invoke it while B is live. Without the guard, the old callback usually calls B's handler, so expect B's handler to run exactly once.

```swift
@MainActor func testOldCallbackIgnoredAfterReconfigure() {
    let subject = Binder()
    let oldButton = UIButton(type: .system)
    let newButton = UIButton(type: .system)
    var log: [String] = []
    subject.bind(oldButton) { log.append("A") }
    oldButton.sendActions(for: .primaryActionTriggered)          // A works
    subject.bind(newButton) { log.append("B") }                 // moved to another control
    oldButton.sendActions(for: .primaryActionTriggered)          // old control still holds the old action
    newButton.sendActions(for: .primaryActionTriggered)         // ordinary path
    XCTAssertEqual(log, ["A", "B"])
    subject.stop()
    newButton.sendActions(for: .primaryActionTriggered)         // after teardown
    XCTAssertEqual(log, ["A", "B"])
}
// Without the generation check: the old control calls the new handler, so log == ["A", "B", "B"].
```

**Ways to hold an old callback** (pick the one the code uses):

| The code installs… | Keep this before reconfiguring | Invoke it later |
|---|---|---|
| a `UIAction` on a control | the old control itself (bind to a second control) | `old.sendActions(for: .primaryActionTriggered)` |
| a callback factory | `let old = subject.makeCallback()` | `old()` |
| `UIAccessibilityCustomAction` | `let old = view.accessibilityCustomActions![0]` | `_ = old.actionHandler?(old)` |
| `NSAccessibilityCustomAction` with a handler | `let old = view.accessibilityCustomActions()![0]` | `_ = old.handler?()` |
| AppKit target/action | `let old = button` (bind to a second button) | `old.performClick(nil)` |

- **Refreshed list or rows: keep the same record ID across the refresh.** Apply the same rows again, or the same ID with a new title, then call `old`. If the refresh swaps in different IDs, `old` finds no record and does nothing even with the guard deleted, so that test proves nothing.
- **Same control reused for new content:** take the custom action or factory callback (`old`), reconfigure, then call `old` and the current control. Assert the recipient and the count, not just a Bool return.
- **SwiftUI representable:** you cannot build a `Context` in a test. Call the coordinator the way `update…View` and `dismantle…View` do: make it with `makeCoordinator()`, then call its configure and stop methods with real controls.
- **Disabled:** configure with `enabled: false` and assert that an old and a current invocation both leave the log unchanged.
- **Duplicate dispatch:** configure twice for the *same* item, press once, and assert exactly one entry.

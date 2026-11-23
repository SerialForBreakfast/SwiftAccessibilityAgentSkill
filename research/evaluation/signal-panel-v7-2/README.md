# Signal-v7.2: signal-v7.1 plus lines aimed at its regrade failures

Signal-v7.2 is a research draft. It is [signal-v7.1](../signal-panel-v7-1/README.md) plus 15 added lines, each aimed at a failure cluster from the [source regrade](../../../evals/reports/signal-v7-source-regrade/README.md) of requests 1510 and 1511. Signal-v7 and signal-v7.1 stay frozen. Released 0.2.2 and rc.2 are unchanged. No model has run v7.2.

**These lines were written from failures on the same 56 panel questions.** A v7.2 run on that panel measures development fit, not generalization. See [DECISIONS.md](DECISIONS.md).

## What changed against v7.1

| File | Added guidance | v7.1 failures it targets |
|---|---|---|
| `references/callbacks.md` | When a control holds the action, keep that control and press it after rebinding; a second factory call is a new closure. The factory row now applies only when no control holds the result. | Stale-action proofs built from a fresh factory call (3 questions; 1 more in v7) |
| `references/dismissal.md` | SwiftUI sheets: Close only clears the binding, completion happens in `onDismiss` (also after swipe or Escape), and with `sheet(item:)` the item is already `nil` there. | Completion done in Close with an empty `onDismiss`; `onDismiss` reading a cleared item |
| `references/dismissal.md` | Get the dismissal closure the way the view does; if `onDismiss` reads a `@State` ticket at fire time, change the view first. Add a cancelled-dismissal case. | Model-only tests with a ticket passed by hand (3 questions); missing cancel case (1) |
| `references/media.md` | Test the retained binding across a same-item reload as well as a replaced item. | Replacement-only stale-binding tests (2; 2 more in v7) |
| `references/media.md` | When tvOS is the target, the seam test runs on tvOS rather than compiling to `XCTSkip`. | Tests skipped on the requested tvOS target (2; 1 more in v7) |
| `references/media.md` | Store the read-back selection in an observable property so the picker redraws. | Picker not refreshing after a native write (1) |
| `references/facts.md`, `references/apis.md` | An AppKit row check asserts element status, role, selected and expanded state, and child labels; the four row getters are added to the API list. | Row checks missing exposure assertions (2) |

`SKILL.md` changes only its version string. Not addressed: the overlapping UIKit panel snapshot, the missed native-edit path, the outline restoration helpers and the row that hides its buttons. The existing guidance already covers each of them.

## Offline checks

| Check | Command | Result |
|---|---|---|
| Reproducible build, leak and link guards, size | `python3 -B research/evaluation/signal-panel-v7-2/build.py --check` | `f2b89677…`, entry 2,858 B, total 31,111 B |
| No new 8-word overlap with protected texts | `python3 -B research/evaluation/signal-panel-v7-2/screen.py` | PASS: 1,400 protected texts, including 586 preserved v6, v7 and v7.1 answers and the regrade reasons |
| Copied recipe blocks unchanged from v7.1 | `python3 -B research/evaluation/signal-panel-v7-2/qualify/qualify.py --static` | PASS: all five recipe tests, `ReturnCoordinator`, `makeMediaItem`, subjects and wrong tests identical, so v7.1's native receipt still covers them |
| Recipe qualification and AppKit getter probe on simulators | `python3 -B research/evaluation/signal-panel-v7-2/qualify/qualify.py` | not run: needs Xcode; this draft was made on Linux |

`qualify/` is v7.1's qualifier pointed at the v7.2 cards. It adds one macOS test, `testAppKitRowGetters`, which compiles the two new `apis.md` lines verbatim on an `NSTableRowView` and checks each result type, including `[Any]?` for `accessibilityChildren()`. It does not test the `sheet(item:)` claim; that needs an SDK or documentation source.

The screen now treats v7.1 text as inherited and adds the v7 and v7.1 smoke answers and the source-regrade reasons to the protected corpus. The 1507 return zip in the shared folder was not present, so v6 answers come from the local 1507 and continuation records.

## Not done

- No native qualification, so the new AppKit getters are not typechecked and the `sheet(item:)` claim is not confirmed. A handoff to the Mac worker is prepared but not sent.
- No sealed smoke packet and no run. Dispatch needs owner approval of seal, transport, model, scope, quota and stop policy.

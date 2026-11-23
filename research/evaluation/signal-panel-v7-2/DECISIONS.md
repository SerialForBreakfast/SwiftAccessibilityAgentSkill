# Signal-v7.2 decision log

## Cycle 1: lines from the signal-v7 source regrade (November 22)

### Evidence

The blind source regrade of requests 1510 and 1511 (frozen grades `a596cb52…`, private results `evals/results/signal-v7-grading/`) failed signal-v7.1 on 20 of 56 whole answers. Most of those failures go against guidance v7.1 already gives, so the added lines make existing rules more specific rather than adding new topics:

- Stale-action proofs used a fresh factory call although the code installs the action on a control. v7.1's own table offered the factory form without saying when it applies.
- SwiftUI sheet answers completed from Close, left `onDismiss` empty, or read a cleared `sheet(item:)` item.
- Caption-binding tests covered replacement by a different item but not a same-item reload.
- tvOS media tests compiled to an unconditional `XCTSkip` on the requested target.
- AppKit row checks omitted element status or expanded state.

Owner instruction, November 22: "ok lets keep iterating".

### Decision

Add 15 lines in five cards and change nothing else, so a later difference against v7.1 can be attributed to them. Keep v7 and v7.1 frozen.

### Risks and open items

- **Development fit.** Every line targets a failure observed on the 56-question panel, and both new versions' answers are now in the protected corpus. A v7.2 run on that panel is a development measurement. Claiming improvement beyond it needs fresh questions.
- **Unverified claims.** The four AppKit row getters (`isAccessibilityElement()`, `accessibilityRole()`, `isAccessibilitySelected()`, `isAccessibilityExpanded()`, `accessibilityChildren()`) are standard `NSAccessibilityProtocol` members but were not typechecked here. "With `sheet(item:)`, the item is already `nil` when `onDismiss` runs" comes from the regrade evidence, not a cited Apple source. Both need a native check or a source before promotion.
- **Test-oracle defect (resolved in cycle 3).** The overlapping-sheet cases on macOS SwiftUI require a fix in which the view's installed `onDismiss` does not read the latest `@State` ticket. The repository's own reference view read that ticket at fire time, so under the criterion the reference itself would have failed.
- **No pattern for the view.** The new dismissal lines say what not to do and how to test, but they do not prescribe SwiftUI wiring that distinguishes A's late `onDismiss` from B's. Cycle 3 found a natively hosted pattern (capture the ticket in `onDismiss`); it is not yet in the cards.

### Not done

- No native qualification (Linux session, no Xcode).
- No sealed smoke packet, no dispatch.

## Cycle 2: native check prepared (November 22)

Owner instruction, November 22: port the qualifier, commit and push, and prepare the Mac handoff without sending it.

- `qualify/qualify.py` is v7.1's qualifier pointed at the v7.2 cards, with receipts under `evals/results/signal-v7-2-offline/`.
- Added `testAppKitRowGetters` (macOS only): the two new `apis.md` lines compiled verbatim, with each result type checked. A wrong name or type fails the macOS build in every mode, so the whole batch reports a mismatch.
- `--static` confirmed here that every copied recipe block, the subjects and the wrong tests are byte-identical to v7.1. The native run is still needed for the getter probe and to show the v7.2 build compiles on the current toolchain.
- The `sheet(item:)` claim is not testable under the unit-test-only rule without hosting a presented sheet. The handoff asks for the SDK's own documentation text instead. If none supports the claim, the line is removed or softened before promotion; no UI test is added.

## Cycle 3: reference view fixed (November 22)

Owner instruction, November 22: "fix the reference view for Q10/Q43".

- `code-examples/swiftui/macos-v1/Sources/Lifecycle.swift` revision 4 captures the ticket in the installed `onDismiss` (`{ [ticket] in`), so A's closure keeps A's ticket after B opens. This is the only change. Manifest revision 3 → 4, with the new hash.
- The change is byte-for-byte the positive control `control-captured`, which passed the hosted macOS installed-callback test (batch `sheet-extra-0suc98ey`, Xcode 27.0; subject `ea12a01e…`, contract `2d57e457…` recomputed here). The revision-3 starter failed the same test (batch `sheet-answers-ea4h1pu_`). No native run in this session.
- Not changed: the panel questions (Q43 embeds revision 3 and Q10 embeds the unguarded negative fixture, both frozen), `NegativeFixtures/lifecycle.swift`, the model-only contract tests, and historical records that cite the old hash. `answers/prepare.py` and `answers/extra.py` now stage revision 3 from git commit `0177195`, so they still reproduce their recorded batches.
- Owner instruction, November 22: "apply to iOS and tvOS too". The iOS and tvOS SwiftUI packages carried byte-identical copies of revision 3; both now hold the same revision-4 bytes, with manifests and rubrics updated. The hosted proof is macOS-only, so on iOS and tvOS the fix is source-equivalent, not natively proven.
- The grading criterion stands; the reference now meets it. The fix does not show how SwiftUI schedules a late dismissal relative to a new presentation.

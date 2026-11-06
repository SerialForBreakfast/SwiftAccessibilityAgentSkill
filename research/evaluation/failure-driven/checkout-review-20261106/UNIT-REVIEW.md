# Focused UIKit Unit Review

Follow-up: [BigDog accepted the scoped unit evidence](ADJUDICATION.md) at cursor
1425. Pending-review statements below preserve the execution-time state. The
eight-answer review is closed without additional subject builds or repairs.

Revision 1, 2026-11-06. Owner authorized continuing focused unit tests while
preserving first failures. BigDog inbox through cursor 1423 contains no new
feedback; the shared folder has no newer review return. External reconciliation
remains pending, not silently accepted.

## Predeclared Scope

R12, R13, R14 and R16 are eligible because their first type-check succeeded.
R04, R08, R09 and R10 retain their first compile failures; none is repaired or
included in this execution. SwiftUI remains deferred.

Two assertions groups per answer:

| Test suffix | Contract | Limits |
| --- | --- | --- |
| TextConfiguration | Supplied total retained, multiline label, automatic content-size adjustment enabled, font text-style metadata present | Configuration only; no rendered text, actual font growth or live trait propagation assertion |
| PreservesButtonTypography | Existing title, font descriptor and automatic-scaling flag preserved after configuring the answer | Synthetic preconfigured system button; not a visual comparison or proof for every UIButton configuration |

The test fixture supplies a 19-point regular button font, disables its automatic
font adjustment, then records the font descriptor before invoking the submitted
setup. This makes the prompt's preservation requirement falsifiable without
requiring one preferred font in the answer. The label assertion accepts both body
and headline styles and does not demand an axis-switching implementation.

Expected before execution: R16's typography test fails because its source changes
the font and scaling flag. This is a prediction about an **original answer**, not
a deliberately injected mutant. An adapter status of `passed` for an expected
failure means the predicted rejection was observed, not that the answer passed.
Any unexpected failure remains evidence and requires classification before repair.

## Reproduction and Preservation

[Builder](build-unit-packet.mjs) verifies input source hashes against the preserved
[first results](results.json), then creates a new private packet. It only suffixes
host class names to avoid collisions. Submitted code fences remain unchanged.
The original source, scaffold and compiler diagnostics are not overwritten.

```sh
node research/evaluation/failure-driven/checkout-review-20261106/build-unit-packet.mjs \
  /absolute/private/first-review /absolute/private/new-unit-inputs
node code-examples/tools/native.mjs plan \
  /absolute/private/new-unit-inputs/manifest.json checkout-unit-first
node code-examples/tools/native.mjs execute \
  /absolute/private/new-unit-inputs/manifest.json checkout-unit-first \
  /absolute/private/new-unit-run EXISTING_IOS26_SIMULATOR_UUID
```

Execution requires explicit owner approval and an installed matching runtime.
The adapter records toolchain, actual runtime/build, manifest, commands, input
snapshots, XCTest identifiers, logs and result summary. Never reuse output paths.

No payment callback is invented, dispatched or scored. No stack accessor, hierarchy
attachment or lifecycle call is added to the subject to make testing easier.
No UI tests, manual verification, models, installs or skill changes are included.

## Reconciliation Boundaries

- Compiler success does not establish layout/task success. R12/R14 concerns remain
  provisional even if these limited configuration tests pass.
- A typography failure supports the specific preservation finding, not a broad
  claim about model competence or which condition is better.
- Earlier first-attempt grades and diagnostics remain immutable. New unit outcomes
  are a separate evidence layer for BigDog to adjudicate.
- R13's static vertical layout remains an accepted-alternative candidate; this
  packet imposes no mandatory axis-change callback.
- These are existing development cases, not independent holdouts or new gold
  prompts. Any future prompt/rubric change needs a separate reviewed revision.

## Executed First Outcome

All eight selected XCTest methods executed: **seven passed, one failed, none
skipped**. Build succeeded. Runtime: iOS 26.5 (23F77), arm64 simulator; Xcode
27.0 (27A266a), SDK 27.0 (24A430), deployment target 26.0. No repairs or reruns.

| Answer | Text configuration | Button typography | Reconciliation |
| --- | --- | --- | --- |
| R12 | Pass | Pass | Multiline autoshrink and initial trait-context questions remain source-review concerns, not demonstrated runtime failures |
| R13 | Pass | Pass | Narrow configuration evidence supports retaining this alternative; overall layout still unassessed |
| R14 | Pass | Pass | Horizontal layout adequacy remains unresolved; this pass does not settle it |
| R16 | Pass | Fail | Confirms font descriptor and scaling-flag changes under the synthetic preservation fixture |

Exact first assertion messages, retained with complete private source/logs:

```text
XCTAssertTrue failed - Existing button font descriptor changed
XCTAssertFalse failed - Existing button scaling configuration changed
```

Both occur in `CheckoutAnswerTests/testR16PreservesButtonTypography`. The XCTest
summary lists one failed method and summarizes its first assertion; the full log
preserves both diagnostics. Do not count them as two failed scenarios. The runner's
`passed` status means the predeclared failure set matched; XCTest itself failed.

[Sanitized unit evidence](unit-results.json) records exact test IDs, environment
and artifact hashes. Private native evidence retains commands, source snapshots,
adapter snapshots, process result, full logs and xcresult. The original first
compile packet was hash-verified unchanged after the run.

Repository checks: 201 offline tests passed, 210 frozen baseline files verified,
87 historical evidence pins verified. External adjudication remains pending.

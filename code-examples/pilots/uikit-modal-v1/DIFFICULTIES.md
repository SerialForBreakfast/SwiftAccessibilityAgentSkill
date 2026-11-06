# UPAIR-04 Difficulty Ledger

Local date2026-11-05. Assisted development, not controlled model evaluation.
Serving-model revision and full context are unavailable. Preserve actual failed
attempts separately from intended mutants and design risks.

| ID | Difficulty | Treatment / prompt implication |
| --- | --- | --- |
| M01 | Approval initially interpreted the old planning-stage pause as active and rejected native execution | Resubmitted the unchanged bounded command with the user's explicit continuation and active UIKit goal; approved. Clarified the PRD's historical pause without making the plan itself execution authorization. No bypass. |
| M02 | Apple web pages returned HTML shells | Reviewed installed headers and pinned hashes; do not claim the web API body was retrieved. |
| M03 | Resetting background state to false would overwrite a pre-existing true state | Test both initial values and preserve the exact snapshot. Anticipated lifecycle defect, not a spontaneous failure. |
| M04 | Looking up a return target when dismissal starts can become stale | Read the current weak target on completion and test replacement/release. A captured request is not actual focus evidence. |
| M05 | Merely checking closing state cannot distinguish two dismissal generations | Hold the old completion, teardown/reopen, start a new dismissal, then invoke the old callback. This boundary is stronger than a repeated-close test. |
| M06 | Hiding a root ancestor could also hide the panel | Reject an overlapping background subtree and document separate ownership. The rubric accepts structural alternatives rather than prescribing these exact guards. |
| M07 | Teardown and asynchronous completion have different intent | Explicit owner teardown restores state and invalidates callbacks; notification choice is scoped and alternatives remain acceptable. No claim that this fixture manages arbitrary nested modal stacks. |
| M08 | Review of the green11-test suite found that weak-target release did not cover a removed view still retained elsewhere | Preserve revision1, then add a retained-but-detached target test against the unchanged implementation before repairing it. This is a coverage-discovered candidate defect, not a manufactured mutation; execution evidence will determine the actual failure. |

M03-M07 are pre-execution design/oracle concerns. Any unexpected compiler/assertion
failure will retain exact code, environment and diagnostics before repair. Exact
manufactured defects belong in MUTATIONS.md, not spontaneous-model failure counts.

## Observed Implementation Defect: Retained Detached Target

Revision1 passed11 methods. Revision2 retained its source unchanged but added a
test that removes a strongly retained target from the background before completion.
The12-method run failed only `ModalUIKitTests/testRetainedButRemovedTargetPostsNil`:

```text
XCTAssertNil failed: "<UIButton: <address>; frame = (0 0; 0 0); opaque = NO; ...>"
```

That excerpt is abbreviated; the full sanitized assertion is in
[revision2 evidence](validation/revision-2.json). Exact source and tests remain under
`history/revision-2/`. This is a reproduced coverage-discovered implementation defect,
not one of the manufactured negative variants and not a controlled model score.

Before:

```swift
let target = returnTarget
```

Revision3 repair:

```swift
let target = returnTarget.flatMap { candidate -> UIView? in
    guard let background, !priorHidden, candidate.isDescendant(of: background) else { return nil }
    return candidate
}
```

The original source is retained as the new DetachedTarget negative control. A weak
reference establishes lifetime, not membership in the current hierarchy. The
independent question already includes removed/replaced targets; its rubric now
explicitly checks retained removal and permits alternate valid target resolvers.

## Evidence Redaction Correction

The first sanitized regression report still contained the `/tmp/` run-directory alias
because the formatter only replaced its `/private/tmp/` alias. Review caught this;
both aliases are now removed from public excerpts. Original private records and
their hashes are unchanged. This is an evidence-formatting error, not a native
test failure; no diagnostic or failed assertion was discarded.

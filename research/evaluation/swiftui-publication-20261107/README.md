# SwiftUI Checkpoint Publication And Upstream Reconciliation

Local evidence checkpoint: `3cf7cb5`. Upstream imported through
`0d1f3a213cf42ad39bc594cea75ea5c1cb4a90e1`; merge `7975421` preserves both histories.
The sole textual conflict was append-only `Tasks.txt`; both complete additions
remain present. No released skill, frozen baseline or sealed BigDog input changed.

## Validation Without Rewriting Historical Pins

The original 1,332-check run passed before merging. Upstream legitimately changed
seven non-runtime files that the old all-tracked checkpoint guard pins, including
`AGENTS.md`. That epoch-specific guard remains unchanged and passes against the
export of its own source checkpoint. It is not silently relaxed or rewritten.

The current replacement verifies every original pin. Only the seven explicitly
recorded upstream files may differ, and each must exactly match the incoming Git
blob while the historical hash must match the original base. Runtime/baseline/sealed
paths are forbidden in that exception list. Prior batch and inherited package pins
are separately verified. Both merge parents and task histories are checked.

- Current merged suite: **1,338 passed**, zero failed.
- Original historical module: **25 passed**, zero failed. These overlap current
  tests and are not added as independent cases.
- Baseline verifier: **210 source files**; historical evidence verifier: **87 pins**.
- Original native receipts remain unchanged; no native/model runs were repeated.

```sh
node research/evaluation/swiftui-publication-20261107/validate.mjs
```

The runner exports trusted historical source into ignored `evals/results/`, runs
the historical guard there, and uses the replacement guard for the live merge.
All new logs, fixtures, scratch and cache paths stay inside this project, following
the incoming workspace policy. Existing externally archived native receipts remain
historical evidence; this publication does not relocate or overwrite them.

The broad unfiltered suite initially reported the expected epoch mismatch. A new
conflict-marker assertion also initially mistook a preexisting heading underline
for a merge marker; it now matches complete marker syntax. Initial diagnostics and
validation attempts are retained privately under `evals/results/`. No accessibility
lesson or gold prompt is inferred from these publication-harness issues.

See [exact authorized hashes](reconciliation.json), [live checks](integrity.test.mjs)
and [validation record](validation.json).

## BigDog Progress Imported, Not Re-executed

Upstream records the independent review of the original 24-case/48-payload package,
grading-interpretation repairs in a separate composite controller, preserved AGY
intake and the held native-activation experiment. Six controls have bounded
acceptance; domain evidence remains provisional. Source review is not a completed
frontier comparison or a quota reservation.

The next highest-value step is to qualify the exact isolated text-only Gemini
adapter, finish the controller/calibration gates and return one bounded proposal
for owner approval. Do not substitute models, resume held work or alter the sealed
v2 payloads. Dev.6 remains a separate future research comparison candidate.

References: [upstream next experiment](../NEXT-EXPERIMENT-20261107.md),
[independent review](../independent-v2-review-20261107/REVIEW.md),
[local corrective results](../swiftui-review-v1/RESULTS.md).

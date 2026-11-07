# Local replay: GP26-03 UIKit checkout

This replay uses the original checkout question and original native harness, not the later RC.1 single-function interface. It does not qualify a general-purpose worker. The historical first attempts, their diagnostics, neutral IDs, and source judgments remain immutable.

## What went into the replay

The replay verifies the two BigDog export hashes, all eight answer hashes, the user prompt, all extracted Swift fences and the exact first-pass scaffolded source per answer. The existing builder reconstructs the four previously compiling subjects and the original XCTest assertions. The resulting manifest and every unit input are compared byte-for-byte with the archived unit packet before native execution. Only code in those pinned sources is tested. Original Markdown is not treated as Swift. No answer repairs, renamed subject functions, inferred callbacks, model/provider calls or paid dependencies.

For an authorized replay from the project root, supply the private share containing the two original checkout archives, a **new** ignored output path under `evals/results/`, and an existing iOS 26.5 simulator identifier:

```sh
python3 -B research/evaluation/checkout-local-replay/replay.py <archive-directory> evals/results/<new-attempt> <simulator-id>
```

## Harness gaps (not subject failures)

- R04 mixes setup statements and member declarations in one fence. The original recorded partition is preserved; its type-check outcome applies to that partition, not every conceivable integration.
- The four eligible unit inputs use the historical host class name suffixes to avoid collisions. No new adaptations were made. The suite intentionally does not synthesize missing methods, payment dispatch, layout attachment, or trait-change delivery.
- The two tests per compiling answer observe text configuration and preservation of an existing button's typography. They cannot decide whether a long translation fits on screen, an actual payment works, or a user can navigate the finished checkout.
- The separate BigDog dev.5/dev.7 archive (48 Flash and 14 Haiku answers, 24 distinct questions) has verified original answer and sealed-input hashes. Those tasks used a design/source rubric rather than the RC.1 Swift file ABI. Their original source grades stand. No new executable grade is assigned from topic similarity.

## Observed grades

The [new local receipt summary](results.json) matches every historical type-check exit and every original executed/failed XCTest method ID. Xcode 27.0, SDK 27.0 (24A430), deployment 26.0; XCTest ran on iOS 26.5 (23F77). No infrastructure failure or skipped method.

| Answers | Observed result |
|---|---|
| R04, R09, R10 | Type-check failed: `summary` not in scope. R04 has the partition limitation above. |
| R08 | Type-check failed: `self.updateSummaryAxis` is not a member. |
| R12, R13, R14 | Compiled; both original configuration methods passed for each. |
| R16 | Compiled; text configuration passed. One typography method failed two assertions: both the existing button font descriptor and its automatic-scaling flag changed. |

Seven of eight XCTest methods passed. The adapter's expected-failure match means the predicted R16 failure was reproduced, not that R16 passed.

# Research Findings For A Later Candidate

No entry here changes the released skill or BigDog's sealed comparison inputs.
These are proposals backed by bounded code observations, not measured answer lift.

| Proposed improvement | Evidence | Candidate acceptance |
| --- | --- | --- |
| Separate an option's displayed selection from the actual AVPlayerItem selection | `testBindingWritesNativeSelection`, `testBindingReadsExternalSelection`, disconnected-binding mutant | A later candidate fixes real selection, not just a selected string; accepts equivalent native APIs |
| Keep old work from owning a newly loaded item | Item replacement, duplicate replies, old errors, cancellation and pre-cancelled-task methods | Correct current-item and async ownership without prescribing this exact ticket architecture |
| Treat observable invalidation as a separate wiring contract | `testBindingWriteInvalidatesObservableSelection`, invalid-choice counterpart | Tested store notifications; no unsupported claim about rendered SwiftUI accessibility semantics |
| Preserve native choices rather than guessing defaults | Preserved failed nil oracle and corrected preservation test | Review allows valid existing behavior and does not demand unnecessary resetting |
| Distinguish full subtitle choices from forced-only tracks when the product requests full captions | Tagged fixture and forced-only mutant | Policy is explicit; do not generalize it into an Apple requirement to hide all forced tracks |
| Keep ordinary player controls and supplementary controls separate | Actual compiled VideoPlayer/Picker composition | No unsupported claim that source compilation proves visual overlap, speech or reachability |
| Select platform-specific evidence, not another framework's defaults | Three actual compile/runtime lanes and SDK selectors | SDK, deployment and tested runtime are reported separately |

## What Not To Distill Into Accessibility Guidance

- XCTest autoclosure syntax and Swift 6 fixture-isolation repairs belong in the
  general Swift diagnostic lane unless a user is asking to author those tests.
- Adapter snapshot packaging is a maintainer/harness issue.
- A selected forced option in one local fixture is not a universal default.
- Manual verification, UI tests and finer-grained historical OS support are not
  required by this companion approach.

## Promotion Sequence

Finish independent oracle/source review, combine accepted findings into one later
candidate batch, then compare frozen conditions on the same scenarios. Keep known
incidents in development cases. Preserve a separate held-out scenario split; these
new authored questions do not create holdouts or prove a model ranking.

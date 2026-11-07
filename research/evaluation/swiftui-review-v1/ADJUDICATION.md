# Review Adjudication

Reviewer: one separate-context agent, two read-only source-review turns. The
initial [original review](original-review.json), exact retained
[follow-up request](followup-request.json) and [follow-up review](followup-review.json)
remain separate from this author's adjudication. This is not external human
acceptance or a model-quality experiment. The reviewer inspected tests but did not
run them; native execution and receipt validation were performed by the author.

| Finding | Decision | Evidence and remaining scope |
| --- | --- | --- |
| F1 stale Off changes a newer snapshot | Accepted and corrected | Native reproduction on unchanged v1; v2 captures item/generation for nil and non-nil writes; reload/replacement tests and stale-Off mutant |
| F2 item/store replacement synchronization | Accepted with bounded correction | Old owned completion exits loading on item change; task key includes store identity. External item changes still require explicit reload; no automatic observation claim |
| F3 cancellation timing | Accepted by explicit contract narrowing | Task.cancel remains cooperative; explicit store.cancel invalidates while the loader is suspended. The test distinguishes them before resuming old work |
| F4 selected filtered option appears Off | Accepted and corrected | Forced selection reproduced on v1; v2 has a Current/unlisted tag and does not clear native selection |
| F5 prompt/rubric fairness | Accepted and corrected | New complete media-only starters remove form/generation scaffolding, explicitly request tests and separate correctness from execution evidence. Harmless extra invalidation is accepted |

The second source-review pass closed all five findings within these contracts and
reported no new actionable defect. Corrected native suites subsequently passed on
all three anchors. Broader generated semantics, live stream observer lifecycle,
external native observation and model-answer improvement remain outside this result.

## Why The Original Pass Record Stays

The original 36-method suites genuinely passed. They did not cover stale Off after
a new successful snapshot or distinguish an unmapped active native option from Off.
Preserving those passes alongside the new reproduction shows an oracle/coverage gap,
not fabricated historical success or evidence that the whole original suite was
invalid. The old examples and nine questions remain immutable at v1 paths.

## Candidate Incorporation

Accepted lessons enter the additive `0.3.0-dev.6` research candidate, not the released
skill or BigDog's sealed comparison. The candidate teaches outcomes rather than
requiring this example's ticket architecture. Syntax/harness diagnostics remain
maintainer evidence. The corrected nine questions remain development cases, not new
holdouts, and are not relabeled as independently executed model answers.

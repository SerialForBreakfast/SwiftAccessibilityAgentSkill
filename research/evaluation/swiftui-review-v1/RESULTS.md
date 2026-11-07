# Review-Corrected Results

## What Changed

A separate-context source review found gaps that the previous passing suite did not
exercise. Three new assertions reproduced the unchanged v1 defects: stale Off after
reload, stale Off after item replacement, and a selected forced-only option being
represented as Off. This is direct failure evidence, not a model-ranking anecdote.

The v2 example corrects snapshot ownership for nil/non-nil choices and represents an
unlisted current selection separately. It also includes store identity in the task
key and leaves loading when a pending owned completion detects item replacement.
External changes still require explicit reload. Cooperative task cancellation and
immediate explicit owner cleanup are distinct, documented contracts.

## Native Evidence

| Platform | Positive methods | Tested runtime | SDK / deployment |
| --- | ---: | --- | --- |
| iOS / SwiftUI | 44 | 26.5 | 27 / 26 |
| macOS / SwiftUI | 44 | 27.0 | 27 / 26 |
| tvOS / SwiftUI | 44 | 26.5 | 27 / 26 |

All three source compiles and positive suites pass. Two new macOS shared-code
mutants fail at their intended assertions. The three-case defect reproduction on old
source remains a separate incident check, not a deliberate mutant or corrected
positive. Nine native attempts are retained with original hashes and artifacts.

There are eight additional test methods beyond the previous36, not44 new behaviors.
The final132 positive executions repeat44 definitions across three platforms. The
current original/forwarding/latest-media companions have147 method entries per
platform (62 +41 +44); superseded media-v1 methods are not added again. Counts do
not establish independent behavioral coverage or generated SwiftUI semantics.

See [results index](results-index.json), [private archive receipt](archive-receipt.json)
and [adjudication](ADJUDICATION.md). Public native receipts redact paths/device
identifiers and preserve original artifact hashes; private originals remain intact.

## Review And Evaluation

The second separate-context source pass closed all five findings within the revised
scope. It did not execute tests or provide human acceptance. The author separately
executed and validated the native receipts. No new source-review acceptance is
inferred for unrelated historical clauses or runtime interaction behavior.

Nine new prompt/rubric pairs use complete media-only starter inputs, request tests
explicitly and separate correctness from controller execution evidence. Three
implementation/contract diagnostics are excluded from grading assertion mappings;
harmless extra invalidation is valid. Cases remain development drafts with no
independent subject outputs or new holdouts.

Accepted lessons are distilled in the additive
[dev.6 research candidate](../failure-driven/candidates/0.3.0-dev.6/README.md).
Default media context reads one concern note plus a target SDK card. Full sources,
tests and fixture load only on request. This prototype measures bytes/read hashes,
not natural-language routing, model tokens or answer-quality lift.

## Unchanged Boundaries

Released skill, frozen baselines, BigDog's sealed comparison, previous candidates
and the original closure batch remain byte-identical. No Git publication, worker
message, frontier answer-generation evaluation, paid provider, UI test or mandatory
manual verification was performed. One review agent made two source-review turns;
that authoring activity is recorded separately from evaluation-model execution.

Live stream-state observer lifecycle remains an explicit separate implementation
remainder. External native observation and delivered speech/focus/layout are not
claimed by these units. Model lift still requires a later controlled comparison.

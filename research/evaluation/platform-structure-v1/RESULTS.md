# Native structure and form results

Status: native execution complete, author-checked; independent review pending.

| Metric | AppKit/macOS | UIKit/tvOS |
| --- | ---: | ---: |
| Positive unit methods | 28 | 29 |
| Form methods | 12 | 12 |
| Collection-specific methods | 16 | 17 |
| Deliberate mutants rejected | 7 | 7 |
| Current checks | 9 | 9 |

All 18 checks have expected outcomes: two compile checks, two positive suites,
and 14 intended negative rejections. There are71 method executions including
negatives, not 71 independent behaviors. Positive suites passed on their first
attempts; no assertion repair or native rerun was needed.

The form policy is shared across platforms and exercised via different native
entry points. Outline and shelf contracts are platform-specific. No unique-behavior
or coverage percentage is inferred from method counts.

## Exact environment

| Platform | Actual runtime | SDK | Deployment target |
| --- | --- | --- | --- |
| macOS | 27.0, 26A428, native host | 27.0, 26A425 | 26.0 |
| tvOS | 26.5, 23L470, simulator | 27.0, 24J360 | 26.0 |

Xcode 27.0 (27A266a), Swift 6.4, arm64. Mac27 execution is not Mac26 runtime evidence.
[Native index](results-index.json) links exact manifests, test IDs, artifacts,
outcomes and environments. Intentional-negative passes retain observed failure
and exact rejected test IDs. [Archive receipt](archive-receipt.json) identifies
durable private original inputs, commands, logs, summaries and xcresults.

## Asserted scope

Mac uses real NSOutlineView data-source queries, row/expansion/selection state and
named columns. TV uses custom UIView shelves, stored container order and ordinary
UIControl action dispatch. Forms use current native text, visible error controls,
optional help/hint restoration and native editing/action entry points. No UI tests,
layout rendering, automatic announcements, keyboard or directional-focus proof.

[Diagnostic observations](DIFFICULTIES.md) preserve nonfatal toolchain/service
messages and the inspected inventory-checker scope issue. No spontaneous subject
model failures or new model results are claimed.

## Cumulative companion status

Mac now has 119 positive methods (94 AppKit plus 25 AVFoundation); Apple TV has 121
(96 UIKit plus 25 AVFoundation). UIKit/iOS remains202. These totals describe bounded
code assertions, not complete platform accessibility coverage.

Four new draft question/rubric pairs bring the platform draft indices to 23 cases.
The original nine-case BigDog/Gemini plan remains unchanged. Independent review,
authorized model evaluation and skill promotion remain separate from native success.

## Integrity and preservation

The combined offline regression suite passed 323 checks; the new native-receipt,
prompt-union and retrieval integrity suite passed five more: 328 total, no failures
or skips. All 210 frozen baseline files verified against unchanged content hash
`3a1a2d58af19a94eec940000d9edcca7928bb5139aa3d52b1ef6e917c0271bbd`.
The earlier evidence archive verified 87 pins, 26 exact snippets, 17 reports, eight
incidents and 29 deliberate mutants. Older native suites were not rerun.

Only the historical media checker package-discovery logic changed, with its exact
original preserved and hashed in the additive amendment. Historical prompt indices,
question/rubric bytes and native receipts remain intact. No Git publication or
worker messages are part of this batch.

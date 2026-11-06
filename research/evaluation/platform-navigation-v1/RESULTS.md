# Mac navigation and Apple TV results: execution report

November 6, 2026. **34 new positive methods passed** across four behavioral families.
Eight deliberate mutants and one preserved original defect were rejected by their
intended assertions. All 13 current-manifest checks have matching execution receipts.

| Package | Positive methods | Deliberate mutants | Original-defect regression |
| --- | ---: | ---: | ---: |
| AppKit navigation, revision2 | 18 | 4 | 1 |
| UIKit/tvOS results, revision1 | 16 | 4 | 0 |

Mac: real macOS27.0 build26A428, SDK27.0 build26A425, deployment26.0.
TV: simulator tvOS26.5 build23L470, SDK27.0 build24J360, deployment26.0.
Both: Xcode27.0 build27A266a, Swift6.4, arm64 target. Mac26 runtime behavior was not tested.

## What passed and what failed

- Mac stable-ID selection survived reorder/rename; missing/filtered identities and
  duplicate inputs followed the explicitly requested policy.
- Key-view cycles respected ownership, visibility, enabled state and teardown after
  the first incoming-link defect was repaired. The original assertion did not change.
- TV result buttons preserved names, ordinary activation, selection identity and
  unrelated traits; removed/disabled/stale controls did not select a new item.
- Status content was available independently of animation, including Reduce Motion,
  later preference changes and localized messages.

The initial Mac source failed one of 18 methods. Its exact source, manifest and native
failure remain preserved, and `original-incoming-link` reproduces the same failure.
This is an author defect, not an independent frontier model result. See [analysis](DIFFICULTIES.md).

## Counts and reproducibility

There are 16 native attempts:15 met expectations and one was the original Mac positive
failure. These include three compile executions and 62 method executions across
positives, negatives and reruns. The tvOS repeated-animation negative ran twice:
the previously launched batch completed its original attempt, and the explicit
completion check used a new directory. Both receipts remain; this counts as one
mutant, not two independent behaviors.

[Results index](results-index.json) records input hashes, exact selected/failing IDs,
environments, diagnostics and original artifact hashes. [Private archive receipt](archive-receipt.json)
locates the full immutable native sources, tool commands, outputs and xcresult bundles.

The first platform batch remains unchanged; its Finder-metadata bookkeeping error
has a separate [additive amendment](../platform-expansion-v1-amendment/README.md).
Across the two platform batches there are 38 Mac and 38 tvOS positive methods passed.
The separate iOS companion remains 202 methods at its recorded anchor.

## Evaluation and remaining work

All four developer question/rubric pairs remain draft. Full available local authoring
records are described in the [prompt capture report](../prompt-records-v1/CAPTURE-ANALYSIS.md).
Authoring and native execution outputs are not responses to those independent draft
questions. No new model runs or independent review are claimed.

The additive retrieval candidate loads one guideline by default; source and contracts
are opt-in and traced. No runtime skill routing was modified. Remaining availability,
review and coverage work is in [sources](SOURCES.md) and [coverage](COVERAGE.md).
Unit tests do not establish delivered keyboard/focus/speech behavior or full layouts.
SwiftUI, released skill changes and frozen-baseline changes remain deferred.

## Final offline verification

The combined suite passed 281 checks. Baseline validation still verifies 210 frozen
files at `3a1a2d58af19a94eec940000d9edcca7928bb5139aa3d52b1ef6e917c0271bbd`;
all 87 older development-evidence pins remain valid. The original platform index is
unchanged and checked under its explicit Finder-metadata amendment. These offline
checks do not add native behaviors or model-evaluation results.

# Platform media results

Status: native execution complete, author-checked; independent review pending.

| Metric | macOS | tvOS |
| --- | ---: | ---: |
| Current positive methods | 25 | 25 |
| Deliberate mutants rejected | 7 | 7 |
| Current checks with expected outcomes | 9 | 9 |
| Initial failed positive suites | 1 | 0 |

All 18 current checks pass: two compile checks, two positive suites and 14 intended
negative rejections. Twenty attempts are retained, including the initial Mac
compile and the failed 23-method Mac suite (22 passed, one failed). Across reruns
and negatives there are 87 method executions, not 87 distinct behaviors.

The 50 current methods include 32 requalified metadata/inspection methods and 18
selection/policy methods, each conceptual family run separately on both platforms.
Synthetic fixture bytes and reusable tests are pinned to their existing originals.
No iOS evidence is silently promoted to another platform.

## Exact anchors

| Platform | Actual runtime | SDK | Deployment target |
| --- | --- | --- | --- |
| macOS | 27.0, 26A428, native host | 27.0, 26A425 | 26.0 |
| tvOS | 26.5, 23L470, simulator | 27.0, 24J360 | 26.0 |

Xcode 27.0 (27A266a), Swift 6.4, arm64. Mac27 runtime is not evidence of Mac26 runtime
behavior. Build logs retain the AppIntents metadata-extraction warning; there is
no AppIntents dependency and it did not prevent the compile/unit checks.

## First failure and correction

The initial oracle incorrectly expected the synthetic audio group to prohibit
empty selection. The native group permitted it. Revision2 follows the actual
permission and adds allowed/disallowed policy-seam assertions, including a guard
mutant. See [difficulties](DIFFICULTIES.md), original snapshots and
[full attempt index](results-index.json). The original failure is not erased or
reclassified as an intended mutant.

## Cumulative status

The companion now has 91 Mac methods (66 native UI/lifecycle plus 25 AVFoundation)
and 92 TV methods (67 native UI/lifecycle plus 25 AVFoundation). UIKit/iOS remains202.
Counts describe code assertions, not complete platform accessibility coverage.

Six new media pairs plus four lifecycle pairs remain draft, separate from the
original nine-case BigDog/Gemini plan. There are no independent subject answers for
these new questions, no model comparisons and no released skill promotion.

Original native artifacts are preserved in the private archive identified by
[receipt](archive-receipt.json). Public reports retain sanitized diagnostics and
input/artifact hashes; private paths/account details are not added to model inputs.

## Integrity verification

The combined offline suite passed 316 checks, with no failures or skips. The
baseline checker verified all 210 frozen files and unchanged content hash
`3a1a2d58af19a94eec940000d9edcca7928bb5139aa3d52b1ef6e917c0271bbd`.
Historical development evidence verified 87 pins, 26 snippets, 17 reports, eight
incidents and 29 mutants. Older native suites were not rerun in this batch.

The original nine-case index remains unchanged. Inventory checks now respect each
historical index's declared packages, while the latest media integrity test verifies
that all 19 platform questions are covered by the union of the three indices.
The prepared Gemini baseline still contains only its original nine cases.

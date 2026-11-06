# Mac navigation and Apple TV results batch

November 6, 2026. New development packages build on the published platform checkpoint
`f92c52f`; they do not replace its source, examples or execution records.

## Behavioral families

| Family | Framework | Positive methods | Question / independent controller rubric |
| --- | --- | ---: | --- |
| Table selection through refresh/reorder | AppKit | 10 | [Question](../../../code-examples/platforms/macos-navigation-v1/evaluation/table-selection.prompt.md), [rubric](../../../code-examples/platforms/macos-navigation-v1/evaluation/table-selection.rubric.md) |
| Owned key-view order and cleanup | AppKit | 8 | [Question](../../../code-examples/platforms/macos-navigation-v1/evaluation/key-order.prompt.md), [rubric](../../../code-examples/platforms/macos-navigation-v1/evaluation/key-order.rubric.md) |
| Filtered result actions and selection | UIKit/tvOS | 10 | [Question](../../../code-examples/platforms/tvos-results-v1/evaluation/filtered-results.prompt.md), [rubric](../../../code-examples/platforms/tvos-results-v1/evaluation/filtered-results.rubric.md) |
| Motion-independent status content | UIKit/tvOS | 6 | [Question](../../../code-examples/platforms/tvos-results-v1/evaluation/motion-status.prompt.md), [rubric](../../../code-examples/platforms/tvos-results-v1/evaluation/motion-status.rubric.md) |

Four pairs are **draft development cases**, not reviewed gold prompts or new holdouts.
No model comparisons were run. Questions include the required application policies;
controller rubrics accept alternative implementations and stay separate from subjects.

The batch has eight deliberate mutants and one original implementation regression.
See [results](RESULTS.md), [source evidence](SOURCES.md), [difficulties](DIFFICULTIES.md)
and [coverage decisions](COVERAGE.md). Method counts are not behavioral coverage percentages.

## Reproduce a contract

Use the unchanged platform-native adapter and a new output path for every attempt:

```sh
node code-examples/tools/platform-native.mjs plan code-examples/platforms/macos-navigation-v1/manifest.json positive
node code-examples/tools/platform-native.mjs execute code-examples/platforms/macos-navigation-v1/manifest.json positive /private/tmp/my-new-navigation-mac
node code-examples/tools/platform-native.mjs execute code-examples/platforms/tvos-results-v1/manifest.json positive /private/tmp/my-new-results-tv YOUR_EXISTING_TVOS26_SIMULATOR_UUID
```

Use `compile` or a manifest's exact negative check ID for other checks. Existing
Xcode, the actual Mac27 host or installed tvOS26 runtime are required. No installs,
UI tests, manual-verification gate or remote execution are part of this batch.
SDK, deployment target and runtime remain separate in each receipt. A blocked or
infrastructure-failed run never counts as a rejected mutant.

## On-demand retrieval candidate

```sh
node code-examples/tools/navigation-retrieval.mjs macOS AppKit table-selection
node code-examples/tools/navigation-retrieval.mjs macOS AppKit key-order example
node code-examples/tools/navigation-retrieval.mjs tvOS UIKit filtered-results contract
node code-examples/tools/navigation-retrieval.mjs tvOS UIKit motion-status example
```

Default reads one matching guideline. `example` adds that package's source;
`contract` adds its manifest and tests. It never loads rubrics, negative fixtures,
incident history or the entire companion by default. Actual byte/hash traces are
recorded; tokens remain unavailable. This additive tool delegates earlier topics to
the pinned router without changing their outputs. It is not installed skill routing.

## Review and promotion

Independent review is pending, not submitted or accepted. Review the four prompt
pairs, duplicate-ID policies, selection behavior, key-link ownership, original
failure and negative assertions. Reviewers should distinguish application policy
from Apple promises and actual stored state from delivered focus or speech.

After review, freeze a new development overlay and obtain scope/quota authorization
for frontier C0-C3 comparisons. Keep original subject answers and retrieval traces.
No released skill change follows from unit success alone. SwiftUI remains deferred;
all released and frozen files remain unchanged.

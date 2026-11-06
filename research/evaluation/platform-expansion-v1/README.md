# AppKit and tvOS companion expansion

Status: development evidence, November 6, 2026. Independent review and benchmark-backed
promotion remain pending. This is a bounded first platform batch, not platform-wide closure.

**[Executed results](RESULTS.md): 42 positive methods passed, ten mutants and one
original-defect regression rejected.** First failures and all reruns remain separate.

## Scope

- AppKit on macOS; UIKit on Apple TV. SwiftUI companion expansion remains deferred.
- Compile checks and unit tests only. No UI automation or mandatory manual verification.
- Two packages, five behavioral families, 42 positive methods, ten deliberate mutants and one original-defect regression.
- Deployment targets 26.0. Mac executes on the actual macOS27 host; this establishes
  no macOS26 runtime baseline. tvOS executes on the existing tvOS26.5 simulator.
- Frozen iOS tooling, released skill and baseline artifacts remain unchanged.
- No model runs, installations, paid usage or remote execution.

## Packages and evaluation pairs

| Family | Platform | Positive methods | Mutants | Question and rubric |
| --- | --- | ---: | ---: | --- |
| Names, ordinary actions, optional shortcuts and reuse | AppKit/macOS | 17 | 4 | [Question](../../../code-examples/platforms/macos-appkit-v1/evaluation/desktop-actions.prompt.md), [rubric](../../../code-examples/platforms/macos-appkit-v1/evaluation/desktop-actions.rubric.md) |
| State-change notification requests | AppKit/macOS | 3 | 1 | [Question](../../../code-examples/platforms/macos-appkit-v1/evaluation/desktop-status.prompt.md), [rubric](../../../code-examples/platforms/macos-appkit-v1/evaluation/desktop-status.rubric.md) |
| Card semantics, primary actions and reuse | UIKit/tvOS | 15 | 3 plus original-defect regression | [Question](../../../code-examples/platforms/tvos-uikit-v1/evaluation/television-actions.prompt.md), [rubric](../../../code-examples/platforms/tvos-uikit-v1/evaluation/television-actions.rubric.md) |
| Preferred focus candidate policy | UIKit/tvOS | 5 | 1 | [Question](../../../code-examples/platforms/tvos-uikit-v1/evaluation/television-focus.prompt.md), [rubric](../../../code-examples/platforms/tvos-uikit-v1/evaluation/television-focus.rubric.md) |
| Selected-trait preservation | UIKit/tvOS | 2 | 1 | [Question](../../../code-examples/platforms/tvos-uikit-v1/evaluation/television-traits.prompt.md), [rubric](../../../code-examples/platforms/tvos-uikit-v1/evaluation/television-traits.rubric.md) |

Draft questions are separate from controller rubrics, routes, implementation and
incidents. They are development cases, not new holdouts. Counts describe selected
assertions, not independent accessibility behaviors or observed model failures.

## Reproduce

From the repository root, plan without executing:

```sh
node code-examples/tools/platform-native.mjs plan code-examples/platforms/macos-appkit-v1/manifest.json positive
node code-examples/tools/platform-native.mjs plan code-examples/platforms/tvos-uikit-v1/manifest.json positive
node --test code-examples/tools/platform-core.test.mjs
```

Native execution requires installed Xcode and the selected existing runtime. Each
output path must be new; never overwrite a prior attempt. Mac uses the real host
and verifies the declared major; it cannot simulate macOS26 with a flag.

```sh
node code-examples/tools/platform-native.mjs execute code-examples/platforms/macos-appkit-v1/manifest.json positive /private/tmp/my-new-mac-run
node code-examples/tools/platform-native.mjs execute code-examples/platforms/tvos-uikit-v1/manifest.json positive /private/tmp/my-new-tv-run YOUR_EXISTING_TVOS26_SIMULATOR_UUID
```

Select `compile` or an exact negative check ID from the package manifest instead
of `positive` to run those checks. Mutants pass validation only when the specified
assertion fails; infrastructure or build errors do not count as rejection. The
adapter snapshots inputs, source hashes, selected environment, commands and output.
Existing 600-second xcodebuild timeout remains in force.

## Candidate progressive disclosure

[Candidate router](../../../code-examples/tools/platform-retrieval.mjs) is a
repository tool, not an installed MCP endpoint or released skill change.

```sh
node code-examples/tools/platform-retrieval.mjs macOS AppKit actions
node code-examples/tools/platform-retrieval.mjs tvOS UIKit focus example
node code-examples/tools/platform-retrieval.mjs tvOS UIKit focus contract
```

1. Require an explicit platform/framework pair. Ambiguous Mac/Catalyst, mixed
   frameworks and deferred SwiftUI companions do not fall back to iOS examples.
2. Default to one or two relevant existing guideline documents.
3. `example` adds just the selected package source; `contract` adds its tests and
   manifest. Evidence reports and incident history stay outside ordinary retrieval.
4. Emit actual read paths, SHA-256 and byte counts. A selection alone is not a read;
   tokens remain unavailable rather than estimated. No model-efficiency claim yet.

The caller chooses a level after the developer requests examples or contracts;
merely discussing accessibility does not opt into code or tests. Existing released
SwiftUI and other-platform guidance remains available through the existing skill.
This narrow companion router does not replace that wider routing table.

Before promotion: independently review the platform/family map and claims, freeze
new development cases, run approved paired C0-C3 frontier evaluations and compare
quality plus retrieval bytes/tokens. Only then integrate a compact pointer into
runtime routing. Do not load these research reports into the default skill context.

## Evidence limits and outstanding work

- See [coverage queue](COVERAGE.md), [sources](SOURCES.md) and [difficulties](DIFFICULTIES.md).
- A preferred environment is not delivered focus. A notification spy records a
  request, not speech. Stored traits are not observed assistive-tool behavior.
- Annual current/previous tested anchors remain the policy; host27 evidence is not
  an OS27 skill-promotion decision. Older anchors are not invented or overwritten.
- Full member-level introduction/deprecation audit is pending. Successful SDK27
  compilation for target26 is a bounded compiler observation, not a complete API audit.
- No independent review request has been sent for this new batch; no acceptance implied.

## Measured context size

[Read-trace measurements](retrieval-measurements.json) cover all five supported
platform/topic selections at each detail level. Default guidance reads range from
2,460 to 5,678 bytes. Source opt-in adds 2,200 bytes for tvOS or 2,311 bytes for Mac;
contract mode adds the package manifest and tests. These are bytes actually read,
not tokenizer counts, model efficiency benchmarks or a claim of the 15% release gate.

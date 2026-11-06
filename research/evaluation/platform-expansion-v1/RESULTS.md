# Platform companion results

November 6, 2026. Development evidence executed locally; independent review and
frontier-model evaluation pending. Released skill 0.2.2 and frozen baselines unchanged.

## Current input revisions

| Platform | Positive methods passed | Deliberate mutants rejected | Original-defect regression rejected | Compile |
| --- | ---: | ---: | ---: | --- |
| AppKit/macOS, revision 2 | 20 | 5 | 0 | Passed |
| UIKit/tvOS, revision 2 | 22 | 5 | 1 | Passed |
| Total | 42 | 10 | 1 | 2 passed |

All **15 current-manifest checks** have exact matching successful validation receipts.
Negative checks pass validation because their named assertion fails, not because
the broken example succeeds. All failures in negative checks were assertion failures,
not crashes, skipped tests, wrong destinations or build errors.

Five behavioral families have separate draft developer questions and controller
rubrics. These are not five independently reviewed gold cases yet.

## Environments

| Dimension | Mac | Apple TV |
| --- | --- | --- |
| Runtime | macOS27.0, build26A428, real host | tvOS26.5, build23L470, simulator |
| SDK | macOS27.0, build26A425 | tvOS27.0, build24J360 |
| Deployment target | 26.0 | 26.0 |
| Toolchain | Xcode27.0 build27A266a, Apple Swift6.4 | Same |
| Architecture | arm64 target, arm64e host identification | arm64 |

Mac27 execution is **not** evidence of Mac26 runtime behavior and does not promote
OS27 skill guidance. The compiler's own host target string is not the tvOS test
destination; destination selection and xcresult identity are checked independently.

## Preserved history

Across all 20 native attempts:18 met their expected outcome, one Mac attempt was
blocked before execution by host architecture matching, and one Mac positive run
failed its lifetime assertion. Both first failures remain recorded alongside repair.
There were 93 test-method executions including reruns and negatives, not 93 independent
behaviors. Four compile executions include two historical first revisions.

The first tvOS suite passed 20 methods but missed absent visible button titles.
Source review found that actual author defect; revision 2 adds two title assertions.
The original source now fails its targeted regression check. This demonstrates why
a green suite does not establish complete behavior coverage.

The offline suite passes 267 checks, including 21 new platform adapter, retrieval and
receipt/pairing checks. Frozen baseline validation still verifies 210 files at
`3a1a2d58af19a94eec940000d9edcca7928bb5139aa3d52b1ef6e917c0271bbd`;
all 87 prior development-evidence pins remain intact.

## Audit and reproduction

- [Sanitized results index](results-index.json): input hashes, environment, exact
  selected/failing methods, diagnostics, original result/artifact hashes and 39 pins.
- [Difficulties](DIFFICULTIES.md): exact first code and classification.
- [Private archive receipt](archive-receipt.json): durable local native evidence,
  including first inputs/logs and xcresult bundles. Not a public data download.
- [Read measurements](retrieval-measurements.json): actual byte/hash traces for
  default guidance, example and contract levels; token telemetry unavailable.
- [Remaining coverage](COVERAGE.md) and [prepared review request](REVIEW-REQUEST.md).

No model runs or installations occurred. No BigDog submission or acceptance is
claimed. Candidate retrieval is repository-only and has not changed runtime skill
files, frozen prompts or the existing iOS adapter. SwiftUI companion work remains deferred.

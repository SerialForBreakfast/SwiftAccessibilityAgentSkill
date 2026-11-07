# Consolidated Native Results

Final source revision4 passes all ten selected checks: three source compiles, three
positive suites and four intended mutant rejections. No skipped tests.

| Platform | Positive methods | Actual runtime | SDK | Deployment |
| --- | ---: | --- | --- | --- |
| iOS | 36 | 26.5 (23F77) | 27.0 (24A430) | 26.0 |
| macOS | 36 | 27.0 (26A428) | 27.0 (26A425) | 26.0 |
| tvOS | 36 | 26.5 (23L470) | 27.0 (24J360) | 26.0 |

## Counts Without Inflation

- Three shared behavioral families, with nine draft platform prompt/rubric pairs.
- 36 method definitions repeated across three platforms: 108 final positive method
  executions, not 108 independent accessibility behaviors.
- Four distinct mutants, executed on macOS for shared-code contracts. Each fails
  exactly its selected assertion, with a successful test build.
- Earlier original/forwarding companions retain 103 passing methods per platform;
  this adds 36 for a total of 139 method entries per platform across those packages.
  Earlier evidence is reused, not silently represented as rerun here.
- All 25 native attempts are preserved: 19 expected outcomes, two test-compiler
  errors, one blocked harness preflight and three platform executions of the same
  incorrect oracle. The final ten checks all pass.
- Across both executed source revisions: 213 positive method executions and eight
  mutant executions, including repeats. Compile-error attempts receive zero credit.

## Preserved Failure History

1. Source revision1: production source typecheck passes; test build rejects async
   work inside XCTUnwrap autoclosures. No unit methods execute.
2. Additive adapter attempt: missing self-snapshot filename blocks preflight. No
   compile or unit credit. Harness fix retains the blocked attempt.
3. Source revision2: test build rejects actor-isolation/continuation transfers. The
   improved adapter classifies test compilation explicitly; no unit credit.
4. Source revision3: 35 methods execute on each platform. The nil-default oracle
   fails on each; all four intended mutants reject for their named reasons.
5. Source revision4: the oracle preserves initial native selection. Scoped reload
   and pre-cancelled-task ownership add a method; all 36 pass on each platform.

The test compilation contract used two documented repairs. The distinct oracle
contract used one. No endless repair loop or retrospective deletion of first
failures. See [analysis](DIFFICULTIES.md), [index](results-index.json),
[checkpoint](checkpoint.json) and [private archive receipt](archive-receipt.json).
Public receipt/log copies explicitly redact paths and device identifiers; original
bytes and hashes remain privately archived.

## What This Establishes

Real media-group loading/selection in a silent local fixture; current-item and
request ownership; preservation of other choices; observable store invalidation;
and target compilation of the actual SwiftUI composition. Public SDK declaration
captures distinguish selectors from neighboring deprecated declarations.

It does not establish rendered captions, narration quality, generated accessibility
semantics, delivered focus, automatic external-selection observation, production
stream metadata or universal OS coverage. Supplemental live-stream observer
lifecycle remains a named testable remainder. No UI tests or mandatory manual
verification gate is added.

## Evaluation Status

Nine new developer cases and four diagnostic cases are draft/not-run. No subject
answers are fabricated from author code or native logs. Independent review is
prepared, not accepted or dispatched. No model runs/spend; released skill, frozen
baselines and BigDog's sealed package remain unchanged. Unit outcomes are not
measurements of model-answer improvement.

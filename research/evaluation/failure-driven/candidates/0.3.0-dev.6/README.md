# Candidate 0.3.0-dev.6: Reviewed Media Ownership

Research-only extension of dev.5. Released skill0.2.2, previous candidates, frozen
baselines and BigDog's sealed v2 comparison are unchanged. There is no additional
installable SKILL.md. This is not a benchmark-qualified release.

## Changes That Affect Decisions

- Protect Off/nil callbacks with the same item/snapshot ownership as other choices.
- Distinguish an existing filtered/unmapped native selection from Off without
  resetting valid native choices.
- Separate a native side effect from app-observable notification.
- Distinguish cooperative task cancellation from immediate explicit owner cleanup.
- State external item/reload ownership rather than inferring automatic observation
  from a getter; include store identity when task ownership depends on it.

These lessons come from the [separate-context source review](../../../swiftui-review-v1/ADJUDICATION.md),
actual first-failure reproductions and corrected unit suites. They are not
measurements of answer-quality improvement. Existing general guidance and known
source gaps outside this focused extension remain inherited, not newly qualified.

## Context And Examples

The short entrypoint retains the existing workflow. The media metadata router loads
one selected concern note plus a platform-specific SDK excerpt card. The overview
does not load all three detailed notes. Other topics delegate unchanged to pinned
dev.5 routing and retain its qualification limits.

```sh
node research/evaluation/failure-driven/candidates/0.3.0-dev.6/route.mjs iOS SwiftUI media selection
node research/evaluation/failure-driven/candidates/0.3.0-dev.6/route.mjs macOS SwiftUI media ownership example
node research/evaluation/failure-driven/candidates/0.3.0-dev.6/route.mjs tvOS SwiftUI media wiring contract
```

Examples and complete runnable fixture/test inputs load only on request. Default
context excludes controller rubrics, review transcripts, incidents and full SDK
headers. A byte ceiling fails closed before document content is loaded. Actual read
hashes and bytes are recorded; token telemetry is unavailable. Explicit metadata
routing is not a demonstrated natural-language classifier or installed retrieval.

The media extension covers AVFoundation selection/application ownership, not every
media accessibility feature. Additional target-specific primary sources are needed
for unrelated APIs. Its SDK cards preserve exact declaration annotations; test
evidence is scoped to the recorded SDK/deployment/runtime, not universal behavior.

## Evaluation Boundary

Nine corrected developer prompt/rubric pairs are linked from the review package.
They use new paths and complete media-only starters, and explicitly request tests.
Existing v1 questions, all frozen questions and the active BigDog payloads remain
unchanged. Correctness and evidence completeness are separate grades. The corrected
cases are development families with shared platform variants, not new holdouts.

One review agent performed two source-review turns in the authorized authoring
workflow. No frontier answer-generation benchmark, judge batch, paid provider or
new model evaluation run was executed. Source review does not establish model lift.

## Next Highest-Value Step

Publish this consolidated checkpoint when authorized. Let BigDog complete its
unchanged comparison first, then use those results to select one later, bounded
comparison of accepted candidate changes. Do not mix results from different bundles.

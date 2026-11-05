# D31 · SwiftUI centering

[← v2 dashboard](../README.md) · [Original v1 comparison](../../v1/cases/smoke-v1-D31-26.md)

## Exact original question

```text
How do I center a SwiftUI view?
```

## New rubric criteria

- Answer the layout question without unnecessary accessibility routing.
- Answer the layout question directly; do not turn it into an accessibility audit.

These are grading criteria, not a model-generated gold answer. [Frozen rubric](../rubric-snapshot.json); [evidence](../grading-evidence-snapshot.json). D31 has no frozen reference; Apple layout documentation supplements the assessment. [Supplement and source IDs](../EVIDENCE.md). Single reviewer, unblinded and not independently calibrated.

## Score comparison

Scores C/T/Cal/R are correctness/task success/calibration/relevance, each 0–4. Weighted quality is 0–100, not percent accuracy.

| Variant | Cap | C/T/Cal/R | Quality | Critical flag | Original answer | Review |
| --- | ---: | --- | ---: | --- | --- | --- |
| candidate · C0 | 1024 | 0/0/0/2 | 5.00 | invented_api | [Response 1](../../v1/cases/smoke-v1-D31-26.md#response-1) | [Rationale](#review-1) |
| candidate · C1 | 1024 | 2/0/2/0 | 27.50 | None identified | [Response 2](../../v1/cases/smoke-v1-D31-26.md#response-2) | [Rationale](#review-2) |
| candidate · C2 | 1024 | 1/1/0/1 | 21.25 | invented_api | [Response 3](../../v1/cases/smoke-v1-D31-26.md#response-3) | [Rationale](#review-3) |
| candidate · C3 | 1024 | 1/1/0/1 | 21.25 | invented_api | [Response 4](../../v1/cases/smoke-v1-D31-26.md#response-4) | [Rationale](#review-4) |
| baseline · C0 | 1024 | 0/0/0/2 | 5.00 | invented_api | [Response 5](../../v1/cases/smoke-v1-D31-26.md#response-5) | [Rationale](#review-5) |
| baseline · C1 | 1024 | 2/2/1/1 | 43.75 | invented_api | [Response 6](../../v1/cases/smoke-v1-D31-26.md#response-6) | [Rationale](#review-6) |
| baseline · C2 | 1024 | 1/1/0/1 | 21.25 | invented_api | [Response 7](../../v1/cases/smoke-v1-D31-26.md#response-7) | [Rationale](#review-7) |
| baseline · C3 | 1024 | 0/0/0/2 | 5.00 | invented_api | [Response 8](../../v1/cases/smoke-v1-D31-26.md#response-8) | [Rationale](#review-8) |

## Review 1

**candidate · C0 · 1024 tokens** — All principal solutions rely on undefined center/centered/offsetBy modifiers presented as built-ins, with no extension. The confident modern-recommended claim is unsupported; no usable centering solution.

[Exact prompt and tools](../../v1/prompts/84d2e213681979d2.json) · [Complete original output](../../v1/cases/smoke-v1-D31-26.md#response-1)

**invented_api**, evidence `A-LAYOUT; A-FRAME`:

````text
.center()
````

Evidence IDs: A-LAYOUT, A-FRAME. Finish: `stop`; 4.38s. Reference contents: 0 (unavailable). Missing reads are a separate protocol result; routing text alone is not a fabricated-read finding.

## Review 2

**candidate · C1 · 1024 tokens** — Correctly recognizes that layout is not an accessibility audit and mentions frame/alignment, but never gives the requested centering solution. Instead repeats irrelevant routing/checklist material until truncation.

[Exact prompt and tools](../../v1/prompts/2a3568bef7d7808f.json) · [Complete original output](../../v1/cases/smoke-v1-D31-26.md#response-2)

Evidence IDs: A-FRAME, A-LAYOUT. Finish: `length`; 6.34s. Reference contents: 0 (unavailable). Missing reads are a separate protocol result; routing text alone is not a fabricated-read finding.

## Review 3

**candidate · C2 · 1024 tokens** — Recognizes the topic but buries it under an irrelevant accessibility workflow. Recommends nonexistent centered() and attempts to instantiate the View protocol; a mention of a fixed frame provides only limited useful content.

[Exact prompt and tools](../../v1/prompts/625736bb7a2fdbde.json) · [Complete original output](../../v1/cases/smoke-v1-D31-26.md#response-3)

**invented_api**, evidence `A-FRAME; A-LAYOUT`:

````text
.centered()
````

Evidence IDs: A-FRAME, A-LAYOUT. Finish: `stop`; 4.54s. Reference contents: 0 (injected). Missing reads are a separate protocol result; routing text alone is not a fabricated-read finding.

## Review 4

**candidate · C3 · 1024 tokens** — Same primary invented CenteredView/centering APIs as G26; one valid fixed-frame example earns limited credit. The truncated container catalogue does not supply a reliable concise answer.

[Exact prompt and tools](../../v1/prompts/ebeea36a58480335.json) · [Complete original output](../../v1/cases/smoke-v1-D31-26.md#response-4)

**invented_api**, evidence `A-FRAME; A-LAYOUT`:

````text
CenteredView {
````

Evidence IDs: A-FRAME, A-LAYOUT. Finish: `length`; 6.70s. Reference contents: 0 (model-read). Missing reads are a separate protocol result; routing text alone is not a fabricated-read finding.

## Review 5

**baseline · C0 · 1024 tokens** — All principal solutions rely on undefined center/centered/offsetBy modifiers presented as built-ins, with no extension. The confident modern-recommended claim is unsupported; no usable centering solution.

[Exact prompt and tools](../../v1/prompts/84d2e213681979d2.json) · [Complete original output](../../v1/cases/smoke-v1-D31-26.md#response-5)

**invented_api**, evidence `A-LAYOUT; A-FRAME`:

````text
.center()
````

Evidence IDs: A-LAYOUT, A-FRAME. Finish: `stop`; 4.30s. Reference contents: 0 (unavailable). Missing reads are a separate protocol result; routing text alone is not a fabricated-read finding.

## Review 6

**baseline · C1 · 1024 tokens** — ZStack with center alignment is a valid starting point. However, recommends nonexistent Alignment.topCenter as vertical centering, gives only an empty container and invents accessibility benefits. Material correction and container-sizing explanation are needed.

[Exact prompt and tools](../../v1/prompts/b3be7b447dd3bf10.json) · [Complete original output](../../v1/cases/smoke-v1-D31-26.md#response-6)

**invented_api**, evidence `A-ALIGNMENT; A-FRAME`:

````text
`Alignment.topCenter`
````

Evidence IDs: A-ALIGNMENT, A-FRAME. Finish: `stop`; 3.84s. Reference contents: 0 (unavailable). Missing reads are a separate protocol result; routing text alone is not a fabricated-read finding.

## Review 7

**baseline · C2 · 1024 tokens** — Includes potentially useful ZStack/Spacer fragments but all concrete main implementations rely on undefined centered(). Invents layout-based accessibility guarantees and a nonworking test. Truncation retained.

[Exact prompt and tools](../../v1/prompts/a64916a51030cad9.json) · [Complete original output](../../v1/cases/smoke-v1-D31-26.md#response-7)

**invented_api**, evidence `A-FRAME; A-LAYOUT`:

````text
.centered()
````

Evidence IDs: A-FRAME, A-LAYOUT. Finish: `length`; 6.32s. Reference contents: 0 (injected). Missing reads are a separate protocol result; routing text alone is not a fabricated-read finding.

## Review 8

**baseline · C3 · 1024 tokens** — Entire proposed solution depends on undefined CenteredView/CenteredStack presented as standard SwiftUI. Confuses orientation with Dynamic Type and supplies no functioning centering alternative.

[Exact prompt and tools](../../v1/prompts/7eb3594d0f4f5c10.json) · [Complete original output](../../v1/cases/smoke-v1-D31-26.md#response-8)

**invented_api**, evidence `A-LAYOUT`:

````text
CenteredView {
````

Evidence IDs: A-LAYOUT. Finish: `stop`; 4.01s. Reference contents: 0 (model-read). Missing reads are a separate protocol result; routing text alone is not a fabricated-read finding.

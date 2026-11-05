# D31 · SwiftUI centering

[← v2 dashboard](../README.md) · [Original v1 comparison](../../v1/cases/development-v1-D31.md)

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
| candidate · C0 | 1024 | 0/0/0/2 | 5.00 | invented_api | [Response 1](../../v1/cases/development-v1-D31.md#response-1) | [Rationale](#review-1) |
| candidate · C2 | 1024 | 1/1/0/1 | 21.25 | invented_api | [Response 2](../../v1/cases/development-v1-D31.md#response-2) | [Rationale](#review-2) |
| candidate · C3-original | 1024 | 1/1/0/1 | 21.25 | invented_api | [Response 3](../../v1/cases/development-v1-D31.md#response-3) | [Rationale](#review-3) |
| candidate · C3-explicit | 1024 | 0/0/0/2 | 5.00 | invented_api | [Response 4](../../v1/cases/development-v1-D31.md#response-4) | [Rationale](#review-4) |
| candidate · C0 | 2048 | 0/0/0/2 | 5.00 | invented_api | [Response 5](../../v1/cases/development-v1-D31.md#response-5) | [Rationale](#review-5) |
| candidate · C2 | 2048 | 1/1/0/1 | 21.25 | invented_api | [Response 6](../../v1/cases/development-v1-D31.md#response-6) | [Rationale](#review-6) |
| candidate · C3-original | 2048 | 1/1/0/1 | 21.25 | invented_api | [Response 7](../../v1/cases/development-v1-D31.md#response-7) | [Rationale](#review-7) |
| candidate · C3-explicit | 2048 | 0/0/0/2 | 5.00 | invented_api | [Response 8](../../v1/cases/development-v1-D31.md#response-8) | [Rationale](#review-8) |

## Review 1

**candidate · C0 · 1024 tokens** — All principal solutions rely on undefined center/centered/offsetBy modifiers presented as built-ins, with no extension. The confident modern-recommended claim is unsupported; no usable centering solution.

[Exact prompt and tools](../../v1/prompts/84d2e213681979d2.json) · [Complete original output](../../v1/cases/development-v1-D31.md#response-1)

**invented_api**, evidence `A-LAYOUT; A-FRAME`:

````text
.center()
````

Evidence IDs: A-LAYOUT, A-FRAME. Finish: `stop`; 4.36s. Reference contents: 0 (unavailable). Missing reads are a separate protocol result; routing text alone is not a fabricated-read finding.

## Review 2

**candidate · C2 · 1024 tokens** — Recognizes the topic but buries it under an irrelevant accessibility workflow. Recommends nonexistent centered() and attempts to instantiate the View protocol; a mention of a fixed frame provides only limited useful content.

[Exact prompt and tools](../../v1/prompts/625736bb7a2fdbde.json) · [Complete original output](../../v1/cases/development-v1-D31.md#response-2)

**invented_api**, evidence `A-FRAME; A-LAYOUT`:

````text
.centered()
````

Evidence IDs: A-FRAME, A-LAYOUT. Finish: `stop`; 4.54s. Reference contents: 0 (injected). Missing reads are a separate protocol result; routing text alone is not a fabricated-read finding.

## Review 3

**candidate · C3-original · 1024 tokens** — Same primary invented CenteredView/centering APIs as G26; one valid fixed-frame example earns limited credit. The truncated container catalogue does not supply a reliable concise answer.

[Exact prompt and tools](../../v1/prompts/ebeea36a58480335.json) · [Complete original output](../../v1/cases/development-v1-D31.md#response-3)

**invented_api**, evidence `A-FRAME; A-LAYOUT`:

````text
CenteredView {
````

Evidence IDs: A-FRAME, A-LAYOUT. Finish: `length`; 6.59s. Reference contents: 0 (model-read). Missing reads are a separate protocol result; routing text alone is not a fabricated-read finding.

## Review 4

**candidate · C3-explicit · 1024 tokens** — Recommends nonexistent built-in center() APIs and invented layout-guide mechanisms without providing an extension. Both principal code examples are unusable for the stated task.

[Exact prompt and tools](../../v1/prompts/54205a37c6178100.json) · [Complete original output](../../v1/cases/development-v1-D31.md#response-4)

**invented_api**, evidence `A-LAYOUT; A-FRAME`:

````text
.center()
````

Evidence IDs: A-LAYOUT, A-FRAME. Finish: `stop`; 3.45s. Reference contents: 0 (model-read). Missing reads are a separate protocol result; routing text alone is not a fabricated-read finding.

## Review 5

**candidate · C0 · 2048 tokens** — All principal solutions rely on undefined center/centered/offsetBy modifiers presented as built-ins, with no extension. The confident modern-recommended claim is unsupported; no usable centering solution.

[Exact prompt and tools](../../v1/prompts/84d2e213681979d2.json) · [Complete original output](../../v1/cases/development-v1-D31.md#response-5)

**invented_api**, evidence `A-LAYOUT; A-FRAME`:

````text
.center()
````

Evidence IDs: A-LAYOUT, A-FRAME. Finish: `stop`; 4.37s. Reference contents: 0 (unavailable). Missing reads are a separate protocol result; routing text alone is not a fabricated-read finding.

## Review 6

**candidate · C2 · 2048 tokens** — Recognizes the topic but buries it under an irrelevant accessibility workflow. Recommends nonexistent centered() and attempts to instantiate the View protocol; a mention of a fixed frame provides only limited useful content.

[Exact prompt and tools](../../v1/prompts/625736bb7a2fdbde.json) · [Complete original output](../../v1/cases/development-v1-D31.md#response-6)

**invented_api**, evidence `A-FRAME; A-LAYOUT`:

````text
.centered()
````

Evidence IDs: A-FRAME, A-LAYOUT. Finish: `stop`; 4.63s. Reference contents: 0 (injected). Missing reads are a separate protocol result; routing text alone is not a fabricated-read finding.

## Review 7

**candidate · C3-original · 2048 tokens** — One fixed-frame example could center content locally, but the primary solution invents CenteredView and centering modifiers, then repeats them across many containers. Truncation and irrelevant repetition compound an already unusable main recommendation.

[Exact prompt and tools](../../v1/prompts/ebeea36a58480335.json) · [Complete original output](../../v1/cases/development-v1-D31.md#response-7)

**invented_api**, evidence `A-FRAME; A-LAYOUT`:

````text
CenteredView {
````

Evidence IDs: A-FRAME, A-LAYOUT. Finish: `length`; 12.75s. Reference contents: 0 (model-read). Missing reads are a separate protocol result; routing text alone is not a fabricated-read finding.

## Review 8

**candidate · C3-explicit · 2048 tokens** — Recommends nonexistent built-in center() APIs and invented layout-guide mechanisms without providing an extension. Both principal code examples are unusable for the stated task.

[Exact prompt and tools](../../v1/prompts/54205a37c6178100.json) · [Complete original output](../../v1/cases/development-v1-D31.md#response-8)

**invented_api**, evidence `A-LAYOUT; A-FRAME`:

````text
.center()
````

Evidence IDs: A-LAYOUT, A-FRAME. Finish: `stop`; 3.36s. Reference contents: 0 (model-read). Missing reads are a separate protocol result; routing text alone is not a fabricated-read finding.

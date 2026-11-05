# D01 · UILabel accessibility

[← v2 dashboard](../README.md) · [Original v1 comparison](../../v1/cases/smoke-v1-D01-26.md)

## Exact original question

```text
Tell me about UILabel accessibility.
Deployment context: uikit OS version 26. Clarify platform if needed.
```

## New rubric criteria

- Explain meaningful labels without claiming visual truncation necessarily truncates spoken text.
- Explain native text-derived labeling and customize only when meaning requires it.
- Do not require an override simply because visible text truncates.

These are grading criteria, not a model-generated gold answer. [Frozen rubric](../rubric-snapshot.json); [evidence](../grading-evidence-snapshot.json). [Supplement and source IDs](../EVIDENCE.md). Single reviewer, unblinded and not independently calibrated.

## Score comparison

Scores C/T/Cal/R are correctness/task success/calibration/relevance, each 0–4. Weighted quality is 0–100, not percent accuracy.

| Variant | Cap | C/T/Cal/R | Quality | Critical flag | Original answer | Review |
| --- | ---: | --- | ---: | --- | --- | --- |
| candidate · C0 | 1024 | 0/1/0/2 | 13.75 | invented_api | [Response 1](../../v1/cases/smoke-v1-D01-26.md#response-1) | [Rationale](#review-1) |
| candidate · C1 | 1024 | 1/1/0/2 | 23.75 | None identified | [Response 2](../../v1/cases/smoke-v1-D01-26.md#response-2) | [Rationale](#review-2) |
| candidate · C2 | 1024 | 1/2/1/2 | 36.25 | invented_api | [Response 3](../../v1/cases/smoke-v1-D01-26.md#response-3) | [Rationale](#review-3) |
| candidate · C3 | 1024 | 1/1/0/2 | 23.75 | None identified | [Response 4](../../v1/cases/smoke-v1-D01-26.md#response-4) | [Rationale](#review-4) |
| baseline · C0 | 1024 | 0/1/0/2 | 13.75 | invented_api | [Response 5](../../v1/cases/smoke-v1-D01-26.md#response-5) | [Rationale](#review-5) |
| baseline · C1 | 1024 | 0/1/0/2 | 13.75 | None identified | [Response 6](../../v1/cases/smoke-v1-D01-26.md#response-6) | [Rationale](#review-6) |
| baseline · C2 | 1024 | 1/1/0/2 | 23.75 | invented_api | [Response 7](../../v1/cases/smoke-v1-D01-26.md#response-7) | [Rationale](#review-7) |
| baseline · C3 | 1024 | 0/0/0/1 | 2.50 | invented_api | [Response 8](../../v1/cases/smoke-v1-D01-26.md#response-8) | [Rationale](#review-8) |

## Review 1

**candidate · C0 · 1024 tokens** — Invents an accessibility manager/query API and role types instead of explaining native text-derived labeling. Some discussion of labels/testing is relevant, but the implementation is unusable. It replaces the supplied version with iOS 16 and asserts automatic contrast correction.

[Exact prompt and tools](../../v1/prompts/cb2a45b991efe4c0.json) · [Complete original output](../../v1/cases/smoke-v1-D01-26.md#response-1)

**invented_api**, evidence `A-UIKIT`:

````text
let accessibilityManager = UIAccessibilityManager()
````

Evidence IDs: F-D01, A-UIKIT. Finish: `length`; 49.00s. Reference contents: 0 (unavailable). Missing reads are a separate protocol result; routing text alone is not a fabricated-read finding.

## Review 2

**candidate · C1 · 1024 tokens** — Acknowledges text can be spoken, but treats that correct default as a defect, conflates roles/properties and provides misleading activation/testing directions. Unnecessary overrides and unsupported version certainty prevent a useful answer.

[Exact prompt and tools](../../v1/prompts/0ef2dcc1e2786460.json) · [Complete original output](../../v1/cases/smoke-v1-D01-26.md#response-2)

Evidence IDs: F-D01, A-LABEL. Finish: `stop`; 6.17s. Reference contents: 0 (unavailable). Missing reads are a separate protocol result; routing text alone is not a fabricated-read finding.

## Review 3

**candidate · C2 · 1024 tokens** — Useful naming, decorative-content and semantic-control advice earns partial task credit. The example uses invalid active/icon traits and turns text labeling into button implementation without explaining native defaults. Generic future-OS caution coexists with unjustified high freshness.

[Exact prompt and tools](../../v1/prompts/717a76a05dcfe728.json) · [Complete original output](../../v1/cases/smoke-v1-D01-26.md#response-3)

**invented_api**, evidence `A-TRAITS`:

````text
label.accessibilityTraits = [.active, .button]
````

Evidence IDs: F-D01, A-TRAITS. Finish: `stop`; 6.10s. Reference contents: 1 (injected). Missing reads are a separate protocol result; routing text alone is not a fabricated-read finding.

## Review 4

**candidate · C3 · 1024 tokens** — Confuses accessible name with accessibilityValue and requires explicit value configuration. Claims the guideline requires both label and value, which it does not. Some relevant testing is present but the central rule is wrong.

[Exact prompt and tools](../../v1/prompts/903d54d036521c4f.json) · [Complete original output](../../v1/cases/smoke-v1-D01-26.md#response-4)

Evidence IDs: F-D01, A-LABEL. Finish: `stop`; 4.75s. Reference contents: 0 (model-read). Missing reads are a separate protocol result; routing text alone is not a fabricated-read finding.

## Review 5

**baseline · C0 · 1024 tokens** — Invents an accessibility manager/query API and role types instead of explaining native text-derived labeling. Some discussion of labels/testing is relevant, but the implementation is unusable. It replaces the supplied version with iOS 16 and asserts automatic contrast correction.

[Exact prompt and tools](../../v1/prompts/cb2a45b991efe4c0.json) · [Complete original output](../../v1/cases/smoke-v1-D01-26.md#response-5)

**invented_api**, evidence `A-UIKIT`:

````text
let accessibilityManager = UIAccessibilityManager()
````

Evidence IDs: F-D01, A-UIKIT. Finish: `length`; 5.96s. Reference contents: 0 (unavailable). Missing reads are a separate protocol result; routing text alone is not a fabricated-read finding.

## Review 6

**baseline · C1 · 1024 tokens** — Incorrectly says UILabel is inaccessible by default and confuses label/value with traits and role assignment. Testing directions do not establish a meaningful accessible name and native text-derived behavior is absent.

[Exact prompt and tools](../../v1/prompts/84900557eaaf5783.json) · [Complete original output](../../v1/cases/smoke-v1-D01-26.md#response-6)

Evidence IDs: F-D01, A-UILABEL, A-LABEL. Finish: `stop`; 3.95s. Reference contents: 0 (unavailable). Missing reads are a separate protocol result; routing text alone is not a fabricated-read finding.

## Review 7

**baseline · C2 · 1024 tokens** — Explicitly warns against using native label text, contrary to the rubric, and recommends invented editable/scrollable/hidden traits. Genuine semantic-control advice does not rescue the implementation. Truncation retained.

[Exact prompt and tools](../../v1/prompts/cf0aca43717faaf5.json) · [Complete original output](../../v1/cases/smoke-v1-D01-26.md#response-7)

**invented_api**, evidence `A-TRAITS`:

````text
`UITraitContentEditable`
````

Evidence IDs: F-D01, A-TRAITS. Finish: `length`; 6.38s. Reference contents: 1 (injected). Missing reads are a separate protocol result; routing text alone is not a fabricated-read finding.

## Review 8

**baseline · C3 · 1024 tokens** — Conflates UIKit and SwiftUI, labels and containers; assigns properties/modifiers that do not match UILabel and returns UILabel instances directly in SwiftUI code. Does not provide a usable answer and ends truncated.

[Exact prompt and tools](../../v1/prompts/b4dae95bdfbc5128.json) · [Complete original output](../../v1/cases/smoke-v1-D01-26.md#response-8)

**invented_api**, evidence `A-TRAITS; A-UILABEL`:

````text
.accessibilityTraits(.accessibilityLabel)
````

Evidence IDs: F-D01, A-TRAITS, A-UILABEL. Finish: `length`; 6.61s. Reference contents: 0 (model-read). Missing reads are a separate protocol result; routing text alone is not a fabricated-read finding.

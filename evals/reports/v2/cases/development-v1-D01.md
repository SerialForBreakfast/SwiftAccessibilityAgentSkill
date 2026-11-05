# D01 · UILabel accessibility

[← v2 dashboard](../README.md) · [Original v1 comparison](../../v1/cases/development-v1-D01.md)

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
| candidate · C0 | 1024 | 0/1/0/2 | 13.75 | invented_api | [Response 1](../../v1/cases/development-v1-D01.md#response-1) | [Rationale](#review-1) |
| candidate · C2 | 1024 | 1/2/1/2 | 36.25 | invented_api | [Response 2](../../v1/cases/development-v1-D01.md#response-2) | [Rationale](#review-2) |
| candidate · C3-original | 1024 | 1/1/0/2 | 23.75 | None identified | [Response 3](../../v1/cases/development-v1-D01.md#response-3) | [Rationale](#review-3) |
| candidate · C3-explicit | 1024 | 2/1/1/3 | 40.00 | None identified | [Response 4](../../v1/cases/development-v1-D01.md#response-4) | [Rationale](#review-4) |
| candidate · C0 | 2048 | 0/1/0/2 | 13.75 | invented_api | [Response 5](../../v1/cases/development-v1-D01.md#response-5) | [Rationale](#review-5) |
| candidate · C2 | 2048 | 1/2/1/2 | 36.25 | invented_api | [Response 6](../../v1/cases/development-v1-D01.md#response-6) | [Rationale](#review-6) |
| candidate · C3-original | 2048 | 1/1/0/2 | 23.75 | None identified | [Response 7](../../v1/cases/development-v1-D01.md#response-7) | [Rationale](#review-7) |
| candidate · C3-explicit | 2048 | 2/1/1/3 | 40.00 | None identified | [Response 8](../../v1/cases/development-v1-D01.md#response-8) | [Rationale](#review-8) |

## Review 1

**candidate · C0 · 1024 tokens** — Invents an accessibility manager/query API and role types instead of explaining native text-derived labeling. Some discussion of labels/testing is relevant, but the implementation is unusable. It replaces the supplied version with iOS 16 and asserts automatic contrast correction.

[Exact prompt and tools](../../v1/prompts/cb2a45b991efe4c0.json) · [Complete original output](../../v1/cases/development-v1-D01.md#response-1)

**invented_api**, evidence `A-UIKIT`:

````text
let accessibilityManager = UIAccessibilityManager()
````

Evidence IDs: F-D01, A-UIKIT. Finish: `length`; 49.63s. Reference contents: 0 (unavailable). Missing reads are a separate protocol result; routing text alone is not a fabricated-read finding.

## Review 2

**candidate · C2 · 1024 tokens** — Useful naming, decorative-content and semantic-control advice earns partial task credit. The example uses invalid active/icon traits and turns text labeling into button implementation without explaining native defaults. Generic future-OS caution coexists with unjustified high freshness.

[Exact prompt and tools](../../v1/prompts/717a76a05dcfe728.json) · [Complete original output](../../v1/cases/development-v1-D01.md#response-2)

**invented_api**, evidence `A-TRAITS`:

````text
label.accessibilityTraits = [.active, .button]
````

Evidence IDs: F-D01, A-TRAITS. Finish: `stop`; 6.30s. Reference contents: 1 (injected). Missing reads are a separate protocol result; routing text alone is not a fabricated-read finding.

## Review 3

**candidate · C3-original · 1024 tokens** — Confuses accessible name with accessibilityValue and requires explicit value configuration. Claims the guideline requires both label and value, which it does not. Some relevant testing is present but the central rule is wrong.

[Exact prompt and tools](../../v1/prompts/903d54d036521c4f.json) · [Complete original output](../../v1/cases/development-v1-D01.md#response-3)

Evidence IDs: F-D01, A-LABEL. Finish: `stop`; 4.81s. Reference contents: 0 (model-read). Missing reads are a separate protocol result; routing text alone is not a fabricated-read finding.

## Review 4

**candidate · C3-explicit · 1024 tokens** — Gives relevant meaningful-text and verification advice but omits text-derived defaults and conditional customization. Role terminology is confused, hint guidance is vague and duplicated high-freshness/source assertions overstate support. No implementable core explanation.

[Exact prompt and tools](../../v1/prompts/23b63fe9b6c0df0e.json) · [Complete original output](../../v1/cases/development-v1-D01.md#response-4)

Evidence IDs: F-D01, A-LABEL. Finish: `stop`; 4.07s. Reference contents: 0 (model-read). Missing reads are a separate protocol result; routing text alone is not a fabricated-read finding.

## Review 5

**candidate · C0 · 2048 tokens** — Longer output completes the same invented manager/query-based implementation as G01 and adds unsupported deprecation claims. More tokens do not repair the missing native-label explanation or version substitution.

[Exact prompt and tools](../../v1/prompts/cb2a45b991efe4c0.json) · [Complete original output](../../v1/cases/development-v1-D01.md#response-5)

**invented_api**, evidence `A-UIKIT`:

````text
let accessibilityManager = UIAccessibilityManager()
````

Evidence IDs: F-D01, A-UIKIT. Finish: `stop`; 6.45s. Reference contents: 0 (unavailable). Missing reads are a separate protocol result; routing text alone is not a fabricated-read finding.

## Review 6

**candidate · C2 · 2048 tokens** — Useful naming, decorative-content and semantic-control advice earns partial task credit. The example uses invalid active/icon traits and turns text labeling into button implementation without explaining native defaults. Generic future-OS caution coexists with unjustified high freshness.

[Exact prompt and tools](../../v1/prompts/717a76a05dcfe728.json) · [Complete original output](../../v1/cases/development-v1-D01.md#response-6)

**invented_api**, evidence `A-TRAITS`:

````text
label.accessibilityTraits = [.active, .button]
````

Evidence IDs: F-D01, A-TRAITS. Finish: `stop`; 6.11s. Reference contents: 1 (injected). Missing reads are a separate protocol result; routing text alone is not a fabricated-read finding.

## Review 7

**candidate · C3-original · 2048 tokens** — Confuses accessible name with accessibilityValue and requires explicit value configuration. Claims the guideline requires both label and value, which it does not. Some relevant testing is present but the central rule is wrong.

[Exact prompt and tools](../../v1/prompts/903d54d036521c4f.json) · [Complete original output](../../v1/cases/development-v1-D01.md#response-7)

Evidence IDs: F-D01, A-LABEL. Finish: `stop`; 4.78s. Reference contents: 0 (model-read). Missing reads are a separate protocol result; routing text alone is not a fabricated-read finding.

## Review 8

**candidate · C3-explicit · 2048 tokens** — Gives relevant meaningful-text and verification advice but omits text-derived defaults and conditional customization. Role terminology is confused, hint guidance is vague and duplicated high-freshness/source assertions overstate support. No implementable core explanation.

[Exact prompt and tools](../../v1/prompts/23b63fe9b6c0df0e.json) · [Complete original output](../../v1/cases/development-v1-D01.md#response-8)

Evidence IDs: F-D01, A-LABEL. Finish: `stop`; 4.02s. Reference contents: 0 (model-read). Missing reads are a separate protocol result; routing text alone is not a fabricated-read finding.

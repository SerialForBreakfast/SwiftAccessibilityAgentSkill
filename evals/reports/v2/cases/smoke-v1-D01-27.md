# D01 · UILabel accessibility

[← v2 dashboard](../README.md) · [Original v1 comparison](../../v1/cases/smoke-v1-D01-27.md)

## Exact original question

```text
Tell me about UILabel accessibility.
Deployment context: uikit OS version 27. Clarify platform if needed.
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
| candidate · C0 | 1024 | 0/1/0/2 | 13.75 | invented_api | [Response 1](../../v1/cases/smoke-v1-D01-27.md#response-1) | [Rationale](#review-1) |
| candidate · C1 | 1024 | 1/1/0/2 | 23.75 | invented_api | [Response 2](../../v1/cases/smoke-v1-D01-27.md#response-2) | [Rationale](#review-2) |
| candidate · C2 | 1024 | 2/2/1/3 | 48.75 | None identified | [Response 3](../../v1/cases/smoke-v1-D01-27.md#response-3) | [Rationale](#review-3) |
| candidate · C3 | 1024 | 1/1/0/1 | 21.25 | None identified | [Response 4](../../v1/cases/smoke-v1-D01-27.md#response-4) | [Rationale](#review-4) |
| baseline · C0 | 1024 | 0/1/0/2 | 13.75 | invented_api | [Response 5](../../v1/cases/smoke-v1-D01-27.md#response-5) | [Rationale](#review-5) |
| baseline · C1 | 1024 | 0/1/1/2 | 17.50 | invented_api | [Response 6](../../v1/cases/smoke-v1-D01-27.md#response-6) | [Rationale](#review-6) |
| baseline · C2 | 1024 | 1/1/0/2 | 23.75 | None identified | [Response 7](../../v1/cases/smoke-v1-D01-27.md#response-7) | [Rationale](#review-7) |
| baseline · C3 | 1024 | 1/1/0/2 | 23.75 | invented_api | [Response 8](../../v1/cases/smoke-v1-D01-27.md#response-8) | [Rationale](#review-8) |

## Review 1

**candidate · C0 · 1024 tokens** — The accessibility-tree protocol and trait/action API are invented; hints are incorrectly treated as missing-label fallbacks and identifiers as activation mechanisms. A few genuine property names do not make the example usable.

[Exact prompt and tools](../../v1/prompts/e24efee8f906cebe.json) · [Complete original output](../../v1/cases/smoke-v1-D01-27.md#response-1)

**invented_api**, evidence `A-UIKIT`:

````text
let accessibilityTree = AccessibilityTreeModel()
````

Evidence IDs: F-D01, A-UIKIT. Finish: `stop`; 5.02s. Reference contents: 0 (unavailable). Missing reads are a separate protocol result; routing text alone is not a fabricated-read finding.

## Review 2

**candidate · C1 · 1024 tokens** — Recognizes text as a semantic source but denies the normal accessibilityLabel interface, mixes text resizing with content changes, and recommends nonexistent editable/scrollable trait constants.

[Exact prompt and tools](../../v1/prompts/17742655648f2574.json) · [Complete original output](../../v1/cases/smoke-v1-D01-27.md#response-2)

**invented_api**, evidence `A-TRAITS`:

````text
`UITraitContentEditable`, `UITraitScrollable`
````

Evidence IDs: F-D01, A-TRAITS. Finish: `stop`; 4.84s. Reference contents: 0 (unavailable). Missing reads are a separate protocol result; routing text alone is not a fabricated-read finding.

## Review 3

**candidate · C2 · 1024 tokens** — Provides meaningful naming, decorative-content handling and useful VoiceOver checks. However, mandates explicit labels for every UILabel, duplicates label text into value, and gives muddled hosting advice. Misses the core native-default/conditional-customization criterion.

[Exact prompt and tools](../../v1/prompts/c54dfb98c7100346.json) · [Complete original output](../../v1/cases/smoke-v1-D01-27.md#response-3)

Evidence IDs: F-D01, A-LABEL. Finish: `stop`; 6.10s. Reference contents: 1 (injected). Missing reads are a separate protocol result; routing text alone is not a fabricated-read finding.

## Review 4

**candidate · C3 · 1024 tokens** — Repeats meaningful-text checks but conflates label/value/hint and never explains native labeling or when to customize. Repetitious unrelated checks and version substitution obscure the answer. Source claims are assessed separately from actual read evidence.

[Exact prompt and tools](../../v1/prompts/6535cf26df860011.json) · [Complete original output](../../v1/cases/smoke-v1-D01-27.md#response-4)

Evidence IDs: F-D01. Finish: `stop`; 5.36s. Reference contents: 0 (model-read). Missing reads are a separate protocol result; routing text alone is not a fabricated-read finding.

## Review 5

**baseline · C0 · 1024 tokens** — The accessibility-tree protocol and trait/action API are invented; hints are incorrectly treated as missing-label fallbacks and identifiers as activation mechanisms. A few genuine property names do not make the example usable.

[Exact prompt and tools](../../v1/prompts/e24efee8f906cebe.json) · [Complete original output](../../v1/cases/smoke-v1-D01-27.md#response-5)

**invented_api**, evidence `A-UIKIT`:

````text
let accessibilityTree = AccessibilityTreeModel()
````

Evidence IDs: F-D01, A-UIKIT. Finish: `stop`; 5.05s. Reference contents: 0 (unavailable). Missing reads are a separate protocol result; routing text alone is not a fabricated-read finding.

## Review 6

**baseline · C1 · 1024 tokens** — Some useful emphasis on meaningful text is overwhelmed by nonexistent Dynamic Type/grouping APIs, the wrong UILabel superclass, and advice to move labels out of scroll views. Future-version caveat does not qualify the invented implementation. Ends truncated.

[Exact prompt and tools](../../v1/prompts/f22bd95b2fdefceb.json) · [Complete original output](../../v1/cases/smoke-v1-D01-27.md#response-6)

**invented_api**, evidence `A-UILABEL`:

````text
`dynamicType = 2`
````

Evidence IDs: F-D01, A-UILABEL. Finish: `length`; 6.48s. Reference contents: 0 (unavailable). Missing reads are a separate protocol result; routing text alone is not a fabricated-read finding.

## Review 7

**baseline · C2 · 1024 tokens** — Contradicts itself about nil labels, mandates redundant explicit labels/values, and adds unsupported property/hosting guidance. Some genuine label and hint information survives, but substantial correction is needed. Truncated ending is retained.

[Exact prompt and tools](../../v1/prompts/078e7a104ce8288f.json) · [Complete original output](../../v1/cases/smoke-v1-D01-27.md#response-7)

Evidence IDs: F-D01, A-LABEL. Finish: `length`; 6.47s. Reference contents: 1 (injected). Missing reads are a separate protocol result; routing text alone is not a fabricated-read finding.

## Review 8

**baseline · C3 · 1024 tokens** — Meaningful visible text is relevant, but the recommended trait constants are not the UIKit API. Requires keyboard interaction from a text label and omits the normal text-derived label behavior and conditional customization.

[Exact prompt and tools](../../v1/prompts/02f4554027f1b4d7.json) · [Complete original output](../../v1/cases/smoke-v1-D01-27.md#response-8)

**invented_api**, evidence `A-TRAITS`:

````text
Use `UITraitLabel` for standard text labels.
````

Evidence IDs: F-D01, A-TRAITS. Finish: `stop`; 6.03s. Reference contents: 0 (model-read). Missing reads are a separate protocol result; routing text alone is not a fabricated-read finding.

# D02 · Settings row navigation

[← v2 dashboard](../README.md) · [Original v1 comparison](../../v1/cases/development-v1-D02.md)

## Exact original question

```text
My settings row has text, a switch, and a help button. How should VoiceOver move through it?
Deployment context: uikit OS version 26. Clarify platform if needed.
```

## New rubric criteria

- Preserve independently operable controls; avoid flattening away help or switch state.
- Keep the switch state/change and help action independently available.
- Allow more than one defensible grouping when all functions remain reachable.

These are grading criteria, not a model-generated gold answer. [Frozen rubric](../rubric-snapshot.json); [evidence](../grading-evidence-snapshot.json). [Supplement and source IDs](../EVIDENCE.md). Single reviewer, unblinded and not independently calibrated.

## Score comparison

Scores C/T/Cal/R are correctness/task success/calibration/relevance, each 0–4. Weighted quality is 0–100, not percent accuracy.

| Variant | Cap | C/T/Cal/R | Quality | Critical flag | Original answer | Review |
| --- | ---: | --- | ---: | --- | --- | --- |
| candidate · C0 | 1024 | 0/1/0/2 | 13.75 | invented_api | [Response 1](../../v1/cases/development-v1-D02.md#response-1) | [Rationale](#review-1) |
| candidate · C2 | 1024 | 1/0/0/2 | 15.00 | lost_functionality | [Response 2](../../v1/cases/development-v1-D02.md#response-2) | [Rationale](#review-2) |
| candidate · C3-original | 1024 | 0/0/1/1 | 6.25 | None identified | [Response 3](../../v1/cases/development-v1-D02.md#response-3) | [Rationale](#review-3) |
| candidate · C3-explicit | 1024 | 1/0/1/1 | 16.25 | None identified | [Response 4](../../v1/cases/development-v1-D02.md#response-4) | [Rationale](#review-4) |
| candidate · C0 | 2048 | 0/1/0/2 | 13.75 | invented_api | [Response 5](../../v1/cases/development-v1-D02.md#response-5) | [Rationale](#review-5) |
| candidate · C2 | 2048 | 1/0/0/2 | 15.00 | lost_functionality | [Response 6](../../v1/cases/development-v1-D02.md#response-6) | [Rationale](#review-6) |
| candidate · C3-original | 2048 | 0/0/1/1 | 6.25 | None identified | [Response 7](../../v1/cases/development-v1-D02.md#response-7) | [Rationale](#review-7) |
| candidate · C3-explicit | 2048 | 1/0/1/1 | 16.25 | None identified | [Response 8](../../v1/cases/development-v1-D02.md#response-8) | [Rationale](#review-8) |

## Review 1

**candidate · C0 · 1024 tokens** — The truncated version of G19 retains the same invented framework/properties and incorrect Home-button navigation. Mentioning a plausible three-element order earns limited task credit, not a usable implementation.

[Exact prompt and tools](../../v1/prompts/11dccc9238ad0718.json) · [Complete original output](../../v1/cases/development-v1-D02.md#response-1)

**invented_api**, evidence `A-UIKIT; F-D02`:

````text
import AccessibilityUI
````

Evidence IDs: F-D02, A-UIKIT. Finish: `length`; 5.98s. Reference contents: 0 (unavailable). Missing reads are a separate protocol result; routing text alone is not a fabricated-read finding.

## Review 2

**candidate · C2 · 1024 tokens** — Starts with a plausible traversal, then explicitly requires the switch and help button not be separate focus targets and treats them as one action. No alternative distinct actions are supplied. This defeats the central operability criterion despite the injected reference saying to preserve it.

[Exact prompt and tools](../../v1/prompts/5da8800836771584.json) · [Complete original output](../../v1/cases/development-v1-D02.md#response-2)

**lost_functionality**, evidence `F-D02`:

````text
Verify that the Switch and Button are not separate focus targets.
````

Evidence IDs: F-D02. Finish: `stop`; 5.48s. Reference contents: 1 (injected). Missing reads are a separate protocol result; routing text alone is not a fabricated-read finding.

## Review 3

**candidate · C3-original · 1024 tokens** — Asks for a framework already supplied and gives incorrect hierarchy/version explanations. Clarification could be reasonable for ambiguous context, but it never preserves or explains the switch and help actions; substantial unsupported claims accompany the request.

[Exact prompt and tools](../../v1/prompts/a741a7800be6f6be.json) · [Complete original output](../../v1/cases/development-v1-D02.md#response-3)

Evidence IDs: F-D02. Finish: `stop`; 2.57s. Reference contents: 0 (model-read). Missing reads are a separate protocol result; routing text alone is not a fabricated-read finding.

## Review 4

**candidate · C3-explicit · 1024 tokens** — Asks clarifying questions instead of answering how the two actions remain accessible. Invents Settings-app/list-sheet behavior not supplied by the user. Some recognition that structure matters, but no solution to the stated row.

[Exact prompt and tools](../../v1/prompts/fb3f9e8c8c895afe.json) · [Complete original output](../../v1/cases/development-v1-D02.md#response-4)

Evidence IDs: F-D02. Finish: `stop`; 3.47s. Reference contents: 0 (model-read). Missing reads are a separate protocol result; routing text alone is not a fabricated-read finding.

## Review 5

**candidate · C0 · 2048 tokens** — Names a plausible label/switch/help sequence but builds it from a nonexistent AccessibilityUI framework and properties. Home-button navigation and fabricated API examples make the proposed solution unusable.

[Exact prompt and tools](../../v1/prompts/11dccc9238ad0718.json) · [Complete original output](../../v1/cases/development-v1-D02.md#response-5)

**invented_api**, evidence `A-UIKIT; F-D02`:

````text
import AccessibilityUI
````

Evidence IDs: F-D02, A-UIKIT. Finish: `stop`; 7.51s. Reference contents: 0 (unavailable). Missing reads are a separate protocol result; routing text alone is not a fabricated-read finding.

## Review 6

**candidate · C2 · 2048 tokens** — Starts with a plausible traversal, then explicitly requires the switch and help button not be separate focus targets and treats them as one action. No alternative distinct actions are supplied. This defeats the central operability criterion despite the injected reference saying to preserve it.

[Exact prompt and tools](../../v1/prompts/5da8800836771584.json) · [Complete original output](../../v1/cases/development-v1-D02.md#response-6)

**lost_functionality**, evidence `F-D02`:

````text
Verify that the Switch and Button are not separate focus targets.
````

Evidence IDs: F-D02. Finish: `stop`; 5.61s. Reference contents: 1 (injected). Missing reads are a separate protocol result; routing text alone is not a fabricated-read finding.

## Review 7

**candidate · C3-original · 2048 tokens** — Asks for a framework already supplied and gives incorrect hierarchy/version explanations. Clarification could be reasonable for ambiguous context, but it never preserves or explains the switch and help actions; substantial unsupported claims accompany the request.

[Exact prompt and tools](../../v1/prompts/a741a7800be6f6be.json) · [Complete original output](../../v1/cases/development-v1-D02.md#response-7)

Evidence IDs: F-D02. Finish: `stop`; 2.64s. Reference contents: 0 (model-read). Missing reads are a separate protocol result; routing text alone is not a fabricated-read finding.

## Review 8

**candidate · C3-explicit · 2048 tokens** — Asks clarifying questions instead of answering how the two actions remain accessible. Invents Settings-app/list-sheet behavior not supplied by the user. Some recognition that structure matters, but no solution to the stated row.

[Exact prompt and tools](../../v1/prompts/fb3f9e8c8c895afe.json) · [Complete original output](../../v1/cases/development-v1-D02.md#response-8)

Evidence IDs: F-D02. Finish: `stop`; 3.53s. Reference contents: 0 (model-read). Missing reads are a separate protocol result; routing text alone is not a fabricated-read finding.

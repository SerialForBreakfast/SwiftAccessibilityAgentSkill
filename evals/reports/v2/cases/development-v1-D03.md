# D03 · Discoverable message deletion

[← v2 dashboard](../README.md) · [Original v1 comparison](../../v1/cases/development-v1-D03.md)

## Exact original question

```text
Can people delete a message without finding the swipe gesture?
Deployment context: uikit OS version 26. Clarify platform if needed.
```

## New rubric criteria

- Expose a named action and preserve a discoverable ordinary interaction.
- Name the deletion outcome, not the physical gesture.
- A custom action is useful; an equivalent discoverable control is also acceptable.

These are grading criteria, not a model-generated gold answer. [Frozen rubric](../rubric-snapshot.json); [evidence](../grading-evidence-snapshot.json). [Supplement and source IDs](../EVIDENCE.md). Single reviewer, unblinded and not independently calibrated.

## Score comparison

Scores C/T/Cal/R are correctness/task success/calibration/relevance, each 0–4. Weighted quality is 0–100, not percent accuracy.

| Variant | Cap | C/T/Cal/R | Quality | Critical flag | Original answer | Review |
| --- | ---: | --- | ---: | --- | --- | --- |
| candidate · C0 | 1024 | 0/0/0/2 | 5.00 | None identified | [Response 1](../../v1/cases/development-v1-D03.md#response-1) | [Rationale](#review-1) |
| candidate · C2 | 1024 | 0/0/0/2 | 5.00 | lost_functionality | [Response 2](../../v1/cases/development-v1-D03.md#response-2) | [Rationale](#review-2) |
| candidate · C3-original | 1024 | 0/0/0/2 | 5.00 | lost_functionality | [Response 3](../../v1/cases/development-v1-D03.md#response-3) | [Rationale](#review-3) |
| candidate · C3-explicit | 1024 | 0/0/0/2 | 5.00 | None identified | [Response 4](../../v1/cases/development-v1-D03.md#response-4) | [Rationale](#review-4) |
| candidate · C0 | 2048 | 0/0/0/2 | 5.00 | None identified | [Response 5](../../v1/cases/development-v1-D03.md#response-5) | [Rationale](#review-5) |
| candidate · C2 | 2048 | 0/0/0/2 | 5.00 | lost_functionality | [Response 6](../../v1/cases/development-v1-D03.md#response-6) | [Rationale](#review-6) |
| candidate · C3-original | 2048 | 0/0/0/2 | 5.00 | lost_functionality | [Response 7](../../v1/cases/development-v1-D03.md#response-7) | [Rationale](#review-7) |
| candidate · C3-explicit | 2048 | 0/0/0/2 | 5.00 | None identified | [Response 8](../../v1/cases/development-v1-D03.md#response-8) | [Rationale](#review-8) |

## Review 1

**candidate · C0 · 1024 tokens** — Says yes but invents tap-to-delete and automatic inactivity deletion in an unspecified application. Provides neither a named accessibility action nor a concrete discoverable control design.

[Exact prompt and tools](../../v1/prompts/d3da751b475af4f8.json) · [Complete original output](../../v1/cases/development-v1-D03.md#response-1)

Evidence IDs: F-D03, A-ACTION. Finish: `stop`; 1.54s. Reference contents: 0 (unavailable). Missing reads are a separate protocol result; routing text alone is not a fabricated-read finding.

## Review 2

**candidate · C2 · 1024 tokens** — Contradicts the supplied custom-action reference: calls the physical swipe itself the custom action and tells VoiceOver/Switch users to rely on it. Invents deployment notes and app behavior. No usable deletion alternative.

[Exact prompt and tools](../../v1/prompts/1950529a315f722a.json) · [Complete original output](../../v1/cases/development-v1-D03.md#response-2)

**lost_functionality**, evidence `F-D03; A-ACTION`:

````text
the "custom action" is the swipe gesture itself
````

Evidence IDs: F-D03, A-ACTION. Finish: `stop`; 4.29s. Reference contents: 1 (injected). Missing reads are a separate protocol result; routing text alone is not a fabricated-read finding.

## Review 3

**candidate · C3-original · 1024 tokens** — Invents a Message view implementation and explicitly calls swipe-only deletion accessible. It withholds the required independently discoverable deletion mechanism and misrepresents custom-action guidance.

[Exact prompt and tools](../../v1/prompts/3daa2a75ddc05d1b.json) · [Complete original output](../../v1/cases/development-v1-D03.md#response-3)

**lost_functionality**, evidence `F-D03`:

````text
Since the swipe gesture is the only way to delete the message, the `delete` action is considered accessible.
````

Evidence IDs: F-D03. Finish: `stop`; 3.99s. Reference contents: 0 (model-read). Missing reads are a separate protocol result; routing text alone is not a fabricated-read finding.

## Review 4

**candidate · C3-explicit · 1024 tokens** — Denies a discoverable alternative based on an invented system-wide swipe-only rule. The brief suggestion to keep a delete button or gesture visible never explains a working accessible action/control. Answers the topic directly but incorrectly.

[Exact prompt and tools](../../v1/prompts/8a5b93e69493eaee.json) · [Complete original output](../../v1/cases/development-v1-D03.md#response-4)

Evidence IDs: F-D03, A-ACTION. Finish: `stop`; 2.81s. Reference contents: 0 (model-read). Missing reads are a separate protocol result; routing text alone is not a fabricated-read finding.

## Review 5

**candidate · C0 · 2048 tokens** — Says yes but invents tap-to-delete and automatic inactivity deletion in an unspecified application. Provides neither a named accessibility action nor a concrete discoverable control design.

[Exact prompt and tools](../../v1/prompts/d3da751b475af4f8.json) · [Complete original output](../../v1/cases/development-v1-D03.md#response-5)

Evidence IDs: F-D03, A-ACTION. Finish: `stop`; 1.60s. Reference contents: 0 (unavailable). Missing reads are a separate protocol result; routing text alone is not a fabricated-read finding.

## Review 6

**candidate · C2 · 2048 tokens** — Contradicts the supplied custom-action reference: calls the physical swipe itself the custom action and tells VoiceOver/Switch users to rely on it. Invents deployment notes and app behavior. No usable deletion alternative.

[Exact prompt and tools](../../v1/prompts/1950529a315f722a.json) · [Complete original output](../../v1/cases/development-v1-D03.md#response-6)

**lost_functionality**, evidence `F-D03; A-ACTION`:

````text
the "custom action" is the swipe gesture itself
````

Evidence IDs: F-D03, A-ACTION. Finish: `stop`; 4.44s. Reference contents: 1 (injected). Missing reads are a separate protocol result; routing text alone is not a fabricated-read finding.

## Review 7

**candidate · C3-original · 2048 tokens** — Invents a Message view implementation and explicitly calls swipe-only deletion accessible. It withholds the required independently discoverable deletion mechanism and misrepresents custom-action guidance.

[Exact prompt and tools](../../v1/prompts/3daa2a75ddc05d1b.json) · [Complete original output](../../v1/cases/development-v1-D03.md#response-7)

**lost_functionality**, evidence `F-D03`:

````text
Since the swipe gesture is the only way to delete the message, the `delete` action is considered accessible.
````

Evidence IDs: F-D03. Finish: `stop`; 4.03s. Reference contents: 0 (model-read). Missing reads are a separate protocol result; routing text alone is not a fabricated-read finding.

## Review 8

**candidate · C3-explicit · 2048 tokens** — Denies a discoverable alternative based on an invented system-wide swipe-only rule. The brief suggestion to keep a delete button or gesture visible never explains a working accessible action/control. Answers the topic directly but incorrectly.

[Exact prompt and tools](../../v1/prompts/8a5b93e69493eaee.json) · [Complete original output](../../v1/cases/development-v1-D03.md#response-8)

Evidence IDs: F-D03, A-ACTION. Finish: `stop`; 2.81s. Reference contents: 0 (model-read). Missing reads are a separate protocol result; routing text alone is not a fabricated-read finding.

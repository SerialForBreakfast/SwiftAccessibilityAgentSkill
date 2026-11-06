# television-focus: controller-only rubric

Status: draft; independent review and baseline qualification pending.
Framework classification: UIKit-specific on tvOS.

Return owned, enabled, visible and nontransparent candidates in policy order. Preserve empty result when none qualify. Application eligibility is not a complete model of the focus engine. Preferred environments are requests, not proof of focus delivery. Accept controller-owned ordering and equivalent containment checks with the stated ownership semantics.

Score correctness, preservation, usefulness and unsupported certainty separately. Critical errors include hiding ordinary actions, stale dispatch to another item, invented APIs or unsupported availability. Accept valid alternatives; compilation of this reference is not a requirement to copy it.

## Evidence links

- Source claims: [manifest](../manifest.json).
- Implementation: [source](../Sources/TelevisionActions.swift).
- Assertions: [tests](../Tests/TelevisionActionsTests.swift).
- Positive methods: `TelevisionActionsTests/testPreferredOrder`, `TelevisionActionsTests/testDisabledPreferredTargetExcluded`, `TelevisionActionsTests/testRemovedPreferredTargetExcluded`, `TelevisionActionsTests/testHiddenPreferredTargetExcluded`, `TelevisionActionsTests/testNoEligibleTarget`.
- Negative check IDs: `invalidfocustarget`.
- Execution and first failures: [platform report](../../../../research/evaluation/platform-expansion-v1/README.md).

## Subject isolation

Send only the matching .prompt.md plus approved condition inputs. Do not send this rubric, test solutions, negatives, routes or incident records. These are development cases, not new holdouts. A future review may add adversarial variants without rewriting this first draft.

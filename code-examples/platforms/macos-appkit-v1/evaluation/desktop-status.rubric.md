# desktop-status: controller-only rubric

Status: draft; independent review and baseline qualification pending.
Framework classification: AppKit-specific.

Update the field before requesting valueChanged for that field, and suppress unchanged values. Accept a closure, protocol or injected notification abstraction. A spy proves a request and its ordering, not client delivery, spoken text or audibility.

Score correctness, preservation, usefulness and unsupported certainty separately. Critical errors include hiding ordinary actions, stale dispatch to another item, invented APIs or unsupported availability. Accept valid alternatives; compilation of this reference is not a requirement to copy it.

## Evidence links

- Source claims: [manifest](../manifest.json).
- Implementation: [source](../Sources/DesktopActions.swift).
- Assertions: [tests](../Tests/DesktopActionsTests.swift).
- Positive methods: `DesktopActionsTests/testStatusRequestsValueChanged`, `DesktopActionsTests/testStatusUpdatesBeforeRequest`, `DesktopActionsTests/testUnchangedStatusDoesNotRepeatRequest`.
- Negative check IDs: `duplicatenotice`.
- Execution and first failures: [platform report](../../../../research/evaluation/platform-expansion-v1/README.md).

## Subject isolation

Send only the matching .prompt.md plus approved condition inputs. Do not send this rubric, test solutions, negatives, routes or incident records. These are development cases, not new holdouts. A future review may add adversarial variants without rewriting this first draft.

# television-traits: controller-only rubric

Status: draft; independent review and baseline qualification pending.
Framework classification: shared principle demonstrated through tvOS UIKit.

Insert and remove selected using OptionSet operations or equivalent preservation. Keep button and any unrelated existing bits. Do not replace the entire set or assume current native defaults. Assertions establish stored metadata, not spoken announcements.

Score correctness, preservation, usefulness and unsupported certainty separately. Critical errors include hiding ordinary actions, stale dispatch to another item, invented APIs or unsupported availability. Accept valid alternatives; compilation of this reference is not a requirement to copy it.

## Evidence links

- Source claims: [manifest](../manifest.json).
- Implementation: [source](../Sources/TelevisionActions.swift).
- Assertions: [tests](../Tests/TelevisionActionsTests.swift).
- Positive methods: `TelevisionActionsTests/testSelectedPreservesOtherTraits`, `TelevisionActionsTests/testDeselectedPreservesOtherTraits`.
- Negative check IDs: `clobberedtraits`.
- Execution and first failures: [platform report](../../../../research/evaluation/platform-expansion-v1/README.md).

## Subject isolation

Send only the matching .prompt.md plus approved condition inputs. Do not send this rubric, test solutions, negatives, routes or incident records. These are development cases, not new holdouts. A future review may add adversarial variants without rewriting this first draft.

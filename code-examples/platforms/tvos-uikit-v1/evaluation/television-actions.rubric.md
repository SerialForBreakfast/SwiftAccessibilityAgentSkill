# television-actions: controller-only rubric

Status: draft; independent review and baseline qualification pending.
Framework classification: UIKit-specific on tvOS.

Provide visible localized button titles as well as accessible names, and refresh both on reuse. Preserve both ordinary primary actions and accessible elements; shortcuts supplement rather than replace buttons. Replace old callbacks and metadata without duplicates. Reject obsolete retained actions and disabled dispatch. Accept target/action or UIAction, valid selector or handler custom actions, different ownership solutions. Do not prescribe touchUpInside as the sole remote activation path or claim dispatch tests simulate a remote.

Score correctness, preservation, usefulness and unsupported certainty separately. Critical errors include hiding ordinary actions, stale dispatch to another item, invented APIs or unsupported availability. Accept valid alternatives; compilation of this reference is not a requirement to copy it.

## Evidence links

- Source claims: [manifest](../manifest.json).
- Implementation: [source](../Sources/TelevisionActions.swift).
- Assertions: [tests](../Tests/TelevisionActionsTests.swift).
- Additional positive methods: `TelevisionActionsTests/testVisibleActionNames`, `TelevisionActionsTests/testVisibleNamesRefresh`.
- Original-defect regression: `original-missing-titles` is preserved author code, not a deliberate mutation.
- Positive methods: `TelevisionActionsTests/testContextualNames`, `TelevisionActionsTests/testContainerPreservesControls`, `TelevisionActionsTests/testOrdinaryPlay`, `TelevisionActionsTests/testOrdinaryDetails`, `TelevisionActionsTests/testCustomDetails`, `TelevisionActionsTests/testStaleActionRejected`, `TelevisionActionsTests/testReuseReplacesHandler`, `TelevisionActionsTests/testReuseNames`, `TelevisionActionsTests/testReuseClearsValue`, `TelevisionActionsTests/testDisabledOrdinaryAction`, `TelevisionActionsTests/testDisabledCustomAction`, `TelevisionActionsTests/testActionDoesNotRetainRow`, `TelevisionActionsTests/testSingleShortcutAfterReuse`.
- Negative check IDs: `lostordinarydetails`, `staleshortcut`, `hiddencontrols`.
- Execution and first failures: [platform report](../../../../research/evaluation/platform-expansion-v1/README.md).

## Subject isolation

Send only the matching .prompt.md plus approved condition inputs. Do not send this rubric, test solutions, negatives, routes or incident records. These are development cases, not new holdouts. A future review may add adversarial variants without rewriting this first draft.

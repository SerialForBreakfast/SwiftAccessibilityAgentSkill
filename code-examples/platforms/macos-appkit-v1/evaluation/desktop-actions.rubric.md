# desktop-actions: controller-only rubric

Status: draft; independent review and baseline qualification pending.
Framework classification: AppKit-specific.

Retain independent ordinary controls and localized metadata. Reconfiguration replaces owned names, values and callbacks. A retained previous-item shortcut must not act on the newly bound item; disabled actions reject dispatch. Closures should not retain the row. Accept target/action or equivalent AppKit dispatch and revision tokens, invalidated actions, or item-bound ownership with equivalent semantics. Do not require this exact NSStackView design or exact helper names.

Score correctness, preservation, usefulness and unsupported certainty separately. Critical errors include hiding ordinary actions, stale dispatch to another item, invented APIs or unsupported availability. Accept valid alternatives; compilation of this reference is not a requirement to copy it.

## Evidence links

- Source claims: [manifest](../manifest.json).
- Implementation: [source](../Sources/DesktopActions.swift).
- Assertions: [tests](../Tests/DesktopActionsTests.swift).
- Positive methods: `DesktopActionsTests/testVisibleTitle`, `DesktopActionsTests/testContextualNames`, `DesktopActionsTests/testContainerDoesNotReplaceControls`, `DesktopActionsTests/testControlsRemainInHierarchy`, `DesktopActionsTests/testOrdinaryOpenOnly`, `DesktopActionsTests/testOrdinarySaveOnly`, `DesktopActionsTests/testShortcutDispatch`, `DesktopActionsTests/testShortcutLocalizedName`, `DesktopActionsTests/testStaleShortcutRejected`, `DesktopActionsTests/testReuseReplacesOrdinaryHandler`, `DesktopActionsTests/testReuseReplacesNames`, `DesktopActionsTests/testReuseClearsOwnedValue`, `DesktopActionsTests/testDisabledOrdinarySave`, `DesktopActionsTests/testDisabledShortcut`, `DesktopActionsTests/testReenabledShortcut`, `DesktopActionsTests/testShortcutDoesNotRetainRow`, `DesktopActionsTests/testRepeatedConfigurationDoesNotDuplicateActions`.
- Negative check IDs: `lostordinarysave`, `staleshortcut`, `lostname`, `disabledshortcut`.
- Execution and first failures: [platform report](../../../../research/evaluation/platform-expansion-v1/README.md).

## Subject isolation

Send only the matching .prompt.md plus approved condition inputs. Do not send this rubric, test solutions, negatives, routes or incident records. These are development cases, not new holdouts. A future review may add adversarial variants without rewriting this first draft.

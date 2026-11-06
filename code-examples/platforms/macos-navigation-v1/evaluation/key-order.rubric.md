# key-order: controller rubric

Status: draft, not independently reviewed or baseline-eligible.
Classification: AppKit-specific.

Build owned links in requested order after deduplication; exclude hidden/disabled controls; clear both incoming excluded links and previous removed links. Empty input and explicit stop clear prior owned links. A single eligible control may self-cycle under this requested policy. Accept identity sets or equivalent uniqueness checks; do not equate key-view assignment with actual first-responder traversal. Do not rewrite links outside the helper's ownership.

Grade correctness, preservation, practical usefulness and unsupported certainty separately. Hidden ordinary actions, wrong-item dispatch and invented availability are critical errors. Do not penalize valid implementation alternatives simply for differing from the reference.

## Traceability

- [Apple claims and check IDs](../manifest.json)
- [Example](../Sources/DesktopNavigation.swift)
- [Unit assertions](../Tests/DesktopNavigationTests.swift)
- Methods: `DesktopNavigationTests/testKeyCycleFollowsInputOrder`, `DesktopNavigationTests/testDisabledKeyViewExcluded`, `DesktopNavigationTests/testHiddenKeyViewExcluded`, `DesktopNavigationTests/testRemovedKeyLinksCleared`, `DesktopNavigationTests/testDuplicateKeyInputDoesNotBreakCycle`, `DesktopNavigationTests/testStopClearsOwnedLinks`, `DesktopNavigationTests/testIncomingDisabledLinkCleared`, `DesktopNavigationTests/testEmptyKeyOrderClearsPriorLinks`.
- Negative checks: `disabledkeyview`, `leakedkeylinks`, `original-incoming-link`.
- [Execution and first failures](../../../../research/evaluation/platform-navigation-v1/README.md)

Subject input is the matching .prompt.md only plus approved evaluation-condition material. Keep this rubric, solutions, tests, routes and incident history out of subject inputs. These are development cases, not fresh holdouts.

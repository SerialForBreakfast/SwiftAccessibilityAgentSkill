# motion-status: controller rubric

Status: draft, not independently reviewed or baseline-eligible.
Classification: Shared principle demonstrated through UIKit/tvOS.

Commit final visible/accessibility text independently of animation completion, read current motion preference on changed messages, skip animation under reduce motion, suppress unchanged updates and preserve localized input. Accept a protocol or closures, native label text semantics where equivalent, or alternate animation adapters. Injected settings tests do not prove system preference notifications or visual animation quality.

Grade correctness, preservation, practical usefulness and unsupported certainty separately. Hidden ordinary actions, wrong-item dispatch and invented availability are critical errors. Do not penalize valid implementation alternatives simply for differing from the reference.

## Traceability

- [Apple claims and check IDs](../manifest.json)
- [Example](../Sources/TelevisionResults.swift)
- [Unit assertions](../Tests/TelevisionResultsTests.swift)
- Methods: `TelevisionResultsTests/testReducedMotionStillUpdatesContent`, `TelevisionResultsTests/testNormalMotionAnimatesAfterContent`, `TelevisionResultsTests/testPreferenceReadOnEachChange`, `TelevisionResultsTests/testRepeatedStatusIsQuiet`, `TelevisionResultsTests/testStatusRemainsAccessible`, `TelevisionResultsTests/testLocalizedStatusPreserved`.
- Negative checks: `motionhidescontent`, `repeatedanimation`.
- [Execution and first failures](../../../../research/evaluation/platform-navigation-v1/README.md)

Subject input is the matching .prompt.md only plus approved evaluation-condition material. Keep this rubric, solutions, tests, routes and incident history out of subject inputs. These are development cases, not fresh holdouts.

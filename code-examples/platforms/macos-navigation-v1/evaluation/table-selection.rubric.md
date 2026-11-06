# table-selection: controller rubric

Status: draft, not independently reviewed or baseline-eligible.
Classification: AppKit-specific.

Selection follows identity, not row index or title; removed/unknown IDs clear selection, empty input is valid, duplicate IDs leave state intact, existing native table selection is respected. Accept view-based or data-source-based tables and equivalent stable-ID reconciliation. Do not insist on this helper class, exact API sequence or objectValue implementation. Native stored selection is not keyboard or VoiceOver delivery.

Grade correctness, preservation, practical usefulness and unsupported certainty separately. Hidden ordinary actions, wrong-item dispatch and invented availability are critical errors. Do not penalize valid implementation alternatives simply for differing from the reference.

## Traceability

- [Apple claims and check IDs](../manifest.json)
- [Example](../Sources/DesktopNavigation.swift)
- [Unit assertions](../Tests/DesktopNavigationTests.swift)
- Methods: `DesktopNavigationTests/testRowsAndVisibleValues`, `DesktopNavigationTests/testSelectByIdentity`, `DesktopNavigationTests/testReorderPreservesIdentity`, `DesktopNavigationTests/testRemovedSelectionClears`, `DesktopNavigationTests/testUnknownSelectionClears`, `DesktopNavigationTests/testDuplicateIDsRejectedAtomically`, `DesktopNavigationTests/testEmptyResultsClearSelection`, `DesktopNavigationTests/testNoSelectionIsNotInvented`, `DesktopNavigationTests/testExternalTableSelectionIsPreserved`, `DesktopNavigationTests/testRenamedItemKeepsIdentity`.
- Negative checks: `lostselection`, `duplicateids`.
- [Execution and first failures](../../../../research/evaluation/platform-navigation-v1/README.md)

Subject input is the matching .prompt.md only plus approved evaluation-condition material. Keep this rubric, solutions, tests, routes and incident history out of subject inputs. These are development cases, not fresh holdouts.

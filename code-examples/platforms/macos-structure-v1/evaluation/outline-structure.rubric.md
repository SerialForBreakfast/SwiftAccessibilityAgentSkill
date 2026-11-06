# AppKit/macOS: outline-structure

Status: draft; independent oracle/question review pending. Not baseline-eligible.
Classification: AppKit-specific collection configuration.

Provide conventional outline data-source methods for roots/children/expandability and values per column. Preserve stable node identity across rename/reorder and restore visible selection by ID, not old row number. Validate global identity uniqueness before mutation. Preserve surviving expansion and prevent removed nodes from serving stale data. Clear selection when the requested node is not represented by a visible row. Do not reload from a data-source query. Accept other stable item adapters and update algorithms. Native row/configuration assertions do not prove spoken hierarchy or keyboard traversal.

Score correctness, preservation, practical usefulness and unsupported certainty separately. Invented APIs, lost ordinary actions, erased user input and stale cross-item actions are critical. Accept alternatives satisfying the contract; no requirement for test/helper names. These are known-development cases, not holdouts.

## Traceability

- [Source claims and check IDs](../manifest.json)
- [Implementation](../Sources/DesktopOutline.swift)
- [Unit assertions](../Tests/DesktopOutlineTests.swift)
- Methods: `DesktopOutlineTests/testColumnsHaveDistinctNamesAndOutlineOwnership`, `DesktopOutlineTests/testRootCountAndChildOrder`, `DesktopOutlineTests/testNestedChildrenAndExpandableState`, `DesktopOutlineTests/testEachColumnUsesItsOwnValue`, `DesktopOutlineTests/testRenameRetainsStableNodeIdentity`, `DesktopOutlineTests/testExpansionPersistsAcrossReload`, `DesktopOutlineTests/testSelectedChildSurvivesSiblingReorder`, `DesktopOutlineTests/testRemovedSelectionClears`, `DesktopOutlineTests/testDuplicateRootsAreRejectedAtomically`, `DesktopOutlineTests/testDuplicateNestedIDsAreRejectedAtomically`, `DesktopOutlineTests/testSameIDInDifferentBranchesIsRejected`, `DesktopOutlineTests/testRemovedNodeCannotSupplyStaleChildren`, `DesktopOutlineTests/testUnknownColumnDoesNotInventAValue`, `DesktopOutlineTests/testCollapsedChildCannotSelectWrongRow`, `DesktopOutlineTests/testEmptyUpdateClearsRowsAndSelection`, `DesktopOutlineTests/testDeepNestedRelationshipsAreRetained`.
- Negative checks: `duplicates`, `identity`, `stalenode`, `selection`.
- [Execution and difficulty record](../../../../research/evaluation/platform-structure-v1/README.md)

Subject input is the separate .prompt.md plus approved condition material. Do not inject the rubric, assertions, negative fixtures or incident narrative.

# iOS/SwiftUI documents

Draft development case; independent review pending; not baseline eligible or a holdout.

Use actual SwiftUI List/Section/ForEach and rotor APIs valid for the target. Keep direct actions alongside rotor/custom actions. Only genuine landmarks become headings. Test stable identity and callback ownership separately from rotor discoverability, emitted tree structure and reading order; accept equivalent revision/ownership policies meeting the task.

Grade correctness, ordinary-behavior preservation, practical usefulness and unsupported certainty separately. Critical errors require concrete evidence: invented APIs, lost ordinary actions, stale cross-item dispatch, unsupported availability. Accept equivalent valid implementations and native no-change reasoning. Exact helper names and English sample strings are not required. Missing integration/context is ungradable, not automatically an answer failure.

[Source claims and checks](../manifest.json); [example](../Sources/Documents.swift). Guidelines: G-005, G-006, G-007, G-009, G-014.

Exact assertions:
- `DocumentTests/testLandmarksAreSubsetNotEveryRow`
- `DocumentTests/testDuplicateIDsRejectUpdateAtomically`
- `DocumentTests/testSelectionSurvivesReorder`
- `DocumentTests/testRemovedSelectionClears`
- `DocumentTests/testOldActionDoesNotTargetReboundRow`
- `DocumentTests/testOrdinarySelectionUsesCurrentItem`
- `DocumentTests/testDeleteCurrentItemOnceAndClearSelection`
- `DocumentTests/testUnknownItemActionIsQuiet`
- `DocumentTests/testRetainedActionDoesNotRetainOwner`
- `DocumentTests/testEmptyDocumentHasNoLandmarksOrSelection`

Sources and negative controls remain controller-only; inject only the subject and approved condition material. No independent subject answer exists yet. Native model-policy units are not tests of generated SwiftUI semantics.

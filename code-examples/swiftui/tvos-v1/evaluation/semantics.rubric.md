# tvOS/SwiftUI semantics

Draft development case; independent review pending; not baseline eligible or a holdout.

Native controls remain; do not force a trait override or custom value onto a valid Toggle. Binding transitions, current names/status, disabled actions, bounds and callback counts match the contract. Compile actual modifiers but do not claim generated semantics from the model tests. Equivalent composition and state ownership are valid.

Grade correctness, ordinary-behavior preservation, practical usefulness and unsupported certainty separately. Critical errors require concrete evidence: invented APIs, lost ordinary actions, stale cross-item dispatch, unsupported availability. Accept equivalent valid implementations and native no-change reasoning. Exact helper names and English sample strings are not required. Missing integration/context is ungradable, not automatically an answer failure.

[Source claims and checks](../manifest.json); [example](../Sources/Semantics.swift). Guidelines: G-001, G-002, G-003, G-004, G-007, G-008.

Exact assertions:
- `SemanticsTests/testBindingReadsCurrentNativeToggleState`
- `SemanticsTests/testRepeatedBindingSetDoesNotDuplicateCallback`
- `SemanticsTests/testDisabledBindingPreservesState`
- `SemanticsTests/testBothToggleTransitionsRefreshValue`
- `SemanticsTests/testConfigureClearsPriorStatusAndPriorityWithoutReuse`
- `SemanticsTests/testCurrentPriorityNameAndStatus`
- `SemanticsTests/testOrdinaryHelpUsesExistingCallback`
- `SemanticsTests/testDisabledHelpDoesNotInvoke`
- `SemanticsTests/testOrdinarySetterAndAdjustmentShareValue`
- `SemanticsTests/testBoundsDoNotDuplicateChange`
- `SemanticsTests/testDisabledAdjustmentCannotChangeState`
- `SemanticsTests/testHintTracksCurrentAvailability`

Sources and negative controls remain controller-only; inject only the subject and approved condition material. No independent subject answer exists yet. Native model-policy units are not tests of generated SwiftUI semantics.

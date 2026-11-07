# tvOS preference-forwarding

Draft development case, independent review pending; not a holdout.

Units assert actual Binding writes and selection-policy ordering/callback counts. Real environment composition is compiled, not runtime-inspected. Accept equivalent state/Binding designs and semantic background styling; do not claim rendered contrast or actual environment propagation from policy tests.

Grade correctness, preservation, usefulness and unsupported certainty separately. No exact English strings, helper names or single layout oracle is required. Invented APIs, lost ordinary actions and stale cross-item callbacks are critical when established.

[Claims and source checks](../manifest.json); [source](../Sources/PreferenceSurface.swift).

- `StoreTests/testBindingWritesSameSnapshotConsumedByWrapper`
- `StoreTests/testSelectionUpdatesBeforeAnimationCallback`
- `StoreTests/testReducedMotionStillUpdatesFinalState`
- `StoreTests/testUnchangedSelectionDoesNotNotifyOrAnimate`
- `StoreTests/testBothSelectionDirectionsUseCurrentStatus`
- `StoreTests/testReentrantAnimationPreservesLatestState`
- `StoreTests/testReduceTransparencyPolicyChoosesOpaque`
- `StoreTests/testPreferenceChangeRestoresNormalPolicy`
- `StoreTests/testTitleEditDoesNotEraseSelection`

Do not inject rubric, mutants or first-failure history into the subject. Independent subject outputs are not run.

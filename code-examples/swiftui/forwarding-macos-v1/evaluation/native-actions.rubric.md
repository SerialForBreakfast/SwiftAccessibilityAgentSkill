# macOS native-actions

Draft development case, independent review pending; not a holdout.

Exercise actual native dispatch and retained custom-action handlers, not only a detached model helper. Test generation and native-control ownership separately; on AppKit detach old target/action. Accept alternatives meeting current-item and disabled contracts. Native metadata and direct dispatch do not establish shortcut discovery or delivered interaction.

Grade correctness, preservation, usefulness and unsupported certainty separately. No exact English strings, helper names or single layout oracle is required. Invented APIs, lost ordinary actions and stale cross-item callbacks are critical when established.

[Claims and source checks](../manifest.json); [source](../Sources/NativeSurface.swift).

- `ForwardingTests/testOrdinaryPrimaryUsesCurrentID`
- `ForwardingTests/testOrdinarySecondaryRemainsIndependent`
- `ForwardingTests/testShortcutUsesSameSecondaryPath`
- `ForwardingTests/testOldShortcutCannotReachNewItem`
- `ForwardingTests/testOldOrdinaryControlCannotReachReboundSurface`
- `ForwardingTests/testExternallyDisabledPrimaryRejectsCapturedAction`
- `ForwardingTests/testExternallyDisabledSecondaryRejectsShortcut`
- `ForwardingTests/testDisabledSnapshotRejectsBothCallbacks`
- `ForwardingTests/testStopInvalidatesCapturedAction`
- `ForwardingTests/testRepeatedConfigureDoesNotDuplicateNativeHandler`
- `ForwardingTests/testShortcutListDoesNotAccumulate`
- `ForwardingTests/testCallbackDoesNotRetainOwner`
- `ForwardingTests/testNativeSurfaceNotRetainedByOwner`
- `ForwardingTests/testPublicDismantleStopsNativeDispatch`

Do not inject rubric, mutants or first-failure history into the subject. Independent subject outputs are not run.

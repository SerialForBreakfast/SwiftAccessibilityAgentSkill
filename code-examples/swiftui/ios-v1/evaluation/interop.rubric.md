# iOS/SwiftUI interop

Draft development case; independent review pending; not baseline eligible or a holdout.

Implement the correct public representable/coordinator API for the target, with explicit current native metadata and callback ownership. Test the coordinator method actually called by update, native action dispatch and public dismantle entry. Do not infer automatic SwiftUI update propagation or generated semantics from direct coordinator calls. Accept alternative identity/generation and handler replacement designs.

Grade correctness, ordinary-behavior preservation, practical usefulness and unsupported certainty separately. Critical errors require concrete evidence: invented APIs, lost ordinary actions, stale cross-item dispatch, unsupported availability. Accept equivalent valid implementations and native no-change reasoning. Exact helper names and English sample strings are not required. Missing integration/context is ungradable, not automatically an answer failure.

[Source claims and checks](../manifest.json); [example](../Sources/Interop.swift). Guidelines: G-001, G-003, G-004, G-005, G-007, G-008, G-014.

Exact assertions:
- `InteropTests/testCoordinatorUpdatesCurrentNameAndEnabledState`
- `InteropTests/testCoordinatorReplacesOldCallback`
- `InteropTests/testNativeActionDispatchUsesCurrentHandlerOnce`
- `InteropTests/testOldNativeViewCannotDispatchAfterRebind`
- `InteropTests/testExternallyDisabledButtonRejectsCallback`
- `InteropTests/testDismantleRejectsRetainedAction`
- `InteropTests/testRetainedCallbackDoesNotRetainCoordinator`
- `InteropTests/testCoordinatorDoesNotRetainNativeView`
- `InteropTests/testUnownedNativeViewLifetimeAfterAutoreleasePool`
- `InteropTests/testPublicDismantleStopsCoordinator`

Sources and negative controls remain controller-only; inject only the subject and approved condition material. No independent subject answer exists yet. Native model-policy units are not tests of generated SwiftUI semantics.

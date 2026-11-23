# macOS/SwiftUI lifecycle

Draft development case; independent review pending; not baseline eligible or a holdout.

Compose sheet/onDismiss and AccessibilityFocusState without delays. State tests prove target-request lifecycle, not delivered focus or modal containment. Preserve controls and correct completion ordering. Accept equivalent generation/session and binding designs; do not require UIKit notification idioms in pure SwiftUI.

Grade correctness, ordinary-behavior preservation, practical usefulness and unsupported certainty separately. Critical errors require concrete evidence: invented APIs, lost ordinary actions, stale cross-item dispatch, unsupported availability. Accept equivalent valid implementations and native no-change reasoning. Exact helper names and English sample strings are not required. Missing integration/context is ungradable, not automatically an answer failure.

[Source claims and checks](../manifest.json); [example](../Sources/Lifecycle.swift). Guidelines: G-006, G-013.

Exact assertions:
- `LifecycleTests/testBeginRecordsEntryWithoutRestorationRequest`
- `LifecycleTests/testDismissResolvesCurrentOrigin`
- `LifecycleTests/testRemovedOriginUsesFallback`
- `LifecycleTests/testOldDismissalCannotConsumeNewSession`
- `LifecycleTests/testRepeatedDismissIsQuiet`
- `LifecycleTests/testCancellationUsesSameRestorationContract`
- `LifecycleTests/testReentrantRequestPreservesNewPresentation`
- `LifecycleTests/testEligibleListIsEvaluatedAtCompletion`

Installed callback: the units above pass the ticket to the model by hand, so they cannot show what the view's `onDismiss` reads. Revision 4 of the example captures its presentation's ticket (`onDismiss: { [ticket] in`). The hosted macOS check `evals/native-calibration/sheet-dismissal/answers/Hosted.swift` (`Hosted/testRetainedRegistrations`) delivers A's retained registration after B opens: late A must be quiet, the first B restores once and a repeated B is quiet. Revision 4 passed it as control `control-captured` (batch `sheet-extra-0suc98ey`, Xcode 27.0). Revision 3, which read the latest `@State` ticket when A fired, failed it (batch `sheet-answers-ea4h1pu_`). The host intercepts registration; it does not prove SwiftUI's own dismissal scheduling or delivered focus.

Sources and negative controls remain controller-only; inject only the subject and approved condition material. No independent subject answer exists yet. Native model-policy units are not tests of generated SwiftUI semantics.

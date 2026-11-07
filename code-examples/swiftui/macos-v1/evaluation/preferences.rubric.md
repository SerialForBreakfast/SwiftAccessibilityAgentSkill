# macOS/SwiftUI preferences

Draft development case; independent review pending; not baseline eligible or a holdout.

Use semantic fonts and real public environment/modifier APIs. Test the explicit preference policy, distinguishing it from real environment propagation or rendered scaling. Non-color text remains regardless of motion/transparency. Layout alternatives are accepted; no fixed numerical scale factor or mandatory axis pattern. TV-specific limitations stay explicit.

Grade correctness, ordinary-behavior preservation, practical usefulness and unsupported certainty separately. Critical errors require concrete evidence: invented APIs, lost ordinary actions, stale cross-item dispatch, unsupported availability. Accept equivalent valid implementations and native no-change reasoning. Exact helper names and English sample strings are not required. Missing integration/context is ungradable, not automatically an answer failure.

[Source claims and checks](../manifest.json); [example](../Sources/Preferences.swift). Guidelines: G-010, G-011, G-012.

Exact assertions:
- `PreferenceTests/testReducedMotionPolicyKeepsFinalStateIndependent`
- `PreferenceTests/testTransparencyPolicyPreservesNonColorText`
- `PreferenceTests/testLargeTextPolicyUsesVerticalComposition`
- `PreferenceTests/testNormalTextDoesNotForceVerticalComposition`
- `PreferenceTests/testDifferentiateFlagDoesNotRequireMotion`
- `PreferenceTests/testPreferencesAreIndependent`

Sources and negative controls remain controller-only; inject only the subject and approved condition material. No independent subject answer exists yet. Native model-policy units are not tests of generated SwiftUI semantics.

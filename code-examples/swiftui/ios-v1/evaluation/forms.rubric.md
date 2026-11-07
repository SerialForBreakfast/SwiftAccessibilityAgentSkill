# iOS/SwiftUI forms

Draft development case; independent review pending; not baseline eligible or a holdout.

Binding edits and direct input changes cannot apply stale validation results. Consume completion before external Save callback; support synchronous/reentrant delivery and weak lifetime. Error text and native controls are explicit. These are callback ownership units, not networking/scheduling or screen-reader error announcement tests.

Grade correctness, ordinary-behavior preservation, practical usefulness and unsupported certainty separately. Critical errors require concrete evidence: invented APIs, lost ordinary actions, stale cross-item dispatch, unsupported availability. Accept equivalent valid implementations and native no-change reasoning. Exact helper names and English sample strings are not required. Missing integration/context is ungradable, not automatically an answer failure.

[Source claims and checks](../manifest.json); [example](../Sources/FormsMedia.swift). Guidelines: G-003, G-014.

Exact assertions:
- `FormsMediaTests/testFormPreservesRawInputSnapshot`
- `FormsMediaTests/testEditBindingInvalidatesPendingReply`
- `FormsMediaTests/testOutOfOrderValidationCannotOverwriteLatest`
- `FormsMediaTests/testDuplicateSuccessDoesNotSaveTwice`
- `FormsMediaTests/testDirectEditRejectsOldSnapshot`
- `FormsMediaTests/testInvalidThenCorrectedFormRecovers`
- `FormsMediaTests/testEmptyValidationMessageIsUnavailableNotSuccess`
- `FormsMediaTests/testReentrantSaveOwnsNewRequest`
- `FormsMediaTests/testRetainedReplyDoesNotRetainForm`

Sources and negative controls remain controller-only; inject only the subject and approved condition material. No independent subject answer exists yet. Native model-policy units are not tests of generated SwiftUI semantics.

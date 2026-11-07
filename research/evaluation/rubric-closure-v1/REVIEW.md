# Operational rubric review

Controller-only author revision. Original subject files and rubrics remain unchanged.
These are grading specifications, not scored model answers or independent acceptance.

## ios-swiftui-semantics

Accepted alternatives:

- Leave correct native semantics alone with a bounded explanation.
- Request a concrete symptom before recommending a semantic override.

### Criterion 1

Does not invent a defect solely from missing overrides.

- Pass: Identifies a supplied defect, or explains that no override/change is justified by the supplied evidence.
- Gap: Treats absent custom label/role as proof the standard control is broken.
- Insufficient evidence: A concrete symptom or native-default evidence is absent; accept bounded no-change rather than inventing it.
- Review channels: answer-review, source-review.

### Criterion 2

Preserves native control and its existing state binding.

- Pass: Retains the native control, existing binding and ordinary behavior unless a demonstrated defect requires a change.
- Gap: Replaces working control/state wiring without a task-related reason.
- Insufficient evidence: Existing example can support only its tested binding/state behavior; actual submitted control wiring still requires review.
- Review channels: answer-review, subject-unit-if-available.

### Criterion 3

Distinguishes meaningful visible naming from implementation identifiers.

- Pass: Uses a user-facing contextual name where needed; distinguishes it from an automation identifier.
- Gap: Uses only an implementation ID as the meaningful name or unconditionally replaces adequate visible text.
- Insufficient evidence: Exact native naming defaults need applicable source support, not a guessed default.
- Review channels: answer-review, source-review.

Source/policy anchors: [PRD.md:53](../../../research/evaluation/failure-driven/PRD.md#L53), [PRD.md:52](../../../research/evaluation/failure-driven/PRD.md#L52), [g-001-labels-meaningful-names.md:11](../../../references/swiftui/guidelines/g-001-labels-meaningful-names.md#L11).

## ios-swiftui-state

Accepted alternatives:

- Cancel and invalidate previous requests plus guard current identity.
- Generation token with current-item identity and explicit optional clearing.

### Criterion 1

Clears obsolete optional metadata on the same instance.

- Pass: Repeated updates on the same instance explicitly replace or clear obsolete status/help/value overrides.
- Gap: Only clears in prepareForReuse or retains A’s optional metadata after B replaces it.
- Insufficient evidence: No same-instance transition is supplied; ask or limit the claim.
- Review channels: answer-review, subject-unit-if-available.

### Criterion 2

Checks current item plus request identity before accepting results.

- Pass: Accepts replies only for the current request and relevant item/input; handles same-item replacement when material.
- Gap: A late callback can change a different item or superseded request.
- Insufficient evidence: An item-only check cannot establish request-generation safety.
- Review channels: answer-review, subject-unit-if-available.

### Criterion 3

Preserves unrelated state and the ordinary Open action.

- Pass: Preserves the existing Open behavior and unrelated state/traits while updating owned fields.
- Gap: Removes Open, accumulates callbacks or clears unrelated state as a shortcut.
- Insufficient evidence: Fixture may use another action name; do not infer all application behavior.
- Review channels: answer-review, subject-unit-if-available.

Source/policy anchors: [PRD.md:51](../../../research/evaluation/failure-driven/PRD.md#L51), [PRD.md:57](../../../research/evaluation/failure-driven/PRD.md#L57), [g-003-values-stateful-controls.md:11](../../../references/swiftui/guidelines/g-003-values-stateful-controls.md#L11).

## ios-swiftui-actions

Accepted alternatives:

- A supported named accessibility action in addition to the ordinary button.
- Retain existing implementation if it already supplies the requested shortcut correctly.

### Criterion 1

Preserves independent visible ordinary actions.

- Pass: Keeps independently reachable ordinary controls while adding the requested shortcut.
- Gap: Deletes or hides ordinary actions solely because a shortcut was added.
- Insufficient evidence: Generated traversal is not proved by callback/configuration units.
- Review channels: answer-review, subject-unit-if-available.

### Criterion 2

Shortcut uses the current file and respects enabled state.

- Pass: Both relevant action paths target the current file and honor the stated enabled policy.
- Gap: Old action reaches a rebound file, or the disabled shortcut still acts.
- Insufficient evidence: Check the actual action owner and enabled policy; do not assume native dispatch fixes custom callbacks.
- Review channels: answer-review, subject-unit-if-available.

### Criterion 3

Repeated updates do not accumulate handlers or retain obsolete owners.

- Pass: Repeated setup replaces obsolete handlers and avoids duplicate calls or unintended ownership.
- Gap: Reconfiguration appends handlers or a stale callback retains an obsolete owner.
- Insufficient evidence: A leak claim needs an appropriate lifetime assertion; absence of weak spelling alone is not a defect.
- Review channels: answer-review, subject-unit-if-available.

Source/policy anchors: [PRD.md:52](../../../research/evaluation/failure-driven/PRD.md#L52), [PRD.md:60](../../../research/evaluation/failure-driven/PRD.md#L60), [g-007-accessibility-actions.md:11](../../../references/swiftui/guidelines/g-007-accessibility-actions.md#L11).

## ios-swiftui-structure

Accepted alternatives:

- Group descriptive fragments separately from independent controls.
- Keep meaningful existing structure and add only justified landmarks.

### Criterion 1

Does not merge away independent controls.

- Pass: Groups descriptive fragments without merging away the independent Open and Details tasks.
- Gap: A single merged element replaces independent required controls.
- Insufficient evidence: Configuration or compilation cannot establish the complete generated accessibility tree.
- Review channels: answer-review, source-review, subject-unit-if-available.

### Criterion 2

Keeps ordinary navigation and stable current item identity.

- Pass: Preserves ordinary task completion and uses stable current identity across reorder/removal; landmarks are meaningful.
- Gap: Rotor familiarity becomes required to complete tasks, or stale entries invoke removed/rebound content.
- Insufficient evidence: Ordinary traversal and rotor discoverability are source/answer-level claims, not inferred from search-block calls.
- Review channels: answer-review, subject-unit-if-available.

### Criterion 3

Does not claim generated tree or rotor discoverability from configuration-only units.

- Pass: Describes only configured children, direct search results or compiled modifiers as those observations.
- Gap: Claims actual generated traversal/discoverability was validated by a model/configuration unit alone.
- Insufficient evidence: If no interaction evidence exists, say what was and was not asserted; no mandatory UI/manual gate.
- Review channels: answer-review, source-review.

Source/policy anchors: [PRD.md:65](../../../research/evaluation/failure-driven/PRD.md#L65), [PRD.md:57](../../../research/evaluation/failure-driven/PRD.md#L57), [g-005-grouping-containment.md:11](../../../references/swiftui/guidelines/g-005-grouping-containment.md#L11).

## ios-swiftui-text

Accepted alternatives:

- Flexible multiline layout with target-appropriate scalable typography.
- A permanent vertical arrangement if justified by the supplied layout requirements.

### Criterion 1

Addresses scalable text and live integration as distinct concerns.

- Pass: Separates target-appropriate scalable font configuration, later updates and flexible layout; supplies integration when requested.
- Gap: Treats wrapping a fixed font or an initial font assignment alone as complete live scaling.
- Insufficient evidence: Policies/flags are narrower than live propagation; missing integration stays inconclusive.
- Review channels: answer-review, source-review, subject-unit-if-available.

### Criterion 2

Preserves Pay behavior and accepts valid layout alternatives.

- Pass: Preserves Pay identity, supplied styling/configuration and existing callback, accepting any justified flexible layout.
- Gap: Replaces Pay wiring/style unnecessarily or requires a particular stack/axis implementation to pass.
- Insufficient evidence: No source project is supplied: evaluate the declared preservation interface rather than inventing hidden payment logic.
- Review channels: answer-review, subject-unit-if-available.

### Criterion 3

Checks platform/OS availability rather than borrowing another target’s text behavior.

- Pass: Separates SDK, deployment target and runtime, and checks the platform availability of each proposed API.
- Gap: Applies iOS/macOS text behavior to tvOS or treats newer-SDK compilation as older-runtime support.
- Insufficient evidence: Do not invent availability boundaries when the applicable primary source/declaration is missing.
- Review channels: answer-review, source-review.

### Criterion 4

Does not equate wrapping or modifier compilation with rendered layout success.

- Pass: Limits unit conclusions to configured fonts, constraints and callbacks; accepts focused compile/unit verification.
- Gap: Calls wrapping, a policy flag or modifier construction proof of rendered layout success.
- Insufficient evidence: Rendered clipping and delivered interaction are outside these unit contracts; that does not block a bounded fix.
- Review channels: answer-review, source-review.

Source/policy anchors: [PRD.md:52](../../../research/evaluation/failure-driven/PRD.md#L52), [PRD.md:57](../../../research/evaluation/failure-driven/PRD.md#L57), [g-010-dynamic-type-layout-resilience.md:11](../../../references/swiftui/guidelines/g-010-dynamic-type-layout-resilience.md#L11).

## ios-swiftui-lifecycle

Accepted alternatives:

- Session token plus current-item lookup and a valid fallback.
- Explicit state machine with equivalent stale-completion and reentrancy handling.

### Criterion 1

Resolves a current valid anchor at completion time.

- Pass: Resolves current eligibility at completion and uses the declared valid fallback if the origin disappears.
- Gap: Uses only the captured opening index/object without revalidation after reorder/removal.
- Insufficient evidence: A focus request target is not evidence of delivered focus.
- Review channels: answer-review, subject-unit-if-available.

### Criterion 2

Rejects stale or duplicate completion and consumes ownership before external callbacks.

- Pass: Rejects old/duplicate completion and consumes request ownership before external code can reenter.
- Gap: An old completion closes a new panel, fires twice or erases a reentrant new request.
- Insufficient evidence: Review state-transition ordering, not just the presence of a token.
- Review channels: answer-review, subject-unit-if-available.

### Criterion 3

Distinguishes requesting restoration from proving delivered focus.

- Pass: Calls the result a restoration request/state change unless stronger evidence actually exists.
- Gap: States VoiceOver focus delivery was proved by an injected request callback.
- Insufficient evidence: No manual/UI testing prerequisite is added to the fix.
- Review channels: answer-review, source-review.

Source/policy anchors: [PRD.md:57](../../../research/evaluation/failure-driven/PRD.md#L57), [PRD.md:52](../../../research/evaluation/failure-driven/PRD.md#L52), [g-013-modal-sheet-focus-containment.md:11](../../../references/swiftui/guidelines/g-013-modal-sheet-focus-containment.md#L11).

## ios-swiftui-media

Accepted alternatives:

- Explicit loading/result state with identity-guarded completion.
- Equivalent typed result model preserving selection and unavailable evidence.

### Criterion 1

Keeps loading, empty/missing, error and positive metadata distinct.

- Pass: Models loading, no current item, successfully absent metadata, positive metadata and errors distinctly where relevant.
- Gap: Converts an error or unfinished load into proof no description/subtitles exist.
- Insufficient evidence: A synthetic option list does not establish native metadata extraction.
- Review channels: answer-review, subject-unit-if-available.

### Criterion 2

Rejects results for an obsolete player item/request.

- Pass: Rejects a completion when request generation or actual current item no longer matches.
- Gap: An old item/request overwrites newer metadata, including external player replacement.
- Insufficient evidence: An injected owner test proves its policy, not all asset/network timing.
- Review channels: answer-review, subject-unit-if-available.

### Criterion 3

Does not change selected media options as a side effect of inspection.

- Pass: Metadata inspection leaves actual selected audio/subtitle options unchanged unless explicitly requested.
- Gap: Inspection silently selects/clears a track; or mute/volume preservation is claimed as selected-option evidence.
- Insufficient evidence: A mute/volume-only fixture is partial evidence, not selected-media validation.
- Review channels: answer-review, subject-unit-if-available.

### Criterion 4

Does not infer spoken description quality or complete caption support from a metadata flag.

- Pass: Reports an audio-description/forced-caption flag as metadata, with conclusions limited to the available source.
- Gap: Infers description quality, complete captions or accessibility of all content from one tag.
- Insufficient evidence: Tagged silent assets and metadata bits do not measure spoken-content quality.
- Review channels: answer-review, source-review.

Source/policy anchors: [PRD.md:57](../../../research/evaluation/failure-driven/PRD.md#L57), [PRD.md:52](../../../research/evaluation/failure-driven/PRD.md#L52), [g-015-media-captions-audio-descriptions.md:11](../../../references/swiftui/guidelines/g-015-media-captions-audio-descriptions.md#L11).

## ios-swiftui-testing

Accepted alternatives:

- Compile real modifier/native compositions and test public state/action dispatch.
- Explicitly record unsupported semantic observations rather than inventing a test oracle.

### Criterion 1

Limits conclusions to actual assertions and compilation.

- Pass: Maps each claim to the actual compile/unit assertion and distinguishes application state from generated semantics.
- Gap: Claims speech, focus delivery or rotor discoverability from compilation or a detached model test.
- Insufficient evidence: No results means proposed checks, not executed validation.
- Review channels: answer-review, source-review.

### Criterion 2

Keeps exact first failures separate from repairs and deliberate mutants.

- Pass: Preserves first source, diagnostics and environment separately from repairs, oracle errors and deliberate mutants.
- Gap: Overwrites the first failure or counts build/infrastructure failure as intended assertion rejection.
- Insufficient evidence: Missing history is marked unavailable rather than reconstructed as an exact transcript.
- Review channels: answer-review, source-review.

### Criterion 3

Checks imported API names and availability on the real selected target.

- Pass: Checks actual Swift imports/annotations and records SDK, deployment and actual runtime separately.
- Gap: Guesses a Swift member spelling or derives a runtime version from a deployment target.
- Insufficient evidence: Unknown annotations or absent runtime results remain explicit.
- Review channels: answer-review, source-review.

### Criterion 4

Does not add mandatory manual verification or UI tests.

- Pass: Uses compile/unit checks only for this request and does not make manual/UI verification a release prerequisite.
- Gap: Requires UI automation or mandatory manual accessibility verification before providing the requested bounded fix.
- Insufficient evidence: Optional broader research is separate and does not become an acceptance dependency.
- Review channels: answer-review, source-review.

Source/policy anchors: [PRD.md:56](../../../research/evaluation/failure-driven/PRD.md#L56), [PRD.md:65](../../../research/evaluation/failure-driven/PRD.md#L65), [g-014-lists-forms-complex-rows.md:11](../../../references/swiftui/guidelines/g-014-lists-forms-complex-rows.md#L11), [PRD.md:54](../../../research/evaluation/failure-driven/PRD.md#L54).

## macos-swiftui-semantics

Accepted alternatives:

- Leave correct native semantics alone with a bounded explanation.
- Request a concrete symptom before recommending a semantic override.

### Criterion 1

Does not invent a defect solely from missing overrides.

- Pass: Identifies a supplied defect, or explains that no override/change is justified by the supplied evidence.
- Gap: Treats absent custom label/role as proof the standard control is broken.
- Insufficient evidence: A concrete symptom or native-default evidence is absent; accept bounded no-change rather than inventing it.
- Review channels: answer-review, source-review.

### Criterion 2

Preserves native control and its existing state binding.

- Pass: Retains the native control, existing binding and ordinary behavior unless a demonstrated defect requires a change.
- Gap: Replaces working control/state wiring without a task-related reason.
- Insufficient evidence: Existing example can support only its tested binding/state behavior; actual submitted control wiring still requires review.
- Review channels: answer-review, subject-unit-if-available.

### Criterion 3

Distinguishes meaningful visible naming from implementation identifiers.

- Pass: Uses a user-facing contextual name where needed; distinguishes it from an automation identifier.
- Gap: Uses only an implementation ID as the meaningful name or unconditionally replaces adequate visible text.
- Insufficient evidence: Exact native naming defaults need applicable source support, not a guessed default.
- Review channels: answer-review, source-review.

Source/policy anchors: [PRD.md:53](../../../research/evaluation/failure-driven/PRD.md#L53), [PRD.md:52](../../../research/evaluation/failure-driven/PRD.md#L52), [g-001-labels-meaningful-names.md:11](../../../references/swiftui/guidelines/g-001-labels-meaningful-names.md#L11).

## macos-swiftui-state

Accepted alternatives:

- Cancel and invalidate previous requests plus guard current identity.
- Generation token with current-item identity and explicit optional clearing.

### Criterion 1

Clears obsolete optional metadata on the same instance.

- Pass: Repeated updates on the same instance explicitly replace or clear obsolete status/help/value overrides.
- Gap: Only clears in prepareForReuse or retains A’s optional metadata after B replaces it.
- Insufficient evidence: No same-instance transition is supplied; ask or limit the claim.
- Review channels: answer-review, subject-unit-if-available.

### Criterion 2

Checks current item plus request identity before accepting results.

- Pass: Accepts replies only for the current request and relevant item/input; handles same-item replacement when material.
- Gap: A late callback can change a different item or superseded request.
- Insufficient evidence: An item-only check cannot establish request-generation safety.
- Review channels: answer-review, subject-unit-if-available.

### Criterion 3

Preserves unrelated state and the ordinary Open action.

- Pass: Preserves the existing Open behavior and unrelated state/traits while updating owned fields.
- Gap: Removes Open, accumulates callbacks or clears unrelated state as a shortcut.
- Insufficient evidence: Fixture may use another action name; do not infer all application behavior.
- Review channels: answer-review, subject-unit-if-available.

Source/policy anchors: [PRD.md:51](../../../research/evaluation/failure-driven/PRD.md#L51), [PRD.md:57](../../../research/evaluation/failure-driven/PRD.md#L57), [g-003-values-stateful-controls.md:11](../../../references/swiftui/guidelines/g-003-values-stateful-controls.md#L11).

## macos-swiftui-actions

Accepted alternatives:

- A supported named accessibility action in addition to the ordinary button.
- Retain existing implementation if it already supplies the requested shortcut correctly.

### Criterion 1

Preserves independent visible ordinary actions.

- Pass: Keeps independently reachable ordinary controls while adding the requested shortcut.
- Gap: Deletes or hides ordinary actions solely because a shortcut was added.
- Insufficient evidence: Generated traversal is not proved by callback/configuration units.
- Review channels: answer-review, subject-unit-if-available.

### Criterion 2

Shortcut uses the current file and respects enabled state.

- Pass: Both relevant action paths target the current file and honor the stated enabled policy.
- Gap: Old action reaches a rebound file, or the disabled shortcut still acts.
- Insufficient evidence: Check the actual action owner and enabled policy; do not assume native dispatch fixes custom callbacks.
- Review channels: answer-review, subject-unit-if-available.

### Criterion 3

Repeated updates do not accumulate handlers or retain obsolete owners.

- Pass: Repeated setup replaces obsolete handlers and avoids duplicate calls or unintended ownership.
- Gap: Reconfiguration appends handlers or a stale callback retains an obsolete owner.
- Insufficient evidence: A leak claim needs an appropriate lifetime assertion; absence of weak spelling alone is not a defect.
- Review channels: answer-review, subject-unit-if-available.

Source/policy anchors: [PRD.md:52](../../../research/evaluation/failure-driven/PRD.md#L52), [PRD.md:60](../../../research/evaluation/failure-driven/PRD.md#L60), [g-007-accessibility-actions.md:11](../../../references/swiftui/guidelines/g-007-accessibility-actions.md#L11).

## macos-swiftui-structure

Accepted alternatives:

- Group descriptive fragments separately from independent controls.
- Keep meaningful existing structure and add only justified landmarks.

### Criterion 1

Does not merge away independent controls.

- Pass: Groups descriptive fragments without merging away the independent Open and Details tasks.
- Gap: A single merged element replaces independent required controls.
- Insufficient evidence: Configuration or compilation cannot establish the complete generated accessibility tree.
- Review channels: answer-review, source-review, subject-unit-if-available.

### Criterion 2

Keeps ordinary navigation and stable current item identity.

- Pass: Preserves ordinary task completion and uses stable current identity across reorder/removal; landmarks are meaningful.
- Gap: Rotor familiarity becomes required to complete tasks, or stale entries invoke removed/rebound content.
- Insufficient evidence: Ordinary traversal and rotor discoverability are source/answer-level claims, not inferred from search-block calls.
- Review channels: answer-review, subject-unit-if-available.

### Criterion 3

Does not claim generated tree or rotor discoverability from configuration-only units.

- Pass: Describes only configured children, direct search results or compiled modifiers as those observations.
- Gap: Claims actual generated traversal/discoverability was validated by a model/configuration unit alone.
- Insufficient evidence: If no interaction evidence exists, say what was and was not asserted; no mandatory UI/manual gate.
- Review channels: answer-review, source-review.

Source/policy anchors: [PRD.md:65](../../../research/evaluation/failure-driven/PRD.md#L65), [PRD.md:57](../../../research/evaluation/failure-driven/PRD.md#L57), [g-005-grouping-containment.md:11](../../../references/swiftui/guidelines/g-005-grouping-containment.md#L11).

## macos-swiftui-text

Accepted alternatives:

- Flexible multiline layout with target-appropriate scalable typography.
- A permanent vertical arrangement if justified by the supplied layout requirements.

### Criterion 1

Addresses scalable text and live integration as distinct concerns.

- Pass: Separates target-appropriate scalable font configuration, later updates and flexible layout; supplies integration when requested.
- Gap: Treats wrapping a fixed font or an initial font assignment alone as complete live scaling.
- Insufficient evidence: Policies/flags are narrower than live propagation; missing integration stays inconclusive.
- Review channels: answer-review, source-review, subject-unit-if-available.

### Criterion 2

Preserves Pay behavior and accepts valid layout alternatives.

- Pass: Preserves Pay identity, supplied styling/configuration and existing callback, accepting any justified flexible layout.
- Gap: Replaces Pay wiring/style unnecessarily or requires a particular stack/axis implementation to pass.
- Insufficient evidence: No source project is supplied: evaluate the declared preservation interface rather than inventing hidden payment logic.
- Review channels: answer-review, subject-unit-if-available.

### Criterion 3

Checks platform/OS availability rather than borrowing another target’s text behavior.

- Pass: Separates SDK, deployment target and runtime, and checks the platform availability of each proposed API.
- Gap: Applies iOS/macOS text behavior to tvOS or treats newer-SDK compilation as older-runtime support.
- Insufficient evidence: Do not invent availability boundaries when the applicable primary source/declaration is missing.
- Review channels: answer-review, source-review.

### Criterion 4

Does not equate wrapping or modifier compilation with rendered layout success.

- Pass: Limits unit conclusions to configured fonts, constraints and callbacks; accepts focused compile/unit verification.
- Gap: Calls wrapping, a policy flag or modifier construction proof of rendered layout success.
- Insufficient evidence: Rendered clipping and delivered interaction are outside these unit contracts; that does not block a bounded fix.
- Review channels: answer-review, source-review.

Source/policy anchors: [PRD.md:52](../../../research/evaluation/failure-driven/PRD.md#L52), [PRD.md:57](../../../research/evaluation/failure-driven/PRD.md#L57), [g-010-dynamic-type-layout-resilience.md:11](../../../references/swiftui/guidelines/g-010-dynamic-type-layout-resilience.md#L11).

## macos-swiftui-lifecycle

Accepted alternatives:

- Session token plus current-item lookup and a valid fallback.
- Explicit state machine with equivalent stale-completion and reentrancy handling.

### Criterion 1

Resolves a current valid anchor at completion time.

- Pass: Resolves current eligibility at completion and uses the declared valid fallback if the origin disappears.
- Gap: Uses only the captured opening index/object without revalidation after reorder/removal.
- Insufficient evidence: A focus request target is not evidence of delivered focus.
- Review channels: answer-review, subject-unit-if-available.

### Criterion 2

Rejects stale or duplicate completion and consumes ownership before external callbacks.

- Pass: Rejects old/duplicate completion and consumes request ownership before external code can reenter.
- Gap: An old completion closes a new panel, fires twice or erases a reentrant new request.
- Insufficient evidence: Review state-transition ordering, not just the presence of a token.
- Review channels: answer-review, subject-unit-if-available.

### Criterion 3

Distinguishes requesting restoration from proving delivered focus.

- Pass: Calls the result a restoration request/state change unless stronger evidence actually exists.
- Gap: States VoiceOver focus delivery was proved by an injected request callback.
- Insufficient evidence: No manual/UI testing prerequisite is added to the fix.
- Review channels: answer-review, source-review.

Source/policy anchors: [PRD.md:57](../../../research/evaluation/failure-driven/PRD.md#L57), [PRD.md:52](../../../research/evaluation/failure-driven/PRD.md#L52), [g-013-modal-sheet-focus-containment.md:11](../../../references/swiftui/guidelines/g-013-modal-sheet-focus-containment.md#L11).

## macos-swiftui-media

Accepted alternatives:

- Explicit loading/result state with identity-guarded completion.
- Equivalent typed result model preserving selection and unavailable evidence.

### Criterion 1

Keeps loading, empty/missing, error and positive metadata distinct.

- Pass: Models loading, no current item, successfully absent metadata, positive metadata and errors distinctly where relevant.
- Gap: Converts an error or unfinished load into proof no description/subtitles exist.
- Insufficient evidence: A synthetic option list does not establish native metadata extraction.
- Review channels: answer-review, subject-unit-if-available.

### Criterion 2

Rejects results for an obsolete player item/request.

- Pass: Rejects a completion when request generation or actual current item no longer matches.
- Gap: An old item/request overwrites newer metadata, including external player replacement.
- Insufficient evidence: An injected owner test proves its policy, not all asset/network timing.
- Review channels: answer-review, subject-unit-if-available.

### Criterion 3

Does not change selected media options as a side effect of inspection.

- Pass: Metadata inspection leaves actual selected audio/subtitle options unchanged unless explicitly requested.
- Gap: Inspection silently selects/clears a track; or mute/volume preservation is claimed as selected-option evidence.
- Insufficient evidence: A mute/volume-only fixture is partial evidence, not selected-media validation.
- Review channels: answer-review, subject-unit-if-available.

### Criterion 4

Does not infer spoken description quality or complete caption support from a metadata flag.

- Pass: Reports an audio-description/forced-caption flag as metadata, with conclusions limited to the available source.
- Gap: Infers description quality, complete captions or accessibility of all content from one tag.
- Insufficient evidence: Tagged silent assets and metadata bits do not measure spoken-content quality.
- Review channels: answer-review, source-review.

Source/policy anchors: [PRD.md:57](../../../research/evaluation/failure-driven/PRD.md#L57), [PRD.md:52](../../../research/evaluation/failure-driven/PRD.md#L52), [g-015-media-captions-audio-descriptions.md:11](../../../references/swiftui/guidelines/g-015-media-captions-audio-descriptions.md#L11).

## macos-swiftui-testing

Accepted alternatives:

- Compile real modifier/native compositions and test public state/action dispatch.
- Explicitly record unsupported semantic observations rather than inventing a test oracle.

### Criterion 1

Limits conclusions to actual assertions and compilation.

- Pass: Maps each claim to the actual compile/unit assertion and distinguishes application state from generated semantics.
- Gap: Claims speech, focus delivery or rotor discoverability from compilation or a detached model test.
- Insufficient evidence: No results means proposed checks, not executed validation.
- Review channels: answer-review, source-review.

### Criterion 2

Keeps exact first failures separate from repairs and deliberate mutants.

- Pass: Preserves first source, diagnostics and environment separately from repairs, oracle errors and deliberate mutants.
- Gap: Overwrites the first failure or counts build/infrastructure failure as intended assertion rejection.
- Insufficient evidence: Missing history is marked unavailable rather than reconstructed as an exact transcript.
- Review channels: answer-review, source-review.

### Criterion 3

Checks imported API names and availability on the real selected target.

- Pass: Checks actual Swift imports/annotations and records SDK, deployment and actual runtime separately.
- Gap: Guesses a Swift member spelling or derives a runtime version from a deployment target.
- Insufficient evidence: Unknown annotations or absent runtime results remain explicit.
- Review channels: answer-review, source-review.

### Criterion 4

Does not add mandatory manual verification or UI tests.

- Pass: Uses compile/unit checks only for this request and does not make manual/UI verification a release prerequisite.
- Gap: Requires UI automation or mandatory manual accessibility verification before providing the requested bounded fix.
- Insufficient evidence: Optional broader research is separate and does not become an acceptance dependency.
- Review channels: answer-review, source-review.

Source/policy anchors: [PRD.md:56](../../../research/evaluation/failure-driven/PRD.md#L56), [PRD.md:65](../../../research/evaluation/failure-driven/PRD.md#L65), [g-014-lists-forms-complex-rows.md:11](../../../references/swiftui/guidelines/g-014-lists-forms-complex-rows.md#L11), [PRD.md:54](../../../research/evaluation/failure-driven/PRD.md#L54).

## tvos-swiftui-semantics

Accepted alternatives:

- Leave correct native semantics alone with a bounded explanation.
- Request a concrete symptom before recommending a semantic override.

### Criterion 1

Does not invent a defect solely from missing overrides.

- Pass: Identifies a supplied defect, or explains that no override/change is justified by the supplied evidence.
- Gap: Treats absent custom label/role as proof the standard control is broken.
- Insufficient evidence: A concrete symptom or native-default evidence is absent; accept bounded no-change rather than inventing it.
- Review channels: answer-review, source-review.

### Criterion 2

Preserves native control and its existing state binding.

- Pass: Retains the native control, existing binding and ordinary behavior unless a demonstrated defect requires a change.
- Gap: Replaces working control/state wiring without a task-related reason.
- Insufficient evidence: Existing example can support only its tested binding/state behavior; actual submitted control wiring still requires review.
- Review channels: answer-review, subject-unit-if-available.

### Criterion 3

Distinguishes meaningful visible naming from implementation identifiers.

- Pass: Uses a user-facing contextual name where needed; distinguishes it from an automation identifier.
- Gap: Uses only an implementation ID as the meaningful name or unconditionally replaces adequate visible text.
- Insufficient evidence: Exact native naming defaults need applicable source support, not a guessed default.
- Review channels: answer-review, source-review.

Source/policy anchors: [PRD.md:53](../../../research/evaluation/failure-driven/PRD.md#L53), [PRD.md:52](../../../research/evaluation/failure-driven/PRD.md#L52), [g-001-labels-meaningful-names.md:11](../../../references/swiftui/guidelines/g-001-labels-meaningful-names.md#L11).

## tvos-swiftui-state

Accepted alternatives:

- Cancel and invalidate previous requests plus guard current identity.
- Generation token with current-item identity and explicit optional clearing.

### Criterion 1

Clears obsolete optional metadata on the same instance.

- Pass: Repeated updates on the same instance explicitly replace or clear obsolete status/help/value overrides.
- Gap: Only clears in prepareForReuse or retains A’s optional metadata after B replaces it.
- Insufficient evidence: No same-instance transition is supplied; ask or limit the claim.
- Review channels: answer-review, subject-unit-if-available.

### Criterion 2

Checks current item plus request identity before accepting results.

- Pass: Accepts replies only for the current request and relevant item/input; handles same-item replacement when material.
- Gap: A late callback can change a different item or superseded request.
- Insufficient evidence: An item-only check cannot establish request-generation safety.
- Review channels: answer-review, subject-unit-if-available.

### Criterion 3

Preserves unrelated state and the ordinary Open action.

- Pass: Preserves the existing Open behavior and unrelated state/traits while updating owned fields.
- Gap: Removes Open, accumulates callbacks or clears unrelated state as a shortcut.
- Insufficient evidence: Fixture may use another action name; do not infer all application behavior.
- Review channels: answer-review, subject-unit-if-available.

Source/policy anchors: [PRD.md:51](../../../research/evaluation/failure-driven/PRD.md#L51), [PRD.md:57](../../../research/evaluation/failure-driven/PRD.md#L57), [g-003-values-stateful-controls.md:11](../../../references/swiftui/guidelines/g-003-values-stateful-controls.md#L11).

## tvos-swiftui-actions

Accepted alternatives:

- A supported named accessibility action in addition to the ordinary button.
- Retain existing implementation if it already supplies the requested shortcut correctly.

### Criterion 1

Preserves independent visible ordinary actions.

- Pass: Keeps independently reachable ordinary controls while adding the requested shortcut.
- Gap: Deletes or hides ordinary actions solely because a shortcut was added.
- Insufficient evidence: Generated traversal is not proved by callback/configuration units.
- Review channels: answer-review, subject-unit-if-available.

### Criterion 2

Shortcut uses the current file and respects enabled state.

- Pass: Both relevant action paths target the current file and honor the stated enabled policy.
- Gap: Old action reaches a rebound file, or the disabled shortcut still acts.
- Insufficient evidence: Check the actual action owner and enabled policy; do not assume native dispatch fixes custom callbacks.
- Review channels: answer-review, subject-unit-if-available.

### Criterion 3

Repeated updates do not accumulate handlers or retain obsolete owners.

- Pass: Repeated setup replaces obsolete handlers and avoids duplicate calls or unintended ownership.
- Gap: Reconfiguration appends handlers or a stale callback retains an obsolete owner.
- Insufficient evidence: A leak claim needs an appropriate lifetime assertion; absence of weak spelling alone is not a defect.
- Review channels: answer-review, subject-unit-if-available.

Source/policy anchors: [PRD.md:52](../../../research/evaluation/failure-driven/PRD.md#L52), [PRD.md:60](../../../research/evaluation/failure-driven/PRD.md#L60), [g-007-accessibility-actions.md:11](../../../references/swiftui/guidelines/g-007-accessibility-actions.md#L11).

## tvos-swiftui-structure

Accepted alternatives:

- Group descriptive fragments separately from independent controls.
- Keep meaningful existing structure and add only justified landmarks.

### Criterion 1

Does not merge away independent controls.

- Pass: Groups descriptive fragments without merging away the independent Open and Details tasks.
- Gap: A single merged element replaces independent required controls.
- Insufficient evidence: Configuration or compilation cannot establish the complete generated accessibility tree.
- Review channels: answer-review, source-review, subject-unit-if-available.

### Criterion 2

Keeps ordinary navigation and stable current item identity.

- Pass: Preserves ordinary task completion and uses stable current identity across reorder/removal; landmarks are meaningful.
- Gap: Rotor familiarity becomes required to complete tasks, or stale entries invoke removed/rebound content.
- Insufficient evidence: Ordinary traversal and rotor discoverability are source/answer-level claims, not inferred from search-block calls.
- Review channels: answer-review, subject-unit-if-available.

### Criterion 3

Does not claim generated tree or rotor discoverability from configuration-only units.

- Pass: Describes only configured children, direct search results or compiled modifiers as those observations.
- Gap: Claims actual generated traversal/discoverability was validated by a model/configuration unit alone.
- Insufficient evidence: If no interaction evidence exists, say what was and was not asserted; no mandatory UI/manual gate.
- Review channels: answer-review, source-review.

Source/policy anchors: [PRD.md:65](../../../research/evaluation/failure-driven/PRD.md#L65), [PRD.md:57](../../../research/evaluation/failure-driven/PRD.md#L57), [g-005-grouping-containment.md:11](../../../references/swiftui/guidelines/g-005-grouping-containment.md#L11).

## tvos-swiftui-text

Accepted alternatives:

- Flexible multiline layout with target-appropriate scalable typography.
- A permanent vertical arrangement if justified by the supplied layout requirements.

### Criterion 1

Addresses scalable text and live integration as distinct concerns.

- Pass: Separates target-appropriate scalable font configuration, later updates and flexible layout; supplies integration when requested.
- Gap: Treats wrapping a fixed font or an initial font assignment alone as complete live scaling.
- Insufficient evidence: Policies/flags are narrower than live propagation; missing integration stays inconclusive.
- Review channels: answer-review, source-review, subject-unit-if-available.

### Criterion 2

Preserves Pay behavior and accepts valid layout alternatives.

- Pass: Preserves Pay identity, supplied styling/configuration and existing callback, accepting any justified flexible layout.
- Gap: Replaces Pay wiring/style unnecessarily or requires a particular stack/axis implementation to pass.
- Insufficient evidence: No source project is supplied: evaluate the declared preservation interface rather than inventing hidden payment logic.
- Review channels: answer-review, subject-unit-if-available.

### Criterion 3

Checks platform/OS availability rather than borrowing another target’s text behavior.

- Pass: Separates SDK, deployment target and runtime, and checks the platform availability of each proposed API.
- Gap: Applies iOS/macOS text behavior to tvOS or treats newer-SDK compilation as older-runtime support.
- Insufficient evidence: Do not invent availability boundaries when the applicable primary source/declaration is missing.
- Review channels: answer-review, source-review.

### Criterion 4

Does not equate wrapping or modifier compilation with rendered layout success.

- Pass: Limits unit conclusions to configured fonts, constraints and callbacks; accepts focused compile/unit verification.
- Gap: Calls wrapping, a policy flag or modifier construction proof of rendered layout success.
- Insufficient evidence: Rendered clipping and delivered interaction are outside these unit contracts; that does not block a bounded fix.
- Review channels: answer-review, source-review.

Source/policy anchors: [PRD.md:52](../../../research/evaluation/failure-driven/PRD.md#L52), [PRD.md:57](../../../research/evaluation/failure-driven/PRD.md#L57), [g-010-dynamic-type-layout-resilience.md:11](../../../references/swiftui/guidelines/g-010-dynamic-type-layout-resilience.md#L11).

## tvos-swiftui-lifecycle

Accepted alternatives:

- Session token plus current-item lookup and a valid fallback.
- Explicit state machine with equivalent stale-completion and reentrancy handling.

### Criterion 1

Resolves a current valid anchor at completion time.

- Pass: Resolves current eligibility at completion and uses the declared valid fallback if the origin disappears.
- Gap: Uses only the captured opening index/object without revalidation after reorder/removal.
- Insufficient evidence: A focus request target is not evidence of delivered focus.
- Review channels: answer-review, subject-unit-if-available.

### Criterion 2

Rejects stale or duplicate completion and consumes ownership before external callbacks.

- Pass: Rejects old/duplicate completion and consumes request ownership before external code can reenter.
- Gap: An old completion closes a new panel, fires twice or erases a reentrant new request.
- Insufficient evidence: Review state-transition ordering, not just the presence of a token.
- Review channels: answer-review, subject-unit-if-available.

### Criterion 3

Distinguishes requesting restoration from proving delivered focus.

- Pass: Calls the result a restoration request/state change unless stronger evidence actually exists.
- Gap: States VoiceOver focus delivery was proved by an injected request callback.
- Insufficient evidence: No manual/UI testing prerequisite is added to the fix.
- Review channels: answer-review, source-review.

Source/policy anchors: [PRD.md:57](../../../research/evaluation/failure-driven/PRD.md#L57), [PRD.md:52](../../../research/evaluation/failure-driven/PRD.md#L52), [g-013-modal-sheet-focus-containment.md:11](../../../references/swiftui/guidelines/g-013-modal-sheet-focus-containment.md#L11).

## tvos-swiftui-media

Accepted alternatives:

- Explicit loading/result state with identity-guarded completion.
- Equivalent typed result model preserving selection and unavailable evidence.

### Criterion 1

Keeps loading, empty/missing, error and positive metadata distinct.

- Pass: Models loading, no current item, successfully absent metadata, positive metadata and errors distinctly where relevant.
- Gap: Converts an error or unfinished load into proof no description/subtitles exist.
- Insufficient evidence: A synthetic option list does not establish native metadata extraction.
- Review channels: answer-review, subject-unit-if-available.

### Criterion 2

Rejects results for an obsolete player item/request.

- Pass: Rejects a completion when request generation or actual current item no longer matches.
- Gap: An old item/request overwrites newer metadata, including external player replacement.
- Insufficient evidence: An injected owner test proves its policy, not all asset/network timing.
- Review channels: answer-review, subject-unit-if-available.

### Criterion 3

Does not change selected media options as a side effect of inspection.

- Pass: Metadata inspection leaves actual selected audio/subtitle options unchanged unless explicitly requested.
- Gap: Inspection silently selects/clears a track; or mute/volume preservation is claimed as selected-option evidence.
- Insufficient evidence: A mute/volume-only fixture is partial evidence, not selected-media validation.
- Review channels: answer-review, subject-unit-if-available.

### Criterion 4

Does not infer spoken description quality or complete caption support from a metadata flag.

- Pass: Reports an audio-description/forced-caption flag as metadata, with conclusions limited to the available source.
- Gap: Infers description quality, complete captions or accessibility of all content from one tag.
- Insufficient evidence: Tagged silent assets and metadata bits do not measure spoken-content quality.
- Review channels: answer-review, source-review.

Source/policy anchors: [PRD.md:57](../../../research/evaluation/failure-driven/PRD.md#L57), [PRD.md:52](../../../research/evaluation/failure-driven/PRD.md#L52), [g-015-media-captions-audio-descriptions.md:11](../../../references/swiftui/guidelines/g-015-media-captions-audio-descriptions.md#L11).

## tvos-swiftui-testing

Accepted alternatives:

- Compile real modifier/native compositions and test public state/action dispatch.
- Explicitly record unsupported semantic observations rather than inventing a test oracle.

### Criterion 1

Limits conclusions to actual assertions and compilation.

- Pass: Maps each claim to the actual compile/unit assertion and distinguishes application state from generated semantics.
- Gap: Claims speech, focus delivery or rotor discoverability from compilation or a detached model test.
- Insufficient evidence: No results means proposed checks, not executed validation.
- Review channels: answer-review, source-review.

### Criterion 2

Keeps exact first failures separate from repairs and deliberate mutants.

- Pass: Preserves first source, diagnostics and environment separately from repairs, oracle errors and deliberate mutants.
- Gap: Overwrites the first failure or counts build/infrastructure failure as intended assertion rejection.
- Insufficient evidence: Missing history is marked unavailable rather than reconstructed as an exact transcript.
- Review channels: answer-review, source-review.

### Criterion 3

Checks imported API names and availability on the real selected target.

- Pass: Checks actual Swift imports/annotations and records SDK, deployment and actual runtime separately.
- Gap: Guesses a Swift member spelling or derives a runtime version from a deployment target.
- Insufficient evidence: Unknown annotations or absent runtime results remain explicit.
- Review channels: answer-review, source-review.

### Criterion 4

Does not add mandatory manual verification or UI tests.

- Pass: Uses compile/unit checks only for this request and does not make manual/UI verification a release prerequisite.
- Gap: Requires UI automation or mandatory manual accessibility verification before providing the requested bounded fix.
- Insufficient evidence: Optional broader research is separate and does not become an acceptance dependency.
- Review channels: answer-review, source-review.

Source/policy anchors: [PRD.md:56](../../../research/evaluation/failure-driven/PRD.md#L56), [PRD.md:65](../../../research/evaluation/failure-driven/PRD.md#L65), [g-014-lists-forms-complex-rows.md:11](../../../references/swiftui/guidelines/g-014-lists-forms-complex-rows.md#L11), [PRD.md:54](../../../research/evaluation/failure-driven/PRD.md#L54).

## ios-uikit-semantics

Accepted alternatives:

- Leave correct native semantics alone with a bounded explanation.
- Request a concrete symptom before recommending a semantic override.

### Criterion 1

Does not invent a defect solely from missing overrides.

- Pass: Identifies a supplied defect, or explains that no override/change is justified by the supplied evidence.
- Gap: Treats absent custom label/role as proof the standard control is broken.
- Insufficient evidence: A concrete symptom or native-default evidence is absent; accept bounded no-change rather than inventing it.
- Review channels: answer-review, source-review.

### Criterion 2

Preserves native control and its existing state binding.

- Pass: Retains the native control, existing binding and ordinary behavior unless a demonstrated defect requires a change.
- Gap: Replaces working control/state wiring without a task-related reason.
- Insufficient evidence: Existing example can support only its tested binding/state behavior; actual submitted control wiring still requires review.
- Review channels: answer-review, subject-unit-if-available.

### Criterion 3

Distinguishes meaningful visible naming from implementation identifiers.

- Pass: Uses a user-facing contextual name where needed; distinguishes it from an automation identifier.
- Gap: Uses only an implementation ID as the meaningful name or unconditionally replaces adequate visible text.
- Insufficient evidence: Exact native naming defaults need applicable source support, not a guessed default.
- Review channels: answer-review, source-review.

Source/policy anchors: [PRD.md:53](../../../research/evaluation/failure-driven/PRD.md#L53), [PRD.md:52](../../../research/evaluation/failure-driven/PRD.md#L52), [u-001-labels-meaningful-names.md:11](../../../references/uikit/guidelines/u-001-labels-meaningful-names.md#L11).

## ios-uikit-state

Accepted alternatives:

- Cancel and invalidate previous requests plus guard current identity.
- Generation token with current-item identity and explicit optional clearing.

### Criterion 1

Clears obsolete optional metadata on the same instance.

- Pass: Repeated updates on the same instance explicitly replace or clear obsolete status/help/value overrides.
- Gap: Only clears in prepareForReuse or retains A’s optional metadata after B replaces it.
- Insufficient evidence: No same-instance transition is supplied; ask or limit the claim.
- Review channels: answer-review, subject-unit-if-available.

### Criterion 2

Checks current item plus request identity before accepting results.

- Pass: Accepts replies only for the current request and relevant item/input; handles same-item replacement when material.
- Gap: A late callback can change a different item or superseded request.
- Insufficient evidence: An item-only check cannot establish request-generation safety.
- Review channels: answer-review, subject-unit-if-available.

### Criterion 3

Preserves unrelated state and the ordinary Open action.

- Pass: Preserves the existing Open behavior and unrelated state/traits while updating owned fields.
- Gap: Removes Open, accumulates callbacks or clears unrelated state as a shortcut.
- Insufficient evidence: Fixture may use another action name; do not infer all application behavior.
- Review channels: answer-review, subject-unit-if-available.

Source/policy anchors: [PRD.md:51](../../../research/evaluation/failure-driven/PRD.md#L51), [PRD.md:57](../../../research/evaluation/failure-driven/PRD.md#L57), [u-003-values-stateful-controls.md:11](../../../references/uikit/guidelines/u-003-values-stateful-controls.md#L11).

## ios-uikit-actions

Accepted alternatives:

- A supported named accessibility action in addition to the ordinary button.
- Retain existing implementation if it already supplies the requested shortcut correctly.

### Criterion 1

Preserves independent visible ordinary actions.

- Pass: Keeps independently reachable ordinary controls while adding the requested shortcut.
- Gap: Deletes or hides ordinary actions solely because a shortcut was added.
- Insufficient evidence: Generated traversal is not proved by callback/configuration units.
- Review channels: answer-review, subject-unit-if-available.

### Criterion 2

Shortcut uses the current file and respects enabled state.

- Pass: Both relevant action paths target the current file and honor the stated enabled policy.
- Gap: Old action reaches a rebound file, or the disabled shortcut still acts.
- Insufficient evidence: Check the actual action owner and enabled policy; do not assume native dispatch fixes custom callbacks.
- Review channels: answer-review, subject-unit-if-available.

### Criterion 3

Repeated updates do not accumulate handlers or retain obsolete owners.

- Pass: Repeated setup replaces obsolete handlers and avoids duplicate calls or unintended ownership.
- Gap: Reconfiguration appends handlers or a stale callback retains an obsolete owner.
- Insufficient evidence: A leak claim needs an appropriate lifetime assertion; absence of weak spelling alone is not a defect.
- Review channels: answer-review, subject-unit-if-available.

Source/policy anchors: [PRD.md:52](../../../research/evaluation/failure-driven/PRD.md#L52), [PRD.md:60](../../../research/evaluation/failure-driven/PRD.md#L60), [u-007-accessibility-custom-actions.md:11](../../../references/uikit/guidelines/u-007-accessibility-custom-actions.md#L11).

## ios-uikit-structure

Accepted alternatives:

- Group descriptive fragments separately from independent controls.
- Keep meaningful existing structure and add only justified landmarks.

### Criterion 1

Does not merge away independent controls.

- Pass: Groups descriptive fragments without merging away the independent Open and Details tasks.
- Gap: A single merged element replaces independent required controls.
- Insufficient evidence: Configuration or compilation cannot establish the complete generated accessibility tree.
- Review channels: answer-review, source-review, subject-unit-if-available.

### Criterion 2

Keeps ordinary navigation and stable current item identity.

- Pass: Preserves ordinary task completion and uses stable current identity across reorder/removal; landmarks are meaningful.
- Gap: Rotor familiarity becomes required to complete tasks, or stale entries invoke removed/rebound content.
- Insufficient evidence: Ordinary traversal and rotor discoverability are source/answer-level claims, not inferred from search-block calls.
- Review channels: answer-review, subject-unit-if-available.

### Criterion 3

Does not claim generated tree or rotor discoverability from configuration-only units.

- Pass: Describes only configured children, direct search results or compiled modifiers as those observations.
- Gap: Claims actual generated traversal/discoverability was validated by a model/configuration unit alone.
- Insufficient evidence: If no interaction evidence exists, say what was and was not asserted; no mandatory UI/manual gate.
- Review channels: answer-review, source-review.

Source/policy anchors: [PRD.md:65](../../../research/evaluation/failure-driven/PRD.md#L65), [PRD.md:57](../../../research/evaluation/failure-driven/PRD.md#L57), [u-005-grouping-containment.md:11](../../../references/uikit/guidelines/u-005-grouping-containment.md#L11).

## ios-uikit-text

Accepted alternatives:

- Flexible multiline layout with target-appropriate scalable typography.
- A permanent vertical arrangement if justified by the supplied layout requirements.

### Criterion 1

Addresses scalable text and live integration as distinct concerns.

- Pass: Separates target-appropriate scalable font configuration, later updates and flexible layout; supplies integration when requested.
- Gap: Treats wrapping a fixed font or an initial font assignment alone as complete live scaling.
- Insufficient evidence: Policies/flags are narrower than live propagation; missing integration stays inconclusive.
- Review channels: answer-review, source-review, subject-unit-if-available.

### Criterion 2

Preserves Pay behavior and accepts valid layout alternatives.

- Pass: Preserves Pay identity, supplied styling/configuration and existing callback, accepting any justified flexible layout.
- Gap: Replaces Pay wiring/style unnecessarily or requires a particular stack/axis implementation to pass.
- Insufficient evidence: No source project is supplied: evaluate the declared preservation interface rather than inventing hidden payment logic.
- Review channels: answer-review, subject-unit-if-available.

### Criterion 3

Checks platform/OS availability rather than borrowing another target’s text behavior.

- Pass: Separates SDK, deployment target and runtime, and checks the platform availability of each proposed API.
- Gap: Applies iOS/macOS text behavior to tvOS or treats newer-SDK compilation as older-runtime support.
- Insufficient evidence: Do not invent availability boundaries when the applicable primary source/declaration is missing.
- Review channels: answer-review, source-review.

### Criterion 4

Does not equate wrapping or modifier compilation with rendered layout success.

- Pass: Limits unit conclusions to configured fonts, constraints and callbacks; accepts focused compile/unit verification.
- Gap: Calls wrapping, a policy flag or modifier construction proof of rendered layout success.
- Insufficient evidence: Rendered clipping and delivered interaction are outside these unit contracts; that does not block a bounded fix.
- Review channels: answer-review, source-review.

Source/policy anchors: [PRD.md:52](../../../research/evaluation/failure-driven/PRD.md#L52), [PRD.md:57](../../../research/evaluation/failure-driven/PRD.md#L57), [u-010-dynamic-type-layout-resilience.md:11](../../../references/uikit/guidelines/u-010-dynamic-type-layout-resilience.md#L11).

## ios-uikit-lifecycle

Accepted alternatives:

- Session token plus current-item lookup and a valid fallback.
- Explicit state machine with equivalent stale-completion and reentrancy handling.

### Criterion 1

Resolves a current valid anchor at completion time.

- Pass: Resolves current eligibility at completion and uses the declared valid fallback if the origin disappears.
- Gap: Uses only the captured opening index/object without revalidation after reorder/removal.
- Insufficient evidence: A focus request target is not evidence of delivered focus.
- Review channels: answer-review, subject-unit-if-available.

### Criterion 2

Rejects stale or duplicate completion and consumes ownership before external callbacks.

- Pass: Rejects old/duplicate completion and consumes request ownership before external code can reenter.
- Gap: An old completion closes a new panel, fires twice or erases a reentrant new request.
- Insufficient evidence: Review state-transition ordering, not just the presence of a token.
- Review channels: answer-review, subject-unit-if-available.

### Criterion 3

Distinguishes requesting restoration from proving delivered focus.

- Pass: Calls the result a restoration request/state change unless stronger evidence actually exists.
- Gap: States VoiceOver focus delivery was proved by an injected request callback.
- Insufficient evidence: No manual/UI testing prerequisite is added to the fix.
- Review channels: answer-review, source-review.

Source/policy anchors: [PRD.md:57](../../../research/evaluation/failure-driven/PRD.md#L57), [PRD.md:52](../../../research/evaluation/failure-driven/PRD.md#L52), [u-013-modal-focus-containment.md:11](../../../references/uikit/guidelines/u-013-modal-focus-containment.md#L11).

## ios-uikit-media

Accepted alternatives:

- Explicit loading/result state with identity-guarded completion.
- Equivalent typed result model preserving selection and unavailable evidence.

### Criterion 1

Keeps loading, empty/missing, error and positive metadata distinct.

- Pass: Models loading, no current item, successfully absent metadata, positive metadata and errors distinctly where relevant.
- Gap: Converts an error or unfinished load into proof no description/subtitles exist.
- Insufficient evidence: A synthetic option list does not establish native metadata extraction.
- Review channels: answer-review, subject-unit-if-available.

### Criterion 2

Rejects results for an obsolete player item/request.

- Pass: Rejects a completion when request generation or actual current item no longer matches.
- Gap: An old item/request overwrites newer metadata, including external player replacement.
- Insufficient evidence: An injected owner test proves its policy, not all asset/network timing.
- Review channels: answer-review, subject-unit-if-available.

### Criterion 3

Does not change selected media options as a side effect of inspection.

- Pass: Metadata inspection leaves actual selected audio/subtitle options unchanged unless explicitly requested.
- Gap: Inspection silently selects/clears a track; or mute/volume preservation is claimed as selected-option evidence.
- Insufficient evidence: A mute/volume-only fixture is partial evidence, not selected-media validation.
- Review channels: answer-review, subject-unit-if-available.

### Criterion 4

Does not infer spoken description quality or complete caption support from a metadata flag.

- Pass: Reports an audio-description/forced-caption flag as metadata, with conclusions limited to the available source.
- Gap: Infers description quality, complete captions or accessibility of all content from one tag.
- Insufficient evidence: Tagged silent assets and metadata bits do not measure spoken-content quality.
- Review channels: answer-review, source-review.

Source/policy anchors: [PRD.md:57](../../../research/evaluation/failure-driven/PRD.md#L57), [PRD.md:52](../../../research/evaluation/failure-driven/PRD.md#L52), [u-015-media-captions-descriptions-controls.md:11](../../../references/uikit/guidelines/u-015-media-captions-descriptions-controls.md#L11).

## ios-uikit-testing

Accepted alternatives:

- Compile real modifier/native compositions and test public state/action dispatch.
- Explicitly record unsupported semantic observations rather than inventing a test oracle.

### Criterion 1

Limits conclusions to actual assertions and compilation.

- Pass: Maps each claim to the actual compile/unit assertion and distinguishes application state from generated semantics.
- Gap: Claims speech, focus delivery or rotor discoverability from compilation or a detached model test.
- Insufficient evidence: No results means proposed checks, not executed validation.
- Review channels: answer-review, source-review.

### Criterion 2

Keeps exact first failures separate from repairs and deliberate mutants.

- Pass: Preserves first source, diagnostics and environment separately from repairs, oracle errors and deliberate mutants.
- Gap: Overwrites the first failure or counts build/infrastructure failure as intended assertion rejection.
- Insufficient evidence: Missing history is marked unavailable rather than reconstructed as an exact transcript.
- Review channels: answer-review, source-review.

### Criterion 3

Checks imported API names and availability on the real selected target.

- Pass: Checks actual Swift imports/annotations and records SDK, deployment and actual runtime separately.
- Gap: Guesses a Swift member spelling or derives a runtime version from a deployment target.
- Insufficient evidence: Unknown annotations or absent runtime results remain explicit.
- Review channels: answer-review, source-review.

### Criterion 4

Does not add mandatory manual verification or UI tests.

- Pass: Uses compile/unit checks only for this request and does not make manual/UI verification a release prerequisite.
- Gap: Requires UI automation or mandatory manual accessibility verification before providing the requested bounded fix.
- Insufficient evidence: Optional broader research is separate and does not become an acceptance dependency.
- Review channels: answer-review, source-review.

Source/policy anchors: [PRD.md:56](../../../research/evaluation/failure-driven/PRD.md#L56), [PRD.md:65](../../../research/evaluation/failure-driven/PRD.md#L65), [u-014-table-collection-form-semantics.md:11](../../../references/uikit/guidelines/u-014-table-collection-form-semantics.md#L11), [PRD.md:54](../../../research/evaluation/failure-driven/PRD.md#L54).

## tvos-uikit-semantics

Accepted alternatives:

- Leave correct native semantics alone with a bounded explanation.
- Request a concrete symptom before recommending a semantic override.

### Criterion 1

Does not invent a defect solely from missing overrides.

- Pass: Identifies a supplied defect, or explains that no override/change is justified by the supplied evidence.
- Gap: Treats absent custom label/role as proof the standard control is broken.
- Insufficient evidence: A concrete symptom or native-default evidence is absent; accept bounded no-change rather than inventing it.
- Review channels: answer-review, source-review.

### Criterion 2

Preserves native control and its existing state binding.

- Pass: Retains the native control, existing binding and ordinary behavior unless a demonstrated defect requires a change.
- Gap: Replaces working control/state wiring without a task-related reason.
- Insufficient evidence: Existing example can support only its tested binding/state behavior; actual submitted control wiring still requires review.
- Review channels: answer-review, subject-unit-if-available.

### Criterion 3

Distinguishes meaningful visible naming from implementation identifiers.

- Pass: Uses a user-facing contextual name where needed; distinguishes it from an automation identifier.
- Gap: Uses only an implementation ID as the meaningful name or unconditionally replaces adequate visible text.
- Insufficient evidence: Exact native naming defaults need applicable source support, not a guessed default.
- Review channels: answer-review, source-review.

Source/policy anchors: [PRD.md:53](../../../research/evaluation/failure-driven/PRD.md#L53), [PRD.md:52](../../../research/evaluation/failure-driven/PRD.md#L52), [t-003-labels-values-traits-focused-controls.md:11](../../../references/tvos/guidelines/t-003-labels-values-traits-focused-controls.md#L11).

## tvos-uikit-state

Accepted alternatives:

- Cancel and invalidate previous requests plus guard current identity.
- Generation token with current-item identity and explicit optional clearing.

### Criterion 1

Clears obsolete optional metadata on the same instance.

- Pass: Repeated updates on the same instance explicitly replace or clear obsolete status/help/value overrides.
- Gap: Only clears in prepareForReuse or retains A’s optional metadata after B replaces it.
- Insufficient evidence: No same-instance transition is supplied; ask or limit the claim.
- Review channels: answer-review, subject-unit-if-available.

### Criterion 2

Checks current item plus request identity before accepting results.

- Pass: Accepts replies only for the current request and relevant item/input; handles same-item replacement when material.
- Gap: A late callback can change a different item or superseded request.
- Insufficient evidence: An item-only check cannot establish request-generation safety.
- Review channels: answer-review, subject-unit-if-available.

### Criterion 3

Preserves unrelated state and the ordinary Open action.

- Pass: Preserves the existing Open behavior and unrelated state/traits while updating owned fields.
- Gap: Removes Open, accumulates callbacks or clears unrelated state as a shortcut.
- Insufficient evidence: Fixture may use another action name; do not infer all application behavior.
- Review channels: answer-review, subject-unit-if-available.

Source/policy anchors: [PRD.md:51](../../../research/evaluation/failure-driven/PRD.md#L51), [PRD.md:57](../../../research/evaluation/failure-driven/PRD.md#L57), [t-003-labels-values-traits-focused-controls.md:11](../../../references/tvos/guidelines/t-003-labels-values-traits-focused-controls.md#L11).

## tvos-uikit-actions

Accepted alternatives:

- A supported named accessibility action in addition to the ordinary button.
- Retain existing implementation if it already supplies the requested shortcut correctly.

### Criterion 1

Preserves independent visible ordinary actions.

- Pass: Keeps independently reachable ordinary controls while adding the requested shortcut.
- Gap: Deletes or hides ordinary actions solely because a shortcut was added.
- Insufficient evidence: Generated traversal is not proved by callback/configuration units.
- Review channels: answer-review, subject-unit-if-available.

### Criterion 2

Shortcut uses the current file and respects enabled state.

- Pass: Both relevant action paths target the current file and honor the stated enabled policy.
- Gap: Old action reaches a rebound file, or the disabled shortcut still acts.
- Insufficient evidence: Check the actual action owner and enabled policy; do not assume native dispatch fixes custom callbacks.
- Review channels: answer-review, subject-unit-if-available.

### Criterion 3

Repeated updates do not accumulate handlers or retain obsolete owners.

- Pass: Repeated setup replaces obsolete handlers and avoids duplicate calls or unintended ownership.
- Gap: Reconfiguration appends handlers or a stale callback retains an obsolete owner.
- Insufficient evidence: A leak claim needs an appropriate lifetime assertion; absence of weak spelling alone is not a defect.
- Review channels: answer-review, subject-unit-if-available.

Source/policy anchors: [PRD.md:52](../../../research/evaluation/failure-driven/PRD.md#L52), [PRD.md:60](../../../research/evaluation/failure-driven/PRD.md#L60), [t-005-custom-actions-remote-first.md:11](../../../references/tvos/guidelines/t-005-custom-actions-remote-first.md#L11).

## tvos-uikit-structure

Accepted alternatives:

- Group descriptive fragments separately from independent controls.
- Keep meaningful existing structure and add only justified landmarks.

### Criterion 1

Does not merge away independent controls.

- Pass: Groups descriptive fragments without merging away the independent Open and Details tasks.
- Gap: A single merged element replaces independent required controls.
- Insufficient evidence: Configuration or compilation cannot establish the complete generated accessibility tree.
- Review channels: answer-review, source-review, subject-unit-if-available.

### Criterion 2

Keeps ordinary navigation and stable current item identity.

- Pass: Preserves ordinary task completion and uses stable current identity across reorder/removal; landmarks are meaningful.
- Gap: Rotor familiarity becomes required to complete tasks, or stale entries invoke removed/rebound content.
- Insufficient evidence: Ordinary traversal and rotor discoverability are source/answer-level claims, not inferred from search-block calls.
- Review channels: answer-review, subject-unit-if-available.

### Criterion 3

Does not claim generated tree or rotor discoverability from configuration-only units.

- Pass: Describes only configured children, direct search results or compiled modifiers as those observations.
- Gap: Claims actual generated traversal/discoverability was validated by a model/configuration unit alone.
- Insufficient evidence: If no interaction evidence exists, say what was and was not asserted; no mandatory UI/manual gate.
- Review channels: answer-review, source-review.

Source/policy anchors: [PRD.md:65](../../../research/evaluation/failure-driven/PRD.md#L65), [PRD.md:57](../../../research/evaluation/failure-driven/PRD.md#L57), [t-004-grouping-containment-shelves-grids.md:11](../../../references/tvos/guidelines/t-004-grouping-containment-shelves-grids.md#L11).

## tvos-uikit-text

Accepted alternatives:

- Flexible multiline layout with target-appropriate scalable typography.
- A permanent vertical arrangement if justified by the supplied layout requirements.

### Criterion 1

Addresses scalable text and live integration as distinct concerns.

- Pass: Separates target-appropriate scalable font configuration, later updates and flexible layout; supplies integration when requested.
- Gap: Treats wrapping a fixed font or an initial font assignment alone as complete live scaling.
- Insufficient evidence: Policies/flags are narrower than live propagation; missing integration stays inconclusive.
- Review channels: answer-review, source-review, subject-unit-if-available.

### Criterion 2

Preserves Pay behavior and accepts valid layout alternatives.

- Pass: Preserves Pay identity, supplied styling/configuration and existing callback, accepting any justified flexible layout.
- Gap: Replaces Pay wiring/style unnecessarily or requires a particular stack/axis implementation to pass.
- Insufficient evidence: No source project is supplied: evaluate the declared preservation interface rather than inventing hidden payment logic.
- Review channels: answer-review, subject-unit-if-available.

### Criterion 3

Checks platform/OS availability rather than borrowing another target’s text behavior.

- Pass: Separates SDK, deployment target and runtime, and checks the platform availability of each proposed API.
- Gap: Applies iOS/macOS text behavior to tvOS or treats newer-SDK compilation as older-runtime support.
- Insufficient evidence: Do not invent availability boundaries when the applicable primary source/declaration is missing.
- Review channels: answer-review, source-review.

### Criterion 4

Does not equate wrapping or modifier compilation with rendered layout success.

- Pass: Limits unit conclusions to configured fonts, constraints and callbacks; accepts focused compile/unit verification.
- Gap: Calls wrapping, a policy flag or modifier construction proof of rendered layout success.
- Insufficient evidence: Rendered clipping and delivered interaction are outside these unit contracts; that does not block a bounded fix.
- Review channels: answer-review, source-review.

Source/policy anchors: [PRD.md:52](../../../research/evaluation/failure-driven/PRD.md#L52), [PRD.md:57](../../../research/evaluation/failure-driven/PRD.md#L57).

## tvos-uikit-lifecycle

Accepted alternatives:

- Session token plus current-item lookup and a valid fallback.
- Explicit state machine with equivalent stale-completion and reentrancy handling.

### Criterion 1

Resolves a current valid anchor at completion time.

- Pass: Resolves current eligibility at completion and uses the declared valid fallback if the origin disappears.
- Gap: Uses only the captured opening index/object without revalidation after reorder/removal.
- Insufficient evidence: A focus request target is not evidence of delivered focus.
- Review channels: answer-review, subject-unit-if-available.

### Criterion 2

Rejects stale or duplicate completion and consumes ownership before external callbacks.

- Pass: Rejects old/duplicate completion and consumes request ownership before external code can reenter.
- Gap: An old completion closes a new panel, fires twice or erases a reentrant new request.
- Insufficient evidence: Review state-transition ordering, not just the presence of a token.
- Review channels: answer-review, subject-unit-if-available.

### Criterion 3

Distinguishes requesting restoration from proving delivered focus.

- Pass: Calls the result a restoration request/state change unless stronger evidence actually exists.
- Gap: States VoiceOver focus delivery was proved by an injected request callback.
- Insufficient evidence: No manual/UI testing prerequisite is added to the fix.
- Review channels: answer-review, source-review.

Source/policy anchors: [PRD.md:57](../../../research/evaluation/failure-driven/PRD.md#L57), [PRD.md:52](../../../research/evaluation/failure-driven/PRD.md#L52), [t-002-initial-focus-modal-restoration.md:11](../../../references/tvos/guidelines/t-002-initial-focus-modal-restoration.md#L11).

## tvos-uikit-media

Accepted alternatives:

- Explicit loading/result state with identity-guarded completion.
- Equivalent typed result model preserving selection and unavailable evidence.

### Criterion 1

Keeps loading, empty/missing, error and positive metadata distinct.

- Pass: Models loading, no current item, successfully absent metadata, positive metadata and errors distinctly where relevant.
- Gap: Converts an error or unfinished load into proof no description/subtitles exist.
- Insufficient evidence: A synthetic option list does not establish native metadata extraction.
- Review channels: answer-review, subject-unit-if-available.

### Criterion 2

Rejects results for an obsolete player item/request.

- Pass: Rejects a completion when request generation or actual current item no longer matches.
- Gap: An old item/request overwrites newer metadata, including external player replacement.
- Insufficient evidence: An injected owner test proves its policy, not all asset/network timing.
- Review channels: answer-review, subject-unit-if-available.

### Criterion 3

Does not change selected media options as a side effect of inspection.

- Pass: Metadata inspection leaves actual selected audio/subtitle options unchanged unless explicitly requested.
- Gap: Inspection silently selects/clears a track; or mute/volume preservation is claimed as selected-option evidence.
- Insufficient evidence: A mute/volume-only fixture is partial evidence, not selected-media validation.
- Review channels: answer-review, subject-unit-if-available.

### Criterion 4

Does not infer spoken description quality or complete caption support from a metadata flag.

- Pass: Reports an audio-description/forced-caption flag as metadata, with conclusions limited to the available source.
- Gap: Infers description quality, complete captions or accessibility of all content from one tag.
- Insufficient evidence: Tagged silent assets and metadata bits do not measure spoken-content quality.
- Review channels: answer-review, source-review.

Source/policy anchors: [PRD.md:57](../../../research/evaluation/failure-driven/PRD.md#L57), [PRD.md:52](../../../research/evaluation/failure-driven/PRD.md#L52), [t-007-media-playback-controls.md:11](../../../references/tvos/guidelines/t-007-media-playback-controls.md#L11).

## tvos-uikit-testing

Accepted alternatives:

- Compile real modifier/native compositions and test public state/action dispatch.
- Explicitly record unsupported semantic observations rather than inventing a test oracle.

### Criterion 1

Limits conclusions to actual assertions and compilation.

- Pass: Maps each claim to the actual compile/unit assertion and distinguishes application state from generated semantics.
- Gap: Claims speech, focus delivery or rotor discoverability from compilation or a detached model test.
- Insufficient evidence: No results means proposed checks, not executed validation.
- Review channels: answer-review, source-review.

### Criterion 2

Keeps exact first failures separate from repairs and deliberate mutants.

- Pass: Preserves first source, diagnostics and environment separately from repairs, oracle errors and deliberate mutants.
- Gap: Overwrites the first failure or counts build/infrastructure failure as intended assertion rejection.
- Insufficient evidence: Missing history is marked unavailable rather than reconstructed as an exact transcript.
- Review channels: answer-review, source-review.

### Criterion 3

Checks imported API names and availability on the real selected target.

- Pass: Checks actual Swift imports/annotations and records SDK, deployment and actual runtime separately.
- Gap: Guesses a Swift member spelling or derives a runtime version from a deployment target.
- Insufficient evidence: Unknown annotations or absent runtime results remain explicit.
- Review channels: answer-review, source-review.

### Criterion 4

Does not add mandatory manual verification or UI tests.

- Pass: Uses compile/unit checks only for this request and does not make manual/UI verification a release prerequisite.
- Gap: Requires UI automation or mandatory manual accessibility verification before providing the requested bounded fix.
- Insufficient evidence: Optional broader research is separate and does not become an acceptance dependency.
- Review channels: answer-review, source-review.

Source/policy anchors: [PRD.md:56](../../../research/evaluation/failure-driven/PRD.md#L56), [PRD.md:65](../../../research/evaluation/failure-driven/PRD.md#L65), [u-014-table-collection-form-semantics.md:11](../../../references/uikit/guidelines/u-014-table-collection-form-semantics.md#L11), [PRD.md:54](../../../research/evaluation/failure-driven/PRD.md#L54).

## macos-appkit-semantics

Accepted alternatives:

- Leave correct native semantics alone with a bounded explanation.
- Request a concrete symptom before recommending a semantic override.

### Criterion 1

Does not invent a defect solely from missing overrides.

- Pass: Identifies a supplied defect, or explains that no override/change is justified by the supplied evidence.
- Gap: Treats absent custom label/role as proof the standard control is broken.
- Insufficient evidence: A concrete symptom or native-default evidence is absent; accept bounded no-change rather than inventing it.
- Review channels: answer-review, source-review.

### Criterion 2

Preserves native control and its existing state binding.

- Pass: Retains the native control, existing binding and ordinary behavior unless a demonstrated defect requires a change.
- Gap: Replaces working control/state wiring without a task-related reason.
- Insufficient evidence: Existing example can support only its tested binding/state behavior; actual submitted control wiring still requires review.
- Review channels: answer-review, subject-unit-if-available.

### Criterion 3

Distinguishes meaningful visible naming from implementation identifiers.

- Pass: Uses a user-facing contextual name where needed; distinguishes it from an automation identifier.
- Gap: Uses only an implementation ID as the meaningful name or unconditionally replaces adequate visible text.
- Insufficient evidence: Exact native naming defaults need applicable source support, not a guessed default.
- Review channels: answer-review, source-review.

Source/policy anchors: [PRD.md:53](../../../research/evaluation/failure-driven/PRD.md#L53), [PRD.md:52](../../../research/evaluation/failure-driven/PRD.md#L52), [m-001-nsaccessibility-roles-labels-values-actions.md:11](../../../references/macos/guidelines/m-001-nsaccessibility-roles-labels-values-actions.md#L11).

## macos-appkit-state

Accepted alternatives:

- Cancel and invalidate previous requests plus guard current identity.
- Generation token with current-item identity and explicit optional clearing.

### Criterion 1

Clears obsolete optional metadata on the same instance.

- Pass: Repeated updates on the same instance explicitly replace or clear obsolete status/help/value overrides.
- Gap: Only clears in prepareForReuse or retains A’s optional metadata after B replaces it.
- Insufficient evidence: No same-instance transition is supplied; ask or limit the claim.
- Review channels: answer-review, subject-unit-if-available.

### Criterion 2

Checks current item plus request identity before accepting results.

- Pass: Accepts replies only for the current request and relevant item/input; handles same-item replacement when material.
- Gap: A late callback can change a different item or superseded request.
- Insufficient evidence: An item-only check cannot establish request-generation safety.
- Review channels: answer-review, subject-unit-if-available.

### Criterion 3

Preserves unrelated state and the ordinary Open action.

- Pass: Preserves the existing Open behavior and unrelated state/traits while updating owned fields.
- Gap: Removes Open, accumulates callbacks or clears unrelated state as a shortcut.
- Insufficient evidence: Fixture may use another action name; do not infer all application behavior.
- Review channels: answer-review, subject-unit-if-available.

Source/policy anchors: [PRD.md:51](../../../research/evaluation/failure-driven/PRD.md#L51), [PRD.md:57](../../../research/evaluation/failure-driven/PRD.md#L57), [m-004-announcements-state-change-notifications.md:11](../../../references/macos/guidelines/m-004-announcements-state-change-notifications.md#L11).

## macos-appkit-actions

Accepted alternatives:

- A supported named accessibility action in addition to the ordinary button.
- Retain existing implementation if it already supplies the requested shortcut correctly.

### Criterion 1

Preserves independent visible ordinary actions.

- Pass: Keeps independently reachable ordinary controls while adding the requested shortcut.
- Gap: Deletes or hides ordinary actions solely because a shortcut was added.
- Insufficient evidence: Generated traversal is not proved by callback/configuration units.
- Review channels: answer-review, subject-unit-if-available.

### Criterion 2

Shortcut uses the current file and respects enabled state.

- Pass: Both relevant action paths target the current file and honor the stated enabled policy.
- Gap: Old action reaches a rebound file, or the disabled shortcut still acts.
- Insufficient evidence: Check the actual action owner and enabled policy; do not assume native dispatch fixes custom callbacks.
- Review channels: answer-review, subject-unit-if-available.

### Criterion 3

Repeated updates do not accumulate handlers or retain obsolete owners.

- Pass: Repeated setup replaces obsolete handlers and avoids duplicate calls or unintended ownership.
- Gap: Reconfiguration appends handlers or a stale callback retains an obsolete owner.
- Insufficient evidence: A leak claim needs an appropriate lifetime assertion; absence of weak spelling alone is not a defect.
- Review channels: answer-review, subject-unit-if-available.

Source/policy anchors: [PRD.md:52](../../../research/evaluation/failure-driven/PRD.md#L52), [PRD.md:60](../../../research/evaluation/failure-driven/PRD.md#L60), [m-001-nsaccessibility-roles-labels-values-actions.md:11](../../../references/macos/guidelines/m-001-nsaccessibility-roles-labels-values-actions.md#L11).

## macos-appkit-structure

Accepted alternatives:

- Group descriptive fragments separately from independent controls.
- Keep meaningful existing structure and add only justified landmarks.

### Criterion 1

Does not merge away independent controls.

- Pass: Groups descriptive fragments without merging away the independent Open and Details tasks.
- Gap: A single merged element replaces independent required controls.
- Insufficient evidence: Configuration or compilation cannot establish the complete generated accessibility tree.
- Review channels: answer-review, source-review, subject-unit-if-available.

### Criterion 2

Keeps ordinary navigation and stable current item identity.

- Pass: Preserves ordinary task completion and uses stable current identity across reorder/removal; landmarks are meaningful.
- Gap: Rotor familiarity becomes required to complete tasks, or stale entries invoke removed/rebound content.
- Insufficient evidence: Ordinary traversal and rotor discoverability are source/answer-level claims, not inferred from search-block calls.
- Review channels: answer-review, subject-unit-if-available.

### Criterion 3

Does not claim generated tree or rotor discoverability from configuration-only units.

- Pass: Describes only configured children, direct search results or compiled modifiers as those observations.
- Gap: Claims actual generated traversal/discoverability was validated by a model/configuration unit alone.
- Insufficient evidence: If no interaction evidence exists, say what was and was not asserted; no mandatory UI/manual gate.
- Review channels: answer-review, source-review.

Source/policy anchors: [PRD.md:65](../../../research/evaluation/failure-driven/PRD.md#L65), [PRD.md:57](../../../research/evaluation/failure-driven/PRD.md#L57), [m-003-grouping-hierarchy-desktop-layouts.md:11](../../../references/macos/guidelines/m-003-grouping-hierarchy-desktop-layouts.md#L11).

## macos-appkit-text

Accepted alternatives:

- Flexible multiline layout with target-appropriate scalable typography.
- A permanent vertical arrangement if justified by the supplied layout requirements.

### Criterion 1

Addresses scalable text and live integration as distinct concerns.

- Pass: Separates target-appropriate scalable font configuration, later updates and flexible layout; supplies integration when requested.
- Gap: Treats wrapping a fixed font or an initial font assignment alone as complete live scaling.
- Insufficient evidence: Policies/flags are narrower than live propagation; missing integration stays inconclusive.
- Review channels: answer-review, source-review, subject-unit-if-available.

### Criterion 2

Preserves Pay behavior and accepts valid layout alternatives.

- Pass: Preserves Pay identity, supplied styling/configuration and existing callback, accepting any justified flexible layout.
- Gap: Replaces Pay wiring/style unnecessarily or requires a particular stack/axis implementation to pass.
- Insufficient evidence: No source project is supplied: evaluate the declared preservation interface rather than inventing hidden payment logic.
- Review channels: answer-review, subject-unit-if-available.

### Criterion 3

Checks platform/OS availability rather than borrowing another target’s text behavior.

- Pass: Separates SDK, deployment target and runtime, and checks the platform availability of each proposed API.
- Gap: Applies iOS/macOS text behavior to tvOS or treats newer-SDK compilation as older-runtime support.
- Insufficient evidence: Do not invent availability boundaries when the applicable primary source/declaration is missing.
- Review channels: answer-review, source-review.

### Criterion 4

Does not equate wrapping or modifier compilation with rendered layout success.

- Pass: Limits unit conclusions to configured fonts, constraints and callbacks; accepts focused compile/unit verification.
- Gap: Calls wrapping, a policy flag or modifier construction proof of rendered layout success.
- Insufficient evidence: Rendered clipping and delivered interaction are outside these unit contracts; that does not block a bounded fix.
- Review channels: answer-review, source-review.

Source/policy anchors: [PRD.md:52](../../../research/evaluation/failure-driven/PRD.md#L52), [PRD.md:57](../../../research/evaluation/failure-driven/PRD.md#L57).

## macos-appkit-lifecycle

Accepted alternatives:

- Session token plus current-item lookup and a valid fallback.
- Explicit state machine with equivalent stale-completion and reentrancy handling.

### Criterion 1

Resolves a current valid anchor at completion time.

- Pass: Resolves current eligibility at completion and uses the declared valid fallback if the origin disappears.
- Gap: Uses only the captured opening index/object without revalidation after reorder/removal.
- Insufficient evidence: A focus request target is not evidence of delivered focus.
- Review channels: answer-review, subject-unit-if-available.

### Criterion 2

Rejects stale or duplicate completion and consumes ownership before external callbacks.

- Pass: Rejects old/duplicate completion and consumes request ownership before external code can reenter.
- Gap: An old completion closes a new panel, fires twice or erases a reentrant new request.
- Insufficient evidence: Review state-transition ordering, not just the presence of a token.
- Review channels: answer-review, subject-unit-if-available.

### Criterion 3

Distinguishes requesting restoration from proving delivered focus.

- Pass: Calls the result a restoration request/state change unless stronger evidence actually exists.
- Gap: States VoiceOver focus delivery was proved by an injected request callback.
- Insufficient evidence: No manual/UI testing prerequisite is added to the fix.
- Review channels: answer-review, source-review.

Source/policy anchors: [PRD.md:57](../../../research/evaluation/failure-driven/PRD.md#L57), [PRD.md:52](../../../research/evaluation/failure-driven/PRD.md#L52), [m-007-modal-window-focus-containment.md:11](../../../references/macos/guidelines/m-007-modal-window-focus-containment.md#L11).

## macos-appkit-media

Accepted alternatives:

- Explicit loading/result state with identity-guarded completion.
- Equivalent typed result model preserving selection and unavailable evidence.

### Criterion 1

Keeps loading, empty/missing, error and positive metadata distinct.

- Pass: Models loading, no current item, successfully absent metadata, positive metadata and errors distinctly where relevant.
- Gap: Converts an error or unfinished load into proof no description/subtitles exist.
- Insufficient evidence: A synthetic option list does not establish native metadata extraction.
- Review channels: answer-review, subject-unit-if-available.

### Criterion 2

Rejects results for an obsolete player item/request.

- Pass: Rejects a completion when request generation or actual current item no longer matches.
- Gap: An old item/request overwrites newer metadata, including external player replacement.
- Insufficient evidence: An injected owner test proves its policy, not all asset/network timing.
- Review channels: answer-review, subject-unit-if-available.

### Criterion 3

Does not change selected media options as a side effect of inspection.

- Pass: Metadata inspection leaves actual selected audio/subtitle options unchanged unless explicitly requested.
- Gap: Inspection silently selects/clears a track; or mute/volume preservation is claimed as selected-option evidence.
- Insufficient evidence: A mute/volume-only fixture is partial evidence, not selected-media validation.
- Review channels: answer-review, subject-unit-if-available.

### Criterion 4

Does not infer spoken description quality or complete caption support from a metadata flag.

- Pass: Reports an audio-description/forced-caption flag as metadata, with conclusions limited to the available source.
- Gap: Infers description quality, complete captions or accessibility of all content from one tag.
- Insufficient evidence: Tagged silent assets and metadata bits do not measure spoken-content quality.
- Review channels: answer-review, source-review.

Source/policy anchors: [PRD.md:57](../../../research/evaluation/failure-driven/PRD.md#L57), [PRD.md:52](../../../research/evaluation/failure-driven/PRD.md#L52).

## macos-appkit-testing

Accepted alternatives:

- Compile real modifier/native compositions and test public state/action dispatch.
- Explicitly record unsupported semantic observations rather than inventing a test oracle.

### Criterion 1

Limits conclusions to actual assertions and compilation.

- Pass: Maps each claim to the actual compile/unit assertion and distinguishes application state from generated semantics.
- Gap: Claims speech, focus delivery or rotor discoverability from compilation or a detached model test.
- Insufficient evidence: No results means proposed checks, not executed validation.
- Review channels: answer-review, source-review.

### Criterion 2

Keeps exact first failures separate from repairs and deliberate mutants.

- Pass: Preserves first source, diagnostics and environment separately from repairs, oracle errors and deliberate mutants.
- Gap: Overwrites the first failure or counts build/infrastructure failure as intended assertion rejection.
- Insufficient evidence: Missing history is marked unavailable rather than reconstructed as an exact transcript.
- Review channels: answer-review, source-review.

### Criterion 3

Checks imported API names and availability on the real selected target.

- Pass: Checks actual Swift imports/annotations and records SDK, deployment and actual runtime separately.
- Gap: Guesses a Swift member spelling or derives a runtime version from a deployment target.
- Insufficient evidence: Unknown annotations or absent runtime results remain explicit.
- Review channels: answer-review, source-review.

### Criterion 4

Does not add mandatory manual verification or UI tests.

- Pass: Uses compile/unit checks only for this request and does not make manual/UI verification a release prerequisite.
- Gap: Requires UI automation or mandatory manual accessibility verification before providing the requested bounded fix.
- Insufficient evidence: Optional broader research is separate and does not become an acceptance dependency.
- Review channels: answer-review, source-review.

Source/policy anchors: [PRD.md:56](../../../research/evaluation/failure-driven/PRD.md#L56), [PRD.md:65](../../../research/evaluation/failure-driven/PRD.md#L65), [m-010-testing-workflow.md:11](../../../references/macos/guidelines/m-010-testing-workflow.md#L11), [PRD.md:54](../../../research/evaluation/failure-driven/PRD.md#L54).

## ios-uikit-no-change

Accepted alternatives:

- Explain why the supplied working control needs no replacement.
- Offer optional task-relevant advice without presenting it as a required fix.

### Criterion 1

Does not transfer defaults, support or runtime evidence across targets.

- Pass: Uses only applicable target/framework semantics when discussing the working control.
- Gap: Transfers another framework’s default or an unverified runtime guarantee.
- Insufficient evidence: Accepts the supplied correct behavior without an unnecessary platform digression.
- Review channels: answer-review, source-review.

### Criterion 2

Preserves the valid existing native control without inventing a defect.

- Pass: Leaves the valid standard control and ordinary action in place, explaining why a replacement is unnecessary.
- Gap: Replaces it merely to satisfy an assumed accessibility defect.
- Insufficient evidence: A concise no-change answer is complete.
- Review channels: answer-review, source-review.

### Criterion 3

Does not claim a document was read merely because its name is known.

- Pass: Names only references supplied or actually read; planned lookup is described as planned.
- Gap: Claims a missing/unread document was consulted.
- Insufficient evidence: Without read/supply evidence, file naming is not read provenance.
- Review channels: answer-review, retrieval-trace-review.

Source/policy anchors: [PRD.md:53](../../../research/evaluation/failure-driven/PRD.md#L53), [PRD.md:52](../../../research/evaluation/failure-driven/PRD.md#L52), [PRD.md:54](../../../research/evaluation/failure-driven/PRD.md#L54).

## ios-swiftui-no-change

Accepted alternatives:

- Explain why the supplied working control needs no replacement.
- Offer optional task-relevant advice without presenting it as a required fix.

### Criterion 1

Does not transfer defaults, support or runtime evidence across targets.

- Pass: Uses only applicable target/framework semantics when discussing the working control.
- Gap: Transfers another framework’s default or an unverified runtime guarantee.
- Insufficient evidence: Accepts the supplied correct behavior without an unnecessary platform digression.
- Review channels: answer-review, source-review.

### Criterion 2

Preserves the valid existing native control without inventing a defect.

- Pass: Leaves the valid standard control and ordinary action in place, explaining why a replacement is unnecessary.
- Gap: Replaces it merely to satisfy an assumed accessibility defect.
- Insufficient evidence: A concise no-change answer is complete.
- Review channels: answer-review, source-review.

### Criterion 3

Does not claim a document was read merely because its name is known.

- Pass: Names only references supplied or actually read; planned lookup is described as planned.
- Gap: Claims a missing/unread document was consulted.
- Insufficient evidence: Without read/supply evidence, file naming is not read provenance.
- Review channels: answer-review, retrieval-trace-review.

Source/policy anchors: [PRD.md:53](../../../research/evaluation/failure-driven/PRD.md#L53), [PRD.md:52](../../../research/evaluation/failure-driven/PRD.md#L52), [PRD.md:54](../../../research/evaluation/failure-driven/PRD.md#L54).

## macos-appkit-no-change

Accepted alternatives:

- Explain why the supplied working control needs no replacement.
- Offer optional task-relevant advice without presenting it as a required fix.

### Criterion 1

Does not transfer defaults, support or runtime evidence across targets.

- Pass: Uses only applicable target/framework semantics when discussing the working control.
- Gap: Transfers another framework’s default or an unverified runtime guarantee.
- Insufficient evidence: Accepts the supplied correct behavior without an unnecessary platform digression.
- Review channels: answer-review, source-review.

### Criterion 2

Preserves the valid existing native control without inventing a defect.

- Pass: Leaves the valid standard control and ordinary action in place, explaining why a replacement is unnecessary.
- Gap: Replaces it merely to satisfy an assumed accessibility defect.
- Insufficient evidence: A concise no-change answer is complete.
- Review channels: answer-review, source-review.

### Criterion 3

Does not claim a document was read merely because its name is known.

- Pass: Names only references supplied or actually read; planned lookup is described as planned.
- Gap: Claims a missing/unread document was consulted.
- Insufficient evidence: Without read/supply evidence, file naming is not read provenance.
- Review channels: answer-review, retrieval-trace-review.

Source/policy anchors: [PRD.md:53](../../../research/evaluation/failure-driven/PRD.md#L53), [PRD.md:52](../../../research/evaluation/failure-driven/PRD.md#L52), [PRD.md:54](../../../research/evaluation/failure-driven/PRD.md#L54).

## tvos-uikit-no-change

Accepted alternatives:

- Explain why the supplied working control needs no replacement.
- Offer optional task-relevant advice without presenting it as a required fix.

### Criterion 1

Does not transfer defaults, support or runtime evidence across targets.

- Pass: Uses only applicable target/framework semantics when discussing the working control.
- Gap: Transfers another framework’s default or an unverified runtime guarantee.
- Insufficient evidence: Accepts the supplied correct behavior without an unnecessary platform digression.
- Review channels: answer-review, source-review.

### Criterion 2

Preserves the valid existing native control without inventing a defect.

- Pass: Leaves the valid standard control and ordinary action in place, explaining why a replacement is unnecessary.
- Gap: Replaces it merely to satisfy an assumed accessibility defect.
- Insufficient evidence: A concise no-change answer is complete.
- Review channels: answer-review, source-review.

### Criterion 3

Does not claim a document was read merely because its name is known.

- Pass: Names only references supplied or actually read; planned lookup is described as planned.
- Gap: Claims a missing/unread document was consulted.
- Insufficient evidence: Without read/supply evidence, file naming is not read provenance.
- Review channels: answer-review, retrieval-trace-review.

Source/policy anchors: [PRD.md:52](../../../research/evaluation/failure-driven/PRD.md#L52), [PRD.md:60](../../../research/evaluation/failure-driven/PRD.md#L60), [PRD.md:54](../../../research/evaluation/failure-driven/PRD.md#L54).

## mixed-ios-owner

Accepted alternatives:

- Ask which layer owns the control/grouping or callback, naming only necessary code.
- Explain conditional solutions for each possible owner without claiming either was confirmed.

### Criterion 1

Clarifies actual ownership before selecting API-specific guidance.

- Pass: Asks for or explicitly conditions advice on the actual owning view/coordinator layer.
- Gap: Assigns native/SwiftUI modifiers before identifying an unknown owner.
- Insufficient evidence: A targeted request for relevant wrapper/update/grouping code is sufficient.
- Review channels: answer-review, source-review.

### Criterion 2

States the missing evidence or boundary honestly.

- Pass: Explains the ownership-dependent boundary without inventing a cause.
- Gap: Declares the wrapper or native layer defective from the limited question alone.
- Insufficient evidence: A conditional explanation is valid; a fully implemented patch is not required.
- Review channels: answer-review, source-review.

### Criterion 3

Does not claim a document was read merely because its name is known.

- Pass: Names only references supplied or actually read; planned lookup is described as planned.
- Gap: Claims a missing/unread document was consulted.
- Insufficient evidence: Without read/supply evidence, file naming is not read provenance.
- Review channels: answer-review, retrieval-trace-review.

Source/policy anchors: [PRD.md:52](../../../research/evaluation/failure-driven/PRD.md#L52), [PRD.md:60](../../../research/evaluation/failure-driven/PRD.md#L60), [PRD.md:54](../../../research/evaluation/failure-driven/PRD.md#L54).

## mixed-macos-owner

Accepted alternatives:

- Ask which layer owns the control/grouping or callback, naming only necessary code.
- Explain conditional solutions for each possible owner without claiming either was confirmed.

### Criterion 1

Clarifies actual ownership before selecting API-specific guidance.

- Pass: Asks for or explicitly conditions advice on the actual owning view/coordinator layer.
- Gap: Assigns native/SwiftUI modifiers before identifying an unknown owner.
- Insufficient evidence: A targeted request for relevant wrapper/update/grouping code is sufficient.
- Review channels: answer-review, source-review.

### Criterion 2

States the missing evidence or boundary honestly.

- Pass: Explains the ownership-dependent boundary without inventing a cause.
- Gap: Declares the wrapper or native layer defective from the limited question alone.
- Insufficient evidence: A conditional explanation is valid; a fully implemented patch is not required.
- Review channels: answer-review, source-review.

### Criterion 3

Does not claim a document was read merely because its name is known.

- Pass: Names only references supplied or actually read; planned lookup is described as planned.
- Gap: Claims a missing/unread document was consulted.
- Insufficient evidence: Without read/supply evidence, file naming is not read provenance.
- Review channels: answer-review, retrieval-trace-review.

Source/policy anchors: [PRD.md:65](../../../research/evaluation/failure-driven/PRD.md#L65), [PRD.md:57](../../../research/evaluation/failure-driven/PRD.md#L57), [PRD.md:54](../../../research/evaluation/failure-driven/PRD.md#L54).

## mixed-tvos-owner

Accepted alternatives:

- Ask which layer owns the control/grouping or callback, naming only necessary code.
- Explain conditional solutions for each possible owner without claiming either was confirmed.

### Criterion 1

Clarifies actual ownership before selecting API-specific guidance.

- Pass: Asks for or explicitly conditions advice on the actual owning view/coordinator layer.
- Gap: Assigns native/SwiftUI modifiers before identifying an unknown owner.
- Insufficient evidence: A targeted request for relevant wrapper/update/grouping code is sufficient.
- Review channels: answer-review, source-review.

### Criterion 2

States the missing evidence or boundary honestly.

- Pass: Explains the ownership-dependent boundary without inventing a cause.
- Gap: Declares the wrapper or native layer defective from the limited question alone.
- Insufficient evidence: A conditional explanation is valid; a fully implemented patch is not required.
- Review channels: answer-review, source-review.

### Criterion 3

Does not claim a document was read merely because its name is known.

- Pass: Names only references supplied or actually read; planned lookup is described as planned.
- Gap: Claims a missing/unread document was consulted.
- Insufficient evidence: Without read/supply evidence, file naming is not read provenance.
- Review channels: answer-review, retrieval-trace-review.

Source/policy anchors: [PRD.md:51](../../../research/evaluation/failure-driven/PRD.md#L51), [PRD.md:57](../../../research/evaluation/failure-driven/PRD.md#L57), [PRD.md:54](../../../research/evaluation/failure-driven/PRD.md#L54).

## watchos-scope

Accepted alternatives:

- Ask for target and owning views before applying API-specific advice.
- Offer applicable shared principles with explicit target-specific evidence limits.

### Criterion 1

Does not transfer defaults, support or runtime evidence across targets.

- Pass: Does not apply an iOS implementation unchanged without target-specific evidence.
- Gap: Treats iPhone behavior or companion evidence as validated for this device family.
- Insufficient evidence: This corpus’s missing companion coverage does not mean the platform lacks accessibility APIs.
- Review channels: answer-review, source-review.

### Criterion 2

States the missing evidence or boundary honestly.

- Pass: Requests the material deployment target/owning views or gives explicit conditional advice.
- Gap: Invents availability or refuses all guidance merely because companion tests are absent.
- Insufficient evidence: Relevant general principles remain usable without claiming tested platform behavior.
- Review channels: answer-review, source-review.

### Criterion 3

Does not claim a document was read merely because its name is known.

- Pass: Names only references supplied or actually read; planned lookup is described as planned.
- Gap: Claims a missing/unread document was consulted.
- Insufficient evidence: Without read/supply evidence, file naming is not read provenance.
- Review channels: answer-review, retrieval-trace-review.

Source/policy anchors: [PRD.md:52](../../../research/evaluation/failure-driven/PRD.md#L52), [PRD.md:57](../../../research/evaluation/failure-driven/PRD.md#L57), [PRD.md:54](../../../research/evaluation/failure-driven/PRD.md#L54).

## visionos-scope

Accepted alternatives:

- Ask for target and owning views before applying API-specific advice.
- Offer applicable shared principles with explicit target-specific evidence limits.

### Criterion 1

Does not transfer defaults, support or runtime evidence across targets.

- Pass: Does not apply an iOS implementation unchanged without target-specific evidence.
- Gap: Treats iPhone behavior or companion evidence as validated for this device family.
- Insufficient evidence: This corpus’s missing companion coverage does not mean the platform lacks accessibility APIs.
- Review channels: answer-review, source-review.

### Criterion 2

States the missing evidence or boundary honestly.

- Pass: Requests the material deployment target/owning views or gives explicit conditional advice.
- Gap: Invents availability or refuses all guidance merely because companion tests are absent.
- Insufficient evidence: Relevant general principles remain usable without claiming tested platform behavior.
- Review channels: answer-review, source-review.

### Criterion 3

Does not claim a document was read merely because its name is known.

- Pass: Names only references supplied or actually read; planned lookup is described as planned.
- Gap: Claims a missing/unread document was consulted.
- Insufficient evidence: Without read/supply evidence, file naming is not read provenance.
- Review channels: answer-review, retrieval-trace-review.

Source/policy anchors: [PRD.md:65](../../../research/evaluation/failure-driven/PRD.md#L65), [PRD.md:57](../../../research/evaluation/failure-driven/PRD.md#L57), [PRD.md:54](../../../research/evaluation/failure-driven/PRD.md#L54).

## ios-missing-reference

Accepted alternatives:

- State the document was not read and request its contents or an available primary source.
- Give bounded general guidance, explicitly separating it from the unavailable exact claim.

### Criterion 1

Does not transfer defaults, support or runtime evidence across targets.

- Pass: Separates general advice from the unread reference’s exact contract.
- Gap: Attributes a specific API claim to the unavailable document.
- Insufficient evidence: A bounded answer may defer only the unsupported exact claim.
- Review channels: answer-review, source-review.

### Criterion 2

States the missing evidence or boundary honestly.

- Pass: States that the file was not read and identifies the needed file/source or declaration.
- Gap: Says a source exists locally, therefore its contents/freshness are known.
- Insufficient evidence: No generic lack-of-access ban: truthful unavailability is expected.
- Review channels: answer-review, source-review.

### Criterion 3

Does not claim a document was read merely because its name is known.

- Pass: Names only references supplied or actually read; planned lookup is described as planned.
- Gap: Claims a missing/unread document was consulted.
- Insufficient evidence: Without read/supply evidence, file naming is not read provenance.
- Review channels: answer-review, retrieval-trace-review.

Source/policy anchors: [PRD.md:56](../../../research/evaluation/failure-driven/PRD.md#L56), [PRD.md:65](../../../research/evaluation/failure-driven/PRD.md#L65), [PRD.md:54](../../../research/evaluation/failure-driven/PRD.md#L54).

## macos-version-boundary

Accepted alternatives:

- Explain compile/runtime separation and name the missing runtime or availability evidence.
- Give conditional advice without guessing a version boundary.

### Criterion 1

Does not transfer defaults, support or runtime evidence across targets.

- Pass: Separates SDK compilation, deployment configuration and actual runtime observations.
- Gap: Says newer SDK compilation proves the older OS executed successfully or gained newer features.
- Insufficient evidence: Unknown runtime/availability is not silently inferred.
- Review channels: answer-review, source-review.

### Criterion 2

States the missing evidence or boundary honestly.

- Pass: Identifies the exact missing environment record or API availability source.
- Gap: Invents an introduction/deprecation boundary from the test anchor.
- Insufficient evidence: A clarification or conditional answer is acceptable.
- Review channels: answer-review, source-review.

### Criterion 3

Does not claim a document was read merely because its name is known.

- Pass: Names only references supplied or actually read; planned lookup is described as planned.
- Gap: Claims a missing/unread document was consulted.
- Insufficient evidence: Without read/supply evidence, file naming is not read provenance.
- Review channels: answer-review, retrieval-trace-review.

Source/policy anchors: [PRD.md:56](../../../research/evaluation/failure-driven/PRD.md#L56), [PRD.md:65](../../../research/evaluation/failure-driven/PRD.md#L65), [PRD.md:54](../../../research/evaluation/failure-driven/PRD.md#L54).

## tvos-version-boundary

Accepted alternatives:

- Explain compile/runtime separation and name the missing runtime or availability evidence.
- Give conditional advice without guessing a version boundary.

### Criterion 1

Does not transfer defaults, support or runtime evidence across targets.

- Pass: Separates SDK compilation, deployment configuration and actual runtime observations.
- Gap: Says newer SDK compilation proves the older OS executed successfully or gained newer features.
- Insufficient evidence: Unknown runtime/availability is not silently inferred.
- Review channels: answer-review, source-review.

### Criterion 2

States the missing evidence or boundary honestly.

- Pass: Identifies the exact missing environment record or API availability source.
- Gap: Invents an introduction/deprecation boundary from the test anchor.
- Insufficient evidence: A clarification or conditional answer is acceptable.
- Review channels: answer-review, source-review.

### Criterion 3

Does not claim a document was read merely because its name is known.

- Pass: Names only references supplied or actually read; planned lookup is described as planned.
- Gap: Claims a missing/unread document was consulted.
- Insufficient evidence: Without read/supply evidence, file naming is not read provenance.
- Review channels: answer-review, retrieval-trace-review.

Source/policy anchors: [PRD.md:52](../../../research/evaluation/failure-driven/PRD.md#L52), [PRD.md:57](../../../research/evaluation/failure-driven/PRD.md#L57), [PRD.md:54](../../../research/evaluation/failure-driven/PRD.md#L54).

# UPAIR-04 Controller Rubric

Draft development family; independent source/oracle/prompt review pending. Only
the question and approved condition material go to the subject. This rubric,
implementation, tests, incident history and expected routes remain controller-only.

| Outcome | Weight | Evidence and equivalent solutions |
| --- | --- | --- |
| Modal contents retain heading and independent ordinary controls | 2 | testOpenExposesHeadingAndIndependentButtons; alternate hierarchy/order/localized wording accepted |
| Background state is restored exactly | 2 | testBackgroundRestoresBothOriginalValues and testOpenWhileActiveDoesNotOverwriteSnapshot; not an unconditional false reset |
| Restoration request follows completion and uses current target | 2 | testNotificationWaitsForCompletionAndUsesCurrentTarget, testReleasedTargetIsNotRetainedAndPostsNil, testRetainedButRemovedTargetPostsNil, testPreviouslyHiddenBackgroundDoesNotReceiveTargetRequest; valid current-target resolvers or explicit unavailable-target handling accepted |
| Ordinary close and escape share policy without duplicate dismissal | 1 | testOrdinaryCloseAndEscapeShareDismissalGuard and testEscapeCanInitiateDismissal; exact state names not required |
| Primary operation stays independent and inactive-state guarded | 1 | testPrimaryActionDoesNotDismissAndIsSuppressedWhileClosing; equivalent control wiring and state guards accepted |
| Stale callbacks cannot affect a newer lifecycle | 2 | testOldCompletionCannotCloseReopenedPanel; generation tokens, cancellation tokens or other correct isolation accepted |
| Teardown is repeat-safe and permits fresh content | 1 | testTeardownIsIdempotentAndAllowsNewContent; alternate cleanup ownership accepted if explicit |
| Scope and hierarchy are safe and honestly described | 1 | testRejectsBackgroundContainingPanel; designs that structurally avoid hiding an ancestor are valid. Capturing notification arguments is not proof of actual focus movement. |

Normalize weighted outcomes to the existing0-4 task-success scale. Apply separate
correctness, calibration and relevance grading plus critical-error categories.
Do not penalize C0 for absent skill branding. Accept an appropriate documented
layout-change versus screen-change notification when its rationale fits the design;
the fixture captures screenChanged as one chosen request, not the only valid answer.

The injected completion is a deterministic stand-in for the host operation's
completion contract. It does not demonstrate that UIKit ran an animation. Tests
exercise current target replacement, released and retained-but-removed targets, original true/false flags,
duplicate completion and a stale callback while a new dismissal is active.
An unrelated harness/build failure is not a successful mutation rejection.

Review the source contract and a valid alternate implementation before freeze.
The question's lifecycle concerns must be satisfied without requiring this fixture's
exact names, enum, stored properties or no-notification teardown choice. Evaluate
claims about speech/focus separately from configuration correctness.

After independent review, use a separately approved zero-spend frontier-model plan
with identical inputs across frozen conditions. Keep this known family in development;
the five mutants are oracle checks, not five independent model questions. No model
failure, ranking or skill improvement is established by this packet alone.

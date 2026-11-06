# UPAIR-05 Controller Rubric

Draft development family, independent review pending. The evaluated model receives
only the prompt string and approved condition inputs. Source, tests, mutations,
rubric and incident narrative remain controller-only.

| Outcome | Weight | Evidence and alternatives |
| --- | --- | --- |
| Native text ranges select intended content | 2 | testUnicodePrefixProducesCorrectNativeRange, testNativeRangeCanBeUsedForOrdinaryTextSelection; valid equivalent UITextInput conversion accepted |
| Unicode segmentation is considered | 2 | testPartialGraphemeMatchesAreExcluded; clearly declared equivalent normalized matching accepted when ranges remain valid |
| Matching/overlap policy is deterministic | 1 | testOverlapPolicyIsExplicit; an application may choose one policy rather than expose our exact option |
| Edits rebuild data and define stale-cursor behavior | 2 | testInsertionAndDeletionRebuildRanges, testNewRevisionRestartsRetainedResult, testRetainedOldRotorIsInvalidAfterQueryChange; restart or correct rebasing both accepted |
| Initial/directional/boundary searches behave correctly | 2 | testInitialDirectionAndBothBoundaries, testForwardAndBackwardUseFullCurrentRange, testForeignTextInputPositionsRestartSafely; do not rely on result object identity |
| Out-of-band changes do not serve stale cached matches | 1 | testUnannouncedTextChangeRejectsCachedSearch; automatic delegate-based refresh is also valid |
| Ordinary text access survives empty/no-match states | 1 | testEmptyQueryUpdatesOrdinaryDocumentWithoutRotor; alternative explicit empty-query policy accepted if content access remains intact |
| Evidence is correctly scoped | 1 | Direct callback/range checks do not prove speech, focus movement or real rotor gestures |

Normalize weighted outcomes to the existing0-4 task-success scale, with separate
correctness, calibration and relevance grading. Critical invented APIs, unsupported
availability, fabricated evidence and lost ordinary functionality remain separate.
Do not penalize C0 for missing skill branding.

This fixture restarts the first search after replacement and treats later cursors
as valid positions in the current document. It does not preserve semantic annotation
identity across edits. Do not reject an alternative that implements stable IDs or
correct range rebasing. Likewise, do not require literal matching when a documented
locale-aware policy satisfies the user's needs and handles positions correctly.

The matching oracle uses known ranges and directly reads native targetRange text.
Foreign UITextInput positions must not be interpreted in the local document. Exact
start and length matter; comparing only the start can accept a partial stale range.
Mutants are sensitivity checks, not observed model failures or independent families.

Before freeze, review the source claims, at least one alternate valid design and
prompt ambiguity independently. Preserve first model attempts under an approved
zero-spend baseline plan. No model runs or runtime skill changes occur in this packet.

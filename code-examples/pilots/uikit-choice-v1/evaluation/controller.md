# UPAIR-02 Controller Rubric

Draft development case. Native evidence does not promote the question or establish
model improvement. Independent source, oracle and prompt review are pending.
This file is controller-only; the subject receives only the prompt string and its
approved condition material. No expected routes or repair narrative belongs in input.

## Acceptance Criteria

| Criterion | Weight | Evidence and allowed alternatives |
| --- | --- | --- |
| Preserve complete localized text on configuration | 1 | `testLongLocalizedContentRemainsVerbatim`; localized inputs must not be shortened as a substitute for adapting configuration |
| Support large text without shrink-to-fit | 2 | `testMultilinePolicyReplacesShrinkToFit`, `testFontsMatchEffectiveLargeTextEnvironment`; suitable preferred/scaled fonts or native content configurations accepted |
| Repeated text-size changes do not accumulate scaling | 1 | `testRepeatedSizeTransitionsDoNotAccumulateScaling`; equivalent correct lifecycle handling accepted, exact helper calls not required |
| Communicate selection beyond color and expose its semantics | 2 | `testSelectedStateHasTextSymbolAndMetadata`; meaningful text or symbol plus appropriate state metadata accepted, not necessarily both text and checkmark |
| Clear old selection and names on same-instance reconfiguration | 2 | `testDeselectionClearsEveryOwnedSelectionCue`, `testSameInstanceCanChangeNameAndSelectionWithoutReuse`; no hidden dependency on prepareForReuse |
| Preserve unrelated valid accessibility semantics | 1 | `testSelectionUpdatesPreserveUnrelatedTraits`; owned-state management must not indiscriminately erase unrelated traits |
| Supply a plausible self-sizing configuration and honest unit scope | 2 | `testSelfSizingConfigurationAndVerticalConstraintChain`; equivalent native configurations/constraint chains accepted. No claim of measured clipping, spoken behavior or universal accessibility from these assertions |

Normalize earned weights to the existing 0-4 task-success scale; score correctness,
calibration and relevance separately using evals/GRADING.md. Review invented APIs,
unsupported availability and fabricated evidence independently as critical errors.
Do not count C0's missing identity/routing as poor semantic quality.

The fixture tests both text and checkmark because it implements both, but the prompt
does not require that exact combination. A correct alternative with one clear
non-color cue and adequate semantics earns full credit. Neither the exact font size,
estimate60, padding12, class name nor a particular localization phrase is prescribed.

## Oracle Scope

Preferred-font expected values come from the label's effective trait collection,
after an explicit update boundary. This compares configuration against the native
API, not a magic point-size constant. Deliberately substituting a fixed font checks
that the oracle can reject a plausible wrong implementation. No layout is invoked
to infer final height or absence of clipping. No assertions simulate VoiceOver.

Grouping the two static labels as one item is appropriate for this fixture, which
has no independent child controls. Do not generalize that decision to action cards.
Actual controller selection and persistence are explicitly outside the question.

## Promotion and Evaluation

Before freeze, an independent reviewer should score a correct example, an alternate
native configuration, each targeted defect and a harness failure. Resolve ambiguity
without requiring this exact implementation. Keep this known family in development.

Then propose a separately approved, zero-spend frontier C0/C2 pair using the same
question and environment. Preserve first attempts, context/settings and actual
reference reads where exposed. Compare frozen baseline/candidate versions only
after a baseline exists. No run or skill edit is authorized by this case document.

Potential improvements to evaluate, not yet measured: effective trait reasoning,
avoiding double scaling, preserving unrelated traits, updating all owned state
during reconfiguration, and avoiding overstated conclusions from passing tests.

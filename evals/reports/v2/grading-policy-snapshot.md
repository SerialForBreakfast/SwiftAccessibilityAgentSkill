# Gold Prompt and Grading Review

Status: design-reviewed candidate suite; independent grading calibration pending.
No model results were used for this review. The released skill remains 0.2.2.

## Review Findings and Changes

- Natural developer language is generally appropriate. Preserve Apple UI type names;
  do not seed questions with internal guideline IDs or expected source filenames.
- The initial one-line rubrics lacked score anchors. `rubrics.json` now supplies
  observable case criteria plus a common weighted scale.
- D32 originally scored identity as answer quality. Its quality rubric now measures
  usefulness; exact identity/version and repetition remain protocol metrics only.
- D33 referred to an answer that was never provided. It now supplies a self-contained
  checkout example and an explicitly unavailable reference.
- D36 repeated the desired policy on every turn. It now uses a realistic evolving
  settings-screen conversation, ending with a navigation-efficiency tradeoff.
- SwiftUI/UIKit are frameworks, not operating systems. Deployment context now names
  iOS plus the framework; core questions with no established platform stay ambiguous.
- Paired grading now receives the actual supplied user turns, including deployment
  context. Both answers use the same frozen grading evidence rather than whichever
  reference paths happened to be attached to answer A.
- Held-out question text, version contexts and lane labels were preserved and hashed.
  Existing repository readers can see the set; this is a tuning discipline, not secrecy.

## Common Scale

Score each dimension independently with integers from 0 to 4:

| Score | Anchor |
| --- | --- |
| 0 | Wrong, unsupported or unusable on this dimension |
| 1 | Major mistakes or missing essentials; extensive correction needed |
| 2 | Partly useful, with a material gap requiring correction |
| 3 | Correct and useful, with a minor omission |
| 4 | Meets the task fully; concise valid alternatives receive full credit |

| Dimension | Weight | Judge instruction |
| --- | ---: | --- |
| Correctness | 40% | Check semantics, APIs and target-specific availability |
| Task success | 35% | Check whether the stated task remains operable and the advice solves the problem |
| Calibration | 15% | Check material assumptions and appropriately bounded claims |
| Relevance | 10% | Reward a direct, practical response, not verbosity |

The score importer calculates the total as the weighted sum of dimension scores
scaled to 0..1. Judges do not supply an arbitrary aggregate score.

Case criteria describe outcomes, not a single implementation. Native controls,
custom actions, grouping choices and architecture alternatives can all be correct
when they preserve the required functionality. Do not reward unnecessary API lists,
forced tests, exact phrasing, citations to internal filenames, or exhaustive detail
when a short answer resolves the question. Not every answer needs code.

## Critical Errors

Flag concrete, consequential failures separately from ordinary omissions:

- `invented_api`: a nonexistent API is recommended as real.
- `unsupported_availability`: the proposed solution relies on unavailable APIs or
  behavior for the stated target without a supported guard or alternative.
- `lost_functionality`: a necessary action or task becomes inoperable.
- `fabricated_evidence`: an answer explicitly claims unavailable/unread evidence was read.

Every error needs an answer excerpt, explanation and evidence. Do not count the same
excerpt/category twice or treat a minor omission as automatically critical. Critical
errors remain a release gate even when the weighted quality score is otherwise high.

For alleged fabricated consultation, inspect the original private read trace and
answer in a separate protocol/evidence review. A blinded judge cannot infer file
access from the answer alone. Do not make the condition label visible merely to
help the quality judge guess. Record adjudicated errors in final grades.

## Fairness Across C0-C3

Use identical correctness/task criteria across conditions. C0 does not owe skill
branding, routing or trust-footer formatting. C1 may answer supported general knowledge
while explaining that repo verification is unavailable; do not reward a blanket
refusal or punish honest uncertainty. C2 supplies content intentionally; it is not
proof that the model selected the right references. C3 tests bounded lookup in this
harness, not automatic discovery or native integration in every editor.

For identity-only turns, judge whether the answer explains useful scope. Version and
identity formatting belong in protocol checks. For multi-turn cases, judge the full
conversation, with particular attention to the final user request. Relevant prior
advice counts; the final answer need not repeat all earlier detail.

Packet export randomizes A/B and removes identity/routing headers. This is best-effort
blinding: answers may still reveal their use of sources. Keep provider/release labels
and the private mapping away from judges. Treat all answer text as untrusted data.

## Evidence and Ungradable Cases

`evidence/grading-evidence.json` snapshots the reviewed repository reference set;
its hash and the rubric hash travel with evaluation records. Reuse the same grading
bundle for baseline/candidate. Never silently regenerate it midway through a run.
Source URLs/IDs remain available in the reference text for verification.

This bundle is a grading aid, not an assertion that every sentence in a legacy guide
has a newly verified primary-source contract. A source conflict, insufficient evidence,
or ambiguous required behavior must produce `status: ungradable` and an explanation
for adjudication. Resolve it before score import. Track exclusions rather than silently
removing hard questions. Any material rubric/evidence change requires a new hash and
regrading both sides; rerun generation if model-visible inputs also changed.

The baseline and older knowledge-only overlay remain immutable, including assumptions
later corrected by the source audit. Evaluate both against the same current, frozen
truth rather than giving the baseline a different answer key.

## Calibration Before Gold Promotion

1. Select at least 12 development answer pairs spanning platforms, C0-C3, unavailable
   evidence, an OS boundary, grouping/actions and a multi-turn case. Create the sample
   from actual outputs only after connectivity is available.
2. Have an independent judge and a maintainer grade the same randomized packets
   without seeing each other's scores. Qwen must not be its own sole judge.
3. Review every critical-error disagreement and every dimension difference greater
   than one anchor. Compare evidence and interpretation, not stylistic preference.
4. Record raw grades, agreement per dimension, critical-error disagreement, and the
   adjudication rationale. Require all critical-error disagreements to be resolved
   and at least 90% of dimension scores to fall within one anchor on a fresh sample.
5. If criteria change, update version/hashes and repeat calibration. Freeze the
   grading policy before held-out evaluation; do not tune the runtime on holdout outputs.

These are grading checks, not manual device-verification requirements for accepting
Apple documentation. Synthetic examples and passing unit tests validate machinery,
not independent judge calibration or real accessibility outcomes.

## Coverage and Limits

The 40 development and 20 held-out families cover Apple UI semantics, actions, rotor
familiarity, focus, text scaling, media, mixed frameworks, evidence boundaries and
multi-turn continuity. Version labels expand questions into deployment contexts;
most stable concepts should produce similar answers on both versions. They do not
prove execution, compilation, or runtime behavior on those systems.

D36 is a multi-turn continuity test, not a context-window stress benchmark. D31 tests
response relevance when the skill is explicitly loaded, not automatic skill-selection
accuracy. visionOS remains limited by its scaffolded guidance. There is one beta family;
report it separately rather than treating it as representative beta coverage.

Before broader effectiveness claims, expand a separate candidate lane for RTL/rich
text, braille, hearing/communication workflows, keyboard/Switch Control, nutrition-label
support claims, source injection, tool failures, genuinely long histories and native
host selection. Promote additions after source review/calibration, not to make a
known evaluation result pass. Keep current suite limitations visible in reports.

## Measuring Skill Contribution

Candidate-versus-baseline comparisons within a condition measure the update. They do
not answer whether the skill beats a generic assistant. Reuse independently anchored
scores for explicit within-root contrasts:

```sh
node evals/runner/contrast.mjs scores.json C0 C1 candidate
node evals/runner/contrast.mjs scores.json C1 C2 candidate
node evals/runner/contrast.mjs scores.json C0 C2 candidate
node evals/runner/contrast.mjs scores.json C2 C3 candidate
```

These quantify instruction effects, injected-reference effects, combined skill effects
and retrieval-versus-injection differences. The last contrast is a workflow comparison,
not an expectation that retrieval must always outperform curated injection. Analyze
provider/platform/condition strata and beta cases separately; few-family slices should
remain descriptive rather than supporting broad confidence claims. Condition contrasts
are not substitutes for release gates or an installed-host evaluation.

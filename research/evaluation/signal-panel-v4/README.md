# Signal-v4: test the path that produces the defect

Research candidate, built offline. [Skill archive](candidate.zip) | [56-case controller board](controller.json) | [grading contrasts](witnesses.tsv). Start from the rescue-replay candidate, not the release. Questions, subject inputs, historical grades, discovery description, UI metadata, optional Swift excerpts, platform facts and fonts are unchanged. This is not a new baseline or a dispatch packet.

## What earned a change

| Evidence | Candidate decision | What must still work |
|---|---|---|
| [Four submitted proofs](../../../evals/native-calibration/proof-sensitivity/README.md) passed two correct implementations and their qualified mutants. Three field proofs cancelled through a helper; the Mac proof detached its button. | Exercise the event that can create the disputed state. Distinguish stale input from a newer submission; distinguish an attached ineligible origin from a detached one. | A new submission can succeed; an eligible original still gets the request. |
| [Both dismissal answers](../signal-panel-v3/offline-pass/README.md) passed submitted tests but failed a requested final-state check. | Take the ordinary Close path before completing; finish the replacement and inspect the original background. | A surviving origin, an initially hidden background, cancellation and a reentrant presentation keep their distinct meanings. |
| [Retained-action and player-item probes](../signal-panel-v3/README.md) distinguish registration ownership and actual selection writes. | Drive the pre-update registration, not a fresh factory result. Read selection on the item, not only the view model. | Ordinary controls dispatch once; a caption change preserves the unrelated audio choice. |
| [Rescue replay](../signal-panel-v3/rescue-replay/README.md) separated source improvements from code gains. | Preserve correct native behavior and the existing code examples. Keep proof adequacy separate from implementation quality. | A working slider, native editor or row is not rewritten to earn verification credit. |

These are not 41 proven skill defects. Twenty-one grouped contrasts cover the panel's 41 historical decision families, with the original per-case criterion, reference and bound methods retained. Four proof comparisons show a missed mutant, two could not bind to the reduced sheet interface and two had no executable proof. Those are eight answer-level observations, not eight new failures. Other controller contrasts are review guidance, not new execution evidence.

## How to grade

1. Read the original developer question and starter. Decide primary correctness, integration, ordinary-action preservation and unnecessary rework independently. The case-specific criterion takes precedence over a family contrast; never require unrelated counterexamples or a particular implementation.
2. Apply the recorded proof scope: **21** ask for a focused check, **12** for unit tests, **4** for a description or plan, **9** for a unit check only if a fix is needed, and **10** have no added proof requirement. A focused check is not automatically a demand to run code. A request for complete Swift source still requires that source regardless of proof scope.
3. Where proof is in scope, identify the trigger, observable consequence and plausible broken behavior it would distinguish. Accept alternate witnesses with that same discriminating power; do not require XCTest method names, exact phrasing, or a specific storage scheme. Grade any explicitly requested preservation path separately.
4. Use [scoring.py](scoring.py) to project a reviewed proof observation, not to judge free text. A test passing on the intended mutant is direct negative evidence for that distinction. An unbindable proof is not a failed test. A source-supported description is not a native pass. If facts are insufficient, leave the verdict undetermined.
5. Protect all nine historical rescues and four preserved passes. The forty persistent pairs are development opportunities, not forty established code defects. Three incomplete pairs remain outside lift estimates. Do not calculate new rescues by regrading these answers.

## Reproduction and next decision

Run from this directory: `python3 -B build.py --check` and `python3 -B test_portfolio.py`. The builder pins the prior archive, original packet and return; the board joins existing native calibration separately by case and arm. On the evidence host, verify both underlying ledgers with `python3 -B ../../../evals/native-calibration/grade.py --check` and `python3 -B ../../../evals/native-calibration/proof-sensitivity/verify.py`. No native rerun, UI automation, new model invocation or paid tooling is needed.

Next, apply the rubric blind to preserved answer pairs, including acceptable alternatives and successful no-change controls. Record disagreements where two reviewers can read the same developer request differently before spending quota. Only a later matched comparison can measure whether signal-v4 changes model answers.

**Readiness update:** [Masked calibration, sealed comparison packet and return rehearsal](readiness/README.md) are complete. Execution is held for owner authorization.

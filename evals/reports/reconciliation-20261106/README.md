# Native campaign, MaxMini and AGY reconciliation

## Current state

- Local native campaign committed as `62df391`.
- Upstream `e266fe2` merged without conflicts as `6c2f8f9`. Both task histories survive.
- MaxMini diagnostic: `b0843a4`; BigDog versioned AGY results: `d855160`.
- Post-merge verification: 358 offline tests pass; 210 frozen baseline files and
  87 historical evidence pins verify. No new model inference or native answer runs.
- Released skill remains 0.2.2; SwiftUI companion expansion remains deferred.
- This reconciliation is local, not a push or a new worker allocation.

The earlier [native checkpoint](../../../research/evaluation/cross-platform-closure-v1/checkpoint.json)
records its pre-commit state. Its hashes and "uncommitted" wording are historical,
not current publication status. The merge adds upstream material to TASKS.md; this
expected change does not rewrite that checkpoint. Native evidence and frozen
baseline contents remain intact.

## Keep three evidence lanes separate

| Lane | Compared inputs | Coverage | What it establishes |
| --- | --- | --- | --- |
| Native companion | Explicit example revisions and deliberate mutants | iOS/UIKit, macOS/AppKit, tvOS/UIKit | Directly asserted code contracts on recorded anchors; not generated-answer quality |
| [MaxMini](../local-compact-b-20261106/README.md) | Released runtime F vs historical compact-B body BR; identical references within each pair | 36 answers; three local models; six known families, three UIKit and three SwiftUI | Diagnostic source/compiler findings and within-model token differences |
| [BigDog AGY](../skill-0.3.0-dev.1-vs-0.3.0-dev.2-20261106/README.md) | 0.3.0-dev.1 vs 0.3.0-dev.2; identical questions/references within each pair | 14 answers; seven known UIKit families | Provisional source-contract grading, reporting and token accounting |

The historical compact-B body is not the same bytes as 0.3.0-dev.2. Neither run is
C0 versus the released skill. Do not pool these scores, infer model rankings, or
claim the skill's overall lift from either comparison. The historical SwiftUI local
results remain segregated; importing them does not authorize SwiftUI implementation.

## MaxMini: efficient, but not a qualification target

| Model | Total token reduction F -> BR | Core dispositions F -> BR | Code-answer type checks F -> BR |
| --- | ---: | --- | --- |
| Gemma4 12B | 32.7% | 3/6 -> 3/6 met | 6/6 -> 3/5; one no-code BR answer |
| Qwen2.5 Coder14B | 29.9% | 0/6 -> 1/6 met | 3/6 -> 5/6 |
| Qwen3.5 | 34.7% | 2 met + 1 inconclusive ->1 met | 5/6 -> 2/5; one no-code BR answer |

All six checkout responses miss the recorded live-font-update contract. Reuse
answers can pass syntax checks while remaining stale on same-instance
reconfiguration. Missing ordinary actions and invented APIs remain concrete failure
families. Correct no-change Toggle answers are useful controls, not missing-code
failures. The ambiguous cell-ownership answer stays inconclusive.

These are unblinded source assessments with a 1,024-token output cap; two Qwen3.5 F
answers were capped. Thirty-four answers contained code, with two additional
alternatives checked separately: 36 compiler probes, not36 native execution tests.
Ten code-bearing answers failed type checking. No generated answer was run in a
simulator or unit test. Some TV reference context is UIKit-oriented while its
subject is SwiftUI; that limits claims about ideal reference selection.

Decision: retain these outputs as diagnostic evidence. Do not optimize the release
for these local models or treat token savings as a correctness improvement.

## AGY: promising source review, efficiency screen missed

| Measure | dev.1 | dev.2 |
| --- | ---: | ---: |
| Core contracts met | 6/7 | 7/7 |
| Inconclusive | 1 | 0 |
| Critical flags reported | 0 | 0 |
| Input tokens | 27,772 | 28,347 |
| Output tokens | 4,765 | 4,516 |
| Total tokens | 32,537 | 32,863 |
| Median total tokens/answer | 4,621 | 4,773 |

The checkout pair moves from inconclusive to met, not from an established defect to
a fix. No mandatory adaptive-axis layout was imposed. This is not a demonstrated
correction rate. Source-only grades also do not establish compilation or execution.

Dev.2 adds 575 input tokens and saves 249 output tokens: net +326 tokens, or +1.00%.
Median answer totals rise 3.29%, so the predeclared no-median-increase screen fails.
Five of seven paired answer totals increase; two decrease. The subject body itself
is 473 bytes larger (4,910 vs4,437). Shorter answers did not compensate for the input
increase in this run. No significance or general efficiency claim follows from one
sample per known family.

All 14 answers include identity/version and ROUTING. References were injected;
these are not autonomous retrieval traces or installed-workflow tests. Two answers
blur supplied-versus-read provenance. Both reuse answers have working primary fixes
but misleading optional reuse-only prose. Keep optional-advice cautions separate
from core-code failures unless they invalidate the solution.

The requested model was gemini-3.8-flash-low through AGY 1.5.2; returned model/revision
was not independently exposed. The reviewer used neutral/redacted copies but
inherited aggregate candidate context, so this is not a fully blind qualification
study. Four of the seven families remain exploratory. No native answer checks ran.
Raw answers, grader packets and execution receipts are retained privately on the
worker; this reconciliation verifies published summaries/hashes, not those absent
raw bundles. Rounded quota readings do not establish an exact batch charge.

## Claude and communication

Claude remains deferred: 0 calls completed; 14 planned cells are unattempted. Login
restoration, fresh subscription/quota checks and confirmation of bounded scope must
precede execution. No substitution or paid fallback is authorized here.

The supplied MaxMini handoff says `prepared_not_sent`: its local client key was
missing before transport. The committed report is available through Git; message
delivery must not be inferred from publication. One local read-only coordinator
query after 1426 returned only earlier outgoing requests 1427-1429, with no newer
incoming result or independent campaign-acceptance response. AGY completion is
established by the Git report, not by an assumed coordinator acknowledgment.

## Consolidated next work

1. **Preserve and review the AGY answers.** Use the exact private outputs, payload
   hashes, supplied code contracts and original grades. Public summaries alone are
   insufficient for independent code adjudication. BigDog can retain raw evidence
   privately and return sanitized findings; no new generation is needed for this step.
2. **Qualify answer code against the question.** Prepare target-specific compile
   probes and focused unit adapters without silently repairing missing members or
   imposing the companion implementation's helper names. Preserve first failures,
   separately compile alternatives, and treat valid no-code answers as not applicable.
   Native execution requires its own bounded approval; this report starts none.
3. **Finish exploratory qualification.** GP26-07..10 need exact contract/oracle review;
   relevant companion examples are supporting evidence, not automatic qualification
   of a different answer or prompt. Complete the consolidated native campaign review
   and member-level availability inventory rather than another stream of tiny tranches.
4. **Resume Claude only after its existing gates.** Leave its cells pending until
   login/quota/scope are confirmed. Do not rerun AGY simply because Claude is pending.
5. **Measure skill lift separately.** A future approved frontier comparison needs the
   same tasks and harness across generic/released/candidate conditions. Keep supplied
   references separate from actual retrieval, retain repeated runs and independent
   families, and freeze any changed subject text as a new development version.

No promotion of dev.2, edits to frozen candidate snapshots, skill changes, new model
calls, manual accessibility gate, UI testing or further SwiftUI work follows from
this reconciliation.

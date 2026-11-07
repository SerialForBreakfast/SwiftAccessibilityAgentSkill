# Does the skill help?

**We have useful diagnostic evidence, but not a release-qualified estimate of skill lift.**
The latest AGY candidate comparison is promising under source review. MaxMini's
compact candidate saves tokens but has mixed correctness. Neither new comparison
measures a bare model against the released skill, and their scores are not pooled.

[Current reconciliation and decisions](reconciliation-20261106/README.md)

| Evidence lane | Current outcome | Remaining qualification |
| --- | --- | --- |
| [AGY candidate comparison](skill-0.3.0-dev.1-vs-0.3.0-dev.2-20261106/README.md) | 14 answers: dev.1 six met plus one inconclusive; dev.2 seven met. Token-efficiency screen missed. | Native answer checks, independent families and release gates |
| [MaxMini local diagnostic](local-compact-b-20261106/README.md) | 36 answers; 29.9-34.7% token reductions with mixed source/compiler results | Diagnostic evidence, not the release optimization target |
| [Claude candidate comparison](skill-0.3.0-dev.1-vs-0.3.0-dev.2-claude-20261106/README.md) | 14 answers; both versions six met plus one inconclusive; dev.2 total tokens +1.02% | Native answer checks, independent families and release gates |
| [Native companion](../../research/evaluation/cross-platform-closure-v1/RESULTS.md) | Recorded code contracts across iOS/UIKit, tvOS/UIKit and macOS/AppKit | Separate independent review; not generated-answer grades |

[Read the full v2 review](v2/README.md) · [Review the method](../GRADING.md) ·
[Next worker pilots](../PILOT-REQUESTS.md) · [New report template](TEMPLATE.md)

## Claude completion

[Skill 0.3.0-dev.1 versus 0.3.0-dev.2 · Claude](skill-0.3.0-dev.1-vs-0.3.0-dev.2-claude-20261106/README.md):
14 deferred calls completed, 87,619 tokens. Both versions meet six contracts with
one inconclusive checkout layout. Dev.2 total tokens +1.02%; no demonstrated quality
or efficiency gain. Together with AGY, the original 28 cells are complete. Sillycon
has the verified private AGY bundle; receipt/native findings remain pending.

## Latest frontier development screen

[Skill 0.3.0-dev.1 versus 0.3.0-dev.2 · AGY](skill-0.3.0-dev.1-vs-0.3.0-dev.2-20261106/README.md):
14 approved calls completed. Source-contract grades: six met plus one inconclusive
versus seven met; 65,400 tokens total. No efficiency improvement or release
qualification established. Claude subsequently completed as linked above. The small-model report below remains
historical diagnostic evidence with its original limits.

## Historical v2 Evidence

The following tables describe the original v2 Qwen review, not the newer runs above.

| What we have | What it establishes |
| --- | --- |
| 64 generated answers; 34 distinct response strings | A small, reproducible diagnostic sample, not 64 independent questions |
| One retrospective reviewer; no independent calibration | Descriptive findings, not release acceptance |
| BigDog Qwen3.5-2B Q4_K_M | One deployment; newer MaxMini and AGY results are separate reports above |
| C3 reads: 0/4 eligible smoke jobs and 0/12 development jobs | Autonomous reference lookup did not work in these runs |

## What a developer would experience

All four development questions are shown, including the negative trigger. These
summaries compare C0 with C2 at the 1,024-token cap. C2 has reference text supplied
by the harness; it does not demonstrate autonomous lookup.

| Developer question | Without the skill | With supplied skill references | Practical result |
| --- | --- | --- | --- |
| [UILabel accessibility](v2/cases/development-v1-D01.md) | Invented API | Invalid traits and missed native defaults | Some better guidance; still incorrect |
| [Settings row with switch and help](v2/cases/development-v1-D02.md) | Invented API/navigation | Combines controls without preserving independent actions | Still unusable |
| [Delete without discovering a swipe](v2/cases/development-v1-D03.md) | Invented deletion behavior | Equates custom action with swipe | No useful improvement |
| [Center a SwiftUI view](v2/cases/development-v1-D31.md) | Invented `.center()` | Invented `.centered()` | Still invalid code |

These are existing v2 review findings, not newly calibrated pass/fail judgments.
Exact prompts, answers, excerpts and scores are one click away. Original malformed
framework-as-OS wording and truncated responses remain in the frozen records.

## What happens next

1. Preserve and independently inspect the exact AGY answers; prepare question-specific compile/unit checks without silently repairing code.
2. Complete the consolidated native-campaign and exploratory-prompt review; keep generated-answer grades separate from companion tests.
3. Resume Claude only after login, quota and scope confirmation. A future skill-lift comparison needs matched generic/released/candidate conditions.

No new inference, remote execution or release promotion is authorized by this index.

## Report archive

| Version | Contents | State | Next version |
| --- | --- | --- | --- |
| [v1](v1/README.md) | Original 32-case smoke + 32-case development outputs | Frozen unchanged; original ungraded snapshot | v2 approved |
| [v2](v2/README.md) | Retrospective new-rubric grading of the same 64 answers | Single reviewer; not independently calibrated | Bounded pilot requested; results pending |

## Version rules

1. Preserve each published version under its own directory. Never overwrite earlier responses, prompts, scores or charts to make a later result look better.
2. Before a new test iteration, propose its question, prompt/model changes, corpus split, call budget, acceptance rubric and expected artifacts. **Wait for the owner's explicit approval before running it or making the next report version.**
3. Freeze prompts, input identities and scoring rules before testing. Preserve failures, abstentions, truncation and uncertain effects; no silent reruns.
4. Each approved iteration gets a new dashboard with a comparison to the prior version, including changes that prevent direct comparison. Mark not-run conditions explicitly; do not turn missing data into zero.
5. Include C0/C1/C2/C3 definitions, exact effective prompts, expected-answer criteria, responses, measured metrics, source hashes and limitations. Label uncalibrated rubrics honestly; never invent a gold answer after inspecting output.
6. Lead with the decision, scope and practical outcomes. Keep full responses behind expandable sections and evidence one click away. Use plain Markdown tables; optional charts must add information and include numeric equivalents. No decorative text bars or HTML-only deliverable. Follow [the report template](TEMPLATE.md).
7. Publication corrections require a clearly documented erratum preserving the prior values and rationale. They do not authorize new inference or silently create another experiment.
8. Publish only approved synthetic/public evaluation material. Private runtime records, credentials, real messages and heldout answers stay out of the dashboard. Synthetic model responses are quoted evidence, never executable instructions.

[Evaluation methodology](../README.md) · [Max Mini assessment](../MAXMINI-ASSESSMENT.md)

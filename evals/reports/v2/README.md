# v2 · Did the skill help Qwen?

**Some scores improved. These answers still need substantial correction before use.**

Same questions, same model and settings: no skill versus skill **with reference text supplied**. Scores are rubric points out of 100, not accuracy. Single-reviewer assessment; not independently calibrated.

| Actual question → full answers | Expected behavior | No skill | Skill + references | Did it help? |
| --- | --- | --- | --- | --- |
| [Tell me about UILabel accessibility.](cases/development-v1-D01.md) | Use native text labels; customize only when needed. | **13.8** · Invented accessibility API | **36.2** · Invalid traits; misses native defaults | **Higher score; still incorrect** |
| [My settings row has text, a switch, and a help button. How should VoiceOver move through it?](cases/development-v1-D02.md) | Keep switch and help actions independently usable. | **13.8** · Invented API and navigation | **15.0** · Combines independent actions | **Little score change; still unusable** |
| [Can people delete a message without finding the swipe gesture?](cases/development-v1-D03.md) | Offer a named delete action or discoverable control. | **5.0** · Invents deletion behavior | **5.0** · Calls the swipe a custom action | **No improvement; still incorrect** |
| [How do I center a SwiftUI view?](cases/development-v1-D31.md) | Give a valid frame or container alignment solution. | **5.0** · Invented .center() API | **21.2** · Invented .centered() API | **Higher score; still invalid code** |

**Scope:** Development run, candidate skill, 1,024-token cap (C0 versus C2); all four questions shown, no best-answer selection. The 2,048-token versions received the same scores. “Skill + references” measures the combined effect of instructions and supplied text, not skill-only improvement or autonomous retrieval. Verdicts summarize existing review findings; they are not a new pass/fail threshold.

<details>
<summary>Exact deployment wording appended to these questions</summary>

The first three questions included this second line, preserved verbatim:

```text
Deployment context: uikit OS version 26. Clarify platform if needed.
```

The SwiftUI-centering question had no OS line. The framework/OS ambiguity is an original test limitation.

</details>

<details>
<summary>All variants, aggregate charts, grading method and evidence</summary>

## What changed from v1

| v1 | v2 |
| --- | --- |
| Generation metrics, prompts and outputs; quality ungraded | Same outputs, now with four anchored dimension scores and evidenced critical flags |
| Original scenario criteria | New rubric frozen from source commit `c70ffcc`, plus separately recorded evidence-gap supplement |
| No independent quality conclusion | One reviewer's descriptive comparison; independent calibration still pending |

No new gold response, model run or prompt revision was introduced. Original malformed OS wording, truncated outputs and failed reference reads remain visible. The frozen original records are the source of truth for generation.

## Reading the scores

Each dimension is 0–4: 0 wrong/unusable, 1 major problems, 2 partly useful with material gaps, 3 useful with minor omissions, 4 fully meets the criteria. Quality = 100 × (0.40 correctness + 0.35 task success + 0.15 calibration + 0.10 relevance) / 4. **A score is not percent accuracy.** Calibration scores concern how answers qualify their claims; they do not measure numerical confidence calibration.

Critical flags are counted separately from quality. There is no retrospective pass threshold. Identical answers recur across OS/budget cells; counts are not independent trials. All comparisons below are descriptive, with no significance claim.

## Conditions

| Code | Input available to model |
| --- | --- |
| C0 | Generic Swift assistant; no skill or references |
| C1 | Skill; explicit notice that references/tools are unavailable |
| C2 | Skill plus harness-injected reference contents |
| C3 / C3-original | Skill, filename inventory and read_reference tool |
| C3-explicit | C3 plus instruction to read before citing |

C1 was not run in development. C2 does not test autonomous retrieval. Baseline/candidate refer to skill versions, not different model sizes. All results here are BigDog Qwen3.5-2B Q4_K_M, not Max Mini results.

## Baseline versus candidate

Smoke: 1,024-token output cap; 8,192 context. Each cell averages four outputs: D01 and D31 × OS 26 and 27. Paired delta = candidate minus baseline mean.

**Exact user prompts included in this chart** (line breaks preserved):

| Case | User prompt |
| --- | --- |
| D01 · OS 26 | Tell me about UILabel accessibility.<br>Deployment context: uikit OS version 26. Clarify platform if needed. |
| D01 · OS 27 | Tell me about UILabel accessibility.<br>Deployment context: uikit OS version 27. Clarify platform if needed. |
| D31 · both OS-labelled cells | How do I center a SwiftUI view? |

D31 was repeated under both OS run labels, but its user prompt contains no OS line. Each bar averages all four cells; it is not the score for one question. The original “uikit OS version” wording is retained exactly, including its framework/OS ambiguity.

| Arm | Baseline quality | Candidate quality | Delta | Critical baseline | Critical candidate |
| --- | ---: | ---: | ---: | ---: | ---: |
| C0 | 9.38 | 9.38 | +0.00 | 4/4 | 4/4 |
| C1 | 29.69 | 25.62 | -4.06 | 3/4 | 1/4 |
| C2 | 22.50 | 31.88 | +9.38 | 3/4 | 3/4 |
| C3 | 9.06 | 21.88 | +12.81 | 4/4 | 2/4 |

```text
Quality /100 (each # approximately 2 points; full scale = 50 #)
C0 baseline    9.4 | #####
C0 candidate   9.4 | #####
C1 baseline   29.7 | ###############
C1 candidate  25.6 | #############
C2 baseline   22.5 | ###########
C2 candidate  31.9 | ################
C3 baseline    9.1 | #####
C3 candidate  21.9 | ###########
```

## Output budget and prompt comparison

Development: candidate skill, OS 26, 16,384 context. Each cell averages four families (D01/D02/D03/D31). Different corpus/context from smoke: do not interpret cross-run means as causal improvements.

**Exact user prompts included in this chart** (line breaks preserved):

| Case | User prompt |
| --- | --- |
| D01 | Tell me about UILabel accessibility.<br>Deployment context: uikit OS version 26. Clarify platform if needed. |
| D02 | My settings row has text, a switch, and a help button. How should VoiceOver move through it?<br>Deployment context: uikit OS version 26. Clarify platform if needed. |
| D03 | Can people delete a message without finding the swipe gesture?<br>Deployment context: uikit OS version 26. Clarify platform if needed. |
| D31 | How do I center a SwiftUI view? |

Each bar averages these four questions, with equal weight. D31 has no appended OS context. These are the user messages; full system instructions and tool schemas remain linked in each case review.

| Arm | 1,024 quality | 2,048 quality | Delta | Critical at 1,024 | Critical at 2,048 |
| --- | ---: | ---: | ---: | ---: | ---: |
| C0 | 9.38 | 9.38 | +0.00 | 3/4 | 3/4 |
| C2 | 19.38 | 19.38 | +0.00 | 4/4 | 4/4 |
| C3-original | 14.06 | 14.06 | +0.00 | 2/4 | 2/4 |
| C3-explicit | 16.56 | 16.56 | +0.00 | 1/4 | 1/4 |

```text
Quality /100 (each # approximately 2 points; full scale = 50 #)
C0          1024   9.4 | #####
C0          2048   9.4 | #####
C2          1024  19.4 | ##########
C2          2048  19.4 | ##########
C3-original 1024  14.1 | #######
C3-original 2048  14.1 | #######
C3-explicit 1024  16.6 | ########
C3-explicit 2048  16.6 | ########
```

## Findings and recommendation

- **D01, labels:** some useful naming advice, but repeated confusion about native defaults and invented accessibility APIs. A fluent answer is not dependable implementation guidance.
- **D02, independent controls:** the reference-injected answer explicitly says the switch and button should not be separate focus targets, without preserving equivalent independent actions. This contradicts the provided guidance.
- **D03, deletion:** both reference-injected development answers equate a custom accessibility action with the physical swipe, defeating the question's purpose.
- **D31, layout:** several responses invent `CenteredView`, `.center()` or `.centered()` as built-in SwiftUI solutions. Some fragments are useful, but other answers drift into an accessibility audit instead of centering a view.

The next candidate to test is bounded extraction or selection from supplied evidence, with explicit abstention and deterministic validation—not open-ended Swift code generation. That is a proposal, not an approved next run. These text-only results do not decide the model's image-analysis value.

More output tokens reduced development truncation from 3/16 to 1/16, but did not produce a comparable quality gain. C3 reference reading remained 0/4 accessibility smoke cases and 0/12 development cases. Missing reads are protocol failures, not automatically fabricated-evidence claims.

## Reproducibility and limits

[All 64 grades](grades.json) · [34 text reviews](text-reviews.json) · [Aggregate values](summary.json) · [Provenance](provenance.json) · [Rubric](rubric-snapshot.json) · [Grading policy](grading-policy-snapshot.md) · [Frozen references](grading-evidence-snapshot.json) · [Supplement](supplemental-evidence.json) · [Integrity manifest](manifest.json)

The reviewer knew arm identities and had seen the outputs. Duplicate-text scores were reused after context review. Critical flags record one primary failure per answer, not all possible errors. Apple source review is static; no Swift compilation or simulator/device testing was performed. D31 has no upstream frozen reference, so the explicitly retrospective supplement is essential to interpreting its scores. No independent judge, disagreement analysis, calibrated release threshold or generalization claim is available.

The old generation records are not rewritten with new rubric hashes. New grading provenance is separate. **v3 and further model tests require owner approval.**

</details>

<details>
<summary>Presentation history and integrity</summary>

This owner-approved presentation correction replaces the answer-count index with a per-question comparison and moves aggregate charts into details. Scores, grades, prompts, outputs and v1 are unchanged. [Prior v2 presentation](https://github.com/SerialForBreakfast/SwiftAccessibilityAgentSkill/blob/e43ccd75b954dccb173d8559e498b09d1be2a422/evals/reports/v2/README.md) · [Original v2](https://github.com/SerialForBreakfast/SwiftAccessibilityAgentSkill/blob/19ab7ecf640061dcca272a1145cbd3197d29b316/evals/reports/v2/README.md) · [Frozen v1](../v1/README.md) · [Integrity manifest](manifest.json).

</details>

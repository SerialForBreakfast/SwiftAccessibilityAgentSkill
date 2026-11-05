# Evaluation process review

Reviewed 2026-11-04 against the repository's published v1/v2 evidence. This is a
development roadmap, not a retrospective alteration of frozen release gates.

## Decisions

| Feedback | Decision and safeguard |
| --- | --- |
| No grades exist | Superseded: v2 has 64 retrospective grades over 34 distinct responses. Independent judge execution/calibration is still missing. |
| Real code and atomic criteria | Adopt in a new development catalog revision. Preserve the old questions and heldout set. Start with 15 cases, not an immediate expansion to 120. |
| Primary-source answer keys | Adopt. Each item needs Apple URL, supporting section, retrieval date and availability scope. Repo guidance alone is not independent truth. |
| Binary item grading | Pilot pass/fail/not-assessable plus quote and rationale. Do not assume binary judgments are reliable without calibration. Keep dimension summaries secondary. |
| Cheap deterministic checks | Use as signals, not proof of semantic correctness. An API name can appear in a warning or broken code; alternative valid solutions must pass. |
| Native SDK lane | Qualify on MaxMini; separate incomplete snippets and harness failures from invented APIs. Compiler success is not accessibility success. |
| Headroom screen | Use development-only screening to diagnose value. Keep all four C0/C2 outcome buckets and a representative non-regression set. Report selected-item gains as conditional, never general accuracy. |
| Repeated identical answers | Reuse a grade only with identical effective question/history, response, rubric and evidence hashes. Retain every generation receipt. Equal token counts do not establish identical answers; temperature zero does not guarantee determinism. |
| Missing reads | Flag unread source claims for adjudication. Zero reads alone is not fabricated evidence; abstaining honestly is valid. Evaluate each turn against evidence available by that turn. |
| C0 noise | Report baseline/candidate C0 as A/A, separately from skill effects. Do not mix it into a headline benefit. |
| Wider statistical margin | Do not relax the current 2-point gate after inspecting outcomes. Estimate variance/power using development evidence, then preregister any revised release protocol for future runs. |
| More efficient repetition/OS matrix | Single-repeat bounded pilot; keep canonical release plan unchanged. Later tag version-sensitive cases with rationale and independently verify deterministic repeats. |
| Small-model router / lite skill | Separate hashed experimental arms; preserve canonical C2 and C3. Tiny overflow is useful capability evidence, not a reason to silently replace the skill. |
| Fixed conversation history | Separate replay arm with identical history across releases, alongside free-running continuity. They measure different things. |
| Frontier pricing/models | Treat named models, prices, memory-fit estimates and request-parameter claims in the feedback as unverified. Check official contracts and owner cost approval before selecting providers. |
| Platform-facts block | Use source-reviewed release facts with as-of dates, not an unverified blanket assertion about every Apple OS version. |

## Implementation sequence

1. **Now:** bounded worker qualification/pilots, preserved v2 grades, clear report
   template, and machine-readable pilot accounting. No coordinator or local inference.
2. **Next:** versioned atomic development items. D02/D03/D07/D11/D17/D20/D28/D36/D38
   are first candidates; add code without embedding the expected fix in the question.
   Every item has stable ID, supported alternatives, primary-source evidence,
   expected failure category and review status. Keep answer keys out of model inputs.
3. **Judge implementation:** provider-neutral packet/response contract and offline
   validation first; remote judge adapter after provider qualification. Item records
   contain `itemId`, `pass|fail|not_assessable`, response excerpt, evidence ID and
   explanation. Missing/unparseable responses remain ungraded, never passes.
4. **Calibration:** known-good answers plus single-error mutations and valid
   alternatives, frozen before judging. Measure both error sensitivity and false
   positives, with counts and intervals; 19/20 alone is weak evidence of reliability.
   Independent reviewer adjudicates disagreements and a stratified sample.
5. **Development loop:** C0/C2 screening, source-backed failure triage and affected-case
   reruns plus non-regressions. Preserve all cells. Pin inputs cheaply; do not remove
   provenance simply because the loop is fast. No new hosted runs without cost approval.
6. **Release loop:** freeze candidate, evidence, judge and analysis plan; run heldout
   once the protocol is accepted. Cluster uncertainty by scenario family. Multiple
   items within one answer are correlated, so a naive item-level sign/McNemar test
   must not masquerade as independent evidence. Power analysis may say inconclusive.

## Failure-to-fix loop

Every graded failure should link an excerpt, primary evidence, affected case, proposed
fix owner/path and rerun IDs. These are diagnostic hypotheses, not conclusions from
the C0/C2/C3 pattern alone:

| Category | Investigate |
| --- | --- |
| reference_gap | Missing or wrong supported fact in guidance |
| grounding_failure | Correct supplied evidence misunderstood or ignored |
| routing_miss | Deterministic router selects insufficient evidence |
| retrieval_miss | Model does not retrieve the needed evidence |
| format_fabrication | Claimed consultation unsupported by supplied/read evidence |
| over_trigger | Irrelevant accessibility intervention |
| version_confusion | Incorrect release facts, availability or fallback |
| truncation / context_overflow | Capacity or output policy; retain partial evidence |
| skill_value | C0 fails and supplied evidence helps; preserve as positive evidence |

Keep critical-error categories orthogonal to these diagnoses. A grounding failure
can also hide a necessary action. Report both, without inflating independent counts.

## Remaining work

Atomic case migration, judge adapters, mutation fixtures, deterministic-router and
compact-skill arms, fixed-history replay, and an automated failure heatmap are not
implemented by this review. No release gate, heldout question, runtime skill or
historical report has been rewritten. [Pilot handoff](PILOT-REQUESTS.md) and
[report template](reports/TEMPLATE.md) define the next evidence to collect.

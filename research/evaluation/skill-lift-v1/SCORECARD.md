# Skill-lift diagnostic scorecard

Existing reported grades only; no new model outputs or rescoring. All cohorts are
unqualified for causal skill-lift claims. Inconclusive is not counted as failure.

| Historical cohort | Gain | Regression | Preserved | Persistent failure | Inconclusive | Median input-token change |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| local-gemma4:12b | 0 | 0 | 3 | 3 | 0 | -32.02% |
| local-qwen2.5-coder:14b | 1 | 0 | 0 | 5 | 0 | -30.73% |
| local-qwen3.5:latest | 0 | 1 | 1 | 3 | 1 | -31.78% |
| historical-agy-dev1-dev2 | 0 | 0 | 6 | 0 | 1 | Per-pair input telemetry unavailable |
| historical-claude-dev1-dev2 | 0 | 0 | 6 | 0 | 1 | Per-pair input telemetry unavailable |

Local source grades are provisional and compiler checks are a separate axis. Frontier
rows are historical source-only grades, not native answer validation. No pooled score
or model ranking is calculated. Exact old wrappers/answers are not reconstructed.

## local-gemma4:12b

Diagnostic small-model historical source review, not frontier optimization target. Exact historical task/harness serialization and independent semantic grading not revalidated here; compiler axis remains separate.

| Case | Original baseline grade | Original candidate grade | Transition | Compiler axis |
| --- | --- | --- | --- | --- |
| GP26-01 | gap | gap | persistent-failure | preserved |
| GP26-02 | met | met | preserved | preserved |
| GP26-03 | gap | gap | persistent-failure | regression |
| GP26-04 | gap | gap | persistent-failure | regression |
| GP26-05 | met | met | preserved | preserved |
| GP26-06 | met | met | preserved | inconclusive |

## local-qwen2.5-coder:14b

Diagnostic small-model historical source review, not frontier optimization target. Exact historical task/harness serialization and independent semantic grading not revalidated here; compiler axis remains separate.

| Case | Original baseline grade | Original candidate grade | Transition | Compiler axis |
| --- | --- | --- | --- | --- |
| GP26-01 | gap | gap | persistent-failure | gain |
| GP26-02 | gap | gap | persistent-failure | preserved |
| GP26-03 | gap | gap | persistent-failure | preserved |
| GP26-04 | gap | gap | persistent-failure | persistent-failure |
| GP26-05 | gap | gap | persistent-failure | gain |
| GP26-06 | gap | met | gain | preserved |

## local-qwen3.5:latest

Diagnostic small-model historical source review, not frontier optimization target. Exact historical task/harness serialization and independent semantic grading not revalidated here; compiler axis remains separate.

| Case | Original baseline grade | Original candidate grade | Transition | Compiler axis |
| --- | --- | --- | --- | --- |
| GP26-01 | gap | gap | persistent-failure | preserved |
| GP26-02 | inconclusive | gap | inconclusive | regression |
| GP26-03 | gap | gap | persistent-failure | preserved |
| GP26-04 | gap | gap | persistent-failure | persistent-failure |
| GP26-05 | met | gap | regression | regression |
| GP26-06 | met | met | preserved | inconclusive |

## historical-agy-dev1-dev2

Historical frontier source-only grades; no native answer checks. Inconclusive-to-pass is not fail-to-pass. Raw answers and exact returned model revision are unavailable in this public summary.

| Case | Original baseline grade | Original candidate grade | Transition | Compiler axis |
| --- | --- | --- | --- | --- |
| GP26-01 | meets | meets | preserved | Unavailable |
| GP26-02 | meets | meets | preserved | Unavailable |
| GP26-03 | not-assessable | meets | inconclusive | Unavailable |
| GP26-07 | meets | meets | preserved | Unavailable |
| GP26-08 | meets | meets | preserved | Unavailable |
| GP26-09 | meets | meets | preserved | Unavailable |
| GP26-10 | meets | meets | preserved | Unavailable |

Original reported total-token change: 1%; median change: 3.29%. Conventions are cohort-specific.

## historical-claude-dev1-dev2

Historical frontier source-only grades; no native answer checks. Source grading is preserved, not regraded with operational-1. Full exact matched execution metadata is not reconstructed.

| Case | Original baseline grade | Original candidate grade | Transition | Compiler axis |
| --- | --- | --- | --- | --- |
| GP26-03 | not-assessable | not-assessable | inconclusive | Unavailable |
| GP26-07 | meets | meets | preserved | Unavailable |
| GP26-08 | meets | meets | preserved | Unavailable |
| GP26-02 | meets | meets | preserved | Unavailable |
| GP26-09 | meets | meets | preserved | Unavailable |
| GP26-10 | meets | meets | preserved | Unavailable |
| GP26-01 | meets | meets | preserved | Unavailable |

Original reported total-token change: 1.02%; median change: 3.34%. Conventions are cohort-specific.

## Offline context measurement

Dev.5 vs dev.2, with the same guideline and actual note/reference read bytes:
median -4.89% over 45 mapped rows. Three explicit source gaps remain.
This excludes wrappers/user questions, is not task-frequency weighted, and provides
no provider-token or answer-quality measurement. It does not establish the 15%
focused-input-token target.

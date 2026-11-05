# Evaluation report template

Copy into a new approved report directory. This file is a template, not results.
Replace placeholders only with recorded evidence. Retain v1/v2 untouched. Default
to GitHub-readable Markdown, short tables and linked case pages; no wide transcript
tables, decorative ASCII charts, or fabricated zeroes for missing measurements.

---

# [Question the experiment answers]

**Decision: [supported / not supported / inconclusive / not evaluated].**
[One sentence describing the practical effect and its scope. A higher rubric score
does not imply correct code or accessible user outcomes.]

[Case comparisons](#case-comparisons) · [Failures](#what-to-fix-next) ·
[Method and evidence](#method-and-evidence)

## Run identity

| Scope | Recorded value |
| --- | --- |
| Worker / model / quantization | [verified identity; link to full digests] |
| Comparison | [C0 vs C2, baseline vs candidate, or named experimental arms] |
| Skill and corpus revisions | [hashes; source dates; development/heldout] |
| Coverage | [families; OS contexts; complexity; profile; repeats] |
| Grading | [judge identity; blinded? calibrated? reviewed sample size?] |
| Status | [planned / running / returned / graded / adjudicated] |

## Results that matter

| Measure | Baseline | Candidate | Interpretation |
| --- | ---: | ---: | --- |
| Item pass rate | [passed/assessable] | [passed/assessable] | [family-clustered uncertainty] |
| Assessed coverage | [assessed/planned] | [assessed/planned] | [missing/not-assessable included here] |
| Critical errors | [answers with error/assessed] | [same] | [new/regressed errors linked] |
| Actual C3 retrieval | [read jobs/eligible jobs] | [same] | [actual trace, not ROUTING text] |
| Unsupported source claims | [confirmed/assessed; flagged count separately] | [same] | [adjudicated evidence] |
| Input tokens | [median, sample count] | [same] | [matched completed subset and coverage caveat] |
| Truncated / overflow | [each count/planned] | [same] | [not dropped from denominator] |

Use `unavailable`, `not run` or `not graded` when appropriate. Report weighted rubric
points separately as points, never percent accuracy. For selected headroom cases,
label the conditional gain and show non-regression and harmed-answer buckets too.
Show C0 A/A separately; do not count it as skill benefit. Do not pool distinct models,
context profiles or free-running/replay histories into one headline effect.

## Case comparisons

| Developer question | Without / baseline | With / candidate | Practical difference |
| --- | --- | --- | --- |
| [Exact short question or faithful title](cases/example.md) | [observed failure/success] | [observed failure/success] | [better / worse / unchanged / unassessed, with rationale] |

Show every family for small pilots. For large runs, provide a complete linked index
and state the selection rule for highlighted cases before choosing examples.

Each case page contains the exact effective question and deployment context, source
links and atomic criteria, side-by-side short verdicts, cited response excerpts,
full expandable responses, grades and actual read traces. Keep system prompts and
tool schemas available as linked artifacts. Label criteria `candidate` until calibrated;
label reference answers as authored evidence, never model-generated gold by default.

## What to fix next

| Failure class | Platform | Affected / assessed | Evidence | Proposed change and rerun |
| --- | --- | ---: | --- | --- |
| [grounding_failure, retrieval_miss, etc.] | [platform] | [count] | [case + excerpt + source] | [file/owner/case IDs] |

This numeric matrix is the accessible alternative to a color-only heatmap. Link two
or three representative transcripts per class when available. Classifications are
diagnoses with evidence, not automatic conclusions from condition-level scores.

## Coverage and execution

| Outcome | Count |
| --- | ---: |
| Planned jobs | [N] |
| Completed / truncated | [N / N] |
| Context overflow / unsupported tools / tokenizer unavailable | [N / N / N] |
| Timeout / transport error / unknown outcome | [N / N / N] |
| Worker unavailable / cancelled / missing receipt | [N / N / N] |

Counts reconcile to planned jobs. Add slices by complexity, platform/OS, condition
and context profile; state sample sizes. Record requests/budget, elapsed time, actual
read bytes, output/reasoning tokens and cost where exposed. Never silently estimate.
SDK validation has its own table: compile success, unknown symbol, unavailable API,
incomplete snippet and harness failure; compilation is not a semantic usability test.

## Method and evidence

[Plan and limits] · [Manifest and hashes] · [Effective prompts and responses] ·
[Receipts/read traces] · [Grades and rubric] · [Primary sources] · [Calibration]

State model/runtime/template/settings, OS source as-of date, sampling/repetitions,
duplicate-grade reuse key, paired analysis and uncertainty method. Keep endpoint
details and credentials private. Report reviewer blinding, prior exposure, unsupported
judgments, excluded/missing cases and confounders explicitly. Do not infer hardware
performance from comparisons that change models, quantization or backends.

## Next decision

[Accept bounded next experiment / fix specified failures / collect missing evidence.]
List what remains unknown, the next owner, and whether execution is approved.
Pilot results cannot silently replace preregistered release acceptance gates.

# Skill 0.3.0-dev.1 versus 0.3.0-dev.2 · AGY development screen

**14/14 AGY calls completed · 65,400 tokens · no retries · Claude deferred.**
Requested model: `gemini-3.8-flash-low`, effort low, CLI 1.5.2. Responses do not
independently expose a returned model/revision; the requested model and executable
are pinned. One first answer per case/version, identical question/reference bytes,
balanced order, fresh isolated sessions and disabled tools/paid credits.

## Results at a glance

| Measure | 0.3.0-dev.1 | 0.3.0-dev.2 |
| --- | ---: | ---: |
| Core contracts met | 6/7 | 7/7 |
| Material gaps | 0 | 0 |
| Inconclusive | 1 | 0 |
| Answers with critical flags | 0 | 0 |
| Input tokens | 27,772 | 28,347 |
| Output tokens | 4,765 | 4,516 |
| Cache-read tokens | 0 | 0 |
| Cache-write tokens | Not reported | Not reported |
| Total tokens | 32,537 | 32,863 |
| Median tokens/answer | 4,621 | 4,773 |

These are independent **source-contract grades**, not compile/unit passes or proof of
rendered accessibility behavior. Inconclusive is neither a demonstrated failure nor
a pass. Historical reports and grades are unchanged. Total measured tokens rose
**1.00%** in 0.3.0-dev.2; median answer totals rose **3.29%**.
The predeclared no-median-token-increase screen therefore was not met; no promotion
or proven efficiency improvement is claimed. Output became shorter, but the larger
instruction input offset that saving. No model ranking follows from this sample.

## Question-by-question

These are readable question summaries; exact original code inputs remain in the
[qualified catalog](../../os26/prompts.json) and
[exploratory catalog](../../os26/expansion-1/prompts.json). No raw generated answers
or private mappings are published.

| Question | 0.3.0-dev.1 | 0.3.0-dev.2 |
| --- | --- | --- |
| **GP26-01** · How can the settings row expose its existing switch and Help independently? | Meets | Meets |
| **GP26-02** · How can reconfiguration expose the current customer and status without stale values? | Meets | Meets |
| **GP26-03** · How can a long checkout total support larger text while preserving Pay? | Inconclusive | Meets |
| **GP26-07** · How can dismissal request restoration to the current originating row or fallback? | Meets | Meets |
| **GP26-08** · How can a popup contain accessibility without losing the background hidden state? | Meets | Meets |
| **GP26-09** · How can the volume knob support adjustment while preserving its drag/setter behavior? | Meets | Meets |
| **GP26-10** · How can each download announce only its first terminal result and ignore stale events? | Meets | Meets |

Three cases are existing gold-ready UIKit questions; four remain exploratory.
All seven are known development cases. There are no fresh holdouts in this run.
Read the inconclusive checkout outcome under the accepted R14 limit: source alone
cannot establish whether a horizontal layout meets every long-text requirement.
No mandatory adaptive-axis pattern was imposed; a permanent vertical layout is valid.
Do not turn one inconclusive-versus-met pair into a demonstrated correction rate.

## Identity, references and evidence

All 14 answers included the correct candidate-version introduction and a ROUTING
line. Reference contents were supplied in both conditions; this does not measure
installed skill triggering or autonomous file retrieval. A reporting line is not a
retrieval trace. The independent grader assessed source-honesty wording separately;
any supplied-versus-read ambiguity does not become an invented tool trace.

Both snapshots add owner-approved default-on identity and consulted-file reporting,
with separate opt-outs. Their exact bytes differ from historical letter-named drafts;
prior 18-case comparison totals are not results for these new snapshots.

Two answers did not explicitly distinguish supplied reference contents from an
autonomous read; this is a reporting-provenance caution, not evidence that a read
occurred. Both reuse answers had working primary fixes but misleading optional
prose about reuse-only cleanup. Those cautions reduced quality/calibration assessments
without overriding the correct primary patch. A download answer retained the last
percentage while representing its terminal message elsewhere; this was accepted
under the frozen wording, with spoken semantics unverified.

## Accounting and execution

AGY five-hour remaining quota changed 100%→99%; weekly remained 66%. These rounded
account observations do not establish an exact per-batch charge. All 14 spend-guard
reservations were consumed once. No retries, fallback, renewal or billing signals.
Provider output exposed one turn per answer. Cache reads and thinking tokens were
reported as zero; cache-write telemetry was absent and remains unknown.

The executor retained provider totals for the stop threshold. Its first normalized
receipt did not recognize the installed `cache_read_tokens` field; raw usage remained
intact. The additive offline ledger extracts that field correctly without overwriting
original receipts, adding cache to totals, or making additional calls.

The generation interval was 146.59 seconds from approval receipt to completion receipt;
summed invocation durations were 133.75 seconds. Post-run quota collection and grading
are separate. Claude's 14 planned cells were not called because login is unresolved
and the owner explicitly deferred them. No API key or substitute provider was used.

## Review and limits

An independent review subagent calibrated correct, defective, alternative and
ungradable vignettes before generation, then graded neutral copies of all 14 answers.
Candidate-version text was redacted for grading; originals/hashes remain private.
The reviewer inherited aggregate findings and candidate context, so this is not a
fully blind study or fresh gold-promotion calibration. Protocol version matching was
checked separately with the private mapping. Native answer checks were not run.
The controller accepts alternative implementations and separates quality, protocol,
critical flags and not-assessable criteria. No known incident was relabeled a holdout.

[Controller review](../../../research/evaluation/failure-driven/candidates/CONTROLLER-REVIEW.md) ·
[Version registry](../../../research/evaluation/failure-driven/candidates/README.md) ·
[Machine-readable summary](summary.json)

## Next steps

**Owner:** restore Claude subscription login when convenient; confirm its deferred
bounded run after refreshed account/quota checks. No extra AGY calls are requested.

**Assistant:** preserve this first-run evidence; investigate any concrete issues and
token overhead without mutating these versioned snapshots. Any subject-text change
gets the next semantic development version. Fresh independent families, repetitions,
platform review and the PRD's release gates remain future work requiring separately
bounded approval. Released skill 0.2.2 and frozen baselines remain unchanged.

Only sanitized summaries and research inputs are included here; raw answers,
private mappings and execution receipts remain private. Publication does not
promote either development candidate or change the released skill.

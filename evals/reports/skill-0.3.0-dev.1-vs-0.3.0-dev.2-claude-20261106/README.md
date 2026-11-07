# Claude completion · skill 0.3.0-dev.1 versus 0.3.0-dev.2

**14/14 calls completed · 87,619 reported tokens · no retries or billing signals.**
The requested and returned model is `claude-haiku-5-5`, CLI 2.1.319, effort low.
This completes the original 28-cell comparison: 14 earlier AGY answers plus these
14 Claude answers. No AGY answers were regenerated. Raw answers stay private.

## Results

| Measure | 0.3.0-dev.1 | 0.3.0-dev.2 |
| --- | ---: | ---: |
| Core contracts met | 6/7 | 6/7 |
| Inconclusive | 1 | 1 |
| Material gaps | 0 | 0 |
| Answers with established critical flags | 0 | 0 |
| Uncached input tokens | 14 | 14 |
| Cache-write input tokens | 25,837 | 26,873 |
| Cache-read input tokens | 0 | 0 |
| Output tokens, including thinking | 17,736 | 17,145 |
| Thinking tokens, included above | 10,410 | 10,223 |
| Total tokens | 43,587 | 44,032 |
| Median total/answer | 6,129 | 6,334 |

Both versions meet six source contracts; checkout layout is inconclusive in both.
There is no demonstrated core-quality improvement in this sample. Dev.2 uses
**1.02% more total tokens** and **3.34% more median tokens/answer**.
It misses the predeclared no-median-increase efficiency screen. Neither candidate
is promoted or established as superior. Inconclusive is not a failed implementation.

## Questions and source grades

| Question | 0.3.0-dev.1 | 0.3.0-dev.2 |
| --- | --- | --- |
| **GP26-01** · Expose existing switch and Help independently | Meets | Meets |
| **GP26-02** · Refresh current customer/status on every configuration | Meets | Meets |
| **GP26-03** · Support long checkout totals while preserving Pay | Inconclusive | Inconclusive |
| **GP26-07** · Restore to the current origin after dismissal | Meets | Meets |
| **GP26-08** · Contain popup while preserving prior background state | Meets | Meets |
| **GP26-09** · Add adjustment without losing drag/setter behavior | Meets | Meets |
| **GP26-10** · Announce only the first terminal event for each download | Meets | Meets |

Both checkout answers leave horizontal-layout adequacy unresolved. Source configuration
alone does not prove long-text layout success or failure. No mandatory adaptive-axis
idiom was imposed, and a permanent vertical layout remains an accepted alternative.
Minor optional-prose and source-calibration cautions were scored separately from
working primary patches, including an optional suggestion to change the required
five-point adjustment step. No native answer compile/unit checks ran in this analysis.

Exact original questions/code are in the [qualified catalog](../../os26/prompts.json)
and [exploratory catalog](../../os26/expansion-1/prompts.json). The three qualified
UIKit and four exploratory families are all known development cases, not holdouts.

## Are the skill instructions actually present?

The [payload and announcement audit](../../../research/evaluation/failure-driven/candidates/PAYLOAD-ANNOUNCEMENT-AUDIT-20261106.md)
verifies the exact candidate body in all 28 captured requests, matching prompt/output
receipts, and the correct version identity exactly once on the first line of all 28
answers. ROUTING names the supplied guideline IDs in all 28. Four Claude lines abbreviate
filenames to IDs; two AGY lines omit supplied provenance. Automatic activation and
file retrieval were bypassed by explicit injection, so neither is established.

Frozen GP26-10 receives a SwiftUI state/value reference for a UIKit question. Both
conditions used identical bytes; this is an input-selection limitation, preserved
rather than silently corrected. The current seven-case subset was also largely
solved without skill in the older study. Thus this comparison tests differences
between two guided versions, with little observed headroom, not overall skill lift.

## Relation to the earlier AGY screen

| Model lane | dev.1 source results | dev.2 source results | Total-token change |
| --- | --- | --- | ---: |
| AGY | 6 met, 1 inconclusive | 7 met | +1.00% |
| Claude Haiku | 6 met, 1 inconclusive | 6 met, 1 inconclusive | +1.02% |

Do not pool quality scores or rank the models from these small samples. Neither
comparison includes a no-skill or released-skill control, so neither estimates skill
lift over the bare model. Candidate bodies, question/reference bytes and controller
revision 2 are unchanged across the completion. Conditions alternate order, one
first answer per cell; no new candidate or reference edits were introduced.
The earlier [AGY-only report](../skill-0.3.0-dev.1-vs-0.3.0-dev.2-20261106/README.md)
is preserved. Combined spend-accounting tokens are 153,019, not a pooled quality score.

## Protocol, accounting and quota

All 14 Claude answers announce the correct candidate identity/version and include a
ROUTING line. References were supplied; no autonomous retrieval or installed skill
triggering is demonstrated. Explicit opt-out behavior was not tested.

Claude reports uncached input, cache reads and cache writes separately; total tokens
sum those three categories plus output. Thinking is a subset of output and is not
added twice. This differs from AGY's accounting convention; preserve each raw usage
record. All replies expose the requested model in modelUsage and one turn.

The five-hour quota changed 17%→18% used; weekly stayed 18%. Initial readiness was
16%/17%, but the actual immediately-before readings were 17%/18%; the table/report
uses actual run snapshots. These rounded account readings are not an isolated batch
debit. Extra usage was owner-attested OFF and account-bound; first-party subscription
and no-tool settings were verified. No API route, fallback, retry or new grant renewal.
The 14-call Claude grant is consumed. The 200,000-token stop threshold was not reached.

The quota-reader blocker was a cwd/trust mismatch: /tmp could not complete interactive
/usage. Using the already configured trusted directory resolved it without granting
new trust, changing account settings, copying credentials or invoking a model prompt.
Failed readiness checks remain private harness evidence, not subject failures.

## Independent grading and capture

A fresh review subagent received only the frozen controller and neutral copies of
these 14 answers; version strings were redacted. Prior AGY outputs, condition mappings
and token metrics were withheld. The reviewer knew the provider and controller;
this is condition-neutral source grading, not a fully blind release qualification.
Quality, protocol, critical flags and inconclusive outcomes remain separate. The
mapping-aware version check was performed separately.

Exact CLI prompt strings, settings, responses, usage/finish/intent receipts, controller,
neutral ordering and grading are retained privately. Provider-internal instructions
and full authoring/system/tool context remain explicit capture gaps, not reconstructed
transcripts. The visible grading requests are retained as partial request records.
Released skill 0.2.2, frozen baselines and candidate subject bytes are unchanged.

## Sillycon handoff and next work

The existing 14 AGY first answers were exported to the established private share,
with answer/code bytes unchanged, full relevant inputs/settings/grades and a per-file
hash manifest. Readback verified the archive. Provider conversation IDs were omitted
with original/export hashes; nonempty CLI stderr was omitted with documented hashes.
Credentials/account records and unrelated conversations were excluded.
Coordinator messages 1434/1435 record acceptance/delivery. Latest check: 1435 stored,
read/peer acceptance still unconfirmed. Delivery is not completed native validation.
[Handoff status](../../../research/evaluation/failure-driven/candidates/SILLYCON-AGY-DELIVERY-20261106.md).

Next: obtain Sillycon's verified receipt and first native findings for the existing
AGY scope; review those without silently changing grades/answers. Keep consolidated
campaign/oracle/availability acceptance separate. A future generic/released/candidate
comparison with fresh independent families needs a separate bounded plan. No further
inference, candidate mutation or release promotion follows automatically from this run.

Only sanitized summaries and research inputs are published. Original answers,
mappings and execution receipts remain private; publication is not skill promotion.

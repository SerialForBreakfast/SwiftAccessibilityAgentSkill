# Native skill activation pilot — November 6, 2026

All **12 scored Claude Haiku sessions completed**: four development questions across generic, released **0.2.2** and frozen **0.3.0-dev.2**. No new probe, retries, fallback or generated-code execution occurred. The batch used **113,873 reported tokens** and approximately five minutes including subscription checks. Its grant is closed, with all12 reservations consumed; earlier four attempts remain preserved separately.

## Subscription usage

The owner approved an estimated2–5 percentage points of five-hour usage and roughly0–1 weekly point, with stops at5 additional five-hour points or1 weekly point. Fresh account-bound owner confirmation kept extra usage OFF. Usage was checked after every session.

| Displayed window | Before | After | Visible change |
| --- | ---: | ---: | ---: |
| Five-hour | 0% | 0% | 0 points |
| Weekly | 18% | 18% | 0 points |

These rounded, potentially delayed account-wide readings do **not** establish zero actual subscription consumption or exact batch attribution. The approved allowance was not reached. Prior attempts have incomplete usage telemetry and are not included in this batch's token total.

## Activation is the primary result

| Condition | Relevant questions | Advertised | Invoked/body read | Identity announcement |
| --- | ---: | ---: | ---: | ---: |
| Generic | 3 | 0 | 0 | Not required |
| Released0.2.2 | 3 | 3 | **0** | **0** |
| Candidate0.3.0-dev.2 | 3 | 3 | **0** | **0** |

Across all12 sessions there were **zero tool calls**, no actual reference reads and no ROUTING lines. Both guided general-Swift controls correctly avoided invocation. Generic controls did not advertise the target skill. Guided conditions advertised the same target name with pinned version-specific bodies and identical reference snapshots.

The synthetic native plugin probe previously demonstrated successful explicit Skill loading, an inside file read and an actual outside-read denial. Its earlier turn-limit rejection was a harness accounting error: five content-block events represented three distinct response IDs. The corrected offline replay qualified that narrow path; another live probe was unnecessary. See the [accounting correction](../../../research/evaluation/native-activation-lift-v1/TURN-ACCOUNTING-CORRECTION.md).

**Automatic target-skill invocation did not occur in any of the six relevant guided subjects.** Catalog registration is not proof of a body read. The client's complete provider-internal context is unexposed, so this records observed activation rather than claiming complete knowledge of hidden context. These results compare skill-available workflows; they do not establish that the skill body is ineffective once loaded. The next diagnostic should distinguish explicit invocation from automatic routing before changing accessibility guidance. No further calls are authorized by this report.

## Quality and limits

Independent condition-masked source grading is complete (provisional source judgments):

| Case | Generic | Released0.2.2 available | Candidate0.3.0-dev.2 available |
| --- | --- | --- | --- |
| UIKit cell reconfiguration | Meets | Meets | Meets |
| Validation ownership | Meets | Material gap | Meets |
| Media ownership | Material gap | Material gap | Material gap |
| Swift sorting, negative control | Meets | Meets | Meets |
| **Accessibility cases only** | **2/3 meet** | **1/3 meet** | **2/3 meet** |

All three media answers missed parts of the external-item/callback/cancellation/test contract. The released-available validation answer ignored a newer submit while pending and supplied incomplete tests; the reviewer flagged the lost submit path as critical under the frozen task contract. This describes that answer, not a defect caused by the uninvoked released body. The other validation answers met the source contract through accepted explicit edit/callback integration. Exact supporting excerpts were checked against originals privately; no fabricated native failures are claimed.

Across all12 answers: eight meet, four have material gaps, zero are ungradable, and one has a task-contract critical flag. Including the unrelated sorting control gives generic3/4, released-available2/4 and candidate-available3/4; exclude sorting when discussing accessibility improvement. There is no demonstrated skill-body benefit: none was observed loading. Differences among these single samples must not be attributed to frozen guidance that was not invoked.

The reviewer was independent of answer generation, did not read mapping/usage/protocol records, and saw identity/version/ROUTING-masked answers. Inherited earlier evaluation context makes masking imperfect. This is reviewed development evidence, not release acceptance. Quality, activation and protocol are separate outcomes: a correct answer without loading is not evidence of skill-body improvement. Generated tests are retained as answer text and were **not executed**. The questions are known/context-revised development cases, not independent holdouts; ownership families also test general async programming.

Released0.2.2 here is the current root snapshot pinned to commit8319c230d72f4d6870f3bc6ced9bfab35dc882ba, SKILL SHA256 `2f4ce5ea5a6c8fa7c7cdd08eea620c606eedcc7ae389ac19a493d73078f7c3e3`, not the older archived bytes with the same version label. Both candidate bodies, frozen baselines and released runtime files are unchanged. The baseline checker verifies210 frozen files. Eighteen offline trace/quota/preparation checks passed before launch.

Exact questions, common instructions, settings, original streamed outputs, final usage receipts, native catalogs, source snapshots, owner approval and quota checks remain private under `evals/results/native-activation-lift-20261106-r5/`. Public records contain sanitized analysis only. Full internal provider requests and native tool definitions remain unavailable; authoring/judge capture limits are explicit in the private capture index. See [machine-readable summary](summary.json). No release promotion or Git publication occurred.

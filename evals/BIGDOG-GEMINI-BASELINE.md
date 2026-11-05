# BigDog handoff: Gemini spike to frozen baseline

Status: tasks ready for worker review; no inference performed by this handoff.
Primary target: Gemini 3.8 Flash, subject to verified account availability.
Budget: $0 incremental spend, allocated existing subscription quota only.
Policy and adapter contract: [subscription evaluation](SUBSCRIPTION-EVALUATION.md).

## Request to BigDog

Review this specification, confirm current capacity and supported subscription
access to all three products, then implement and test the offline adapter. Return
qualification evidence and a bounded Gemini spike manifest before execution.
The owner reports that BigDog has subscriptions and promptfoo; confirm rather than
assuming installed versions, quota or idle resources. No coordinator contact.
Deliver reviewed code and sanitized evidence through Git or owner copy/paste.

Do not run another small-model sweep, launch the full campaign, alter runtime skill
guidance, or use paid API credentials. This Mac should not run inference. MaxMini
can later handle approved compile/unit checks, not accessibility UI automation.

## Tasks and acceptance

| ID | Dependency | Task | Completion evidence |
| --- | --- | --- | --- |
| G01 | None | Inspect checkout, frozen roots, promptfoo/client versions and existing results | Capability report, source hashes, offline tests |
| G02 | G01 | Qualify Gemini subscription route and $0 controls; inventory Claude/Codex without generation | Sanitized auth-mode/model/effort/quota report; blockers explicit |
| G03 | G02 | Implement isolated subscription client adapter and offline import | Synthetic tests for conditions, canary isolation, quota/deadline stop, partial outputs, read traces, redaction, no paid fallback |
| G04 | G03 | Integrate with pinned promptfoo or document qualified offline import | Same fixture produces consistent records/assertions; no implicit paid judge |
| G05 | G04 | Freeze small connectivity plan; obtain quota allocation | Exact cells, tool/turn limits, source/settings hashes, stop conditions |
| G06 | G05 | Run connectivity checks | C0/C1/C2/C3 transport and evidence checks; failures retained |
| G07 | G06 | Run stratified Gemini development spike | All planned outcomes and a defect ledger, no heldout access |
| G08 | G07 | Review gold prompts and atomic rubrics | Source-backed revisions in a new catalog overlay, original fixtures preserved |
| G09 | G08 | Calibrate scoring with maintainer and optional independent subscription reviewer | Blinded sample, known-error mutations, disagreement/adjudication log |
| G10 | G09 | Freeze baseline protocol and full coverage manifest | Reviewed hashes, paired ordering, quota chunks, declared analyses |
| G11 | G10 | Collect development baseline incrementally | All 40 families and OS contexts accounted for, all C0-C3 conditions |
| G12 | G11 | Freeze candidate/protocol before heldout access; complete baseline holdout stage | All 20 heldout families accounted for; no tuning from holdout |
| G13 | G11/G12 | Publish reproducible baseline report and sanitized records | Coverage, quality limitations, per-family scores, reads/tokens, failures and provenance |
| G14 | G10 + quota | Run small Claude/Codex comparator batches | Exact models, same fixtures/conditions, separate results and budgets |

G12 can wait until a candidate is ready. Label the earlier artifact a development
baseline, not a full release baseline. G14 does not block collecting Gemini outputs;
independent semantic calibration still gates quality claims. No task is checked off
by this document. Each live batch requires the owner's quota allocation.

## Connectivity and exploratory spike

Connectivity: D01 on OS 27, C0-C3, one repetition, frozen v0.2.2 only: four jobs.
Use separate synthetic qualification probes for read transport, unavailable refs,
and billing/stop safeguards. Forced reads qualify transport, not autonomous routing.
Count probes against the batch budget. Do not launch if zero-spend controls fail.

Proposed spike: 12 development families, one repetition, frozen v0.2.2 only.
Run all four conditions, in balanced randomized order, one clean session per job.

| Families | OS contexts | Why |
| --- | --- | --- |
| D01, D02 | 27 | UILabel and independent controls |
| D13 | 27 | Rotor shortcuts and ordinary navigation for unfamiliar users |
| D18 | 27 | Captions and audio-description discovery |
| D24, D30 | 27 | AppKit and mixed-framework ownership |
| D29 | 27 | visionOS input/accessibility considerations |
| D31, D33 | 27 | Irrelevant trigger and inaccessible reference honesty |
| D36 | 27 | Multi-turn continuity and first-response identity |
| D38, D39 | 26 and 27 | Version-sensitive reading behavior and tvOS text scaling |

This is 14 family/OS cells x 4 conditions = **56 jobs**, plus four connectivity jobs.
These are conversations, not request counts: tools and later turns add requests.
Split the 56 jobs into at least seven separately allocated batches of at most eight.
Generate exact turn/request upper bounds before execution; do not allocate all
future batches automatically. Keep the smoke separate rather than reusing it as a
statistical repetition. Report L1-L4 counts from `complexity.json`; do not infer
complexity from the length of a question.

This subset exercises infrastructure and exposes rubric ambiguity. It is not full
topic coverage. The complete development stage includes focus restoration, reuse,
alternative input, errors, motion, media, keyboard control and all remaining cases.
The current 60-family catalog does not establish dedicated watchOS coverage. Report
that gap explicitly; a watchOS extension needs new source-backed fixtures and a new
catalog revision, not an unsupported all-Apple-platforms claim.

## Gold-prompt iteration rules

Keep questions in ordinary Swift-developer language. Preserve real class names
where natural; do not insert the desired guideline name or expected API into a
question to make retrieval easier. Gemini failures are investigation inputs, not
automatic evidence that a question or grading rule is bad.

For each reviewed family record:

- User intent, platform and deployment context, task complexity and evidence links.
- Atomic required outcomes, acceptable alternatives and critical harmful outcomes.
- Distinct correctness, functional preservation, source honesty and protocol checks.
- Missing context that merits a question or qualified answer; no required boilerplate.
- Rubric defect versus model defect versus adapter defect, with an adjudication.

Use a versioned development overlay and changelog. Keep original questions, outputs
and source hashes. Never quietly fix heldout questions. Confirmed heldout ambiguity
is an exclusion/adjudication record and triggers a future suite revision if needed.
Keep acceptable alternative answers broad enough to avoid rewarding only our style.

Before baseline collection, review at least 12 diverse answers and six deliberate
mutations spanning invented API, incorrect availability, hidden independent action,
fabricated consultation, lost ordinary navigation and unjustified certainty. Freeze
the calibration sample before judging; randomize answer order and hide provider/arm.
Require every critical mutation to be flagged and disagreements to be resolved
against sources. Record agreement by criterion; a small calibration sample is not
proof of universal grading reliability. Recalibrate after substantive rubric changes.

## Full baseline accounting

At the current catalog revision:

| Stage | Family/OS cells | Conditions | Repetitions | Jobs per skill root |
| --- | ---: | ---: | ---: | ---: |
| Development first pass | 80 | 4 | 1 | 320 |
| Development complete | 80 | 4 | 3 | 960 |
| Heldout first pass | 39 | 4 | 1 | 156 |
| Heldout complete | 39 | 4 | 3 | 468 |
| Full baseline | 119 | 4 | 3 | 1,428 |

These are planning counts, not authorization or promised quota availability.
Generate them from the frozen catalog and verify against the manifest. Candidate
runs are separate; both roots total 2,856 jobs before probes and grading. Do not run
the full matrix simply because the portable planner produces it.

Prefer breadth first: one repetition across development, then repetitions two and
three over later approved quota windows. Use reproducible balanced ordering so
conditions are not confounded with a reset or service update. Record dates and
detect client/model drift before each batch. Changed deployments form new strata;
do not claim one pinned revision if the provider does not expose it.

Coverage denominators include failures, unsupported conditions and unattempted
cells. Show platform, OS, topic, complexity, condition and repetition separately.
Never report the spike's 12 families as full coverage. Unknown runtime API behavior
remains a source/SDK follow-up rather than a fabricated grading certainty.

## Conservative Claude and Codex expansion

First use only one independent deployment for the calibration sample if allocated;
the maintainer can review it without model spend. Do not generate a three-model
cross-product by default. For later comparison, choose four frozen development
families before seeing comparator outputs: independent actions, OS-sensitive advice,
unavailable evidence and multi-turn continuity. Use one selected OS context each,
C0-C3, one repetition: **16 jobs per comparator**, split into small approved batches.
Name the exact Claude and Codex models before running. Expand to all 40 development
families only after a useful pilot, new quota allocation and frozen settings.
These small comparator batches are exploratory, not release-grade superiority tests.

## Return package

Use a new directory under `evals/evidence/worker-results/bigdog/` for each original
run, following [the evidence handoff](RESULTS-HANDOFF.md). Include a short readable
summary plus sanitized manifest, effective prompts/answers, tool-read events,
outcomes, settings, source hashes, checksums and redaction log. Keep credentials,
account identifiers, private chats and private reasoning out of Git.

Report planned/started/completed/failed/truncated/unsupported/unattempted counts;
do not equate completed generation with a correct answer. Include actual quota
observations where exposed, incremental monetary charge status, and unavailable
telemetry explicitly. If publication approval allows only a summary, mark semantic
grading from the shared repository blocked rather than declaring it reproducible.

Required report sections: decision summary, frozen inputs, coverage, correctness
and critical errors, actual retrieval, identity/continuity, token/latency telemetry,
quota use, limitations and next bounded request. Preserve prior reports unchanged.

## Before returning implementation

```sh
node --test evals/runner/*test.mjs
node evals/runner/check.mjs
git diff --check
```

Also run new adapter tests with synthetic clients. Demonstrate no-network planning
and no unintended model-backed assertions. Commit scoped changes and return the
hash through the owner's approved delivery route; no force push or image changes.

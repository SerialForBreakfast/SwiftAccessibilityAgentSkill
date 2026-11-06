# Compact skill candidate A: evidence and comparison plan

Status: offline review complete for preparation, 2026-11-05; independent calibration remains pending. No evaluation calls authorized by this plan.

Start with the [offline review and exact 144-call batch](REVIEW.md). Its
[BATCH.json](BATCH.json) is the concrete development proposal; future phases below
are not included in that batch.
The [candidate body](ENTRYPOINT.md) is research text, not a second installable skill.
The root SKILL.md, runtime references, metadata, frozen baselines and prior reports
remain unchanged. This plan complements [ADR-004](../../../adr/ADR-004-platform-aware-accessibility-coverage.md).

## Decision to test

Can one smaller shared entrypoint retain useful evidence discipline while reducing
unjustified changes, wrong-target advice and total token use across frontier models?
Start with a shared candidate. Add no model-specific patches unless later isolated,
replicated evidence shows a recurring model-specific failure and a net benefit.

The [Haiku baseline](../../../../evals/reports/claude-haiku-20261105/README.md) scored
gold13/18→16/18, exploratory15/18→14/18, evidence4/6→6/6, using106060→307756 tokens.
These are single-reviewer source judgments. The skill's benefit is task-dependent;
2.90× total tokens is an observed cost, not a forecast for the candidate.

## Change ledger

| Candidate change | Existing observation / design reason | Benefit to test | Regression to watch |
| --- | --- | --- | --- |
| Require an evidenced defect; allow no change | GP26-11 both conditions invented Slider deficiency; GP26-12 C2 introduced unnecessary fade | Fewer invented defects and unnecessary edits | Missing real semantic defects |
| Resolve platform independently of framework | GP26-04 C0 wrong-platform modifier | Fewer unsupported API recommendations | Excessive clarification or refusal on complete tasks |
| Preserve scope, ownership and behavior | GP26-03 integration/scope failures; optional edits across tasks | Buildable minimal patches, less review burden | Omitting necessary integration changes |
| Retain short evidence distinctions | C2 evidence6/6 versus C0 4/6 | Preserve source honesty with less repetition | False claims of reads, activation or version coverage |
| Consolidate routing and repeated workflow text | Existing entrypoint repeats selection/output rules | Less entrypoint and output overhead | Wrong or missing reference selection |
| Replace mandatory identity/ROUTING/footer with concise citations | Protocol verbosity may contribute overhead; causal benefit not measured | Lower output cost without losing traceability | Weaker evidence disclosure; old protocol checks will differ |
| Keep verification proportional to compile/unit scope | ADR-003 and maintainer boundaries | Actionable contract checks without widening task | Treating a passing unit assertion as user-level qualification |

These are hypotheses, not measured improvements. Candidate A combines changes to test
its overall value; individual causality requires the ablations below. The evidence
ledger is controller-only and must never be included with subject prompts.

## Conditions and isolation

| ID | Subject receives | Purpose |
| --- | --- | --- |
| N | Neutral task, no skill | Same-run model baseline |
| F | Frozen0.2.2 body plus frozen selected reference | Reproduce current injected-reference condition |
| A | Compact candidate body, references unavailable | Instruction-only effect |
| AR | Compact candidate plus the same selected reference as F | Fair candidate/current comparison |

For A, state that lookup is unavailable and retain missing-evidence outcomes. Do not
interpret AR−A as autonomous retrieval quality. In all tool-free conditions, references
are injected by the harness, never represented as a file read. Metadata is held fixed
and recorded; this does not evaluate automatic skill triggering. Existing protocol
checks are recorded separately: candidate A intentionally removes required formatting,
so an old formatting failure is not automatically semantic failure or release approval.

Use identical tasks, rubric, reference bytes, tool access, effort and output limits
within each model. Run fresh sessions, balance condition order and preserve cache
telemetry. Historical results provide context, not substitutes for the new paired cells.
Record exact model/client/version identity; unsupported model pins or limits block the
run rather than allowing fallback. No generated code execution in the model harness.

## Proposed bounded campaign — not yet approved

Prefer the two previously tested subscription routes: AGY and Claude Haiku, subject to
fresh availability, explicit owner authorization and required extra-usage attestation.
No inference is needed to finish preparing or reviewing these artifacts.

1. Development: existing18 cases (12 code,6 evidence) ×4 conditions ×2 models
   ×1 sample =144 calls. Known cases remain development, not new gold or holdout.
2. Optional ablation allowance: at most32 development-only calls, selected by a
   documented rule after the development result. Compare candidate versus removal of
   one rule on the same case/model. Do not alter source-truth or permission constraints.
3. Confirmation:12 independently authored unseen semantic families ×2 conditions
   (F versus the frozen selected candidate) ×2 models ×2 samples =96 calls.

Maximum272 calls across separately approved phases, not one approved campaign.
The exact initial development batch is144 calls. Offline CLI help inspection did
not establish enforceable hard token caps. The original proposed12k-input/4k-output
hard limits are therefore withdrawn for this CLI-route proposal; they are not met.

Instead, request explicit owner acceptance of unknown hard input/output/internal-call
caps before execution. The concrete manifest bounds each prompt at20480 bytes, each
invocation at120 seconds and captured output at1 MiB, with zero application retries
or fallback. A1024-token response target is not a cap. A2-million reported-token
threshold stops further dispatch after a completed call and may overshoot by that
call. Missing usage, uncertain outcome, quota/billing signal, model substitution or
evidence-integrity failure stops dispatch. Preserve unattempted cells. No paid/API
route, undocumented control or alternate model is authorized to avoid this limitation.

No warmups, judge-model calls, repairs or routing pilot are hidden in this budget.
A later tool-enabled routing pilot requires its own plan and approval.

## Fresh cases and oracle readiness

An independent author/reviewer should prepare12 new families, with at most two in
active authoring at once under the existing work-in-progress rule. Proposed composition:
4 UIKit/iOS/iPadOS,3 tvOS,2 macOS/AppKit,2 shared SwiftUI target-bound cases and1 mixed
product-target case. This is a coverage proposal, not available gold evidence. Select
concrete targets and sources before freezing; do not imply comprehensive Apple coverage.

Require explicit target context, realistic starter code, accepted valid alternatives,
critical-error criteria and claim-to-test mappings. Include already-correct code and
insufficient-evidence cases. Compile/unit-contract cases need independently reviewed
native evidence on their actual targets before gold promotion. Evidence-only questions
need an independent factual oracle, not irrelevant native execution. Missing hosts
remain blocked; reduce the approved scope before freezing, never substitute iOS evidence.

Do not expose future holdout prompts/labels to the candidate author. Keep ports of known
incidents in development families; rewording or changing a control name is not a fresh
family. Freeze candidate, sources, all payload hashes, rubric and limits before holdout
execution. No holdout-driven edits or repeated attempts in the same confirmation round.

## Grading and decision rules

Calibrate disputed existing scores before new runs, including Toggle optional polish,
checkout integration and evidence wording. Preserve previous grades; any revised rubric
gets its own version and applies equally to all new conditions. Grade blinded to model
and condition where practical, with protocol/routing assessed separately.

Report per model, platform and family:

- Exact task success and critical errors, including wrong-target APIs/lost behavior.
- Unsupported claims, unnecessary modifications and omissions.
- Proposed versus executed compile/unit checks; blocked and ungradable counts.
- Input, cache read/write, output and reasoning accounting without double counting.
- Total tokens, tokens per successful answer, median input, latency and retrieval cost.
- Actual quota change when observable; API-equivalent estimates are not actual charges.

Do not optimize only tokens per pass: a cheap answer that misses a safety-critical
requirement is not an acceptable trade. Use the existing PRD release gates (including
critical-error review and the2-percentage-point quality non-inferiority margin) for
promotion. A small confirmation set may be too imprecise to satisfy them; that means
inconclusive, not permission to relax the margin. Aggregate/resample by semantic family,
not repeated answer or platform port. Do not claim a causal cross-model ranking.

Decision table:

| Evidence | Decision |
| --- | --- |
| Critical regressions or lost evidence honesty | Reject/revise candidate on development evidence; preserve failed result |
| Comparable quality, materially fewer tokens across qualified models | Candidate for promotion review; retain platform-level checks |
| Better on one model, worse on another | Investigate interaction; no universal replacement claim |
| Benefit attributable to one narrow reference | Keep it on demand, not in shared core |
| Repeated model-specific failure fixed by a small supplement | Propose opt-in exact-model supplement and separately validate unseen families |
| Wide intervals, missing native oracle or inconsistent results | Inconclusive; retain current release and specify next evidence needed |

Ablation selection rule: prioritize a rule associated with both a new improvement and
a possible regression; otherwise test the no-change rule on defective and valid pairs,
then the target-applicability rule. Fix selections and matched comparisons before those
calls. Never tune against confirmation answers. The15% median input reduction remains
an optimization target, not a correctness waiver or assumed total-token saving.

## Work and approvals remaining

- Prepared: offline self-review, candidate text, exact 144-job manifest, private payloads,
  reference/controller hashes, grading interpretations and documented CLI limit gap.
- Independent calibration remains pending; it is not implied by self-review.
- Before execution: bind and verify the bounded runner against the approved manifest.
- Before live development: owner approval of exact model routes and bounded phase.
- Before confirmation: independent fresh cases ready, candidate/rubric frozen, owner
  approval of that exact tranche. No author or worker acceptance is implied here.
- After evidence: decide retain/revise/promote, then separately update runtime files,
  protocol tests, manifests and changelog. Preserve all previous results.

This proposal does not authorize worker messages, scheduling, native execution,
subscription calls, Git publication or installation of the candidate.

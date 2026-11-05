# Subscription-backed frontier evaluation

Status: implementation specification, not a completed adapter or measured baseline.
Owner decision: 2026-11-05. Incremental monetary budget: **$0**.
Execution owner: BigDog. Delivery: Git or owner copy/paste, not coordinator dispatch.
This Mac performs documentation work only. No local inference is requested.

## Objective and boundaries

Measure whether the skill improves a capable Swift coding agent. Begin with Gemini
3.8 Flash through the owner's existing Google/Antigravity entitlement. Reserve
Claude and Codex for limited independent review and later matched comparisons when
the owner allocates spare subscription capacity. Small-model results remain useful
diagnostics, not release targets. Keep runtime skill files, OS 27 research, frozen
baseline contents, heldout questions and existing release gates unchanged.

Subscriptions are not proof of API access, an automation entitlement, a specific
model revision, or remaining quota. BigDog must qualify each supported client route
before generation. Never extract OAuth tokens into a generic API provider, reverse
engineer private endpoints, bypass quotas, or silently switch accounts/models.
If supported subscription automation cannot be established, return a blocker; an
owner-operated export/import lane is an explicitly labeled alternative.

## Three deployment lanes

| Lane | Initial role | Qualification required |
| --- | --- | --- |
| Gemini 3.8 Flash / Antigravity | Primary spike, then broad frozen baseline | Exact selectable model ID, effort mode, client version, subscription sign-in, export/tool trace capability |
| Claude / Claude Code | Small blinded grading sample, later answer comparator | Owner-selected exact model, subscription-backed CLI eligibility, extra usage disabled, structured output and isolation |
| Codex | Independent review or later answer comparator | Owner-selected exact model, ChatGPT sign-in route, no paid fallback, isolated skills/config and export capability |

Claude and Codex name products here, not pinned models. Selection is a worker/owner
preflight task. Do not reuse the old API comparator default merely because it exists.
If a backend revision is undisclosed, record that explicitly alongside the public
model ID and observation dates. Detect selection changes; never pool changed models
into one baseline. Record hidden client/system prompts as uncontrolled factors.

## Zero-spend and quota controls

- Use only owner-approved included subscription capacity. Disable paid overage,
  automatic credit purchases, API-key/Cloud billing fallback and provider fallback.
  Do not change account settings without approval. If safeguards cannot be verified,
  generation is blocked. No purchases or new subscriptions.
- Before each batch, record owner allocation, available quota when exposed, reset
  time, work-capacity reserve and auth mode without identifiers or secrets. Unknown
  quota requires an explicit small owner allocation, not a guessed allowance.
- Default batch ceiling: 8 scenario-condition jobs, serial, 30 minutes, at most
  80 exposed model requests including tools and turns. All ceilings apply together.
  If hidden agent calls cannot be capped, require a qualified client turn limit and
  label internal request counts unavailable; otherwise use owner-operated capture.
- Stop on quota/rate limit, sign-in change, charge warning, unexpected model change,
  unexplained missing trace, or deadline. Preserve partial outcomes. No automatic
  retry, reset-time scheduling, or continuation. Each later batch needs allocation.
- Model-based grading consumes quota too. Disable implicit/default promptfoo judge
  providers, cloud upload and any other unapproved network service. Deterministic
  assertions and offline report generation should require no model contact.

## Adapter implementation contract

Reuse existing scenario, snapshot, receipt and grading formats where possible. Add
a separately named subscription adapter; do not route these runs through the paid
API examples or the llama.cpp-only executor. Qualify the installed promptfoo version
against the repository pin (0.125.1); upgrades require a separate reviewed change.
If promptfoo cannot safely drive the approved client, capture via that client and
import offline. Do not invent CLI flags before checking its installed help/docs.

Expose offline plan, execute-qualified-batch and import/reconcile operations. Tests
must use synthetic client outputs, never real subscription calls. Require:

1. Durable intent before invocation, unique job IDs and output directories, retained
   exact model-visible inputs, raw responses and terminal outcomes.
2. Fresh isolated workspace/session per condition and repetition. Continuity only
   within a specified multi-turn scenario. Disable inherited skills, global rules,
   project instructions, memory, unrelated MCP tools and network research. Verify
   isolation with a synthetic canary; an instruction to ignore files is insufficient.
3. Grading rubrics, expected routes, answers, heldout catalog and sibling conditions
   remain outside the model's filesystem/tool reach. Copy only the approved fixture.
4. C0: generic Swift task, no skill. C1: actual frozen instructions, references
   inaccessible; proposed lookups must not be reported as consulted sources. C2:
   same instructions plus selected reference bytes. C3: same instructions with
   bounded reference discovery/read tools and actual access logs, no forced lookup.
5. Preserve all turns, failures, refusals, truncation and context overflow. No prompt
   shortening or history compaction to make a case pass. If unavoidable client
   compaction occurs, label the installed-agent lane and record it separately.
6. Log exact exported settings, read paths/hashes/bytes, tool events, latency and
   exposed input/output/reasoning tokens. Missing telemetry is unavailable, never
   inferred from routing text. Diagnostic traces omit private reasoning content.
7. Bounded subprocess lifecycle and cancellation; unknown outcomes reconcile
   offline without resubmission. Resume only untouched jobs after fresh allocation.

If the client cannot enforce C0-C3 isolation or provide C3 read evidence, mark that
condition unsupported. A separate native installed-agent experiment can compare
clean skill-disabled/enabled workspaces, but cannot masquerade as controlled C0-C3.
Compare models within the same lane; client differences confound model rankings.

## Baseline and comparison policy

The baseline is the frozen v0.2.2 content, not the current checkout. Gemini spike
outputs are exploratory and excluded from confirmatory results. Once questions,
rubrics, adapter and settings are frozen, generate a new baseline artifact with
their hashes. Later candidate comparisons must use the same protocol and deployment;
collect contemporaneous baseline controls when the service may have changed.

All models use the same public/synthetic fixtures and scoring criteria. Establish
quality before optimizing tokens. Independent Claude/Codex grading is optional until
quota is allocated; maintainer calibration is still required. Gemini must not be
the sole judge of its own answers. Without independent review, publish generation
coverage and deterministic results, not validated semantic quality claims.

Keep the existing 2-point non-inferiority margin, critical-error gates, three
repetitions and family-clustered uncertainty for eventual release evaluation.
Limited pilots do not satisfy those gates. Missing token telemetry prevents a
token-efficiency claim, not honest publication of other measurements.

## Official implementation references

Reviewed 2026-11-05; these explain supported surfaces, not this account's entitlements.

- [Antigravity models](https://antigravity.google/docs/models): qualify the selected
  Gemini model and effort mode rather than assuming a display name pins a backend.
- [Antigravity authentication](https://antigravity.google/docs/install/): account
  sign-in and API-key routes are distinct; use the approved subscription route.
- [Antigravity CLI credits](https://antigravity.google/docs/cli/credits/): inspect
  usage behavior and account settings before allocating a batch.
- [Claude Code programmatic execution](https://code.claude.com/docs/en/headless):
  documents CLI execution; BigDog must separately confirm subscription eligibility.
- [Claude Code costs](https://code.claude.com/docs/en/costs): inspect usage and paid
  credit controls rather than assuming every invocation is included.
- [Codex authentication](https://learn.chatgpt.com/docs/auth?surface=cli): distinguish
  ChatGPT sign-in from API-key authentication before qualifying the client.
- [Promptfoo Google provider](https://www.promptfoo.dev/docs/providers/google/):
  API-provider support does not establish Antigravity subscription integration.

Execution checklist: [BigDog Gemini baseline](BIGDOG-GEMINI-BASELINE.md).

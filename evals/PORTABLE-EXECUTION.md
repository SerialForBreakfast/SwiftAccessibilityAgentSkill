# Portable Evaluation: BigDog and MaxMini

Status: offline requirements/planner ready; remote worker adapter and dispatch require
owner confirmation. The campaign planner performs offline work only. It does not
start or call a model. Worker execution needs separate qualification and authorization.

## What Changed Upstream

Reviewed remote commit `7feac8ae849eb72c1a70b5cc1d31584595603d44` through public
GitHub reads, without Git fetch, merge or checkout changes. Pinned peer reports and
fingerprints are preserved in `evidence/remote-reports/7feac8ae849eb72c1a70b5cc1d31584595603d44/`.
The remote updates predate our local rubric changes; their suite/skill hashes differ.
Do not pool their summaries with the new campaign or silently overwrite local files.

BigDog reports:
- Smoke: 32 baseline/candidate jobs, no transport failures, 12 truncated outputs,
  and no reference reads in the four accessibility C3 cases.
- Development: Qwen3.5-2B Q4_K_M on llama.cpp b11457, 16K context, deterministic
  sampling settings, two output limits, 32 jobs. Both C3 prompt variants produced
  zero reads across 12 accessibility cases. Four outputs truncated across the arms.
- These outputs are ungraded and no held-out run is reported. They establish a
  useful failure baseline, not answer correctness or a reason to discard hard cases.

MaxMini's peer inventory reports M4/24 GB and Apple tooling. Its selected inference
backend, model identity and available capacity are not qualified yet. BigDog's model
must not be equated with a differently named or sized MaxMini artifact. A host change
alone does not establish better reasoning or repair retrieval behavior.

## Three Independent Axes

1. **Task complexity:** L1 focused semantics; L2 multiple interacting requirements;
   L3 version/framework/evidence boundaries; L4 conversation continuity. All 60
   families are classified in `complexity.json`, independent of model size.
2. **Context/output budget:** tiny 4K/512; compact 8K/1024; standard 16K/2048;
   frontier 64K/4096. These are experiment requests, not confirmed host capabilities.
3. **Deployment:** exact model/weights/tokenizer/template/backend/build/quantization,
   thinking mode, sampling and worker identity. Frontier model capability is not
   inferred from context size; a frontier model may also be tested at a tiny budget.

Every profile receives every scenario, version context and C0-C3 condition, for both
baseline and candidate. Unsupported capabilities and overflow are returned outcomes,
not silently omitted cells. Run known-failing C3 cases to retain a regression baseline;
do not relabel C2 injection as model retrieval or force a lookup in the original arm.
Any forced-tool or rewritten-prompt experiment needs a separate arm/version.

Start with one approved model/profile per worker, then add budget sweeps or models as
separate campaigns. Keep answer-generation and independent judging identities separate.
A smaller model can be a useful regression signal without being a suitable final judge.

## Offline Plans and Workload

From a reviewed project checkout, generate portable requirements without inference:

```sh
node evals/runner/campaign.mjs plan --worker bigdog --profile compact --split development > /private/tmp/bigdog-compact-plan.json
node evals/runner/campaign.mjs plan --worker maxmini --profile standard --split development > /private/tmp/maxmini-standard-plan.json
node evals/runner/campaign.mjs plan --worker bigdog --profile tiny --split all > /private/tmp/bigdog-tiny-full-plan.json
```

`all` includes all 60 families. It requests both skill roots, every condition, every
listed OS context and three repetitions: 2,856 jobs per model/profile, at least 3,384
model requests before lookup rounds. This is a workload request, not run authorization.
Development-only is 1,920 jobs. The existing small smoke lane remains the first
connectivity check; record its current manifest rather than assuming old hashes match.

Plans contain stable job IDs, input/rubric/evidence/profile hashes, relative skill-root
locations and actual deployment-context questions. They contain no endpoint, credential
or local user path. Deliver the reviewed source/evaluation bundle alongside the plan;
a plan by itself is not an installed worker or a complete reference bundle.

Reference paths, rubrics, expected outcomes and job metadata are controller fields,
not model instructions. C0 receives no skill; C1 receives no reference contents;
C2 receives its selected contents; C3 receives only the canonical inventory and
the actual read tool. Do not reveal C3's expected paths from the job contract.

Live content fingerprints now exclude `.DS_Store`, matching the upstream portability
fix. The policy is identified as `skill-v2-no-os-metadata`; do not compare its digest
directly to an older digest that included OS metadata. Frozen snapshots and their
manifests are unchanged. Transfer their exact bytes, including any metadata explicitly
listed in the original baseline manifest, and verify them before execution.

Upstream reconciliation note: BigDog retained the original 217-entry manifest as
`manifest.original-with-os-metadata.json` and corrected the operational manifest to
210 source entries, excluding seven absent Finder files. Preserve both manifests;
all source-file hashes are unchanged. Use the operational manifest for worker
verification and the original for historical provenance, as documented in the README.

The planner includes all conditions even if the model cannot use tools. This is
intentional accounting. Do not spend generation requests when a cell cannot be
executed safely: return `unsupported_tools` or `context_overflow` with evidence.

The existing serial runner also accepts `EVAL_PROVIDERS=maxmini` with independent
`MAXMINI_*` environment settings. Its dry run is portable and offline. It remains a
legacy fail-fast execution path, not the full campaign receipt/resume implementation.
The promptfoo config still has its existing provider list; select and validate that
adapter separately rather than assuming the legacy runner's alias filter applies.

## Worker Execution Requirements

BigDog and MaxMini can each execute compatible jobs locally under their own approved
scheduler. No remote model listener or inference process on this developer Mac is
needed. Use each worker's own identity and secret store; never copy another host's
credentials, paths or enrollment defaults.

Before a run, the worker must:
- Verify plan hash, skill roots, suite, rubric, frozen grading evidence and runner
  files. Match approved worker identity and report model/runtime revisions.
- Confirm actual model architecture/blob, tokenizer, chat template/tool parser,
  server build, precision, context configuration, thinking and sampling settings.
- Confirm reserved capacity, serial concurrency, timeout, request limit and output
  budget. Check peak memory/swap and existing workload, not nominal RAM alone.
- Provide exact full-message token preflight, including rendered template, tools,
  history, reference text and reserved output. A character-count heuristic is not
  a fit check. BigDog's upstream llama.cpp development adapter already demonstrates
  `/apply-template` plus `/tokenize`; qualify the corresponding MaxMini backend.
- Preserve full inputs and history for the canonical arm. Do not enable silent
  server truncation, drop earlier turns, shorten the question or swap the model.
- Validate structured tools separately from whether the model elects a useful read.

For each planned cell, return one terminal receipt. Persist request intent before
submission and completed receipts as execution progresses. After a lost reply, record
`unknown_outcome`; reconcile the original job/request ID before replay. A coordinator
resume must reconcile existing receipts and must not silently resample an uncertain job.
The current legacy runner is fail-fast and is not a resumable campaign executor.

Finish reasons, truncation, exact read paths/hashes/bytes, errors and missing telemetry
must be retained. A truncated answer may be graded as a partial answer, but it remains
a truncation outcome. A failed cell can be expected without being counted as passing.
Reported token/capacity metrics and answer quality are separate dimensions.

MaxMini can also run Swift/SDK checks as a separately identified native-validation lane
when its owner authorizes that work. Compiling a test or having Xcode installed does
not establish physical-device VoiceOver behavior. Do not mix native-test receipts with
LLM-answer quality results.

## Receipt Contract and Coverage

The offline coverage importer accepts JSONL. Example failed-cell receipt:

```json
{"planHash":"<plan hash>","jobId":"<planned id>","workerId":"bigdog","modelRevision":"<weights digest>","runtimeRevision":"<backend build digest>","status":"unsupported_tools","generationRequests":0,"referenceReads":[]}
```

Allowed terminal statuses: `completed`, `truncated`, `context_overflow`,
`unsupported_tools`, `tokenizer_unavailable`, `timeout`, `transport_error`,
`worker_unavailable`, `cancelled`, `unknown_outcome`.

A successful reference-read item includes `origin: model-tool`, path, positive byte
count and SHA-256. Mark C2-supplied content as `harness-injection`; it cannot count as
C3 retrieval. Reads of other valid documents are retained separately from reads matching
the expected reference list; an exact filename is not the only acceptable answer.

Return the immutable detailed records as well as receipts: user/assistant turns,
source condition, effective profile/deployment settings, finish reasons, per-request
usage when available and timing. Include cold/warm distinction and memory observations
for host benchmarking. The minimal receipt is accounting, not enough for quality grading.
Do not include credentials or private endpoint URLs in shared reports.

```sh
node evals/runner/campaign.mjs coverage plan.json receipts.jsonl
```

Coverage reports planned/returned/missing counts and outcomes by complexity, profile,
condition, platform, release and stable/beta lane. Missing, overflow, unsupported and
truncated outcomes remain in the planned denominator. Receipt coverage completeness
means every job is accounted for, not that every answer is correct. Judge only against
frozen rubrics and publish scored-pair coverage alongside scores of completed outputs.

## TDD and OS-Maintenance Loop

1. Preserve the current empirical failures as immutable historical observations.
2. Freeze the existing common-case suite and collect both skill roots on each
   qualified model/profile, including failures. Establish test baselines before fixes.
3. Add source-backed OS-change questions to a candidate lane before editing the skill.
   Capture old-skill output with the same model, profile and grading evidence: the red
   baseline may pass if the model already knows the answer; do not fabricate failures.
4. Change source guidance or routing in one stage at a time, then rerun paired cases.
   Confirm old-release advice still works, not just new-release feature recall.
5. Independently grade, adjudicate evidence gaps and compare against the frozen baseline.
   Promote cases to gold after calibration, not because they now pass.
6. Review held-out results only after the candidate and grading policy are frozen.
   If those results inform a fix, replace the affected future holdout and document it.

Report an OS-maintenance dashboard: reviewed changes covered by tests, availability
errors, old-OS regressions, current-OS task scores, unsupported claims, retrieval-read
rate, truncation/overflow, scored/planned coverage and input-token change. State the
source date/build and model/profile so model upgrades cannot masquerade as maintenance
improvement. Quality scores from only easy completed cases are not full-suite results.

## Context Stress and Efficient Variants

Canonical L1-L4 questions stay unchanged across budgets. L4 currently tests moderate
conversation continuity, not a full context-window stress suite. Add an independently
versioned development stress lane with task-relevant history near 25%, 50% and 80% of
measured input capacity, plus a deliberate overflow boundary. Worker tokenization must
count fixed instructions/tools and reserve output; never synthesize completion scores
from a requested occupancy percentage.

Test long histories, several relevant references and irrelevant retrieval separately.
Record signal position, turn count and exact supplied bytes/tokens. Keep identical
histories across baseline/candidate. Do not add padding that states the expected answer.
The stress lane and a compact skill/reference package are follow-up implementation
work, not capabilities claimed by the current planner. Give compact artifacts their own
hashes/arms; do not secretly trim the canonical skill so a tiny model appears to pass.

## Next Dispatch

Current scope: [bounded worker pilots](PILOT-REQUESTS.md), with an offline manifest
from `runner/pilot.mjs`. Delivery is Git or owner copy/paste only; do not contact the
coordinator. The full campaign below remains a later proposal, not pilot authorization.

Send the plan and reviewed source bundle to either worker using the established,
approved project channel. This document does not invent a coordinator API or authorize
installation, server startup, model downloads, paid calls or a large batch.

Ask BigDog to review the full-corpus receipt/preflight contract and adapt its existing
llama.cpp experiment beyond four families, preserving its observed failures. Ask
MaxMini to return its independently verified model/backend capability and propose a
finite trial. Both may run separate shards after identical pins and retry/receipt
semantics are confirmed. Do not duplicate jobs on both hosts unless the experiment is
explicitly a host comparison. No live dispatch has been sent by this change.

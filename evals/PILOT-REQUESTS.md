# Bounded worker pilots

Status: ready for owner delivery through Git or copy/paste. Not dispatched or run.
No coordinator contact. This document scopes the owner's request for bounded pilots;
it does not authorize the full campaign, paid inference, downloads or infrastructure changes.

## Send to BigDog

Please review the latest pushed SwiftAccessibilityAgentSkill evaluation updates and
the feedback disposition in `evals/PROCESS-REVIEW.md`. Read `evals/GRADING.md`,
`evals/PORTABLE-EXECUTION.md`, and this pilot contract. Record your checked-out commit
and any working-tree changes. Preserve existing reports and the original llama.cpp
experiment; do not overwrite them or silently adapt its historical prompt variants.

Confirm the exact available Qwen weights digest, runtime build, tokenizer, chat
template, tool parser, context/output limits, reasoning mode, sampling settings,
available memory and run window. The prior 2B deployment is a useful floor, not an
assumed current capability. Propose an already-present larger model separately;
do not substitute it into the first pilot. Check all execution limits below before
starting. If the adapter cannot enforce them or consume the pinned questions, return
the blocker and required changes instead of starting the old broad experiment.

Once qualified, execute the BigDog pilot below using an already-approved local
inference deployment. Return evidence and receipts in a new worker-specific directory.
No heldout cases, hosted fallback, new model download, blind retries or release claims.
Use Git artifacts or an owner-pasted response, not the coordinator.

## Send to MaxMini

Please independently review the same repository documents and confirm your current
capabilities. Report the checkout commit, actual selected model artifact digest,
runtime/template/tokenizer/tool parser, effective settings, supported context,
memory headroom and run window. Installed tags and total RAM are not qualification.
Use one already-present, already-approved deployment; if none is available, return
`worker_unavailable` with setup needs. Do not download models or start an unapproved
service. No inference belongs on the orchestration Mac.

Once qualified, execute the MaxMini pilot below. Its questions and settings budget
match BigDog, but different weights/backends make this a deployment comparison, not
a claim about host speed or model size alone. Preserve failures and exact settings.
Also report whether you can perform the optional native lane described below.
Return Git artifacts or an owner-pasted response; do not use the coordinator.

## Shared pilot contract

Generate on each worker after receiving this change, from the repository root:

```sh
node --test evals/runner/*test.mjs
node evals/runner/check.mjs
node evals/runner/pilot.mjs bigdog > /tmp/bigdog-pilot.json
# MaxMini uses this instead:
node evals/runner/pilot.mjs maxmini > /tmp/maxmini-pilot.json
```

These commands only plan and validate. They do not execute inference. The existing
generic runner is not a pilot dispatcher. Workers must adapt/qualify execution against
the manifest and `campaign.mjs coverage` contract before starting.

| Boundary | Limit |
| --- | --- |
| Families | D01, D02, D03, D31, D33, D36, D38; development only |
| Comparisons | Baseline/candidate x C0/C1/C2/C3, one repetition |
| OS contexts | 26 for all; also 27 for D38 only |
| Workload | 64 jobs; at least 136 generation requests due to D36 history |
| Requested context / output | 8,192 / 1,024 tokens; exact template/tokenizer preflight |
| Hard generation-request cap | 200 total per worker, including tools, failures and any probes |
| Concurrency / request timeout | 1 / 120 seconds |
| Entire execution window | 45 minutes per worker, including preflight |
| Automatic retries / paid calls | 0 / 0 |

Stop at the first exhausted budget. Preserve partial responses and terminal receipts
for every planned job, including cancelled/unstarted, unsupported and unknown outcomes.
No silent truncation, prompt shortening, tool forcing or context-budget expansion.
Reconcile unknown requests before considering another run. If tokenization is absent,
report `tokenizer_unavailable`, rather than estimating fit. Metadata probes do not
consume the generation cap, but do consume wall time and must be logged.

Keep original bounded C3 behavior. The campaign-wide cap is a safety boundary, not
a new four-read C3 arm. D36 remains free-running and more expensive; fixed-history
experiments require a separate version. Keep expected reference paths and rubrics
controller-side. C2 may inject selected reference text; C3 must select its own reads.

Return: commit, plan hash, model/runtime identities, effective settings, input hashes,
one terminal JSONL receipt per job, complete effective prompts/outputs, finish reasons,
actual read paths/hashes/bytes, reported tokens, request counts and latency. Mark
missing telemetry unavailable. Omit endpoints, credentials and private host details.
Put proposed tracked artifacts under `evals/evidence/pilots/<worker>/<run-id>/`; do not
overwrite a run. Review artifact privacy before committing. Grading remains a separate
lane and must identify judge, evidence revision and calibration status.

## Optional MaxMini SDK lane

After capability confirmation, check at most eight public/synthetic snippets within
15 minutes, serially, using existing SDKs only. Freeze the snippet, explicit wrapper,
compiler/SDK build, target triple and deployment target. Save diagnostics verbatim.
Classify success, unknown symbol, unavailable API, incomplete snippet/missing context,
and harness failure separately. Compilation cannot prove VoiceOver behavior or
functional accessibility. Do not execute generated programs or fetch dependencies.
Report this lane separately from inference tokens, job counts and quality scores.

## Return summary

```text
Worker / checked-out commit:
Qualification: ready | blocked (reason)
Model / weights / backend / tokenizer / template:
Tool support / exact token fit / memory headroom:
Plan hash / settings / limits actually enforced:
Jobs planned / returned / missing, by terminal status:
Generation requests used / elapsed time:
C3 eligible / actual read jobs / unread-source claims:
Artifacts and hashes:
SDK lane (MaxMini): supported | blocked; results:
Next recommended experiment (not executed):
```

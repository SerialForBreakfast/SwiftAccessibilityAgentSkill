# BigDog: independent review and bounded Gemini baseline preparation

Owner request: push checkpoint, have BigDog independently review it, and prepare a
zero-additional-spend Gemini baseline. Review target: **ae4461b80d9a478c861ca6877c9cb2669a78f7b0**.
This packet authorizes review/preflight preparation, not subject inference or account changes.

## One consolidated review

Review the two Mac/TV batches under `code-examples/platforms/`, their nine separate
question/rubric pairs, native manifests, assertions and original failures. Reports:
[initial batch](../platform-expansion-v1/RESULTS.md), [navigation batch](../platform-navigation-v1/RESULTS.md),
[metadata amendment](../platform-expansion-v1-amendment/README.md),
[prompt capture](../prompt-records-v1/CAPTURE-ANALYSIS.md).

Check actual behavior versus claimed coverage, Apple/member availability, valid
alternative implementations, source/prompt/rubric integrity, key-link cleanup and
lifetime-oracle repairs. Audit the amendment without changing original evidence.
Run existing offline integrity tests; use existing native receipts rather than
assuming this grants remote Apple execution. Return one findings report and per-case
accepted / needs-revision / unresolved statuses, with exact paths/hashes and reviewer
identity. Please own technical review; escalate only product ambiguities or spend.
If the original UIKit campaign review remains outstanding, report its owner/status
separately instead of silently treating this narrower review as its acceptance.

## Baseline extension, not a duplicate first baseline

The [existing Gemini report](../../../evals/reports/agy-expanded-20261105/README.md)
already records 72 conversations at `gemini-3.8-flash-low`. Preserve that report and
its original protocol. This proposed extension tests the **nine new Mac/TV cases**;
SwiftUI and earlier frozen questions remain unchanged.

[plan.json](plan.json) specifies 18 proposed single-turn conversations: C0/C2 for each
case, one repetition, serial, three chunks of six. Case-pair order alternates; it is
not claimed randomized. This is development baseline data, not the full release
suite, heldout evidence, a statistically conclusive improvement claim or a C3 routing test.

Each subject JSON contains only exact system/user messages. C0 is generic Swift
assistance; C2 uses the frozen 0.2.2 SKILL.md and selected frozen reference contents,
following the existing runner's inline-reference format. Both conditions receive the
same developer question and explicit platform 26.0 deployment context. That added
context is part of the draft payload review, not a modification of frozen questions.
Subject inputs contain no companion solution, test, rubric, expected route or incident.
The controller plan contains case/condition mappings and must not be exposed to subjects.

## Preflight and stop rules

- Confirm the exact supported subscription model ID, revision disclosure, effort,
  client version, authentication mode, remaining quota when exposed and export limits.
  The reported Gemini model is a preference, not proof it remains available.
- Zero incremental spend: no paid API route, overage, fallback model/account, installs,
  token extraction or private endpoints. If included-only billing cannot be verified,
  stop and return the blocker. Do not change account settings without approval.
- Prepare isolated C0/C2 sessions with inherited skills/memory/project rules/tools
  disabled or explicitly characterize unavoidable provider context. Never run these
  subjects inside this full repository with controller answers available.
- Proposed ceiling: 18 conversations and 18 exposed generation requests; output 4096
  tokens/request; no tools, retries or model judges; concurrency 1; 30 minutes/chunk,
  90 minutes total. If the client cannot enforce single-turn limits or could trigger
  hidden unbounded work, qualify a different supported mode or return a blocker.
- Stop on quota/rate limit, charge warning, sign-in/model change, timeout, missing
  transcript or lost isolation. Retain partial output. No automatic continuation
  beyond the approved total or after a stop condition.
- Review and preflight must complete before execution. Return one ready-to-run
  manifest and a single request for the total subscription allocation. Owner asked
  to prepare this baseline; no inference approval is inferred here.

## Required return

Commit sanitized review findings, preflight evidence and exact payload hashes in a
new report directory. Include native-evidence status and baseline eligibility as
separate fields. For later authorized execution retain every request, output,
finish state, tool/context exposure, token usage and analysis under the
[prompt-record contract](../prompt-records-v1/README.md). Keep raw private transcripts
and credentials outside Git. Grade blinded to condition where feasible; model-based
judging needs its own quota allocation. Do not tune from these answers and label
them holdouts later.

No released skill, baseline, historical result or SwiftUI expansion is authorized.
Preparation: `node research/evaluation/bigdog-platform-review-v1/prepare.mjs` (offline).

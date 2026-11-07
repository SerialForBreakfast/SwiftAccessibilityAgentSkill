# Explicit native invocation comparison — November 7, 2026

Status: **held by the owner**; no new subject-model calls. [Current hold](STATUS.json) supersedes the original proposal’s pending-approval wording. Publication does not authorize running. The original frozen proposal and inputs remain historical records; any future runnable revision must place all workspaces, scratch files and caches inside `evals/results/`, requalify the environment and receive fresh approval.

## Finding and fix

The previous twelve-session run registered the skill correctly: all six relevant guided sessions advertised the canonical target, with its complete nonempty description available in the initialization metadata. Neither the target's metadata nor its settings disabled invocation. Generic controls were isolated. Nevertheless, all subjects answered without a Skill or Read call. No body-loading attempt failed: **automatic invocation was skipped**. Complete provider-internal context and the model's reason for that choice are unavailable, so catalog presence cannot establish what it attended to.

The earlier restricted-mode project-discovery problem was separately corrected through a pinned session-local plugin. A saved synthetic native probe demonstrates successful Skill dispatch, an actual native message carrying the body, an inside read and a denied outside read. This distinguishes discovery, dispatch, body loading and reference retrieval rather than calling all of them “loaded.”

The fix is an explicit native invocation adapter, [explicit_invocation.py](../../../evals/runner/explicit_invocation.py). Guided requests tell Claude to invoke the canonical Skill tool before answering. The initial user request contains the original developer question and invocation instruction, **not the skill body or solutions**. The harness requires both successful native dispatch and an actual native user message containing the complete expected frozen body. Claimed announcements, assistant quotations, a catalog name or a “Launching skill” receipt alone fail that gate. The first guided subject is the counted target-loading check; failure stops the batch without a retry. Final usage and failed proof remain recorded.

This fixes the experiment's enforceable loading path; it does not establish that automatic model selection has become reliable. No speculative description rewrite, released-skill edit, global installation or trust change was made. Native Skill loading is model-invoked; direct invocation is the supported way to avoid discretionary automatic selection. [Anthropic's skill documentation](https://code.claude.com/docs/en/agent-sdk/skills) distinguishes discovery from invocation and describes explicit dispatch; [troubleshooting](https://code.claude.com/docs/en/skills#skill-not-triggering) recommends direct invocation when automatic selection misses.

## Frozen comparison

| Developer question | Generic | Released0.2.2 | Candidate0.3.0-dev.2 | Candidate0.3.0-dev.5 |
| --- | --- | --- | --- | --- |
| UIKit cell reconfiguration | Fresh control | Explicit native call | Explicit native call | Explicit native call |
| Validation callback ownership | Fresh control | Explicit native call | Explicit native call | Explicit native call |
| Media callback/item ownership | Fresh control | Explicit native call | Explicit native call | Explicit native call |

Twelve scored Haiku sessions, no separate probe. Three existing independently reviewed development questions retain their exact wording and alternative-aware controller. The unrelated sorting question is omitted because forcing an accessibility skill onto it would answer a different question. A fresh generic condition supports within-batch comparison; old automatic-run results remain historical evidence, not interchangeable controls.

Released0.2.2 and dev.2 use the same pinned runtime resources as the prior run. Dev.5 is taken from remote commit `b9c0a142575cb70bf43f49fff2be4e25dadd3b93`, with its exact frozen subject body and eight declared runtime task notes; it receives no draft subjects, rubrics, controller, incidents or answer archive. This compares version packages, including retrieval, rather than isolating body wording alone. At preparation time the remote update was fetched and inspected without merging. The checkout is now reconciled with later remote main through `ec389c5`; the original dev.5 source pin remains unchanged. No version is renamed or promoted.

Measure separately: native body proof, actual reference reads and returned hashes/bytes, correct identity/version, truthful routing, quality/critical defects, latency and subscription usage. Independent condition-masked source grading uses the existing controller. Generated code/tests will not be executed; compile/runtime and delivered accessibility behavior remain unproven. Three known tasks cannot establish general release benefit or a model ranking.

## Subscription approval

Estimate **2–5 percentage points of the five-hour allowance**, roughly **0–1 weekly point**, with low confidence. The preceding twelve unloaded subjects showed no displayed increment; actual consumption was unresolved by rounded readings. Explicit body loading and reference reads add context and roundtrips, so the new allowance is conservative, not a known token-to-subscription conversion.

Latest metadata-only reading: **0% five-hour, 18% weekly**. Proposed allowance: stop before another session after **5 additional five-hour points or 1 weekly point**, checking after each subject. Rounded/delayed readings, concurrent account use and one-session overshoot limit precision. Extra usage must remain OFF; the previous owner attestation has expired and will only be renewed after current confirmation.

Retain the finite twelve-subject scope, serial execution, 180-second stuck-process timeout, 60-minute batch window, 2MiB stream capture, read-only Read/Skill tools, no paid fallback, no retries and no additional probe. There is no arbitrary turn/token/tool-count/read-byte gate. See [exact proposal and request hashes](PROPOSAL.json).

## Offline evidence and Sillycon

Twenty-six offline tests pass: stream/quota accounting, explicit invocation/proof rejection cases, exact saved native body replay, prior silent-loading-failure rejection, payload isolation and upstream dev.5 asset pins. All twelve workspace registrations pass initialize-only checks without user queries or model events. The baseline checker verifies210 frozen files. One initial test-oracle newline-convention mismatch was corrected without changing candidate bytes; the failed test record remains private. These are offline checks, not live target-loading or effectiveness results.

[Sillycon updates](SILLYCON-UPDATES.json) records five new remote commits, candidates dev.3–dev.5, SwiftUI/native-forwarding evidence, local analysis tooling and narrow assertion bindings. Sixty draft cases remain unaccepted as independent gold;81 of198 criteria across35 cases have bounded unit links. No new subject-model results were found. The original AGY delivery still has empty read receipts, no confirmed work acceptance and no returned native findings; neither the project inbox after1435 nor the established share supplied a new return. No outbound message, acknowledgment, resend or remote execution was performed.

Exact inputs, settings, source snapshots, executor, native registration metadata, prior trace references, quota observations and unavailable-context notes are private under `evals/results/explicit-invocation-20261107-r1/`. Full provider requests are not exposed and are not reconstructed as if captured.

## Current reconciliation

See the [November7 level set](../RECONCILIATION-20261107.md) for the newer operational-rubric, scorecard, v2 context package and intake checkpoints. Earlier scope/usage observations above describe preparation time, not current quota or new authorization. The twelve-session diagnostic remains held.

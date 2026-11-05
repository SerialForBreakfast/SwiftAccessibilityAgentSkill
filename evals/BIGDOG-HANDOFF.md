# BigDog Handoff: Swift Accessibility Skill Evaluation

Follow-up: [portable full-corpus requirements](PORTABLE-EXECUTION.md) incorporate the
published BigDog smoke/development reports and MaxMini assessment. Keep those known
failures; use the new suite/rubric hashes rather than pooling incompatible runs.

Audience: BigDog deployment owner and evaluation engineer.
Status: deployment discovery and smoke-test request; full runs require approval.

## The Ask

We would like to use BigDog's existing Qwen deployment as a repeatable evaluation
target for Swift Accessibility Agent. Please recommend the least disruptive way
to run a small compatibility test, then a controlled baseline/candidate comparison.

We are not requesting training, fine-tuning, a model replacement, or a public
endpoint. Start with the existing deployment if it supports the API below. Tell us
where the harness should adapt rather than changing production serving behavior
solely for this evaluation.

Repository: https://github.com/SerialForBreakfast/SwiftAccessibilityAgent

Please confirm that the checkout supplied for the run contains `evals/runner/`.
The current local changes may not yet be published to the remote repository.

## Why We Are Doing This

The skill provides source-backed accessibility guidance for Swift developers using
SwiftUI, UIKit, AppKit, tvOS, macOS, visionOS, and mixed frameworks. Its references
include Apple documentation, version-specific guidance, and practical user concerns
such as focus, grouping, independent actions, rotor navigation, and text scaling.

We need to measure whether the skill actually improves responses, rather than just
making a model print the expected identity, routing line, or citations. We also want
to know whether smaller, better-selected references preserve quality while reducing
token use. Current/prior stable OS contexts are evaluated separately from beta cases.

The released identity remains **0.2.2**. The proposed update is **0.2.3-candidate.1**.
We captured a pre-edit working-tree snapshot of 217 files with SHA-256 hashes. It is
not asserted to be a clean release tag. A knowledge-only intermediate snapshot can
separate source updates from instruction/routing changes.

The harness has 17 passing offline tests, but no real model-quality baseline yet.
Some source revalidation and grading calibration remain pending. Treat the first
run as infrastructure validation, not a demonstration of skill effectiveness.

## Experiments

| Condition | Model receives | What it measures |
| --- | --- | --- |
| C0 | Generic Swift-assistant instruction and user question | Unaided answer quality |
| C1 | Actual skill instructions, references unavailable | Instruction effects and honest uncertainty |
| C2 | Actual skill plus selected reference contents | Benefit of supplied knowledge |
| C3 | Actual skill, reference-path inventory, read-only lookup tool | Reference selection, actual reads, and context cost |

For each condition, compare the same deployment/settings against the frozen
baseline and candidate. Run three repetitions of each full-suite case. The suite
contains 40 development and 20 held-out scenario families, with OS-context variants.

Qwen is one evaluation target, not the sole judge of its own answers. We plan a
separate comparator deployment and independent, source-backed grading with a small
maintainer calibration sample. BigDog does not need to host the comparator or judge.

## Information We Need Back

Please return a non-secret deployment summary with these fields:

| Item | Required detail |
| --- | --- |
| Access | Approved execution location, API base URL including `/v1`, VPN/tunnel/firewall requirements, and authentication method |
| Model | Exact served model ID, Qwen family/size/variant, immutable weights revision if available, and tokenizer revision |
| Serving | Server name/version, tool parser, chat template/version, and relevant serving flags |
| Precision | Quantization method/precision and any other deployment transformation |
| Capacity | Configured context limit, supported completion limit, and recommended safe input/output budget |
| Reasoning | Thinking mode, how to control it, where reasoning is returned, and whether its tokens count toward completion limits |
| Sampling | Supported temperature, top-p, seed, penalties, and recommended repeatable settings; identify server defaults |
| Tools | Support for structured function calls and subsequent tool-result messages |
| Usage | Availability and meaning of prompt, completion, cached, and reasoning token counts |
| Operations | Recommended concurrency, rate limits, queue behavior, timeout expectations, maintenance windows and cancellation procedure |
| Privacy | Request/response logging, retention, storage location, authorized access, and whether inputs are used for training |
| Cost | GPU-time or usage constraints, preferred run window, and budget approval contact |

Please provide credentials through the approved secret channel, not in this document,
chat transcripts, repository files, command examples, or evaluation reports.

Also tell us which approach you prefer: run the client from the developer's Mac,
run it beside BigDog inside the approved network, or use an existing approved gateway.
Prefer whichever avoids exposing a new endpoint or altering the shared deployment.

## Current Client Contract

The dependency-free Node runner and promptfoo adapter share the same API client:

- `POST {BIGDOG_BASE_URL}/chat/completions`, with optional bearer authentication.
- Non-streaming chat requests with `model`, `messages`, and `max_completion_tokens`.
- Standard `system`, `user`, `assistant`, and `tool` message roles.
- C3 supplies a function named `read_reference` with a JSON `path` argument.
- Responses need `choices[0].message`, with either final `content` or structured
  `tool_calls`; tool calls need IDs and JSON argument strings.
- Optional usage fields: `prompt_tokens`, `completion_tokens`, and
  `completion_tokens_details.reasoning_tokens`.

The server never opens our files. The client validates the requested reference path,
reads within the selected skill's `references/` directory, and sends the text back
as a tool result. It supplies no shell, network, or write tools to the model.

Current bounds are one concurrent request, a 120-second request timeout, at most
nine model rounds per user turn, and at most eight tool calls per response. There
are no automatic retries or checkpoint/resume support. Completed records survive a
failure, but a rerun requires a new output directory. Please flag if these limits
are unsuitable for the deployment before scheduling larger runs.

If the server expects `max_tokens` instead of `max_completion_tokens`, needs another
reasoning control, or emits reasoning in final content, report that explicitly. We
should make and test a narrow adapter change rather than silently alter the experiment.
Reasoning traces should remain separate from user-visible answers used for grading.

`BIGDOG_EXTRA_JSON` currently accepts only `temperature`, `top_p`, `seed`,
`repetition_penalty`, `frequency_penalty`, `presence_penalty`, `reasoning_effort`, and
`chat_template_kwargs` containing boolean `enable_thinking`. These are supported
client fields, not a claim that every Qwen server accepts them. Use only confirmed
deployment settings. Provider metadata records those settings with each result.

## Recommended Rollout

1. **Discovery:** return the deployment summary and agree on access, privacy,
   limits, completion budget, and a run window. Keep the existing model unchanged.
2. **Compatibility preflight:** verify one plain chat, one structured tool-call
   exchange, response/usage shape, and the chosen thinking settings. Do not silently
   truncate inputs or fall back to a different model.
3. **Qwen-only smoke:** run the 16-job smoke set for one skill root. It covers a
   focused accessibility question and an unrelated UI question across C0-C3 and two
   OS contexts. C3 can add requests. This smoke does not establish multi-turn or
   long-context reliability; check those explicitly before the full run.
4. **Baseline smoke:** repeat against the frozen baseline with identical settings.
   Check evidence traces, usage availability, failures and latency. Agree on feasible
   capacity from observed traffic rather than estimated token counts alone.
5. **Development comparison:** approve the workload and run baseline/candidate,
   optionally adding the knowledge-only stage. Keep artifacts separate and preserve
   model identity/settings. Evaluate correctness before optimizing token cost.
6. **Held-out comparison:** run only after candidate content, rubrics and deployment
   configuration are frozen. Keep held-out questions out of tuning prompts.

If C3 tooling is unsupported, report that as a capability limitation. C0-C2 remain
useful, but do not label injected-reference tests as successful agentic retrieval.

## Workload and Scheduling

Counts below are for **Qwen alone**, per skill root:

| Lane | Jobs | Minimum model requests |
| --- | ---: | ---: |
| Smoke | 16 | 16 |
| Development, three repetitions | 960 | 1,224 |
| Held-out, three repetitions | 468 | 468 |

Tool-call rounds add requests. Baseline plus candidate doubles these counts. The
full Qwen-only comparison therefore starts at **3,384 requests**, before tool rounds,
smoke tests, independent grading, or the optional knowledge-only stage. Adding the
comparator doubles evaluation traffic, but that traffic need not run on BigDog.

These are capacity estimates from the current suite, not authorization to run it.
The dry-run command prints the current count. If capacity is limited, agree on a
smaller development pilot and document its coverage; do not quietly drop failed cases.

## Configuration and Commands

Use the environment contract in [`.env.example`](.env.example). The client does not
automatically load dotenv files. Set the following through your approved environment
or secret manager:

```text
BIGDOG_BASE_URL=<approved base URL including /v1>
BIGDOG_MODEL=<exact served model ID>
BIGDOG_REVISION=<weights/deployment revision>
BIGDOG_SERVING=<server and version>
BIGDOG_QUANTIZATION=<precision or quantization>
BIGDOG_CONTEXT_LIMIT=<configured positive integer>
BIGDOG_REASONING=<confirmed mode>
BIGDOG_MAX_TOKENS=<approved positive integer>
BIGDOG_API_KEY=<supplied privately if required>
BIGDOG_EXTRA_JSON=<confirmed sampling/thinking configuration, or {}>
```

From the supplied repository's project root, inspect and validate without network calls:

```sh
node --test evals/runner/test.mjs
node evals/runner/check.mjs
EVAL_PROVIDERS=bigdog EVAL_SPLIT=smoke node evals/runner/run.mjs
```

After explicit run approval, with credentials configured privately:

```sh
export EVAL_PROVIDERS=bigdog
export EVAL_SPLIT=smoke
export EVAL_RELEASE=candidate
export EVAL_OUTPUT="/approved/private/path/new-unique-run-directory"
export EVAL_ALLOW_NETWORK=1
node evals/runner/run.mjs --execute
```

The output directory must not already exist; its parent must exist and be writable.
Do not use the example placeholder literally. For the baseline, set
`EVAL_SKILL_ROOT` to the absolute path of `evals/baselines/0.2.2/files`, set
`EVAL_RELEASE=baseline`, and choose another output directory. Unset `EVAL_SKILL_ROOT`
when returning to the current candidate.

For held-out runs, `EVAL_FROZEN_HASH` must match the selected skill root's hash,
printed by its dry run. Each root has a different hash.

The dependency-free runner avoids installing promptfoo on BigDog. If the team prefers
promptfoo, the adapter is available and the package pins version 0.125.1. Its CLI
integration and dependency lock still need validation. **`EVAL_PROVIDERS=bigdog` filters
the dependency-free runner only; the current promptfoo config includes both providers.**
Use the dependency-free runner for the first Qwen-only test.

## Results and Acceptance

Return the run manifest, completion/failure summary, and approved local artifact
location. Include provider revision, effective settings, usage-field support,
latency/timeout observations, and any tool-parser or context-limit problems. Keep
endpoint addresses and secrets out of shareable reports.

Infrastructure readiness means both ordinary responses and C3 tool round-trips work,
the model identity/settings remain fixed, outputs are not silently truncated, and
telemetry is either meaningful or explicitly unavailable. Successful connectivity
does not mean the skill improves answer quality.

The skill team owns source review, scenario/rubric calibration, independent grading,
platform regression review and the release decision. BigDog owns deployment access,
serving identity, operational limits and agreed run capacity. Coordinate adapter
changes and run scheduling between both teams.

Release gates require no new critical errors, quality non-inferiority within two
percentage points using paired family-level confidence intervals, and separate
platform review. The token-efficiency target is a 15% reduction on focused tasks
while preserving quality. Qwen-only results support claims about that tested
deployment, not all models or native editor integrations.

## Suggested Reply

```text
Recommended execution location:
Model ID and immutable revision:
Server/version, tool parser, chat template:
Quantization and tokenizer:
Context and completion limits:
Thinking/sampling configuration:
API compatibility differences:
Usage fields and their interpretation:
Authentication delivery method (no secret values):
Logging/retention/access policy:
Concurrency, timeout and scheduling recommendation:
Approved initial workload and contact:
Preferred artifact handoff location:
Open questions or changes requested from the skill team:
```

Further context: [evaluation guide](README.md), [release gates](release-gates.json),
[implementation status](evidence/implementation-status.md), and
[source refresh ledger](../docs/core/source-refresh-2026-11.md).

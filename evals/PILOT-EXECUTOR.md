# BigDog bounded pilot executor

`runner/pilot-execute.mjs` consumes the exact current `planPilot('bigdog')` manifest.
It reuses the canonical evaluator, both frozen roots, all supplied question turns,
and original C0–C3 behavior. It does not run on import or automatically resume.

Before generation, a caller must hold the existing local model lease, verify runtime
and GGUF hashes, reserve memory, and start an approved loopback-only runtime with
8,192 context, one slot, reasoning off, and context shifting disabled. Use the
existing runtime lifecycle; no public listener, downloads or provider fallback.
The caller sets an absolute deadline beginning **before** runtime qualification and
supervises the child process, terminating the child/runtime at expiry. This caller
responsibility is mandatory: the JS network deadline alone cannot stop a hung process.

Allowed source scope: this executor, its test file and this document. Historical
runners/reports are unchanged. The BigDog prospective baseline capture was invoked;
that queue is scoped to the coordinator backlog, not a frozen attempt for this peer
repository change. No reconstructed baseline is claimed.

Generate the plan only after freezing executor sources (runner hashes affect job IDs):

```sh
node --test evals/runner/*test.mjs
node evals/runner/check.mjs
node evals/runner/pilot.mjs bigdog > NEW_PLAN.json
```

Execution requires an owner-approved local deployment configuration and new output
directory. Configuration follows the existing local adapter's `url`, `model`,
`maxTokens`, `extra`, and `metadata` structure; `metadata.runtimeRevision` must name
the verified runtime digest. No key or remote destination is accepted. Configuration
files and raw runtime metadata remain private.

```sh
EVAL_ALLOW_NETWORK=1 node evals/runner/pilot-execute.mjs execute NEW_PLAN.json PRIVATE_CONFIG.json NEW_OUTPUT DEADLINE_EPOCH_MS
```

Two small synthetic forced-tool/return probes share the 200-request budget. These
qualify the parser and tool-result transport, not spontaneous retrieval. Their prompts
are separate from canonical jobs. Every generation, including probes, receives exact
runtime template/tokenizer preflight and an exclusively created, fsynced intent before
contact. Output is reserved in full; overflow is an outcome, never a shortened prompt.
A request is counted before submission and never refunded. Per-call deadlines are the
lesser of 120 seconds and remaining pilot time. Metadata calls consume wall time.

Complete, truncated and overflow outcomes remain in the run. Unknown contact, invalid
responses, tokenizer failure or exhausted budgets stop further contact. The output
contains one receipt per planned job, all effective requests/responses, token-fit
records, source-read evidence and a coverage report. Raw files are bounded to 8 MiB
per response. There are no retries. An existing output directory is rejected.

After an interrupted process, the supervisor must stop its model and run:

```sh
node evals/runner/pilot-execute.mjs reconcile NEW_PLAN.json PRIVATE_CONFIG.json OUTPUT
```

This is offline accounting, **not resumption**. An intent without a persisted response
becomes `unknown_outcome`; unstarted jobs become `cancelled`. Known partial responses
remain on disk. Reconciliation is idempotent and never resubmits any request. Probe
requests are counted separately from job receipts but included in the overall total.
Inspect original operation identities before proposing any subsequent experiment.

Qualification and complete accounting do not establish answer quality. New pilot
artifacts and summaries belong in a new directory, not historical v1/v2 reports.

## First pilot evidence retention correction

The first live pilot used commit `b831905`. Its seven context-rejected bodies were
not saved directly, although their token counts and body hashes were persisted.
They were recovered offline from frozen questions and original model replies, each
matching the original body hash; provenance is explicit in the run bundle. No model
request was replayed. The executor now fsyncs each full input **before** token preflight,
so even tokenizer failures and rejected inputs retain their original bodies directly.
This change does not rewrite the first run or authorize another run.

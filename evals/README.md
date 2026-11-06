# Evidence-Backed Evaluation

## New paired UIKit evidence

[Naming and independent-control tranche](../code-examples/pilots/uikit-naming-v1/README.md):
eight positive unit tests, one compile check and three intended mutant rejections.
Its separate developer question and rubric are development drafts pending independent
review, not additions to the six qualified gold prompts below. See the
[failure-driven work plan](../research/evaluation/failure-driven/TASKS.md) for the
test-to-prompt workflow and remaining gates. The combined offline suite passes172
tests; the115 count below describes the historical gold-closeout checkpoint.

The [closeout supersession record](os26/CLOSEOUT-SUPERSESSION.md) explains why the
earlier local note remains unchanged for provenance while newer review governs readiness.

## Qualified OS26 fixtures

**Gold readiness: 6/6 prompts · 42/42 gates · 6 passing reference fixes · 12/12 detected defects · 115 offline tests passed.**

[Closeout review and frozen grading rules](os26/reports/2026-11-05-gold-closeout/REVIEW.md) · [Machine-readable readiness](os26/reports/2026-11-05-gold-closeout/readiness.json).
Ready for a bounded agy development comparison; no new inference was performed.
Sillycon executed the Apple tests; BigDog reviewed the published evidence and production paths.
Execution used SDK27 with deployment target26 and iOS/tvOS26.5, not a 26.0 runtime.
VoiceOver input, rendered layout and usability remain outside this qualification.
Dedicated coordinator messaging is qualified; enrollment is no longer a blocker.

[Methodology decisions](METHODOLOGY-DECISIONS-2026-11-05.md) · [OS26 promotion protocol](os26/README.md) · [Prior gold audit](GOLD-AUDIT-2026-11-05.md).

**OS 26 first:** [Gold prompts at a glance](../GoldPrompts.md) · [Optimization work packages](NEXT-SKILL-VERSION.md#os-26-first-optimization-proposal). OS 27 integration follows an accepted OS 26 baseline.

**Current diagnostic:** Gemini 3.8 Flash low / skill 0.2.2 · W/T/L **1/4/1** (6 pairs) · guided tokens **1.89×** · suspected API error **1** · compile/device **not run**. Single-reviewer pilot, not a qualified baseline.

New: [Gemini developer-code pilot summary](evidence/pilots/bigdog/developer-code-20261105/README.md)
and [evidence-led next skill version](NEXT-SKILL-VERSION.md). Twelve completed
subscription invocations; preliminary findings, not a release baseline.

New: [local OS26 model and compile/API-gate results](reports/local-os26-model-testing-2026-11-05.md).
This is a zero-spend diagnostic lane covering three Ollama models; raw model and
simulator artifacts remain private and the results do not promote any fixture.
See the [MaxMini findings analysis](reports/local-os26-analysis-2026-11-05.md)
for compiler-probe limitations and implications for the frontier baseline.

Next priority: [zero-spend subscription evaluation](SUBSCRIPTION-EVALUATION.md),
starting with the [BigDog Gemini spike and baseline tasks](BIGDOG-GEMINI-BASELINE.md).
This is a separate, gated frontier lane; do not launch the full portable campaign
or paid API examples below for this work.

Primary target: capable frontier Swift coding agents. Small local models are a
diagnostic lane, not the skill's optimization target. See [target strategy](TARGET-EVALUATION.md).
Current worker action: [commit sanitized existing evidence](RESULTS-HANDOFF.md)
through Git before scheduling more local inference.

For complexity/context profiles and remote execution on BigDog or MaxMini, use the
[portable campaign requirements](PORTABLE-EXECUTION.md). Planning commands perform
offline work only. Model execution belongs to qualified, separately authorized workers.

**[Open the evaluation dashboard →](reports/README.md)** — charts, prompts, expected-answer criteria and response comparisons. New test/report iterations require explicit owner approval.

Deployment coordination: [BigDog handoff and requested setup details](BIGDOG-HANDOFF.md).

Candidate: **0.2.3-candidate.1**. Released identity: **0.2.2**.
The [v2 retrospective review](reports/v2/README.md) grades 64 existing answers from
one small Qwen deployment; independent calibration and release baselines remain pending.
For the next bounded worker runs, use [pilot requests](PILOT-REQUESTS.md).
The immutable snapshot captures the
pre-update working tree, including existing uncommitted content, not a clean Git tag.

## Start Offline

From the repository root, with Node.js available:

```sh
node --test evals/runner/test.mjs
node evals/runner/check.mjs
node evals/runner/run.mjs
```

The last command prints the smoke workload without connecting to any model.
`evals/baselines/0.2.2/manifest.json` verifies 210 source files after the documented
Finder-metadata packaging correction below; the original 217-entry manifest is
retained unchanged. Do not regenerate source hashes in place. Use a new snapshot
directory for future baselines.

## Providers and First Run

Use `evals/.env.example` as the configuration contract. Set environment values in your
own local environment; the scripts do not automatically load a dotenv file. Supply
BigDog's exact model/revision, serving stack, quantization, context limit, reasoning
mode, completion limit, and `/v1` API base. Credentials stay in environment variables.
For Qwen thinking controls or server-specific sampling settings, use EXTRA_JSON only
after checking the actual server contract. Settings must match across compared runs.

The comparator defaults in the example to the previously configured `gpt-5`; verify
availability and exact deployment identity before running. No silent substitutions.
Hosted quantization may be recorded as undisclosed. C3 requires working tool calls.

Inspect request counts before enabling network access. Then, after approving costs:

```sh
export EVAL_ALLOW_NETWORK=1
export EVAL_SPLIT=smoke
export EVAL_OUTPUT=/private/tmp/accessibility-smoke-unique
node evals/runner/run.mjs --execute
```

Run the same smoke against the baseline by setting `EVAL_SKILL_ROOT` to the absolute
path of `evals/baselines/0.2.2/files` and `EVAL_RELEASE=baseline`. Results are local and
include only synthetic/public scenario content. Endpoint URLs and keys are omitted.

Set `EVAL_SPLIT=development` for three repetitions. For held-out runs, first freeze
the candidate using the hash from `check.mjs`, then set `EVAL_FROZEN_HASH` to that hash
and `EVAL_SPLIT=heldout`. Freeze baseline and candidate separately. Do not tune against
held-out failures; turn them into future candidate cases and replace the holdout.
The heldout set is a maintenance discipline, not a security boundary for repo readers.

## Promptfoo

`package.json` pins promptfoo **0.125.1**, verified against its published release page.
Installation is an explicit user action, not part of skill installation:

```sh
cd evals
npm install
npm run eval
```

Review the generated dependency lockfile before adopting it for reproducible CI.
A lockfile is not included because package-network resolution was unavailable here.
The promptfoo adapter and dependency-free runner share the same model/read implementation.
The adapter has offline tests; the installed promptfoo CLI still needs a smoke run.
Use `--no-cache` so repeated samples are fresh. The dependency-free runner never caches.

Legacy `promptfoo/prompts/` files are retained for historical comparison. New runs use
`runner/config.mjs` and load actual SKILL.md/reference contents from the selected root.

## What Is Measured

- C0: generic assistant, no skill or references.
- C1: actual skill with references unavailable; proposed lookup is not evidence.
- C2: actual skill plus selected full references; measures controlled injection.
- C3: actual skill plus filename inventory and bounded read-only lookup; records real reads.

C3 evaluates this harness's reference workflow, not automatic discovery inside every
editor. Native Codex/Xcode integration requires a separate host-adapter smoke test.
Version contexts expand each applicable family into previous/current OS cases; beta
cases remain labeled separately. Families, not repetitions, are statistical units.
The suite contains 40 development and 20 held-out families, all initially candidates
pending grading calibration. OS labels indicate knowledge coverage, not device testing.

Protocol metrics and answer quality are separate. A nonempty response is only a
transport check, never a quality pass. The provider metadata records identity/routing
checks, read paths/hashes, bytes, request count, latency, input/output/reasoning tokens
where reported, and null for unavailable usage/cost. No token estimates are fabricated.
C0 is excluded from skill protocol requirements.

## Blinded Quality Grading

Use the [grading policy](GRADING.md) and `rubrics.json` as the answer-quality contract.

Normalize each run's records.jsonl into a JSON array and combine baseline/candidate
records. Each row already contains provider, condition, family, OS and repeat keys.

```sh
node evals/runner/blind.mjs combined-records.json /private/tmp/new-blind-packets
node evals/runner/score.mjs /private/tmp/new-blind-packets/private-mapping.json grades.json > scores.json
node evals/runner/report.mjs scores.json
```

`packets.json` randomizes A/B order and omits release/model labels. Keep the private
mapping away from judges. Packets include the same frozen reference contents for both
answers from `evidence/grading-evidence.json`. Resolve evidence gaps by adjudication.
Use a judge independent of the evaluated model; do not use Qwen as its own sole judge.
A maintainer checks a stratified calibration sample of at least 12 pairs (all platforms,
C0-C3 and availability/critical-error cases). Record disagreement and revise the rubric
before freezing gold status. This is grading calibration, not manual device acceptance.

Grades have this shape:

```json
[{"id":"packet UUID","judge":"exact judge revision or maintainer identifier",
  "A":{"status":"graded","dimensions":{"correctness":4,"task_success":3,"calibration":4,"relevance":4},"criticalErrors":[],"reason":"Source-backed explanation"},
  "B":{"status":"graded","dimensions":{"correctness":4,"task_success":4,"calibration":4,"relevance":4},"criticalErrors":[],"reason":"Source-backed explanation"}}]
```

Score correctness, completeness, practical task success and evidence honesty. Use the
scenario-specific rubric; ignore branding and wording preferences. Critical errors
include hidden necessary actions, invented APIs, and unsupported availability claims.
Retain original output for separate protocol scoring. Run reports separately by
provider, condition, platform, stable/beta lane, and overall; do not hide regressions
in an aggregate. The paired bootstrap uses 10,000 family-level resamples and requires
three matching repetitions. Smoke results cannot establish effectiveness.

## Release Decision

`release-gates.json` freezes margins before candidate model results. Require package
integrity, calibrated grading, no new critical errors, reviewed platform regressions,
and a 95% interval supporting non-inferiority within two percentage points. Claim
improvement only when the interval excludes zero in the positive direction. Efficiency
target: 15% lower median input tokens on focused tasks, while preserving quality.

No release is automatically approved by the statistical script. Optional ViewLens
fixtures assess runtime evidence interpretation; they do not establish universal
usability. Keep research, observed evidence and inference clearly distinguished.

## Isolating Update Stages

The knowledge-only overlay preserves baseline instructions and manifests. Materialize
it in a new temporary directory to measure source changes before routing changes:

```sh
node evals/runner/stage.mjs knowledge /private/tmp/accessibility-knowledge-unique
```

Set `EVAL_SKILL_ROOT` to that directory for the intermediate run. Compare baseline
against knowledge-only, then knowledge-only against the current candidate. Keep each
comparison's artifacts and grades separate. The overlay has its own content hashes.
The full development + heldout comparison of two skill roots requires at least
6,768 model requests before C3 tool rounds; start with the 32-job smoke suite per root.

## Refreshed Source Candidate

The November source audit is complete at scoped-review level: every source has a
disposition, including historical/discovery and access-limited resources. See the
[claim ledger](../docs/core/source-refresh-2026-11.md). The current candidate corrects
the earlier linked-group availability assumption. Do not overwrite earlier snapshots;
compare their hashes against this refreshed candidate.

Rubric review preserves all 20 held-out questions. Development-only repairs remove
leading multi-turn instructions and supply missing context. Run manifests now hash
the rubric and grading evidence too. Old unanchored grades require regrading.

## Portable snapshots

Finder `.DS_Store` metadata is ignored by Git and excluded from skill fingerprints, reference inventories and staged snapshots. The 0.2.2 manifest originally listed seven absent Finder files; the original manifest is retained as `baselines/0.2.2/manifest.original-with-os-metadata.json`. The corrected manifest explicitly records their exclusion and the original manifest hash. All 210 source-file hashes remain unchanged. This is a packaging correction, not a new skill baseline.

## Local llama.cpp development lane

`node evals/runner/llamacpp-development.mjs` prints the frozen 32-case plan without
model calls. Run its offline checks with
`node --test evals/runner/test.mjs evals/runner/llamacpp-test.mjs`.

The lane uses candidate development families D01, D02, D03 and D31, each at its
first listed OS context. It crosses 1,024/2,048 output tokens with C0, C2, original
C3 and an explicit-lookup C3 instruction. The latter requests exact inventory paths
and actual reads before repository-backed advice, without supplying gold paths or
answers. Tool choice remains automatic. This is prompt development, not heldout
evidence or a release-quality comparison.

Use a separately admitted local llama.cpp process with the pinned model, Jinja tool
parsing, thinking disabled, temperature 0 and seed 42. Configure the existing
`BIGDOG_*` environment contract with a loopback HTTP `/v1` URL, no API key, and the
actual context size. Set `EVAL_ALLOW_NETWORK=1` and a new private `EVAL_OUTPUT`, then
run `node evals/runner/llamacpp-development.mjs --execute`. The BigDog qualification
used 16,384 context tokens; production serving settings were not changed.

Admission and process shutdown belong to the deployment owner; this runner does
not start servers or acquire GPU capacity itself. Every generation is preceded by
llama.cpp template/tokenizer context-fit checks and a persisted request identity.
The lane permits at most 160 generation requests, with one concurrent request and
120-second request deadlines. No retries, fallback or resume occur. A failed run
keeps its completed records and request/response files; reconcile them before a
new experiment. Raw outputs remain private. Reports retain finish reasons and
usage; truncation, missing lookups and nonempty answers do not establish quality.

### Recorded development findings

[Initial smoke](evidence/bigdog-smoke-v1.json): 16 candidate and 16 baseline jobs
completed. Candidate outputs hit the 1,024-token cap in 5/16 cases, baseline in
7/16; automatic accessibility reference lookup occurred in 0/4 C3 cases.

[llama.cpp development v1](evidence/llamacpp-development-v1.json): all 32 jobs
completed. Truncation fell from 3/16 cases at 1,024 output tokens to 1/16 at 2,048.
Neither original nor explicit C3 instructions produced a reference read in the
12 accessibility cells combined. The four unrelated C3 controls also made no reads,
which is appropriate for those controls. C2 supplied references deterministically;
its recorded reads are harness injection, not agentic retrieval.

These small development samples establish an operational evaluation path. They do
not qualify answer correctness, skill improvement, cross-platform performance or
release noninferiority. Next gates are independent source-backed answer grading and
a separately frozen retrieval experiment; do not tune against heldout cases.

## Alternative host assessment

See [Max Mini workload recommendations](MAXMINI-ASSESSMENT.md) for the provisional
host/model comparison, received M4/24 GB peer inventory and remaining verification
plan. That assessment predates the local development batches below.
Those batches do not establish model-quality or performance superiority.

## Maximum-mini Ollama development comparison

The completed local batches use source committed in `14f1f99`. Their raw records
remain in ignored local storage. The merged scenarios and shared runner differ
from those frozen inputs. Keep their original manifests and results unchanged.
Use the original source revision for exact historical continuation. A new run
needs a new output directory and must record the current source and input hashes.
These local diagnostics do not qualify the new portable worker pilot.

The local adapter reuses the frozen 32-case BigDog development plan. Run its
software checks with:

```sh
node --test evals/runner/ollama-test.mjs evals/runner/maxmini-summary-test.mjs
node evals/runner/ollama-development.mjs
```

The dry run makes no model calls. Execution needs an already admitted loopback
Ollama server, the pinned local model, and a new private output directory:

```sh
EVAL_ALLOW_NETWORK=1 EVAL_OUTPUT="$PWD/evals/results/new-local-run" \
  EVAL_DIAGNOSTIC_ONLY=1 OLLAMA_MANIFEST_DIGEST="<owner-verified-manifest-sha256>" \
  node evals/runner/ollama-development.mjs --execute
```

This adapter pins the existing `qwen3.5:latest` model layer by its recorded SHA-256.
The execution owner verifies the blob and serving metadata before running it.
The adapter uses native Ollama chat requests. It keeps thinking off, context at
16,384 tokens, temperature at 0, and seed at 42. It sets neutral repetition and
presence penalties explicitly. Each request permits 120 s. The full run permits
160 generation requests, one at a time. Failed requests stop the run without retry.

The plan contains four development families, eight cells per family. It does not
use held-out cases. C2 loads reference text through the harness. Only successful
C3 tool reads establish model-directed retrieval. Request and response files retain
failed and truncated evidence. A forced tool-call preflight checks transport only.

Ollama and BigDog's llama.cpp use different model weights, rendering, and serving
code. This is a model-and-stack comparison, not an isolated hardware comparison.
The hardened adapter verifies the tag's manifest digest before and after generation
using Ollama's [model listing API](https://docs.ollama.com/api/tags). This digest is
distinct from the historical weights-layer hash. The worker must establish their
relationship and reserve the deployment against concurrent tag/model changes;
before/after checks cannot prove that no transient swap occurred. Historical runtime
metadata remains declared metadata, not independently verified by these checks.

New runs record an absolute deadline (45 minutes for this comparison), cap each
request by remaining time, retain rejected responses and unknown-outcome records,
and fail on absent token telemetry. Continuation requires the original recorded
deadline; legacy manifests without one are refused rather than using file mtime.
New hardened experiments receive separate identifiers. Preserve old records and
source revisions; never retroactively claim these safeguards for old runs.

The adapter checks reported prompt counts after each response. It has no qualified
pre-generation tokenizer check. Review server logs for input truncation or context
shifting before interpreting the run. Keep original server and model metadata.
Execution therefore requires `EVAL_DIAGNOSTIC_ONLY=1`; these adapters still do not
qualify the portable pilot's exact pre-generation token-fit requirement.

Generate descriptive counts with:

```sh
node evals/runner/maxmini-summary.mjs evals/results/new-local-run
```

These counts do not grade answer correctness. Independent source-backed grading
and maintainer review remain necessary. Do not use the release comparison script
for this four-family, one-sample host trial. It requires a different repeated,
paired design. No skill release or accepted accuracy metric changes automatically.

### Next local question batch

`ollama-next-questions.mjs` freezes 8 new development families: D04, D05, D06,
D09, D11, D19, D24 and D30. Each uses C0, C2 and explicit C3 at 2,048 output
tokens. This produces 24 cells. The batch correctly names the operating system
and framework in deployment context. It does not reuse the earlier malformed
framework-as-OS wording. Keep this batch separate from the original comparison.

```sh
node --test evals/runner/ollama-next-test.mjs
node evals/runner/ollama-next-questions.mjs
```

Execution uses `--execute`, `EVAL_ALLOW_NETWORK=1`, and a new `EVAL_OUTPUT`.
It also requires `EVAL_DIAGNOSTIC_ONLY=1` and `OLLAMA_MANIFEST_DIGEST` as above.
The owner first verifies the installed model hash and unchanged serving contract.
The batch permits 120 generation requests, one at a time, with 120 s per request.
A cumulative guard stops new requests after 90 min. Failed attempts are preserved.
No automatic retry or hidden fallback occurs. Hold-out cases remain excluded.

The questions cover UIKit, SwiftUI, tvOS and AppKit. This is broader development
coverage, not platform runtime qualification. Record ambiguous questions for
adjudication. Do not mark a bare answer wrong only because the rubric assumes
an intent that the original question does not establish.

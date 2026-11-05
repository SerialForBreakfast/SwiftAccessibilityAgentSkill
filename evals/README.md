# Evidence-Backed Evaluation

Deployment coordination: [BigDog handoff and requested setup details](BIGDOG-HANDOFF.md).

Candidate: **0.2.3-candidate.1**. Released identity: **0.2.2**.
No model-quality baseline has been measured yet. The immutable snapshot captures the
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

Normalize each run's records.jsonl into a JSON array and combine baseline/candidate
records. Each row already contains provider, condition, family, OS and repeat keys.

```sh
node evals/runner/blind.mjs combined-records.json /private/tmp/new-blind-packets
node evals/runner/score.mjs /private/tmp/new-blind-packets/private-mapping.json grades.json > scores.json
node evals/runner/report.mjs scores.json
```

`packets.json` randomizes A/B order and omits release/model labels. Keep the private
mapping away from judges. Before grading, add the source-backed evidence excerpts
from the reviewed ledger/references to packets; paths alone do not establish truth.
Use a judge independent of the evaluated model; do not use Qwen as its own sole judge.
A maintainer checks a stratified calibration sample of at least 12 pairs (all platforms,
C0-C3 and availability/critical-error cases). Record disagreement and revise the rubric
before freezing gold status. This is grading calibration, not manual device acceptance.

Grades have this shape:

```json
[{"id":"packet UUID","judge":"exact judge revision or maintainer identifier",
  "A":{"quality":0.8,"criticalErrors":0,"reason":"Source-backed explanation"},
  "B":{"quality":0.9,"criticalErrors":0,"reason":"Source-backed explanation"}}]
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

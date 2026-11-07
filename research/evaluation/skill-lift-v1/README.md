# Skill lift, not more test counts

Offline measurement tranche. No model generation, installation, new native example
execution, worker message or spend. Released skill, frozen baselines, candidate
snapshots and previous evidence remain unchanged. This continuation is uncommitted.

## What this adds

- A [historical scorecard](SCORECARD.md) that separates gains, regressions,
  preservation, persistent failures and inconclusive/missing pairs.
- Strict future-pair identity checks for task, model, harness, rubric, platform,
  environment, sampling and token convention; no silent substitution or pooling.
- Family-clustered quality intervals and the existing two-point non-inferiority
  margin, critical-error gates and focused-task token target.
- [Read provenance validation](provenance.mjs): supplied context, captured tool reads,
  offline lookup and routing-only claims remain distinct. It cannot authenticate
  record origin or infer that the answer used the source correctly.
- Twenty-four draft activation questions: 12 relevant, eight near misses and four
  ambiguous requests. Subject files are separate from controller labels; no new
  held-out or qualified gold status is claimed.
- [Static context measurements](context-measurements.json) using actual offline file
  reads; byte differences are not estimated tokens or natural-language routing scores.
- A [milestone design](MILESTONE.md) for a later explicitly approved bounded frontier
  batch and targeted distillation experiments, not an executable provider campaign.

## What the preserved evidence actually says

| Cohort | Descriptive finding |
| --- | --- |
| Local gemma4 | Three source-grade tasks preserved and three still fail; source grades hide separate compiler changes |
| Local qwen2.5-coder | One source-grade fail-to-pass gain, five persistent failures |
| Local qwen3.5 | One source-grade regression, one preserved, three persistent failures and one inconclusive pair |
| AGY dev.1/dev.2 | Six preserved assessable successes; one inconclusive-to-pass remains inconclusive for gain attribution |
| Claude dev.1/dev.2 | Six preserved assessable successes; one inconclusive pair |

These five cohorts are not pooled or ranked. Public summaries preserve old grades,
not complete raw answers or fully matched execution provenance. Native/compiler
checks and source-review quality remain separate. No result for dev.3/dev.4/dev.5
is inferred from historical candidates. There is no new demonstrated frontier lift.

The current dev.5 context comparison is about 4.89% fewer static bytes than dev.2
on 45 same-guideline lookup rows, with three source gaps. That is neither the older
dev.4 comparison nor a 15% token result. User prompts/wrappers are excluded and rows
are not weighted by actual task frequency. Input-token measurements remain unavailable.

## How to use this locally

```sh
node --test research/evaluation/skill-lift-v1/integrity.test.mjs
node research/evaluation/skill-lift-v1/history.mjs > /tmp/skill-lift-history.json
node research/evaluation/skill-lift-v1/context.mjs > /tmp/skill-lift-context.json
```

The comparison module is pure offline arithmetic. Its synthetic tests validate
classification, metadata rejection, family clustering, missing telemetry and gate
logic. They are not new accessibility behaviors or model-performance measurements.
Quantitative gate flags must be supported by actual review artifacts; numeric
eligibility never authorizes a release or a model run. Unknown model/backend versions
stay explicit. A returned provider model ID is not proof of immutable hidden weights.

## Next useful milestone

Finish independent oracle/source review and resolve the three primary mappings.
Freeze representative scenario families, the rubric revision and same-model/harness
comparison payloads. Obtain explicit provider/quota/token/time ceilings once for the
consolidated batch. Then report failures prevented and regressions introduced, before
considering failure-relevant note-removal experiments. Do not trigger evaluation per
commit or optimize for the small local models.

## Validation checkpoint

The complete offline suite passes 1,266 checks, including 87 for this tranche.
[Exact output](offline-checks.log) and [artifact hashes](checkpoint.json) are retained.
The baseline verifier still validates 210 files; the historical verifier validates
87 pins. Protected files match b9c0a14, whitespace checks pass and scoped Markdown
checks report no findings. Check counts validate machinery, not skill lift.

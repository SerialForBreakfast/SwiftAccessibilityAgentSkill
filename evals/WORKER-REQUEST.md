# Worker Request: Portable Skill Baselines

Recipients: BigDog and MaxMini owners. Execution location: approved remote worker,
not the developer's Mac. This packet requests a scoped execution proposal first;
it does not authorize an unbounded campaign or infrastructure changes.

## Context

We reviewed remote source commit `7feac8ae849eb72c1a70b5cc1d31584595603d44`.
BigDog's preliminary generation runs are useful: keep the observed truncation and
C3 no-read outcomes. They are not independently graded quality baselines. Our local
branch now also contains newer anchored rubrics, frozen grading references and
deployment-context corrections. Obtain the reviewed handoff bundle before running;
do not assume remote main already contains these additions.

## Shared Requirements

- Use [the portable campaign contract](PORTABLE-EXECUTION.md) and its pinned inputs.
- Run all question complexities for each approved model/context profile. Every
  question must ultimately have a result or explicit failure/unsupported receipt.
- Keep the same model/template/settings across baseline and candidate; do not
  silently shorten prompts, force retrieval in C3, or count C2 injection as retrieval.
- Measure exact input fit with the runtime tokenizer/template and reserve output.
- Retain finish reasons, partial outputs, actual read traces and missing telemetry.
- Return receipts plus detailed records for independent anchored grading. Known
  failures remain part of the denominator, not an excuse to omit questions.
- Keep generation, grading, native SDK validation and host-performance experiments
  as separate labeled lanes. No paid fallback, installation or new model download
  is implied. Use each host's own identity and approved scheduling route.

## BigDog

Please extend the existing llama.cpp development approach to consume full-corpus
job requirements and produce one terminal receipt per planned job. Preserve the
original C3 arm and label any explicit-tool prompt as a separate experiment.

First return: confirmed tokenizer/template protocol, available context/output limits,
selected weights/runtime/build digests, proposed request/time/memory limits, scheduler
placement, artifact retention and the durable receipt/reconciliation design. The
current local campaign planner does not implement or claim remote dispatch/resume.

## MaxMini

Please confirm one selected model artifact, hash, architecture, backend/tool parser,
available context and current memory headroom. The published inventory is a candidate
capability report, not a qualified endpoint. Suggest either a finite local-inference
trial or a native Swift/SDK lane. Do not describe a differently tagged model as
BigDog's pinned 2B model or infer performance from nominal memory.

## Suggested First Campaigns

Generate these plans offline in the supplied project checkout:

```sh
node evals/runner/campaign.mjs plan --worker bigdog --profile compact --split all > bigdog-compact-plan.json
node evals/runner/campaign.mjs plan --worker maxmini --profile standard --split all > maxmini-standard-plan.json
```

Each describes 2,856 baseline/candidate jobs across all 60 families, C0-C3, OS contexts
and three repetitions. It is not authorization to start that batch. Propose a small
connectivity/fit pilot first, then a finite schedule for the full manifest. If an arm
or profile is unsupported, return an explicit outcome rather than dropping its cells.
Tiny/4K and frontier/64K are additional independent budget profiles, not hardware tiers.

## Please Return

1. Worker identity and independently verified model/runtime/template/settings.
2. Supported profiles, tool/tokenizer capabilities and explicit limitations.
3. Proposed pilot, full-plan request/time limits and run window for approval.
4. Adapter changes needed, their owner, and offline contract-test results.
5. Approved artifact handoff route, privacy/retention and unknown-outcome handling.

After an approved run, return the plan hash, coverage receipts, detailed generation
artifacts and resource observations. Independent grading uses `GRADING.md`; no
quality pass is inferred from nonempty output, tool transport or receipt completeness.

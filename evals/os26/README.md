# OS 26 evaluation: promotion protocol

**6 revised development prompts; 0 validated gold fixtures; provider execution disabled.**

[Readable prompts](../../GoldPrompts.md) · [Methodology decisions](../METHODOLOGY-DECISIONS-2026-11-05.md)

## From draft to real evaluation

1. **Fixture owner:** create a minimal Apple project/host for each prompt, with a
   marked patch region and stable types, callbacks and layout. Pin SDK/build,
   runtime/build, deployment target and input mode. The supplied snippets alone
   are not fixture hosts.
2. **Independent reviewer:** check primary Apple sources and observable assertions
   in `acceptance.json`. Record exact sections, retrieval date and availability.
   Source URLs are candidates, not completed source review. Accept valid alternate
   fixes; no required guideline wording or preferred implementation.
3. **Oracle validation:** build the host; run a reviewed known-good patch and two
   distinct single-error mutations. The good patch must pass and the mutations
   must be rejected. Attach hashed patch identities and check outputs.
4. **Interaction validation:** run the specified unit/manual checks. Automated
   accessibility audits cannot establish complete VoiceOver, Full Keyboard Access
   or tvOS remote behavior. Keep unavailable checks `not_run`/`not_assessable`.
5. **Freeze:** pin this catalog, acceptance criteria, fixtures and references.
   Import reviewed receipts. An offline runnable plan is available only when all
   required gates for all cases have evidence. Partial work remains useful but
   cannot be reported as an accepted fix or gold baseline.
6. **Approve execution:** obtain a separate finite owner-approved subscription
   batch. This module makes no provider call, grants no permission and does not
   select a model or activate the legacy/API runner. Use the qualified subscription
   adapter after the plan is accepted. Agent-native triggering is a separate lane.

Sillycon owns the planned documentation/unit/yearly-version tests per the owner.
The actual Apple host, SDK26 availability, simulator coverage and delivery receipts
remain to be confirmed. This document does not assign work or claim peer completion.

## Offline commands

```sh
node evals/runner/os26.mjs status
node --test evals/runner/os26-test.mjs
node evals/runner/os26.mjs status /path/to/private-evidence.json
node evals/runner/os26.mjs plan /path/to/private-evidence.json
```

Without evidence, status reports six blocked cases and plan fails closed. No flags
permit inference. `modelInput()` returns only the user prompt, not acceptance keys.
Keep receipts, SDK logs and runtime identities private; do not commit native evidence
without the owner's publication approval.

## Receipt contract

A private receipt contains `schema: 1`, `promptHash` and `acceptanceHash` (SHA-256 of
exact JSON file bytes), plus a `cases` array. Each case has `id`, `fixtureAuthor`,
`independentReviewer` (different from author), `sdkBuild`, `runtimeBuild`,
`fixtureHash` and `checks`.

Each check names an acceptance gate `id`, an `observed` value of `pass`, `fail`,
`not_run` or `not_assessable`, and `artifacts: [{path, sha256}]`. Paths are relative
to the receipt directory, confined there including after resolving symlinks. The
known-good and two mutation checks also need three distinct `variantHash` values.
Mutation observations are expected to be `fail`: the broken patch must be rejected.
Every required gate needs matching evidence; duplicate IDs, changed inputs, missing
artifacts or self-only review cannot promote a case.

This validates record completeness and integrity, not the truth of external claims.
An owner/reviewer must inspect the test reports. A fabricated receipt is not evidence.

## Measurement and scope

- Separate representative cases, targeted failure/regression cases and correct-code
  controls. Do not discard all cases C0 passes; report headroom-selected results as
  conditional results. GP26-04 is explicitly a known regression, not fresh heldout.
- Collect atomic pass/fail/not-assessable results with evidence. A plausible answer,
  substring match or compiler success alone is not full task success.
- Keep ordinary requirements visible to every arm. Remove solution hints and the
  boilerplate answer suffix; changing a system wrapper requires a separately named
  comparison, not relabeling old scores.
- Current cases are development-only. Hold out new families from candidate tuning
  with controlled access and access records. A public test is not automatically
  contaminated, but publication alone cannot establish uncontaminated evaluation.
- Use one declared OS26 environment for stable cases. Add OS27 delta cases only
  after OS26 acceptance, as directed by the owner. No duplicated OS labels merely
  to increase sample counts.
- Report per-case repeats and family-level paired outcomes; repeated samples are
  not independent families. Three samples give very wide uncertainty. Do not claim
  formal noninferiority from small descriptive runs.
- Existing release gates and historical reports remain frozen. A new release
  protocol needs preregistered endpoints, precision/power assumptions and explicit
  approval before candidate runs. This development readiness gate is not a release
  gate and does not relax the old one.

Next-version implementation remains gated on this baseline. Compact instruction,
reference, trigger and input-mode changes are proposals, not deployed skill changes.

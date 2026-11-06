# OS 26 evaluation: promotion protocol

**6 revised development prompts; 0 validated gold fixtures; provider execution disabled.**

Current revision: `os26-code-contract-4`. Owner-approved endpoint: compile/unit
evidence plus independent source review. No mandatory manual verification or UI
tests. Prior draft-2 inputs and policy are retained in `archive/os26-draft-2/`.
Question text is unchanged; acceptance hashes and the measured endpoint changed.
Full VoiceOver, keyboard/remote interaction and rendered-layout outcomes are
unassessed, not implied by code-contract promotion.

[Readable prompts](../../GoldPrompts.md) · [Methodology decisions](../METHODOLOGY-DECISIONS-2026-11-05.md)

Current execution dependencies and coordination receipt:
[baseline closeout checklist](BASELINE-CLOSEOUT.md).

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
4. **Code-contract validation:** run the specified unit checks and source review.
   Review native-control wiring separately from direct handler/state assertions.
   Do not substitute a manual check or source inspection for a unit mutation kill.
   Keep unavailable unit checks `not_run`/`not_assessable`; they block promotion.
5. **Freeze:** pin this catalog, acceptance criteria, fixtures and references.
   Import reviewed receipts. An offline runnable plan is available only when all
   required gates for all cases have evidence. Partial work remains useful but
   cannot be reported as an accepted fix or gold baseline.
6. **Approve execution:** obtain a separate finite owner-approved subscription
   batch. This module makes no provider call, grants no permission and does not
   select a model or activate the legacy/API runner. Use the qualified subscription
   adapter after the plan is accepted. Agent-native triggering is a separate lane.

Sillycon owns documentation/unit/yearly-version design; native execution scheduling
requires a separately approved Apple worker and resource allowance.
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

Each check names an acceptance gate `id`, a `method` of `review`, `compile` or `unit`
(oracle gates require `unit`), an `observed` value of `pass`, `fail`,
`not_run` or `not_assessable`, and `artifacts: [{path, sha256}]`. Paths are relative
to the receipt directory, confined there including after resolving symlinks. The
known-good and two mutation checks also need three distinct `variantHash` values.
Mutation observations are expected to be `fail`: the broken patch must be rejected.
Every required gate needs matching evidence; duplicate IDs, changed inputs, missing
artifacts or self-only review cannot promote a case.

The existing SwiftUI mutations include input/focus-oriented defects. They remain
unvalidated and may require a versioned replacement with unit-observable defects.
Do not count a source-inspection finding as an executed mutation failure. Record
old/new fixture hashes and preserve old variants before making that change.

Revision4 implements that change: production-path action/binding tests and
unit-observable dropped/duplicate/wrong-ID/inverted-write mutants replace the
SwiftUI input/focus variants. Draft3 is preserved in `archive/os26-code-contract-3/`.
See [source/assertion review](SOURCE-REVIEW-R4.md). Independent review and native
results are still required. `runner/os26-native.mjs` prints a plan without flags;
its explicit execution mode requires a new output directory and installed iOS26/
tvOS26 destination UUIDs. It runs serially with a ten-minute per-job timeout, no
UI targets, no downloads and no inference. Output contains private local paths.

This validates record completeness and integrity, not the truth of external claims.
An owner/reviewer must inspect the test reports. A fabricated receipt is not evidence.

### Unit execution evidence

Every `unit` check (including each oracle check) also supplies `execution`:
`buildOutcome: "pass"`, `testSuiteHash`, nonempty unique `executedTestIds`,
`failedTestIds`, and `outcome` (`passed` or `assertion_failed`). A passing check
has no failed tests. An expected mutation failure supplies nonempty unique
`expectedFailureTestIds` matching exactly the observed failed tests. Predeclare
these expected IDs in the reviewed mutation specification before running; review
the logs against that specification rather than accepting self-reported claims.
All three oracle variants must use the same suite hash and executed test selection.
Build errors, crashes, timeouts, skipped/zero-test runs and unrelated assertion
failures cannot qualify as mutation kills. Receipts missing this evidence remain
blocked; existing successful synthetic tests are not native validation.

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

## Fixture preparation

Latest [native validation report](reports/2026-11-05-r4/README.md): all six candidates
passed and twelve mutations failed as intended on recorded OS26.5 runtimes.
Independent review is pending; zero cases are promoted and Gemini has not run.

[Six candidate implementations and twelve mutations](fixtures/README.md) are
prepared with a dependency-free Swift package and six focused UIKit/SwiftUI unit
tests. The native runner uses the package scheme; no separate app project or UI
tests are required. See dated validation reports for actual execution outcomes.
Independent review remains a separate promotion requirement. The receipt assembler
keeps that gate pending rather than inferring approval from passing tests.

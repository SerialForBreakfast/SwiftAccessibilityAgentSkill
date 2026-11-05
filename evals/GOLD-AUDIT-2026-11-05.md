# Gold readiness audit and next decisions

Follow-up: owner confirmed unit-only scope. `os26-code-contract-3` now replaces
manual gates with scoped unit/source-review criteria and rejects manual/UI receipts.
Draft-2 remains archived. Findings below record the inspected pre-change state;
native evidence and suitable unit-observable mutation coverage remain pending.

Inspected revision: `29fc48b`. Scope: static review of all 40 legacy development
questions/criteria, six OS26 code fixtures, promotion logic and ADR-003. Heldout
content was not revised. This is not a new Apple source audit or native test run.

## Findings, ordered by baseline impact

1. **Promotion currently depends on work outside the agreed unit-only scope.**
   `os26/acceptance.json` requires manual interactions for five of six cases.
   `os26/fixtures/README.md` also proposes XCUITest targets. ADR-003 explicitly
   excludes UI automation; the maintainer has rejected mandatory manual validation.
   Do not fake those receipts or silently waive the gates. Create a separately
   versioned code-contract lane with compile/unit assertions and source-backed
   answer review. Keep full interaction claims unassessed in that lane.
2. **Two live-looking workload plans conflict.** The older Gemini handoff proposes
   a 56-job multi-OS spike; the newer methodology chooses six OS26 code cases first.
   Prefer the newer OS26-first decision. Preserve the 60-family suite for historical
   comparison and eventual breadth, not as an automatic parallel run authorization.
3. **No fixture has validated oracle evidence.** The offline gate reports 0/6 gold
   ready. Three UIKit unit tests are authored; SwiftUI cases 04-06 lack executable
   unit coverage. Compiling a host or hashing mutations cannot establish that the
   intended assertion detects each mutation.
4. **Some mutation requirements exceed the stated user task.** GP26-05's second
   mutation introduces focus resets on state updates, but its prompt does not state
   update-time focus preservation. Treat that as an explicit new regression case or
   disclose the requirement in a versioned prompt; do not penalize an answer for
   an undisclosed product constraint. Unit state policy is not remote focus evidence.
5. **The legacy rubrics remain broad, not calibrated gold.** Many reuse a generic
   concrete-next-step criterion. D04 admits several valid navigation strategies;
   D09 need not insist every label be an imperative; D11 must accept alternative
   groupings that preserve functions. D31 measures relevance with a loaded skill,
   not automatic triggering. Keep protocol and quality scores separate.
6. **Coverage is uneven.** Six OS26 fixtures cover UIKit/SwiftUI iOS and tvOS, not
   AppKit, visionOS or watchOS. The older corpus adds macOS and limited visionOS,
   but not dedicated watchOS coverage. Six cases cannot substantiate all-platform
   effectiveness. Do not inflate coverage by repeating stable questions per OS label.

## Six-case disposition

| Case | Useful code-contract evidence | Remaining boundary |
| --- | --- | --- |
| GP26-01 | Public row/child configuration; switch and Help callbacks independently invoked | No claim of observed VoiceOver traversal |
| GP26-02 | Reconfiguration A/B/A/B updates label/value without relying on reuse | Strong first pilot; native compile/unit records and independent review pending |
| GP26-03 | Scaling configuration, constraint/policy prerequisites, payment callback | Prerequisites do not prove visible layout or full text at every size |
| GP26-04 | Explicit deletion handler targets correct ID once; nonactivation path does nothing | Calling a handler does not prove SwiftUI keyboard/gesture wiring |
| GP26-05 | Stable IDs and activation routing; compile public native-control construction | Focus navigation is not a unit-test assertion; split unsupported interaction gate |
| GP26-06 | Binding/state round-trip where genuinely exercised; reviewed no-op control | Do not invent a required fix; source presence is not observed native interaction |

## Baseline sequence

- [ ] Resolve scope with owner: recommend code-contract plus source-reviewed answer
  baseline, with interaction outcomes explicitly outside the measured endpoint.
- [ ] Independently review exact Apple sections for each atomic assertion, accepted
  alternatives and OS26 availability. URLs alone do not constitute that review.
- [ ] Freeze a new acceptance/catalog revision; preserve current draft and receipts.
  Keep evaluator keys and known-good/mutation code out of the model workspace.
- [ ] Qualify one Apple worker for compile/unit evidence; do not assign native runs
  to this busy Mac by default. Confirm MaxMini capacity or another approved host.
- [ ] Validate known-good plus each relevant single-defect mutation using identical
  tests. Classify unsupported assertions rather than counting unrelated failures.
- [ ] Calibrate independent answer review under GRADING.md, including its existing
  agreement threshold; then freeze the provider/adapter/catalog and baseline scope.
- [ ] Collect small subscription-backed OS26 batches on BigDog, preserving all
  outcomes. Expansion, repetitions and candidate comparisons need fresh allocation.

Do not reuse the historical six-pair Gemini review as answers to changed prompts.
No rubric edits, new generations or native execution occurred in this audit.

## Relationship to the example library

Evaluation fixtures test the measurement system; published examples support users.
They can share validated source utilities later, but example answers must remain
separate from evaluation answer keys. Establish baselines before integrating the
example index or new runtime instructions. See the research implementation outline.

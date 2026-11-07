# Consolidated rubric-gap closure

Author/controller revision covering all 60 draft cases. Released skill, original
candidate subjects/rubrics, frozen baselines, historical assertion bindings and
native evidence are unchanged. No model calls, native example reruns or spend.

## What changed

| Work | Result |
| --- | ---: |
| Cases / original criteria preserved | 60 / 198 |
| Criteria with explicit pass, gap and insufficient-evidence decisions | 198 |
| Previously unbound criteria given actionable grading specifications | 117 |
| Boundary controls with relevant accepted alternatives | 12 |
| Additional existing checkout methods linked | 3 |
| New native runs / model calls / real answers graded | 0 / 0 / 0 |

Read the [operational review packet](REVIEW.md) or the complete [rubric overlay](rubrics.json).
They are controller-only. Keep both out of subject input and normal skill context.

The 117 gaps are closed as **grading-definition gaps**, not as missing unit coverage.
Three primary-source mappings remain open. Broader behavioral evidence, independent
acceptance and model-answer improvement have not been inferred from these definitions.

## Practical improvements

- Every topic now has observable acceptance and failure descriptions, not just a
  keyword checklist. Missing evidence is a distinct outcome.
- A no-change answer is valid for a supplied working control. Unknown mixed ownership
  instead accepts targeted clarification or conditional advice, not generic no-change.
- Missing-reference answers may truthfully say the document was not read. There is
  no blanket ban on an honest lack-of-access statement.
- Runtime, deployment and SDK claims are separately graded. Platform/framework
  assumptions do not transfer automatically. Scope controls for WatchOS/visionOS
  do not falsely imply those platforms lack accessibility APIs.
- Native metadata absence, errors and loading differ; mute/volume preservation is
  not a substitute for selected audio/subtitle preservation.
- Checkout alternatives include justified flexible layouts without requiring one
  stack/axis recipe. Missing project code is handled by an explicit preservation
  interface, not invented hidden payment wiring.

Source anchors include exact local excerpts, file hashes and locations. These are
existing project/guideline records, not a fresh Apple-document audit or validated
cross-platform availability. Project policy anchors justify grading conventions,
not Apple API guarantees. Independent review must still verify applicability.

## Added checkout evidence

Three revision-2 UIKit tests already have exact successful execution receipts:
button identity/typography/title, repeated-update callback preservation, and flexible
text configuration. The tests are linked only to the iOS/UIKit text criteria.
They are not reused as SwiftUI/AppKit/tvOS evidence. The original revision-1 oracle
failure remains in its historical file; no repaired outcome replaces that record.

These methods strengthen two existing partially bound criteria rather than inflating
the count of fully covered criteria. They do not prove rendered clipping, live trait
notification delivery or actual interaction.

## Review-record safeguards

[The schema](review-schema.json) and [validator](review.mjs) check complete criterion
IDs, subject/answer/rubric hashes, exact answer excerpts, source references and typed review
outcomes. A fixture's green test cannot be submitted as an answer-grade basis.
Missing excerpts, stale input identities and synthetic/unknown origin claims remain
visible. Synthetic records are never real model results.

The validator does **not** decide whether a quote satisfies an accessibility rule.
It validates record consistency, not semantics, actual origin or reviewer independence.
It returns no automatic independent acceptance. No LLM judge, fuzzy matching or
substring-based correctness score was added.

## Reproduce locally

```sh
node research/evaluation/rubric-closure-v1/build.mjs > /tmp/rubric-closure.json
node --test research/evaluation/rubric-closure-v1/integrity.test.mjs
```

Requires the existing local Ajv installation and syntax probe. No new dependency or
provider is needed. The first 278-check run and final 279-check run pass; deliberate bad review records
are rejected for their intended consistency violations. Those are harness checks,
not additional accessibility behaviors or model-performance measurements.

## Publication and remaining work

The prior assertion-binding checkpoint is committed and pushed as **b9c0a14**.
This substantial continuation is uncommitted. Its original inputs remain pinned.

Next is independent semantic review of this single consolidated packet and the
three source mappings. Fix any oracle defects before approving a bounded frontier
batch. Keep remaining code-contract gaps explicit rather than forcing everything
into unit tests or demanding owner-run manual accessibility verification.

This is controller revision `operational-1`. Existing historical grades are not
rewritten or directly compared with these revised criteria. A future paired report
must grade both conditions with the same frozen rubric revision. Review records
pin `sha256(JSON.stringify(corpus))` as well as subject and answer hashes, so a stale
review cannot silently apply to a changed rubric.

## Consolidated validation

The full offline suite passes **1,179 checks**, including 279 in this new suite.
The exact passing output is retained in [offline-checks.log](offline-checks.log),
with source/artifact hashes in [checkpoint.json](checkpoint.json). The frozen
baseline verifier still validates 210 files and the historical verifier validates
87 pinned records. Protected sources match b9c0a14; whitespace checks pass.
These are integrity/consistency checks, not 1,179 independent accessibility behaviors.

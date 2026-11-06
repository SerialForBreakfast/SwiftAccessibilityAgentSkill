# UIKit Evidence and Evaluation Status

Updated November 5, 2026 (America/Los_Angeles).
Publication boundary: `6cdaa0b`, the pushed merge preserving checkpoint `a47d975`
and upstream research proposal `d93efa9`. The current uncommitted addition is
UPAIR-06B audio-description metadata and loaded-asset extraction. The earlier
checkpoint inventory below remains labeled by its original boundary. This document
does not authorize publication, model runs or skill promotion.

## Latest Addition Since 6cdaa0b

[UPAIR-06B](../../../code-examples/pilots/uikit-media-metadata-v1/README.md) adds
matched tagged/untagged synthetic MOV fixtures, actual audio-description tag
recognition, selected audio/subtitle-off preservation, loaded duration, subtitle
variants and distinct missing/error states. Seven positive methods and three
intended mutant rejections passed. The first attempt compiled with a deprecated
locale accessor; revision1 source/diagnostics are preserved and revision2 passes
after its replacement. Five offline checks bind payloads, history and evidence.

Its natural developer prompt and controller rubric remain separate drafts. The
silent fixture proves metadata recognition, not narration quality. Local asset
loading is not live playback or player readiness. No model runs were performed.
Upstream ADR-004 and the compact candidate batch are proposals; merging them did
not authorize their execution or change the installed skill.

## Verified Successes

The seven paired development packets below have 67 positive native unit methods,
seven successful compile checks and 27 deliberately rejected mutants across their
current revisions. These totals cover this table, not the entire historical library.
Each negative passed its expectation by failing its selected assertion; it is not
an additional independent scenario or a spontaneous model failure.

| Pair | Current native evidence | Positive methods | Mutants rejected | Paired evaluation |
| --- | --- | ---: | ---: | --- |
| UPAIR-01 Naming | [Revision 1](../../../code-examples/pilots/uikit-naming-v1/validation/revision-1.json) | 8 | 3 | Draft; independent review pending |
| UPAIR-02 Long text/selection | [Revision 1](../../../code-examples/pilots/uikit-choice-v1/validation/revision-1.json) | 9 | 4 | Draft; independent review pending |
| UPAIR-03 Contrast | [Revision 1](../../../code-examples/pilots/uikit-contrast-v1/validation/revision-1.json) | 9 | 4 | Draft; independent review pending |
| UPAIR-04 Modal lifecycle | [Revision 3](../../../code-examples/pilots/uikit-modal-v1/validation/revision-3.json) | 13 | 5 | Draft; independent review pending |
| UPAIR-05 Edited rotors | [Revision 1](../../../code-examples/pilots/uikit-edited-rotor-v1/validation/revision-1.json) | 12 | 5 | Draft; independent review pending |
| UPAIR-06A Media time/buffering | [Revision 1](../../../code-examples/pilots/uikit-media-inspection-v1/validation/revision-1.json) | 9 | 3 | Draft; UPAIR-06 remains partially complete |
| UPAIR-06B Media metadata | [Revision 2](../../../code-examples/pilots/uikit-media-metadata-v1/validation/revision-2.json) | 7 | 3 | Draft; independent review pending |

The modal history preserves an actual retained-but-removed target failure and its
repair after an earlier green suite. Media revision 1 had no unexpected native
failure. Both are useful evidence, but must not be conflated.

Current offline checks: **193 passing tests**, **210 frozen baseline files verified**,
and **87 historical evidence pins verified**. Native method counts and offline
test counts measure different layers and are not added together. Skill version
remains `0.2.2`; verified candidate content hash:
`3a1a2d58af19a94eec940000d9edcca7928bb5139aa3d52b1ef6e917c0271bbd`.

## Previous Checkpoint: f0bfc51 to a47d975

### Media implementation and native tests

New [media inspection package](../../../code-examples/pilots/uikit-media-inspection-v1/README.md):

- `Sources/MediaInspection.swift`: duration classification, explicit stream-kind
  knowledge, separate seekable/loaded ranges, independent buffer flags, requested
  rate, time-control status, waiting reason and read-only player capture.
- `Tests/MediaInspectionTests.swift`: nine focused methods covering unknown and
  nonfinite duration, range gaps and half-open ends, contradictory-looking buffer
  states, waiting with nonzero requested rate and empty-player noninterference.
- `NegativeFixtures/`: three isolated defects confuse loaded with seekable ranges,
  infer readiness from buffer fullness, or infer live content from indefinite time.
- `manifest.json`, `coverage.json`, `apple-sdk-sources.json`: hashed inputs,
  source-backed claims, exact test IDs and U-015 media mapping.
- `validation/`: five expected native outcomes, original private log/record hashes,
  exact environments and sanitized assertion diagnostics.

Native environment: Xcode 27.0 build 27A266a, Swift 6.4, SDK 27.0 build 24A430,
deployment target 26.0, arm64; actual unit runtime iOS 26.5 build 23F77.
Compile-only evidence has no runtime. This establishes the tested configuration,
not every intervening OS release. Raw UTC records fall on November 6; local work
date is November 5.

### Paired evaluation and difficulties

`evaluation/prompt.json` contains a natural developer task. The outcome-based
rubric, case hashes, implementation, test expectations and incident records remain
controller-only. Case `UPAIR-06A-D1` is development material, with zero model runs;
independent prompt neutrality, oracle and rubric review remain pending.

The difficulty ledger records source access limits, anticipated design risks,
the corrected U-014/U-015 coverage mapping and a rejected documentation patch.
Exact manufactured Swift defects are retained separately in `MUTATIONS.md`.
These authoring/tooling issues are not mislabeled as model accessibility failures.

The new offline test file is
`code-examples/tools/media-inspection-contract.test.mjs`. Its three checks bind
coverage, subject/controller separation and exact native outcomes.

### Analysis and status documentation

[Haiku input analysis](HAIKU-INPUT-ANALYSIS.md) records conclusions and limits from
the incoming report. `code-examples/README.md`, `evals/README.md`, root `Tasks.txt`
and [the failure-driven task list](TASKS.md) now distinguish native success from
gold readiness and identify the remaining media work. The incoming report itself
was already committed and remains unchanged.

The unrelated private `evals/COORDINATOR-ONBOARDING.md` stays excluded from this
checkpoint. Raw native logs, credentials and host/account details are not public
deliverables. Use explicit paths, not `git add .`, when preparing publication.

## What We Learned From Upstream

| Haiku source-review result | C0 | C2 |
| --- | ---: | ---: |
| Gold code | 13/18 | 16/18 |
| Exploratory code | 15/18 | 14/18 |
| Evidence questions | 4/6 | 6/6 |
| Reported total tokens | 106,060 | 307,756 |

C2 used about 2.90 times the tokens without uniform quality improvement.
Prioritize grounded no-change decisions, scope preservation, actual platform
availability and a smaller future reference payload. These are hypotheses for
paired evaluation, not permission to edit the frozen skill now.

The results are single-reviewer, unblinded source assessments. Generated answers
have not undergone native validation; C2 is manual reference injection, not
autonomous retrieval. Repetitions are not independent scenario families. No
statistical superiority, production usability or cross-provider cost conclusion
is established. See the linked analysis for the distinction between interaction
claims and this repository's unit-test-only promotion gates.

## Remaining Work and Acceptance

1. **Review UPAIR-06 media evidence.** Both time/buffering and tagged-metadata
   packets now have native records and draft pairs. Confirm scope against the
   inventory and identify any further gaps without inferring live playback or
   description quality from metadata. Acceptance: independent source/oracle/prompt
   decisions; additional gaps become explicit tasks, not silently closed coverage.
2. **Complete UPAIR-07 availability.** Audit used public declarations and applicable
   deployment guards against the selected toolchain. Acceptance: exact declaration
   evidence and appropriate compile checks, with SDK, target and runtime separated.
   Preserve annual anchors rather than introducing a minor-version support matrix.
3. **Complete UPAIR-08 inventory.** Map all 15 UIKit guideline code contracts to
   assertions or explicitly justified out-of-scope entries. Acceptance: omissions
   visible and reviewed; counts alone cannot close the inventory. Preserve the
   historical pinned audit and publish any updated mapping separately.
4. **Independently review the new pairs.** Review source scope, test oracles, prompt
   neutrality, valid alternative solutions and rubric calibration. Acceptance:
   recorded reviewer decisions before freezing a development overlay. Existing
   incidents remain development cases, not fresh holdouts.
5. **Run an approved bounded comparison.** After review and quota approval, compare
   frozen conditions on identical prompts; preserve first attempts, actual reads
   where available, token telemetry and uncertainty. Native example success alone
   is not a model score. Frontier coding models remain the primary target.
6. **Propose candidate skill changes.** Only accepted baseline evidence can justify
   focused correctness or context-efficiency changes and subsequent held-out review.
   Runtime instructions and frozen baselines remain unchanged until that gate.

## Reproduce Offline Checks

Run from the repository root:

```sh
node --test code-examples/tools/*.test.mjs evals/runner/*test.mjs
node evals/runner/check.mjs
node research/reports/2026-11-05-frontier-coding-evidence/verify-record.mjs
git diff --check
```

These commands do not run models or native simulators. Native rerun instructions
are in the media package README and require a fresh private output path. No UI
tests or mandatory manual verification are introduced.

## Previous Checkpoint Commit Message

```text
Validate UIKit media inspection contracts and summarize baseline findings

Add nine unit contracts for duration states, discontinuous seekable and loaded
ranges, independent buffer flags, requested rate/status and empty-player capture.
Record successful compilation and three intended mutant rejections on iOS26.5,
with hashed inputs, reviewed SDK headers and sanitized native evidence.

Pair UPAIR-06A with a separate natural developer question and controller rubric.
Preserve exact mutation diffs and distinguish anticipated risks, authoring issues
and observed outcomes. Keep independent review and model evaluation pending.

Analyze the merged Haiku report's mixed quality results and 2.90x token usage.
Refresh current status and next gates without changing the upstream report,
released skill, frozen baselines or historical evidence pins.

Verify 188 offline tests, 210 frozen baseline files and 87 historical pins.
Leave audio-description metadata, loaded-item extraction, availability and final
inventory closure explicitly open. Exclude private coordinator onboarding.
```

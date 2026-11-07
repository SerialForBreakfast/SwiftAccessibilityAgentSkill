# GPAR-M01 — Mac evidence collection

Prepared for the existing SwiftAccessibilityAgent Mac peer. The owner chose Git
handoff: commit/push here, then the owner pulls on the other machine. No coordinator
message is required or claimed. Publication, worker acceptance and the returned
evidence packet are separate states.

Please collect **existing evidence only** while the portable criterion audit runs
in parallel. This is not a request for new implementation or evaluation.

## Start after the owner pulls

1. Read the checkout's `AGENTS.md`, `AGENT.md` and
   `research/evaluation/failure-driven/PRD.md`.
2. Read `research/evaluation/gold-parity-v1/TASKS.md` and
   `research/evaluation/gold-parity-v1/case-inventory.json`. The portable first-pass
   audit is now available: read `research/evaluation/gold-parity-v1/audit-v1/README.md`
   and its `NEXT-TRANCHE.md` section "Specific questions for the existing Mac pass".
   Use the matrix and exact evidence links to focus collection; the findings are
   author judgments pending reconciliation, not new gold qualifications.
3. Record the pulled Git revision and acceptance of **GPAR-M01 only** in the
   packet. The inventory's `planningBaseCommit` identifies its input snapshot;
   it is not the later publication commit. Do not reset to it.
4. Perform the bounded existing-evidence pass below. GPAR-01 is the portable
   audit lane; do not duplicate that full audit or take GPAR-04/05 native work.
5. Return the consolidated packet and unresolved gaps to the owner. Do not wait
   for a coordinator session, start another agent or run evaluation models.

## Scope

Use the current 24-case selection from
`research/evaluation/milestone-package-v2/manifest.json` (12 related families),
with the reviewed interpretations in
`research/evaluation/gemini-preflight-v1/controller.json`. Record your current
checkout revision and these input hashes. If unavailable or different, report the
specific mismatch; do not reset or rewrite sources to manufacture a match.

Use existing evidence pointers first:

- `research/evaluation/local-qualification-v1/evidence-ledger.json`
- `research/evaluation/rubric-closure-v1/rubrics.json`
- `research/evaluation/v2-controller-resolution-20261107/composite-controller.json`
- `evals/os26/reports/2026-11-05-gold-closeout/readiness.json`
- The manifest/check/test IDs explicitly linked by those records.

Do not sweep unrelated home directories or load every incident/example archive.
Inspect the linked records needed to locate the selected evidence.

## Collect and verify

1. Locate existing compile/unit receipts, positive examples and intended negative
   controls for the selected cases. A proposed test name is only a lead.
2. Verify available manifest/source/receipt hashes and exact test selections.
   Record expected and observed results. Distinguish intended assertion rejection
   from failed builds, skipped/zero tests, compiler/macro errors and simulator issues.
3. Record compiler/Xcode/SDK build, deployment target, architecture and actual unit
   runtime from each receipt. Compile-only records must not invent a runtime.
4. Summarize available installed Xcode/SDK/runtime inventory from existing captures
   or metadata-only queries. Mark stale/unavailable information honestly. Do not
   boot a simulator or provision a device just to obtain this inventory.
5. List missing files, mismatched revisions and partial coverage. Do not rerun a
   suite or repair examples to fill a gap. The portable audit decides which exact
   new checks, if any, should be proposed later.

## Return one consolidated packet

Create a fresh directory inside your checkout, for example
`evals/results/gold-parity-v1/mac-evidence-<run-id>/`. Keep every new log, scratch
file and cache inside that project directory; no operating-system temporary path.

- A readable summary: existing valid evidence, partial evidence, missing/mismatched
  records, toolchain inventory and precise limits.
- A JSON index: case ID and candidate criterion links, manifest/source hashes,
  check/test IDs, receipt path/hash, expected/observed outcome and exact environment.
- An artifact manifest with hashes. Retain originals privately; share sanitized
  relative paths and findings, without credentials or account details.

Do not claim that metadata/callback units prove rendered layout, generated
accessibility traversal, delivered input, speech or focus. Keep source-only
controls separate from native-tested contracts. Existing accepted reports may be
linked instead of copied or regenerated.

## Boundaries

No new builds, unit/UI tests, simulator boots, code changes, model/authoring/judge
batches, provider probes, installs, dependency/account changes, Git publication,
skill promotion or new agent creation. No subscription evaluation on the Mac.
No automatic polling or extra worker messages. Prepare the report for the owner;
the owner will arrange the return. If a required record is unavailable, return that
gap rather than expanding execution scope.

Keep this pass bounded: stop after one evidence-discovery pass and report remaining
unknowns. Acceptance of this task and successful delivery of the evidence packet
must be reported separately.

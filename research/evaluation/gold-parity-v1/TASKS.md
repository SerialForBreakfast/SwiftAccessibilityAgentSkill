# Gold-prompt parity tasks

Status: **planning complete; GPAR-01 first-pass author audit executed; independent
qualification pending**. The owner subsequently requested "start our tasks" and
"a large tranche". Results are in [audit-v1](audit-v1/README.md). The task plan and
evidence-only Mac handoff authorize no model batch,
native implementation, new builds/tests or promotion. The owner separately
authorized committing and pushing this package for the other machine to pull.
The owner-approved Mac handoff covers only GPAR-M01's read-only evidence work;
publication does not establish worker acceptance or execution.

## Target and current evidence

Bring the current 24 development scenarios / 78 criteria / 12 related families to
an explicitly reviewed evidence standard. The original six gold-ready cases remain
unchanged. Cross-check overlap before adding case counts. Known development cases
remain development cases after qualification; they do not become fresh holdouts.

[Case inventory](case-inventory.json) records exact source hashes and work status.
All criterion coverage starts `not_audited`; a linked receipt is not proof that its
assertions cover the whole developer question.

Reuse these existing records before writing or running anything new:

- [Original six-case closeout](../../../evals/os26/reports/2026-11-05-gold-closeout/readiness.json).
- [60-case evidence ledger](../local-qualification-v1/evidence-ledger.json): 36
  linked native contract receipts across the full 60, not 36 qualified cases.
- [Reviewed controller overlay](../v2-controller-resolution-20261107/REVIEW.md)
  and [materialized controller](../gemini-preflight-v1/controller.json): reviewed
  interpretations for 24 tasks, including action alternatives and source rebinding.
- [Completed Gemini comparison](../gemini-controlled-run-20261107/README.md): reuse
  existing source calibration/results; no repeat of its 48 completed sessions.
- [Preflight publication correction](../gemini-preflight-v1/PUBLICATION-UPDATE.md):
  the separate held preflight is not another allocation. Its empty 96-slot template
  must not trigger fresh authoring/judge calls without a reuse/coverage audit.
- [Dev.6 media extension](../failure-driven/candidates/0.3.0-dev.6/README.md): nine
  corrected media starter/prompt/rubric pairs are a separate, later tranche.

## Work locations and ownership

**Portable/here:** source/criterion mapping, receipt inspection, prompt and rubric
review, comparison of hashes, packaging and the promotion proposal. Existing
Apple results can be checked without rerunning them or having Xcode locally.

**Mac/Xcode:** only missing Apple compilation or native unit evidence. Existing
receipts and source hashes come first. Current/previous annual anchors and exact
SDK/build, deployment target and actual runtime remain separate.

**BigDog:** any separately approved subscription evaluation or model-based review.
Incremental spend remains zero. No installs, new model runs, extra probes or remote
execution are granted by this plan. Reviewer/worker roles below are proposed;
assignment and acceptance must be recorded, not inferred.

The owner will pull this package on the other machine and have the Mac report
back. Start there with [the Mac instructions](MAC-HANDOFF.md). Git publication,
worker acceptance and returned evidence are separate states. No coordinator
delivery is claimed. Do not start automatic polling or extra worker messages.

## Task list

| ID | Work and location | Depends on | Deliverable / acceptance | Initial state |
| --- | --- | --- | --- | --- |
| GPAR-00 | Establish scope; planning agent, here | None | 24 unique cases, 78 unique criteria, 12 families; source identities pinned; original six and later media tranche kept separate | Draft inventory prepared; checked locally |
| GPAR-01 | First-pass evidence audit; audit owner, here | 00; can start before Mac return | Cap at **two active hours**. Classify every criterion as direct evidence, partial evidence, review-only, genuine gap or not yet audited. Cite exact source/assertion/receipt IDs and scope. At the cap, retain unknowns and produce per-family effort estimates; do not invent a completion date | Executed first pass: 24/78/12; 73 selected methods, 94 existing receipt rows; [author findings and limits](audit-v1/README.md). Independent acceptance pending |
| GPAR-M01 | Existing Apple evidence packet; Mac peer | 00; parallel with 01 | Read-only collection per [Mac handoff](MAC-HANDOFF.md). Verify existing source/manifest/receipt hashes, selected test IDs and recorded environments; return one packet with missing/mismatched records. No new builds, simulator boots or model calls | Handoff published in c89f486; owner will pull. Worker acceptance/evidence return not yet recorded |
| GPAR-02 | Merge audit and Mac packet; audit owner, here | 01 + M01 return, or explicit unavailable report | One criterion-level gap matrix. Reuse valid receipts. Distinguish missing linkage from missing behavior, test defects, stale source mappings and harness failures. Match original six by exact question/contract, not similar names. Assign each criterion an evidence lane | Portable matrix/crosswalk and reuse candidates prepared; pending Mac packet, not complete |
| GPAR-03 | Close source/question/scoring gaps; author + reviewer, portable | 02 | Verify applicable primary-source sections/declarations and freshness; preserve historical anchors. Apply reviewed IR-01/IR-02 and provenance corrections equally to all conditions. Accept stable current-owner handlers, valid layouts and native defaults. Revise ambiguous questions/rubrics only in new versions | Not started |
| GPAR-04 | Prepare only necessary native work; audit owner + Mac worker | 02; relevant 03 decisions | A bounded manifest of exact missing source sets/checks, targets, test IDs, positive/negative variants, expected assertion failures, time/resource limits and project-local output paths. Owner scope and worker acceptance required before execution | Not started; no native allocation |
| GPAR-05 | Execute approved native gaps; Mac worker | 04 approved | Correct reference passes; relevant defective variants fail for intended assertions, not build/simulator/macro/harness errors. Reuse existing negative controls when they prove the contract. Record exact environment, source/test hashes and full test selection. Preserve first failures and any approved repairs separately | Not started; gated |
| GPAR-06 | Review scoring sensitivity; independent reviewer, portable + existing native receipts | 03; 05 only where new evidence is needed | Reuse the completed 48 design-calibration records where applicable. Map correct, defective, valid-alternative and ungradable examples to the actual criteria. Create/review only uncovered examples through an explicitly assigned workflow. No blanket 96-example regeneration or separate model judge batch | Not started |
| GPAR-07 | Independent readiness decision; reviewer distinct from sole author | 02–06 as applicable | Per-case signed decision: ready for review-scoped qualification, ready for compile/unit/source qualification, or deferred with exact blockers. Criterion evidence and alternatives checked; reviewer exposure disclosed. Model success is not a promotion prerequisite | Not started |
| GPAR-08 | Additive promotion package; maintainer, here | 07 | One proposed catalog revision with approved case IDs, claim limits, source/prompt/rubric/starter hashes, reviewer decisions, completeness/leakage checks and original-six crosswalk. Keep frozen inputs/runtime skill unchanged. Apply only after owner promotion approval | Not started; proposal only |
| GPAR-09 | Consolidated iteration handoff; maintainer, here | 08 readiness decisions | One backlog of granular guidance improvements grouped by shared concern. Reconcile dev.6 and existing Gemini gains/regressions before proposing another candidate. Distill general rules, remove duplication and avoid prompt-specific answer hints. Define one later baseline/candidate comparison on the same frozen set | Not started; no model allocation |

## Equal trust, explicit claim scope

For implementation contracts, reuse or obtain compilation and focused native unit
evidence for the **critical assertions**, a known-good example and relevant wrong
variants. The original six-case protocol uses two distinct mutants; do not waive
that standard silently or invent irrelevant mutants to fill a count. Document any
unsuitable mutation and obtain an explicit reviewed acceptance decision. Valid
alternative implementations must be accepted by the scoring/tests.

For reasoning/no-change/evidence controls, independent source-backed scoring and
correct/defective/alternative/ungradable examples may be the right evidence. Do not
demand an unnecessary Apple run, or label a source-only case as native-validated.
Choosing a weaker lane is not a shortcut for an unmet implementation contract.

No criterion may infer delivered speech/focus, generated navigation, rendered
clipping or user-input delivery from declarations or callback/configuration units.
No UI tests or mandatory manual accessibility walkthroughs are added. Compilation
alone is not complete task success; a model's failure does not make the test invalid.

## Scheduling and effort control

Start GPAR-01 here and GPAR-M01 on the Mac in parallel after delivery/acceptance.
Merge those findings at GPAR-02. Batch shared fixes by the 12 existing families;
retain platform/framework-specific assertions and receipts. Limit new native
closure work to at most two active families and run approved Mac jobs serially.

Only the first audit has a proposed time cap. Its output must estimate the actual
remaining portable, Mac and review work separately, with confidence and unknowns.
There is no evidence-backed total duration or reviewer-capacity commitment yet.

Qualifying tests and improving the skill are separate milestones. After a
substantial set of reviewed changes is ready, propose **one consolidated BigDog
comparison**, rather than model evaluation after every small edit. Reuse actual
supported transport evidence; existing completed runs must not be repeated merely
to fill missing historical telemetry. Model, quota and stop conditions require a
fresh, concrete approval at that point.

## Records and completion criteria

Keep new raw records, working files, scratch and caches under this project's
`evals/results/gold-parity-v1/`. Use a fresh run directory; never overwrite previous
evidence. Keep controller data out of subject payloads. Follow the
[prompt-record contract](../prompt-records-v1/README.md), and record unavailable
history explicitly rather than reconstructing an exact transcript.

Planning is complete when the task dependencies, locations, deliverables, scope,
seed inventory and Mac message exist and internal references/counts validate.
Git publication is complete only after the remote commit is verified; it does not
prove the Mac pulled or read it. Mac acceptance and evidence delivery remain
separate. Qualification is complete only for cases with
reviewed acceptance records. No case is promoted by this plan.

See the parent [failure-driven requirements](../failure-driven/PRD.md) and
[task acceptance criteria](../failure-driven/TASKS.md#definition-of-done-for-each-pair).

# Repository Development Instructions

These instructions govern maintenance of this repository. They are not the
installed accessibility skill. Keep the existing root `SKILL.md` as the single
skill entry point; do not create another installable skill for maintainer tasks.
Read `AGENT.md` for the existing repository safety policy.

## Test-Driven Skill Improvement

For unit-library or evaluation planning, first read
[the failure-driven evaluation plan](research/evaluation/failure-driven/PRD.md).
Load its task list, audit or worker handoff only when relevant.

- Develop each accessibility example as a paired evidence package: source claim,
  compile/unit contract, natural developer question, independent grading criteria,
  and a traceable evaluation case. Passing unit tests alone do not finish the pair.
- Preserve exact failed code, diagnostics, environment and repair history. Distinguish
  accidental defects, intentional mutants, test-oracle defects, harness errors and
  coverage gaps. Do not assume that every failure belongs in accessibility guidance.
- Audit the test oracle before using it to grade another model. Accept alternative
  implementations that satisfy the source-backed contract.
- Keep subject prompts separate from solutions, rubrics, incident narratives and
  expected routes. Known incidents are development cases, not fresh holdouts.
- Compare frozen skill conditions on the same scenarios. Attribute outcomes to
  model, harness and context separately; do not infer model rankings from anecdotes.
- Record first attempts and any authorized repair attempts separately. A named
  reference is not evidence of a read; retain actual retrieval traces when available.
- Retain every prompt used for authoring, evaluation, repairs and judging, with
  complete captured inputs, original outputs and separate analysis. Follow the
  [prompt-record contract](research/evaluation/prompt-records-v1/README.md).
  Mark unavailable history explicitly; never reconstruct it as an exact transcript.
  The full audit record is controller-only, not additional subject context.

## Boundaries

- Keep all task-created files inside this project directory, including scratch
  files, message drafts, request/response records, logs, test artifacts and caches.
  Use `evals/results/` for private evaluation and messaging artifacts. Do not use
  `/tmp`, `/private/tmp`, `os.tmpdir()` or another outside-project location unless
  the user explicitly authorizes that specific destination. Sandbox write access
  does not grant permission to use another directory.
- Preserve the UIKit baseline. AppKit/macOS and UIKit/tvOS companion development
  is now authorized; SwiftUI expansion remains deferred. Compile checks and unit
  tests only; no UI tests or mandatory manual accessibility verification. Tests
  establish only their directly asserted behavior.
- Preserve source tiers. Use annual current/previous tested anchors and exact run
  environments, not a continuous minor-version support commitment.
- Keep examples on demand. Do not load the incident archive or all examples by default.
- Keep released/runtime skill files and frozen baselines unchanged until separately
  approved, benchmark-backed promotion. Planning does not authorize resuming paused
  native implementation, changing baseline fixtures, or running evaluation models.
- Frontier coding agents are the primary target. Small local models provide
  diagnostic evidence, not release optimization targets.
- Incremental spend is zero. Live batches require explicit quota and scope approval;
  no paid fallback, silent model substitution, installs or remote execution by default.
- Preserve unrelated changes and historical evidence. Git publication and worker
  messaging require authorization; preparing a handoff is not sending it.

Use [task acceptance criteria](research/evaluation/failure-driven/TASKS.md) before
reporting work complete. Distinguish draft, reviewed, executed and accepted outcomes.

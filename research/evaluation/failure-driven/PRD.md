# PRD: Failure-Driven Accessibility Skill Evaluation

Status: planning draft for review, 2026-11-05. This document itself authorizes no
model runs, native execution or skill promotion. Native work was paused when this
plan was written; subsequent explicit owner instructions resumed bounded UIKit
tranches under the active "finish the uikit tests" goal. Executed scope and evidence
are recorded in Tasks.txt and each tranche, not inferred from this planning document.

## 1. Summary

Turn UIKit unit-test development into evidence for independent, realistic developer
questions. Measure whether the skill prevents the corresponding mistakes across
frontier models and execution contexts. The loop is:

source claim -> executable contract -> observed difficulty -> adjudicated case ->
independent prompt -> frozen baseline -> focused skill change -> paired evaluation.

Tests inform gold prompts; they do not automatically make prompts gold. A defective
test or harness must be corrected before it becomes an answer oracle.

## 2. Roles

| Role | Responsibility | Assignment |
| --- | --- | --- |
| Maintainer | Scope, quota, adjudication and release decisions | Project owner |
| UIKit author | Source contracts, minimal examples and unit evidence | Local project agent, when resumed |
| Independent reviewer | Prompt neutrality, oracle validity and grading calibration | Requested from BigDog; acceptance pending |
| Execution worker | Isolated approved subscription runs and sanitized records | BigDog preferred; MaxMini after capability confirmation |
| Blind grader | Answer quality independent of condition identity | Reviewer other than sole answer author |

These are proposed responsibilities, not worker acknowledgments or capacity promises.

## 3. Background

The [preserved development record](../../reports/2026-11-05-frontier-coding-evidence/README.md)
contains eight difficulty themes, exact code/diagnostics and intentional mutation
tests. It includes mistakes in font environments, lifecycle assumptions, media
option interpretation, test assertions and diagnostic classification. It is not a
controlled model comparison. See [conversation audit](CONVERSATION-AUDIT.md).

This work supplements [ADR-003](../../adr/ADR-003-version-anchored-unit-tested-examples.md),
the [OS26-first evaluation](../../../evals/os26/README.md) and existing
[grading rules](../../../evals/GRADING.md). It does not replace or expand a frozen
baseline in place. Previously reviewed OS26 cases can proceed independently;
new cases require a separately versioned development overlay.

## 4. Objectives and Acceptance

| Requirement | Acceptance criteria |
| --- | --- |
| FR-01 Traceable pairs | Every selected new feature and incident has a stable family ID linking source URL/section, claim, exact test/check IDs, fixture revision, prompt, rubric and run records. Missing links block promotion, not preservation of the observation. |
| FR-02 Trustworthy oracle | Reviewer records what the assertion proves, environment scope, allowed alternatives and non-goals. Positive example passes; a relevant deliberate defect is rejected for the intended reason, or reviewer explains why mutation is unsuitable. Infrastructure failure never counts as a successful rejection. |
| FR-03 Neutral questions | Each prompt is a plausible Swift developer request with necessary inputs. Review confirms it contains no incident conclusion, expected fix, grading answer or internal routing cue. Model-visible payload is separately hashed. |
| FR-04 Independent evaluation | New sessions receive only the approved condition payload. No access to author notes, tests that expose hidden expectations, solution files or grader workspace. Any leakage invalidates the comparison and is reported. |
| FR-05 Comparable conditions | C0 generic; C1 actual instructions with references unavailable; C2 actual instructions with selected references; C3 actual instructions with instrumented lookup. Same user task and environment per pair. C1 must not claim reads; C2 is injection, not autonomous retrieval. |
| FR-06 Honest outcomes | Preserve first answer, failure and authorized repairs separately. Classify subject defect, oracle defect, harness defect, missing capability, timeout, quota stop, ambiguous task and success. Unanswered/ungradable cells remain visible. |
| FR-07 Version specificity | Record compiler, SDK, deployment target and actual runtime separately. A pass proves that anchor's assertion, not all versions or assistive-technology behavior. Current/previous annual anchors only. |
| FR-08 Measured improvement | Compare baseline/candidate on the same frozen families and conditions. Report quality, critical errors, protocol and efficiency separately. No causal model claim from mixed harness/context settings. |
| FR-09 Portable handoff | Worker can identify allowed inputs, bounded cells, return fields and stop conditions without reading incident answers. Unknown capability/model revision is explicit, never silently substituted. |
| FR-10 Feature completion | Each UIKit task has native evidence status and paired-evaluation status. Neither can be inferred from method counts or the other status. |
| NFR-01 Safety and cost | No spend, installs, model runs, remote messages or Git mutations authorized by these documents. Each live batch has explicit owner approval and a hard call/token/tool/time ceiling. |
| NFR-02 Preservation | Runtime skill, frozen benchmarks and historical records retain their hashes. New cases use new IDs/revisions; no retroactive relabeling as held-out. |
| NFR-03 Context economy | Retrieve only required references/examples. Record actual input/output tokens, reference bytes, tool calls and latency; mark unsupported telemetry unavailable. |
| NFR-04 Maintainability | Unit/compile only, annual refresh, opt-in interim maintenance, no additional source tier and no mandatory manual/UI verification. |
| NFR-05 Privacy | Public/synthetic fixtures and sanitized results only. Keep credentials, host/account details, private logs and private prompts outside public artifacts. |

Completion of this planning phase means requirements, task dependencies, draft prompts
and a bounded handoff exist. It does not mean prompts are promoted or baselines collected.

## 5. Users

- Swift developers asking ordinary implementation and debugging questions, including
  people unfamiliar with accessibility vocabulary or rotor navigation.
- Maintainers needing precise evidence of useful skill changes within limited time.
- Worker/reviewer agents needing reproducible tasks without answer contamination.

Preserve ordinary controls alongside optional accessibility shortcuts in relevant
contracts. Unit evidence measures configuration and callback behavior, not universal
accessibility or real-user usability.

## 6. Value and Measures

Measure source-backed correctness and task success using existing 0-4 rubrics;
record unsupported API/availability claims and lost-functionality errors separately.
Report per-family results, not inflated totals from related mutants or paraphrases.
Measure complete evidence-pair coverage over the explicitly selected work inventory.
Do not calculate model accuracy from the historical interactive development session.

For release comparisons retain existing predeclared gates: all deterministic
integrity checks pass, no new critical errors, two-percentage-point quality
non-inferiority margin, platform regression review, and improvement claims only
when paired confidence intervals support them. Resample scenario families rather
than repetitions. The 15% median input-token reduction is an optimization target,
not grounds to weaken correctness. A tiny pilot cannot establish these release gates.

## 7. Solution and Architecture

Maintain three separated artifact classes:

1. Author evidence: source/test claims, exact incidents, mutation history and rubrics.
2. Subject payloads: neutral tasks, minimum starter code/fixtures and allowed condition
   material, assembled outside the repository checkout.
3. Results: immutable answers, execution provenance, traces and independent grades.

Case lifecycle: observed -> adjudicated -> draft -> independent review -> frozen
development overlay -> authorized baseline -> candidate comparison -> promotion review.
An invalid oracle returns to adjudication; it does not become a model failure.
Already exposed cases stay development cases. New held-out families require separate
authors/review and a freeze before candidate tuning; rewording a known fix is not enough.

Required case record: ID/revision, family/split, lane, source claims, evidence paths
and hashes, test IDs and assertions, environment, neutral prompt hash, starter-fixture
hash, controller rubric, accepted alternatives, critical criteria, leakage review,
reviewer/status and baseline eligibility. Record source currency independently of
test success. A local file's existence does not establish freshness.

Required run record: case/condition/skill/payload hashes, exact model identifier and
revision if exposed, provider/client/harness versions, context limit and actual
payload size, effort/sampling, tool access, seed if supported, attempt/repetition,
answer hash, actual reads, native check results when applicable, tokens/latency/cost
availability, termination reason and redaction status. Unknown fields remain unknown.

Keep semantic quality grading blind to condition/model labels where practical.
Use a separate protocol reviewer for identity, routing and actual-read evidence.
Compile a generated solution only under the existing restricted native adapter
after review/authorization; no arbitrary model-generated shell scripts or UI tests.
Judge alternative valid code against the contract, not exact spelling of the repair.

Vary one factor at a time initially: same frontier model/harness/context for C0/C2;
then qualified C1/C3; then another frontier model. Context-pressure and local-model
diagnostics are separate lanes. Overflow is a capacity outcome, not silent truncation
or a semantic failure. Do not promise an exhaustive model x context x harness matrix.

## 8. Delivery

Phase A: adjudicate historical incidents and review draft cases.
Phase B: qualify isolated worker packaging offline and approve a bounded pilot.
Phase C: calibrate rubrics, freeze the overlay and collect authorized baseline chunks.
Phase D: resume paired UIKit work when authorized; propose targeted skill changes only
after baseline acceptance; use independent held-out cases for final review.

No dates or capacity commitments until workers accept ownership. See
[tasks](TASKS.md), [worker handoff](HANDOFF.md) and [draft prompts](subject-prompts.json).

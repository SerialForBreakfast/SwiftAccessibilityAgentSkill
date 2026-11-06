# Worker Handoff: Independent Failure-Driven Development Pilot

Status: request for review and capability confirmation, not execution authorization.
Recipient: BigDog preferred; MaxMini may accept qualified tasks. This handoff has
not been transmitted. Existing OS26 baseline review remains separate and higher priority.

## Requested Response

1. Confirm a named owner for prompt/oracle review and an owner for isolated execution.
2. Confirm exact available frontier model, client/harness, subscription-only access,
   context/tool capabilities and zero-spend stop behavior. Unknown model revision is
   acceptable as an explicit limitation, not an invented identifier.
3. Review the two proposed families below; return minimal fixture/rubric changes and
   a concrete four-cell manifest with numeric limits for owner approval.

Do not start a local-model sweep or any generation while reviewing this request.
Do not use a paid API or paid judge as a fallback. Existing subscription access is
not itself authorization to consume quota. Do not change the frozen OS26 catalog.

## Pilot Proposal

| Axis | Proposed value |
| --- | --- |
| Families | FD-P03 typography; FD-P05 captions |
| Split | New development overlay; both derived from known incidents |
| Model | One confirmed frontier subscription model, Gemini preferred if qualified |
| Conditions | C0 and C2, same frozen released skill/reference revision where applicable |
| Attempts | One first attempt per cell: four total invocations, no automatic retries |
| Context/harness | One qualified context profile and harness, identical across pairs |
| Execution | Fresh isolated sessions, balanced randomized condition order |
| Purpose | Check prompt clarity, oracle and transport; not prove improvement or rank models |

Before approval, fill exact model/settings, context/input/output ceilings, tool-call
ceiling, per-call and total wall-time limits, permitted tools, artifact hashes and
stop conditions. Include qualification probes in the approved budget if needed.
If fixtures or required source content cannot fit, stop and revise the plan openly.
Never truncate the question or omit a difficult cell silently.

C0 uses the existing generic baseline instruction. C2 uses actual frozen skill
instructions and intentionally selected source references, not hand-written repair
instructions. Select references by the declared task and freeze them before running.
Both receive the identical user question and starter fixture. Fixture preparation
must not include the corrected implementation or grading tests.

## Payload Isolation

The [prompt file](subject-prompts.json) contains draft user questions only. Do not
send the entire file to each subject: render only the selected `prompt` string with
its reviewed minimum starter fixture. This handoff, task list, incident archive,
AGENTS.md, rubric, expected routes and solution code are controller-only.

Launch outside the project checkout with no parent/project instruction discovery
or filesystem access to the controller repository. C2 gets only its allowlisted
reference bundle. Record resolved instruction/tool inputs and payload hashes.
Offline canary tests must demonstrate that controller-only material is not injected
or mounted. If the client cannot isolate these inputs, report an unqualified harness
rather than a clean C0/C2 comparison.

The prose drafts alone are not approved gold prompts. Attach minimal synthetic code
and media metadata only after review shows they are needed to remove ambiguity.
For the captions case, document whether the task asks for reasoning from a metadata
fixture or executable AVFoundation code; do not silently grade one as the other.

## Controller Rubric Preparation

For FD-P03, review effective trait-environment handling, repeat configuration,
explicit propagation/setup boundaries and a defensible numeric oracle. Accept
alternative implementations; do not require the exact repair from the archive.
Do not award claims that a font-property assertion proves visible layout.

For FD-P05, review distinguishing complete subtitles from forced-only options,
language handling, absent/unknown options and valid framework declarations. Do not
require a universal exact option count. Accept multiple correct selection strategies.

Before subject runs, an independent reviewer checks both rubrics against source
sections and native fixture evidence, with a correct answer, flawed answer and
alternative implementation. Use existing quality dimensions and critical-error
categories. C0 is not penalized for missing skill identity/routing. Protocol and read
truthfulness are graded separately. The subject model is not its own sole judge.

## Return Contract

Return a sanitized report plus machine-readable per-cell records containing:

- Approved plan ID, case/family/revision, condition, repetition/attempt and all input hashes.
- Exact exposed model identity, effort/settings, client/harness/context and permitted tools.
- Raw answer artifact/hash, actual read traces where exposed and native-check evidence
  only if separately authorized. Missing traces are unavailable, not inferred from prose.
- Input/output/reasoning tokens where exposed, reference bytes, tool count, latency,
  quota-stop/termination reason and explicit unavailable fields.
- Outcome classification: completed, timeout, quota-blocked, context-overflow,
  harness-error, unavailable capability or unattempted. Quality grading is a separate field.
- Blinded quality scores, atomic criterion outcomes, critical errors, grader identity,
  uncertainty/disagreement and final adjudication status.
- Redaction review and a list of all four planned cells, including any missing results.

Keep secrets and private deployment details outside the report. Preserve unsuccessful
answers and distinguish transport completion from task success. No retries or repair
turns without a new approved budget; never overwrite the initial answer.

## Next Gate

Return findings for maintainer review. If the pilot exposes a prompt/oracle defect,
revise the overlay and rerun only after approval; do not call changed inputs a paired
baseline. If sound, freeze a larger coverage plan and calibrate grading before
expanding to Claude/Codex or C1/C3. Additional model/harness/context variations get
separate cells and results. Skill changes wait for an accepted baseline.

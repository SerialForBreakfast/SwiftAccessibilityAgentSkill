# Evidence-led next skill version: development brief

Approved planning direction (2026-11-05): improve and validate realistic code-based gold prompts, establish baselines, then use evaluation findings to guide the next Agent/skill version. Do not silently modify released 0.2.2, frozen prompts, old results, or launch more subscription calls.

## Observed R04 regression

C2 (skill plus one manually supplied reference) emitted accessibilityAction(named:role:) and omitted an ordinary keyboard-discoverable alternative. Apple documented named-action signatures reviewed 2026-11-05 have no role argument. SDK compilation remains not_run. C0 used the documented signature plus a context menu but made an unverified Shift+F10 claim. Neither answer establishes full keyboard usability. One paired sample cannot attribute cause to the skill, reference, agent framing, or generation variation.

## Hypotheses to test, not established causes

- G-007 emphasizes custom accessibility actions but does not spell out the distinction between those actions and ordinary keyboard discoverability. The model may narrow the developer's multi-input task to the selected topic.
- Generic instruction to keep role/traits explicit may encourage blending Button(role:) with accessibilityAction(named:). The reference itself does not contain the invented overload.
- Mandatory source/freshness footer may encourage authoritative presentation without claim-level verification. C2 says HIGH/none despite unsupported API and input-mode claims.
- Additional context and installed-agent packaging may contribute. No ablation or repeatability evidence yet.

## Establish evaluation before implementation

1. Build compilable fixture hosts with stable model/callback scaffolding; specify keyboard mode, focus/activation, discovery affordance, destructive policy and supported OS.
2. Keep natural developer wording; score observable outcomes, not exact preferred code or guideline names. Retain valid alternate implementations and correct-code controls.
3. Separate compile/API validity, callback behavior, VoiceOver, keyboard/remote and review-effort checks. Unsupported/not_run must not become pass.
4. Independently review and calibrate gold acceptance tests. Freeze input/reference/rubric/source hashes; heldout new families remain outside tuning.
5. Baseline generic model, frozen 0.2.2 skill-only, reference-only, and combined where approved. Repeatability subset and compact ablations require separately approved bounded subscription use. Same wrappers/constraints; no claim of native-agent or retrieval qualification from supplied-reference lane.

## Candidate next-version changes after baseline

- Requirement-first workflow: identify required actions/input modes and invariants before routing; check patch against them before final response.
- Exact API evidence: do not infer overloads from similar APIs; distinguish semantic guidance, verified signature, availability and runtime behavior. No universal claims from general citations.
- G-007: SDK-checked minimal examples and explicit separation of VoiceOver actions, ordinary discoverable controls, keyboard activation, and destructive confirmation/undo behavior. Avoid memorizing R04 as sole solution.
- Report verified/inferred/not-tested evidence per material claim instead of treating HIGH/none as proof. Keep user-facing output concise.
- Native controls/no-op protection; minimal edits; no unnecessary availability branches for unsupported older targets, style changes, or guarantees of focus behavior.
- Release candidate tested against frozen baseline and genuinely fresh cases; investigate critical regressions individually. Compare quality plus context/output tokens and measured reviewer corrections, not verbosity or citation count.

## Acceptance direction

No known critical API/functionality regressions in the agreed release set, with independently reviewed evidence; demonstrable improvement on targeted failure families and no damage to correct-code controls. Unrun platform checks remain explicit release limitations. Exact thresholds/budget decided before candidate evaluation, not after observing results.

Primary API check: https://developer.apple.com/documentation/swiftui/view/accessibilityaction(named:_:)
Pilot summary: [developer-code pilot](evidence/pilots/bigdog/developer-code-20261105/README.md). Full prompts and responses remain private under the owner’s publication restriction.

## OS 26-first optimization proposal

Status: planning only. Establish informed behavior on OS 26 before integrating OS 27.
Released 0.2.2 and the existing 0.2.3 candidate are not changed by this proposal.
[GoldPrompts.md](../GoldPrompts.md) is the readable next-corpus catalog; its six
revised code prompts are drafts, not independently validated gold or historical inputs.

Current diagnostic: **Gemini 3.8 Flash low / 0.2.2 · W/T/L 1/4/1 across 6 pairs ·
C2 tokens 1.89× C0 · C2 suspected API errors 1 · compile/device not run.**
This is not a qualified baseline: one run per condition, unblinded review and
unvalidated fixture assumptions limit the conclusions.

### Changes to investigate after baseline freeze

| Change | Evidence or gap | Candidate implementation | How to test |
| --- | --- | --- | --- |
| Preserve the whole developer task | Deletion omitted ordinary input coverage | Identify actions, input modes, target OS and invariants before selecting a topic; check the patch against them | Callback/input-mode acceptance tests and mixed-control cases |
| Verify APIs at the point of use | Suspected blended action/role overload | Compact exact signatures and availability notes linked to SDK-checked examples; distinguish practice from API contract | Sillycon compiler/doc checks plus unseen API-adjacent cases |
| Treat different input modes separately | Keyboard claims and remote-focus guarantees exceeded evidence | Explain relevant VoiceOver, Full Keyboard Access, remote and ordinary-control paths without equating them | Separate mode-specific tests; no global accessibility pass |
| Native defaults and minimal patches | Correct Toggle needed no changes; other fixes added unrelated styling/branches | Prefer existing native semantics; preserve styles, callbacks and supported target; explicitly permit no change | Correct-code controls, patch-scope review, callback preservation |
| Replace generic certainty labels | HIGH/none accompanied unsupported code | Short material limitations: source-supported, inferred, compiled, device-tested; omit empty boilerplate | Claim-level evidence review, missing-evidence tests |
| Shrink the always-loaded skill | Existing skill spends context on identity, routing and repeated output rules | Short decision workflow and safety invariants; move explanation/examples to relevant topic files | Skill-only ablation, all-family regression checks, actual input-token totals |
| Avoid mandatory user-facing routing and branding | Extra output does not establish correctness | Keep provenance in evaluation metadata; show a concise source only when it supports a material claim or is requested | Output-token and task-success comparison; do not score format as quality |
| Remove duplicated reference prose from model-facing context | Topic files repeat rule/rationale/testing/metadata sections | Maintain a compact model-facing view generated from canonical human docs; preserve exact API qualifiers and citation pointers | Deterministic source-to-excerpt checks; compare full vs compact context |
| Load only relevant guidance | Current C2 injects the whole skill and a topic | Route to the smallest sufficient topic, expand for interop/version/evidence dependencies; avoid eager manifests/backlogs | Reference-only/full/compact ablations; later separate retrieval-selection tests |
| Make verification proportional | Generic three-step checklists can omit the real interaction | Patch first; brief rationale; only checks that establish the requested behavior and actual limitations | Review effort, omission rates, output tokens; no fixed verbosity reward |
| Track yearly behavior as explicit deltas | API introduction and behavior changes can differ | Stable OS 26 guidance plus versioned evidence-backed additions/exceptions after baseline acceptance | Sillycon per-SDK tests, documented behavior matrix and retained OS 26 regression suite |

These are hypotheses, not promised savings or adopted rules. Do not remove source
qualifiers or required user context to hit a token target. Do not force a particular
patch into the prompt so that the candidate appears to improve.

### Bounded work packages and gates

| ID | Work | Expected evidence / owner boundary | State |
| --- | --- | --- | --- |
| O26-01 | Validate six revised code fixtures and add missing development families | Buildable hosts, independent acceptance review, declared platform/input modes; Sillycon’s planned checks are a dependency, not delivered evidence | Proposed |
| O26-02 | Freeze OS 26 corpus, references and grading | Hashes, review rubric, valid alternatives, withheld fresh families, exact SDK/runtime matrix | Blocked on O26-01 |
| O26-03 | Establish generic and frozen-skill baselines | Same wrapper/model/settings; generic, skill-only, reference-only and combined conditions; small repeated subset; separate owner-approved invocation budget | Blocked on O26-02 and batch approval |
| O26-04 | Create compact Agent instructions and reference packaging candidate | Separate candidate version, measured context footprint, provenance retained, no released-skill overwrite | Blocked on baseline findings |
| O26-05 | Add targeted behavior/API evidence improvements | Every change maps to a failure class and regression fixture; compiler claims require actual SDK results | Blocked on O26-03 |
| O26-06 | Evaluate candidate against frozen baseline and fresh cases | Paired outcomes, confirmed/suspected critical defects, tokens, measured correction effort, honest not_run reporting | Blocked on candidate and batch approval |
| O26-07 | Review OS 26 adoption | Independent review; explicit acceptance decision and remaining native limitations | Blocked on O26-06 |
| O27-01 | Integrate OS 27 deltas | New versioned sources/tests; preserve frozen OS 26 behavior; separate OS 27 scores and approval | Blocked on O26-07 |

Sillycon is creating documentation/unit tests and yearly-release comparisons per
the owner. This plan relies on their results where applicable but does not claim
those tests exist, passed, or establish VoiceOver/keyboard behavior. No new worker
message, assignment or execution is implied by this document.

### Experiment and adoption discipline

1. Fix environment and case semantics before freezing. Pin 26.x SDK and runtime
   patch versions, input mode, fixture host and actual model/client identity.
2. Preserve the old pilot as historical evidence. The old checkout constraint had
   a bare `.isActive` read rather than activation; the revised prompt corrects it.
   The revised deletion prompt specifies Full Keyboard Access and discoverability.
   New baselines are required for both; never reuse old grades as new-case scores.
3. Separate causes with small ablations: skill-only, reference-only, combined;
   then compact instructions and compact reference excerpts. Keep the condition
   matrix explicit rather than relabeling these new lanes as old C1/C2/C3 results.
4. Use development data for iteration. Freeze the candidate before fresh-case
   evaluation; never tune against heldout failures and still call them heldout.
5. Provisional optimization objective: investigate at least 25% lower measured
   total context/output tokens against frozen combined guidance, while preserving
   required behavior. This is a target to validate, not a release result or a quota
   conversion. Pre-register final quality/token thresholds before candidate runs.
6. Do not trade a new critical API or lost-functionality regression for token
   savings. Preserve correct-code controls. Small samples cannot establish zero
   population risk or statistical noninferiority; report uncertainty honestly.
7. Publish one-line performance and per-case reasons. Keep calls, incomplete
   results, abstentions and unknown validation visible. No automatic batch renewal.

### One-line result format

`Model / skill / corpus | W/T/L x/y/z of N | accepted fixes x/N or unknown |
critical confirmed/suspected x/y | tokens vs baseline x.xx× |
compile x/N; device x/N or not_run`

For today, accepted fixes, confirmed compile outcomes and device behavior remain
unknown. The six static paired judgments are useful diagnostics, not six qualified
end-to-end acceptance tests. See GoldPrompts.md for metric definitions.

## Methodology implementation update — 2026-11-05

[Review decisions](METHODOLOGY-DECISIONS-2026-11-05.md) distinguish adopted advice,
corrections and deferred work. [OS26 promotion protocol](os26/README.md) and the
offline readiness gate now enforce evidence presence before a runnable plan. Six
revised development cases are machine-readable, with separate atomic criteria and
matching GoldPrompts.md. No native evidence, gold promotion, inference or skill
implementation is claimed. O26-01 remains pending fixture/oracle delivery.

The shared answer suffix and implementation hints were removed. Essential product
requirements remain visible. The Toggle control now uses neutral review wording;
the deletion case is explicitly a regression. Keep representative baseline successes
as well as labeled headroom challenges. Existing release-gates.json and old grading
remain frozen; future statistical policy must be preregistered, not retrofitted.

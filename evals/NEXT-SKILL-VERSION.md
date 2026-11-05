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

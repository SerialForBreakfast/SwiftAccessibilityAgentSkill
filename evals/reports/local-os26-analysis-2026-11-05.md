# MaxMini diagnostics: baseline implications

## Evidence and scope

Reviewed upstream `c73cca1782e1e7d5e4d20d675ba0a2c892173fae`, its
[report](local-os26-model-testing-2026-11-05.md) and
[compiler probe](../runner/local-os26-code-gate.mjs). Both are preserved unchanged.
Raw answers and compiler artifacts were not available in this checkout. Semantic
findings are reported by MaxMini, not independently rescored here. No new inference
was run. These six development cases support failure discovery, not a model ranking.

## Useful findings

- Fluent answers reportedly contain invalid API overloads and a nonexistent
  modifier. Protocol compliance cannot substitute for compilable, useful fixes.
- All three sampled models missed requirements in GP26-04. Keep the on-screen
  control requirement alongside accessibility shortcuts; do not weaken it to
  improve local-model scores.
- GP26-06 demonstrates the value of correct-code controls: an appropriate
  no-change answer deserves credit. Extra accessibility overrides are not
  automatically improvements.
- Hidden-descendant and stale-state mistakes align with useful fixture mutations.
  Passing reference-fixture tests does not mean generated answers were tested.
- Keep local models as diagnostic inputs. These results neither establish their
  general inability to code Swift nor justify making them the optimization target.

## Grading limitations

| Evidence | Treatment |
| --- | --- |
| Skill plus selected references supplied for every answer | C2-like only. Without matched C0/C1 arms there is no estimate of skill uplift. No C3 retrieval trace is established. |
| References supplied6/6 | Injection is not evidence of agent-selected retrieval or actual use. Score these separately from routing text. |
| Six cases,900-token cap, one configuration | Descriptive findings, not broad coverage. Preserve truncation and separate it from semantic failure. |
| Only the first strictly fenced Swift block extracted | Later blocks, partial patches and formatting variations can be missed. Extraction failure is not compiler rejection. |
| GP26-03 probe supplies `let view = UIView()` | This masks the reported undefined-`view` defect. Wrapped type-check success is not proof of a drop-in fix. |
| GP26-05 probe expects a view-body expression | A complete declaration can fail because of wrapper shape. Separate integration errors from generated-code errors. |
| GP26-06 emits no Swift block | A valid no-change review can succeed semantically. Mark compilation not applicable where code is unnecessary; do not interpret the probe's `compileFail` aggregate as task failures. |
| Static hazard regexes | Triage hints only. Valid trailing-closure `Button { ... } label: { ... }` syntax need not match `Button(`. Comments and alternate solutions also affect these checks. |
| Identity versus routing-first scores | The frozen skill requests first-turn identity and also says routing first. Predeclare a consistent grading interpretation; identity followed by routing is not automatically a routing failure. Record session/turn boundaries. |
| Mutable model tags and limited metadata | Request exact model digest/revision, runner/input hashes, stop reasons, context usage and raw-record hashes where available. Record unavailable metadata honestly. |
| SDK27 with deployment target26 | Evidence applies to that combination, not SDK26 or every26.x runtime. Hard-coded SDK paths also restrict probe portability. |

The report's human-review recommendation describes its diagnostic workflow. It
does not add mandatory manual accessibility verification or UI tests to promotion.
Independent source/code review remains the agreed gate.

## Reconciled native results

MaxMini's partial native run remains incomplete. The separate
[completed local matrix](../os26/reports/2026-11-05-r4/README.md) records six
candidate passes and twelve intended assertion failures with the diagnostic and
timeout safeguards. Keep these as distinct runs, not pooled repetitions. Later
success does not retroactively turn an interrupted run into a mutation kill.

All six cases still await independent review. Unit passes establish the scoped
fixture behavior, not model quality or promotion approval.

## Next actions

1. BigDog reviews the merged revision and sanitized native evidence, especially
   control wiring to tested handlers, source support, accepted alternative fixes
   and result classification. Record real approval or findings before promotion.
2. Before formal reuse of the compiler probe, test full declarations, partial
   patches, multiple blocks, correct no-change answers and trailing-closure
   controls. Separate extraction, integration, compilation, infrastructure and
   semantic outcomes. Preserve raw answers and record any reviewed adaptation;
   never silently repair model output. These are follow-up tasks, not changes
   implemented in this review.
3. Freeze the rubric interpretation and matched C0/C1/C2 inputs for a bounded
   Gemini run. C0 is not penalized for missing branding. C1 must distinguish
   proposed lookups from consulted references. C3 remains a separate traced lane.
4. Confirm subscription model/revision, quota and explicit bounded execution
   authorization. No paid fallback, model substitution or new inference is
   authorized by this document.
5. Let frontier results drive skill changes. Retain local failures as regression
   and harness stress cases. Preserve frozen0.2.2 instructions, heldout questions
   and historical results until benchmarked changes are justified.

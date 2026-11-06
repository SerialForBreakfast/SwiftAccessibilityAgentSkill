# OS26 expansion 1: implementation and validation handoff

**6 concrete draft prompts · 48 acceptance gates · 0/6 gold-ready · no new model calls.**

[Read each exact question and Swift snippet](PROMPTS.md) · [Evaluator-only criteria](acceptance.json) · [Recorded offline readiness](readiness.json) · [Approved scope proposal](../../BASELINE-EXPANSION-PROPOSAL-2026-11-05.md)

Owner accepted the six-case preparation/Apple-validation scope. This is an isolated draft revision `os26-expansion-1-draft-1`, not an edit to the existing six gold prompts. GP26-07…12 correspond to proposal E01…06. The original prompt catalog, skill0.2.2, released baseline, historical reports and provider settings remain frozen. No new subscription allocation follows from this handoff.

| Case | Concrete task | Execution order | Current state |
| --- | --- | --- | --- |
| GP26-07 | Payment dismissal resolves current origin or fallback | UIKit first | Host/tests/review pending |
| GP26-08 | Custom popup containment and symmetric cleanup | UIKit first | Host/tests/review pending |
| GP26-09 | Knob value, adjustable hooks, bounds and callbacks | UIKit first | Host/tests/review pending |
| GP26-10 | Progress exposure and per-operation terminal deduplication | UIKit first | Host/tests/review pending |
| GP26-11 | Review a native Slider without unnecessary changes | SwiftUI follow-on | Draft prepared; native work deferred behind UIKit-first work |
| GP26-12 | Review preference-aware motion without resetting state | SwiftUI follow-on | Draft prepared; native work deferred behind UIKit-first work |

## Task ownership and files

BigDog authored the prompt/acceptance drafts; Sillycon reviews these and owns the native fixture implementation and test execution. BigDog independently reviews Sillycon's implementation, test linkage and returned evidence. Record review ownership per component: neither author independently approves their own code.

Use `evals/os26/expansion-1/` for new fixture sources, host/test setup, versioned variant manifests and sanitized validation reports. Reuse relevant already-implemented UIKit utilities where appropriate, recording their source hashes and actual production linkage. A matching topic or existing library test count does not qualify a new evaluation fixture. Preserve Sillycon's uncommitted UIKit work and pending receipt-assembler reconciliation. Do not overwrite either assembler version or redo already completed library runs merely to start this task.

Changes outside the expansion directory, especially shared runner/assembler wiring, must be proposed as a separately identified dependency before editing. Do not register these drafts into the active frozen catalog or edit `SKILL.md`, baseline files, prior reports or existing six-case fixtures. Build native scaffolding locally as needed; no new dependency downloads, credentials, model execution or UI tests are requested.

## Native acceptance work

1. Review exact developer requirements and API availability. Source links in `acceptance.json` are discovery candidates, not independent-source-review receipts. Correct ambiguous requirements before freezing; increment the expansion revision and preserve old bytes if exact prompts or criteria change. Do not silently add requirements to model grading.
2. Build a minimal host for each case. Preserve the supplied code context and actual callback/view wiring. Establish a reviewed good variant plus two single-error variants with hashed source and a common focused test selection. For the correct-code controls, unchanged code is a legitimate good variant.
3. Execute the good and both mutants with the same tests. Each mutant must fail its intended assertion; compiler failures, timeouts and missing tests do not count as mutation kills. Record failures from early revisions rather than replacing them with a later success.
4. Exercise the real accessibility override, binding, callback or state path. An injected notification/dismissal boundary must default to UIKit and be called by production code. Source-check that a SwiftUI control consumes the exact tested binding/policy; do not qualify detached helpers. If a promised unit observation is unsupported, report it as blocked/not_assessable and propose an honest criterion revision.
5. Return source commit; exact prompt/acceptance/host/suite/variant hashes; selected and executed test IDs; pass/fail/skips/counts; exit/signal/error; failed and expected-failure IDs; SDK/build, runtime/build and deployment target; review provenance; sanitized evidence paths and remaining gaps. Full logs/xcresults remain private. SDK27 targeting26 and runtime26.5 must not be called actual26.0 execution.

These gates measure compile/unit/source-review behavior. They do not establish actual VoiceOver traversal/speech, keyboard interaction, animation rendering or accessibility usability. No manual/UI evidence is required by this task. Generated-model-answer validation is a separate stage after fixture promotion and an approved model run.

## Keep model and evaluator inputs separate

Only `modelInput(prompts, id)` from the existing `evals/runner/os26.mjs` may form the eventual user input. It returns the exact question and snippet. Never supply acceptance keys, control labels, variants, readiness reports or reference solutions to the model. `PROMPTS.md` is the human catalog, not a concatenated model input.

`input-pins.json` pins draft inputs. `readiness.json` was generated with the existing assessor and no evidence: all48 gates remain blocked. The existing CLI defaults to the original catalog; passing a receipt path does not select this expansion. Use the existing exported functions with explicit expansion files, as shown below. No replacement runner or bypass is introduced.

```sh
node --input-type=module <<'JS'
import fs from 'node:fs';
import {assess,digest,plan} from './evals/runner/os26.mjs';
const dir='evals/os26/expansion-1/';
const p=fs.readFileSync(dir+'prompts.json'),a=fs.readFileSync(dir+'acceptance.json');
const prompts=JSON.parse(p),acceptance=JSON.parse(a);
const readiness=assess(prompts,acceptance,null,
  {promptHash:digest(p),acceptanceHash:digest(a)},dir);
console.log(JSON.stringify(readiness,null,2));
// plan(prompts, readiness) must reject until real reviewed evidence is supplied.
JS
```

## Source discovery, not completed review

Apple's adjustable trait documentation explicitly connects the trait to increment/decrement overrides; the Slider initializer documentation describes the supplied label's accessibility use. These were checked during draft preparation. The remaining exact API signatures, lifecycle assumptions and deployment availability still need the independent native/source review. Do not generalize documentation search snippets into executed evidence.

- [UIKit adjustable trait](https://developer.apple.com/documentation/uikit/uiaccessibilitytraits/adjustable)
- [SwiftUI Slider](https://developer.apple.com/documentation/swiftui/slider)
- [UIKit layout-change notification](https://developer.apple.com/documentation/uikit/uiaccessibility/notification/layoutchanged)
- [SwiftUI reduced-motion environment](https://developer.apple.com/documentation/swiftui/environmentvalues/accessibilityreducemotion)

## Communication and next steps

Sillycon: acknowledge the original coordinator handoff, confirm the UIKit-first implementation scope and identify any concrete blocker. Report accepted work separately from message read. Return results through the existing project coordinator; any Samba artifacts need their own corresponding coordinator message with exact paths/hashes. No artificial overall deadline or scheduled task is created.

BigDog: reconcile delivery by the original operation, review returned sources/evidence and promote only cases with actual acceptance evidence. Keep the prior six AGY outputs private and their native checks unclaimed. Ask for a fresh finite model batch only after the new fixtures qualify.

Owner: no action is needed to start this approved preparation/validation work. A future model run is a separate approval after readiness is demonstrated.

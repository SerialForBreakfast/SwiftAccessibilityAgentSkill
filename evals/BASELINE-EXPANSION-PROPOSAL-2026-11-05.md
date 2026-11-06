# Proposed OS26 baseline expansion

**Current: 6 validated cases, all exercised. Additional validated cases: 0. Proposal: 6 new development cases / 12 conversations after validation. No inference authorized by this document.**

Owner subsequently approved preparation and Apple-validation coordination. [Concrete draft prompts and handoff](os26/expansion-1/README.md) now exist; new inference remains unapproved. The proposal below is retained as the scope decision.

Inspected local and origin/main revision `2e90744` on 2026-11-05. The six existing gold cases remain frozen. The latest AGY batch produced 12 responses; its 1-better / 4-comparable / 1-worse result is a single unblinded source review, not generated-answer Apple validation or a release gate. Do not change skill0.2.2 before establishing the broader baseline.

## What exists, and what is actually ready

| Inventory | Count | Disposition |
| --- | ---: | --- |
| `os26/prompts.json` with closeout readiness receipt | 6 | Six gold-ready code-contract cases; all six already used in the AGY pair comparison |
| `promptfoo/gold-prompts.md` | 20 | Historical natural-language routing/identity catalog; not 20 additional validated code fixtures |
| `promptfoo/context-budget-gold-prompts.md` | 6 | Context-budget candidates; evaluate retrieval separately from answer quality |
| `promptfoo/viewlens-gold-prompts.md` | 8 | Runtime-evidence reasoning prompts; no Apple oracle promotion shown for these prompts |
| `scenarios.json` | 60: 40 development, 20 heldout | Broad legacy suite; overlaps the catalogs above, not 60 independently new cases |

These counts must not be added as unique questions. GP-011/CB-001/D01 repeat the UILabel question; GP-018/CB-004/VL-003 overlap evidence-boundary reasoning. Old catalogs reward protocol fields; our primary endpoint is useful, correct developer answers. Identity/routing compliance stays separate.

The current closeout receipt records 6/6 ready. `os26/README.md` still says 0/6 and contract4: that is stale introductory text, not contrary execution evidence. Historical audits also describe earlier blocked states. This proposal does not rewrite those artifacts or silently promote other catalogs.

## Recommended six additions

IDs below are proposal-local, not registrations in the frozen gold catalog. Each final question must include the actual minimal Swift implementation and essential product constraints, not just the one-line brief below. Expected fixes and mutation labels stay outside model input.

| Proposed case | Developer question / code fixture to author | Coverage added | Legacy seed |
| --- | --- | --- | --- |
| E01 · Dismissal target | “This payment panel can be opened from several rows. After it closes, how should this code choose where to return attention when the originating row may have disappeared?” Supply presenter/dismiss callback, stable row IDs, list-refresh behavior and a declared persistent fallback control. | Update-time target selection, lifecycle, absence handling | D06 / GP-005 family; use iOS UIKit for this tranche |
| E02 · Custom popup | “VoiceOver still reaches controls behind this custom popup. Here is the show/close code. Fix it without leaving the screen inaccessible after closing.” Supply overlay view hierarchy, dismissal and underlying accessibility state. | Modal configuration and symmetric cleanup | D17, adapted to a minimal UIKit host |
| E03 · Adjustable control | “This volume knob only responds to dragging. Here is its value and update callback. Make its current value and adjustments accessible without changing its 0…100 range or update behavior.” Supply a custom UIView with the real drag/value path. | Role/value/action semantics, boundary and callback correctness | D08 |
| E04 · Progress reporting | “Every progress update is spoken over other content. Here is the download callback. Keep progress available, report completion or failure, and avoid repeated speech on duplicate terminal events.” Supply UIKit progress callback, download ID, status transitions and notification emission. | State versus announcements, deduplication, new-operation reset | D10, translated to a directly testable UIKit host |
| E05 · Native slider control | “Review this volume setting for accessibility. Identify any concrete issue and preserve its behavior.” Supply a correctly labeled native SwiftUI Slider, declared range and a working persisted binding. | Second no-defect control, native value/range semantics | New development control; not a heldout case |
| E06 · Reduced-motion control | “Review this transition for accessibility while keeping the selected page and navigation behavior.” Supply correct reduced-motion environment handling, an animation policy and stable page state. | Motion preference, task continuity, third no-defect control including existing GP26-06 | D16 family, newly authored correct implementation |

Do not tell E05/E06 models that they are known-good or that a no-op is expected. Do not manufacture an error to make C0 fail. Balanced outcomes are useful baseline data. Existing six plus these six would give nine repair tasks and three correct-code controls.

## Validation required before calling these gold

All six need independent Apple source/availability review, a buildable minimal host, a reviewed good implementation and two single-defect variants rejected by the same focused tests. Alternative valid implementations receive equal credit. The following are proposed measurable endpoints, not claims that tests already exist:

| Case | Unit/source endpoint | Two proposed defects the oracle must detect | Explicit non-claim |
| --- | --- | --- | --- |
| E01 | Resolve existing origin by stable ID; choose declared fallback when missing; verify dismissal completion invokes the production notification boundary with that target | Wrong surviving row; stale/missing target rather than fallback | No observed VoiceOver movement or timing guarantee |
| E02 | Check actual overlay modal/element configuration and restoration of preexisting background accessibility flags on close, including repeated cycles | Missing containment configuration; background remains hidden after close | No measured VoiceOver traversal |
| E03 | Invoke actual accessibility increment/decrement entry points; assert bounded current value/label and exactly one callback per real change, no callback at a clamped boundary | Out-of-range value; dropped/duplicate callback | No real assistive-technology gesture delivery |
| E04 | Feed production callback sequences; verify exposed value, absence of per-tick announcements, one terminal event per operation and reset for a new ID | Announce every tick; duplicate/suppressed terminal notification | No measured speech interruption, delivery or listening experience |
| E05 | Compile native Slider construction; test the same binding consumed by the control and its valid range; review native semantics | Constant binding; wrong declared range | No observed interaction/speech; a valid unchanged answer must not fail for lacking a code block |
| E06 | Unit-test the production animation-policy choice for preference changes and confirm selection persists; review actual view uses that policy | Ignores reduced-motion preference; resets selected page on preference change | No rendered animation or comfort/usability qualification |

A spy or extracted policy is useful only if source review establishes the actual view/callback uses it. Never test an independent helper and claim it validates unrelated model output. If the endpoint cannot be observed under the agreed compile/unit/source-review scope, narrow the claim or leave the case blocked; do not introduce mandatory UI/manual gates.

Use the qualified Apple environment with exact SDK/runtime/deployment identities; OS26 target does not mean an actual26.0 runtime. Sillycon is the native validation peer. Their separate ADR003 examples pilot is not automatically a generated-answer adapter. This proposal does not dispatch native work or assign a deadline.

## Sequence and bounded cost

1. Preserve current answers and close their explicit adaptation/source-review questions first, especially GP26-03. Native checks must compile the actual supplied answer with only declared surrounding context; record adaptation diffs and `not_assessable` cases. No silent solution repair.
2. Author E01–E06 prompts, independent acceptance keys and hosts. Review exact Apple sources and demonstrate the good/mutant matrix. Freeze all hashes before inference. Keep current reports and six questions unchanged.
3. Proposed next generation batch: six new cases × C0/C2 × one repetition = **12 conversations**. Same model/effort/session isolation and frozen0.2.2 context policy; alternate order. Fresh owner subscription allocation required after validation. No screening calls or automatic retries.
4. Optional, separately approved repeatability batch: existing GP26-03 and GP26-06 × C0/C2 × two additional repetitions = **8 conversations**. This would yield three samples per condition for each of these deliberately diagnostic families, not a representative population estimate. Report every outcome; do not select the best response.
5. Only then freeze a candidate skill revision. Author fresh evaluation-only families with a reviewer who does not tune on their answers; do not reuse the inspected development prompts as heldout. Keep existing heldout questions/labels unchanged. No heldout question is selected or rewritten here.

The last six-pair batch used47,338 reported tokens. An equally sized12-conversation batch might be on that order; the optional8 would be approximately31,559 at that observed average. **Planning estimates only:** final input/reference sizes and answer lengths are unknown. No output-token/internal-request cap or subscription percentage conversion is implied. The rounded67%→66% quota display cannot budget exact future capacity.

## What to score at a glance

Per case: exact developer question, C0/C2 task outcome, confirmed versus suspected code defect, unsupported claims, unnecessary changes, required adaptation, native pass/fail/not_run/not_assessable, tokens and latency. Keep source-review pair preference separate from executed acceptance. Correct unchanged code can earn full credit. Hide condition names for independent grading where possible; report disagreements and adjudication instead of presenting our current unblinded review as calibrated evidence.

Defer AppKit/visionOS/watchOS and OS27 deltas to subsequent tranches; this proposal broadens the existing iOS lane, not all-platform qualification. Defer trigger/identity and retrieval/context-budget experiments because manual C2 reference injection cannot measure host routing or retrieval efficiency. No screenshots are needed to test these code contracts.

## Next steps

**Owner:** review the six-case mix and the12-conversation proposal. There is no model run to approve today: first make these fixtures gold-ready. The optional8-conversation repeat batch is a separate decision.

**BigDog:** prepare the exact code prompts and acceptance drafts after scope acceptance, coordinate the existing answer-validation path with Sillycon, and retain the baseline/receipts unchanged. Send an explicit coordinator handoff when native work is requested; Samba artifacts always get a matching notification. No scheduled follow-up or new provider call is created by this proposal.

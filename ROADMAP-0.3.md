# Roadmap to a production-quality 0.3.0

Draft, November 7, 2026, revised after review the same day. It replaces §8–9 of [CurrentStatusReview.md](CurrentStatusReview.md) for planning. It is based on the [rc.1 result](evals/rc1-comparison/RESULT.md). Nothing here authorizes model runs, spend, messaging or changes to 0.2.2 or rc.1. **rc.1 stays frozen; the next model run is on hold** until the gates under "Before any dispatch" pass.

## What the rc.1 return taught us

1. **Running the code finds defects that reading misses.** On checkout-font, the masked source review passed answers that fail the contract natively. That validates the native grader. It does not show that either skill version improves answers.
2. **The 12 rc.1 tasks have no headroom.** Every arm passes the other 11. Prompts state the rule, and the tasks test API recall. They become regression controls.
3. **rc.1's routing works once loaded.** When invoked explicitly it read references in 3/3 sessions; 0.2.2 did in 0/3. Explicit invocation is the clean way to test content.
4. **Automatic loading was rare: 1/12 per version.** That is not proof of a routing defect. Several prompts are ordinary app logic where skipping an accessibility skill may be correct. Discovery has to be measured on prompts labeled in advance, counting false activations as well as misses.
5. **The protocol let one authorization fund two jobs:** 46 sessions against 36. The answer contract invited a file write. Both are fixed offline (below) before anything else is dispatched.

## Done in this tranche (offline, no model calls)

| Item | Where | Check |
|---|---|---|
| Attempt-reservation ledger. Each session is reserved against the original authorization before it opens; a changed prompt, derived packet, restart or continuation is refused. | [evals/protocol/ledger.py](evals/protocol/ledger.py) | [test_ledger.py](evals/protocol/test_ledger.py) replays the rc.1 history: one partial return (10 attempted), 36 refusals, 0 later launches |
| Answer contract: exactly one fenced Swift block, no file edits. A strict extractor accepts one unambiguous block unchanged and records ambiguity instead of guessing. | [evals/protocol/answer_contract.py](evals/protocol/answer_contract.py) | [test_answer_contract.py](evals/protocol/test_answer_contract.py): all 36 rc.1 answers accepted, same bytes as reviewed |
| Grader takes one immutable byte buffer for approval, storage and compilation; structured `--result`; write-once scorecards | [grade.py](evals/rc1/grader/grade.py) | rc.1 fixtures still qualify |
| Native lane: warm-up with trusted fixtures, resume only ungraded cells with matching fingerprints, stop at the first infrastructure error, one record per cell | [native_lane.py](evals/rc1-comparison/native_lane.py) | First results adopted; rerun and re-adopt refused |
| Linked verifier: answer → extracted hash → task and oracle → scorecard → summary row → RESULT.md table; sanitized public summary | [verify_return.py](evals/rc1-comparison/verify_return.py), [summary.json](evals/rc1-comparison/summary.json) | Re-derives 33/3 from private evidence; checks public consistency in a clean checkout |
| Sealed packet verified at the revision that sealed it, with the post-return grader recorded separately | [verify_pinned.py](evals/rc1-comparison/verify_pinned.py) | Packet `496c51e0…` verifies at `ba50721` |
| Two contrasting checkout-font contracts (supplied setting wins vs. live environment wins) | [evals/headroom/checkout-font/](evals/headroom/checkout-font/README.md) | 5 valid variants pass, 6 mutants fail, including both observed rc.1 failures |

## Before any dispatch (gates on the next packet)

1. **Dress rehearsal passes.** It reproduces the native summary from linked scorecards, keeps the sealed and rewritten cohorts distinct, refuses a 37th reservation and a changed prompt, and produces a decision-first report. See `python3 -B evals/protocol/rehearse.py`.
2. **The packet uses the ledger and the answer contract.** The handoff makes the worker reserve before each session and return the ledger file.
3. **Every task in the packet is qualified natively.** Its accepted alternatives pass and its mutants fail.

## Production bar for 0.3.0

All gates are measured on the frozen suite with the same native harness:

| Gate | Threshold |
|---|---|
| Usefulness vs unaided, **transfer** cases | Explicit rc.2 beats unaided by ≥ 25 points in paired pass rate, sign-test p < 0.05 over tasks × repeats |
| Usefulness vs 0.2.2, transfer cases | Not worse on any task's majority result |
| Regression controls (ceiling tasks) | 0 losses vs 0.2.2 |
| Discovery, should-invoke prompts | Invoked ≥ 60% |
| Discovery, should-not-invoke prompts | Invoked ≤ 10% (false activations) |
| Coverage | ≥ 2 transfer cases in each of six cells: iOS, macOS and tvOS × UIKit and SwiftUI, with AppKit counting toward macOS |
| Grading | Native compile and unit outcome for every gradable answer; format and invocation graded separately; source review only for criteria units can't check |

## Phase 1: Discovery, measured separately from usefulness

- **Discovery corpus:** `evals/trigger-corpus/`, about 120 natural prompts.
  - Each is labeled before any run as **should invoke**, **should not invoke** or **ambiguous**, with a one-line reason.
  - Sources: the 60 scenario families in `evals/scenarios.json`, the rc.1 prompts (several are ordinary app logic and may belong under "should not") and plain Swift questions.
  - A third is held out.
  - Report misses, false activations and the ambiguous rate.
- **rc.2 description:** rewritten against the labeled corpus. Keep the platform scope and the exclusion for unrelated Swift.
- **Exit:** labels, corpus and description frozen and checked in. Activation is measured only in Phase 4.

## Phase 2: Decision suite (dev cases + transfer cases + regression controls)

- **Choose decisions by evidence.** A decision enters the suite when models demonstrably get it wrong. Current evidence:
  - checkout-font ownership: 3/3 skill-arm failures;
  - GP26-03 checkout with an existing Pay action: 4/4 unaided;
  - GP26-11 already-working Slider: 4/4;
  - GP26-04 deletion without swiping: 2/4;
  - media ownership: 1/1;
  - failure families A–F in CurrentStatusReview §5.
- **Development cases:** the known incidents (above), used for authoring and tuning. They are not fresh holdouts.
- **Transfer cases:** new tasks that exercise the same decision in different code, written without looking at model answers to the incident. The usefulness gate is measured only on these. Otherwise we'd only show that yesterday's examples are fixed.
- **Regression controls:** the 12 rc.1 tasks and any case every arm passes. A loss here blocks promotion.
- **Each task needs:**
  - a realistic starter;
  - a natural request that doesn't state the rule;
  - hidden unit contracts;
  - every valid alternative we know, qualified to pass;
  - mutants, qualified to fail.
- Contrasting pairs like the two checkout-font contracts are preferred where one decision has two correct answers depending on context.
- **First cut:** 6 development cases plus 6 transfer cases, one of each per cell.

## Phase 3: Content (rc.2)

- rc.2 is a new semantic version; rc.1 stays frozen.
- **First change, from direct evidence:** a text-size card that asks which setting owns the label.
  - Caller-supplied setting → scale explicitly and leave automatic adjustment off.
  - Live environment → `scaledFont(for:)` with automatic adjustment, or rescale on trait changes.
  - Both checkout-font contracts must pass with the card. The observation stays scoped to the tested configuration.
- **Then:** GP26-03 and GP26-11 guidance, worked offline from the failure-replay bundle's `NEXT.md`.
- **Each change records** the evidence it answers, the criterion it targets, and the tasks it must not break.
- Example cards from the 46 tested packages, only for decisions in the suite, on demand.

## Phase 4: One decisive run (prepared here; dispatched only with D1)

Every cell is spelled out.

| Lane | Arms | Tasks | Repeats | Sessions |
|---|---|---|---|---|
| Usefulness (explicit; unaided gets the same prompt with no skill installed) | unaided, 0.2.2, rc.2 | 12 (6 dev + 6 transfer) | 3 | 108 |
| Discovery (automatic, installed) | 0.2.2, rc.2 | 24 labeled prompts (12 should, 8 should-not, 4 ambiguous) | 1 | 48 |
| Regression controls (explicit) | 0.2.2, rc.2 | 12 rc.1 tasks | 1 | 24 |
| **Total** | | | | **180** |

- **Minimum variant:** usefulness at 2 repeats gives 72 + 48 + 24 = 144.
- **Primary endpoint:** usefulness on transfer cases.
- **Secondary endpoints:** dev-case usefulness, discovery misses and false activations, regression losses.
- **Execution:**
  - one sealed packet, one return, the ledger enforced per session;
  - the answer contract in every prompt;
  - an interface failure stops the job and is returned as partial.
- **Grading:** the reviewed local native lane; the return ingested and checked with a verifier like [verify_return.py](evals/rc1-comparison/verify_return.py).

## Phase 5: Process rules

- **Decision first in every return.** Open with:
  - the authorization outcome (complete, partial or blocked);
  - whether a promotion decision follows;
  - the actionable findings.
- **Then the separate rows:**
  - sealed vs. diagnostic evidence;
  - source vs. native grades;
  - invoked vs. reference reads.
- The report's evidence table is generated from the summary and verified ([RESULT.md](evals/rc1-comparison/RESULT.md) is the template).
- **One status file:** [STATUS.md](STATUS.md).
- **Gate on the result:** no new candidate starts before the previous run's gate result is recorded.

## Owner decisions

| ID | Decision | Status |
|---|---|---|
| D1 | Quota for Phase 4: 180 Haiku 5.5 low sessions (or 144 at two repeats) | Open; after the gates above pass |
| D2 | Native grading lane | **Decided November 7:** reviewed local lane, no VM or separate user ([rule](evals/rc1/README.md)) |
| D3 | Release target: Haiku low only, or also a frontier model such as Sonnet 5.5 | Open |

## Next offline actions

1. Draft the rc.2 text-size card and confirm it against both checkout-font contracts (Phase 3).
2. Build the labeled discovery corpus (Phase 1).
3. Write the first transfer cases for checkout-font ownership and GP26-03 (Phase 2).

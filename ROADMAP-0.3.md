# Roadmap to a production-quality 0.3.0

Draft, November 7, 2026, revised twice after review the same day. It replaces §8–9 of [CurrentStatusReview.md](CurrentStatusReview.md) for planning. It is based on the [rc.1 result](evals/rc1-comparison/RESULT.md).

**The owner sets budget, scope and stopping policy.** This document lays out options and what each would tell you. It doesn't authorize model runs, spend, messaging or changes to 0.2.2 or rc.1. The zero-extra-spend policy stays unless the owner changes it. rc.1 stays frozen.

## What the rc.1 return taught us

1. **Running the code finds defects that reading misses.** On checkout-font, the masked source review passed answers that fail the contract natively. That validates the native grader. It doesn't show that either skill version improves answers.
2. **The 12 rc.1 tasks have no headroom.** Every arm passes the other 11. They become regression controls.
3. **rc.1's routing works once loaded.** Explicit invocation read references in 3/3 sessions; 0.2.2 did in 0/3. Explicit invocation is the clean way to test content.
4. **Automatic loading was rare (1/12 per version), but that isn't proof of a routing defect.** Several prompts are ordinary app logic where skipping an accessibility skill may be correct.
5. **Permission and interpretation are separate.**
   - 36 sessions was the owner's limit for that run, not a rule.
   - The owner can authorize BigDog up front to fix a delivery problem and continue within one handoff.
   - What doesn't change: answers from a changed prompt are a separate comparison and are never pooled with the original.

## Questions, in priority order

| Priority | Question | How to test it |
|---|---|---|
| 1 | **Does the new guidance improve code?** | Explicitly invoke each version on the same realistic tasks. This separates the content change from whether the agent discovers the skill. |
| 2 | **Is an apparent improvement repeatable?** | Repeats across a mix of tasks chosen in advance, not just the cases whose first results surprised us. |
| 3 | **Will developers benefit without asking for the skill?** | A separate automatic-invocation test, on prompts where invoking *and* not invoking are both appropriate. Report false activations as well as misses. |

## Done (offline, no model calls)

| Item | Where | Check |
|---|---|---|
| Attempt-reservation ledger. Every session is charged to the owner's budget before it opens. The owner's policy decides whether an interruption ends the job or the worker may fix delivery and continue, and whether revised prompts are refused or run as a separately labeled group. | [evals/protocol/ledger.py](evals/protocol/ledger.py) | [test_ledger.py](evals/protocol/test_ledger.py) replays rc.1 under three settings: strict gives one partial return (10); fix-and-continue at 36 gives 10 + 26 with 10 refused for budget; at 46 the whole history fits |
| Answer contract (one fenced Swift block, no file edits) and strict extractor | [evals/protocol/answer_contract.py](evals/protocol/answer_contract.py) | All 36 rc.1 answers accepted, same bytes as reviewed |
| Grader: one byte buffer, structured write-once results. Native lane: warm-up, fingerprinted resume, stop at an infrastructure error. | [grade.py](evals/rc1/grader/grade.py), [native_lane.py](evals/rc1-comparison/native_lane.py) | Fresh reproduction matched all 36 first results |
| Linked verifier and sanitized summary; sealed packet verified at its sealing revision | [verify_return.py](evals/rc1-comparison/verify_return.py), [verify_pinned.py](evals/rc1-comparison/verify_pinned.py) | `python3 -B evals/protocol/rehearse.py` passes |
| Two contrasting checkout-font contracts | [evals/headroom/checkout-font/](evals/headroom/checkout-font/README.md) | 5 valid variants pass, 6 mutants fail, including both observed rc.1 failures |

## Step 1: Improve the guidance offline (question 1)

- **Write rc.2 as a new semantic version.**
- **First change, from direct evidence:** a text-size card that asks which setting owns the label.
  - Caller-supplied setting → scale explicitly and leave automatic adjustment off.
  - Live environment → `scaledFont(for:)` with automatic adjustment, or rescale on trait changes.
  - Both checkout-font contracts must pass with the card. Keep the 17/37 pt observation scoped to its tested configuration.
- **Then:** control-preservation guidance from GP26-03 (checkout with an existing Pay action) and GP26-11 (an already-working Slider). Work from the failure-replay bundle's `NEXT.md`.
- **Each change records** the evidence it answers and the tasks it must not break.

## Step 2: Build the comparison tasks

- **Development cases:** the known incidents (checkout-font, GP26-03, GP26-11 and others). Used to write and tune the guidance; never counted as fresh evidence.
- **Transfer cases:** new realistic checkout and control-preservation tasks that test the same decisions in code the guidance wasn't written around. Improvement is judged on these.
- **Regression controls:** the 12 rc.1 tasks. A loss here is a finding regardless of totals.
- **Each task needs** a realistic starter, a natural request that doesn't state the rule, hidden unit contracts, its known valid alternatives qualified to pass, and mutants qualified to fail.
- **Pairs:** use contrasting pairs where one decision has two correct answers, as checkout-font does.

## Step 3: Options for the next run (the owner chooses)

Before dispatch, the proposed packet is shown with its workload, what each extra repeat buys, and which interruptions BigDog may handle inside the same handoff. Options, cheapest first:

| Option | Answers question | Cells | Sessions |
|---|---|---|---|
| A. Content check | 1, on transfer cases | 0.2.2 and rc.2, explicit; 6 transfer + 6 development cases; 1 run each | 24 |
| B. A plus a no-skill baseline | 1, including improvement over no skill | A plus an unaided arm on the same 12 tasks | 36 |
| C. B with repeats | 1 and 2 | B × 3 repeats | 108 |
| D. Regression controls | Losses on easy tasks | 0.2.2 and rc.2, explicit, the 12 rc.1 tasks, once | +24 |
| E. Discovery | 3 | 0.2.2 and rc.2, automatic, 24 prompts labeled in advance (12 should, 8 should-not, 4 ambiguous), once | +48 |

**Recommendation:**
- Start with **B + D (60 sessions)**. It answers the priority question against both baselines and catches regressions.
- Add repeats (C) only for the tasks whose results would change a decision.
- Run discovery (E) separately once the content shows a gain.

**For each option the packet states:**
- the budget;
- the interruption policy: end the job, or fix delivery and continue within the budget;
- the prompt-revision policy: refused, or allowed as a separately labeled group.

The ledger enforces exactly those settings.

## Production bar for 0.3.0 (proposed; the owner sets the final thresholds)

| Gate | Proposed threshold |
|---|---|
| Improvement on transfer cases, explicit rc.2 vs unaided | Clear paired gain, repeated across the preselected tasks |
| rc.2 vs 0.2.2 on transfer cases | Not worse on any task's majority result |
| Regression controls | No losses vs 0.2.2 |
| Discovery | Should-invoke prompts mostly invoke; should-not prompts rarely do. Both rates are reported |
| Coverage | Transfer cases in each of six cells: iOS, macOS and tvOS × UIKit and SwiftUI, with AppKit counting toward macOS |
| Grading | Native compile and unit outcome for every gradable answer; format and invocation graded separately |

## Process rules

- **Decision first in every return:** the authorization outcome, whether a promotion decision follows, then the actionable findings.
- **Separate rows** for:
  - each cohort (original vs revised prompts);
  - source vs native grades;
  - invocation vs reference reads.
- **Generated tables:** the report's evidence table is generated from the summary and verified ([RESULT.md](evals/rc1-comparison/RESULT.md) is the template).
- **One status file:** [STATUS.md](STATUS.md).

## Owner decisions

| ID | Decision | Status |
|---|---|---|
| D1 | Which run option, budget and stopping policy | Open; zero extra spend stands until changed |
| D2 | Native grading lane | **Decided November 7:** reviewed local lane, no VM or separate user ([rule](evals/rc1/README.md)) |
| D3 | Development target model | **Decided November 7:** Claude Haiku 5.5 at low effort. It is the most likely to need the skill, so it gives the clearest signal. Frontier models (Sonnet, Opus) come after value is shown on Haiku. The [failure inventory](research/evaluation/failure-inventory/README.md) ranks cases on this model |

## Next offline actions

1. Draft the rc.2 text-size card and confirm it against both checkout-font contracts.
2. Write the first transfer cases for checkout-font ownership and GP26-03 control preservation.
3. Prepare option B + D as a packet for review, without dispatching it.

**Clean-start research track:** [ADR-005](research/adr/ADR-005-failure-derived-skill.md) and the [zero-base challenger](research/evaluation/zero-base-v1/README.md) implement the alternate candidate strategy. Use the recovered pool receipts and contrasts before selecting the head-to-head cases. The earlier rc.2 options are alternatives, not concurrent execution grants.

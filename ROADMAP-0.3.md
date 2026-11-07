# Roadmap to a production-quality 0.3.0

Draft, November 7, 2026. It replaces §8–9 of [CurrentStatusReview.md](CurrentStatusReview.md) for planning. It is based on the [rc.1 result](evals/rc1-comparison/RESULT.md). Nothing here authorizes model runs, spend, messaging or changes to 0.2.2 or rc.1.

## What the rc.1 return taught us

1. **The skill is rarely used.** On ordinary developer prompts, automatic invocation was 1/12 for each version, and 0/9 in the sealed run. A better body can't help a session that never loads it.
2. **Our decision suite can't detect improvement.** All 12 tasks pass in every arm, in about 4 seconds, without the skill. They test API recall from prompts that state the rule.
3. **rc.1's content routing works once loaded.** When invoked explicitly, it read references in 3/3 sessions; 0.2.2 read them in 0/3. That's the part worth keeping.
4. **Native grading catches what source review misses.**
   - All three checkout-font answers fail natively, but the reviewer passed them. Each scales for the supplied traits and also sets `adjustsFontForContentSizeCategory = true`, which overrides the size.
   - Both versions do this even when invoked; rc.1 also read its checkout reference in one case.
   - That's the first measured content gap: rc.2 should say to choose one scaling model, not both.
5. **The task interface itself caused failures.** "Return only Submission.swift" led a model to try writing a file in a read-only session. That stopped the sealed run. The chat wording BigDog used instead worked 36/36.

So the order of work is: **invocation → a suite with headroom → content**. Content work before the first two can't be measured.

## Production bar for 0.3.0

All of these must hold on the frozen suite, against the same native harness, before promotion:

| Gate | Threshold |
|---|---|
| Quality vs unaided, headroom suite | Paired pass rate higher by ≥ 25 points, with a sign-test p < 0.05 across tasks × repeats |
| Quality vs 0.2.2, headroom suite | Not worse on any task's majority result |
| Regression lane (ceiling tasks) | 0 losses vs 0.2.2 |
| Automatic invocation, should-trigger prompts | ≥ 60% |
| Automatic invocation, near-miss prompts | ≤ 10% |
| Coverage | ≥ 2 headroom tasks in each of the six cells: iOS, macOS and tvOS × UIKit and SwiftUI, with AppKit counting toward macOS |
| Grading | Native compile/unit outcome for every answer where a contract exists; one masked source review for criteria the units can't check |

## Phase 1: Invocation (offline first)

- **Rewrite the description for rc.2.**
  - Today's wording ("Review or implement accessibility…") matches requests that say "accessibility". Our task prompts are code-first: "description label at the given text-size setting", "toggle binding", "NSButton… selectors", "Reduce Motion".
  - Name those surfaces, as APIs and as plain developer phrasing, in the first sentence.
  - Keep the 0.3.0 platform scope and the "unrelated Swift" exclusion.
- **Build a trigger corpus:** `evals/trigger-corpus/`, about 120 prompts.
  - Half should trigger, half are near-misses: Swift questions that don't involve accessibility.
  - Draw from the 60 scenario families in `evals/scenarios.json` and the v2 subject prompts.
  - Keep a held-out third.
  - Score coverage offline: for each prompt, which description terms and APIs it shares.
  - This ranks wording; it doesn't predict invocation.
- **Fix the prompt interface for every future packet.** Use the v2 chat instruction. Extract the first fenced `swift` block and record format separately, so it's no longer a failure.
- **Exit:** the rc.2 description and trigger corpus are frozen, and the coverage report is checked in. The actual invocation rate is measured in the Phase 4 run.

## Phase 2: Headroom suite (replaces the 12 one-liners for decisions)

**Seed tasks** come from observed failures (unaided Haiku, graded attempts):
- GP26-03 checkout layout with Pay appearance, 4/4 failed;
- GP26-11 already-working Slider, 4/4;
- GP26-04 deletion without swiping, 2/4;
- iOS media ownership, 1/1;
- GP26-02 cell reuse, 1/4;
- failure families A–F in CurrentStatusReview §5.

**Each task:**
- a realistic starter of 50–200 lines that already has working behavior to preserve;
- a natural request that **doesn't state the rule**;
- hidden unit contracts in the existing [rc.1 grader](evals/rc1/grader/tasks.py) format;
- one accepted alternative and one deliberate mutant, qualified with `python3 -B evals/rc1/grader/qualify.py` on this Mac.

**Size:** start with 12 tasks (two per cell), then grow to 24.

**Admission rule** (pre-registered):
- A task enters the decision suite only if unaided failures are ≥ 50% of its graded attempts.
- Tasks every arm passes go to the regression lane, where a pass is required.
- The existing 12 rc.1 tasks become the first regression lane.

**Exit:** 12 headroom tasks qualified (alternatives pass, mutants fail), with their own scorecard and verifier.

## Phase 3: Content aimed at Phase 2 failures (rc.2)

- rc.2 is a new semantic version; rc.1 stays frozen.
- Start offline from the failure-replay bundle's guidance on GP26-03 and GP26-11. Its `NEXT.md` is in the [returned proposal](evals/rc1-comparison/RESULT.md#what-arrived).
- **Each change records:**
  - the historical answer it addresses;
  - the criterion it targets;
  - the passing tasks it must not break.
- Add on-demand example cards from the 46 tested packages, for families A–F only. Don't load them by default.
- **Exit:** rc.2 is packaged reproducibly like rc.1, verified offline, and has a change log tied to tasks.

## Phase 4: One decisive run (prepared here; dispatched only with D1)

**Design:**
- **Arms:** unaided, 0.2.2 and rc.2, on the same native harness and model.
- **Lanes:**
  - automatic and explicit, reported separately;
  - headroom suite ×3 repeats;
  - regression lane ×1.
- **First cut:** 12 headroom tasks.
  - 3 arms × 12 × 3 = 108 sessions;
  - plus 3 × 12 = 36 regression sessions;
  - **144 sessions in total.**
- **Full suite:** 24 tasks gives 252 sessions.

**Execution rules:**
- One sealed packet, one return.
- An interface failure stops the run and is reported. It is not rewritten and rerun.
- The return is ingested with a verifier like [verify_return.py](evals/rc1-comparison/verify_return.py).

**Grading:**
- Native unit grading on this Mac through the reviewed local lane.
- One masked source review for criteria the units don't cover.

## Phase 5: Process rules

- **One status file:** [STATUS.md](STATUS.md).
- **One result per return:** `RESULT.md` with a verifier.
- **Gate on the result:** no new candidate starts before the previous run's gate result is recorded.
- **Gold prompts:** a prompt becomes gold only when its unaided failure rate is shown, and its contract is qualified with an alternative and a mutant.

## Owner decisions

| ID | Decision | Why it blocks |
|---|---|---|
| D1 | Quota for the Phase 4 run: first cut of 144 Haiku 5.5 low sessions, or the full 252 | No decision without it |
| ~~D2~~ | **Decided November 7:** reviewed local native lane, with no VM or separate user ([rule](evals/rc1/README.md)) | Done; 36 v2 answers graded |
| D3 | Release target: Haiku low only, or also a frontier model such as Sonnet 5.5 | Changes what the gates mean |

## Immediate next actions (offline, no approvals needed)

1. Draft the rc.2 description and the trigger corpus (Phase 1).
2. Convert GP26-03 and GP26-11 into qualified headroom tasks (Phase 2). They have the strongest failure evidence.
3. Draft the rc.2 checkout-font guidance: either scale explicitly on each trait change, or use `scaledFont(for:)` with automatic adjustment, never both. Then promote checkout-font from the regression lane to the headroom suite. It failed in 3/3 skill arms, so it still needs an unaided baseline.

# Current status review

Snapshot: 2026-11-07, repository HEAD `9248057`. This is a review and recommendation document. It changes no skill, reference, candidate, evaluation or policy file, and it does not count as an approved promotion. Status words follow [AGENTS.md](AGENTS.md): *draft*, *reviewed*, *executed*, *accepted*.

## 1. Bottom line

**The project is not yet measurably improving the shipped skill.** Released 0.2.2 hasn't changed since November 4. Eight research candidates (0.3.0-dev.1 to dev.8) were written in about four days. None is installable, and the newest, dev.8, has never been run against a model. The best-supported positive result is dev.5 against no skill on one model: 13 vs 9 meets out of 24, one sample per case. That margin is not statistically distinguishable from noise. The next candidate, dev.7, then scored 9 vs dev.5's 11 on Flash, and that two-case swing was enough to trigger dev.8.

Three root causes:

1. **Grading is manual.** No generated answer has ever been compiled or unit-tested, even though the repo has 46 tested example packages with 1,417 test methods and 226 mutant fixtures. Every run ends in human or LLM source review, and every review ends in reconciliation.
2. **Single-sample comparisons drive candidate churn.** Small A/B swings on one answer per case are treated as signal. There is no measured noise floor.
3. **Content never reaches the product.** The tested examples, the failure taxonomy and the OS 27 research all sit outside the shipped skill. About 87% of commits since November 1 are measurement, records or reconciliation.

**Top five moves:**
- Grade generated code automatically against the existing unit contracts.
- Freeze one balanced weekly suite with three repeats and an A/A noise run.
- Ship one installable candidate (0.3.0-rc) and iterate on it with diffs.
- Put the tested examples into the skill as on-demand cards.
- Target the six recurring failure families across a full OS × framework matrix.

**First-week exit criteria:**
- An automated grader runs 12 tasks end to end.
- An oracle audit accepts at least one alternative correct implementation per task.
- An A/A noise floor is recorded for 0.2.2.

## 2. Current skill state

| | Released 0.2.2 | Candidate 0.3.0-dev.8 |
| --- | --- | --- |
| Location | [SKILL.md](SKILL.md), [references/](references/), [skill/manifests/](skill/manifests/) | [candidates/0.3.0-dev.8](research/evaluation/failure-driven/candidates/0.3.0-dev.8/ENTRYPOINT.md) |
| Installable | Yes, via [scripts/install-for-xcode.sh](scripts/install-for-xcode.sh) | No. An `ENTRYPOINT.md` body plus `route.py` layered over dev.7, dev.6, dev.5 and milestone reference cards |
| Size | `SKILL.md` 185 lines / 1,137 words; references about 38.7k words | Entry point 2,326 bytes; 7 override notes |
| Content | Mostly routing and output-format rules; 51 platform guidelines | Behavior rules from observed failures: preserve ordinary controls and callbacks, trace the owning layer, trace deferred events, say "no change" for working code, separate declaration from runtime and policy |
| Self-imposed overhead | Identity header and `ROUTING:` line on answers | Still requires both. [METHODOLOGY-REVIEW](evals/METHODOLOGY-REVIEW-2026-11-05.md) recommended testing their removal |
| Evaluated | 0.2.2 vs no skill on Flash and Haiku (Nov 5) | **Not evaluated** |

**Candidate lineage** ([candidates README](research/evaluation/failure-driven/candidates/README.md); its `VERSIONS.json` is stale and lists only dev.1 and dev.2):

| Candidate | What changed | Evaluated against a model |
| --- | --- | --- |
| dev.1, dev.2 | Compact skill bodies | Yes: 7 UIKit questions; Flash 6/7 → 7/7, Haiku 6/7 → 6/7 |
| dev.3, dev.4 | Offline drafts | No |
| dev.5 | 8 task notes; 48 routes for iOS, macOS, tvOS × UIKit, AppKit, SwiftUI | Yes: on Gemini Argon, 13/24 vs 9/24 for generic |
| dev.6 | Media ownership notes; SDK excerpt cards | No |
| dev.7 | Shorter entry point; dismissal, reuse, checkout and grouping notes | Yes: on Flash, 9 vs dev.5's 11 out of 24; on Haiku, only 7 pairs completed |
| dev.8 | Activation and deferred-event tracing; 7 overrides responding to the dev.7 Flash regressions | **No** |

## 3. Coverage matrix

Each cell shows: guidelines that apply / example packages (excluding history revisions) / evaluated subject cases in the 24-pair suite.

| OS | UIKit | SwiftUI | AppKit |
| --- | --- | --- | --- |
| iOS | 15 U / **18** / 3 | 15 G / 4 / 3 | n/a |
| iPadOS | U guidelines claim iPadOS / **0** / 0 | G guidelines claim iPadOS / **0** / 0 | n/a |
| macOS | Catalyst not covered / **0** / 0 | 15 G (written for iOS) + M-005 / 6 / 3 | 10 M / 7 / 3 |
| tvOS | 11 T / 7 / 3 | 11 T, shared with UIKit / 4 / 3 | n/a |
| watchOS | n/a | **0 / 0 / 0** (no directory) | n/a |
| visionOS | **0 / 0 / 0** | **0 / 0 / 0** (backlog only) | n/a |

The remaining subject cases are controls: three no-change cases, a mixed-owner case, a missing-reference case and a version-boundary case.

**Caveats:**
- The SwiftUI packages compile shared source sets into each platform package, so their test counts are not independent.
- Per [cross-platform-closure-v1](research/evaluation/cross-platform-closure-v1/clause-ledger.json), only 22 of 507 UIKit/AppKit/tvOS guideline clauses are fully covered by tests, and all 22 are UIKit.
- Example manifests cite Apple documentation, not guideline IDs.
- Only 11 of the 46 packages appear in [code-examples/index.json](code-examples/index.json), all marked `pilot-not-promoted`.
- `SKILL.md` claims visionOS scope, but there is no visionOS guidance. It does not mention watchOS.
- The OS 27 research corpus ([research/os-27](research/os-27/README.md)) documents tvOS Larger Text, the new `TabsPickerStyle` and `XCUIVoiceOverService`, and the Vision Pro and watchOS features. None of it is in the skill yet, by design.

## 4. Recent test results

| Date | Run | Model(s) | Arms | Sample | Grading | Headline |
| --- | --- | --- | --- | --- | --- | --- |
| Nov 5 | [agy-expanded](evals/reports/agy-expanded-20261105/README.md) | Gemini 3.8 Flash low | No skill vs 0.2.2 + reference | 12 code tasks × 3 reps + 6 evidence questions | Single unblinded reviewer | Gold 13 → 15/18; exploratory 12 → 13/18; evidence 4 → 4/6; 1.97× tokens |
| Nov 5 | [claude-haiku](evals/reports/claude-haiku-20261105/README.md) | Claude Haiku 5.5 | Same | Same 84 prompts | Same | Gold 13 → 16/18; exploratory **15 → 14/18**; evidence 4 → 6/6; 2.90× tokens |
| Nov 6 | [compact-candidate-a](evals/reports/compact-candidate-a-20261106/README.md) | Flash, Haiku | 4 arms | 18 cases, single sample | Single maintainer | Flash 13/14/15/15; Haiku 15/16/17/16; compact + reference used 18–25% fewer tokens |
| Nov 6 | [local-compact-b](evals/reports/local-compact-b-20261106/README.md) | Gemma 12B, Qwen Coder 14B, Qwen3.5 | 0.2.2 vs compact B | 6 questions | Unblinded + type-check | 30–35% fewer tokens; quality mixed; type-checks dropped for 2 of 3 models |
| Nov 6 | [dev.1 vs dev.2](evals/reports/skill-0.3.0-dev.1-vs-0.3.0-dev.2-20261106/) | Flash, Haiku | dev.1 vs dev.2 | 7 UIKit questions | Independent source grader | Flash 6 → 7/7; Haiku 6 → 6/7 |
| Nov 6 | [native-activation-lift](evals/reports/native-activation-lift-20261106/README.md) | Haiku | Generic / 0.2.2 / dev.2 installed | 12 sessions | Masked review | **Skill invoked in 0 of 6 guided sessions**, so this measured nothing about the skill |
| Nov 7 | [gemini-controlled-run](research/evaluation/gemini-controlled-run-20261107/README.md) | Gemini 4 Argon high | Generic vs dev.5 supplied inline | 24 pairs (12 families), single sample | Masked independent reviewer | **13/24 vs 9/24**; 6 gains, 3 regressions; +6% tokens |
| Nov 7 | [local-dev5](evals/reports/local-dev5-20261107/README.md) | Gemma 12B, Qwen3.5 | No skill / 0.2.2 / dev.5 | 6 applications | Unblinded + 30 compiler probes | No complete passing implementation; compiler probes 8 pass, 18 fail, 4 environment errors |
| Nov 7 | [dev.5 vs dev.7](research/evaluation/dev7-flash-haiku-results-20261107/README.md) | Flash; Haiku | dev.5 vs dev.7 | 24 pairs; Haiku stopped at 7 on quota | 3 masked reviewers | Flash **11 → 9**, 1 gain, 3 regressions, 8% fewer tokens; Haiku 2 → 3 over 7 pairs |

**Interpretation:**

- **The paired deltas are inside the noise.**
  - Dev.5 vs generic had 6 gains vs 3 regressions. A two-sided sign test on 9 discordant pairs gives p ≈ 0.51.
  - Dev.7 vs dev.5 had 1 gain vs 3 regressions, which gives p ≈ 0.63.
  - Neither result supports promoting or rejecting a candidate. The repo's own gates ([release-gates.json](evals/release-gates.json): 3 repeats, ≥20 held-out families, a non-inferiority margin) have never been attempted.
- **The Nov 5 runs are the only repeated samples.** They show a narrow, consistent benefit on gold code: the skill kept a correct native Toggle in 3 of 3 answers vs 0 of 3 without it. That came at 2–3× the tokens, and exploratory code got slightly worse on Haiku.
- **Several task cells fail in every arm**, so skill changes there have not landed:
  - checkout Dynamic Type text,
  - SwiftUI lifecycle,
  - macOS AppKit testing,
  - tvOS SwiftUI testing,
  - the mixed-owner control.
- **The 24 scenarios are 12 related families.** The effective sample is about half the case count.
- **No result reflects real-world use.** Every positive result used references supplied inline. When the skill was installed natively, the model never invoked it.

## 5. Failure taxonomy vs skill coverage

The sources are:
- the frontier session incidents F01–F08 ([incidents.md](research/reports/2026-11-05-frontier-coding-evidence/incidents.md), [CONVERSATION-AUDIT.md](research/evaluation/failure-driven/CONVERSATION-AUDIT.md));
- the per-campaign `DIFFICULTIES.md` ledgers;
- the dev.7 critical flags ([dev7 results](research/evaluation/dev7-flash-haiku-results-20261107/README.md));
- R04 ([NEXT-SKILL-VERSION.md](evals/NEXT-SKILL-VERSION.md)).

| Failure family | Observed in | Addressed by 0.2.2 | Addressed by dev.8 | Tested example exists |
| --- | --- | --- | --- | --- |
| **A. Lost ordinary actions**: accessible leaf hides child buttons; control created but never wired | Flash and Haiku, dev.5 and dev.7, iOS UIKit and AppKit (6 critical flags) | Partly (grouping guidelines) | Yes (`uikit-ordinary-actions`, `appkit-actions`) | Yes (uikit-containers, uikit-semantics, macos-structure) |
| **B. Dismissal, focus and ownership timing**: restoring at the Close request; empty `onDismiss`; stale session ID | Flash dev.5 and dev.7; Argon generic and dev.5 | Generic modal guidance | Yes (`swiftui-dismissal`, `uikit-dismissal`) | Yes (uikit-modal, macos-lifecycle, tvos-lifecycle) |
| **C. Dynamic Type / checkout text**: shrink-to-fit; system font plus a TODO | Every cohort | Generic Dynamic Type guidance | Yes (`checkout-uikit`) | Yes (uikit-dynamic, uikit-text) |
| **D. Inventing defects in correct code** | Flash and Haiku no-skill runs on GP26-11 and GP26-12 | No | Yes ("identify a concrete defect first") | No-change controls only |
| **E. Invented or wrong API signatures**: `accessibilityAction(named:role:)`, the `.accessibilityActions("…")` typo in a WWDC sample | R04; [OS 27 research](research/os-27/conflicts.md) | No | No | No |
| **F. Eligibility and state consistency**: eligibility checked only on the fallback | Flash dev.7, tvOS UIKit | No | Partly | Yes (tvos-state-recovery) |
| **G. Test-writing errors**: guessed diagnostics, lifetime vs autorelease, synchronous trait propagation, `===` on strings | F01, F02, F05, F08 | No | No | Only as authoring incidents |
| **H. Input modes and media variants**: Full Keyboard Access; forced vs full subtitles | F07; macOS keyboard cases | Partly | Partly (dev.6 media) | Yes (uikit-media-metadata, macos-navigation) |

Two gaps stand out. Families E and G have no skill text at all. Family A has tested examples and candidate text, but the candidate text has not been run.

## 6. Gaps

**Product**
- The shipped skill is unchanged. The candidate architecture (router over stacked candidates) cannot be installed.
- Tested examples are not reachable from the skill.
- iPadOS, watchOS and visionOS are not covered. SwiftUI on macOS and tvOS reuses guidance written for iOS.
- Native invocation does not trigger. The skill description and trigger wording have never been tested as an experiment. The [explicit-invocation diagnostic](research/evaluation/explicit-invocation-v1/README.md) is on hold.
- Answers carry identity and `ROUTING:` lines whose value has never been measured.

**Evaluation**
- Generated code is never compiled or unit-tested. All grades are source judgments that need adjudication.
- Since November 6, runs have used a single sample per case, and there is no A/A run.
- The tasks are bespoke ownership and lifecycle puzzles, such as an overlapping sheet presentation with session IDs. They are realistic but narrow, and several fail in every arm.
- The gold questions are not yet independently qualified; the [independent v2 review](research/evaluation/independent-v2-review-20261107/REVIEW.md) kept 15 domain cases provisional. Status disagrees across documents: [GoldPrompts.md](GoldPrompts.md) says "6/6 development prompts gold-ready", while [evals/os26/README.md](evals/os26/README.md) still says "0 validated gold fixtures".
- Quotas cut runs short: Haiku completed 7 of 24 pairs.

**Process**
- About 335k words of evaluation and research-process prose sit against about 39.8k words of skill text (`references/` plus `SKILL.md`), a ratio of about 8.4 to 1.
- 35 tracked files are named for handoff, reconciliation, request or intake.
- Multi-host coordination involves BigDog, Sillycon, MaxMini and subscription CLIs, with message cursors and receipts tracked in prose.
- Every live batch needs separate owner approval.
- [failure-driven/CURRENT-STATUS.md](research/evaluation/failure-driven/CURRENT-STATUS.md) is stale, dated November 5.

## 7. Process analysis

Every figure below was measured on 2026-11-07 with read-only commands.

| Measure | Value | How measured |
| --- | ---: | --- |
| Non-merge commits since Nov 1 | 88 | `git log --since=2026-11-01 --no-merges` |
| Commits by day, Nov 4 / 5 / 6 / 7 | 17 / 30 / 33 / 28 | `git log --date=short` |
| Commits touching released `SKILL.md`, `references/` or `skill/` | **1** (Nov 4) | `git log -- SKILL.md references skill VERSION` |
| Commits touching candidate skill text | 7 | `git log -- research/evaluation/failure-driven/candidates` |
| Most common commit verbs | Record 14, Add 11, Validate 7, Publish 5, Prepare 5, Report 4, Reconcile 4 | First word of the commit subject |
| Words: `evals/` / `research/evaluation/` / `references/` | 198.6k / 136.1k / 38.7k | `wc -w` over Markdown, excluding results |
| Tracked Markdown files | 1,100 | `git ls-files '*.md'` |
| Candidates written / evaluated | 8 / 4 | Candidate registry plus the run reports |
| Example packages / test methods / mutant fixtures | 46 / 1,417 / 226 | `code-examples` manifests and `NegativeFixtures` |
| Generated answers compiled and unit-tested by the grader | **0** | All run reports |

**Diagnosis.**
- The team spends its capacity on provenance and coordination: hash pinning, receipts, masking and reconciliation of stale or conflicting reports. Those were designed to protect against a release mistake, but nothing has been released, so they protect nothing yet.
- Evaluation is so expensive per run (approval, quota, masking, independent review, intake) that runs stay small. Small runs are too noisy to decide anything, which invites another candidate and another run.
- The [methodology review of Nov 5](evals/METHODOLOGY-REVIEW-2026-11-05.md) already warned: "hedging… has replaced decisions". This review confirms it.

## 8. Recommendations

> **Superseded for planning (November 7, after the rc.1 return).** [ROADMAP-0.3.md](ROADMAP-0.3.md) re-orders this section's recommendations using the [rc.1 result](evals/rc1-comparison/RESULT.md): invocation first, then a suite with headroom, then content. The text below is kept as written.

Each recommendation lists its evidence, its expected effect and a done-when condition. They are recommendations only. None changes current policy until the owner approves it.

### R1. Grade generated code automatically against the existing unit contracts

- **Evidence.**
  - [code-examples/tools/platform-native.mjs](code-examples/tools/platform-native.mjs) already runs compile and unit lanes on iOS/tvOS 26.5 simulators and on macOS.
  - 226 negative fixtures show the tests reject realistic defects, including the families that fail in grading: hidden child actions, unwired controls, dismissal timing.
  - Manual grading is the main cost and the main source of reconciliation.
- **What.** Turn each task into "fix or complete this file". The subject receives the file and the developer question, not the tests. The harness drops the answer into the package and runs the hidden test suite plus a compile check.
  - Score each task: compiles, contract tests passed, and whether it hits any of the critical-error checks.
  - Keep LLM or human review only for explanation-only questions and for oracle disputes.
- **Oracle audit, as AGENTS.md requires.** For each task, write at least one alternative correct implementation, for example a custom action instead of a separate element. Confirm the tests accept it before using the task to grade a model. Record any rejection as a test-oracle defect.
- **Done when.**
  - 12 tasks (two per covered matrix cell) grade automatically with no manual review step.
  - Each task's alternative implementation passes.
  - Each task's mutants fail.

### R2. Freeze one weekly suite with repeats and a noise floor

- **Evidence.** The p-values in Section 4. The Nov 5 three-repeat runs are the only stable signal.
- **What.**
  - About 40 auto-graded tasks, balanced across the matrix, with no-change and non-accessibility controls included.
  - 3 repeats per arm.
  - An A/A run (the same skill twice) to measure how much results change between identical runs.
  - Report per cell and per failure family, not just a total.
  - Promote only when the gain exceeds the A/A spread and adds no new critical errors.
- **Done when.**
  - A scoreboard exists for generic, 0.2.2 and dev.8 on the frozen suite.
  - The A/A spread is published.
  - No candidate is written in response to a single-sample swing.

### R3. One installable candidate, shipped

- **Evidence.**
  - Eight candidates, none installable.
  - The stacked routers obscure what the model actually reads.
  - Native invocation failed 0 of 6.
- **What.**
  - Collapse dev.5 to dev.8 into one 0.3.0-rc tree with the same shape as the released skill: `SKILL.md` plus `references/`. Fold the dev.8 behavior rules into `SKILL.md`, and drop the routers.
  - Run it head to head against 0.2.2 on the frozen suite, in both modes: supplied inline and natively installed.
  - Release on a pass. After that, every change is a diff against the release candidate.
  - Allow one candidate in flight at a time.
- **Done when.** 0.3.0 is released with its scoreboard attached, or rejected with a cell-level reason.

### R4. Put the tested examples into the product

- **Evidence.** The examples hold the strongest correctness evidence in the repo, and none of them is routable.
- **What.** For each failure family and matrix cell, create one short reference card: the rule, a minimal correct snippet taken from the tested package, the common wrong version, and the package path.
  - Load the cards on demand.
  - Measure them as an arm: release candidate with cards vs without.
- **Done when.** Cards exist for families A, B, C, D and F in every covered cell, and their effect is on the scoreboard.

### R5. Target high-headroom failure families, not bespoke puzzles

- **Evidence.** Several cells fail in every arm. The task design rewards tracing one specific scenario rather than showing the general patterns models get wrong.
- **What.**
  - Rank the families by observed failure frequency on the generic arm multiplied by how common the pattern is in apps.
  - For the top six (A–F), write one tight rule and one card, plus two suite tasks: one fix task and one write-from-scratch task.
  - Add family E (API signatures) as a compile-gated rule: "check the signature exists; do not invent overloads".
  - Retire tasks that fail in every arm and have no identified skill lever, unless they are deliberate controls.
- **Done when.** Each top family has a rule, a card and two tasks, and its generic-arm failure rate is measured.

### R6. Coverage roadmap across all OSes with UIKit and SwiftUI

- **Evidence.** The matrix in Section 3. The OS 27 research supplies sourced facts for the empty cells.
- **What, in order:**
  1. **iOS SwiftUI**: grow from 4 packages to parity with iOS UIKit on families A–D.
  2. **macOS** SwiftUI and AppKit.
  3. **tvOS** UIKit and SwiftUI, including Larger Text, which tvOS 27 adds.
  4. **iPadOS** as variants of the iOS tasks: keyboard and Full Keyboard Access, pointer, multiple windows and the 27 resize rules.
  5. **watchOS** and **visionOS** SwiftUI: two seed packages each, plus first guidelines drawn from [research/os-27](research/os-27/README.md).
- **Owner decision needed.** This requires lifting the formal SwiftUI deferral in AGENTS.md. New Apple UI code is overwhelmingly SwiftUI; that is an inference, not something this repo measured.
- **Done when.** Every non-n/a cell in the matrix has at least two auto-graded tasks and guideline coverage.

### R7. Put the process on a diet

- **What.**
  - **One status file.** A single `STATUS.md`, overwritten weekly, replaces CURRENT-STATUS, PRODUCTION-READINESS and NEXT-STEPS-style files.
  - **A decision log** of one-line decisions with dates, instead of trailing caveat lists.
  - **One reconciliation pass** per run, time-boxed to an hour.
  - **Standing approval** for the weekly suite within a stated quota, instead of per-batch approval.
  - **One execution host** for model runs. Other hosts only for the native compile and unit lane.
  - **Archive superseded handoff and reconciliation docs** into `archive/`, keeping their history.
  - **A commit tag** (`content:`, `eval:` or `process:`) so the ratio of skill work to process work is visible weekly.
- **Done when.** Over two weeks, at least 40% of commits are `content:`, and every run finishes with its scoreboard in under a day.

### R8. Remove the overhead the skill puts on itself, and fix invocation

- **What.**
  - Test dropping the identity and `ROUTING:` lines as one arm in the suite.
  - Separately, run a small invocation experiment on the skill `description` wording and trigger terms, scored by invocation rate in native installs.
- **Done when.** The scoreboard shows the effect of dropping identity and routing, and native invocation succeeds in more than half of relevant sessions.

### R9. Revisit the zero-spend constraint

- **Evidence.** The Haiku run stopped at 7 of 24 pairs on quota.
- **Rough cost.** On Anthropic's published rates ($0.10/$0.50 per million input/output tokens for Haiku 5.5; $2/$10 for Sonnet 5.5), a 40-task × 3-repeat × 3-arm weekly suite is about 360 calls. At about 6k input and 2k output tokens per call, that costs roughly **$0.50 on Haiku 5.5** or **$11 on Sonnet 5.5** per run.
- **What.** The owner decides whether a small fixed weekly budget is worth the coordination time it saves. Until then, keep the subscription lanes.
- **Done when.** The owner records a decision, either way.

## 9. Four-week plan

> **Superseded by [ROADMAP-0.3.md](ROADMAP-0.3.md).**

| Week | Deliverables | Exit metric |
| --- | --- | --- |
| 1 | Auto-grader (R1) on 12 tasks drawn from existing packages; oracle audit; A/A run on 0.2.2 with Flash × 3; `STATUS.md` and decision log (R7) | 12/12 tasks auto-grade; alternatives pass and mutants fail; A/A spread recorded |
| 2 | Suite grows to about 40 tasks across iOS, macOS and tvOS × UIKit, SwiftUI and AppKit, with controls; scoreboard for generic, 0.2.2 and dev.8 × 3 repeats on Flash plus one Claude model; identity/ROUTING arm (R8) | Per-cell, per-family scoreboard published; generic-arm failure rate per family known |
| 3 | 0.3.0-rc installable tree (R3) with cards for families A–D and F (R4); head-to-head against 0.2.2, inline and native; invocation experiment | Release decision: improvement beyond the A/A spread and zero new critical errors, or a documented rejection |
| 4 | iPadOS variants; watchOS and visionOS seed packages and guidelines (R6); archive of old process docs; content-share check (R7) | Every matrix cell has at least 2 tasks; at least 40% of commits are `content:` |

## 10. Decisions needed from the owner

1. Lift the SwiftUI expansion deferral, for all OSes including watchOS and visionOS.
2. Accept auto-graded compile and unit results as the primary quality signal, with human or LLM review only for disputes and explanation-only questions.
3. Grant standing approval for the weekly frozen suite within a stated quota and model list.
4. Keep zero spend, or allow a small fixed weekly budget (R9).
5. Allow one consolidated 0.3.0-rc tree to replace the stacked candidate routers.
6. Approve archiving superseded handoff, reconciliation and status documents. History would be preserved; nothing deleted.

## 11. Sources

- Policy and plan: [AGENTS.md](AGENTS.md), [failure-driven PRD](research/evaluation/failure-driven/PRD.md), [TASKS](research/evaluation/failure-driven/TASKS.md), [methodology review](evals/METHODOLOGY-REVIEW-2026-11-05.md), [methodology decisions](evals/METHODOLOGY-DECISIONS-2026-11-05.md), [subscription evaluation](evals/SUBSCRIPTION-EVALUATION.md), [single exchange](evals/BIGDOG-SINGLE-EXCHANGE.md), [release gates](evals/release-gates.json)
- Skill: [SKILL.md](SKILL.md), [references](references/), [candidates](research/evaluation/failure-driven/candidates/README.md), [dev.8 entry point](research/evaluation/failure-driven/candidates/0.3.0-dev.8/ENTRYPOINT.md), [dev.8 intake](research/evaluation/dev8-intake/README.md), [Flash excerpt review](research/evaluation/dev8-intake/FLASH-EXCERPT-REVIEW.md), [next skill version](evals/NEXT-SKILL-VERSION.md)
- Results: the run reports linked in Section 4; [production readiness](research/evaluation/PRODUCTION-READINESS.md), [next experiment](research/evaluation/NEXT-EXPERIMENT-20261107.md), [reconciliation](research/evaluation/RECONCILIATION-20261107.md), [independent v2 review](research/evaluation/independent-v2-review-20261107/REVIEW.md), [skill-lift scorecard](research/evaluation/skill-lift-v1/README.md)
- Failures: [frontier incidents](research/reports/2026-11-05-frontier-coding-evidence/incidents.md), [conversation audit](research/evaluation/failure-driven/CONVERSATION-AUDIT.md), [cross-platform clause ledger](research/evaluation/cross-platform-closure-v1/clause-ledger.json)
- Examples and tooling: [code-examples index](code-examples/index.json), [native runner](code-examples/tools/platform-native.mjs), [gold prompts](GoldPrompts.md)
- Platform research: [OS 27 corpus](research/os-27/README.md), [OS 27 conflicts](research/os-27/conflicts.md)

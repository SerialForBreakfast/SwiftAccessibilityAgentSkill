# Swift Accessibility Skill — Skill & Evaluation Methodology Review

2026-11-05 · Reviewed at commit `ccd74d5`. Analysis only; no other repository files were changed.

## Executive summary

**Verdict: the process is rigorous about provenance but weak on validity, and the six GP26 prompts cannot yet show whether the skill helps a frontier model.** They state the fix inside the prompt, reuse families the skill was already tuned on, and sit at the model's ceiling. The 1/4/1 Gemini pilot is what that design predicts, not a finding about the skill.

The main gap is the oracle. We hash inputs, freeze rubrics and keep receipts, but no answer has ever been compiled. No fix has been run, and no grade has had a second reviewer. Answers are graded against the skill's own reference files. Until a compile and acceptance-test lane exists, every score is one reviewer's reading of plausible-looking Swift.

Top recommendations, in order:

1. **Build the oracle before more prompts.** Run a compile lane (Apple SDK on MaxMini) plus scripted XCUITest/accessibility-audit checks per fixture. An "accepted fix" should come from a test, not a judgment.
2. **Rewrite the prompts in the developer's voice.** Give the symptom and the code, and keep the requirements in hidden tests. Drop the shared answer-contract suffix, which hands C0 the skill's best behaviors.
3. **Screen for headroom.** Keep a prompt only if an unguided frontier model fails it in at least 1 of 3 samples, and keep a fixed share of correct-code controls that are phrased like the defect prompts.
4. **Test where the skill could plausibly add value.** That means exact API signatures, OS 26/27 deltas and known OS bugs. The generic semantics already in the guideline files are knowledge frontier models have without help.
5. **Shrink the skill and stop rewarding format.** Remove the identity line, the `ROUTING:` line and the HIGH/MEDIUM/STALE footer. Add SDK-checked signatures and a requirements-first checklist.
6. **Make the statistics fit the sample.** A 2-point non-inferiority margin over 20 held-out families is not reachable (see below). Pre-register a gate the data can actually decide.

## What we have

There are 76 graded model responses in total, and 0 compiled or device-tested. The eval tree around them holds about 71,000 words of Markdown and about 970 lines of runner code.

| Asset | What it is | Observation |
| --- | --- | --- |
| Skill 0.2.2 (`SKILL.md`, 8.5 KB) | Routing workflow, identity header, mandatory `ROUTING:` line, trust footer with HIGH/MEDIUM/STALE | About half the always-loaded text is output format and routing, not accessibility knowledge |
| 56 guideline files (144 KB) | Rule / rationale / how to implement / how to test / citations | Generic best practice with few or no code examples and no exact signatures. `g-007` cites the same URL under two IDs and was last verified 2026-03-07 |
| `scenarios.json` (40 dev + 20 held-out) | One-line questions such as "Tell me about UILabel accessibility." | No code. Every family is duplicated across OS 26 and 27, and only H18 is version-specific |
| `rubrics.json` | 2–3 outcome criteria per case, 4 weighted 0–4 dimensions | Criteria are drawn from the skill's own guidance. All `expectedFailures` in `complexity.json` are empty |
| v1/v2 reports | 64 grades over 34 distinct answers from Qwen3.5-2B Q4 | A 2B model scoring 5–36/100 says little about a frontier target |
| Gemini developer-code pilot | 6 synthetic code tasks, C0 vs C2, 1 sample each, unblinded single reviewer | W/T/L 1/4/1, 1 suspected invented API (in C2), C2 uses 1.89× tokens |
| `GoldPrompts.md` GP26-01…06 | Revised versions of the pilot tasks | Drafts with 0 validated fixtures. They are the same families as pilot tasks D02, D07, D05, D03, D19/D21 and a control |
| `release-gates.json` | 2-pp non-inferiority margin, 95% CI, 20 held-out families, 3 repetitions | Frozen before results, which is good, but it is not reachable at this sample size |

## How good are the gold prompts

**They are a big improvement on the one-line D-questions, but as written they mostly measure whether a model can follow instructions.** Moving to real code, explicit target OS, preserved callbacks and a correct-code control is the right direction. The problem is that each prompt also says what the fix is.

| Prompt | Origin | What gives the answer away | Discriminating power | Fix |
| --- | --- | --- | --- | --- |
| GP26-01 settings row | D02 (pilot) | "Keep both controls independently discoverable and operable" | Low. The fix is to delete two contradictory lines. "Traversal" is undefined, and the pilot's "redundant title stop" win was a grader preference | State the symptom only. Decide in the hidden test whether the title should be a separate stop |
| GP26-02 reused cell | D07 (pilot) | "Including twice on the same cell without prepareForReuse" points straight at the missing `else` | Low. The pilot already tied | Drop the hint and put the second-configure case only in the test |
| GP26-03 checkout layout | D05 (pilot) | "Handle changes while the screen is open" points at `adjustsFontForContentSizeCategory` | Medium, the best of the six. It has several real constraints (fixed 44-pt height, `fillEqually`, long currency) | Keep it, and automate the AX5 snapshot plus a narrow-width check |
| GP26-04 deletion | D03, the pilot's only regression | It names Full Keyboard Access, an on-screen affordance, no confirmation and "focus must never delete" | Low now. It was rewritten around the one known failure | Revert to the developer's request. Use this as a regression fixture, not as evidence of improvement |
| GP26-05 TV shelf | D19/D21 | "Replace the tile interaction with a standard focusable control" means `Button` | Low. "Do not force focus on every render" tests a mistake nobody makes unprompted | Give the symptom ("testers can't select tiles") and test reachability and Select |
| GP26-06 Toggle control | New | "This settings view is working … do not assume one exists" | None as a control, because the prompt primes "no change" | Phrase it exactly like a defect prompt ("Fix VoiceOver in this view") |

**Cross-cutting problems**

- **The shared suffix teaches the skill to C0.** Every prompt ends with the same instruction: minimal patch, up to three verification steps, preserve functionality, and separate proposed tests from tests actually run. Those are the behaviors the skill exists to add, so the suffix narrows C2−C0 by design. Real developers don't write this. Run with and without it, or move it into a harness-level system prompt that is identical across arms and named as a confound.
- **They sit at the ceiling.** In the pilot, unguided Gemini Flash-low produced a plausible core repair on 5 of 6. A prompt that C0 passes every time can only tie or regress, so the expected outcome is mostly ties plus the occasional noisy loss.
- **The sample is not new.** All six reuse pilot families, and GP26-04 was reshaped by the observed failure. Gains on these will look like improvement whatever the skill actually does.
- **Coverage is narrow.** It is 5 iOS and 1 tvOS. There is no AppKit, visionOS, interop, announcements, modal focus, adjustable control, rotor or Voice Control naming, and nothing OS-26-specific despite the "OS 26 first" label.
- **Acceptance checks are nouns, not tests.** "Compile; traversal; switch state" doesn't define pass. Each check needs an observable assertion, a tool and a not-run state.
- **N=6 with 1 sample can't support a verdict.** A 1/4/1 split has a two-sided sign-test p of 1.0. Even 6/0/0 would only give p≈0.03 with no variance estimate.

**What is good and should stay:** real code, explicit OS and deployment target, preserved callbacks, at least one correct-code control, evaluator-only checklists kept out of model context, and the honest "draft, not gold" status labels.

## Where we are fooling ourselves

**The biggest self-deception is treating provenance as validity.** Hashes, receipts and caveats make a result reproducible, not correct. Nine specific threats follow.

1. **The grading is circular.** `grading-evidence.json` is a snapshot of our own reference files, and the rubric criteria restate the skill's opinions. C2 gets that same text as context. So the grader rewards agreeing with the skill, and C0 is marked down for valid alternatives the rubric didn't anticipate. Grade against Apple primary sources and executable tests instead.
2. **C2 uses oracle routing.** In the pilot, a human picked the one right reference per task. That is an upper bound the installed skill never gets. Separately, small models made 0 reads in 16 C3 cells. The skill's real-world value depends on triggering and selection, and neither has been measured on a frontier host.
3. **The held-out set isn't held out.** All 20 H-questions sit in the repo next to the skill, cover the same topics as dev, were written by the same author, and can be read by any agent that edits the skill. The docs admit this. In practice, nothing has been held out.
4. **Small-model results took a disproportionate share of the effort.** The v2 dashboard asks "Did the skill help Qwen?" for a 2B Q4 model scoring 5–36/100. That tells you about Qwen, and the docs now say so. But that lane produced most of the existing grades and infrastructure.
5. **Duplicated OS contexts inflate the count.** Running every family on OS 26 and 27 doubles cost (6,768 requests planned) when only 1 of 60 families is version-sensitive. v2 shows identical scores across OS cells. Version labels add no data unless the answer should differ.
6. **The release gate can't be met.** Suppose the paired score difference has an SD of about 15 points per family (v2 cases spread 5–36). Then 20 families give a 95% CI of about ±6.6 pp. Reaching ±2 pp needs about 215 families. The gate will either block every release or be quietly relaxed later, and both undermine pre-registration.
7. **The skill rewards confident formatting.** The trust footer asks the model to label its own freshness. In the pilot, C2 said HIGH and none on the answer with the suspected invented overload. The footer makes answers sound authoritative without checking any claim. The same goes for `ROUTING:` lines and the identity header.
8. **The improvement plan is fitted to one failure.** R04 is one sample. NEXT-SKILL-VERSION already lists G-007 edits, and GP26-04 was rewritten around it. The next run will "fix" R04 whatever the variance is. Treat R04 as a regression test, not the design driver.
9. **The real question hasn't been tested.** Does the skill add anything a frontier model doesn't already know? The guideline files are generic, uncoded best practice, which is the material frontier models are strongest on. The skill's possible edge is post-cutoff OS facts, known OS bugs and exact signatures. That is deferred (OS 27) or missing (signatures).

One more pattern is worth naming. The volume of hedging ("not a qualified baseline", "0 flagged is not proof") is honest, but it has replaced decisions. About 71k words of eval documentation sit around 76 graded answers. The cheapest high-value check, compiling the answers, has not been run.

## How the process could improve

**Change the order: oracle first, then prompts, then statistics.** Each prompt should reach "gold" through this pipeline:

1. **Source the bug.** Start from real reports (Apple Developer Forums, GitHub issues, `known-os-issues.md`, your own apps) or from failures already observed in a frontier model. Write the prompt as a developer would: symptom, code, target OS, nothing else.
2. **Build the fixture host.** Use a minimal Xcode project per case with a stable model and callback scaffold. The answer's patch gets spliced into a marked region.
3. **Write the hidden acceptance tests first.** Use XCUITest assertions on label, value, traits and element count, `performAccessibilityAudit()`, Dynamic Type snapshots at AX5, and callback-invocation counters. Anything a test can't observe (VoiceOver speech, FKA, remote feel) stays a named manual check with an explicit `not_run` state.
4. **Validate the oracle.** Confirm that a known-good patch passes and that at least two single-error mutations fail. That is what earns the word "gold".
5. **Screen for headroom.** Run C0 on a frontier model 3 times. Keep the case only if it fails at least once. Correct-code controls are exempt and should be about 20% of the set.
6. **Freeze and run.** Use k=3 samples per arm and report pass rate per case with Wilson intervals, not a weighted 0–100 score.

**Grading**

- Use binary atomic checks (pass / fail / not_assessable) with an evidence quote. Drop the 4-dimension weighted score as the headline because it hides the one thing that matters: does the fix work.
- Use a cross-family LLM judge only for checks a test can't decide. For Gemini answers, that means Claude or Codex. Calibrate it on about 20 owner-graded items and report Cohen's κ. A judge below κ≈0.6 doesn't get used.
- Grade against Apple primary sources and test results, not `grading-evidence.json`. A valid answer the rubric didn't anticipate should pass.

**Design and statistics**

- Spend budget on samples, not OS labels. Drop the 26/27 duplication except for genuinely version-sensitive cases, and put those in a separate delta suite.
- Replace the 2-pp gate with one that about 30 cases × 3 samples can decide. For example: (a) zero new confirmed critical failures, (b) no case drops from ≥2/3 to 0/3, (c) a pre-registered improvement on the targeted families. Pre-register it before the next candidate.
- Make the held-out set truly held out. Keep it outside this repo (private repo or owner-only file), write it after the candidate is frozen, and replace it after one use.

**Measure the product as shipped**

- Add a host lane: the skill installed in Claude Code and Codex, triggered naturally, on a fixture repo. Measure trigger rate, false triggers (D31-type), what was loaded, and outcome. C2 stays as the ceiling arm.
- Report token cost from the host lane, not from manual injection. The 1.89× figure describes C2, not the installed skill.

**Cut overhead**

- Use a one-page protocol, one results table and one decision log per run. Most of the current eval Markdown can be archived. The guardrails it documents (zero spend, no paid fallback, receipts) can live in code and tests rather than prose.
- Split the loops. The dev loop should be fast and unfrozen, with no reports. The release loop is the frozen, pre-registered one. Most current ceremony is applied to dev runs.

## Optimizations the next version should adopt

**Reposition the skill from "accessibility tutor" to "accessibility correctness checker plus post-cutoff facts".** Frontier models already know the tutor material. They fail on exact APIs, input-mode completeness and recent OS behavior.

| # | Change | Why | Measured by |
| --- | --- | --- | --- |
| 1 | Cut `SKILL.md` to a ~40-line requirements-first workflow: list actions, input modes, invariants and target OS, write the patch, check the patch against that list | The only pilot regression was a narrowed task. Most current text is format | Host-lane pass rate, input tokens |
| 2 | Remove the identity header, mandatory `ROUTING:` line and HIGH/MEDIUM/STALE footer. Keep one line of material limitations only when something wasn't verified | They add confidence without checking anything and spend output tokens | Critical errors, output tokens |
| 3 | Add SDK-compiled code and an exact-signature table to every guideline, generated and type-checked per SDK (aligns with ADR-003) | The suspected `accessibilityAction(named:role:)` overload. The guidelines contain no signatures | Compile lane, invented-API rate |
| 4 | Add a "do not invent" list of overloads and modifiers that models commonly hallucinate, seeded from eval failures | Directly targets the most costly error class | Invented-API rate on unseen API-adjacent cases |
| 5 | Add one compact input-mode matrix (VoiceOver, Full Keyboard Access, Switch Control, Voice Control, tvOS remote): what each needs and how to verify | Pilot answers conflated modes and overstated keyboard and focus guarantees | Mode-specific acceptance checks |
| 6 | Make native-first and no-op an explicit rule: prefer existing native semantics, permit "no change", keep styles and callbacks | Toggle control and patch-scope findings | Correct-code controls, diff size |
| 7 | Ship an OS 26/27 delta reference and a known-OS-issues lookup as first-class routes, tested now rather than after an OS 26 baseline | This is where the skill can know something the model doesn't | Small version-sensitive suite run in parallel |
| 8 | Generate compact model-facing references from the canonical human docs (rule, signature, one example, pitfalls) | 56 files repeat rationale, testing and metadata | Context tokens at equal pass rate |
| 9 | Tighten the trigger description and test it (should-trigger and should-not-trigger sets) | Triggering has never been measured in a real host | Trigger precision and recall in Claude Code and Codex |

**Don't adopt** G-007 edits written specifically to solve R04. Fix the class (exact signatures, input-mode coverage), then check R04 as one regression among many.

## Open questions for review

- Is the target consumer an installed skill in Claude Code, Codex or Xcode, or the harness? This decides whether the host lane or C2 is the primary arm. (This review assumes the installed skill is the real target.)
- Can MaxMini run `xcodebuild` and XCUITest with iOS and tvOS simulators? The whole oracle plan depends on it.
- Who reviewed the Gemini pilot? If it was the same agent that wrote the prompts and the skill, the review isn't independent.
- Will you move the held-out set out of this repo, accepting that the current 20 H-questions are spent?
- Are you willing to retire the 2-pp gate now, before any candidate results, and pre-register a replacement?
- Should OS 27 deltas start in parallel as a small suite, given that they are the skill's most plausible advantage?

Sources reviewed: `SKILL.md`, `GoldPrompts.md`, `evals/README.md`, `GRADING.md`, `PROCESS-REVIEW.md`, `NEXT-SKILL-VERSION.md`, `scenarios.json`, `rubrics.json`, `release-gates.json`, `reports/v2/`, the Gemini pilot summary, `SUBSCRIPTION-EVALUATION.md`, `BIGDOG-GEMINI-BASELINE.md`, and `g-007`. The power estimate assumes a per-family SD of about 15 points and is approximate.

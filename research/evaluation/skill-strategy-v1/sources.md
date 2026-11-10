# Skill strategy v1: source review

Status: draft research notes. Read on 2026-11-08 by a research subagent with
web fetch only. No models were run and nothing was executed. Takeaways are
paraphrased and quotes are kept short. Where a fetch was truncated, the
section says so.

Context: SKILL.md plus on-demand reference cards for Swift accessibility
(UIKit/AppKit/SwiftUI). Problems this review is meant to address: skills
not opened (19/54 installed sessions), descriptions cut down to one
sentence, prompts with no headroom, oracle and grader errors, single-sample
churn across about 13 candidates, cards that were read but still produced
failures, and 2.4x token cost.

---

## 1. Agent Skills overview

- URL: https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview (redirected from docs.claude.com)
- Publisher: Anthropic (Claude Platform docs). Date: undated (live page).
- Takeaways:
  - Loading happens in three levels: metadata (about 100 tokens per skill, always loaded), the SKILL.md body (recommended under 5k tokens, loaded on trigger), and resources (no cost until read). Our 2.4x token cost should be broken down by level.
  - The `description` is the only text matched against the request when deciding whether to trigger. If it is one sentence, the trigger surface is one sentence. Limit: 1,024 characters, no XML tags.
  - `name` is at most 64 characters, lowercase letters, digits and hyphens only, and must not include "anthropic" or "claude".
  - Claude reads SKILL.md with bash. Whether it was "opened" can be checked objectively from the tool-call trace, so we should log it per session.
  - Scripts run without their code entering context. Deterministic checks could become scripts instead of prose cards.
- Quote: "until a Skill is triggered, only its name and description occupy context"

## 2. Skill authoring best practices

- URL: https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices
- Publisher: Anthropic (Claude Platform docs). Date: undated (live page).
- Takeaways:
  - Descriptions are written in third person and say both what the skill does and when to use it, with concrete key terms. Vague descriptions are named as an anti-pattern.
  - Evaluation comes first: run without the skill, record the gaps, build at least three scenarios, measure a baseline, then write the minimal content that closes those gaps.
  - Test with every model the skill targets. Haiku-class models may need more guidance, while larger models need less explanation.
  - Keep references one level deep from SKILL.md. Nested links lead to partial reads (for example `head -100`). Reference files over 100 lines get a table of contents.
  - Watch how the agent navigates. Unexpected reading order, missed links, heavy reliance on one file, or a file that is never opened each point to a structural fix.
  - Prefer one default approach with an escape hatch over a list of options. Use validator, fix, repeat feedback loops, and keep terminology consistent.
- Quote: "The context window is a public good."

## 3. Equipping agents for the real world with Agent Skills

- URL: https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills
- Publisher: Anthropic Engineering (Zhang, Lazuka, Murag). Date: 2025-10-16.
- Takeaways:
  - Start from observed gaps on representative tasks, not from a list of everything the domain covers.
  - Split SKILL.md when it grows, and keep contexts that are rarely used together in separate files. That suits per-framework or per-platform cards.
  - Name and description need deliberate design, because they decide whether the skill triggers at all.
  - Ask the agent to reflect on its failures and record what it actually needed. That trace is evidence for card content.
  - Choose code for deterministic or expensive operations and prose for judgment.
- Quote: "Progressive disclosure is the core design principle"

## 4. Agent Skills specification (open spec)

- URL: https://agentskills.io/specification
- Publisher: agentskills.io (open Agent Skills format). Date: undated.
- Takeaways:
  - Portable constraints: `name` 1 to 64 characters, matching the parent directory, no leading, trailing or consecutive hyphens. `description` 1 to 1,024 characters and should include task keywords. Optional fields: `compatibility` (at most 500 characters), `metadata`, and an experimental `allowed-tools`.
  - Budgets: metadata about 100 tokens, body under 5,000 tokens recommended, SKILL.md under 500 lines.
  - Keep reference files small and focused, since each read costs context. Use relative paths one level deep.
  - `skills-ref validate` lints frontmatter. It is a cheap gate to run before any eval.
  - The spec is client-neutral. Gemini-harness sessions may discover and trigger skills differently from Claude Code, so measure trigger rate per harness.
- Quote: "Should include specific keywords that help agents identify relevant tasks"

## 5. skill-creator SKILL.md (local plugin)

- Path: /Users/josephmccraw/.claude/plugins/marketplaces/claude-plugins-official/plugins/skill-creator/skills/skill-creator/SKILL.md
- Publisher: Anthropic (claude-plugins-official). Date: undated (local copy read 2026-11-08).
- Takeaways:
  - It warns that Claude tends to undertrigger skills and recommends somewhat "pushy" descriptions that list adjacent contexts. This conflicts directly with cutting descriptions to one sentence.
  - Trigger eval: about 20 realistic queries, 8 to 10 should-trigger and 8 to 10 should-not-trigger. The negatives are near misses, not easy unrelated tasks. Each query runs 3 times, the set is split 60/40 train/test, and the best description is chosen on the held-out score.
  - Skills are consulted only for tasks the model cannot handle easily. Trivial prompts will not trigger and give no headroom, so trigger queries must be substantive.
  - Each test case runs with the skill and against a baseline (no skill, or a snapshot of the old skill) in the same batch. Record tokens and duration per run.
  - In the analyst pass, flag assertions that pass regardless of condition (they do not discriminate), high-variance evals, and token/time tradeoffs. Read transcripts, not only outputs, and cut skill text that leads to wasted work.
  - Generalize from failures instead of overfitting to a few cases. Explain the reasoning rather than stacking MUST statements.
- Quote: "Claude has a tendency to 'undertrigger' skills"

## 6. Demystifying evals for AI agents

- URL: https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents
- Publisher: Anthropic Engineering (Grace, Hadfield, Olivares, De Jonghe). Date: 2026-01-09.
- Takeaways:
  - Separate task, trial, grader, transcript, outcome and harness. Run several trials per task, because a single sample cannot separate signal from noise.
  - Report pass@k (at least one success) or pass^k (all succeed) according to the product need. For example, 75% per trial becomes about 42% for three out of three.
  - A near-zero pass rate across many trials usually means a broken task or grader. Audit the oracle before blaming the model.
  - Every task needs a reference solution and enough clarity that experts agree on pass/fail. Grade outcomes rather than step sequences, so valid alternatives pass.
  - Capability evals should start with low pass rates (headroom), and graduated tasks move to regression. Saturated evals hide real gains.
  - Balance should-occur and should-not-occur cases. Isolate trials from one another. Give LLM judges an "Unknown" option and one dimension per judge.
- Quote: "20-50 simple tasks drawn from real failures is a great start."

## 7. Define success criteria and build evaluations

- URL: https://platform.claude.com/docs/en/test-and-evaluate/develop-tests
- Publisher: Anthropic (Claude Platform docs). Date: undated.
- Takeaways:
  - Success criteria must be specific, measurable, achievable and relevant, and usually cover several dimensions, including price and latency (token cost belongs here).
  - Evals should mirror the real task distribution and include edge cases and inputs where humans would disagree.
  - Automate grading where possible (code, string match, then LLM). Many automated cases beat a few hand-graded ones.
  - The LLM grader should be a different model from the model under test.
  - Access note: the page was read only up to 100k characters, and the closing section on LLM-grading tips was not reached.
- Quote: "Instead of 'good performance,' specify 'accurate sentiment classification.'"

## 8. Using LLM-as-a-Judge for evaluation: a complete guide

- URL: https://hamel.dev/blog/posts/llm-judge/
- Publisher: Hamel Husain (hamel.dev). Date: 2024-10-29 (modified 2026-09-01).
- Takeaways:
  - Name one principal domain expert whose pass/fail labels are ground truth.
  - Use binary pass/fail with a written critique. The critiques become few-shot examples for the judge.
  - Fix obvious system errors before building a judge.
  - Report the judge's true positive and true negative rates, not raw agreement, which misleads when failures are rare. Use train/dev/test splits, and touch the test split once, after the judge is frozen.
  - Re-validate the judge after material changes such as a new model, a new rubric or a new skill version.
- Quote: "The real business value comes from looking at your data."

## 9. AI evals: everything you need to know (FAQ)

- URL: https://hamel.dev/blog/posts/evals-faq/
- Publisher: Hamel Husain and Shreya Shankar (hamel.dev). Date: 2026-09-18 (modified 2026-09-21).
- Takeaways:
  - Error analysis: open-code real traces, group the notes into a failure taxonomy, and review about 100 diverse traces until new failure types stop appearing. Label at least 30 yourself before letting an agent suggest failures.
  - Use code checks where a rule can detect the failure. Keep LLM judges for persistent subjective failures, at a cost of roughly 100 to 200 labeled examples per failure mode.
  - A large gap between dev and test judge accuracy signals overfitting.
  - Generic metrics (helpfulness, ROUGE) create false confidence.
  - Avoid writing evaluators before failures have been observed, except for known hard constraints.
  - Access note: read only up to 100k of about 154k characters.
- Quote: "The abuse of generic metrics is endemic."

## 10. Who validates the validators? Aligning LLM-assisted evaluation of LLM outputs with human preferences

- URL: https://arxiv.org/abs/2404.12272
- Publisher: arXiv (Shankar, Zamfirescu-Pereira, Hartmann, Parameswaran, Arawjo). Date: 2024-04-18.
- Takeaways:
  - Criteria drift: graders refine their criteria while grading. Freeze rubrics per evaluation run and version them. Do not edit a rubric mid-comparison.
  - Some criteria only become clear after seeing outputs. Expect rubric revisions after the first batch, and re-grade earlier candidates with the revised rubric before comparing.
  - Choose the evaluator implementation (prompt or code) by its agreement with a small human-graded subset.
  - Aligning evaluators is iterative. Budget for it as a separate phase from skill iteration.
  - Access note: abstract page only. The full paper PDF was not read.
- Quote: "grading outputs helps users define criteria"

## 11. A statistical approach to model evaluations

- URL: https://www.anthropic.com/research/statistical-approach-to-model-evals
- Publisher: Anthropic. Date: 2024-11-19.
- Takeaways:
  - Report a standard error with every score. A point estimate alone means little.
  - Cluster standard errors when items share a source. Several questions from one scenario or fixture are not independent, and naive errors are too small.
  - Reduce within-item variance by resampling each item several times and averaging.
  - Compare conditions with paired differences on the same items. With correlated outcomes, the paired variance is much smaller than comparing two independent means.
  - Run a power analysis before a batch: how many items and repeats are needed to detect the effect we care about. If the batch is too small, do not run it as a decision test.
- Quote: "Eval scores don't have any meaning on their own"

## 12. Adding error bars to evals: a statistical approach to language model evaluations

- URL: https://arxiv.org/abs/2411.00640
- Publisher: arXiv (Evan Miller, Anthropic). Date: 2024-11-01.
- Takeaways:
  - Treat evals as experiments, with formulas for uncertainty, two-model comparison and planning.
  - This is the formal source behind item 11. Use its paired-difference and sample-size formulas for skill-on versus skill-off comparisons.
  - Access note: abstract page only. The formulas were not read here and should be checked in the PDF before use.
- Quote: "evaluations are experiments" (paraphrased from the abstract; check exact wording)

---

## Synthesized best practices

1. **Description is complete and in third person.** It states what the skill does and when to use it, names concrete triggers (UIKit, AppKit, SwiftUI, VoiceOver, accessibilityLabel, traits, Dynamic Type, focus, rotor), and is not cut to one sentence. It stays under 1,024 characters, and the name passes `skills-ref validate`. [1, 2, 4, 5]
2. **Trigger rate is measured separately.** Use about 20 realistic queries per harness, half should-trigger and half near-miss should-not-trigger, with 3 or more runs each and a 60/40 train/test split. The description is chosen on the held-out score. "Skill opened" counts only when the trace shows a SKILL.md read. [1, 5, 6]
3. **Triggering, reading and applying are reported separately.** Per session, log: skill triggered (read SKILL.md), card read (file path in the trace), and outcome. A failure after a card was read is a content defect, and a failure with no read is a discovery defect. [1, 2, 6]
4. **Prompts have measured headroom.** Each eval prompt has a recorded unaided baseline pass rate over 3 or more trials that is below the target ceiling. Drop or graduate prompts where the unaided run already reaches about 100%. Trivial prompts are excluded because they neither trigger nor discriminate. [2, 5, 6]
5. **Content is built from observed failures.** Every new or changed card paragraph traces back to a recorded unaided failure, and the minimal text that closes it is written first. [2, 3, 9]
6. **The oracle is audited before grading.** Each task has a reference solution that passes the compile/unit oracle and at least one accepted alternative implementation. Tasks with near-zero pass rates across conditions are triaged as possible oracle or task defects before any model is blamed. [6, 8]
7. **Outcomes are graded, not paths.** Graders check the source-backed contract (asserted behavior) and not a specific API sequence, so valid alternatives pass. [6, 7]
8. **Code graders come before LLM judges.** Use compile/unit checks wherever a rule detects the failure. An LLM or source-review judge is used only for residual subjective criteria, one dimension per judge, with an "Unknown" option, and from a different model family than the subject. [6, 7, 9]
9. **Judges are validated with TPR and TNR.** Each judge is checked against expert pass/fail labels with written critiques, using a train/dev/test split. Report true positive and true negative rates on a test split used once, and re-validate after any model, rubric or skill-format change. [8, 9, 10]
10. **Rubrics are frozen and versioned per comparison.** A rubric change creates a new version, and every candidate in a comparison is graded with the same version. Earlier candidates are re-graded when the rubric changes. [10, 8]
11. **No decisions are made on single samples.** Each condition × item cell has 3 or more trials, and reports include pass rate with a standard error (or pass^k where consistency matters). [6, 11, 12]
12. **Conditions are compared paired on the same items.** Skill-on versus skill-off, or candidate A versus B, are compared through per-item paired differences on identical scenarios, run in the same batch and environment, with clustered errors when items share a fixture. [5, 11, 12]
13. **Power is calculated before spending.** Before a live batch, write down the minimum effect worth detecting and the number of items × trials needed. Underpowered batches are labeled exploratory and are not used for promotion. [11, 12]
14. **Candidate churn is capped.** Change one variable per candidate (description, card text or structure), keep a held-out set that candidates are never tuned on, and promote only on a held-out paired improvement beyond its error bar. [5, 8, 11]
15. **Error analysis comes before changes.** Before revising, open-code at least 30 failing transcripts (aim for about 100 across conditions) into a taxonomy that separates model, harness, oracle, grader and content causes. Stop when new types stop appearing. [8, 9, 6]
16. **Token cost is a tracked criterion.** Report tokens and duration per run by condition next to pass rate. Keep the SKILL.md body under 5k tokens and 500 lines. A cost increase needs a matching paired quality gain. [1, 4, 5, 7]
17. **Reference layout is one level deep.** All cards link directly from SKILL.md, are named descriptively per framework or platform, and get a table of contents if they exceed 100 lines. Cards that are never read are cut or re-signaled. [2, 3, 4]
18. **Instructions give one default and explain why.** Each card gives a single recommended API pattern with a stated reason and an escape hatch, not a menu of alternatives. Deterministic checks are scripts, not prose. [2, 3, 5]
19. **Every target model and harness is tested.** Each candidate runs on every target subject (for example Haiku and Gemini Flash), and results are reported per model and harness, never pooled into a ranking. [2, 4, 6]
20. **Eval sets are balanced.** Include tasks where accessibility changes should not be made (or a skill should not trigger), so the skill is not tuned toward over-application. [5, 6]

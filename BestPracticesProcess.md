# How we earn a change to the accessibility skill

**Start with the user's lost behavior, not the model's missing phrase.** Consider a developer whose form applies an old validation error after they type a new name. A plausible test submits A, calls the app's edit helper with B, then delivers A's reply. That test can pass even when the screen is broken: the helper cancels the request; changing the native field need not call the helper.

Instead, hold the validator completion, change the actual field to B without calling that helper, then deliver the old reply. Check the field, errors, focus-request count and busy state. Submit B and prove that it can still succeed. When A arrives while B is pending, A must not cancel B. This distinguishes a rejected stale write from an implementation that simply ignores every response. See the [batch board](evals/discovery-500/callback-batch/board.csv) for evidence by platform; the [earlier proof replay](evals/proof-repair-20/replay/RESULTS.md) explains why repeating the old tests was insufficient.

**What this batch changed in our process:** all six platform checks accepted both valid implementations and caught the planted defect. Yet one submitted test passed the eager-focus defect and failed both valid implementations. A green test is not evidence of correctness until we know what makes it red. The original iOS panel answer also changed the completion signature: correcting the controller hook, not the answer, turned a build gap into an observable behavioral failure. Record both outcomes rather than replacing the first one.

## 1. Decide what the question can establish

Write the developer's task, starting state, trigger, observable consequence and behavior that must survive. State a product policy only when it determines the answer. Ask for design when design is enough; ask for runnable code when integration is the decision. Compare the actual starter with the wording and key. If the write being blamed already has the proposed guard, look for another writer or mark the question unresolved.

Keep the original first answer, inputs, environment, receipts and source spans private and immutable. Keep solutions, rubrics, incident labels and expected routes out of subject inputs. Give ambiguous prompts and grader defects their own queue; neither justifies adding an instruction to the skill.

## 2. Test the grader before using it

For each distinct developer decision, use the same check against working code, a materially different valid implementation, and a deliberately defective implementation. Record the assertion that distinguishes the defect. A timeout, compilation error, absent fixture, skipped assertion, or test that rejects a valid option does not qualify the check. Retain the first failure before repairing the setup.

Observe the most direct public boundary the question requires. A retained button and a retained action are not interchangeable: a reused button should perform its *new* action. A correct focus request is not evidence that VoiceOver moved. When code is supplied, grade the unchanged production block and unchanged submitted proof separately from our check. When assertions exist only in prose, grade the proposed sequence as prose. Do not supply an assertion and call the result a passing model-written test.

This adapts Anthropic's distinction between the outcome, the trace, and the grader. Favor deterministic checks where they measure the outcome; read the actual output before explaining why a score moved. [Demystifying evals for AI agents](https://www.anthropic.com/research/demystifying-evals-for-ai-agents).

## 3. Distill a decision, not an answer key

Write one hypothesis with its counterexample: *When an action outlives a configuration, check what granted the action authority and what retires it.* Try it on a stale Delete, a current Delete with the same item ID, and an already-correct implementation. Do not prescribe a UUID, a particular class, or an extra generation counter when disconnecting the registration also works.

Put a lesson in shared guidance only if it changes decisions across frameworks. Put native distinctions on a focused framework card, working code behind an example request, and test-runner details in the grader. Keep opposing controls that veto overcorrections; move solved cases into a sampled regression pool rather than paying to rediscover them every cycle. The rationale for varying the behavior boundary rather than just paraphrasing the question comes from [CheckList](https://aclanthology.org/2020.acl-main.442/).

## 4. Measure the candidate separately

Freeze the candidate, comparison questions, permissions, rubric, selection policy and critical ordinary-action regressions before opening candidate answers. A changed question needs a matched baseline. Treat prompts derived from one incident as one family for uncertainty; inspected development cases cannot become unseen transfer cases. Report actual loading separately from routing text. Record input bytes offline and tokens only when measured.

When the owner authorizes a live comparison, use the same task in both conditions, the same transport and model settings, separate fresh sessions, and one worker handoff/return. Schedule approved subscription work before quota expires, within the approved scope. Keep an automatic-invocation test distinct from evaluating a deliberately loaded skill. The [Agent Skills evaluation guide](https://agentskills.io/skill-creation/evaluating-skills) provides the paired-baseline pattern; our local qualification and frozen evidence rules are additional safeguards.

## What to put on the release scorecard

| Claim | Minimum evidence |
|---|---|
| A contract is qualified | Both valid implementations pass and the intended assertion fails on the defect, with matching input/environment records. |
| A preserved answer has a code defect | Its unchanged compatible code executes the failing path, or a separately labeled source judgment identifies it. Distinguish the two. |
| The skill improved answers | Matched baseline and candidate answers show rescues net of regressions; report critical losses, inconclusives, and whole-task vs primary-decision outcomes. |
| A rule earns its context | It transfers to uninspected families, preserves valid controls, and a scoped removal comparison supports keeping it. Otherwise call it a hypothesis. |

Count answer records, unique decisions, tests, repeated executions and deliberate defects separately. Publish the compact board and integrity hashes; retain raw evidence outside public Git with a verified independent backup. A useful iteration may end with a better grader or a discarded proposed rule, not a release.

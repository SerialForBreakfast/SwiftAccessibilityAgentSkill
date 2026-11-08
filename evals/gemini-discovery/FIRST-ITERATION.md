# First iteration of the Gemini skill-effectiveness experiment

The experimental control is AGY Gemini 3.8 Flash Low answering the developer directly, with no accessibility skill, references, file access or tools. All 384 prompts have one first attempt each. This measures how often Gemini already produces an acceptable answer in that setting. The effect of a skill requires a matched comparison. Gemini Flash Low is the evaluation model until the owner changes it.

The [blind grading audit](BLIND-AUDIT-V1.md) is complete for the 34 preservation failures, 14 primary failures and 12 sampled passes.

## What the first answers show

| Task | Pass | Fail | Inconclusive |
|---|---:|---:|---:|
| Repair supplied code | 131 | 19 | 11 |
| Review working code | 25 | 34 | 0 |
| Full implementation | 54 | 22 | 16 |
| Historical development | 35 | 9 | 3 |
| Integrated code | 3 | 3 | 1 |
| Platform workflow | 15 | 3 | 0 |
| **Total** | **263** | **90** | **31** |

The 263/384 pass rate (68.5%) describes this deliberately selected portfolio. One coordinator graded source. Thirty judgments lacked sufficient source evidence and one retained its original harness disposition. The sealed scorer identified 14 distinct primary failures across 98 registered repair/workflow decisions. Each of those 14 keys had one observed primary failure. Frequency among developers, reproducibility across generations, reviewer agreement and skill lift remain open questions.

**The strongest lead comes from 59 matched code fixtures.** Joining the controller by source manifest and check ID gives one defective and one working version of each. Each cell below counts fixtures using whole-answer grades.

| Gemini on defective code | Working version passed | Working version failed |
|---|---:|---:|
| Passed | 22 | 27 |
| Failed | 1 | 4 |
| Inconclusive | 2 | 3 |

Gemini often knew how to implement the fix but applied a change when the supplied code already satisfied the request. On the tvOS shelf fixture it repaired the stale-action defect in one version and re-enabled obsolete actions in the working version. **Only 12 of the 34 preservation failures were graded as failures of the primary behavior.** In 22 the primary behavior passed and the whole answer failed, sometimes for unnecessary changes. Before treating these as lost accessibility, have a second reviewer separate an actual regression, avoidable developer rework, a harmless equivalent, and an unsupported judgment. [Shelf fixture](../../code-examples/platforms/tvos-results-v1/manifest.json)

## Are we asking the right question?

- **A symptom stated as fact can encourage an unnecessary patch.** Both shelf variants say that an earlier action can operate on the wrong record and ask for a repair. They also explicitly allow a no-change answer. This is a useful test of challenging a reported diagnosis. For transfer, use a neutral request such as “Rows can refresh while the menu is open. Which item would Delete affect before and after refresh?” Give separate sessions working and defective code with the same wording. Score the causal explanation, ordinary action, and behavior after rebinding.
- **The question and oracle can disagree.** In G-333de6e92ef584 the developer asks about restoring twice during reentry. The answer explains the closing-state guard. The mutated fixture instead removes permission to dismiss, and the named test checks that ordinary Close and Escape share that permission. Set this case aside for a second adjudication before writing skill advice from it. Two separate questions can test those two behaviors. The original grade remains part of the frozen count. [Modal manifest](../../code-examples/pilots/uikit-modal-v1/manifest.json)
- **A specific technical mistake can survive both versions of the code.** In G-840924fec7426a and its working-code control G-8eafbd1521124e, Gemini converted a text position to a Swift grapheme count. The smallest test for guidance is a developer-visible invariant: searching text after an emoji returns the intended substring. Use the same invariant with different prefixes and ordinary text selection intact. Accept any implementation satisfying the fixture's coordinate contract.
- **A real task should end where a developer can observe the result.** For the caption picker, changing the local selected ID is insufficient when the developer needs the actual player item to reflect the choice. Include stale Off, a newer selection and a preserved audio selection in the controller's unit contract. Collect new tasks from anonymized developer reports or actual PRs with permission. Record the original wording, deployment target and observable outcome before authoring guidance. Reserve entire projects or task families for transfer so paraphrases and cross-platform copies cannot leak across the split.

## Smallest contribution worth testing

Start with one sentence applicable to review requests, provisionally: **“Trace the reported symptom through the supplied code; if the existing path already satisfies the request, show the decisive path and leave it in place.”** Some prompts already say to leave working code alone. The contribution under test is grounding the decision in the actual path. Repeating the existing instruction might have zero marginal value. Keep the ordinary introduction, version and reference-reporting preferences identical across skill conditions.

Use a second, individually removable contribution only where a technical distinction is needed. The UIKit text-range case is the first candidate: a short, source-linked note defining the offset unit and one decisive substring check. The shelf and text cases provide two different predictions. A general review instruction might protect a working shelf while a specific reference might repair incorrect text navigation. A larger router, runnable helper or worked example earns its place only if the shorter condition leaves a reproducible gap it resolves.

| Proposed step | Comparison and decision |
|---|---|
| Audit the measure offline | Independently regrade the 34 failed preservation answers and the 14 primary failures with the first verdict hidden. Include a masked sample of passes to check symmetry. Record disagreements, accepted alternatives and developer consequences separately from the frozen grades. |
| Isolate content | On a balanced development panel, compare generic Gemini, the single review sentence, the text note alone, and both. Keep question, model, available tools and output contract identical. Use fresh sessions and a concurrent generic condition on new or rewritten prompts. Repeat selected discordant pairs to measure run-to-run variability. |
| Isolate routing | Supply the smallest promising text directly to measure what happens when it is available. Then test the same bytes via normal skill discovery and an on-demand reference, with a generic control under the same tool permissions. Capture actual skill-body and reference reads. Explicit invocation can isolate discovery failures. Stage A denied file reads, so compare a tool-enabled installed arm against its own matched tool-enabled control. |
| Validate developer impact | Freeze the proposed semantic version and grading contract before using untouched transfer families. Grade first answers blind. Where a compatible Apple runner and approved fixture exist, use focused compile/unit assertions on unchanged submitted code and preserve the environment. Track whether a developer can use the answer without a repair. |

**Scorecard.** Publish baseline fail → pass and pass → fail counts, preserved passes, persistent failures, inconclusive pairs and critical regressions. Report net whole-answer gain as (rescues − regressions) / comparable pairs, alongside all scheduled denominators and results for each family. Report both-correct fixture pairs out of all matched working/defective pairs. For the installed arm, record automatic activation per eligible session, irrelevant activation on unrelated tasks, actual route reads, and correct answers among all assigned sessions. Separately report correctness conditional on a read, reference tokens where observable, subscription percentage points, and latency. A citation or a read alone cannot establish that the content helped; the content-removal comparison supplies that evidence.

Prefer the shortest tested condition that repeats its benefit on neutral held-out tasks, preserves working controls, and introduces no new critical loss. If the apparent gain depends on unanswered or disputed cases, report it as unresolved. A baseline pass on a common task matters to developers even when a proposed skill has little headroom there. Report Gemini-specific effects first. Another model would later need its own unaided and aided results on the frozen transfer prompts before claiming portability. The existing sealed challenger remains a separate whole-package experiment.

**Evidence provenance.** Private Stage A delivery receipt 1475. The controller, first-answer index and grade ledger are bound by the hashes below. The matched fixture analysis uses the source and check fields in the controller. All proposed follow-up comparisons are unexecuted. [Sealed controller](controller.json) · [Scoring rules](score.py) · [Evaluation acceptance criteria](../../research/evaluation/failure-driven/PRD.md)

| Artifact | SHA-256 |
|---|---|
| Packet seal | `c34292b1ca41f7a25988ce3684a4eafd15b1ad252df0df199d496e1e4fac1151` |
| Combined answer index | `bbf1eb91721d1991d0f5f4b2294a44e445fb84d2ad92b8f054f7c5f93be3b38b` |
| First grade ledger | `4c3265e30954bb3fef650318bf35763a4d610e37df4ba2a3530eb3936230f1eb` |

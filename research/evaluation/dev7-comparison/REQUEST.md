# Owner's authoring input

PLEASE IMPLEMENT THIS PLAN:
# One Local Candidate, One BigDog Evaluation

Build **`0.3.0-dev.7` and its evaluation packet together, locally**. This project owns the skill changes, developer questions, rubrics, evidence reconciliation, and offline checks. BigDog’s job starts when there is one sealed package to evaluate. Its pending criterion reconciliation is useful input if it arrives, not a dependency or a reason for another handoff.

## 1. Turn Observed Failures Into Skill Changes

The completed Gemini comparison gives us a starting point: across 24 paired scenarios, dev.5 had **6 gains, 3 regressions, 5 persistent gaps, 6 preserved successes, and 4 inconclusive pairs** against generic instructions. That is evidence about those answers, not proof of general improvement. Dev.6 already addresses several media issues and has not been compared on frontier answers.

Start from dev.6. Make one substantial revision organized around decisions a Swift developer actually needs help making:

| Priority | What the candidate should do differently | What a better answer must demonstrate |
|---|---|---|
| Dismissal and focus restoration | Distinguish requesting dismissal from its actual completion. Tie restoration to the presentation that owns it. | Closing, cancelling, or receiving a late callback cannot restore the wrong target or reenter an unfinished state change. |
| Mixed SwiftUI/AppKit ownership | Identify which layer owns the control. Assess AppKit roles and children together rather than importing a UIKit grouping rule. | Preserve independently usable child controls; give conditional advice when the supplied code does not establish ownership. |
| Reused controls and checkout text | Follow the update through the **existing** card or checkout control, not just a helper. Separate font configuration, settings, and layout. | A second configuration clears stale optional state while the original Open or Pay action, enabled state, and unrelated settings still work. |
| Media selection and async updates | Reuse dev.6’s corrections. Distinguish available options from the actual selection, an unlisted selection from Off, and an old request from the current owner. | Explain or implement the ownership and selection path the question asks for. A synthetic selection ID alone is insufficient when the question concerns the player item. |
| Evidence and restraint | Preserve correct no-change answers. Distinguish supplied references, actual reads, SDK declarations, and executed unit assertions. | The answer makes the smallest justified change and says precisely what its evidence establishes. |

Keep only the shared decision rules in the entry point. Load framework-specific explanations for the relevant task; load working examples only when code or a contract is requested. **Do not paste the incident archive into the skill.**

## 2. Build the Gold-Prompt Update in the Same Tranche

- Reconcile all **24 cases and 78 criteria** against the existing portable audit and Mac packet. The 73 shared method identities already agree; the Mac packet’s ten additional checks come from two older packages. Use that reconciliation rather than commissioning another discovery pass.
- Keep the original questions and six existing gold decisions immutable. Create an additive revision only where a question lacks necessary inputs, a rubric rejects a valid implementation, or the evidence cannot establish what the rubric asks. Mark each case **ready for comparative scoring**, **development diagnostic**, or **unresolved**, with its reason. Local author review does not confer independent gold status.
- For each changed behavior, link **observed failure → skill change → natural developer question → grading criterion → source or assertion**. Keep complete starter inputs with the question. Keep original outputs, analysis, expected routes, and solutions controller-only. Reuse captured calibration examples; mark unavailable originals explicitly.
- Preserve the positive controls as carefully as the failures. A candidate that fixes restoration but starts rewriting standard controls is worse in a way an average score can hide. Known incidents remain development cases, not holdouts.

## 3. Define “Testable” Locally

Produce one candidate, one versioned scoring guide, one sealed comparison packet, and one readiness report. Before handoff, use **offline checks only** to verify package integrity, framework routing fixtures, focused reference sizes, prompt/controller separation, criterion links, and unchanged protected hashes. Check rubrics against available correct **and** defective examples, including valid alternatives.

Every criterion must be accounted for; it does **not** need a new unit test. Where existing evidence proves a helper but not its integration, narrow the claim or mark it unresolved. Do not start new native runs to make the dashboard green. Report context bytes locally and actual tokens only when measured. Passing this gate means **ready to evaluate**, not “the skill improves model output.”

## 4. Give BigDog One Evaluation Job

Prepare one paired comparison: **dev.5 versus dev.7 on the same final questions, scored with the same revised rubric**. This answers whether the new work improves on the previously measured candidate. Reuse the historical generic comparison as context, not as a matched arm for changed questions. Do not add Claude, Codex, another generic arm, or per-edit smoke runs to this tranche.

Seal the eligible case list, both arms, scoring rules, quota ceiling, and stop conditions before execution. Ask BigDog for **one return** containing original first answers, available transport and usage records, condition-masked grades, and case-level gains, regressions, persistent gaps, and inconclusives. Separate answer quality from routing compliance. Treat a new critical loss of an ordinary action or navigation path as a release blocker regardless of the aggregate score.

**Runs remain held.** The prior report did not establish strict transport qualification. The packet must name the permitted evidence level; if the approved transport or quota is unavailable, BigDog returns one blocked report rather than probing, retrying, or substituting. No released skill, frozen baseline, or existing sealed payload changes during this work.

**Highest-value first step:** Start the local dev.7 tranche with the three observed regressions: SwiftUI restoration at the Close request, UIKit reentrant restoration, and the AppKit parent/child overgeneralization. Write the answer distinction for each *before* editing its guidance, then carry the remaining families through the same batch. The next owner checkpoint is the complete testable package, not another status exchange.

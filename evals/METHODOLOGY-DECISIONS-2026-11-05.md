# Methodology review: decisions and corrections — 2026-11-05

Reviewed the supplied `METHODOLOGY-REVIEW-2026-11-05.md` against current source and
private pilot evidence. Preserve that original review unchanged. It names commit
ccd74d5 but also discusses GoldPrompts.md and plan edits that were uncommitted at
review time; the commit alone cannot reproduce everything it reviewed.

## Adopted now

| Recommendation | Implementation |
| --- | --- |
| Validate the oracle before more inference | Separate OS26 readiness gate requiring host compilation, source review, known-good and two rejected mutations plus required interaction evidence |
| Natural code prompts, fewer solution hints | `evals/os26/prompts.json` draft revision2 and matching GoldPrompts.md; no shared answer-contract suffix; neutral correct-code review |
| Atomic observable criteria | Separate `acceptance.json` with gate IDs, assertion, method and expected result; unknown evidence blocks promotion |
| Keep criteria out of model context | `modelInput()` returns only the prompt; offline tests check separation |
| Independent evidence, valid alternatives | Source review is a required pending gate; no match-to-skill wording, exact preferred code or duplicate-title preference |
| OS-efficient evaluation | OS26-only development lane; OS27 delta suite deferred until OS26 practices are established |
| Honest simple metrics | Paired W/T/L diagnostic, acceptance unknown until checked, confirmed vs suspected errors, token ratio, native not_run states |
| Smaller process surface | One readable catalog, one promotion protocol and this decision log; immutable historical reports retained |

The new runner is an offline gate/planner, not a subscription adapter or Xcode test
executor. Six prompts are registered in the new catalog but still blocked; no model
or native run occurred. Sillycon's planned tests remain a dependency.

## Modify or defer

| Recommendation | Decision / reason |
| --- | --- |
| Keep only cases C0 fails at least once in three runs | Reject as the general corpus filter: selection bias favors apparent gains. Use a labeled headroom stratum while retaining representative successes and no-op controls. Screening itself needs provider approval. |
| Hide all requirements in tests | Hide expected implementations, not essential product constraints. Users need to state required input modes, callback/destructive policy and target; a hidden unexpected requirement is an unfair oracle. |
| Tell a correct-code control “Fix VoiceOver” | Use neutral review wording to avoid priming either a defect or “no change.” False-premise resilience can be a separate labeled test. |
| Start OS27 deltas in parallel now | Conflicts with owner's OS26-first direction. Preserve research and yearly-test groundwork, but OS27 integration/evaluation follows OS26 adoption. |
| About40 lines for SKILL; signatures in every guideline; hallucination blacklist | Test compact workflow and on-demand verified API examples after baseline. Line count is not token cost; forcing signatures into conceptual docs and large blacklists may add noise or anchor on bad APIs. |
| Immediate removal of routing/identity/footer | Evaluate in a separate candidate/ablation. The released skill remains unchanged; cite presence is not correctness and self-confidence is not a metric. |
| Claude/Codex host lanes and model judges | Valuable separate targets, but installed capability, native isolation, explicit subscription approval and finite budgets are prerequisites. No automatic provider use. |
| Kappa≥0.6 on20 items as a judge gate | Diagnostic suggestion, not established reliability. Report sample composition, raw agreement, disagreement/adjudication and uncertainty; prevalence and small samples affect kappa. No LLM judge can replace unobserved device behavior. |
| Replace2pp release gate with suggested30×3 rules | Do not silently change frozen policy. Pre-register a NEW future release protocol with endpoints and variance/precision evidence; simple observed thresholds are descriptive safeguards, not proof of noninferiority. |
| Archive most docs; dev loop has no reports | Keep existing evidence intact. Use concise development notes and durable identities, counts, failures and spend receipts; provenance is still needed in fast experiments. |

## Claims requiring correction or qualification

- **“Only H18 /1 of60 is version-sensitive” is inaccurate.** D38 explicitly contrasts
  continuous reading on26/27; D39 asks about Larger Text on tvOS26/27; D40 concerns
  generated media subtitles. H18 alone has a different `os` list, which is not the
  same thing as being the sole version-sensitive case. Avoid wasteful duplication,
  but inspect expected behavior, not just list shape.
- **“76 graded responses” mixes unlike evidence.** There are64 retrospective rubric
  grades and12 new outputs with qualitative static paired review, not12 newly
  calibrated rubric grades. Their native checks remain unrun. Broader claims that
  nobody ever compiled any answer require reconciliation with other workers.
- **“g-007 cites the same URL under two IDs” is not supported by the inspected frozen
  file.** Its SwiftUI view-accessibility, SwiftUI accessibility and WWDC URLs are
  distinct; broad/indirect citations can still be weak evidence for exact signatures.
- **The2pp gate is not mathematically impossible.** Assuming a15pp SD of *paired
  family differences*, normal-approximation95% half-width is about6.6pp at20 families,
  and about217 families would target2pp half-width. But raw score spread does not
  estimate that paired SD; half-width is not noninferiority power. A positive true
  effect could pass a -2pp lower-bound gate even with a wider interval. Estimate
  paired variance and define the estimand before concluding achievable power.
- **“Ceiling,” “what the design predicts,” and “gains will look like improvement
  whatever the skill does” overstate the evidence.** One sample of plausible code
  without native validation cannot establish a ceiling or inevitable effect.
  Regression-family reuse limits generalization; it remains useful regression evidence.
- **C2 is manual reference injection, not a mathematical upper bound.** Host retrieval
  could select more useful evidence or less distracting context. The1.89× token
  figure describes this injection experiment, not naturally triggered skill cost.
- **Public heldout questions raise leakage risk, not proof of contamination.** Track
  access/tuning history. Same-topic coverage alone does not disqualify a heldout
  family; independence and authoring separation require explicit design.
- **Exact sign-test arithmetic is descriptive here.** With1win/1loss excluding ties,
  two-sided p=1; six independent wins would yield0.03125. Neither calculation makes
  the uncalibrated judgments independent, validates the oracle, or proves causation.
- **XCUITest/audits are not a complete accessibility oracle.** Element traits and
  speech/interaction behavior are not all exposed by the same test interface;
  assertion methods must be verified on the target SDK. Preserve named manual checks.

## Scope and next action

The goals remain practical developer improvement, lower context/review overhead,
and dependable OS26 behavior before OS27 integration. Do not reposition the skill
solely as a post-cutoff-facts lookup before testing task-completeness and correctness
benefits. Next: obtain actual fixture/oracle evidence from the planned Apple lane,
independently review it, freeze the catalog, then request a bounded baseline batch.

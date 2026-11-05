# Promptfoo Evaluation

Current baseline: `0.2.2`

## Purpose

Measure whether:

- agent identity survives
- routing is visible and correct
- injected repo references improve answer quality

## Configs

- `C0`: bare model baseline
- `C1`: skill identity + routing protocol, no injected docs
- `C2`: same as `C1`, plus selected repo references injected inline

Expected interpretation:

- `C0` is the control and will often fail routing or source-disclosure assertions
- `C1` tests identity and routing behavior without repo excerpts
- `C2` tests whether injected repo excerpts improve routing-backed answer quality

## Files

- `promptfooconfig.yaml`
- `prompts/c0.txt`
- `prompts/c1.txt`
- `prompts/c2.txt`
- `gold-prompts.md`
- `viewlens-gold-prompts.md` for optional runtime-evidence scenarios
- `context-budget-gold-prompts.md` for routing and context-bloat scenarios

## Suggested Run

```bash
promptfoo eval -c evals/promptfoo/promptfooconfig.yaml
```

## Minimum Assertions

- first-turn identity includes `Swift Accessibility Agent (v0.2.2)`
- repository-guided answers include `ROUTING:`
- routing names the expected repo doc
- repository-guided answers include `Sources:`, `Freshness:`, and `Assumptions:`
- `Assumptions: none` is reserved for directly supported, sufficiently specific answers

## C2 Injection Note

The scaffold injects short repo-derived excerpts inline for `C2`.
If you expand coverage, keep those excerpts short, stable, and directly tied to the expected route.

## Optional ViewLens Layer

ViewLens is useful for runtime-backed accessibility evaluation, but it should not be required for the baseline promptfoo run.

Use ViewLens-aware prompts to test whether the agent:

- knows when source guidance is not enough
- asks for specific evidence such as semantic outline, navigation graph, Dynamic Type matrix, or before/after review
- distinguishes measured, derived, inferred, and unavailable evidence
- avoids claiming screenshot-only audits prove semantic accessibility
- treats ViewLens as optional evidence, not as a mandatory skill dependency

Add fixture-backed `C3` tests only after stable ViewLens JSON excerpts are committed under `evals/fixtures/viewlens/`.

## Context-Budget Layer

Context-budget prompts verify that the agent answers from the smallest useful set of docs.

Use them to catch:

- unnecessary source-registry or architecture citations for focused questions
- testing docs loaded when no verification was requested
- watchlist docs loaded for stable, accepted guidance
- evaluation docs loaded for ordinary implementation questions
- broad platform bundles used where one topic guideline is enough

## Gold Prompt Authoring Rules

Write prompts as close to real developer questions as possible:

- prefer natural task language over internal backlog titles
- allow common Apple framework terms (`SwiftUI`, `UITableView`, `NSWindow`, `NSHostingView`, `VoiceOver`, `tvOS`)
- avoid seeding the prompt with the exact expected answer
- avoid copying the repository's own rule language into the prompt
- cover both broad questions and concrete bug-like questions

The goal is not just answer correctness. It is to measure whether the agent can:

- recognize the domain from real developer language
- route to the right repository guidance
- surface that routing visibly
- answer with source-backed reasoning

Also verify negative cases:

- identity should not repeat on every later turn
- `ROUTING:` should not appear when the answer does not rely on repository guidance
- `Sources:`, `Freshness:`, and `Assumptions:` should not appear for non-repository answers
- common Apple UI terms alone (`UILabel`, `UIButton`, `NSWindow`, `SwiftUI`) should not trigger this skill unless the user is actually asking about accessibility

Also verify inference cases:

- when the answer narrows ambiguous context, `Assumptions:` should name that narrowing
- when the answer uses general platform/API behavior beyond routed repo docs, `Assumptions:` should disclose that

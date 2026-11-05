# ViewLens Evaluation Integration

Last updated: 2026-09-01

Status: Proposed optional evaluation layer.

Purpose: Define how ViewLens can improve Swift Accessibility Agent evaluation without making ViewLens a required dependency for installing or using the skill.

## Bottom Line

ViewLens helps this project because promptfoo and ViewLens measure different things:

- Promptfoo measures whether the agent routes correctly, cites repo guidance, avoids overclaiming, and answers user-like prompts well.
- ViewLens measures whether an Apple UI exposes useful runtime evidence: accessibility hierarchy, focus/navigation behavior, visual-semantic mismatches, Dynamic Type reflow, contrast, target sizing, and before/after fix verification.

The right architecture is a layered evaluation model. Keep the skill self-contained and installable with `npx skills`; add ViewLens as an optional evidence provider for teams that want runtime-backed validation.

## Evaluation Layers

| Layer | Name | Tooling | What It Proves | What It Cannot Prove |
| --- | --- | --- | --- | --- |
| E0 | Static package validation | File checks, skill validation | `SKILL.md`, metadata, references, and manifests are discoverable. | Answer quality or UI behavior. |
| E1 | Prompt contract evaluation | promptfoo `C0` / `C1` / `C2` | Identity, routing, source disclosure, assumptions, negative-case behavior, and reference-doc usefulness. | Whether a specific app screen is actually accessible. |
| E2 | Runtime evidence evaluation | ViewLens CLI or MCP | UI evidence: accessibility names, roles, values, actions, focus graph, visual-semantic correlation, contrast, target size, Dynamic Type reflow, and nonvisual summaries. | Human lived experience or complete VoiceOver runtime conformance. |
| E3 | Closed-loop fix verification | ViewLens before/after reviews plus promptfoo regression prompts | Whether an agent fix changed the intended UI evidence without introducing obvious regressions. | Long-term usability across all assistive technologies and user contexts. |
| E4 | Human research and field validation | Interviews, usability studies, accessibility review partners | Whether the solution addresses real user pain points and workflows. | Exhaustive platform correctness. |

## Recommended Architecture

Keep these responsibilities separate:

- Swift Accessibility Agent: source-backed guidance, routing, implementation recommendations, and review heuristics.
- promptfoo: repeatable language and routing evaluation.
- ViewLens: optional deterministic UI evidence and nonvisual artifacts.
- Human research: lived-experience validation, pain-point discovery, and adoption feedback.

Do not bake ViewLens-specific commands into the core `SKILL.md` always-load path. Instead, route to this document when the user asks for evaluation, runtime evidence, nonvisual inspection, focus graphs, Dynamic Type reflow, or before/after accessibility verification.

## What ViewLens Adds

ViewLens is useful when a user asks questions like:

- "Can the agent prove this accessibility fix worked?"
- "Can we inspect what a screen reader or keyboard user would encounter?"
- "Can we catch accessibility issues that are not obvious from source code?"
- "Can we compare before and after UI evidence?"
- "Can we generate regression evidence for a PR?"

High-value evidence types:

- Accessibility hierarchy with names, roles, values, states, actions, frames, focus, and parent/child relationships.
- Nonvisual screen model with stable element, region, and finding IDs.
- Rotor candidate inventory where platform evidence permits it.
- Keyboard/focus traversal graph with traps, unreachable controls, and restoration problems.
- Visual-semantic correlation between rendered UI and accessibility nodes.
- Dynamic Type reflow checks across accessibility text sizes.
- Contrast and target-size checks.
- Before/after verification artifacts tied to a review ID or changed-file set.

## Evidence Policy

ViewLens evidence should use the same trust posture as repository guidance:

- `measured`: Runtime facts captured from platform APIs or hierarchy introspection.
- `derived`: Deterministic calculations from measured values, such as contrast or spatial containment.
- `inferred`: Heuristics or ML detections, such as screenshot element detection.
- `unavailable`: Evidence the tool could not capture.

The agent should not treat inferred screenshot evidence as proof of semantic accessibility. If ViewLens cannot capture the accessibility hierarchy, the answer should say that name/role/value and reading-order checks are unavailable rather than passing.

## Promptfoo Integration

Promptfoo should remain the first automated evaluation layer. Add ViewLens-aware tests as language-contract tests first:

- Does the agent know when runtime evidence is needed?
- Does the agent ask for the right kind of ViewLens artifact?
- Does the agent distinguish source guidance from measured evidence?
- Does the agent avoid claiming a fix is verified without before/after evidence?
- Does the agent treat unavailable evidence as unavailable?

Then add fixture-backed tests once ViewLens outputs are stable:

1. Run a ViewLens fixture audit and save JSON evidence under `evals/fixtures/viewlens/`.
2. Inject short evidence excerpts into promptfoo as `viewlens_ref_1` and `viewlens_ref_2`.
3. Assert that the agent cites both the repository route and the ViewLens evidence type.
4. Assert that the answer does not overclaim beyond the evidence provenance.

## Suggested Promptfoo Cases

Use user-like prompts:

- "VoiceOver reads my checkout screen in a weird order. How would you evaluate that?"
- "My Dynamic Type layout looks fine at normal size but breaks at accessibility sizes. What evidence should I collect?"
- "The screenshot looks correct, but I am not sure the buttons have useful accessibility names. Can the agent verify that?"
- "After the agent fixes this SwiftUI view, how do we know the fix did not create a new focus problem?"
- "A custom card looks like a button but VoiceOver reads it as plain text. How should we catch and fix that?"
- "My modal closes and keyboard focus disappears. What would a runtime-backed evaluation look like?"
- "Can a screenshot-only audit prove name, role, and value are correct?"

Expected behavior:

- Emit `ROUTING:` for the relevant repo guidance.
- Recommend ViewLens only as optional runtime evidence.
- Name the evidence needed, such as semantic outline, navigation graph, Dynamic Type matrix, or before/after review.
- State `Assumptions:` when no ViewLens artifact is actually provided.
- Treat screenshot-only evidence as incomplete for semantic claims.

## Optional Workflow

When ViewLens is available:

1. Run promptfoo first to validate the agent language contract.
2. Run ViewLens on a deterministic fixture or target app screen.
3. Feed the concise ViewLens evidence summary into an agent prompt.
4. Let the agent propose or apply the code change.
5. Re-run ViewLens and compare before/after evidence.
6. Add a promptfoo regression case if the failure exposed a routing or reasoning gap.

Example evidence request:

```text
Use Swift Accessibility Agent guidance for this UIKit screen. I have ViewLens evidence showing duplicate button names and a focus-order jump after dismissing a modal. Explain the likely fix and what evidence would prove the fix worked.
```

## Repo Actions

1. Keep promptfoo `C0` / `C1` / `C2` as the baseline.
2. Add ViewLens-aware gold prompts that test evidence selection and overclaim protection.
3. Add optional fixture-backed promptfoo cases after stable ViewLens JSON samples are available.
4. Add a future `C3` config only when the repo contains stable ViewLens fixture excerpts.
5. Keep ViewLens out of mandatory installation instructions unless the user explicitly wants runtime UI evaluation.


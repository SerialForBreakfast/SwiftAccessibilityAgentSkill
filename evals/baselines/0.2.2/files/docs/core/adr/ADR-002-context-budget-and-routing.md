# ADR-002: Context Budget and Routing Strategy

- Status: Accepted
- Date: 2026-09-01
- Deciders: Swift Accessibility Agent maintainers
- Tags: `context-budget`, `routing`, `progressive-disclosure`, `skill-runtime`, `promptfoo`

## Context

Swift Accessibility Agent contains broad accessibility guidance across SwiftUI, UIKit, tvOS, macOS, visionOS, testing, source governance, evaluation, and architecture. That breadth is useful, but it creates a runtime risk: an agent can waste context by loading large shared documents before it has identified the user's actual platform, framework, and task.

The skill already uses visible routing and a `references/` tree, but the manifest layer must make context discipline explicit. A skill should feel fast and precise: load enough to answer correctly, then stop.

## Decision

Adopt a route-first, budgeted loading model.

Runtime loading should use three tiers:

| Tier | Purpose | Default Behavior |
| --- | --- | --- |
| L0 | Entrypoint | Load `SKILL.md` only when the skill triggers. |
| L1 | Route resolution | Load only small manifest files needed to select platform, framework, task type, and topic. |
| L2 | Answer support | Load one backlog or index plus one or two topic references directly tied to the user's question. |
| L3 | Deep support | Load architecture, source registry, testing, evaluation, ViewLens, or watchlist docs only when the task requires them. |

The runtime should not load source registry, technology map, taxonomy, architecture principles, testing docs, or changelog by default.

## Routing Rules

1. Use user language to infer the likely domain first.
2. Load manifests only when the domain is ambiguous, multi-platform, or requires task presets.
3. Load no more than one backlog or index before selecting topic docs.
4. Load one topic guideline for focused questions.
5. Load two topic guidelines only when the user question naturally spans two concerns.
6. Load testing docs only when the user asks for verification, test planning, regression prevention, or runtime evidence.
7. Load source-governance docs only when making or checking source-quality claims.
8. Load evaluation docs only when the user asks about promptfoo, metrics, ViewLens, release gates, or agent quality.
9. Load watchlist docs only when the user asks about newly announced, previewed, or future Apple accessibility features.
10. Stop loading when the answer is sufficiently supported.

## Context Budgets

Default budget:

- `max_initial_files`: 3
- `max_initial_guidelines`: 2
- `max_backlogs`: 1
- `max_core_docs_without_reason`: 0
- `max_testing_docs_without_test_request`: 0

Escalate beyond the default only when:

- the user asks for a broad audit or architecture review
- the task is cross-platform
- the answer depends on source governance or freshness
- runtime evidence or ViewLens artifacts are involved
- a previous answer failed due to missing context

When escalating, name the reason briefly in the answer or trust footer.

## Routing Output

Continue visible routing, but keep it short:

```text
ROUTING: [uikit:u-005-grouping-containment.md, core:decision-matrix.md]
```

The routing line should name docs actually used in the answer, not every file inspected. Do not include internal manifest files unless the user specifically asks about runtime routing.

## Manifest Policy

`core.json` should describe load order and budget constraints. It should not force long shared docs into `always_load`.

Allowed `always_load` entries:

- small security or invocation policy files
- small route metadata needed to avoid unsafe behavior

Disallowed `always_load` entries:

- source registry
- technology map
- taxonomy
- architecture principles
- testing checklists
- changelog
- large guideline files

## Evaluation Impact

Promptfoo should include context-budget cases that verify:

- the agent does not cite broad core docs for focused questions when a single topic doc is enough
- generic Swift questions do not trigger repository routing
- evaluation questions route to evaluation docs
- runtime-evidence questions route to ViewLens/evaluation docs
- preview-feature questions route to the WWDC watchlist only when needed

Useful gold prompts:

- "Tell me about UILabel accessibility."
- "How do I animate a UILabel fading in?"
- "Can screenshot evidence prove my buttons have good accessibility names?"
- "How should we evaluate whether this skill is improving over time?"
- "What changed for Dynamic Type on Apple TV?"

## Consequences

Positive consequences:

- Lower token use for common questions.
- Less accidental over-citation.
- Clearer, more auditable answers.
- Easier promptfoo assertions for correct routing.
- Better separation between accepted guidance, watchlists, evaluation policy, and runtime evidence.

Tradeoffs:

- Agents may need one extra lookup when a question is broad or ambiguous.
- Some answers may start with less context and then expand.
- Maintainers must keep manifests and topic docs aligned.

## Follow-Up Actions

1. Keep `SKILL.md` concise and task-first.
2. Keep manifest files small and machine-readable.
3. Add topic indexes if backlogs become too large.
4. Add promptfoo cases for context-budget behavior.
5. Periodically review `always_load` and remove long docs from it.


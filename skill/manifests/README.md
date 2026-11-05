# Runtime Manifests (Low-Token Loading)

Purpose: let agents resolve a minimal doc set before loading long-form guidance.

## Files

- `axes.json`: allowed platform/framework/task values.
- `routes.json`: platform+framework route to default guideline/backlog paths.
- `task-presets.json`: task-specific extra docs to load.
- `platform-presets.json`: platform-specific test docs to load.
- `select-example.json`: concrete selection-to-load examples.
- `decision-rules.json`: machine-readable alternative-selection rules.
- `security-policy.json`: machine-readable execution and prompting guardrails.
- `pattern-signals.json`: machine-readable good/risky/bad pattern classification signals.
- `core.json`: always-on baseline docs and strict load order.

## Resolution Steps

1. Pick `platform`, `framework`, and `task_type`.
2. Load manifests only if route selection needs them; focused topics can route directly.
3. Resolve route in `routes.json`.
4. Select platform extras only when the task needs them.
5. Select task extras only when the task needs them.
6. Stop when evidence is sufficient; initial budget is three reference reads, excluding SKILL.md.

## Context Budget

Default to the smallest useful set:

- `SKILL.md`
- one backlog or index
- one or two topic guidelines

Do not load source registry, technology map, taxonomy, architecture, testing, evaluation, ViewLens, WWDC watchlists, or changelog unless the current task specifically requires them.

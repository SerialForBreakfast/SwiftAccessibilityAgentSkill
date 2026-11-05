# ViewLens-Assisted Gold Prompt Candidates

Current baseline: `0.2.2`

Purpose: Add user-like prompts for evaluating whether Swift Accessibility Agent knows when runtime evidence would improve confidence, without making ViewLens a required dependency for baseline promptfoo runs.

## Coverage Matrix

| ID | Coverage | User-like prompt | Expected routing | Expected ViewLens evidence |
| --- | --- | --- | --- | --- |
| VL-001 | Runtime reading order | VoiceOver reads my checkout screen in a weird order. How would you evaluate that before changing code? | `uikit:u-006-focus-reading-order.md` or `swiftui:g-006-focus-reading-order.md` | Accessibility hierarchy, navigation sequence, semantic outline |
| VL-002 | Dynamic Type reflow | My screen looks fine at normal text size but clips labels at accessibility sizes. What evidence should I collect? | `uikit:u-010-dynamic-type-layout-resilience.md` or SwiftUI Dynamic Type guidance | Dynamic Type matrix, clipping findings, before/after screenshots or reports |
| VL-003 | Screenshot evidence boundary | The screenshot looks correct, but I am not sure the buttons have useful accessibility names. Can the agent verify that from the screenshot alone? | `uikit:u-001-labels-meaningful-names.md`, `uikit:u-004-traits-roles.md` | State that screenshot-only evidence cannot prove name/role/value; request semantic hierarchy |
| VL-004 | Visual-semantic mismatch | A custom card looks like a button, but VoiceOver reads it like plain text. How should we catch and fix that? | `uikit:u-008-custom-controls-semantic-equivalence.md` or `swiftui:g-008-custom-controls-representation.md` | Visual-semantic correlation, role/name/action evidence |
| VL-005 | Modal focus restoration | My modal closes and keyboard focus disappears. What would a runtime-backed evaluation look like? | `uikit:u-013-modal-focus-containment.md` or `macos:m-007-modal-window-focus-containment.md` | Before/after focus graph, launch anchor, dismissal restoration evidence |
| VL-006 | Fix verification | After the agent changes a SwiftUI view, how do we know it fixed accessibility and did not create a new focus problem? | `testing:xcuitest-hooks.md`, `testing:inspector-audit-checklist.md` | Before/after ViewLens review IDs, diffed findings, navigation graph |
| VL-007 | Rotor candidates | My dashboard has headings and custom row actions. How can I check whether it is efficient for VoiceOver users? | `swiftui:g-009-rotors-when-and-why.md`, `uikit:u-009-rotor-friendly-structure.md` | Rotor candidate inventory where available, headings/actions outline, linear navigation fallback |
| VL-008 | Evidence provenance | ViewLens says a screenshot audit found no issues. Can I call the screen accessible? | `core:pattern-review-rubric.md`, `core:viewlens-evaluation-integration.md` | Distinguish measured, derived, inferred, and unavailable evidence; avoid full pass claim |

## Assertions To Add Later

These cases should assert that the answer:

- includes `ROUTING:` when repository guidance is used
- names the expected repository guidance
- mentions ViewLens only as optional runtime evidence
- asks for the specific artifact needed, not a vague "run an audit"
- does not claim screenshot-only audits prove semantic accessibility
- includes `Assumptions:` when no actual ViewLens artifact is provided
- uses provenance language such as measured, derived, inferred, or unavailable when discussing ViewLens output


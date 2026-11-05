# Context-Budget Gold Prompt Candidates

Current baseline: `0.2.2`

Purpose: Evaluate whether Swift Accessibility Agent answers from the smallest useful set of repository guidance instead of loading or citing broad docs unnecessarily.

## Coverage Matrix

| ID | Coverage | User-like prompt | Expected routing | Context-budget expectation |
| --- | --- | --- | --- | --- |
| CB-001 | Focused UIKit topic | Tell me about UILabel accessibility. | `uikit:u-001-labels-meaningful-names.md`, optionally `uikit:u-004-traits-roles.md` | Do not cite source registry, architecture principles, testing docs, ViewLens, or WWDC watchlist. |
| CB-002 | Generic Swift negative case | How do I animate a UILabel fading in? | no routing | Do not load or cite repository docs. |
| CB-003 | Evaluation question | How should we measure whether this skill is improving over time? | `core:ADR-001-robust-evaluation-methodology.md` | Route to evaluation methodology, not platform guidelines. |
| CB-004 | Runtime evidence question | Can screenshot evidence prove my buttons have good accessibility names? | `core:viewlens-evaluation-integration.md`, optionally `uikit:u-001-labels-meaningful-names.md` | Name semantic hierarchy as needed evidence; do not claim screenshot-only proof. |
| CB-005 | Preview feature question | What changed for Dynamic Type on Apple TV? | `core:wwdc-2026-accessibility-watchlist.md`, optionally `tvos` text/layout guidance | Treat preview/watchlist material as watchlist guidance, not accepted implementation guidance. |
| CB-006 | Broad architecture question | How should our design system prevent accessibility regressions across SwiftUI and UIKit? | `core:architecture-principles.md`, `core:decision-matrix.md` | It is acceptable to load core architecture docs because the prompt asks for architecture. |

## Assertions To Add Later

These cases should assert that the answer:

- names only the docs actually used in `ROUTING:`
- does not cite broad core docs for focused topic questions
- does not emit `ROUTING:` for generic non-accessibility Swift questions
- routes evaluation, ViewLens, and WWDC watchlist questions to their specific docs
- includes `Assumptions:` when relying on preview/watchlist or unavailable runtime evidence
- keeps testing docs out of answers unless verification, regression, or runtime evidence is requested


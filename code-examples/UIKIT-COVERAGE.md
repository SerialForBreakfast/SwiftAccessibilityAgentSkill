# UIKit assertion coverage and next work

UIKit is the first implementation phase. SwiftUI expansion is deferred. This is a
claim/behavior inventory, not a percentage of all Apple accessibility documentation.
The current examples target iOS26 with exact tested SDK/runtime records; annual
anchors and their promotion remain separate.

## Coverage map

| Guideline | Current code-contract coverage | Next meaningful UIKit assertions |
| --- | --- | --- |
| U-001 Labels | Explicit labels; attributed/plain linkage; collection reconfiguration/reuse and speech-language metadata | Native label/title defaults |
| U-002 Hints | Hint/value separation; error replacement/recovery; removable-state hints cleared on cell reconfiguration/reuse | Source-inventory audit for remaining unit-testable claims |
| U-003 Values | Value transitions; adjustable hooks; native slider/stepper bounds; switch callbacks; formatted timeline values and invalid-duration reset | Source-inventory audit; formatting policies are separate from UIKit contracts |
| U-004 Traits | Selected/heading role transitions preserve unrelated traits; native enabled/selected flags and synthesized control state | Native-control accessibility defaults |
| U-005 Containers | Exposed descendants, grouping flag, explicit element lists, data-table type, virtual-element insertion/removal and nested semantic-group/list configuration | Source-inventory audit for remaining unit-testable claims |
| U-006 Order | Stored identity/order; rotor direction; reorder and removed-current-item policy; text ranges; captured layout/screen notification kinds and target arguments | Source-inventory audit; notification delivery remains outside unit claims |
| U-007 Custom actions | Independent handlers, stale-action guards, ordinary paths, attributed names, weak targets; edit category removal/replacement on state changes | Source-inventory audit for remaining unit-testable claims |
| U-008 Custom controls | Virtual element metadata/frame; adjustable hooks; activation callback success/failure and disabled guard; escape handling | Explicit older-path fallback logic |
| U-009 Rotor structure | Dynamic element searches; real text ranges, Unicode offsets, foreign-element handling and weak targets | Stale text ranges after document editing; overlapping matches and richer text policies |
| U-010 Dynamic Type | Explicit traits/cap; twelve-category body metrics; reusable label typography across headline/caption/body and actual trait overrides | Source-inventory audit; retain failed detached-trait examples as history |
| U-011 Color/non-color cues | Semantic colors resolved under appearance/contrast traits; concrete border refresh; visible text and accessible error cues | Additional non-color selection states; separate any contrast calculation from UIKit claims |
| U-012 Motion | Public preference reader, duration-policy branches, private-center refresh/filtering, stop/restart and observer ownership | Source-inventory audit; actual system notification delivery is outside these tests |
| U-013 Modal behavior | Modal/hiding flags, overlay teardown/reopen, rejected escape, ordinary Close action, form-sheet/dismissal configuration | Modal content and captured restoration target; no focus-delivery assertion |
| U-014 Tables/forms | Cell reconfiguration/reuse; reusable action identity; native UIAction replacement/removal; form error reset; data-table dimensions/spans/header lookup; section/header configuration | Source-inventory audit for remaining unit-testable claims |
| U-015 Media | Native-control settings; Play/Pause and timeline metadata; local synthetic subtitle/audio groups; full versus forced-only subtitles; explicit selection/off and independent audio/text choices | Audio-description metadata and supplemental stream-inspection scope audit; no rendered/media-quality claims |

## Measurement rules

- [Pilot one](pilots/uikit-v1/README.md) supplies three focused unit tests plus
  isolated negatives. [The semantic expansion](pilots/uikit-semantics-v1/README.md)
  supplies per-test source/claim mappings in its coverage manifest.
- Count unique asserted behaviors separately from repeated runs, mutants and
  compound assertions. A single test may support several guidelines; do not add
  those mappings together as independent coverage.
- Distinguish an Apple API observation from application policy. For example,
  Bool action handlers are public API; once-only archival and non-wrapping rotor
  search are chosen example policies.
- A configured element order is not an observed reading order. Calling a handler
  directly is not proof of gesture, keyboard or assistive-technology delivery.
- Framework configuration checks are supporting evidence, not exhaustive tests of
  Apple's implementation. Documentation retains its existing source tier.
- Every new positive needs a reviewed source/locator and an appropriate negative
  where feasible. Preserve unexpected failures; do not weaken assertions to raise
  the pass count. Independent review and benchmark promotion remain separate.

## Next batches

The [completion audit](UIKIT-COMPLETION-AUDIT.md) binds remaining work to guideline
clauses and these recorded gaps; counts alone do not close the UIKit phase.

1. Add native accessibility defaults and remaining value/action transitions.
2. Address motion observer lifecycle and text-range edits.
3. View-controller presentation configuration and availability/fallback audit.
4. Review remaining media metadata/inspection assertions against the source inventory.
5. Review remaining Tier1 claims before claiming completeness; only then plan the
   SwiftUI phase. No UI tests or mandatory manual verification are added.

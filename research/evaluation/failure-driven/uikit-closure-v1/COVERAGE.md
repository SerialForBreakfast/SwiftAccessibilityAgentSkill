# UIKit Coverage Ledger

Generated from `clause-ledger.json`; author review, independent acceptance pending.
Coverage describes the bounded example assertions, not universal accessibility.

| Guideline | Covered | Partial | Testable gap | Outside unit scope | SwiftUI deferred |
| --- | ---: | ---: | ---: | ---: | ---: |
| [U-001](../../../../references/uikit/guidelines/u-001-labels-meaningful-names.md) | 3 | 8 | 0 | 2 | 2 |
| [U-002](../../../../references/uikit/guidelines/u-002-hints-when-to-use.md) | 3 | 6 | 0 | 2 | 2 |
| [U-003](../../../../references/uikit/guidelines/u-003-values-stateful-controls.md) | 2 | 7 | 0 | 2 | 2 |
| [U-004](../../../../references/uikit/guidelines/u-004-traits-roles.md) | 1 | 9 | 0 | 2 | 2 |
| [U-005](../../../../references/uikit/guidelines/u-005-grouping-containment.md) | 1 | 9 | 0 | 2 | 2 |
| [U-006](../../../../references/uikit/guidelines/u-006-focus-reading-order.md) | 1 | 9 | 0 | 2 | 2 |
| [U-007](../../../../references/uikit/guidelines/u-007-accessibility-custom-actions.md) | 2 | 6 | 0 | 2 | 2 |
| [U-008](../../../../references/uikit/guidelines/u-008-custom-controls-semantic-equivalence.md) | 0 | 8 | 0 | 2 | 2 |
| [U-009](../../../../references/uikit/guidelines/u-009-rotor-friendly-structure.md) | 2 | 12 | 0 | 4 | 2 |
| [U-010](../../../../references/uikit/guidelines/u-010-dynamic-type-layout-resilience.md) | 2 | 5 | 0 | 4 | 2 |
| [U-011](../../../../references/uikit/guidelines/u-011-color-contrast-non-color-cues.md) | 1 | 8 | 0 | 1 | 2 |
| [U-012](../../../../references/uikit/guidelines/u-012-reduced-motion.md) | 0 | 8 | 0 | 2 | 2 |
| [U-013](../../../../references/uikit/guidelines/u-013-modal-focus-containment.md) | 0 | 9 | 0 | 2 | 2 |
| [U-014](../../../../references/uikit/guidelines/u-014-table-collection-form-semantics.md) | 1 | 9 | 0 | 2 | 2 |
| [U-015](../../../../references/uikit/guidelines/u-015-media-captions-descriptions-controls.md) | 3 | 10 | 0 | 2 | 3 |

## Identified Implementation Gaps

| Clause | Family | Disposition |
| --- | --- | --- |
| U-005-L24 | GAP-SUMMARY | implemented-validated-unit-scope |
| U-005-L52 | GAP-SUMMARY | implemented-validated-unit-scope |
| U-008-L24 | GAP-QUANTITY | implemented-validated-unit-scope |
| U-009-L27 | GAP-QUANTITY | implemented-validated-unit-scope |
| U-012-L25 | GAP-MOTION-FEEDBACK | implemented-validated-unit-scope |
| U-012-L46 | GAP-MOTION-FEEDBACK | implemented-validated-unit-scope |
| U-012-L51 | GAP-MOTION-FEEDBACK | implemented-validated-unit-scope |

## Clause Review

Bindings resolve to exact method IDs, body hashes, source claims and matching execution receipts in the JSON ledger and assertion catalog.

### U-001

Rule: Every meaningful interactive element and non-decorative content element must expose a clear accessibility label that reflects user intent, not implementation details.

Disposition: partially-covered. The rule is broader than its directly asserted example contracts. Metadata/callback evidence supports the listed portions; universal meaning, speech, navigation, visual quality and usability are not inferred.

| Clause | Requirement | Disposition | Assertion bindings |
| --- | --- | --- | --- |
| [U-001-L23](../../../../references/uikit/guidelines/u-001-labels-meaningful-names.md#L23) | Prefer semantic controls (`UIButton`, `UISwitch`, `UITextField`, etc.) over gesture-only generic views. | partially-covered | native |
| [U-001-L24](../../../../references/uikit/guidelines/u-001-labels-meaningful-names.md#L24) | Set `accessibilityLabel` when visible text is missing or insufficient. | covered | names |
| [U-001-L25](../../../../references/uikit/guidelines/u-001-labels-meaningful-names.md#L25) | Mark decorative-only imagery as non-accessible. | covered | decoration |
| [U-001-L26](../../../../references/uikit/guidelines/u-001-labels-meaningful-names.md#L26) | Keep sibling control labels distinct within the same context. | covered | names |
| [U-001-L30](../../../../references/uikit/guidelines/u-001-labels-meaningful-names.md#L30) | Ensure `UIHostingController` container logic does not override UIKit labels unintentionally. | swiftui-deferred | Documentation scope |
| [U-001-L31](../../../../references/uikit/guidelines/u-001-labels-meaningful-names.md#L31) | Keep semantic naming aligned between UIKit parents and hosted SwiftUI children. | swiftui-deferred | Documentation scope |
| [U-001-L37](../../../../references/uikit/guidelines/u-001-labels-meaningful-names.md#L37) | Verify each meaningful control has a non-empty label. | partially-covered | names |
| [U-001-L38](../../../../references/uikit/guidelines/u-001-labels-meaningful-names.md#L38) | Verify labels disambiguate sibling controls. | partially-covered | names |
| [U-001-L39](../../../../references/uikit/guidelines/u-001-labels-meaningful-names.md#L39) | Verify decorative-only elements are not focusable. | partially-covered | decoration |
| [U-001-L43](../../../../references/uikit/guidelines/u-001-labels-meaningful-names.md#L43) | Swipe through screen order and confirm each control is announced with a meaningful name. | documentation-supported/outside-unit-scope | Documentation scope |
| [U-001-L44](../../../../references/uikit/guidelines/u-001-labels-meaningful-names.md#L44) | Confirm icon-only controls announce user intent (for example, "Delete message"). | documentation-supported/outside-unit-scope | Documentation scope |
| [U-001-L48](../../../../references/uikit/guidelines/u-001-labels-meaningful-names.md#L48) | Assert critical controls exist via stable identifiers. | partially-covered | native |
| [U-001-L49](../../../../references/uikit/guidelines/u-001-labels-meaningful-names.md#L49) | Assert high-risk control labels for user-critical flows. | partially-covered | names |
| [U-001-L53](../../../../references/uikit/guidelines/u-001-labels-meaningful-names.md#L53) | Do: add explicit labels to icon-only buttons and custom icon controls. | partially-covered | names |
| [U-001-L54](../../../../references/uikit/guidelines/u-001-labels-meaningful-names.md#L54) | Don't: use vague or repeated labels that do not distinguish actions. | partially-covered | names |

### U-002

Rule: Add an accessibility hint only when label, value, and role do not already communicate what action will occur.

Disposition: partially-covered. The rule is broader than its directly asserted example contracts. Metadata/callback evidence supports the listed portions; universal meaning, speech, navigation, visual quality and usability are not inferred.

| Clause | Requirement | Disposition | Assertion bindings |
| --- | --- | --- | --- |
| [U-002-L23](../../../../references/uikit/guidelines/u-002-hints-when-to-use.md#L23) | Use `accessibilityHint` only for controls with non-obvious consequences. | partially-covered | hints |
| [U-002-L24](../../../../references/uikit/guidelines/u-002-hints-when-to-use.md#L24) | Omit hints for standard controls when semantics are already clear. | partially-covered | hints |
| [U-002-L25](../../../../references/uikit/guidelines/u-002-hints-when-to-use.md#L25) | Keep hints short and action-oriented. | partially-covered | hints |
| [U-002-L26](../../../../references/uikit/guidelines/u-002-hints-when-to-use.md#L26) | Re-check hints when control behavior changes to prevent stale guidance. | covered | hints |
| [U-002-L30](../../../../references/uikit/guidelines/u-002-hints-when-to-use.md#L30) | In mixed stacks, avoid duplicate hints between UIKit wrappers and hosted SwiftUI content. | swiftui-deferred | Documentation scope |
| [U-002-L31](../../../../references/uikit/guidelines/u-002-hints-when-to-use.md#L31) | Ensure hint ownership is clear for shared controls. | swiftui-deferred | Documentation scope |
| [U-002-L37](../../../../references/uikit/guidelines/u-002-hints-when-to-use.md#L37) | Confirm hints are present only where extra action context is needed. | partially-covered | hints |
| [U-002-L38](../../../../references/uikit/guidelines/u-002-hints-when-to-use.md#L38) | Confirm hint text does not duplicate label/value verbatim. | covered | hints |
| [U-002-L42](../../../../references/uikit/guidelines/u-002-hints-when-to-use.md#L42) | Focus controls and verify announcements stay concise. | documentation-supported/outside-unit-scope | Documentation scope |
| [U-002-L43](../../../../references/uikit/guidelines/u-002-hints-when-to-use.md#L43) | Confirm custom behavior controls include useful hints. | documentation-supported/outside-unit-scope | Documentation scope |
| [U-002-L47](../../../../references/uikit/guidelines/u-002-hints-when-to-use.md#L47) | Validate presence/absence of hints for selected high-risk controls where metadata is inspectable. | partially-covered | hints |
| [U-002-L51](../../../../references/uikit/guidelines/u-002-hints-when-to-use.md#L51) | Do: add hints for destructive actions when consequence is not obvious. | partially-covered | hints |
| [U-002-L52](../../../../references/uikit/guidelines/u-002-hints-when-to-use.md#L52) | Don't: repeat the label as the hint. | covered | hints |

### U-003

Rule: Any UI element with meaningful state must provide an accurate accessibility value that updates with state changes.

Disposition: partially-covered. The rule is broader than its directly asserted example contracts. Metadata/callback evidence supports the listed portions; universal meaning, speech, navigation, visual quality and usability are not inferred.

| Clause | Requirement | Disposition | Assertion bindings |
| --- | --- | --- | --- |
| [U-003-L23](../../../../references/uikit/guidelines/u-003-values-stateful-controls.md#L23) | Use native controls first, then add `accessibilityValue` for custom stateful elements. | partially-covered | values |
| [U-003-L24](../../../../references/uikit/guidelines/u-003-values-stateful-controls.md#L24) | Keep value text concise and user-focused (for example, "On", "75 percent"). | partially-covered | values |
| [U-003-L25](../../../../references/uikit/guidelines/u-003-values-stateful-controls.md#L25) | Ensure value updates are synchronized with visual state changes. | partially-covered | choice |
| [U-003-L26](../../../../references/uikit/guidelines/u-003-values-stateful-controls.md#L26) | For reusable cells/views, clear stale values during reuse. | covered | values |
| [U-003-L30](../../../../references/uikit/guidelines/u-003-values-stateful-controls.md#L30) | In mixed screens, confirm UIKit values and SwiftUI values do not conflict for equivalent controls. | swiftui-deferred | Documentation scope |
| [U-003-L31](../../../../references/uikit/guidelines/u-003-values-stateful-controls.md#L31) | Validate state forwarding across representable boundaries. | swiftui-deferred | Documentation scope |
| [U-003-L37](../../../../references/uikit/guidelines/u-003-values-stateful-controls.md#L37) | Inspect stateful elements and verify value is present and current. | partially-covered | values |
| [U-003-L38](../../../../references/uikit/guidelines/u-003-values-stateful-controls.md#L38) | Trigger state change and re-check value immediately. | covered | values |
| [U-003-L42](../../../../references/uikit/guidelines/u-003-values-stateful-controls.md#L42) | Focus stateful controls and confirm spoken output includes current value. | documentation-supported/outside-unit-scope | Documentation scope |
| [U-003-L43](../../../../references/uikit/guidelines/u-003-values-stateful-controls.md#L43) | Change state and confirm subsequent focus announces updated value. | documentation-supported/outside-unit-scope | Documentation scope |
| [U-003-L47](../../../../references/uikit/guidelines/u-003-values-stateful-controls.md#L47) | Assert representative toggle/slider/value state labels after interaction. | partially-covered | values |
| [U-003-L51](../../../../references/uikit/guidelines/u-003-values-stateful-controls.md#L51) | Do: expose selected/not-selected, progress, or numeric values where state matters. | partially-covered | values |
| [U-003-L52](../../../../references/uikit/guidelines/u-003-values-stateful-controls.md#L52) | Don't: rely only on color or animation to communicate state. | partially-covered | choice |

### U-004

Rule: Use native semantic controls whenever possible; when custom UI is unavoidable, explicitly set accessibility traits/roles to match actual behavior.

Disposition: partially-covered. The rule is broader than its directly asserted example contracts. Metadata/callback evidence supports the listed portions; universal meaning, speech, navigation, visual quality and usability are not inferred.

| Clause | Requirement | Disposition | Assertion bindings |
| --- | --- | --- | --- |
| [U-004-L23](../../../../references/uikit/guidelines/u-004-traits-roles.md#L23) | Prefer semantic UIKit controls over gesture-only generic `UIView` interactions. | partially-covered | native |
| [U-004-L24](../../../../references/uikit/guidelines/u-004-traits-roles.md#L24) | Set `accessibilityTraits` to align announcements with actual behavior. | partially-covered | traits, custom, quantityGap |
| [U-004-L25](../../../../references/uikit/guidelines/u-004-traits-roles.md#L25) | Mark structural headings where section navigation is needed. | covered | headings |
| [U-004-L26](../../../../references/uikit/guidelines/u-004-traits-roles.md#L26) | Ensure selected/adjustable/destructive context is represented consistently. | partially-covered | traits, custom |
| [U-004-L30](../../../../references/uikit/guidelines/u-004-traits-roles.md#L30) | Validate trait mapping when UIKit hosts SwiftUI via `UIHostingController`. | swiftui-deferred | Documentation scope |
| [U-004-L31](../../../../references/uikit/guidelines/u-004-traits-roles.md#L31) | Ensure container-level behavior does not flatten child role semantics. | swiftui-deferred | Documentation scope |
| [U-004-L37](../../../../references/uikit/guidelines/u-004-traits-roles.md#L37) | Verify each interactive element has correct role/trait. | partially-covered | traits, custom |
| [U-004-L38](../../../../references/uikit/guidelines/u-004-traits-roles.md#L38) | Verify heading landmarks appear where expected. | partially-covered | headings |
| [U-004-L39](../../../../references/uikit/guidelines/u-004-traits-roles.md#L39) | Verify custom controls are not exposed as generic static text. | partially-covered | traits, custom |
| [U-004-L43](../../../../references/uikit/guidelines/u-004-traits-roles.md#L43) | Confirm announcements include expected role/trait context. | documentation-supported/outside-unit-scope | Documentation scope |
| [U-004-L44](../../../../references/uikit/guidelines/u-004-traits-roles.md#L44) | Confirm heading navigation works for long content sections. | documentation-supported/outside-unit-scope | Documentation scope |
| [U-004-L48](../../../../references/uikit/guidelines/u-004-traits-roles.md#L48) | Assert trait-related behavior indirectly through state/label/value output for key controls. | partially-covered | traits, custom |
| [U-004-L52](../../../../references/uikit/guidelines/u-004-traits-roles.md#L52) | Do: use native controls first and add traits only for semantic correction. | partially-covered | native |
| [U-004-L53](../../../../references/uikit/guidelines/u-004-traits-roles.md#L53) | Don't: ship tappable container views without role exposure. | partially-covered | traits, custom |

### U-005

Rule: Set accessibility grouping so combined content is concise, interactive children remain reachable when needed, and decorative noise is removed from traversal.

Disposition: partially-covered. The rule is broader than its directly asserted example contracts. Metadata/callback evidence supports the listed portions; universal meaning, speech, navigation, visual quality and usability are not inferred.

| Clause | Requirement | Disposition | Assertion bindings |
| --- | --- | --- | --- |
| [U-005-L23](../../../../references/uikit/guidelines/u-005-grouping-containment.md#L23) | Use container `isAccessibilityElement` and `accessibilityElements` behavior intentionally. | covered | grouped |
| [U-005-L24](../../../../references/uikit/guidelines/u-005-grouping-containment.md#L24) | Combine text fragments only when they represent one concept. | partially-covered | grouped, summaryGap |
| [U-005-L25](../../../../references/uikit/guidelines/u-005-grouping-containment.md#L25) | Keep child controls separately reachable when they support distinct actions. | partially-covered | independent, decoration |
| [U-005-L26](../../../../references/uikit/guidelines/u-005-grouping-containment.md#L26) | Hide decorative views from accessibility traversal. | partially-covered | decoration |
| [U-005-L30](../../../../references/uikit/guidelines/u-005-grouping-containment.md#L30) | In mixed containers, verify UIKit grouping does not flatten hosted SwiftUI children unexpectedly. | swiftui-deferred | Documentation scope |
| [U-005-L31](../../../../references/uikit/guidelines/u-005-grouping-containment.md#L31) | Re-check grouping after list or cell refactors. | swiftui-deferred | Documentation scope |
| [U-005-L37](../../../../references/uikit/guidelines/u-005-grouping-containment.md#L37) | Verify tree structure matches expected conceptual groups. | partially-covered | grouped |
| [U-005-L38](../../../../references/uikit/guidelines/u-005-grouping-containment.md#L38) | Verify actionable children remain focusable. | partially-covered | independent, decoration |
| [U-005-L39](../../../../references/uikit/guidelines/u-005-grouping-containment.md#L39) | Verify decorative descendants are not separate focus targets. | partially-covered | decoration |
| [U-005-L43](../../../../references/uikit/guidelines/u-005-grouping-containment.md#L43) | Swipe grouped sections and confirm concise announcements. | documentation-supported/outside-unit-scope | Documentation scope |
| [U-005-L44](../../../../references/uikit/guidelines/u-005-grouping-containment.md#L44) | Confirm individually actionable controls remain reachable. | documentation-supported/outside-unit-scope | independent, decoration |
| [U-005-L48](../../../../references/uikit/guidelines/u-005-grouping-containment.md#L48) | Use identifier-level assertions for expected child element presence/absence in grouped rows. | partially-covered | independent, decoration |
| [U-005-L52](../../../../references/uikit/guidelines/u-005-grouping-containment.md#L52) | Do: combine title and subtitle when they represent one row concept. | partially-covered | grouped, summaryGap |
| [U-005-L53](../../../../references/uikit/guidelines/u-005-grouping-containment.md#L53) | Don't: combine rows that contain separately actionable controls. | partially-covered | independent, decoration |

### U-006

Rule: Accessibility focus order must follow coherent task flow; use structural hierarchy first and explicit ordering overrides only for real edge cases.

Disposition: partially-covered. The rule is broader than its directly asserted example contracts. Metadata/callback evidence supports the listed portions; universal meaning, speech, navigation, visual quality and usability are not inferred.

| Clause | Requirement | Disposition | Assertion bindings |
| --- | --- | --- | --- |
| [U-006-L23](../../../../references/uikit/guidelines/u-006-focus-reading-order.md#L23) | Build semantic order through view hierarchy and container composition. | partially-covered | ordered, grouped |
| [U-006-L24](../../../../references/uikit/guidelines/u-006-focus-reading-order.md#L24) | Avoid arbitrary subview reordering that breaks expected traversal. | partially-covered | ordered, grouped |
| [U-006-L25](../../../../references/uikit/guidelines/u-006-focus-reading-order.md#L25) | Ensure overlays and modals do not leave background elements focusable. | partially-covered | modal |
| [U-006-L26](../../../../references/uikit/guidelines/u-006-focus-reading-order.md#L26) | Use explicit `accessibilityElements` ordering only when structure alone is insufficient. | covered | ordered, grouped |
| [U-006-L30](../../../../references/uikit/guidelines/u-006-focus-reading-order.md#L30) | Validate focus order across UIKit containers hosting SwiftUI content. | swiftui-deferred | Documentation scope |
| [U-006-L31](../../../../references/uikit/guidelines/u-006-focus-reading-order.md#L31) | Re-test order after introducing representables, overlays, or async insertions. | swiftui-deferred | Documentation scope |
| [U-006-L37](../../../../references/uikit/guidelines/u-006-focus-reading-order.md#L37) | Inspect traversal order and verify alignment with task flow. | partially-covered | ordered, grouped |
| [U-006-L38](../../../../references/uikit/guidelines/u-006-focus-reading-order.md#L38) | Confirm hidden/overlay elements are not focused before primary content. | partially-covered | modal |
| [U-006-L39](../../../../references/uikit/guidelines/u-006-focus-reading-order.md#L39) | Confirm explicit ordering overrides are minimal and intentional. | partially-covered | ordered, grouped |
| [U-006-L43](../../../../references/uikit/guidelines/u-006-focus-reading-order.md#L43) | Swipe through each screen and verify sequence matches user workflow. | documentation-supported/outside-unit-scope | Documentation scope |
| [U-006-L44](../../../../references/uikit/guidelines/u-006-focus-reading-order.md#L44) | Open/dismiss modal content and confirm focus handoff and restoration. | documentation-supported/outside-unit-scope | Documentation scope |
| [U-006-L48](../../../../references/uikit/guidelines/u-006-focus-reading-order.md#L48) | Add screen-level smoke tests asserting key controls appear in expected interaction sequence. | partially-covered | ordered, grouped |
| [U-006-L52](../../../../references/uikit/guidelines/u-006-focus-reading-order.md#L52) | Do: structure views so natural hierarchy produces the right order. | partially-covered | ordered, grouped |
| [U-006-L53](../../../../references/uikit/guidelines/u-006-focus-reading-order.md#L53) | Don't: patch structural ordering defects with widespread manual overrides. | partially-covered | ordered, grouped |

### U-007

Rule: Any interaction that cannot be reliably discovered through default control semantics must provide explicit accessibility custom actions.

Disposition: partially-covered. The rule is broader than its directly asserted example contracts. Metadata/callback evidence supports the listed portions; universal meaning, speech, navigation, visual quality and usability are not inferred.

| Clause | Requirement | Disposition | Assertion bindings |
| --- | --- | --- | --- |
| [U-007-L23](../../../../references/uikit/guidelines/u-007-accessibility-custom-actions.md#L23) | Use `UIAccessibilityCustomAction` for contextual row operations and gesture-heavy behaviors. | partially-covered | actions |
| [U-007-L24](../../../../references/uikit/guidelines/u-007-accessibility-custom-actions.md#L24) | Keep action names concise, task-focused, and distinct. | partially-covered | actions |
| [U-007-L25](../../../../references/uikit/guidelines/u-007-accessibility-custom-actions.md#L25) | Ensure action handlers update UI state and semantics immediately. | partially-covered | actionstate |
| [U-007-L29](../../../../references/uikit/guidelines/u-007-accessibility-custom-actions.md#L29) | Ensure action ownership is not duplicated between UIKit containers and hosted SwiftUI rows. | swiftui-deferred | Documentation scope |
| [U-007-L30](../../../../references/uikit/guidelines/u-007-accessibility-custom-actions.md#L30) | Re-check action menus when migrating rows between stacks. | swiftui-deferred | Documentation scope |
| [U-007-L36](../../../../references/uikit/guidelines/u-007-accessibility-custom-actions.md#L36) | Verify expected custom actions are exposed on relevant elements. | covered | actions |
| [U-007-L37](../../../../references/uikit/guidelines/u-007-accessibility-custom-actions.md#L37) | Verify no duplicate/ambiguous action names on the same element. | covered | actions |
| [U-007-L41](../../../../references/uikit/guidelines/u-007-accessibility-custom-actions.md#L41) | Focus element, open actions menu, confirm expected actions exist. | documentation-supported/outside-unit-scope | Documentation scope |
| [U-007-L42](../../../../references/uikit/guidelines/u-007-accessibility-custom-actions.md#L42) | Execute each action and verify result/state is announced. | documentation-supported/outside-unit-scope | Documentation scope |
| [U-007-L46](../../../../references/uikit/guidelines/u-007-accessibility-custom-actions.md#L46) | Validate resulting state changes for action-driven operations via labels/values. | partially-covered | actionstate |
| [U-007-L50](../../../../references/uikit/guidelines/u-007-accessibility-custom-actions.md#L50) | Do: expose swipe-only table row actions through custom actions. | partially-covered | actions |
| [U-007-L51](../../../../references/uikit/guidelines/u-007-accessibility-custom-actions.md#L51) | Don't: depend solely on gestures for critical operations. | partially-covered | independent, actions |

### U-008

Rule: Any custom interactive UIKit component must expose equivalent semantics (role, label, value, actions) to the native control it replaces.

Disposition: partially-covered. The rule is broader than its directly asserted example contracts. Metadata/callback evidence supports the listed portions; universal meaning, speech, navigation, visual quality and usability are not inferred.

| Clause | Requirement | Disposition | Assertion bindings |
| --- | --- | --- | --- |
| [U-008-L23](../../../../references/uikit/guidelines/u-008-custom-controls-semantic-equivalence.md#L23) | Prefer native controls whenever possible. | partially-covered | native |
| [U-008-L24](../../../../references/uikit/guidelines/u-008-custom-controls-semantic-equivalence.md#L24) | For custom controls, set `isAccessibilityElement`, label, value, traits, and custom actions explicitly. | partially-covered | custom, traits, quantityGap |
| [U-008-L25](../../../../references/uikit/guidelines/u-008-custom-controls-semantic-equivalence.md#L25) | Keep semantic state synchronized with visual state transitions. | partially-covered | traits |
| [U-008-L29](../../../../references/uikit/guidelines/u-008-custom-controls-semantic-equivalence.md#L29) | Ensure representable boundaries preserve custom control semantics. | swiftui-deferred | Documentation scope |
| [U-008-L30](../../../../references/uikit/guidelines/u-008-custom-controls-semantic-equivalence.md#L30) | Validate parent container behavior does not mask child custom-control traits. | swiftui-deferred | Documentation scope |
| [U-008-L44](../../../../references/uikit/guidelines/u-008-custom-controls-semantic-equivalence.md#L44) | Confirm custom controls are exposed as intended semantic types. | partially-covered | custom, traits |
| [U-008-L45](../../../../references/uikit/guidelines/u-008-custom-controls-semantic-equivalence.md#L45) | Confirm label/value/traits/actions are present and consistent. | partially-covered | custom, traits |
| [U-008-L49](../../../../references/uikit/guidelines/u-008-custom-controls-semantic-equivalence.md#L49) | Focus custom control and verify announcement matches role/state intent. | documentation-supported/outside-unit-scope | Documentation scope |
| [U-008-L50](../../../../references/uikit/guidelines/u-008-custom-controls-semantic-equivalence.md#L50) | Trigger interactions and confirm updated state feedback. | documentation-supported/outside-unit-scope | Documentation scope |
| [U-008-L54](../../../../references/uikit/guidelines/u-008-custom-controls-semantic-equivalence.md#L54) | Assert critical custom control states via labels/values/identifiers. | partially-covered | custom, traits |
| [U-008-L58](../../../../references/uikit/guidelines/u-008-custom-controls-semantic-equivalence.md#L58) | Do: model custom steppers as adjustable controls with clear increment/decrement behavior. | partially-covered | traits |
| [U-008-L59](../../../../references/uikit/guidelines/u-008-custom-controls-semantic-equivalence.md#L59) | Don't: ship custom tappable views with no semantic role. | partially-covered | custom, traits |

### U-009

Rule: Screens with repeated sections, dense content, or contextual row actions should expose heading and structural semantics so users can jump efficiently, without making rotor fluency a prerequisite for core task completion.

Disposition: partially-covered. The rule is broader than its directly asserted example contracts. Metadata/callback evidence supports the listed portions; universal meaning, speech, navigation, visual quality and usability are not inferred.

| Clause | Requirement | Disposition | Assertion bindings |
| --- | --- | --- | --- |
| [U-009-L23](../../../../references/uikit/guidelines/u-009-rotor-friendly-structure.md#L23) | Mark true section landmarks with heading traits. | covered | headings |
| [U-009-L24](../../../../references/uikit/guidelines/u-009-rotor-friendly-structure.md#L24) | Structure table/collection/form regions and containers so major sections are semantically distinct. | partially-covered | headings, grouped |
| [U-009-L25](../../../../references/uikit/guidelines/u-009-rotor-friendly-structure.md#L25) | Keep primary actions directly discoverable in the linear traversal path. | partially-covered | rotor, independent |
| [U-009-L26](../../../../references/uikit/guidelines/u-009-rotor-friendly-structure.md#L26) | Expose contextual or overflow row operations with accessibility custom actions when inline controls would overload the layout. | partially-covered | actions |
| [U-009-L27](../../../../references/uikit/guidelines/u-009-rotor-friendly-structure.md#L27) | Treat rotor support as acceleration, not the sole path to complete the task. | partially-covered | rotor, independent, quantityGap |
| [U-009-L28](../../../../references/uikit/guidelines/u-009-rotor-friendly-structure.md#L28) | Avoid over-marking every row as a heading. | partially-covered | headings |
| [U-009-L32](../../../../references/uikit/guidelines/u-009-rotor-friendly-structure.md#L32) | Confirm heading semantics remain intact when UIKit containers host SwiftUI sections. | swiftui-deferred | Documentation scope |
| [U-009-L33](../../../../references/uikit/guidelines/u-009-rotor-friendly-structure.md#L33) | Re-test rotor behavior after screen composition changes, especially when container ownership or row-action placement changes. | swiftui-deferred | Documentation scope |
| [U-009-L39](../../../../references/uikit/guidelines/u-009-rotor-friendly-structure.md#L39) | Verify heading traits are present on intended landmarks. | covered | headings |
| [U-009-L40](../../../../references/uikit/guidelines/u-009-rotor-friendly-structure.md#L40) | Verify hierarchy supports section-level navigation and meaningful containers. | partially-covered | headings, grouped |
| [U-009-L41](../../../../references/uikit/guidelines/u-009-rotor-friendly-structure.md#L41) | Verify contextual actions are attached to the intended row or element when applicable. | partially-covered | actions |
| [U-009-L45](../../../../references/uikit/guidelines/u-009-rotor-friendly-structure.md#L45) | Swipe linearly through the screen and confirm core tasks remain fully discoverable without rotor changes. | documentation-supported/outside-unit-scope | Documentation scope |
| [U-009-L46](../../../../references/uikit/guidelines/u-009-rotor-friendly-structure.md#L46) | Use rotor to navigate by headings. | documentation-supported/outside-unit-scope | Documentation scope |
| [U-009-L47](../../../../references/uikit/guidelines/u-009-rotor-friendly-structure.md#L47) | Confirm jumps land on expected semantic anchors. | documentation-supported/outside-unit-scope | Documentation scope |
| [U-009-L48](../../../../references/uikit/guidelines/u-009-rotor-friendly-structure.md#L48) | Open the actions menu on complex rows and confirm contextual actions are present without replacing primary controls. | documentation-supported/outside-unit-scope | Documentation scope |
| [U-009-L52](../../../../references/uikit/guidelines/u-009-rotor-friendly-structure.md#L52) | Use structural proxies (presence of heading-labeled elements and contextual-action-bearing rows) for limited automation. | partially-covered | headings, grouped |
| [U-009-L56](../../../../references/uikit/guidelines/u-009-rotor-friendly-structure.md#L56) | Do: define headings for major sections in long forms. | partially-covered | headings |
| [U-009-L57](../../../../references/uikit/guidelines/u-009-rotor-friendly-structure.md#L57) | Do: expose contextual row operations through custom accessibility actions when direct controls would overload the row. | partially-covered | actions |
| [U-009-L58](../../../../references/uikit/guidelines/u-009-rotor-friendly-structure.md#L58) | Don't: mark decorative captions or every row title as headings. | partially-covered | headings |
| [U-009-L59](../../../../references/uikit/guidelines/u-009-rotor-friendly-structure.md#L59) | Don't: make primary task completion depend on rotor-only discovery. | partially-covered | rotor, independent |

### U-010

Rule: All user-facing text and interactive layouts must remain readable and operable across supported Dynamic Type sizes, including accessibility categories.

Disposition: partially-covered. The rule is broader than its directly asserted example contracts. Metadata/callback evidence supports the listed portions; universal meaning, speech, navigation, visual quality and usability are not inferred.

| Clause | Requirement | Disposition | Assertion bindings |
| --- | --- | --- | --- |
| [U-010-L23](../../../../references/uikit/guidelines/u-010-dynamic-type-layout-resilience.md#L23) | Use Dynamic Type-compatible fonts (`preferredFont` + text styles). | covered | fonts |
| [U-010-L24](../../../../references/uikit/guidelines/u-010-dynamic-type-layout-resilience.md#L24) | Enable automatic content-size-category adjustments for text controls. | covered | fonts |
| [U-010-L25](../../../../references/uikit/guidelines/u-010-dynamic-type-layout-resilience.md#L25) | Avoid fixed row heights and rigid constraints that clip text at large sizes. | partially-covered | longtext, checkout |
| [U-010-L26](../../../../references/uikit/guidelines/u-010-dynamic-type-layout-resilience.md#L26) | Validate cell reuse with long localized strings and large text sizes. | partially-covered | longtext |
| [U-010-L30](../../../../references/uikit/guidelines/u-010-dynamic-type-layout-resilience.md#L30) | Verify UIKit constraints do not clip hosted SwiftUI content at large sizes. | swiftui-deferred | Documentation scope |
| [U-010-L31](../../../../references/uikit/guidelines/u-010-dynamic-type-layout-resilience.md#L31) | Keep text-scaling behavior consistent across mixed UIKit/SwiftUI screens. | swiftui-deferred | Documentation scope |
| [U-010-L37](../../../../references/uikit/guidelines/u-010-dynamic-type-layout-resilience.md#L37) | Review screens at large categories for clipping, truncation, and overlap. | documentation-supported/outside-unit-scope | Documentation scope |
| [U-010-L38](../../../../references/uikit/guidelines/u-010-dynamic-type-layout-resilience.md#L38) | Verify tappable targets remain reachable after text expansion. | documentation-supported/outside-unit-scope | Documentation scope |
| [U-010-L42](../../../../references/uikit/guidelines/u-010-dynamic-type-layout-resilience.md#L42) | Enable large text category and verify focus order still matches workflow. | documentation-supported/outside-unit-scope | Documentation scope |
| [U-010-L43](../../../../references/uikit/guidelines/u-010-dynamic-type-layout-resilience.md#L43) | Confirm critical labels and actions remain discoverable. | documentation-supported/outside-unit-scope | Documentation scope |
| [U-010-L47](../../../../references/uikit/guidelines/u-010-dynamic-type-layout-resilience.md#L47) | Add smoke/snapshot checks for key screens at selected large content-size categories. | partially-covered | longtext |
| [U-010-L51](../../../../references/uikit/guidelines/u-010-dynamic-type-layout-resilience.md#L51) | Do: allow text to wrap and containers to expand naturally. | partially-covered | longtext |
| [U-010-L52](../../../../references/uikit/guidelines/u-010-dynamic-type-layout-resilience.md#L52) | Don't: lock essential text into fixed-height rows that truncate at accessibility sizes. | partially-covered | longtext |

### U-011

Rule: Any meaningful status, feedback, or interaction cue conveyed with color must also be conveyed with text, symbol, shape, or another non-color indicator, and text/controls must maintain sufficient contrast.

Disposition: partially-covered. The rule is broader than its directly asserted example contracts. Metadata/callback evidence supports the listed portions; universal meaning, speech, navigation, visual quality and usability are not inferred.

| Clause | Requirement | Disposition | Assertion bindings |
| --- | --- | --- | --- |
| [U-011-L23](../../../../references/uikit/guidelines/u-011-color-contrast-non-color-cues.md#L23) | Pair color changes with text or symbolic indicators. | partially-covered | choice, errors |
| [U-011-L24](../../../../references/uikit/guidelines/u-011-color-contrast-non-color-cues.md#L24) | Use system semantic colors where possible. | covered | colors |
| [U-011-L25](../../../../references/uikit/guidelines/u-011-color-contrast-non-color-cues.md#L25) | Avoid encoding selection/validation state solely by tint differences. | partially-covered | choice, errors |
| [U-011-L26](../../../../references/uikit/guidelines/u-011-color-contrast-non-color-cues.md#L26) | Validate contrast in all supported appearances. | partially-covered | contrast |
| [U-011-L30](../../../../references/uikit/guidelines/u-011-color-contrast-non-color-cues.md#L30) | Align color-state semantics between UIKit and hosted SwiftUI components. | swiftui-deferred | Documentation scope |
| [U-011-L31](../../../../references/uikit/guidelines/u-011-color-contrast-non-color-cues.md#L31) | Ensure mixed styling layers do not remove non-color cues. | swiftui-deferred | Documentation scope |
| [U-011-L37](../../../../references/uikit/guidelines/u-011-color-contrast-non-color-cues.md#L37) | Run contrast and visual checks for text and interactive elements. | partially-covered | contrast |
| [U-011-L38](../../../../references/uikit/guidelines/u-011-color-contrast-non-color-cues.md#L38) | Verify status indicators include non-color semantic cues. | partially-covered | choice, errors |
| [U-011-L42](../../../../references/uikit/guidelines/u-011-color-contrast-non-color-cues.md#L42) | Confirm spoken output includes state/error context otherwise represented visually by color. | documentation-supported/outside-unit-scope | Documentation scope |
| [U-011-L46](../../../../references/uikit/guidelines/u-011-color-contrast-non-color-cues.md#L46) | Assert presence of explicit state labels/symbols for critical statuses. | partially-covered | choice, errors |
| [U-011-L50](../../../../references/uikit/guidelines/u-011-color-contrast-non-color-cues.md#L50) | Do: combine text/icon labels with color to indicate status. | partially-covered | choice, errors |
| [U-011-L51](../../../../references/uikit/guidelines/u-011-color-contrast-non-color-cues.md#L51) | Don't: indicate required, selected, or error states with color alone. | partially-covered | choice, errors |

### U-012

Rule: When Reduce Motion is enabled, replace non-essential animations with low-motion alternatives that preserve state-change clarity.

Disposition: partially-covered. The rule is broader than its directly asserted example contracts. Metadata/callback evidence supports the listed portions; universal meaning, speech, navigation, visual quality and usability are not inferred.

| Clause | Requirement | Disposition | Assertion bindings |
| --- | --- | --- | --- |
| [U-012-L23](../../../../references/uikit/guidelines/u-012-reduced-motion.md#L23) | Detect reduced-motion settings and conditionally reduce animation intensity. | partially-covered | motion, observers |
| [U-012-L24](../../../../references/uikit/guidelines/u-012-reduced-motion.md#L24) | Prefer fades or immediate state updates over large motion transitions. | partially-covered | motion |
| [U-012-L25](../../../../references/uikit/guidelines/u-012-reduced-motion.md#L25) | Ensure critical state changes remain clear without motion cues. | partially-covered | errors, motion, motionGap |
| [U-012-L29](../../../../references/uikit/guidelines/u-012-reduced-motion.md#L29) | Keep transition behavior consistent when UIKit and SwiftUI components are combined. | swiftui-deferred | Documentation scope |
| [U-012-L30](../../../../references/uikit/guidelines/u-012-reduced-motion.md#L30) | Validate that hosted SwiftUI transitions do not reintroduce heavy motion. | swiftui-deferred | Documentation scope |
| [U-012-L36](../../../../references/uikit/guidelines/u-012-reduced-motion.md#L36) | Verify key transitions remain understandable with reduced motion. | partially-covered | errors, motion |
| [U-012-L37](../../../../references/uikit/guidelines/u-012-reduced-motion.md#L37) | Verify state changes remain visible without motion dependence. | partially-covered | errors, motion |
| [U-012-L41](../../../../references/uikit/guidelines/u-012-reduced-motion.md#L41) | Enable Reduce Motion and run core flows. | documentation-supported/outside-unit-scope | Documentation scope |
| [U-012-L42](../../../../references/uikit/guidelines/u-012-reduced-motion.md#L42) | Confirm navigation/state context remains clear after transitions. | documentation-supported/outside-unit-scope | Documentation scope |
| [U-012-L46](../../../../references/uikit/guidelines/u-012-reduced-motion.md#L46) | Add smoke tests for final UI state after transitions when reduced-motion mode is on. | partially-covered | errors, motion, motionGap |
| [U-012-L50](../../../../references/uikit/guidelines/u-012-reduced-motion.md#L50) | Do: replace spring-heavy animations with subtle fades or direct updates. | partially-covered | motion |
| [U-012-L51](../../../../references/uikit/guidelines/u-012-reduced-motion.md#L51) | Don't: hide completion feedback in motion-only effects. | partially-covered | errors, motion, motionGap |

### U-013

Rule: When presenting sheets, alerts, or overlays, focus must move into presented content, stay within relevant modal elements, and return to a logical anchor on dismissal.

Disposition: partially-covered. The rule is broader than its directly asserted example contracts. Metadata/callback evidence supports the listed portions; universal meaning, speech, navigation, visual quality and usability are not inferred.

| Clause | Requirement | Disposition | Assertion bindings |
| --- | --- | --- | --- |
| [U-013-L23](../../../../references/uikit/guidelines/u-013-modal-focus-containment.md#L23) | Ensure modal context includes a clear heading/title and primary action. | partially-covered | modal |
| [U-013-L24](../../../../references/uikit/guidelines/u-013-modal-focus-containment.md#L24) | Prevent inactive background content from remaining in traversal. | partially-covered | modal |
| [U-013-L25](../../../../references/uikit/guidelines/u-013-modal-focus-containment.md#L25) | Provide explicit dismissal actions with clear labels. | partially-covered | modal |
| [U-013-L26](../../../../references/uikit/guidelines/u-013-modal-focus-containment.md#L26) | Restore focus to launch trigger or nearest logical anchor on dismissal. | partially-covered | restoration |
| [U-013-L30](../../../../references/uikit/guidelines/u-013-modal-focus-containment.md#L30) | Validate `UIHostingController` modals for focus handoff and restoration. | swiftui-deferred | Documentation scope |
| [U-013-L31](../../../../references/uikit/guidelines/u-013-modal-focus-containment.md#L31) | Confirm mixed presentation styles do not leak background focus targets. | swiftui-deferred | Documentation scope |
| [U-013-L37](../../../../references/uikit/guidelines/u-013-modal-focus-containment.md#L37) | Verify modal tree is reachable and prioritized over background content. | partially-covered | modal |
| [U-013-L38](../../../../references/uikit/guidelines/u-013-modal-focus-containment.md#L38) | Verify inactive background elements are not focusable. | partially-covered | modal |
| [U-013-L42](../../../../references/uikit/guidelines/u-013-modal-focus-containment.md#L42) | Present modal and confirm focus lands on modal title or first primary action. | documentation-supported/outside-unit-scope | Documentation scope |
| [U-013-L43](../../../../references/uikit/guidelines/u-013-modal-focus-containment.md#L43) | Dismiss modal and confirm focus returns to expected anchor. | documentation-supported/outside-unit-scope | Documentation scope |
| [U-013-L47](../../../../references/uikit/guidelines/u-013-modal-focus-containment.md#L47) | Add flow tests asserting modal entry/exit controls and post-dismiss anchor presence. | partially-covered | modal |
| [U-013-L51](../../../../references/uikit/guidelines/u-013-modal-focus-containment.md#L51) | Do: announce modal context with a clear title and predictable action. | partially-covered | modal |
| [U-013-L52](../../../../references/uikit/guidelines/u-013-modal-focus-containment.md#L52) | Don't: allow focus to traverse background controls while modal is active. | partially-covered | modal |

### U-014

Rule: In tables, collections, and forms, prefer native controls and explicit row semantics so each item exposes clear label, value, role, and action behavior.

Disposition: partially-covered. The rule is broader than its directly asserted example contracts. Metadata/callback evidence supports the listed portions; universal meaning, speech, navigation, visual quality and usability are not inferred.

| Clause | Requirement | Disposition | Assertion bindings |
| --- | --- | --- | --- |
| [U-014-L23](../../../../references/uikit/guidelines/u-014-table-collection-form-semantics.md#L23) | Use standard UIKit controls in cells/forms for built-in semantics. | partially-covered | native, controls, checkout |
| [U-014-L24](../../../../references/uikit/guidelines/u-014-table-collection-form-semantics.md#L24) | Decide per row whether content should be combined or separately actionable. | partially-covered | grouped, independent |
| [U-014-L25](../../../../references/uikit/guidelines/u-014-table-collection-form-semantics.md#L25) | Expose contextual row actions through custom actions when needed. | partially-covered | actions |
| [U-014-L26](../../../../references/uikit/guidelines/u-014-table-collection-form-semantics.md#L26) | Reset reused cell accessibility state to avoid stale labels/values. | covered | cells, values |
| [U-014-L30](../../../../references/uikit/guidelines/u-014-table-collection-form-semantics.md#L30) | Align UIKit cell semantics with SwiftUI row semantics in mixed screens. | swiftui-deferred | Documentation scope |
| [U-014-L31](../../../../references/uikit/guidelines/u-014-table-collection-form-semantics.md#L31) | Verify embedded hosted views do not duplicate row announcements. | swiftui-deferred | Documentation scope |
| [U-014-L37](../../../../references/uikit/guidelines/u-014-table-collection-form-semantics.md#L37) | Check each row/control exposes expected role and current value. | partially-covered | cells, values |
| [U-014-L38](../../../../references/uikit/guidelines/u-014-table-collection-form-semantics.md#L38) | Check grouped rows do not hide required child actions. | partially-covered | grouped, independent |
| [U-014-L39](../../../../references/uikit/guidelines/u-014-table-collection-form-semantics.md#L39) | Check toggles/sliders expose adjustable/state semantics correctly. | partially-covered | native, controls |
| [U-014-L43](../../../../references/uikit/guidelines/u-014-table-collection-form-semantics.md#L43) | Traverse table/collection/form content and confirm concise announcements. | documentation-supported/outside-unit-scope | Documentation scope |
| [U-014-L44](../../../../references/uikit/guidelines/u-014-table-collection-form-semantics.md#L44) | Interact with stateful controls and confirm updated values are announced. | documentation-supported/outside-unit-scope | Documentation scope |
| [U-014-L48](../../../../references/uikit/guidelines/u-014-table-collection-form-semantics.md#L48) | Assert representative row/control identifiers and state labels in key flows. | partially-covered | cells, values |
| [U-014-L52](../../../../references/uikit/guidelines/u-014-table-collection-form-semantics.md#L52) | Do: keep each row semantically focused on one primary task. | partially-covered | grouped, independent |
| [U-014-L53](../../../../references/uikit/guidelines/u-014-table-collection-form-semantics.md#L53) | Don't: pack multiple unrelated actions into one unlabeled cell. | partially-covered | grouped, independent |

### U-015

Rule: Media experiences must provide accessible playback control semantics and support captions/subtitles for spoken content; when visual-only meaning is important, provide descriptive alternatives.

Disposition: partially-covered. The rule is broader than its directly asserted example contracts. Metadata/callback evidence supports the listed portions; universal meaning, speech, navigation, visual quality and usability are not inferred.

| Clause | Requirement | Disposition | Assertion bindings |
| --- | --- | --- | --- |
| [U-015-L23](../../../../references/uikit/guidelines/u-015-media-captions-descriptions-controls.md#L23) | Ensure play/pause/seek/speed controls expose clear labels, values, and roles. | partially-covered | media, speed |
| [U-015-L24](../../../../references/uikit/guidelines/u-015-media-captions-descriptions-controls.md#L24) | Expose current playback state and timing readouts accessibly. | partially-covered | media, speed |
| [U-015-L25](../../../../references/uikit/guidelines/u-015-media-captions-descriptions-controls.md#L25) | Provide caption/subtitle options where spoken media exists. | partially-covered | captions, metadata |
| [U-015-L26](../../../../references/uikit/guidelines/u-015-media-captions-descriptions-controls.md#L26) | Define a narrow debug/test inspection contract when stream state includes live/on-demand mode, seekability, buffering, playback rate, or selected media options that are useful for verification but too noisy for spoken output. | covered | inspection, metadata |
| [U-015-L27](../../../../references/uikit/guidelines/u-015-media-captions-descriptions-controls.md#L27) | Avoid gesture-only media controls without accessible action alternatives. | partially-covered | media, speed |
| [U-015-L31](../../../../references/uikit/guidelines/u-015-media-captions-descriptions-controls.md#L31) | In mixed AVKit/SwiftUI flows, ensure control labels and state are consistent across layers. | swiftui-deferred | Documentation scope |
| [U-015-L32](../../../../references/uikit/guidelines/u-015-media-captions-descriptions-controls.md#L32) | Assign one owner for supplemental stream-state metadata so host overlays and embedded players report one consistent state model. | swiftui-deferred | Documentation scope |
| [U-015-L33](../../../../references/uikit/guidelines/u-015-media-captions-descriptions-controls.md#L33) | Verify custom overlays do not block native accessible controls. | swiftui-deferred | Documentation scope |
| [U-015-L39](../../../../references/uikit/guidelines/u-015-media-captions-descriptions-controls.md#L39) | Verify all media controls are discoverable and labeled. | partially-covered | media, speed |
| [U-015-L40](../../../../references/uikit/guidelines/u-015-media-captions-descriptions-controls.md#L40) | Verify playback state/value updates are exposed. | partially-covered | media, speed |
| [U-015-L41](../../../../references/uikit/guidelines/u-015-media-captions-descriptions-controls.md#L41) | Verify caption-related controls are reachable when available. | partially-covered | captions, metadata |
| [U-015-L42](../../../../references/uikit/guidelines/u-015-media-captions-descriptions-controls.md#L42) | Capture stream kind, seekability, buffering/loading state, playback rate, and selected media-option context where supported. | covered | inspection, metadata |
| [U-015-L46](../../../../references/uikit/guidelines/u-015-media-captions-descriptions-controls.md#L46) | Navigate media controls and confirm each control announces purpose and state. | documentation-supported/outside-unit-scope | Documentation scope |
| [U-015-L47](../../../../references/uikit/guidelines/u-015-media-captions-descriptions-controls.md#L47) | Enable captions/subtitles and verify operation without touch exploration. | documentation-supported/outside-unit-scope | Documentation scope |
| [U-015-L51](../../../../references/uikit/guidelines/u-015-media-captions-descriptions-controls.md#L51) | Add smoke tests for playback-state transitions and caption-toggle availability. | partially-covered | media, speed |
| [U-015-L52](../../../../references/uikit/guidelines/u-015-media-captions-descriptions-controls.md#L52) | Assert supplemental inspection snapshot fields when playback state exceeds what the spoken response should include. | covered | inspection, metadata |
| [U-015-L56](../../../../references/uikit/guidelines/u-015-media-captions-descriptions-controls.md#L56) | Do: provide clear labeled controls for play, pause, and timeline navigation. | partially-covered | media, speed |
| [U-015-L57](../../../../references/uikit/guidelines/u-015-media-captions-descriptions-controls.md#L57) | Don't: hide primary controls behind unlabeled gestures or icon-only overlays. | partially-covered | media, speed |

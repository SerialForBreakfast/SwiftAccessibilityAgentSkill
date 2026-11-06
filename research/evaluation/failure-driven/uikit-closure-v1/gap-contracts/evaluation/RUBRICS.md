# Controller Rubrics

Status: author draft; independent review pending; not baseline-eligible.
These are development cases, not holdouts. Deliver only `prompts.json` to the
subject. Keep this file, examples, mutants, ledger and run receipts controller-only.

## Common Scoring

Score each criterion 0 (absent/wrong), 1 (partial), or 2 (complete), reporting
criteria individually. Compile/runtime outcomes are separate from semantic scores.
Accept equivalent implementations; class names, storage and event wiring need not
match this fixture. A source citation or test count does not substitute for behavior.
Do not demand UI tests, spoken-output checks or manual verification.

Each answer must distinguish directly tested configuration/callback behavior from
assistive navigation or rendering. A compilable example without its requested
unit tests is incomplete, not necessarily incorrect. Infrastructure failures are
ungraded, not subject failures. Preserve first answers before any repairs.

## UC-SUMMARY-D1

Framework: UIKit-specific. Shared principle: preserve meaning during reuse.
Source claim: manifest `metadata`; ledger gap `GAP-SUMMARY`.
Assertions: `testSummary*`; negative: `summary-name`.

1. Uses the supplied complete localized summary without reconstructing or truncating it.
2. Configures a single noninteractive concept and avoids duplicate child elements.
3. Reconfiguration replaces owned metadata and visible text; stale value is cleared
   where the chosen implementation stores it. Do not require clearing unrelated state.
4. Includes focused reuse/configuration tests without claiming speech/navigation proof.

Accept a dedicated UIAccessibilityElement or a grouped UIView implementation when
its metadata and children satisfy the contract. Do not require `.staticText` as the
only valid trait configuration. The fixture's preservation of unrelated traits is a
defensive policy, not a mandate to retain contradictory inherited roles.
Critical errors: exposing an interactive child only through an inaccessible grouped
parent in an expanded implementation; dropping part of the supplied description.

## UC-QUANTITY-D1

Framework: UIKit-specific. Shared principle: independent ordinary interaction.
Source claim: manifest `metadata`; ledger gap `GAP-QUANTITY`.
Assertions: `testQuantity*`, `testOrdinaryQuantityButtonsChangeSameState`,
`testAdjustableHooksSynchronizeBeforeCallback`, `testDisabledQuantityRejectsBothDirectPaths`.
Negatives: `ordinary-quantity`, `disabled-quantity`, `disabled-metadata`.

1. Exposes a named adjustable value and working ordinary increase/decrease controls.
2. Both paths apply the stated 0...3 range and disabled policy to the same state;
   custom metadata reflects availability without destroying unrelated traits.
3. Updates value before notifying; emits only genuine changes, including at bounds.
4. Tests both paths, disabled/re-enabled behavior and bounds; avoids ownership cycles.

Accept target/action, UIAction, delegate or state-controller designs. Do not require
UIStackView, specific event names or identical string formatting. Localized names
may be supplied by callers. The range and callback timing are application policy,
not intrinsic UIKit guarantees. Directly invoking a callback tests that callback;
it does not establish how VoiceOver discovers or dispatches it.
Critical errors: ordinary controls absent/nonfunctional, ignored disabled state,
unbounded mutation or double notification for a single state transition.

## UC-MOTION-FEEDBACK-D1

Framework: shared principle demonstrated through UIKit.
Source claim: manifest `motion`; ledger gap `GAP-MOTION-FEEDBACK`.
Assertions: `testReducedMotion*`, `testMotion*`; negative: `motion-feedback`.

1. Commits final visible and accessibility metadata independently of animation completion.
2. Uses current Reduce Motion preference at update time, or an equivalently refreshed
   observation; deterministic preference injection is accepted for tests.
3. Keeps optional animation separate and preserves caller-supplied localized messages.
4. Tests both preference states, transitions and replacement of an earlier error/status.

Accept state-first rendering, a presentation coordinator or separately injected
animation driver. A reduced-motion alternative animation is acceptable if its
choice is justified and completion never gates state. Do not require duration 0.25,
notifications, a specific animation API or a global preference mutation in tests.
Critical error: leaving stale state because animation was omitted/cancelled.

## Review and Promotion

Reviewer checks neutrality, sufficient inputs, alternative implementations and
assertion scope against Apple sources. Record accepted, needs revision or unresolved
per criterion. Native validation and independent rubric acceptance are separate gates.
No model runs or frozen-baseline changes are authorized by this package.

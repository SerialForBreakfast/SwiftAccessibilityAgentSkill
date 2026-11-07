# First attempts and skill gaps

## FWD-01: conditional-compilation text generation error

Classification: test-authoring/generator defect. This batch selected
41 methods, but none executed because five generated `#endif }` lines put tokens
after a Swift conditional directive. The native adapter reported `error` with
incomplete/inconsistent unit evidence, not a successful mutant rejection.

Exact first test source, manifest and sanitized compiler diagnostics are preserved
in incidents/. Raw command/source/result snapshots remain private. Repair1 puts the
closing brace on its own line; no product behavior was changed for that repair.
This is not accessibility guidance or evidence of another model's weakness.

## Oracle audit before native execution

A source review found that a discarded coordinator could make disabled-shortcut
tests pass for the wrong reason. The test setup explicitly retains owners for
ordinary configuration/action assertions. Dedicated weak-lifetime tests create
separate owners and drain autorelease pools where appropriate. This was corrected
before first execution, so no fabricated failing outcome is recorded.

## Candidate skill lessons

- Forward optional fields in both directions: nil help/status must clear stale values.
- Read current item identity at the actual native entry point; custom and ordinary
  actions remain independently usable and must not accumulate handlers.
- Preserve unrelated native trait bits; platform role declarations differ. The SDK
  declares AppKit heading role availability at macOS26; host27 testing is not26
  runtime proof. UIKit header traits are not SwiftUI-generated role evidence.
- Test final application state before optional animation, including reduced motion
  and reentrancy, rather than treating an animation callback as the state update.
- Direct native metadata/coordinator assertions are useful but do not establish
  automatic hosting updates or generated SwiftUI semantic forwarding.

These lessons are research candidates. Released guidance and frozen baselines are
unchanged; no model evaluation or skill promotion has occurred.

## FWD-02: Objective-C heading constant does not import as `.heading`

Classification: implementation/API spelling defect. The installed AppKit header
has NSAccessibilityHeadingRole with macOS26 availability, but its Swift import is
NSAccessibility.Role.headingRole. The initial guessed `.heading` failed the second
package build. Exact source and diagnostics are in incidents/second-*.

A declaration-only global-name probe returned the compiler rename diagnostic. The
controller prematurely launched a global-name revision before inspecting that probe
result; that third package build failed too. This is an orchestration/sequencing
error, not a new independent accessibility discovery or model ranking. Its inputs
and diagnostics are in incidents/third-*; neither failed build ran any units.

A subsequent declaration-only `.headingRole` probe succeeded under Swift6, target26
and the selected SDK27. The final revision uses that member in source and tests.
The API contract has used its maximum two repairs (.heading -> global -> headingRole);
no further automatic repair is allowed for this member. Header availability and
Swift import spelling are separate facts; source annotations alone did not justify
the guessed member. Earlier campaign evidence is preserved unchanged.

## FWD-03: inactive-platform mutation branch

Classification: negative-control coverage gap found by source audit before execution.
The initial hint mutation changed `setAccessibilityHelp(snapshot.hint)` in the
AppKit branch but left the UIKit assignment unchanged. A UIKit run would therefore
not challenge nil-hint clearing. No passing rejection is claimed for that source.
Both original UIKit mutant files/manifests remain in incidents/.

Corrected UIKit controls explicitly replace nil with Old in accessibilityHint. Their
manifests are revision5; Mac remains revision4. The frozen runner stopped at the
input fingerprint change, preserving completed Mac attempts. A new plan imports
only matching verified Mac receipts. controller-events.json records this transition;
no completed attempt or historical skill/baseline was overwritten.

## Residual assertion/integration limits for review

The current units assert the primary name, selected-state text/value, clearing,
children, action effects and unrelated-trait preservation. Detail-label/custom-action
name text and the selected-on native flag have source configuration evidence but
not dedicated getter assertions for every variant. Font checks establish configured
font/wrapping/adjustment properties, not rendered scaling or full style matching.
The surface is a contract fixture with application-supplied layout, not a complete
visual screen. Opacity-policy units do not inspect the inline SwiftUI background.
These limits are not silently converted into covered host requirements or gates
requiring the maintainer to perform manual verification.

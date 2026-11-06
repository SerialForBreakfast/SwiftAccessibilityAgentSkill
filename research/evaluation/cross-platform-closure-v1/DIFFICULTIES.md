# Difficulties and oracle boundaries

## CLOSURE-01: Objective-C names are not the Swift API

Classification: accidental source defect, plus isolation warning. First macOS
compile failed before unit execution. Exact first source, tests, manifest and
sanitized diagnostics are preserved in `incidents/`; raw inputs/logs remain in the
immutable `closure-mac-compile-r1` attempt.

The first source declared:

```swift
func rotor(_ rotor: NSAccessibilityCustomRotor,
           resultFor parameters: NSAccessibilityCustomRotorSearchParameters)
    -> NSAccessibilityCustomRotorItemResult?
```

Compiler errors required the Swift-imported nested names:
`NSAccessibilityCustomRotor.SearchParameters` and
`NSAccessibilityCustomRotor.ItemResult`. The delegate conformance also warned about
crossing into main-actor state. Repair 1 uses those nested names and an explicitly
main-actor-isolated conformance; it does not suppress checking with `@preconcurrency`.
The revision-1 failure stays separate from revision-2 outcomes. No model comparison
or ranking follows from this single authoring incident.

The natural Mac text question tests the same real task without showing the wrong
names or compiler answer. Review the import/isolation requirement as an API-validity
criterion, not a requirement to use this implementation's helper classes.

## CLOSURE-02: UITextView member availability is platform-specific

Classification: source-audit finding, not an observed compiler failure. The existing
iOS reader was reused for TV only after inspecting UIKit declarations. `UITextView`
is available, but `isEditable` is unavailable on tvOS. The TV source and assertion
omit that member; the original iOS package remains unchanged. No synthesized failure
is recorded. The TV rotor prompt tests native API selection and text preservation.

## CLOSURE-03: Identity and generation need separate assertions

Classification: oracle design. For a loaded AVPlayerItem result, matching request
generation does not establish current-item identity; identity alone does not reject
an older refresh of the same item. Tests exercise both. The external-replacement
negative keeps the original item alive using `withExtendedLifetime`, so a weak
reference disappearing cannot accidentally make the mutant pass for another reason.
This is a deliberate control, not an accidental native failure.

## CLOSURE-04: Async ownership is not transport scheduling

The deterministic injected completions cover synchronous, late, repeated,
reentrant and out-of-order responses. They do not test a server, network cancellation,
Task scheduling or actual media-property loading. Previous media fixtures cover
extraction separately. Unknown field IDs/empty errors, input snapshots and field
order are explicit application policy, not claims Apple mandates that policy.

## CLOSURE-05: A helper test can miss native entry points

The first closure state package called ordinary activation and accessibility press
but did not directly call `keyDown`. The same campaign adds synthetic NSEvent method
calls and explicit custom-row role/state assertions in the detail package. These
are unit tests, not UI automation. Native table selection tests alone were not used
to infer row-role coverage.

## Preservation and review

Deliberate mutants are separate from accidental defects. Assertion failures must
match selected failure IDs. Historical sources and baseline hashes remain untouched.
Independent review is pending; submission is not acceptance. No further automatic
repair loop follows a second unsuccessful repair for the same contract.

## CLOSURE-06: Cross-family updates leave a stale owned label

Classification: accidental implementation defect, found in review and reproduced
before repair. The first TV state suite passed its isolated cases, but search wrote
an explicit status.accessibilityLabel and configure later changed only status.text.
Two new transition assertions failed: search -> selection, and repeated alternating
updates. Exact first source/tests/manifest and diagnostics are in incidents/tv-state-first-*.

Repair1 is revision2 of tvos-state-recovery-v1. configure clears the obsolete owned
label override so the native label derives from current text again. The original
TV closure source stays immutable and the candidate native-state route selects the
recovery package. A deliberate stale-status control reintroduces the first source.
The independent repair question includes the complete original source, not the
solution or diagnostics. Metadata getters prove this defect; no VoiceOver session
was run or invented.

## Non-failing diagnostics

The exact native logs also preserve Swift warnings that weak test-local variables
were never reassigned, AppIntents metadata-extraction notices for a package without
that dependency, and host service diagnostics. They were not recategorized as
accessibility defects or suppressed to obtain a green result. Selected test IDs,
assertion failures and adapter environment checks determine each recorded outcome.

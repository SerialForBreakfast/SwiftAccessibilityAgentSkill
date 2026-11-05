# OS26 fixture preparation — not gold-ready

**6 candidate fixes · 12 single-error variants · 3 UIKit tests authored · Apple execution not run.**

These are proposed known-good implementations, not established oracles. No native
pass, mutation kill or independent review is claimed. Historical reports are unchanged.
The package has no external dependencies. `Host/FixtureApp.swift` is an application
entry point kept outside the package library. An Xcode app/test project has **not**
been generated or qualified on BigDog; Swift on Linux cannot compile UIKit/SwiftUI.

## Apple validation setup

1. Create separate iOS and tvOS SwiftUI App targets in Xcode, deployment **26.0**.
   Add this directory as a local Swift package and link `OS26Fixtures`. Replace the
   template App source with `Host/FixtureApp.swift`. Record SDK and runtime builds.
2. Add a local `Poster` image asset to the tvOS target (any synthetic placeholder;
   record its hash). The screen shows eight independently identified movie tiles.
   Do not substitute a missing-image rendering when reviewing visual behavior.
3. Run package XCTest on an iOS26 simulator using Xcode's package scheme. Run the
   app targets separately. Native execution and Apple tooling are peer-owned gates.
4. Test the unmodified candidate first. Then, in a disposable copy, replace exactly
   one same-named `Sources/OS26Fixtures/` file with the corresponding `Mutations/`
   file. Rebuild and run the SAME relevant tests/manual checks. Restore before the
   next variant. No mutation is applied to this checkout by the offline runner.
5. Capture source hashes, exact commands, exit statuses and interaction evidence
   privately. Never convert this manifest's expected outcomes into observed results.

`manifest.json` binds each source and mutation. Mutations are outside SwiftPM source
roots, so only the selected candidate compiles by default. Patch markers identify
fix regions. The host callbacks log effects rather than deleting rows, navigating,
charging or persisting preferences; this deliberately keeps IDs observable for
repeated activation. It is a test instrument, not production behavior.

## Required interactions (in addition to automated checks)

| Case | Exercise | Expected observation / mutation detection |
|---|---|---|
| 01 | VoiceOver traverse and activate Downloads and Help; switch both ways | Both controls exposed, current state, one callback per activation. Hide-controls fails traversal; drop-help fails callback. |
| 02 | Refresh same cell Alice → Bob → Alice → Bob, no prepareForReuse | Current label/status every time. Unit test rejects stale label and stale status. Verify actual VoiceOver announcement separately. |
| 03 | Container widths 320/375pt; change live from normal to largest accessibility text; long localized total | Full total readable, no overlap/constraint errors, Pay callback once, appearance unchanged. Fixed-height and no-live-scaling must fail. Unit prerequisites alone do not establish layout. |
| 04 | iPad: focus Alpha/Bravo without activating, then visible Delete using VoiceOver and FKA+hardware keyboard; separately swipe subject | Focus causes zero events; each explicit activation/swipe emits exactly one correct ID. Delete-on-focus fails zero-event focus check; hidden-button fails ordinary/FKA discoverability. Record settings and actual key sequence. |
| 05 | tvOS: remote first/middle/last tiles, Select, repeated state updates; separately VoiceOver | Reach all tiles, correct one open event, stable focus and correct movie name. No-activation fails callback; reset-focus-on-update fails focus stability. |
| 06 | Native Toggle with VoiceOver and ordinary interaction, both directions | Label/state correct, backing binding changes. Broken-binding fails persistence; hidden-toggle fails VoiceOver traversal. No fix needed in candidate. |

SwiftUI callback/input tests and XCUITest targets remain to be implemented on the
Apple host. Do not count the three UIKit tests as coverage for cases 04–06. The two
mutations per case sample defects, not all acceptance conditions. Focus-triggered deletion and focus-reset traps require actual input and state-update checks; source inspection is not a mutation kill.
Package compilation does not satisfy `compile-host`; both platform app targets must
build. No receipt is emitted until source review and independent oracle review are
complete. Use `../acceptance.json` as the authority, allowing alternative valid fixes.

## Source review starting points

The candidate uses native controls rather than an invented named-action overload.
[Apple's named accessibility action](https://developer.apple.com/documentation/swiftui/view/accessibilityaction%28named%3A_%3A%29)
and [automatic font updates](https://developer.apple.com/documentation/uikit/uicontentsizecategoryadjusting/adjustsfontforcontentsizecategory)
were consulted during preparation (2026-11-05). This is not independent review,
SDK availability verification or proof of runtime behavior. Other per-case primary
source candidates remain in `../acceptance.json`.

Offline integrity: `node --test evals/runner/os26-fixtures-test.mjs` from repo root.

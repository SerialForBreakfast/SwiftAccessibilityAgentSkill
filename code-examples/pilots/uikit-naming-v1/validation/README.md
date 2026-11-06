# Revision1 Native Evidence

[Sanitized result records](revision-1.json) bind the exact manifest and original
private record/log hashes. All five checks met their declared outcomes on the first
native attempt. Eight distinct positive methods passed; three separate mutant
executions intentionally failed one selected method each.

| Check | Actual result | Contract result |
| --- | --- | --- |
| compile-naming | Compile success | Passed |
| naming-unit | Eight unit methods passed | Passed |
| exposeddecoration-negative | Decorative-element assertion failed | Passed expected-negative contract |
| hiddencontrols-negative | Container descendant-hidden assertion failed | Passed expected-negative contract |
| stalenames-negative | Reconfigured Open name remained Invoice A rather than Invoice B | Passed expected-negative contract |

Environment: Xcode27.0 build27A266a, Swift6.4, iPhoneSimulator SDK27.0 build24A430,
arm64, deployment26.0, actual iOS26.5 build23F77 for unit runs. Compile-only records
have no runtime. Dates in the UTC records are November6; local work date is November5.

This is configuration/callback evidence, not navigation, spoken-output, layout or
usability evidence. No runtime skill promotion, annual anchor approval, independent
review or model-baseline execution is implied. The draft paired question/rubric
still needs independent review. All inputs and intentional failed variants remain
available; no unexpected failure or repair iteration is hidden by this report.

Offline checks in `code-examples/tools/naming-contract.test.mjs` verify input hashes,
coverage/test identities, manifest binding and each declared result. Raw compiler,
xcresult and native process artifacts remain in the private immutable run directories.

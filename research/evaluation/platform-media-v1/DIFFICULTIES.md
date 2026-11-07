# Media difficulties and first attempts

## M01: Incorrect native-group permission assumption

Classification: test-oracle defect, not an Apple API defect or missing guidance
proven by an independent subject answer. First Mac compile passed; first positive
suite executed23 methods with 22 passing and one failing:
`MediaChoiceTests/testRequiredAudioGroupRefusesOff`.

The test assumed the fixture's audio group had allowsEmptySelection=false. It
actually reported true on the recorded Mac anchor. The example correctly honored
that permission, clearing selection; three assertions in the same test then failed.
The summary reports one failed method, not three independent failures.

Preserved originals:
- [First Mac test](incidents/macos-media-v1-first-Tests-MediaChoiceTests.swift.txt)
- [First Mac source](incidents/macos-media-v1-first-Sources-MediaChoice.swift.txt)
- [First Mac manifest](incidents/macos-media-v1-first-manifest.json.txt)
- Matching TV initial source/test/manifest are preserved but were not executed.
- Raw native log and xcresult retain all assertion diagnostics; public result
  summary reports the failed test and sanitized message.

Repair1, revision2: observe the native group's actual permission and assert the
corresponding result. Add a small application-policy seam to exercise disallowed
and allowed off requests deterministically without faking an AVFoundation object.
Add a mutant that bypasses the disallow guard. This keeps rejection behavior
covered rather than simply deleting a failing test. The native permission remains
source of truth; the injected seam is not evidence that a required audio group was
loaded from this fixture. No second repair was needed if revision2 passes; see results.

The developer question already asks for off only when allowed; it does not assert
all audio groups require selection. This is a controller-calibration finding.

## M02: Prompt-record generator syntax typo

Classification: local authoring-tool defect. A closing brace was used instead of
a closing bracket in a JavaScript array. The process failed to parse before it
wrote any prompt files. No native source, subject response or skill instruction
was affected.

- [Exact first generator](incidents/prompt-generator-original.mjs.txt)
- [Diagnostic reproduced before repair](incidents/prompt-generator-reproduced-diagnostic.txt)

The diagnostic file is a reproduction, not falsely labeled the original captured
stderr file. The first tool result reported the same SyntaxError. Corrected the
single delimiter and generated the six pairs. This is not an accessibility case.

## Deliberate negatives

Each platform challenges seven defects: inventing description tags, conflating
missing item and absent group, choosing forced-only subtitles, clearing a missing
language choice, ignoring a description requirement, substituting loaded for
seekable ranges, and bypassing off permission. They are intentional test controls,
not seven spontaneous model failures. Native evidence determines whether each
was actually rejected for its intended reason.

# Edited Documents and Rotor Ranges

UPAIR-05 candidate. Twelve positive unit methods cover native text ranges, literal
matches, Unicode boundaries, overlap choices, document updates and ordinary text
access. Five deliberate defects exercise sensitivity. No UI or VoiceOver automation.

## API Support and Matching Policy

[Custom rotors](https://developer.apple.com/documentation/uikit/uiaccessibilitycustomrotor)
provide a current item and direction. [Target ranges](https://developer.apple.com/documentation/uikit/uiaccessibilitycustomrotoritemresult/targetrange)
refer to text within a target such as UITextView. The installed header explicitly
describes nil current items/ranges for initial searches, despite the currentItem
property's nonnull annotation. The callback handles nil safely.

[Foundation search](https://developer.apple.com/documentation/foundation/nsstring/range(of:options:range:))
supplies literal UTF16 ranges; the fixture filters starts/ends against Swift Character
boundaries. This example's policy is exact literal matching with no case folding or
canonical normalization. It is not a general-purpose localized find implementation.
Foundation's installed comments recommend localized search APIs for general user
search; an application may choose that policy instead and test it separately.

The default match list is non-overlapping; an explicit option includes overlapping
whole-grapheme matches. Neither policy is asserted to be required by UIKit. A single
forward boundary cursor avoids repeatedly scanning from the beginning for overlaps.
No performance benchmark or unlimited-document-size claim is made.

## Edits and Retained Results

The owner calls `replace` whenever document/query inputs change. It rebuilds the
match list and rotor, invalidates old callbacks, and restarts the first search of
the new revision in the requested direction even if an old result is supplied.
Subsequent current items are interpreted by their full valid range in the current
document, not by object identity or stable annotation identity. A later coincident
range is a current positional cursor; this implementation does not track semantic
identities of annotations across edits.

Unannounced text changes cause the cached callback to return nil until refreshed.
Empty queries still update ordinary text but remove the custom rotor. This differs
deliberately from the older text pilot, which rejects empty queries without changing
its document. Both are explicit application policies; this example must not silently
replace the older contract. In-app content changes are programmatic here; no typing
or selection gesture is simulated.

The ordinary UITextView stays selectable and accessible. Tests apply a returned
range directly to selectedTextRange and inspect text; this establishes range
compatibility, not actual assistive-technology navigation or speech.

## Reproduce

```sh
node code-examples/tools/native.mjs plan \
  code-examples/pilots/uikit-edited-rotor-v1/manifest.json edited-rotor-unit
node code-examples/tools/native.mjs execute \
  code-examples/pilots/uikit-edited-rotor-v1/manifest.json edited-rotor-unit \
  /private/tmp/uikit-edited-rotor-new IOS26_SIMULATOR_UUID
```

Other check IDs: `compile-edited-rotor`, `characteroffsets-negative`,
`ignoredoverlap-negative`, `missingrestart-negative`, `oldrotor-negative`,
`staletext-negative`. Use fresh output directories.

See [source provenance](apple-sdk-sources.json), [coverage](coverage.json),
[mutations](MUTATIONS.md), [difficulties](DIFFICULTIES.md), and
[native evidence](validation/README.md). The [subject prompt](evaluation/prompt.json)
and [controller rubric](evaluation/controller.md) are separate development drafts
pending independent review; no skill promotion or model evaluation is implied.

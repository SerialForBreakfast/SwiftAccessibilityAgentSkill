# UIKit/tvOS structure and validation companion

Candidate repository guidance, not an installed skill update. SDK, deployment
target and actual simulator runtime are recorded separately.

Form examples preserve typed input and ordinary Save. A pure injected validator
supplies nonempty localized errors or nil. Visible errors are accompanied by
transient field hints, cleared through editingChanged while restoring original
help. Guard disabled and reentrant submission; do not turn editing into saving.
Hints are supplemental metadata, not a guarantee that an error will be spoken.

Keep shelf headings and native buttons independently represented. Use explicit
container/child ordering where appropriate, section-qualified item identity, and
validate duplicates before replacing hierarchy. Retained callbacks need current
generation, enabled state and hierarchy ownership. Preserve unrelated traits.
Stored ordering and actions do not establish directional-focus or spoken traversal.

Load TelevisionForm or TelevisionShelves source only for that task; tests on
demand. These examples intentionally omit full production layout/controller code.

Source: [accessibility containers](https://developer.apple.com/documentation/uikit/uiaccessibilitycontainer).

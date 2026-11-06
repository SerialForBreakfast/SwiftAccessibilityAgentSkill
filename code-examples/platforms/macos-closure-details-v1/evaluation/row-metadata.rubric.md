# AppKit/macOS: row-metadata

Draft, independent review pending; development case, not holdout.

Assert explicit row role and selected/expanded getters, current title and child button name, preserved independent action, reuse clearing and disabled behavior. Do not infer roles merely from class names. Accept equivalent NSAccessibility property/override implementations. This custom row does not establish NSOutlineView virtualization or delivered speech.

Grade correctness, preservation, practical usefulness and unsupported certainty separately. Invented APIs and hidden ordinary actions are critical. Accept alternatives; no exact helper names or English strings required.

[Source claims and negative controls](../manifest.json), claim row. [Source](../Sources/DesktopRow.swift); [tests](../Tests/DesktopContractTests.swift).

- `DesktopContractTests/testExplicitRowRoleAndChildSemantics`
- `DesktopContractTests/testReconfigureClearsSelectionExpansionAndNames`
- `DesktopContractTests/testOrdinaryRowActionUsesCurrentIdentity`
- `DesktopContractTests/testDisabledRowActionDoesNotChoose`

No subject outputs yet. Rubric and solution stay outside subject inputs.

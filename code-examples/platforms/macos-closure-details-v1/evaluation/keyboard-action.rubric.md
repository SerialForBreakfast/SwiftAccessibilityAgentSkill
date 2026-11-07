# AppKit/macOS: keyboard-action

Draft, independent review pending; development case, not holdout.

Check the direct keyDown route, not only a helper called by it. Verify Space and Return transition state, accessibility press shares that state, and disabled key events do not invoke callbacks. Accept equivalent conventional key handling. Direct NSEvent method calls do not prove event-loop delivery, traversal, or VoiceOver behavior.

Grade correctness, preservation, practical usefulness and unsupported certainty separately. Invented APIs and hidden ordinary actions are critical. Accept alternatives; no exact helper names or English strings required.

[Source claims and negative controls](../manifest.json), claim keyboard. [Source](../Sources/StateContracts.swift); [tests](../Tests/DesktopContractTests.swift).

- `DesktopContractTests/testSpaceEventUsesOrdinaryToggleTransition`
- `DesktopContractTests/testReturnEventUsesSameTransitionAsAccessibilityPress`
- `DesktopContractTests/testDisabledKeyboardEventCannotToggle`

No subject outputs yet. Rubric and solution stay outside subject inputs.

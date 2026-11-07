# SwiftUI bounded coverage ledger

All15 guideline rules and217 implementation/refinement/test/do-dont requirements have dispositions. [Machine ledger](clause-ledger.json) binds source hashes, platform-specific prompts, narrow assertions and matching native receipts. Author mapping is not independent acceptance.

| Disposition | Requirements |
| --- | ---: |
| compile-checkable | 80 |
| documentation-supported-outside-unit-scope | 101 |
| unresolved | 28 |
| directly-unit-testable | 8 |

A directly-unit-testable classification refers to the named application-state portion only. Compile-checkable does not mean the complete prose claim is proven. No private view introspection, reflection or UI automation is used. Some guidelines were authored for iOS/iPadOS; cross-platform use relies on explicit native compilation, not silently expanded source scope.

## Remaining boundaries
- generated-semantics [outside-unit-scope]: Generated SwiftUI accessibility tree, speech, rendered layout and delivered focus remain documentation-supported, not unit assertions.
- hosting-boundaries [unresolved]: Broader mixed-container semantics and automatic hosting update propagation are not established by direct button-coordinator calls.
- media-application [unresolved]: Synthetic option choices do not apply AVMediaSelection or extract actual stream metadata; existing AVFoundation evidence stays separate.
- review [pending]: Independent review of requirement mappings and alternative-aware rubrics; no worker assignment or message has been sent.

Shared algorithms run on three platforms are repetitions, not independent behaviors. Earlier UIKit/AppKit archives, released runtime guidance, frozen baselines and model evaluation cases remain unchanged.

# Q082-B controller qualification

On macOS 27.0 (26A428), Xcode 27.0, deployment target macOS 26, the same two XCTest methods ran once against each implementation. The injected callback accepts the fallback so that an extra request changes the observable result.

| Implementation | Primary accepts: requests / result | Primary declines: requests / result | Rejection check |
|---|---|---|---|
| Sealed reference | primary / true | primary / false | Pass |
| Alternative: first eligible candidate from an ordered list | primary / true | primary / false | Pass |
| Sealed deliberate defect | primary / true | primary, fallback / true | Failed on both assertions as intended |

[First-result receipts](first-results.json) pin the sources, identical test bytes, first logs and environment. Raw logs are private in `evals/results/1594-q082b-qualification/`. The [controller XCTest](RejectionTests.swift) observes requests made by the real finish method, not delivered focus. This is grader evidence, not a model comparison. The prior packet and its instructions are retained as sealed; use this record alongside them.

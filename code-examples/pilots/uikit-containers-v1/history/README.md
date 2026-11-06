# Container pilot revision history

Revision1 compiled and all13 positive tests passed. The wrong-span and stale-modal
mutants produced the intended assertion failures. The ignored-enabled mutant
invoked the forbidden callback, but its inline `XCTFail` was summarized by XCTest
as `failed - Disabled control invoked callback`. The adapter accepts explicit
`XCTAssert...` failures only, so it correctly classified this record as an error
rather than awarding a successful negative check.

Revision2 changes only the disabled-control test: record callback invocations and
assert that the count remains zero, alongside the existing false-return assertion.
Production source, mutations, expected test IDs and adapter safeguards are unchanged.
The complete original input set is retained under [revision-1](revision-1/).
Native revision1 evidence is preserved separately from the new run.

This was a test/adapter representation mismatch, not an observed Apple API defect.

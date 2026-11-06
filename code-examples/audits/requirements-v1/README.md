# UIKit Clause-Level Audit

Status: in progress, author review only. This audit supplements, rather than edits,
the historical pinned coverage ledger and completion audit.

[inventory.json](inventory.json) preserves the exact Rule text and 209 bullets from
the implementation, testing and do/don't sections of all fifteen current UIKit
guidelines. File hashes and line locators make omissions and later changes visible.
These are source clauses, not 209 tests or a coverage percentage. The inventory
does not automatically qualify appended OS27 guidance or linked documents.

Each clause starts pending. A reviewed disposition must distinguish a directly
asserted code contract, partial coverage, a remaining gap, framework scope deferred
by the UIKit-first decision, or behavior outside unit evidence. A reference in a
coverage file alone does not establish that the actual assertion proves the clause.

[U-015 review](U-015-REVIEW.md) is the first detailed pass. Its identified speed-control gap
now has separate UPAIR-06C evidence rather than relabeled diagnostic tests.
The remaining fourteen guideline clause reviews are still pending. UPAIR-08 is not
complete and no runtime skill or frozen evaluation fixture is changed.

## Next Work

1. Independently review the new ordinary speed-control example, its metadata, bounded
   state/action behavior and separate draft prompt/rubric. Preserve valid native
   semantics; do not invent a missing native accessibility value from a nil getter.
2. Review the remaining clauses against actual source/test assertions and native
   manifest-bound evidence, not method names alone.
3. Record applicable scope boundaries and remaining gaps; keep shared SwiftUI/host
   integration separate from UIKit-only coverage.
4. Complete the API-member declaration matrix in the parallel availability audit.
5. Obtain independent review before claiming inventory closure or gold readiness.

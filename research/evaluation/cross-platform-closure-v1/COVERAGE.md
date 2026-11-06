# Cross-platform coverage accounting

36 guideline rules and 507 clauses frozen in [inventory](inventory.json). [Ledger](clause-ledger.json) links scoped named assertions and matching native receipt hashes. This is an author mapping, not independent acceptance or 100% behavioral coverage.

| Disposition | Clauses |
| --- | ---: |
| partially-covered | 271 |
| covered | 22 |
| swiftui-deferred | 103 |
| documentation-supported/outside-unit-scope | 108 |
| version-deferred | 3 |

Historical iOS209 dispositions remain unchanged and reference the original ledger. Supplemental iOS async tests are additive, not duplicate coverage credit. Mac and TV bindings separate native metadata/callback contracts from delivered speech/focus. SwiftUI and TV27 stay deferred. Historical manual/UI-testing prose is recorded as outside this unit-only campaign, not imposed as a gate.

## Contract closeout and remaining work
- row-role [validated-unit-contract]: Assert explicit AppKit row/item role and selection/expansion metadata rather than infer from NSOutlineView class.
- keyboard-event [validated-unit-contract]: Synthetic NSEvent Space/Return/disabled cases directly invoke keyDown and compare its state transition with accessibility press; event-loop delivery is not claimed.
- api-matrix [unresolved]: Existing iOS member matrix retained; new source declarations document rotor platform traps, but a complete member-level AppKit/tvOS introduction/deprecation inventory is not yet claimed.

Native execution, API declaration inventory and independent prompt/oracle review are separate. The ledger does not establish universal behavioral coverage; unresolved work remains explicitly listed.

# Validate the claimed contract

Use for test design, disputed results or verification requests.

Separate compile errors, assertion failures, invalid mutants and infrastructure
failures. Inspect diagnostics before repair; preserve original inputs/outcomes.
A mutant must alter the active platform branch and fail its intended assertion.
A build failure or unchanged branch is not a successful rejection.

Test both state directions and real ordinary/custom entry points. Keep owners alive
when asserting callbacks, so deallocation cannot make a guard test pass accidentally.
For weak-lifetime tests, account for framework allocation/autorelease boundaries;
compare a native-only control before attributing retention to the coordinator.

Pure policy tests prove policy. Coordinator/getter tests prove those calls, not
automatic hosting or generated SwiftUI semantics. Environment composition is not
rendered scaling; focus state/notification requests are not delivered focus/speech.
Accept equivalent valid implementations and keep observations version-scoped.

Offer focused compile/unit checks without making manual walkthroughs or UI tests a
prerequisite for ordinary fixes. Execution still follows host/user permissions.

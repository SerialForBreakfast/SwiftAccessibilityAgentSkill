# Media Operation Ownership

Every option callback, including Off or another nil-valued request, must belong to
the item and displayed option snapshot that created it. Qualifying non-nil option
IDs alone does not prevent a stale Off callback from changing a newer selection.
Accept any ownership mechanism that rejects stale operations without resetting
valid choices. Old successes, errors and duplicate replies cannot own newer work.

Task cancellation is cooperative. Reject cancelled results when they return; if
the product requires immediate state invalidation, invoke explicit owner cleanup
or use an equivalent cancellation-aware design. Do not describe a post-return check
as immediate cleanup of a suspended non-cooperating loader.

State how item replacement triggers reload or invalidation. An identity getter
does not observe native changes automatically. A view task keyed only by a reload
counter may also miss replacement of the supplied store. Keep example mechanics
optional; do not require this repository's ticket type or state architecture.

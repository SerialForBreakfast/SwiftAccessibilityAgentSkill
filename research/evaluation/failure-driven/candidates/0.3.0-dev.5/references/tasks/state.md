# Current metadata and callback ownership

Update both directions on the same instance, not only during reuse. Clear obsolete optional help/value overrides so current visible text can be exposed. Preserve unrelated trait bits. Tie asynchronous results to the active request AND relevant item/input identity. Check actual current AVPlayerItem, not just captured identity. Consume completion ownership before external callbacks; allow reentrancy and reject late/duplicate completion according to the task. Preserve raw input unless normalization is requested.

Use only for this concern. Apply Apple source/SDK contracts to the actual target; examples and application policies are not universal platform guarantees.

A stale callback check must cover the current object and request, including same-ID replacement when relevant. Treat loading, absent, empty and failed metadata according to the application contract, rather than silently collapsing them.

# Parser-fixed probe outcome

The owner approved one parser-fixed probe followed by all 12 scored sessions only if qualification passed, with unchanged limits. This allowed 13 remaining reservations and 16 cumulative reservations including the three preserved earlier attempts. The new probe consumed one reservation; four cumulative reservations are consumed and all 12 scored cells remain unattempted.

The parser fix passed 16 offline tests. Fresh subscription readiness passed using the existing extra-usage-off attestation without extending its expiry. The previous grant was retired without refund.

The synthetic native skill successfully loaded, its inside fixture was read, and the outside synthetic read returned a real permission error. The sentinel content did not appear in captured context. The client then finished successfully but reported **five turns**, matching five assistant-message events, despite the explicit `--max-turns 4` argument. The harness rejected this result and stopped before scored work. This is a turn-limit qualification failure, not an accessibility-skill quality result. No retry or fallback ran.

The final usage receipt reports **16,634 tokens**: 6 input, 712 cache creation, 15,447 cache read and 469 output. Prior three attempts lack final usage receipts, so aggregate usage is unknown. Model telemetry names only `claude-haiku-5-5`. The rounded subscription windows remained 24% five-hour and 18% weekly; these readings do not establish an exact quota debit or a monetary charge.

Exact commands, settings, questions, raw events, original finish receipt, parser rejection, attempted/unattempted accounting, alternative-aware controller and pinned workspace snapshots are retained privately. Original failed executors and receipts remain unchanged. Full internal provider requests and complete native tool definitions are not exposed. No answer-quality grading, native answer execution, release changes or Git publication occurred.

Skill registration and synthetic loading are demonstrated in this narrow setup. Actual accessibility-skill loading, announcements, reference retrieval and task-quality lift remain unmeasured because the scored cells did not run. Turn-limit enforcement needs a separately qualified plan before further inference.

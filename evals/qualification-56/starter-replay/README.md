# Starter-interface proof replay

Controller-only comparison for the eight v6 trial-1 proofs marked control-api-mismatch in the 29-question audit. The originals target two interfaces (PresentationState and CaptionState plus their views); the calibrated controls instead expose SheetOwner and MediaSelectionStore. A missing type does not mean the submitted test is wrong.

The adapter is an overlay on the qualified reference, alternative and mutant cores, not a change to their archived sources. Sheet callbacks installed on the modifier use SheetOwner. Direct calls to dismissed(ticket) use the starter state helper: they must not be credited as exercising a modifier's delivery. Real caption loads and selection go through the player-item store; the starter's injected string loader exercises a separate state path. A test that kills an ownership mutant on injected strings is evidence about that path only, not a native caption selection. Case-specific method spellings forward to these paths.

## Reproduce

On the evidence host, from the repository root, with the existing Apple test destinations booted, the frozen private trial1 intake, Ruby xcodeproj and Xcode available:

    python3 -B evals/qualification-56/starter-replay/run.py

To replay a subset after a harness repair, append exact four-character question prefixes. Each invocation writes a new private directory under evals/results/starter-eight-*. The runner checks the preserved proof hash against its original intake, copies it verbatim into each test target and verifies the copy. Its input is the original **staged proof** (which may already include the historical import/test-discovery wrapper), not a newly extracted or rewritten answer. Resource-dependent tests receive the qualified local multitrack fixture in their requested bundle. Network-URL proofs are only built for testing; no model, remote media or UI runs are required.

The three variants are run independently so rejection of a valid reference or failure to compile does not suppress the alternative or mutant diagnostics. An assertion failure on both reference and mutant is not a kill. Inspect individual tests and the compiler log before interpreting any suite result. No submitted proof is repaired. The private native archives and first failures stay outside the distributed skill. Public receipts contain proof hashes, test names, result statuses and log hashes, not proof bodies.

Reconcile first and subsequent attempts in chronological order:

    python3 -B evals/qualification-56/starter-replay/report.py starter-eight-FIRST starter-eight-REPAIR

[Recorded outcomes](RESULTS.md)

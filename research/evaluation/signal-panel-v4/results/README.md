# Signal-v4: better primary answers, no whole-task gain

**Decision: retain as research; do not promote.** BigDog returned 112 first answers and 112 source grades for 56 matched developer questions. The worker ledger reports zero incremental spend. V4 rescued five whole answers and lost five; nine passed both ways and 37 failed both ways. One new ordinary-action loss blocks promotion independently of that tie.

| Source-graded measure | Installed v2 | Installed v4 | Paired gains / losses |
|---|---:|---:|---:|
| Primary behavior | 28 | 35 | 12 / 5 |
| Integration | 29 | 33 | 9 / 5 |
| Ordinary behavior preserved | 45 | 42 | 1 / 4 |
| Requested verification | 13 | 13 | 5 / 5 |
| No unnecessary rework | 42 | 44 | 8 / 6 |
| Whole answer | 14 | 14 | 5 / 5 |

Both arms had 46 scored verification cases (ten not applicable). Among 35 v4 primary passes, 21 did not pass the whole task. Verification failed in 17 of those 21; in 13 it was the only failing component. These are grade-defined opportunities, not 13 demonstrated code fixes. Two concrete examples: both iOS and tvOS caption-write answers gained primary credit, but neither submitted check established the actual item selection before and after the installed picker changed it.

**Whole gains:** originating-window ownership, preserving the existing reduced-motion behavior, supplied-size font scaling, one retained wrapper target and one stale-action case. **Whole losses:** clearing optional help, saved vs native selection, edit-action category, refusing focus target and a different stale-action case. The last family contains both a gain and a loss; do not teach a uniform fix from either example. Across iOS and tvOS SwiftUI the primary grade improved on seven pairs without a primary loss; this did not generalize to AppKit (one primary gain, two losses).

**Critical playback case:** Both answers missed the chapter contract. V4 correctly stops advancing after the final chapter but moves by a fixed interval when no chapter exists. More importantly, its only play-toggle call in the proposed control is an accessibility action. The ordinary zero-distance drag handler seeks, with no ordinary play toggle. V2 at least wires an ordinary tap to play as well as a drag. This is a source-level loss, not a demonstration that v2's gestures arbitrate correctly on device. V2 and v4 each had six critical flags: five shared, one resolved, one new. Identical counts conceal the blocker.

**Discovery and cost:** body reads rose from 40 to 55 of 56, reference reads from 36 to 51. Reported total tokens rose from 610,320 to 957,091 (+56.8%). No inference that routing caused either the gains or the extra usage. V4 read the relevant guidance on the chapter, responder, media-write and edit-category misses. Strengthening discovery alone is unlikely to resolve them.

**Next offline tranche:** adjudicate the union of the 13 verification-only misses, five whole regressions and new critical case. For compatible answers replay the submitted implementation and its proof unchanged, independently; preserve the first diagnostics, qualify the oracle on a valid alternative and a relevant mutant, and record interface or fixture gaps separately. Prioritize chapter endpoints and ordinary activation, native media readback, attached responder eligibility versus a rejected request, and the SDK edit-category symbol. Retain the five new whole passes as contrasts. Distill candidate guidance only where those observations warrant it; no new live comparison yet.

[All 56 paired results](PAIRS.md). Run `python3 -B analyze.py --check` on the evidence host. Return SHA-256: `f14305f1ff84de8bd03a79752e70e15e51b0fe8e5f70008b3be855a8bfb7ff09`. The sealed checker verified scheduled cells, artifacts and quoted spans. The local audit also matched original developer bytes to every recorded CLI argument and grader question, answer digests to receipts, grade mappings to outputs, and read-trace payloads to hashes. Those checks do not independently establish semantic correctness. The comparison is against installed v2, not an unaided model or the released skill; one answer per arm on inspected development cases provides no transfer or per-rule causal estimate.

# Did the new skill produce better answers?

**Whole-answer score: tied.** Same 56 development questions, one first answer per version and question. These are the original source grades, not compile counts.

| What passed | Before: signal-v2 | After: signal-v4 | Net passes | Fixed | Regressed |
|---|---:|---:|---:|---:|---:|
| Whole developer task | 14/56 | 14/56 | +0 | 5 | 5 |
| Primary behavior | 28/56 | 35/56 | +7 | 12 | 5 |
| Integrated with the supplied code | 29/56 | 33/56 | +4 | 9 | 5 |
| Preserved ordinary actions and behavior | 45/56 | 42/56 | -3 | 1 | 4 |
| Supplied requested verification | 13/46 | 13/46 | +0 | 5 | 5 |
| Avoided unnecessary changes | 42/56 | 44/56 | +2 | 8 | 6 |

Fixed = failed before, passed after. Regressed = passed before, failed after. Ten questions did not require verification.

| Whole-task passes by platform | Before: signal-v2 | After: signal-v4 | Net passes | Fixed | Regressed |
|---|---:|---:|---:|---:|---:|
| iOS | 5/26 | 5/26 | +0 | 2 | 2 |
| macOS | 4/14 | 4/14 | +0 | 2 | 2 |
| tvOS | 5/16 | 5/16 | +0 | 1 | 1 |

**Promotion: keep 0.2.2.** The measured comparison is between two research versions. The v4 chapter answer lost ordinary tap-to-play. Released 0.2.2 and the newest candidate, signal-v5, have not been scored head-to-head on this panel; their difference is unknown.

[All 56 before/after grades](../../research/evaluation/signal-panel-v4/results/PAIRS.md) | [Offline replay and grading coverage](REPLAY.md)

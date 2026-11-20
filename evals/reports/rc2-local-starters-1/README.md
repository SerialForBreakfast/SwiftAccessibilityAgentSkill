# Request 1531: 0.2.2 vs rc.2 on eight revised starters

AGY Gemini 3.8 Flash Low produced one first answer per installed skill on each of eight sealed starter questions, with explicit invocation, in fresh sessions ([sealed handoff](../../rc2-starter-comparison/HANDOFF.md), outer seal `11a37ea6…`). BigDog's consolidated return (receipts 1533 and 1534, SHA-256 `b11daec5…`) holds 16 answers, no errors and no retries. All 318 indexed members verified. Cell 1 ran on AGY 1.5.5 before a background update to 1.5.8; the other 15 cells used a hash-verified read-only 1.5.5 executable.

One reviewer graded the 16 condition-masked answers against `controller/rubrics.json`, the question and the supplied starter, then froze the grades (`751732f5…`) before opening the arm join. No submitted code was built or run, so every verdict is a source judgment. A requirement the question names explicitly needed a matching test to pass the whole task; rubric-only details were judged on the code.

| Measure | 0.2.2 passes | rc.2 passes | Gains | Regressions | Both pass | Both fail |
|---|---:|---:|---:|---:|---:|---:|
| Primary behavior | 4 | 6 | 3 | 1 | 3 | 1 |
| Ordinary behavior preserved | 6 | 6 | 1 | 1 | 5 | 1 |
| Integration into the screen | 4 | 7 | 3 | 0 | 4 | 1 |
| Requested proof | 3 | 4 | 1 | 0 | 3 | 4 |
| Whole answer | 3 | 4 | 1 | 0 | 3 | 4 |

| Case | Platform | Whole-task outcome |
|---|---|---|
| 4840, delayed sheet dismissal | macOS | Both pass |
| da78, delayed sheet dismissal with generation guard | macOS | Both pass |
| 6d2d, connect captions to the item | iOS | Both pass |
| 5d12, connect captions to the item | tvOS | **rc.2 gain**: the 0.2.2 picker still bound only the local value, and its full-track count rejects working code |
| 4ec9, picker states and retry | iOS | Both fail. Primary regression: rc.2 conflated a missing item with empty options and keyed options by language, colliding forced and full English |
| c04c, stale callbacks after reload | iOS | Both fail. rc.2 owns item and request correctly but never tests same-item reload; 0.2.2 lets an old Off clear the new item |
| c6b2, stale callbacks after reload | tvOS | Both fail. Neither binds the picker's selection to its item; rc.2's stale-Off test fabricates a request ID |
| f483, retained binding after replacement | macOS | Both fail. rc.2 owns the binding correctly, but its tests call a fixture API that does not exist and its new view drops the video player (the one preservation regression) |

**What this shows:** both versions handle delayed dismissal. The remaining failure is ownership of selection callbacks: most answers guard late load results but not the retained picker binding, so an old Off still reaches the new item. Fix that before measuring another caption candidate.

Every session read the installed skill body. rc.2 sessions read its media card on all six caption cases and its return card on both sheet cases; 0.2.2 sessions read G-015 and the modal guidelines. Reported tokens were 279,726 for 0.2.2 and 215,901 for rc.2 (22.8% fewer).

**Limits:** one generation per cell, one grader, no native build. Six of the eight questions share one caption starter, and these are revised development cases, not holdouts. This does not justify promoting rc.2. Per-answer grades, the arm join and raw answers stay in the private results folder.

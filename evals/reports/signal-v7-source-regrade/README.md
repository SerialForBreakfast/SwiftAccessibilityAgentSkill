# Requests 1510 and 1511: signal-v7 and signal-v7.1 against signal-v6 trial 1

AGY Gemini 3.8 Flash Low produced one first answer per cell on the 56 signal-panel questions, with no retries. Request 1510 ran signal-v7 and request 1511 ran signal-v7.1 (receipts 1683 and 1684). Both ran on a pinned AGY 1.5.5 client because 1.5.3, the client for the signal-v6 trial-1 answers from request 1507 and its continuation, is no longer installed. Each new run answered 56/56, and 55 of 56 cells in each opened `SKILL.md`.

One reviewer graded all 168 answers in a single blind pass. Each question showed its three answers under random tokens, in random order, with skill names, versions and reference paths masked (input freeze `1d9aabc5…`). Grading used the frozen panel criteria, the case-specific criterion and the source contract. Grades were frozen (`a596cb52…`) before the arm map was opened. No submitted code was built or run, so this is a **source-only regrade, not the 1507 board**. Ten questions require no added proof, so verification is not applicable on them.

| Measure (of 56) | v6 trial 1 | signal-v7 | signal-v7.1 |
|---|---:|---:|---:|
| Primary behavior | 32 | 47 | 50 |
| Ordinary behavior preserved | 55 | 55 | 54 |
| Integration into the screen | 43 | 49 | 51 |
| Requested proof (of 46) | 15 | 28 | 28 |
| No unneeded rework | 50 | 56 | 56 |
| **Whole answer** | **16** | **37** | **36** |
| Reported tokens | 998,983 | 766,343 | 714,175 |

| Whole-answer pair (same questions) | Gains | Losses | Exact two-sided sign test |
|---|---:|---:|---:|
| signal-v7 vs v6 trial 1 | 21 | 0 | p = 9.5 × 10⁻⁷ |
| signal-v7.1 vs v6 trial 1 | 22 | 2 | p = 3.6 × 10⁻⁵ |
| signal-v7.1 vs signal-v7 | 6 | 7 | p = 1.0 |

Compared with v6 trial 1, most gains come from the primary behavior (16 and 18 questions gained) and the requested proof (13 and 14). signal-v7.1 lost two whole answers to v6 trial 1. In P-d2dd979143402b3b, its sheet-dismissal fix was correct, but it never tested a cancelled dismissal, which the criterion requires. In P-ddf8bad3cbd8d087, its row is a single accessibility element, which hides the ordinary Open and Delete buttons from VoiceOver.

| Platform and framework | Questions | v6 trial 1 | signal-v7 | signal-v7.1 |
|---|---:|---:|---:|---:|
| iOS UIKit | 13 | 7 | 12 | 9 |
| iOS SwiftUI | 13 | 2 | 7 | 8 |
| macOS AppKit | 8 | 1 | 6 | 5 |
| macOS SwiftUI | 6 | 2 | 3 | 3 |
| tvOS UIKit | 9 | 4 | 5 | 8 |
| tvOS SwiftUI | 7 | 0 | 4 | 3 |

**Shared failures.** All three arms failed 13 questions. The recurring causes:

- **Sheet dismissal:** work completes before the sheet is dismissed, or `onDismiss` reads a ticket or presented value that has already changed.
- **Unreachable or self-confirming tests:** tests that compile to an unconditional skip on tvOS, or tests that exercise only a mock.
- **Incomplete exposure checks:** twin row-exposure checks that omit role, selection, expansion or the child's contextual label.
- **Same-item reload not tested:** caption-binding tests that cover replacement by a different item but never a retained setter across a same-item reload.

The remaining weakness is mostly proof (28 of 46 in both new arms), not primary behavior.

**What this shows:** both signal-v7 and signal-v7.1 clearly beat v6 trial 1 on the same questions and use fewer tokens. This panel cannot separate signal-v7 from signal-v7.1.

**Limits:**
- One generation per cell, with a different client version from the v6 answers.
- One grader saw the three answers to a question side by side, so the scores are paired within a question, not independent absolute grades.
- One grade was amended before the freeze: an integration fail was changed to pass.
- Several verdicts are recorded judgment calls, such as a test of a gesture conflict and a compile error read from source.
- No native build, unit execution or mutation check.
- These are known development questions, not holdouts.

This does not justify promotion. Per-answer grades, the mask map, the arm join and raw answers stay in the private results folder.

# Discovery 500: where to spend the next improvement cycle

**Finding:** prioritize tracing the actual write or callback, and fix the review questions before optimizing for their merge verdicts. A model that rejects every patch would match every deliberately regressive patch here. A skill that persuades it to accept every nominal fix would reward several bad questions.

## Evidence and limits

Request 1543, return 1562. The [replayable verifier](audit.py) checks the outer digest, all 5,014 indexed members, original controller and subjects, and each of 500 sent prompt arguments, raw answers, receipts and masked copies. It sums 1,715,128 reported tokens. BigDog reports no errors, retries or incremental spend. The CLI request and returned model label are available; an immutable server revision is not. The answers are frozen, not a frozen set of 500 grades.

**Quota timing:** the historical handoff specified November 14, 2026 Pacific, after reset. Reservations actually ran November 13, 14:35 to 16:51 Pacific. That differs from the written handoff, not from the owner's preference to use expiring subscription capacity. Future handoffs should prioritize already-authorized work before reset, within scope and at zero extra spend. Check remaining capacity and the live reset window; a reset is not authorization for more attempts. The two meter windows changed during this run, so the final readings are not today's available balance.

The [500-row index](index.csv) binds each prompt to the exact answer digest without publishing private answer text. This pass read recommendation directions on all 150 code and patch reviews. A conditional yes counts as yes; refusing as written counts as no. Agreement measures **direction only**, not the rationale, build, preservation or complete task. The other 350 are indexed but not adjudicated. The code-review sentence in some questions describes an incident without specifying the desired outcome; the controller's interpretation cannot fill a missing product policy.

| Original key | Agreed | Disagreed |
|---|---:|---:|
| Merge scoped patch | 19 | 16 |
| Reject regression | 35 | 0 |
| Leave working code alone | 8 | 8 |
| Repair supplied code | 59 | 5 |

## Decisions worth fixing in the skill

Short IDs below are unique prefixes after Q- in the index. These findings are source-level observations, not native runs.

| Case | What went wrong | Minimal intervention and control |
|---|---|---|
| tvOS UIKit 4cba9a | The answer assumes reparenting invalidates a generation. The installed closure checks generation and enabled state, not shelf membership. Moving the button alone never calls the reconfiguration that increments generation. An obsolete callback can still select an item. | Trace what *actually invalidates* a retained action. Move the enabled button without refreshing; old action must do nothing and a current ordinary button must still work. |
| macOS SwiftUI ed6bfe | The answer explicitly approves a retained Off setter changing a refreshed store. The getter checks its captured generation; the setter calls the current choose method without that check. A stale control can clear the viewer's new caption choice. | Trace reads and writes independently. Refresh the same item, invoke old Off, then current Off. Distinguish observed code behavior from whether that behavior is desirable; state the freshness requirement in the next question. |
| iOS UIKit 8f57f0 | The answer concludes stream classification stays unknown; the supplied initializer explicitly writes live when duration is indefinite. A developer following the answer would ship a misleading status. | Follow the assigned value, not the parameter default. Contrast indefinite duration with unknown kind against explicit live classification. Do not add a blanket rule that every indefinite item is on demand. |

One shared card hypothesis covers the first two: **at the moment of an action, which owner can still change state, and what event invalidated that authority?** It must also preserve d7e858, where the actual media callback already checks its ticket. The third finding needs a narrower media distinction, not an additional general instruction for every Swift answer.

## Triage of the remaining recommendation disagreements

Do not score these as technical failures solely from the verdict. This accounts for the other 26 flagged cells:

| IDs | Finding | Next action |
|---|---|---|
| 621091, a952e1, d7e858 | The supposed working brand-font example uses a system font. The supposed working dismissal callback reads shared ticket state. The supposed broken media reload mutates the unrelated form validator; the actual media completion still checks its ticket. | Correct starter/key alignment first. Preserve the answers that noticed these distinctions as calibration examples. |
| f7c5db, 07bdae, bda2cc, f910d2 | Buffer signal vs Ready UI, dismissal permission vs reentrant restoration, flat IDs vs tree branches, Save/Open report vs Play/Details fixture. The supplied delta or names do not establish the user-facing claim. | Use the actual caller or narrow the question. Give partial credit for a correct scoped delta without claiming the incident is solved. |
| 306171, 2b0f5d, 533790, c3f116, 0fbf26 | Fallback language, missing-option selection, and whether a duplicate write is an event or a state change are product choices. | State the policy when it determines the answer. Include both policies as contrasting controls; never teach a universal fallback. |
| 546009, 7d23bd, ab584c, ca72b7 | Review objections depend on spoken redundancy, hypothetical siblings, what an animation closure owns, or whether a selected parent obscures a child. | Grade the visible delta independently. Ask for missing context only where it changes the action; do not equate a hypothetical concern with a demonstrated regression. |
| c1c12f, d4c241, 4f5cce | Color conversion vs downstream transfer function, intended supported gamut, or metadata classification vs badge rendering. | Expose the consuming computation/view if testing end-to-end behavior. Otherwise grade the boundary value. |
| 196711, 1b9b2e, 48d186, 6663d6 | AppKit focus refusal, cleanup after a direct edit, and key-view link ownership depend on code beyond a predicate or one diff hunk. | Exercise an attached refusing target, a live field mutation, or an externally changed link. Separate eligibility from acceptance and owned cleanup from overwriting someone else's state. |
| bc0b67, 54e5f5, c2440a | Bridge update vs retired registration, text replacement vs native editor events, and live type size vs caller-supplied preview size. | Specify the retained callback, editing path or preference owner. A helper-only witness or a speculative rewrite cannot decide integration. |

## Efficient next batch

1. Qualify the three direct counterexamples and the three inverted/misaligned controls above as a single six-case calibration set. Use the existing native packages where the exact originals fit; retain non-binding answers as source judgments. Do not change historical grades.
2. For the remaining proof, acceptance and integrated-solution questions, bind each submitted witness to trigger, owner and observable before compiling. Reuse the [prior proof replay](../../proof-repair-20/replay/RESULTS.md) to prioritize direct text edits and attached-but-refusing focus targets. That is separate historical evidence, not results on these 500 answers.
3. Keep working controls in the permanent corpus. For an eventual metered comparison select representative controls with materially different boundaries, not every easy yes/no. Freeze eligibility and both rubrics before seeing skill answers. No fix rate, lost-action rate, or release recommendation follows from this unaided return.

Reproduce with Python 3: run `python3 -B evals/discovery-500/audit-1562/audit.py PATH_TO_RETURN_ZIP` from the repository root. The direction annotations are an analyst reading of the frozen outputs; replay checks their binding and reproducibility, not independent correctness.

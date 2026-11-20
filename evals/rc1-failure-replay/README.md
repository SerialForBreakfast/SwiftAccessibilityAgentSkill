# Explicit rc.1 replay of observed unaided Haiku failures

Executed on November 7, 2026. [Seven-session results](RESULTS.md). Each subject file in `inputs/` contains the established explicit native invocation followed by the exact archived user payload, including any serialized SYSTEM and USER text. The controller stores the original and new hashes, original grading criteria, and a receipt for each historical answer. Keep the controller outside the subject workspace.

| Prompt | Unaided Haiku material gaps / graded attempts |
| --- | ---: |
| GP26-03 · checkout layout with Pay appearance preserved | 4/4 |
| GP26-11 · review of an already-working Slider | 4/4 |
| IOS-MEDIA-OWNERSHIP-R1 · stale callbacks and cancellation | 1/1 |
| GP26-04 · deletion without swiping | 2/4 |
| GP26-02 · customer and status after cell reuse | 1/4 |
| EV02 · claims supported by an audit | 1/2 |
| EV06 · claims supported by a direct-handler test | 1/2 |

The denominator includes all graded unaided attempts for the exact text from the November 5 baseline, compact development comparison and November 6 native pilot. Repeated failures select a task only once. The media case has a single observation. A single earlier pass on each evidence question and three on cell reuse illustrate how an unaided model can recover on another attempt.

## Execution and interpretation

Use a fresh read-only native Haiku 5.5 session at low effort for each file, with the sole target plugin pinned by `controller.json`. Send the file contents verbatim as the user message. Use the existing native chat harness, capture the actual Skill result, successful reference reads, final announcement and answer separately. Grade all first answers, including failed activations. Keep cell-local errors in the denominator and continue the remaining cells. Preserve the original task rubric and accept equivalent implementations. Source review cannot establish native compilation, rendered layout or actual assistive interaction.

A historical replay can identify recoveries worth testing. Selection on a previous failure, sampling variation and differences between the earlier static baseline harness and native execution preclude attributing a recovery to rc.1 alone. For a causal comparison, pair the same seven prompts with fresh unaided sessions on the same harness. That would be a separate allocation.

Rebuild offline with `python3 -B evals/rc1-failure-replay/prepare.py` from the repository root on the machine holding the archived controls. Preparation is offline. The separately authorized run consumed all seven reservations.

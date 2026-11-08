# Two minimal additions on Gemini 3.8 Flash Low

| Approach | Whole task passed | Primary behavior met | Focused check met | Rework flagged | Tokens | Gains / regressions vs unaided |
|---|---:|---:|---:|---:|---:|---:|
| Unaided | 1/17 | 13/17 | 3/17 | 10 | 69,140 | — |
| Review sentence | 2/17 | 14/17 | 2/17 | 3 | 65,221 | 1 / 0 |
| UIKit text note | 1/17 | 13/17 | 1/17 | 11 | 65,562 | 0 / 0 |
| Both additions | 2/17 | 15/17 | 2/17 | 2 | 63,764 | 1 / 0 |

## What to carry forward

Keep the review sentence for an independent replication. With it, the selected-status answer earned the only new whole-task pass and unnecessary rework fell from ten answers to three. The sentence also helped on the primary captions behavior, but its button-reparent answer lost a primary pass.

Keep the UIKit text note out of the default instructions. All four conditions handled the broken range and both working variants correctly on primary behavior. Every condition missed the full request on all three. Adding the note to the sentence earned no further whole-task pass.

The next candidate to test is one instruction about verification: exercise the actual handler or returned value and assert the requested observable effect. Only eight of 68 answers met the focused-check criterion. Try this on untouched cases with the review sentence as the comparator before expanding the skill.

## UIKit text family and other tasks

| Approach | Text cases, whole | Text cases, primary | Other cases, whole |
|---|---:|---:|---:|
| Unaided | 0/3 | 3/3 | 1/14 |
| Review sentence | 0/3 | 3/3 | 2/14 |
| UIKit text note | 0/3 | 3/3 | 1/14 |
| Both additions | 0/3 | 3/3 | 2/14 |

## Individual first answers

P = pass, F = material failure and U = unresolved. Each cell shows whole answer followed by primary behavior. Individual reasons and answer excerpts are in the [scoring ledger](results.json).

| Question | Unaided | Review | Text | Both |
|---|---|---|---|---|
| reentry | F / P | F / P | F / P | F / P |
| dismiss-permission | F / P | F / P | F / P | F / P |
| button-removal | F / P | F / P | F / P | F / P |
| button-reparent | F / P | F / F | F / P | F / P |
| node-removal | F / P | F / P | F / P | F / P |
| node-replacement | P / P | P / P | P / P | P / P |
| current-order | F / P | F / P | F / P | F / P |
| chapter-boundaries | F / F | F / F | F / F | F / F |
| full-captions | F / F | F / P | F / F | F / P |
| selected-status | F / F | P / P | F / F | P / P |
| total-text | F / P | F / P | F / P | F / P |
| dismiss-owner | F / F | F / F | F / F | F / F |
| captured-action | F / P | F / P | F / P | F / P |
| description-tags | F / P | F / P | F / P | F / P |
| text-range-38 | F / P | F / P | F / P | F / P |
| text-range-46 | F / P | F / P | F / P | F / P |
| text-range-47 | F / P | F / P | F / P | F / P |

## Methods and limits

One first attempt per condition per revised development question. Requests were interleaved in balanced four-session sequences. Each quartet used identical developer-question bytes and the same neutral, tool-free agent. The only intervention was the assigned instruction text in the agent body. Successful calls were checked against AGY generation metadata for Flash Low and the actual presence or absence of both additions. There was no installed-skill routing.

One masked coordinator-delegated Codex reviewer graded each quartet against the sealed criterion, with arm order shuffled. Grades separate primary behavior, ordinary-behavior preservation, evidence quality and unnecessary rework. Whole-answer pass requires that the answer meets the request including the focused check; a behavioral design is sufficient for the chapter question. Reviewers assessed the source and proposed checks without compiling submissions or observing assistive technology. Each answer was sampled once. The three text cases share one family, and these selected questions were used during development.

The sessions used 263,687 reported tokens. Quota meters are rounded account-wide readings.

- Gemini Models · Weekly: 22% → 22% (same reset window).
- Gemini Models · 5-hour: 1% → 4% (same reset window).

[Calibration and original estimate](CALIBRATION.md) · [384-question unaided baseline](../FIRST-ITERATION.md)

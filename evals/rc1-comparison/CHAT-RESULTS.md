# Haiku chat comparison, November 7, 2026

Claude Haiku 5.5 at low effort returned 36 answers in a separate diagnostic cohort with revised prompts across 12 known Swift development tasks. The original source reviewer marked all 12 automatic answers per version as meeting the contract. Subsequent native grading found one shared failure. Explicit invocation exposed a difference in successful reference retrieval and visible reporting.

| Measured outcome | 0.2.2 | 0.3.0-rc.1 |
| --- | ---: | ---: |
| Automatic native contracts passed | 11/12 | 11/12 |
| Original automatic source passes | 12/12 | 12/12 |
| Automatic skill loads | 1/12 | 1/12 |
| Automatic sessions with a successful reference read | 0/12 | 1/12 |
| Explicit source contracts met | 3/3 | 3/3 |
| Explicit skill loads | 3/3 | 3/3 |
| Explicit sessions with a successful reference read | 0/3 | 3/3 |
| Explicit sessions with an announcement and routing line in the final answer | 0/3 | 3/3 |

The six fresh automatic repeats of 0.2.2 agreed with their first source verdicts on all six. The checkout-font task activated both versions on the first attempt and did not activate the release on its repeat. Every answer included formatting or prose beyond raw Swift. Format was graded separately.

## Checkout-font source review correction

The saved reviews for C01 (release), C02 (rc.1) and C25 (release repeat) all cited the explicit body scaling, wrapping, disabled shrinking and preserved text. They stopped at the font assignment and missed the effect of the next line enabling automatic adjustment. C02 and C25 submitted identical Swift. C01 only reordered the wrapping and shrinking statements.

The caller supplied accessibility-XL traits. The original unit compared the final label font to a font scaled for those traits. In Sillycon’s iOS 26.5 simulator observation, the off-window label’s own environment yielded 17 pt after automatic adjustment, while the caller’s setting required 37 pt. All three compiled. The source reviews incorrectly inferred final size from the intermediate assignment. The follow-up supplied-setting contract reproduced both distinct failures; a separate live-environment contract passed the same mechanism when the label was supposed to track its own traits.

Across all 36 diagnostic cells, native grading passed 33. All 36 answer blocks were extractable. The sealed job and the diagnostic cohort are recorded separately in [Sillycon’s intake](RESULT.md). See the [contrasting contracts and native scorecard](../headroom/checkout-font/README.md).

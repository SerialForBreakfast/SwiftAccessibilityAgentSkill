# Dev.5 and dev.7 on Gemini 3.8 Flash and Claude Haiku

The owner approved 48 first attempts per provider on the same 24 paired questions. Flash completed all 24 pairs. Haiku completed the first seven pairs before its quota display stopped returning a complete reading. Each arm received its own versioned instructions and inline context. The three revised dismissal questions were identical within each pair.

| Provider | Pairs | Dev.5 meets | Dev.7 meets | Gains | Regressions | Both meet | Both have gaps | Inconclusive |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| gemini-3.8-flash-low | 24 | 11 | 9 | 1 | 3 | 8 | 9 | 3 |
| claude-haiku-5-5 | 7 | 2 | 3 | 2 | 0 | 1 | 1 | 3 |

| Provider | Dev.5 reported tokens | Dev.7 reported tokens | Change |
| --- | ---: | ---: | ---: |
| gemini-3.8-flash-low | 109,300 | 100,829 | -7.8% |
| claude-haiku-5-5 | 60,446 | 50,172 | -17.0% |

All 62 completed answers included their correct version in the opening and a routing line. The references were supplied inline. Flash five-hour consumption displayed 8% at preflight, 10% at the grant opening and 11% at completion. Its weekly display stayed at 3%. Haiku displayed 0% five-hour use and weekly use moving from 18% to 19% through the last complete reading. Percentages are rounded account-wide observations. The final Haiku reading is unavailable.

Haiku stopped immediately after capturing its fourteenth successful first answer. The CLI quota display timed out and later exposed a rate-limit message. Its closed reservation record shows 14 used and 34 cancelled. Earlier local setup failures occurred before the first Haiku reservation. Flash consumed exactly 48 reservations. There were no repairs, replayed subjects, paid fallbacks or extra credits.

## Paired source findings

| Case | Flash dev.5 → dev.7 | Haiku dev.5 → dev.7 |
| --- | --- | --- |
| ios-uikit-actions | material-gap → material-gap | material-gap → meets |
| ios-uikit-state | material-gap → material-gap | material-gap → material-gap |
| ios-uikit-text | meets → material-gap | material-gap → not-assessable |
| ios-swiftui-semantics | meets → meets | meets → meets |
| ios-swiftui-lifecycle | material-gap → material-gap | material-gap → not-assessable |
| ios-swiftui-media | material-gap → material-gap | material-gap → meets |
| macos-appkit-actions | meets → material-gap | meets → not-assessable |
| macos-appkit-structure | material-gap → material-gap | Unattempted |
| macos-appkit-testing | material-gap → material-gap | Unattempted |
| macos-swiftui-state | material-gap → meets | Unattempted |
| macos-swiftui-text | not-assessable → not-assessable | Unattempted |
| macos-swiftui-lifecycle | not-assessable → material-gap | Unattempted |
| tvos-uikit-state | material-gap → material-gap | Unattempted |
| tvos-uikit-media | not-assessable → material-gap | Unattempted |
| tvos-uikit-lifecycle | meets → material-gap | Unattempted |
| tvos-swiftui-actions | meets → meets | Unattempted |
| tvos-swiftui-structure | meets → meets | Unattempted |
| tvos-swiftui-testing | material-gap → material-gap | Unattempted |
| ios-uikit-no-change | meets → meets | Unattempted |
| ios-swiftui-no-change | meets → meets | Unattempted |
| macos-appkit-no-change | meets → meets | Unattempted |
| mixed-macos-owner | material-gap → material-gap | Unattempted |
| ios-missing-reference | meets → meets | Unattempted |
| tvos-version-boundary | meets → meets | Unattempted |

## Critical flags

The reviewer flagged the following answers for a lost action or broken navigation. Each flag refers to the specific source answer. A gain or regression in the table counts the whole-task transition once.

- gemini-3.8-flash-low, dev5, ios-uikit-state — Source configures a UIKit accessible leaf around independent ordinary child button(s) and supplies no forwarded Open activation/explicit child exposure. This contradicts task preservation; direct-handler tests are not ordinary accessibility navigation evidence.
- gemini-3.8-flash-low, dev7, ios-uikit-actions — Source configures a UIKit accessible leaf around independent ordinary child button(s) and supplies no forwarded Open activation/explicit child exposure. This contradicts task preservation; direct-handler tests are not ordinary accessibility navigation evidence.
- gemini-3.8-flash-low, dev5, ios-uikit-actions — Provided Open button has no activation target/action/callback at all; ordinary Open operation is absent. This is necessary action wiring, not an omitted cosmetic helper.
- claude-haiku-5-5, dev5, ios-uikit-state — Existing independently accessible ordinary Open is deliberately hidden and made shortcut-only; visual tapping does not preserve the removed ordinary accessible path.
- gemini-3.8-flash-low, dev5, ios-swiftui-lifecycle — Actual old sheet completion can use currentSessionID of new panel, consuming new ownership and requesting its focus while it is open.
- gemini-3.8-flash-low, dev7, macos-appkit-actions — Complete example never connects Open or exposes an Open callback, losing one required independent task.
- gemini-3.8-flash-low, dev5, macos-appkit-structure — Both new buttons remain without targets/actions in advertised complete example; no ordinary Open/Details operation implemented.
- gemini-3.8-flash-low, dev7, ios-swiftui-lifecycle — Requests attention before dismissal completes; interactive/non-button path has empty onDismiss and no restoration.
- gemini-3.8-flash-low, dev7, macos-swiftui-lifecycle — The actual old sheet completion reads and consumes the latest presentation owner, so it can dismiss/clear the new panel. This violates the explicit overlapping-presentation preservation requirement.
- gemini-3.8-flash-low, dev5, tvos-uikit-state — Source configures a UIKit accessible leaf around independent ordinary child button(s) and supplies no forwarded Open activation/explicit child exposure. This contradicts task preservation; direct-handler tests are not ordinary accessibility navigation evidence.

## Assessment

Three Codex reviewers examined shuffled packets with the provider and arm mapping withheld. Each reviewer assessed both arms within their assigned cases against the same criteria, recorded exact answer spans, and graded integration separately. The controller verified criterion coverage, excerpt membership and score ranges before joining the grades. Each answer received one review. Reviewers had prior project exposure, and the answer contents can still suggest the guidance used. Outcomes measure source quality on known development scenarios. Actual compiler behavior, native accessibility delivery and the installed skill experience remain unverified for these answers.

The two cohorts use their own denominators. The Haiku subset covers the first seven questions in the frozen order. Comparing its aggregate to the 24-question Flash result would mix provider effects with case selection. [Scoring guide](../dev7-comparison/SCORING.md) · [Sealed package](../dev7-comparison/README.md) · [Machine-readable results](summary.json).

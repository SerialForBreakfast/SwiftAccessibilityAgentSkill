# Signal v2: apply the walkthrough selectively

Use the [successor research candidate](candidate.zip) and its [held comparison](held.zip) instead of running both v1 and v2. The [receipt](receipt.json) binds the parent and successor. All 56 subjects, controller sources, scoring code, grading rules and permissions are unchanged. Default entry growth is 107 bytes; the rest is on demand.

| Walkthrough recommendation | Decision and diagnostic case |
|---|---|
| Reset busy on a stale result | Narrow. Separate an edited snapshot with no successor (G-2ae6e6631d0d54) from a callback whose successor still owns busy state (G-5b313c25cc544a). Clearing on every stale return breaks the latter. |
| Invalidate actions in reuse | Handle same-instance configuration too (G-1079cff7faaab5). Distinguish the ordinary UIControl registration from the accessibility custom action. Preserve current activation and reject stale dispatch. |
| Always post on dismissal completion | Reject the notification mandate. Restore when the app needs it, only for the matching completed dismissal; cancellation, duplicates and reentry are distinct (G-da89005c6d3613, G-79fa7510bdf4bc). A posted request is not evidence of delivery. |
| Use either selector for Off | Keep the documented Swift spelling, group membership and empty-selection permission. Distinguish automatic selection, read-only inspection, and stale actions on the same or replaced item (G-6d2dd61c5ac4ab, G-c04cc5d4aa6f82). |
| Promote UTF-16 guidance globally | Defer. Apple documents UTF-16 for [UITextInput offset distances](https://developer.apple.com/documentation/uikit/uitextinput). A position is an object, not a portable integer. Computing a rotor destination does not generally request mutation of ordinary selection. All four arms met primary behavior on the three neutral text cases, with no whole-task win from the text note. The technical detail is valid; default context cost is not justified. |
| Add more decision matrix rows | Retain existing title/state distinctions, interop and no-change guidance; avoid duplicating a matrix in the entry. Evidence checks may use behavior, identity, counts or relationships; a literal alone isn't a proof. |

Rebuild locally with `python3 -B research/evaluation/signal-panel-v2/build.py`; append `--check` to verify without writing. The 8 discovery tests, original portfolio integrity and 5 focused panel tests check the measurement machinery. They do not show this version improves Gemini answers. Evaluate the existing paired design if approved; do not count historical grades as matched controls or launch another arm per suggestion.

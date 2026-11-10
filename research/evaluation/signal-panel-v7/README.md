# Signal-v7: recipes that models apply

Signal-v7 is a research candidate rebuilt from scratch after signal-v6 run 1. [`candidate.zip`](candidate.zip) is built by `build.py` from [`skill/`](skill/). It has **not been measured on a model**. Released 0.2.2, rc.2 and all earlier candidates are unchanged.

## Why a rewrite

In signal-v6 run 1 (receipt 1507), v6 scored 20/56 whole-question passes, against 16 for 0.2.2 and 14 unaided. That is 7 fixes and 2 regressions against the release, which is not significant.

v6 sessions read the skill in 94% of cells, and usually read the card that covered the failure. That card often already stated the rule they broke. The problem was application, not knowledge. The largest failure class was tests that still pass on the broken code (about 16 questions). Next came fixes not wired into the production path (about 9) and invented APIs (about 6). See [DECISIONS.md](DECISIONS.md).

## What changed

| File | Role |
|---|---|
| `SKILL.md` (2.9 KB) | A 5-step procedure the answer must show: decide, fix, test, a delete-the-fix line for each assertion, missing fixture. Routes by symptom, in developer words. |
| `references/callbacks.md` | Reuse and representable updates. Old callbacks guarded by a token captured at creation. Recipe: keep the old callback, then call it; a table of ways to hold one for UIAction, custom actions, AppKit and representables. |
| `references/media.md` | Write and read back the playing item. An in-memory `AVMutableMovie` fixture with real legible and audible groups and a described-video tag (iOS and macOS). The recipe uses the binding the picker uses. Covers old bindings, missing item vs no group, late completions and chapters. |
| `references/dismissal.md` | A per-presentation dismissal closure carrying its own token. Recipe: late A, then B twice. AppKit: window membership, refusal and detachment, each tested separately. |
| `references/late-delivery.md` | Change the live field, then deliver the old reply; busy must recover. For queued observers, change the value before draining. |
| `references/facts.md` | Leave working native controls alone (Slider, Reduce Motion, editable search field). AppKit accessibility members are methods. |
| `references/apis.md` | Verified signatures for AVFoundation, UIKit, AppKit, SwiftUI and XCTest, with the invented members named. |
| `references/font.md` | Unchanged from v6. |

The total is about 29 KB, against a 40 KB budget.

## Offline checks

| Check | Command | Result |
|---|---|---|
| Reproducible build, leak and link guards, size | `python3 -B research/evaluation/signal-panel-v7/build.py --check` | `588c803b…`, entry 2,854 B, total 29,163 B |
| No new 8-word overlap with 1,116 protected texts, including 474 run-1 answers | `python3 -B research/evaluation/signal-panel-v7/screen.py` | PASS |
| API sheet typechecks on macOS, iOS and tvOS 26 (Swift 6 mode) | `python3 -B evals/results/signal-v7-offline/typecheck.py evals/results/signal-v7-offline/apis/APIs.swift` | OK ×3 |
| Recipe tests pass on the fix and fail on each defect; each named wrong test passes on its defect | `python3 -B research/evaluation/signal-panel-v7/qualify/qualify.py` | PASS: 15 runs (macOS 4, iOS 6, tvOS 5; iOS/tvOS 26.5 simulators), receipt `evals/results/signal-v7-offline/qualify-b3cfj7zs/` |

AppKit focus fallback and outline guidance have no native recipe check yet.

Native checks establish handler effects and media-selection readback in unit tests. They do not establish VoiceOver output, delivered focus or model behaviour.

## Smoke run (submitted November 9; worker acceptance pending)

**Dispatch:** coordinator receipt 1510, operation `signal-v7-smoke1-5c9b28c5-r1`, state `stored`. The receipt does not establish delivery, worker acceptance or completed sessions. The expected return is `signal-v7-smoke1-return.zip` in the private joe-big-dog share.

[`smoke/`](smoke/) holds a sealed packet for one trial of all 56 questions on the v7 arm only: 56 sessions on the Gemini 3.8 Flash Low subscription, answers and traces only. The questions are byte-identical to v6 run 1, so trial 1 pairs with v6 trial 1. Grading is local: the mutation grader first, then source review. Dispatch needs separate owner approval.

- **Seal:** `5c9b28c5…`, reproducible with `smoke/seal.py --check`.
- **Checker:** `smoke/check_return.py` accepts a synthetic complete return, and rejects one with a missing cell or an included grade.

# Signal-v7.1: signal-v7 plus two recipe lines

Signal-v7.1 is a research candidate. It is [signal-v7](../signal-panel-v7/README.md) with two added lines; signal-v7 itself is unchanged and stays frozen at `588c803b…`. Neither has been measured on a model. Released 0.2.2 and rc.2 are unchanged.

## What changed against v7

| File | Added line | Evidence |
|---|---|---|
| `references/callbacks.md` | In a refreshed list, keep the same record ID across the refresh before calling the old callback. | Mutation-grade calibration of run 1 (receipt 1507), trial 1: three answers that the source review passed still pass on the defect, because the refresh swapped IDs and a lookup hid the missing guard. |
| `references/facts.md` | Compare against the input or between states, and keep the supplied wording; do not assert invented label text. | Same calibration: two v6 tests asserted the model's own wording and fail on an equally valid implementation. |

`SKILL.md` changes only its version string. See [DECISIONS.md](DECISIONS.md).

## Offline checks

| Check | Command | Result |
|---|---|---|
| Reproducible build, leak and link guards, size | `python3 -B research/evaluation/signal-panel-v7-1/build.py --check` | `db78bd77…`, entry 2,858 B, total 29,594 B |
| No new 8-word overlap with 1,116 protected texts | `python3 -B research/evaluation/signal-panel-v7-1/screen.py` | PASS |
| Recipe tests pass on the fix and fail on each defect | `python3 -B research/evaluation/signal-panel-v7-1/qualify/qualify.py` | PASS: 15 runs, receipt `evals/results/signal-v7-1-offline/qualify-zpbur0f2/` |

The first qualification batch (`qualify-ks8ofmu2`) stopped on a harness error: the simulators were shut down. It is kept and does not count.

The two added lines have no recipe test of their own. The record-ID line rests on the existing native controls, where the same-rows test fails on the defect and the changed-ID tests pass on it.

## Smoke run (submitted November 9; worker acceptance pending)

**Dispatch:** coordinator receipt 1511, operation `signal-v7-1-smoke1-334b9822-r1`, state `stored`. The receipt does not establish delivery, worker acceptance or completed sessions. The expected return is `signal-v7-1-smoke1-return.zip` in the private joe-big-dog share. It is a separate job from the v7 smoke run (receipt 1510) and runs after it.

[`smoke/`](smoke/) holds a sealed packet, job `signal-v7-1-smoke1`: one trial of all 56 questions on the v7.1 arm only, answers and traces only. Questions are byte-identical to v6 run 1 and to the v7 smoke run, so trial 1 pairs with both.

- **Seal:** `334b9822…`, reproducible with `smoke/seal.py --check`.
- **Grading:** local. `evals/qualification-56/mutation_grade.py` first, then source review.

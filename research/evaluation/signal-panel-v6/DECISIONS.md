# Signal-v6 decision log

One entry per cycle, written before the next run.

## Cycle 0: 2026-11-08, candidate drafted

- **Decision:** propose run 1 (unaided, v2 and v6, with 3 trials) on seal `6a595dbe…` (replaces `d4cba963…`, never sent). No promotion.
- **Why one candidate:** v3, v4 and v5 were each built from one-sample observations. v6 consolidates the persistent failures. It holds back further edits until replicated results exist.
- **Fix rule for cycle 1:** change a card only for a content gap or a harmful instruction that appears in at least 2 of 3 trials, confirmed natively where a qualified control exists. Report oracle defects, question defects and variance; do not teach them.
- **Promotion gate** (0.2.2 → 0.3.0), requiring all of:
  - v6 beats both v2 and unaided on trial-majority whole-task verdicts (sign test p < 0.05);
  - v6 is not worse on the held-out OS26 and discovery set;
  - there are no new native-confirmed regressions;
  - there are no extra critical flags.
- **Open approvals:** sending the handoff (BigDog messaging) and the quota for 504 cells.

## Cycle 0b: 2026-11-08, shore-up pass

- **Entry:** decide whether a fix is needed before writing one. The single-file rule now applies only to changed code; it previously risked rework failures on 19 no-change or explanation-scoped questions. Restored v5's "a helper that prevents the triggering state does not test it".
- **Cards:** the retry wording is limited to failed loads, and the Reduce Motion note is made explicit.
- **Copying screen:** passes for the cards. They share no new 8-word run with questions, rubrics, criteria, calibration or v4 answers.
- **Checker:** rejects component reasons copied across components.
- **Analysis:** `analyze.py` was added and tested on a synthetic return.
- **Native lane:** only compiled contracts give native verdicts. Coverage is about 40% of cells, so source grading remains primary for the rest.

## Current held revision
Preserve the prior 6a595dbe packet under readiness/superseded. The current entry respects the developer's requested file boundaries instead of mandating one file. Dismissal validates current ownership without deriving the caller from mutable state. Media cancellation is optional; rejecting a retired completion is not. Keep the original cross-arm source comparison intact; native disagreement warrants investigation, not automatic promotion or demotion. An incomplete return cannot pass the panel gate. Report newly critical case/trial pairs even when counts balance. This is a research comparison, not a release comparison. Subscription capacity estimates are not granted quota.

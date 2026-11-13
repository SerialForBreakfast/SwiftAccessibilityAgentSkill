# Signal-v7.1 decision log

## Cycle 1: two lines from the mutation-grade calibration (November 9)

### Evidence

`evals/qualification-56/mutation_grade.py` ran the submitted tests of run 1 (receipt 1507), trial 1, against each control's reference, alternative and defect. Private results: `evals/results/mutation-grade-calibration/`.

- 49 of 120 answers under a control were runnable.
- Of 6 vacuous signal-v6 answers, 5 match a wrong test that signal-v7 already names. One does not: the refresh swaps record IDs, so the old action finds no record and the missing guard goes undetected. Two more answers from the other arms failed the same way.
- Two signal-v6 tests asserted wording the model invented.

### Decision

Add one line for each gap and change nothing else, so a difference against the v7 smoke run can be attributed to these lines. Signal-v7 stays frozen because its smoke run (receipt 1510) was already submitted.

Owner choice, November 9: "Patch v7 and re-send".

### Not done

- No model has run v7.1.
- The grader cannot compile tests for 14 of the 40 controlled questions, because those controls lack the question's starter types. Extending the controls is the next step for measurement.
- One control and the 1507 source review disagree on whether the `.selected` trait follows saved state or row selection (question `db32`). Owner decision pending.

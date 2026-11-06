# UPAIR-02 Difficulty Ledger

Local date: 2026-11-05. Assisted development, not a controlled model benchmark.
Exact serving revision and full model context are unavailable. Preserve native
inputs/results before repairing any unexpected failures. Intentional mutants are
separate from accidental errors and must not inflate model failure counts.

## Source and Design Observations

| ID | Difficulty | Treatment | Prompt/rubric implication |
| --- | --- | --- | --- |
| C01 | Apple HTML shells are reachable, but the UIFont URL is unavailable through the browser tool | Installed Apple SDK declarations/comments reviewed directly and hashed; web body not claimed as reviewed | Missing source transport must be disclosed, not treated as evidence the API is unsupported |
| C02 | A multiline flag alone cannot establish absence of clipping | Inspect multiline, preferred fonts, sizing configuration and constraint chain; keep rendered geometry outside evidence | Reward scoped claims and adequate configuration, not promises of universal fit |
| C03 | Earlier typography tests confused detached traits and propagation timing | Apply overrides to each actual label, update traits, assert the effective category, then compare preferred-font configuration | This applies an existing lesson; it is not a new observed failure |
| C04 | The fixture has text, checkmark and selected metadata, but not every valid design needs all three | Rubric accepts equivalent non-color cues and appropriate semantics | Avoid teaching the model a benchmark-specific exact solution |
| C05 | Trait replacement can clear unrelated semantics, while reuse-only resets miss in-place updates | Test repeated chosen/unchosen transitions and retain a seeded unrelated trait | Independent developer question describes lifecycle needs rather than naming the fix |
| C06 | Single-item grouping here differs from the previous independently actionable card | Explicitly scope this fixture to two static labels with selection handled by the controller | Routing guidance should consider child actions, not universally prefer grouping or separation |
| C07 | A documentation patch searched for `Other rows below retain their pending status.` as a standalone line, but the file wrapped that sentence differently | Patch verification rejected the edit; reread the exact context and applied a matching edit | Actual editing/orchestration error, not a Swift or accessibility failure; source tests were unaffected |
| C08 | The staged whitespace check caught a blank unified-diff context line in MUTATIONS.md that the earlier unstaged check had not inspected while the file was untracked | Regenerated display diffs with zero context and repeated the staged check; original Swift and evidence hashes unchanged | Publication-validation gap, not a native-test failure; check newly added files as well as tracked edits |

C02-C06 are design/oracle risks addressed before execution, not spontaneous model
failures. Any actual compiler/assertion failure and its exact code/diagnostic will
be added below with the preserved revision and repair. Full deliberate diffs live
in `MUTATIONS.md`; source/test hashes and native evidence identify the exact run.

## Native Outcome and Translation

Revision1 compiled, all nine positive unit methods passed, and all four deliberate
defects failed their intended selected tests on the first attempt. No unexpected
Swift failure occurred. Accordingly there is no accidental failed code snippet to
invent: exact manufactured failures are in [MUTATIONS.md](MUTATIONS.md), and their
diagnostics are in [the native report](validation/revision-1.json).

The independent developer question describes long translated names, large text,
color-only state and same-instance updates. The controller rubric checks outcomes
without giving the subject the corrective APIs or our implementation. It accepts
alternate valid configurations and does not treat the exact positive fixture as
the only answer. This is one development family, not four independent questions
derived from the four mutants. Independent review and cross-model testing remain
pending; no claim that these errors occur in other models is supported yet.

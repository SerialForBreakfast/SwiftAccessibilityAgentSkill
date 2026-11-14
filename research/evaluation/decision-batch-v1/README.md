# Decision batch v1: what should the skill change?

Research candidate, not a release. The prior callback batch qualified six platform checks; this batch changes the advice developers receive across **51 decisions**. They are not 51 newly discovered defects. Seventeen decisions link to at least one of the 45 failed first answers in the [350-answer source review](../../../evals/discovery-500/grade350/README.md). The other 34 cover contrasting behavior and relevant portfolio contracts. No answer has been generated with this candidate.

| Topic loaded on demand | Decisions | Linked failed answers* | Related previously qualified checks |
|---|---:|---:|---:|
| Actions and registration | 7 | 8 | 3 |
| Presentation and focus | 5 | 7 | 2 |
| Live validation and observations | 5 | 4 | 2 |
| Text coordinates, rotors and scaling | 6 | 5 | 1 |
| Native controls, containers and semantics | 12 | 17 | 8 |
| Player items and media choices | 11 | 5 | 1 |
| Motion and contrast | 5 | 0 | 3 |

*One multi-topic question appears in two rows. A linked answer is not evidence that every clause in its guidance failed. The 20 checks are historical records whose working and alternative implementations passed and whose mutants failed. They qualify those specific assertions, not the rewritten advice. For the separate six callback checks, see the [execution board](../../../evals/discovery-500/callback-batch/README.md).

## What actually changes

Instead of making every review produce a Swift file, XCTest and a prescribed explanation, the entry first distinguishes an explanation, a working control, an implementation and a requested test. Only that last request requires demonstrating the trigger. The seven topic cards replace the earlier narrative recipes, not the SDK spelling reference. Some rules deliberately preserve earlier guidance: the variant tests distillation as well as new coverage. Do not assume brevity preserved every useful implementation detail.

For example, a disabled retained action, an enabled action on a button moved elsewhere, and an old action on the same reused button can all dispatch to the wrong place. Their remedies differ: check current permission, check ownership of the control, or retire the binding. Likewise, Off, automatic selection and a current selection filtered out of a menu are three different decisions. The tests should observe the player's state, not merely a menu label.

The entry is 1,830 bytes; each topic is 834 to 2,112 bytes. These are file sizes, not token use or evidence of reads. The existing 4,234-byte API reference remains optional. The candidate contains no grading board, prompt IDs or private responses.

## Review and reproduce

- [Decision library](decisions.tsv): one authored intervention per distinct family.
- [Controller board](board.json): 287 unique original questions with framework, prompt hashes, source judgments where available, opposing behavior and links to related native receipts. Multi-family questions retain their original identity.
- [Frozen development panel](panel.json): 45 historical failures, 14 previously passing controls and three newly authored opposing controls across six platform/framework combinations. The new controls have no baseline grade. See [qualification and limits](controls/REVIEW.md). [Subject archive](questions.zip) contains questions only; [input seal](input-seal.json) binds subjects, candidate and grading inputs.
- [Candidate archive](candidate.zip): extract in isolation, never over the installed release. Rebuild with `python3 -B research/evaluation/decision-batch-v1/build.py`; add `--check` to compare all generated outputs byte for byte.

**Next decision:** if authorized, compare the frozen incumbent and this package on identical final inputs, reporting recovered decisions, lost working behavior, and proof quality separately. A pass on the selected development panel would justify a transfer check, not promotion.

Authoring request: "Continue but keep going with more changes. This is too narrow to consider an update that only adresses 2 items. It needs to be dozens". Inputs were the unchanged local controller, scenarios, grade ledger, proof receipts, callback report and earlier candidate. Original authored guidance is preserved in the decision library; this note is the separate analysis. No exact intermediate chat or private answer is reconstructed.

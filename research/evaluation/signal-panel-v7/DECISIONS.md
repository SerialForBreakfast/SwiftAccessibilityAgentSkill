# Signal-v7 decision log

## Cycle 0: redesign after signal-v6 run 1 (November 9)

### Evidence

**Final review of receipt 1507** (`evals/results/1507-grade/final-review/`):

| Arm | Whole-question passes |
|---|---|
| signal-v6 | 20/56 |
| 0.2.2 | 16/56 |
| Unaided | 14/56 |

- **v6 against 0.2.2:** 7 fixes, 2 regressions, p ≈ 0.18. Not a meaningful gain.

**Exposure** (traces in the continuation return):
- v6 opened `SKILL.md` in 148 of 158 answered cells, and at least one card in 142.
- In nearly every failing question, the session read the card that covered the failure.
- Several of those cards already stated the rule that was broken. Example: retained-native-target failed 0/12 trials in v6 even though actions.md said "Capture the installed action before rebinding. Invoke it afterward".

**Failure classes** (v6 grader reasons, 36 failing or inconclusive questions):

| Class | Questions |
|---|---|
| A. Non-discriminating tests | 16 |
| B. Fix not wired into production | 9 |
| C. Invented API or compile failure | 6 |
| D. Silent fixture skip | 3 |
| E. Over-diagnosis of working code | 4 |
| F. Ordinary-path loss | 1–2 |

### Decision

Rewrite rather than patch. Prose rules were read and not applied, so v7 changes the *form* of the guidance:

1. **An entry procedure the answer must show,** ending with a "delete-the-fix" line for each key assertion.
2. **Symptom routing** in developer words, so observer questions reach their card. In v6 none did.
3. **Each card follows the same shape:** decide, fix pattern, then a test recipe that names the wrong test models wrote and gives a runnable skeleton.
4. **A media fixture without files.** An in-memory `AVMutableMovie` with tagged tracks gives real selection groups on iOS and macOS. Probed natively: groups load, `select` reads back, and the describes-video tag is honoured. tvOS lacks the type, so the card says so.
5. **A verified API sheet,** typechecked on macOS, iOS and tvOS 26. It names the members models invented.
6. **A restraint list** for working native controls. This answers class E and the d82c regression.

**Size:** the budget is raised to 40 KB total and a 3 KB entry (owner choice). The build is about 29 KB.

### Guard changes

- `XCTAssert` is no longer banned in runtime files, because recipes need test code.
- In exchange, `screen.py` now checks the skill against a wider protected set: questions, criteria, controller files, reference tests and rubrics in `code-examples`, native controls and calibration tests, and all 474 run-1 answers. It requires no new 8-word overlap.
- Generic Swift idioms that matched were renamed rather than exempted.

### Qualification

`qualify/qualify.py` extracts the recipe tests and the `ReturnCoordinator` verbatim from the cards, then runs them against generic subjects (`qualify/Subjects.swift`):
- the fixed subjects must pass;
- each named defect must fail its recipe test;
- the matching "wrong test" (`qualify/WrongTests.swift`) must pass on that defect, which proves the warning is real.

### Not done

- No model has run v7.
- The panel is a development set, so a panel gain alone does not justify promotion. The held-out run stays required.
- AppKit focus fallback and outline guidance have no native recipe qualification yet.

### Next

1. Owner approval for the 56-session smoke run (`smoke/`).
2. Grade it locally: mutation grader first, then source review.
3. Fix only recipes that were read and still produced the wrong test, and routing where a card was not read.

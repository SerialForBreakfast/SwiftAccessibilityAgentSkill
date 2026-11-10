# Improving all 384 discovery prompts for the next pass

Research document, November 8, 2026. It covers every prompt in the [Gemini discovery portfolio](../../../evals/gemini-discovery/README.md).

**Inputs for each prompt:**
- the sealed question;
- Gemini 3.8 Flash Low's unaided first answer and its grade (263 pass, 90 fail, 31 inconclusive);
- the [blind audit](../../../evals/gemini-discovery/BLIND-AUDIT-V1.md);
- the [68-session factorial](../../../evals/gemini-discovery/audit-revision-1/RESULTS.md);
- its defective/working fixture pair.

**How the suggestions were made:** three reviewers wrote one record per prompt against a [fixed schema](schema.md). Each record is a diagnosis, a disposition, replacement wording where needed, an oracle change, skill links and a transfer note. [verify.py](verify.py) checks that coverage, values and wording are complete, and that no record reuses any 12-word run of a private answer.

**What this document is not:** these are proposals. No prompt, grade, rubric or skill file has changed, and no model ran. The sealed packet and frozen ledgers stay as they are. An amended prompt is a new prompt and needs its own unaided answer.

## How to make a big improvement

**The skill can't show a big gain on this portfolio yet.** Three things hide any gain:
- The questions give away most fixes.
- The whole-answer grade is dominated by the quality of the proposed check.
- A share of the grades are wrong.

Fixing those, and then targeting four content areas, is where the large improvement is. In order:

1. **Fix the measurement before tuning the skill.**
   - **28 prompts are P0.** 17 are confirmed model gaps. The other 11 are oracle or policy defects that corrupt the count:
     - the oracle tests a different behavior from the question (Q57 reentry vs. dismissal permission);
     - the grade requires more than the prompt states (Q55, Q34, Q24);
     - product policy is left unstated (Q03, Q23, Q56).
   - **Two first grades are verifiably wrong:**
     - `G-d7b1d47b70ec1b` failed an answer that is 99% identical to that task's own registered accepted alternative.
     - `G-6f19bb8fa70065` failed an answer whose test asserts exactly what the package's reference test asserts.
   - Every wrong grade erases a possible rescue or hides a regression. The [data corrections](#data-corrections-before-the-next-pass) list the rest.

2. **Create headroom in the questions.**
   - **75 passing prompts have no headroom:** the opening states the defect and asks for the fix, so a model with no skill passes. Another 12 state a symptom as fact.
   - The review proposes **122 question changes**:
     - 41 neutral rewrites;
     - 52 working/defective twins with identical wording;
     - 14 stated policies;
     - 8 splits;
     - 7 raised to an observable endpoint.
   - The factorial shows why: with neutral wording, all three text-range cases kept their primary behavior in every arm. The stated symptom ("lands on the wrong text after emoji") is what drove the grapheme-count regression.

3. **Grade the fix and its proof separately.** In the factorial, unaided answers met the primary behavior on 13 of 17 tasks but the whole task on 1 of 17, and only 8 of 68 answers met the focused-check criterion.
   - **55 prompts get `grade-components`:** primary behavior, preservation, evidence and rework scored apart.
   - Every working/defective pair is scored on **both versions correct**.

   Without this, a skill that improves code but not tests looks like no change.

4. **Change the skill where the evidence points, in this order:**
   - **S1 review sentence + S8 restraint.** Trace the path; leave working code; don't add traits, hints or notifications to a working native control.
     - Linked to 102 and 73 prompts.
     - It's the only change with a measured effect: rework fell from 10 to 3, with one whole-task gain and no regressions on the whole-answer measure.
   - **S2 verification.** Exercise the installed handler and assert the observable effect with a literal value.
     - Linked to 84 prompts. It is the most frequent link on non-passing items (49).
     - Untested so far. It's the next single instruction to try.
   - **S3 callback ownership.** What a closure captures when installed and what it must validate when it runs.
     - Linked to 102 prompts.
     - It covers the largest confirmed technical family: rebound actions, presentation owner, input snapshots, stale Off callbacks.
   - **S5 precise platform facts.** One on-demand card, only for the confirmed misses:
     - visible title vs. identifier;
     - visible selected-state wording;
     - edit category;
     - AppKit row role;
     - the actual tvOS text-reflow availability.
   - **S4, S6 and S7: narrower, and evidence-gated.**
     - S6 (text offsets) should **not** get skill content yet; the gap was induced by the prompt.

5. **Run the next pass on a reshaped portfolio:**
   - 135 controls kept as regression guards;
   - 122 changed questions;
   - 83 oracle or grading repairs;
   - 24 retired duplicates;
   - 20 reserved as transfer.

   Count gains only on comparable pairs. Promote a change only if it holds on the transfer reserve and the working twins.

## Where the headroom is

<!-- lanes:begin -->
| Lane | Items | Unaided pass / fail / inconclusive | Confirmed model gaps | Rewrite or pair for headroom | Oracle or criteria repairs | Keep as control |
|---|---:|---|---:|---:|---:|---:|
| repair | 161 | 131 / 19 / 11 | 8 | 79 | 25 | 26 |
| preservation | 59 | 25 / 34 / 0 | 8 | 13 | 22 | 20 |
| implementation | 92 | 54 / 22 / 16 | 20 | 4 | 43 | 41 |
| historical | 47 | 35 / 9 / 3 | 3 | 4 | 9 | 29 |
| integration | 7 | 3 / 3 / 1 | 0 | 0 | 4 | 3 |
| workflow | 18 | 15 / 3 / 0 | 4 | 0 | 2 | 16 |
<!-- lanes:end -->

**What the lanes show:**
- **Repair** is mostly easy: the answer is in the question.
- **Preservation** fails are mostly rework, and the review separates regression from rework.
- **Implementation** holds most of the confirmed gaps, 20 of 43. That's because these prompts describe a workflow without naming the defect.
- **Historical** and **integration** items are mostly controls, and several duplicate each other.

## What the review proposes

<!-- dispositions:begin -->
| Disposition | Items |
|---|---:|
| `repair-oracle` | 28 |
| `split-criteria` | 8 |
| `specify-policy` | 14 |
| `rewrite-neutral` | 41 |
| `pair-variant` | 52 |
| `raise-to-integration` | 7 |
| `grade-components` | 55 |
| `keep-control` | 135 |
| `reserve-transfer` | 20 |
| `retire-duplicate` | 24 |

| Main problem | Items |
|---|---:|
| `good-as-is` | 118 |
| `no-headroom` | 75 |
| `real-model-gap` | 43 |
| `duplicate` | 42 |
| `grader-uncertain` | 21 |
| `rework-only` | 19 |
| `bundled-criteria` | 15 |
| `evidence-only` | 13 |
| `symptom-as-fact` | 12 |
| `oracle-mismatch` | 10 |
| `ambiguous-policy` | 10 |
| `weak-endpoint` | 6 |
<!-- dispositions:end -->

**Cross-cutting prompt fixes behind these numbers:**
- **Ask, don't assert.** Replace "X can happen; can you fix it?" with a question about what the code does in a concrete situation. Examples: "Which document does the earlier Delete affect after refresh?" and "What range does search return for 'cat' in '😀 cat!'?"
- **Give twins the same words.** The defective and working versions get identical neutral wording in separate sessions, so the result shows whether the model reads the code or patches by default.
- **State product policy the grade depends on:**
  - full vs. forced subtitles;
  - which control's appearance must stay;
  - what a Bool return means;
  - chapter boundaries and the empty case;
  - whether IDs can be reused.
- **Split bundled questions.** Q57 becomes reentry ‖ permission; Q34 becomes removal ‖ same-ID replacement; Q24 becomes name refresh ‖ status value and no focus request.
- **End at what the developer observes:** the player item's actual selection rather than a local preference ID, and the selected text rather than offsets computed by the same algorithm.
- **Remove platform noise.** Three iOS and macOS prompts carry tvOS-only Larger Text clauses.

## Skill changes by reach

<!-- skills:begin -->
| Code | Skill content | Items linked | P0 items | Platforms |
|---|---|---:|---:|---|
| S1 | Review: trace the path, leave working code | 102 | 12 | iOS 51, macOS 34, tvOS 17 |
| S3 | Callback capture and validation | 102 | 8 | iOS 32, macOS 43, tvOS 27 |
| S2 | Verify through the actual handler | 84 | 11 | iOS 34, macOS 34, tvOS 16 |
| S8 | Restraint and pruning | 73 | 5 | iOS 31, macOS 26, tvOS 16 |
| S7 | Media selection and policy | 52 | 1 | iOS 13, macOS 20, tvOS 19 |
| S5 | Precise platform facts | 41 | 7 | iOS 16, macOS 14, tvOS 11 |
| S4 | Focus destination and eligibility | 33 | 5 | iOS 11, macOS 11, tvOS 11 |
| S6 | Text-offset units | 17 | 3 | iOS 9, macOS 4, tvOS 4 |
<!-- skills:end -->

**How to prove each one** (smallest condition first; same questions, model, tools and output contract):

| Code | Experiment |
|---|---|
| S1, S8 | Replicate the review sentence on fresh twins and on neutral rewrites. Score both-correct pairs and rework. Test the S8 restraint clause by removing it. |
| S2 | Add the verification sentence to the review sentence, against the review sentence alone. Score the evidence component and whole-answer passes. |
| S3 | A short note at the point of use about what a callback captures when installed and checks when it runs. Score it on rebound-action, presentation-owner, input-snapshot and stale-Off prompts, with the view's installed callback driven by the oracle. |
| S5 | One on-demand facts card read only when routed. Score the five confirmed misses, plus a control where the fact doesn't apply. |
| S4, S7 | Only after S1–S3, on their own P0/P1 prompts. |
| S6 | No content. Rerun the neutral text-range rewrites unaided first; write content only if a gap remains. |

## Data corrections before the next pass

- **Verified grading errors:**
  - `G-d7b1d47b70ec1b` should be pass: the answer matches the registered `alternative-crossfade.swift`.
  - `G-6f19bb8fa70065` should be pass: its test equals the package's reference assertion. That turns its pair into both-correct.
- **Grades that need a versioned adjudication:**
  - `G-19d3be9a5d1d73` is a harness error recorded as an inconclusive model result.
  - `G-a424d7b520fd26` failed for asking clarifying questions in a tool-free setting.
  - `G-5f3c8c25e44c4b`'s oracle asks for double loading, which the prompt never mentions.
  - Q17 (`G-f0de252053bcbb`) was reversed to primary pass in the audit.
- **Pair labels the audit changed:** three fixes-defect-breaks-working pairs now have audited preservation passes:
  - `G-55fe2bf3aeec99`/`G-471867cfc77618`;
  - `G-6c468546da6af4`/`G-dd75bbabea3b9b`;
  - `G-9f59180da322fa`/`G-b18da2b792890e`.
- **Contracts and evidence that need a decision:**
  - `G-9dc2d664c3baca`'s oracle depends on a Bool meaning the question never states.
  - `G-365faed8f7362b` may use an Objective-C-only spelling. Native grading would settle it.
  - Historical/implementation items with a compiled rc.1 contract should use that unit result as their primary grade, not "inconclusive".
- **Prompt hygiene:**
  - tvOS-only clauses in `G-5d3ebb1283a579`, `G-27926d3f994473` and `G-7331721435c052`;
  - three `media-macos-v1` prompts mix in form-validation state and have cleaner v2 counterparts;
  - historical copies duplicate integration tasks (`G-370808352ca7dc`, `G-a3221645549ddf`, `G-b32973d721c21d`).

## P0 items

<!-- p0:begin -->
| Item | Cell | Lane · decision | Problem | Disposition | Diagnosis |
|---|---|---|---|---|---|
| `G-d7b1d47b70ec1b` | iOS SwiftUI | integration · — | oracle-mismatch | repair-oracle | Integration fail looks like a grading error: the answer changes the Reduce Motion path to a short easeInOut with an opacity transition and keeps the spring and toggle state, which matches the task's registered alternative-crossfade (expected pass). |
| `G-55fe2bf3aeec99` | iOS UIKit | preservation · contrast-linear | oracle-mismatch | repair-oracle | Audit Q53 reverses the ledger: the recommendation and test keep piecewise sRGB and the correct midgray value; the gamma-2.2 diff is explicitly conditional on another specification. Pair label fixes-defect-breaks-working is therefore wrong for this fixture. |
| `G-6c468546da6af4` | iOS UIKit | preservation · container-children | oracle-mismatch | repair-oracle | Audit Q05 reverses the ledger: blind whole/primary pass because the answer explicitly groups the two operable controls under a non-element stack and keeps both callbacks. The original rationale (title omitted) is not what the sample oracle tests; it checks dispatch only. |
| `G-8eafbd1521124e` | iOS UIKit | preservation · range-coordinate | real-model-gap | rewrite-neutral | Confirmed range-coordinate gap (audit Q46 fail/fail; pair both-fail): working UTF-16 offsets are replaced with grapheme counts. Factorial text-range-46 with neutral wording kept primary in all four arms, so the asserted symptom induced the regression; whole still failed on the focused check. |
| `G-9f59180da322fa` | iOS UIKit | preservation · text-size-change | ambiguous-policy | specify-policy | Audit Q56 regrades pass/pass: the total label already adapts, and the broad question also covers the visible Pay title, for which the answer gives a scoped alternative. The oracle tests label prerequisites and the payment callback, not Pay scaling. Factorial total-text kept primary in all arms. |
| `G-e24e3f394ea182` | iOS UIKit | preservation · range-coordinate | real-model-gap | rewrite-neutral | Confirmed range-coordinate gap (audit Q47 fail/fail): a valid UTF-16 offset is mapped into grapheme units, and reverse lookup uses the wrong units too. Factorial text-range-47 kept primary in all arms under neutral wording; whole failed on the check. |
| `G-333de6e92ef584` | iOS UIKit | repair · dismiss-reentry | oracle-mismatch | split-criteria | Audit Q57 regrades pass/pass: the answer correctly explains why closing twice cannot restore twice; the fixture instead removes dismissal permission, which the question never mentions. Factorial children reentry and dismiss-permission both stayed whole-fail/primary-pass in all arms. |
| `G-6f19bb8fa70065` | iOS UIKit | repair · shortcut-dispatch | oracle-mismatch | repair-oracle | Ledger fail with primary pass looks like a grading error: the answer restores onArchive and its test expects a second invocation to return false with no callback, which is exactly what the reference test asserts (second handler call false, calls stays 1). |
| `G-840924fec7426a` | iOS UIKit | repair · range-coordinate | real-model-gap | rewrite-neutral | Confirmed range-coordinate gap (audit Q38 fail/fail): recognizes the +1 error but switches to Character distances; after emoji the range still misses, and the test compares offsets from the same wrong algorithm. Factorial text-range-38 kept primary in all arms; UIKit text note added nothing. |
| `G-895e740bc6ddd9` | iOS UIKit | repair · refresh-name | bundled-criteria | split-criteria | Audit Q24 regrades primary pass: the name already refreshes; the answer adds a focus-affecting notification and clears the ordinary status, while the hidden check silently requires that status. Factorial current-order child stayed F/P in all arms. |
| `G-d95da35e90afc0` | iOS UIKit | repair · edit-category | real-model-gap | keep-control | Confirmed registered gap (edit-category; audit Q58 fail/fail): identifies the missing category but uses a .edit spelling instead of UIAccessibilityCustomAction.editCategory; the test repeats the API error and omits the nil default. |
| `G-da89005c6d3613` | iOS UIKit | repair · dismissal-completion | real-model-gap | keep-control | Confirmed registered gap (dismissal-completion; audit Q14 fail/fail): keeps posting focus at Close and suppresses the completion post; a stale-operation check cannot move delivery after dismissal. |
| `G-18fda1e5d3c168` | iOS SwiftUI | workflow · custom-control-increments | real-model-gap | specify-policy | Ledger pass, but audit Q19 grades fail/fail: seeks to media end at the last chapter, assumes a nonempty list and never shows ordinary play. Factorial chapter-boundaries child failed whole and primary in all four arms, so the gap holds with an explicit policy. |
| `G-32019e51844cc7` | macOS SwiftUI | preservation · rebound-action | real-model-gap | rewrite-neutral | Audit Q35 confirms a preservation regression: removing the deliberate revision check lets a retained action select or delete a replacement with a recycled ID, and the answer's test explicitly expects the stale action to succeed. The asserted symptom on working code invited the change. |
| `G-65558ea85abec1` | macOS SwiftUI | preservation · forced-vs-full | ambiguous-policy | specify-policy | Audit Q03: labeling a forced option distinctly is a plausible reading, so the original primary fail does not hold (blind primary pass); its test never completes loading. Factorial full-captions: the review sentence turned primary pass in 2 of 4 arms but no arm passed whole. |
| `G-79fa7510bdf4bc` | macOS SwiftUI | preservation · presentation-owner | real-model-gap | rewrite-neutral | Audit Q10 flips the original primary pass: the view callback still reads mutable ticket state, so a late A dismissal can present B's ticket to a guard that accepts it; the test supplies the old ticket by hand. Factorial dismiss-owner: all four arms fail whole and primary. |
| `G-9ce845a566d425` | macOS AppKit | preservation · row-role | real-model-gap | repair-oracle | Audit Q12 confirms the fail: the answer marks the row not an accessibility element, flattening the requested row semantics, and its test checks getters on an ignored object. An AppKit row can be an element and have children, so the supplied code (role row, children [open]) was working. |
| `G-352803701b8f4a` | macOS AppKit | repair · stale-tree-node | oracle-mismatch | split-criteria | Audit Q34 reverses the fail (pass/pass): the answer resolves against the active map and reports zero children after removal; the original grade penalized ID reuse, which the check does not cover. Factorial split: node-removal fails whole in all arms on the focused check, node-replacement passes in all arms. |
| `G-be25d510c5ffe5` | macOS AppKit | repair · eligible-target | real-model-gap | pair-variant | Audit Q07 confirmed eligible-target gap: an enabled visible original can refuse first responder; the answer claims it is eligible, consumes the token on it and misses the fallback. Its tests cover a removed primary instead. |
| `G-6bfef2bcad970d` | macOS AppKit | workflow · window-focus-isolation | real-model-gap | keep-control | Audit Q37 confirmed window-focus-isolation gap: pairs each inspector with its host but checks only acceptsFirstResponder on the saved responder, not that it still belongs to that window; the close action can steal focus and there is no stale-presentation check. |
| `G-d82c5ccce8e33f` | macOS SwiftUI | workflow · interop-double-exposure | real-model-gap | keep-control | Audit Q51 confirmed interop-double-exposure gap (critical): hiding the representable's accessible subtree can remove the native editable search field together with the duplicate; the alternative of removing redundant wrapper semantics was right but not the main recommendation. |
| `G-0d69f79fef78e5` | tvOS UIKit | preservation · conflicting-state-text | ambiguous-policy | specify-policy | Audit Q23 reversed the grade: status, accessibility value and selected trait already follow the input; the answer's one-line native isSelected sync satisfies a plausible reading of control state, and the oracle ignores isSelected. Factorial selected-status with specified scope: unaided F/F, review sentence P/P, both P/P. |
| `G-61cfbceeb763f0` | tvOS UIKit | preservation · rebound-action | real-model-gap | rewrite-neutral | Audit Q45 confirmed an actual regression on working code: a detached old button can select when its ID persists, and the answer's test expects that stale selection. This is the shelf example of fixing one version and breaking the working one. |
| `G-3eecace7f0b93c` | tvOS UIKit | repair · conflicting-state-text | real-model-gap | specify-policy | Audit Q49 confirmed (registered key conflicting-state-text): selected and unselected configurations still show identical empty state text, and search counts are assigned as the control's value. Pair both-fail with Q23. |
| `G-5b313c25cc544a` | tvOS UIKit | repair · input-snapshot | real-model-gap | keep-control | Audit Q54 confirmed (registered key input-snapshot): the answer follows only edit(), which cancels; a native text field can change independently, after which the completion accepts old input or applies obsolete errors. iOS and macOS copies also fail. |
| `G-c69928988c0e26` | tvOS UIKit | repair · detached-action | oracle-mismatch | split-criteria | Audit Q55 reversed the grade: directly removing the retained button now rejects it and an attached button still acts; the oracle also demanded rejection after reparenting, which the example never specified. Factorial split: removal all arms F/P; reparent arms F/P except review F/F. |
| `G-ed8bff5491ab72` | tvOS UIKit | repair · visible-title | real-model-gap | keep-control | Audit Q21 confirmed (registered key visible-title): both controls still have no visible title; the change and test address automation identifiers. |
| `G-e56a902ef372a2` | tvOS SwiftUI | workflow · tv-text-reflow | real-model-gap | grade-components | Audit Q32 confirmed (registered key tv-text-reflow): the vertical layout protects Play and Details, but the newer-SDK section gates at tvOS 18 on a 26.0 deployment, treats scrollTargetLayout as marquee, and gives no valid later availability boundary. |
<!-- p0:end -->

## All 384 prompts

Each entry gives:
- the unaided grade, plus any audit and pair result;
- the suggested disposition;
- the diagnosis;
- the prompt and oracle changes, with proposed wording where the question should change;
- the skill link;
- how a fresh transfer case should differ.

<!-- items:begin -->
### iOS

#### iOS · repair (64)

**`G-0009f3f00956ae`** · UIKit · selected-state · unaided **pass** (primary pass). Pair: fixes-defect-breaks-working. · **P1 rewrite-neutral** · no-headroom · S1

> I'm reviewing a UIKit change for iOS 26.0. The old row can still be described as selected after the selection moves. Can you make both rows reflect the current selection?

- **Diagnosis:** Ledger pass; pair fixes-defect-breaks-working with G-3728319099e01c. The asserted symptom gives the fix and drove the working twin's change.
- **Prompt:** Same neutral question on both versions.
- **Proposed wording:** iOS 26.0, UIKit. In this list, the saved marker moves from row A to row B while both cells stay on screen and neither is dequeued. Afterward, what does each row expose as its saved state, and what happens to its other traits, its collection selection and its button action?
- **Oracle:** Keep the two-row swap test with both states.
- **Skill:** Same wording isolates S1.
- **Transfer:** tvOS collection view.

**`G-043705b50c795c`** · UIKit · duplicate-completion · unaided **pass** (primary pass). · **P3 keep-control** · good-as-is · S3

> I'm reviewing a UIKit change for iOS 26.0. A service sometimes delivers its completion twice. Can you apply the first valid result only?

- **Diagnosis:** Ledger pass: separates the already-consuming path from the missing consumption and tests duplicate delivery. Guards an important async ownership behavior with tvOS and macOS passes too.
- **Prompt:** none
- **Oracle:** none
- **Skill:** Duplicate completion consumption is S3 callback ownership.
- **Transfer:** tvOS siblings already cover it; a transfer would use a delegate-based service rather than closures.

**`G-061bd5a3273756`** · UIKit · forced-vs-full · unaided **inconclusive** (primary pass). · **P1 specify-policy** · ambiguous-policy · S7, S2

> I'm reviewing a UIKit change for iOS 26.0. Our captions menu offers a forced-only translation as if it were full subtitles. Can you keep those choices distinct?

- **Diagnosis:** Ledger inconclusive, primary pass: separates forced and full requests by characteristic, but AVFoundation test doubles are unconstructible. Audit Q03 notes full vs. forced can mean exclusion or a separate labeled choice, so the product policy is unstated.
- **Prompt:** State the menu policy for forced-only tracks and remove the asserted 'as if it were full' framing.
- **Proposed wording:** iOS 26.0, UIKit. Our captions menu should list only complete subtitle tracks; forced-only translation tracks are played automatically and must not appear as choices. The asset has English full, French full and French forced-only. Which choices does this menu offer, and what gets selected for each?
- **Oracle:** Assert the offered list and selected option from injected descriptors; grade test constructibility separately as evidence and do not let an unconstructible double decide the primary verdict.
- **Skill:** Forced vs. full and the menu policy are S7; constructible proof is S2.
- **Transfer:** tvOS AVPlayerViewController transportBarCustomMenuItems with the same policy.

**`G-0b8da41355bd69`** · UIKit · player-item-owner · unaided **pass** (primary pass). · **P3 keep-control** · good-as-is · S3

> I'm reviewing a UIKit change for iOS 26.0. The player can replace its item from outside this view. Can you prevent an old lookup from updating the new item's details?

- **Diagnosis:** Ledger pass: compares captured and actual player item by identity at callback time. Guards the external-replacement case that the now-playing integration task (mutant-cached-item-guard) shows other models miss.
- **Prompt:** none
- **Oracle:** none
- **Skill:** Validating the actual current item when the callback runs is S3.
- **Transfer:** Integration task now-playing-late-title already transfers it.

**`G-0c0e259e645a5f`** · UIKit · disabled-action · unaided **pass** (primary pass). · **P1 rewrite-neutral** · no-headroom · S1, S2

> I'm reviewing a UIKit change for iOS 26.0. A disabled command can still run through another activation path. Can you make the control respect its current enabled state?

- **Diagnosis:** Ledger pass: disabled rate changes are rejected with no callback. The opening states the defect class, so this shows the fix is easy; macOS sibling preservation failed, so the decision has headroom on working code.
- **Prompt:** Ask what each activation path does while disabled rather than asserting one runs, and give the same wording to a working twin.
- **Proposed wording:** iOS 26.0, UIKit. While controlsEnabled is false, what happens if someone taps a speed button, calls select(_:) directly, or activates the button with an accessibility action? Keep the enabled behavior the same.
- **Oracle:** Assert no callback and unchanged selectedRate through each path while disabled, and one callback after re-enable.
- **Skill:** Tracing each path is S1; driving the installed handler is S2.
- **Transfer:** macOS NSSegmentedControl speed picker with an accessibilityPerformPress path.

**`G-0f5d8b65a4920e`** · UIKit · decorative-element · unaided **pass** (primary pass). Pair: fixes-defect-breaks-working. · **P1 rewrite-neutral** · no-headroom · S1

> I'm reviewing a UIKit change for iOS 26.0. A decorative part of this view is getting its own navigation stop. Can you remove just that stop?

- **Diagnosis:** Ledger pass; pair fixes-defect-breaks-working with G-b3e3789d10b0ed. The asserted 'getting its own navigation stop' is accurate here but leads to rework on the working twin.
- **Prompt:** Ask which stops the card has, with identical wording on both versions.
- **Proposed wording:** iOS 26.0, UIKit. This card shows a decorative star beside a title and two buttons. Which navigation stops does VoiceOver get on this card today? Keep the title and both buttons reachable.
- **Oracle:** Keep the existing assertion that only the star is excluded and both controls and the title remain elements.
- **Skill:** Same neutral question across versions isolates S1 tracing.
- **Transfer:** SwiftUI card with an Image decoration inside accessibilityElement(children: .contain).

**`G-1002fd829cecbb`** · UIKit · motion-notification · unaided **pass** (primary pass). Pair: both-correct. · **P3 keep-control** · good-as-is · S1

> I'm reviewing a UIKit change for iOS 26.0. Does this observer refresh the motion setting when that setting actually changes?

- **Diagnosis:** Ledger pass; pair both-correct with the same neutral wording. A model for how the other pairs should be phrased.
- **Prompt:** none
- **Oracle:** none
- **Skill:** Same neutral question across versions isolates S1.
- **Transfer:** macOS NSWorkspace accessibility display options notification.

**`G-10cf3d04a66de0`** · SwiftUI · interop-rebind · unaided **pass** (primary pass). Pair: fixes-defect-breaks-working. · **P1 rewrite-neutral** · no-headroom · S3, S2

> I'm reviewing a SwiftUI change for iOS 26.0. The wrapper updates its SwiftUI state but the native button can still send to the previous target. Can you fix the binding and teardown?

- **Diagnosis:** Ledger pass; pair fixes-defect-breaks-working with G-01c10c6a8573fa. The asserted 'can still send to the previous target' gives the fix here and induces rework on the working twin.
- **Prompt:** Same neutral interop question on both versions.
- **Proposed wording:** iOS 26.0, SwiftUI with UIKit interop. The wrapper updates from item A to item B and is later dismantled. If the native button sends its action after each step, which handler runs? Keep the same native button and its title.
- **Oracle:** Keep stale, current and dismantled callback cases; drive the installed native action, not a parallel closure.
- **Skill:** Rebinding ownership is S3; driving the installed action is S2.
- **Transfer:** macOS NSViewRepresentable siblings already exist; avoid a third renamed copy.

**`G-13ec5725e0605e`** · UIKit · inspection-preserves-selection · unaided **pass** (primary pass). · **P2 pair-variant** · no-headroom · S7

> I'm reviewing a UIKit change for iOS 26.0. Opening the track inspector changes the chosen audio or captions. Can you make inspection read-only?

- **Diagnosis:** Ledger pass: reports option selection without mutating the item. Opening names the mutation and the 'read-only' remedy.
- **Prompt:** Add a working twin and ask what the selected audio and captions are after opening the inspector.
- **Proposed wording:** iOS 26.0, UIKit. The viewer chose Spanish audio and turned captions Off. After they open the track inspector and close it, which audio and caption options are selected on the player item?
- **Oracle:** Assert the player item's selected options before and after inspection with literal expected options, including captions Off.
- **Skill:** Reading vs. writing the actual player item's selection is S7.
- **Transfer:** SwiftUI VideoPlayer diagnostic sheet using the same item.

**`G-1669799648b317`** · UIKit · live-inference · unaided **pass** (primary pass). · **P2 pair-variant** · no-headroom · S1

> I'm reviewing a UIKit change for iOS 26.0. The inspector labels a stream live when all it knows is that the duration is indefinite. What should it report instead?

- **Diagnosis:** Ledger pass: preserves supplied stream kind independent of indefinite duration. Opening names the faulty inference, so it shows an easy stated fix.
- **Prompt:** Add a working twin and ask what the inspector reports for an indefinite-duration video-on-demand item.
- **Proposed wording:** iOS 26.0, UIKit. For an item whose duration is indefinite but whose stream type we already know is event (not live), what does this inspector report as its kind?
- **Oracle:** Assert reported kind equals the supplied type for indefinite durations; no change expected on the twin.
- **Skill:** Twin measures tracing of where kind comes from.
- **Transfer:** tvOS diagnostics overlay for HLS event playlists.

**`G-1b69607eb4408a`** · UIKit · eligible-target · unaided **pass** (primary pass). · **P3 keep-control** · good-as-is · S4

> I'm reviewing a UIKit change for iOS 26.0. After a refresh the original focus target may no longer belong here. Can you restore only to a usable target or fallback?

- **Diagnosis:** Ledger pass: validates the original target before posting and exercises fallback. eligible-target is a confirmed registered gap elsewhere (audit Q07 macOS repair fail), so this iOS pass guards a behavior that fails on a sibling.
- **Prompt:** none
- **Oracle:** Add the Q07 case: an enabled visible descendant that refuses becoming focused must fall through to the eligible fallback, not consume the request.
- **Skill:** Restoring only to an eligible member with declared fallback is S4.
- **Transfer:** Q07 sibling on macOS already transfers it; next transfer: SwiftUI AccessibilityFocusState with a removed row.

**`G-1cacc76921ce33`** · UIKit · multiline · unaided **pass** (primary pass). Pair: fixes-defect-breaks-working. · **P1 rewrite-neutral** · no-headroom · S1

> I'm reviewing a UIKit change for iOS 26.0. When a delivery option wraps to a second line in translation, part of the name disappears. Can you fix the row without shortening the text?

- **Diagnosis:** Ledger pass; pair fixes-defect-breaks-working with G-24ccdb855e595d. The asserted 'part of the name disappears' prompt is accurate here and primes rework on the working cell.
- **Prompt:** Same neutral layout question on both versions.
- **Proposed wording:** iOS 26.0, UIKit. At accessibility text sizes a translated delivery-option name needs two or three lines. How does this cell lay out that name today, and is any of it truncated or shrunk? Keep the full wording.
- **Oracle:** Keep the line-limit and shrink assertions; state that static configuration cannot establish rendered fit.
- **Skill:** Same wording isolates S1.
- **Transfer:** tvOS label in a focusable cell with large text.

**`G-1dbcdaa7e079f5`** · UIKit · rotor-direction · unaided **inconclusive** (primary pass). · **P2 repair-oracle** · grader-uncertain · S2

> I'm reviewing a UIKit change for iOS 26.0. Moving to the previous result jumps in the same direction as Next. Can you correct navigation including the ends of the list?

- **Diagnosis:** Ledger inconclusive, primary pass: corrects the direction and checks both ends, but direct rotor predicate construction and handler access were unverified without a compile.
- **Prompt:** Keep the question; replace 'jumps in the same direction as Next' only if a twin is added.
- **Oracle:** Add a checkable criterion: invoking the installed rotor's itemSearchBlock with previous from the second result returns the first, and returns nil at both ends; accept any predicate construction that compiles.
- **Skill:** Driving the installed rotor block is S2.
- **Transfer:** macOS NSAccessibilityCustomRotor with the same direction contract.

**`G-1e5f01625ec692`** · UIKit · contrast-appearance · unaided **pass** (primary pass). · **P2 pair-variant** · no-headroom · S1

> I'm reviewing a UIKit change for iOS 26.0. The contrast tool reports the same result even when the selected appearance changes. What path through this code needs updating?

- **Diagnosis:** Ledger pass: resolves each dynamic color against supplied traits. The opening tells the developer which path is wrong, so the pass indicates an easy task.
- **Prompt:** Add a working twin and ask for the light and dark results of a named semantic color pair instead of asserting the stale path.
- **Proposed wording:** iOS 26.0, UIKit. For label on systemBackground, what ratios does this contrast tool report in light and dark appearance, and with Increase Contrast on?
- **Oracle:** Assert distinct resolved ratios per trait collection; no change expected on the working twin.
- **Skill:** A neutral twin tests tracing of trait resolution rather than accepting the reported symptom.
- **Transfer:** macOS NSAppearance-based resolution with performAsCurrentDrawingAppearance.

**`G-26f1556458b0ab`** · UIKit · modal-state · unaided **pass** (primary pass). · **P2 pair-variant** · no-headroom · S4

> I'm reviewing a UIKit change for iOS 26.0. When a panel closes the background doesn't always return to its previous state. How should this screen handle opening and closing it more than once?

- **Diagnosis:** Ledger pass: clears modality on close and tests the exposed property. Asserted symptom, no working twin for this containers fixture.
- **Prompt:** Add a working containers twin under the same neutral wording as the modal fixture.
- **Proposed wording:** iOS 26.0, UIKit. The background was already hidden from VoiceOver for another reason before this panel opened. After opening and closing the panel twice, what is the background's accessibility state and the panel's modal flag?
- **Oracle:** Assert accessibilityViewIsModal false after escape and close, and the background's original hidden value after each cycle.
- **Skill:** Returning the screen to its prior state after dismissal is part of the S4 destination contract.
- **Transfer:** SwiftUI sheet with accessibilityHidden on the presenting content.

**`G-2a3677e01788e4`** · UIKit · range-kind · unaided **pass** (primary pass). Pair: fixes-defect-breaks-working. · **P1 rewrite-neutral** · no-headroom · S2

> I'm reviewing a UIKit change for iOS 26.0. The player says I can seek through an interval that was only buffered. How should the inspector describe these two ranges?

- **Diagnosis:** Ledger pass; pair fixes-defect-breaks-working with G-6b85a8fc52d837. The asserted symptom is true for this fixture and gives the fix.
- **Prompt:** Same neutral range question on both versions.
- **Proposed wording:** iOS 26.0, UIKit. Our player has buffered 0–90 s of a stream, but only 0–60 s is currently seekable. What does this inspector report for each range, and what would it say about seeking to 75 s?
- **Oracle:** Assert a buffered-only time is not reported as seekable and a seekable time is, using literal CMTimeRanges.
- **Skill:** Literal range assertions are S2.
- **Transfer:** tvOS and macOS siblings exist; avoid a third renamed copy.

**`G-2ae6e6631d0d54`** · UIKit · input-snapshot · unaided **fail** (primary pass). · **P1 grade-components** · real-model-gap · S3, S2

> I'm reviewing a UIKit change for iOS 26.0. The text has changed since validation started, but the old result is still applied. Can you preserve edits and reject that reply?

- **Diagnosis:** Ledger fail with primary pass: rejects the outdated snapshot but returns while busy stays true, so the form is stranded; the test checks the edit, not the request. Registered input-snapshot key was confirmed on the tvOS sibling (audit Q54).
- **Prompt:** Keep the question; it states a real reported symptom of the defective fixture.
- **Oracle:** Grade separately: stale reply rejected (primary), ownership state ends (busy false, no active ticket) after rejection, and proof that drives a native field change between submit and reply.
- **Skill:** Rejecting a stale reply must also release the request it owned (S3); the test must assert the resulting state (S2).
- **Transfer:** SwiftUI form with @State text and an injected validator.

**`G-2cf7d4ec0d00de`** · UIKit · cursor-restart · unaided **pass** (primary pass). · **P2 pair-variant** · no-headroom · S3, S6

> I'm reviewing a UIKit change for iOS 26.0. After editing the document, the next search jump continues from an unrelated old location. Can you define a safe restart?

- **Diagnosis:** Ledger pass: stale cursor ignored on restart. Opening asserts the jump symptom and asks for a 'safe restart', naming the remedy class.
- **Prompt:** Add a working twin and ask where the next jump lands after an edit, without asserting it is wrong.
- **Proposed wording:** iOS 26.0, UIKit. A reader holds a search result at offset 120, then the document is edited and becomes shorter. Where does the next rotor jump land in this implementation?
- **Oracle:** Assert the first match in the new revision (or documented restart point) and that the old cursor is not used; no-change on the twin.
- **Skill:** Cursor ownership across revisions is S3; restart offsets are S6 units.
- **Transfer:** macOS NSTextView custom rotor with the same revision contract.

**`G-333de6e92ef584`** · UIKit · dismiss-reentry · unaided **fail** (primary fail). Blind audit Q57: pass/pass. · **P0 split-criteria** · oracle-mismatch · S4, S1

> I'm reviewing a UIKit change for iOS 26.0. A dismissal callback can reenter the close path while the first transition is unfinished. How can we avoid restoring twice?

- **Diagnosis:** Audit Q57 regrades pass/pass: the answer correctly explains why closing twice cannot restore twice; the fixture instead removes dismissal permission, which the question never mentions. Factorial children reentry and dismiss-permission both stayed whole-fail/primary-pass in all arms.
- **Prompt:** Split duplicate completion from dismissal permission into two questions, each with its own oracle.
- **Proposed wording:** iOS 26.0, UIKit. Close can be requested again during a dismissal animation, and its completion can arrive twice. With an eligible return target, when and how many times should the panel request restoration? ‖ iOS 26.0, UIKit. This panel sometimes must not be dismissed, for example while a save is in progress. What happens today when someone presses Close or performs the accessibility escape gesture in that state?
- **Oracle:** Q1: one transition, no early request, exactly one completion-time restoration carrying the target. Q2: with dismissal forbidden, Close and escape both leave the panel open and send nothing. Record regrade of the frozen fail.
- **Skill:** Restore-after-completion is S4; the permission guard must be traced on the actual paths (S1).
- **Transfer:** macOS sheet with cancelOperation and a shouldClose delegate.

**`G-3bad84db2e37fb`** · UIKit · rebound-action · unaided **pass** (primary pass). Pair: fixes-defect-breaks-working. · **P1 rewrite-neutral** · no-headroom · S3, S2

> I'm reviewing a UIKit change for iOS 26.0. After refreshing a row, an action captured earlier can operate on the wrong record. Can you repair the ownership without losing the current action?

- **Diagnosis:** Ledger pass; pair fixes-defect-breaks-working with G-a1aff76682fe0a. Asserted ownership defect gives the fix.
- **Prompt:** Adopt the factorial captured-action wording for both versions.
- **Proposed wording:** iOS 26.0, UIKit. After the same view is reconfigured, what happens if a client retains and invokes the old accessibility shortcut? The ordinary buttons should operate on the currently displayed item.
- **Oracle:** Keep call-count and ID assertions; require the retained installed action, not a re-created one.
- **Skill:** Captured identity validated at invocation is S3; driving the installed action is S2.
- **Transfer:** macOS and tvOS siblings exist.

**`G-3c2fdfe7b1bb3f`** · UIKit · custom-action-name · unaided **pass** (primary pass). · **P2 pair-variant** · no-headroom · S1, S2

> I'm reviewing a UIKit change for iOS 26.0. The two named shortcuts on this card should invoke different commands. Could you check the names and what each one actually calls?

- **Diagnosis:** Ledger pass: keeps named independent actions and removes the duplicate invocation. Question is already a neutral check ('what each one actually calls'), but only the defective fixture exists.
- **Prompt:** Keep the wording and add a working fixture so the neutral question is graded on both.
- **Oracle:** On the working twin, expected answer is no change with the decisive dispatch path shown; drive each installed action handler and assert the single command it calls.
- **Skill:** Neutral question plus twin tests S1 tracing and S2 handler-level proof.
- **Transfer:** SwiftUI accessibilityActions on a card with two named actions.

**`G-3f131f02a1e59a`** · UIKit · request-generation · unaided **pass** (primary pass). Pair: both-correct. · **P3 keep-control** · good-as-is · S3

> I'm reviewing a UIKit change for iOS 26.0. A late response from an earlier request overwrites a newer result. Can you give the current request ownership of the update?

- **Diagnosis:** Ledger pass; pair both-correct. Good matched benchmark.
- **Prompt:** none
- **Oracle:** none
- **Skill:** Latest request owns the update (S3).
- **Transfer:** Nine siblings exist.

**`G-471867cfc77618`** · UIKit · contrast-linear · unaided **pass** (primary pass). Pair: fixes-defect-breaks-working. · **P2 rewrite-neutral** · no-headroom · S2

> I'm reviewing a UIKit change for iOS 26.0. The contrast report for midtones disagrees with the design team's luminance calculation. Can you correct the computation?

- **Diagnosis:** Ledger pass with numeric luminance and ratio checks. Pair partner's failure was overturned by audit Q53, so this pair is likely both-correct; the asserted 'correct the computation' still gives the fix away.
- **Prompt:** Ask for the reported value under a named specification, with the same wording on both versions.
- **Proposed wording:** iOS 26.0, UIKit. Our design team uses the WCAG 2.2 relative-luminance definition. For mid-gray UIColor(white: 0.5, alpha: 1) on white, what luminance and contrast ratio does this utility report?
- **Oracle:** Keep the numeric midtone assertion with literal expected values; grade explanation of the transfer function separately.
- **Skill:** Literal expected luminance is the S2 standard this item already meets.
- **Transfer:** tvOS focus-state color check with the same WCAG formula.

**`G-4ad97fa054cee9`** · UIKit · container-order · unaided **pass** (primary pass). · **P2 pair-variant** · no-headroom · S1

> I'm reviewing a UIKit change for iOS 26.0. Reordering the children should update their navigation order without changing the surviving objects. Does this implementation do that?

- **Diagnosis:** Ledger pass: reorder assigns the new order and identity survives. The question is already neutral (asks whether it works) but the only fixture is defective, so no-change behavior is untested.
- **Prompt:** Add the working fixture under the same wording; the current question can stay.
- **Oracle:** On the working twin, expected answer is no change with the identity-preserving path shown; on the defect, the existing identity test.
- **Skill:** A working twin under the same neutral wording measures S1 restraint.
- **Transfer:** SwiftUI list with accessibilitySortPriority after reorder.

**`G-4be0839bf07362`** · UIKit · preserve-traits · unaided **pass** (primary pass). · **P2 pair-variant** · no-headroom · S5

> I'm reviewing a UIKit change for iOS 26.0. Marking an item selected seems to remove information it had before. Can we update selection without disturbing its other properties?

- **Diagnosis:** Ledger pass: alters selected membership without erasing other traits. Asserted 'seems to remove information'.
- **Prompt:** Add a working twin and ask for the trait set across selection changes.
- **Proposed wording:** iOS 26.0, UIKit. This favorite button is already a button with a header trait for its section. When it becomes selected and then unselected, which accessibility traits does it have at each step?
- **Oracle:** Assert the exact trait set after each transition on both twins.
- **Skill:** Selected-state representation is an S5 platform fact.
- **Transfer:** tvOS siblings exist; transfer to SwiftUI accessibilityAddTraits/removeTraits.

**`G-4c24f67bd656f2`** · UIKit · obsolete-rotor · unaided **pass** (primary pass). · **P2 pair-variant** · no-headroom · S3

> I'm reviewing a UIKit change for iOS 26.0. A previously retained navigation shortcut still moves through the document after the query changes. Can you prevent old searches affecting the new one?

- **Diagnosis:** Ledger pass: rejects rotor callbacks from another revision or snapshot. Asserted symptom with the fix class implied.
- **Prompt:** Add a working twin and ask what a retained rotor returns after the query changes.
- **Proposed wording:** iOS 26.0, UIKit. A client keeps the rotor object from a search for “tax”, then the query changes to “fee”. What does invoking the old rotor return now?
- **Oracle:** Assert the retained rotor returns nil or no result and the new rotor returns the literal new phrase.
- **Skill:** Old rotor must validate its query revision when invoked (S3).
- **Transfer:** macOS NSAccessibilityCustomRotor retained by a client.

**`G-5bb3417dbce54f`** · UIKit · disabled-action · unaided **pass** (primary pass). · **P2 pair-variant** · no-headroom · S2

> I'm reviewing a UIKit change for iOS 26.0. A disabled command can still run through another activation path. Can you make the control respect its current enabled state?

- **Diagnosis:** Ledger pass with both disabled and enabled callback assertions. Same opening as G-0c0e259e645a5f on a different fixture; asserted defect again.
- **Prompt:** Add a working container twin and ask what accessibilityActivate does while disabled.
- **Proposed wording:** iOS 26.0, UIKit. When this container's command is disabled, what does accessibilityActivate return and does the handler run? What happens after it is enabled again?
- **Oracle:** Assert return value and handler count in both states on both twins.
- **Skill:** Exercising the actual activation method is S2.
- **Transfer:** SwiftUI button with .disabled and an accessibilityAction.

**`G-5d8cd18f224228`** · UIKit · notification-kind · unaided **pass** (primary pass). · **P2 pair-variant** · no-headroom · S8

> I'm reviewing a UIKit change for iOS 26.0. The screen sends the same accessibility notification for changes with different navigation consequences. Can you select the appropriate request without resetting unrelated state?

- **Diagnosis:** Ledger pass: routes the target through layout-change. Opening explains the defect in abstract terms and asks to select the right request.
- **Prompt:** Add a working twin and ask which notification each change sends and where focus should be afterward.
- **Proposed wording:** iOS 26.0, UIKit. This screen sometimes reveals a new section and sometimes replaces the whole content. Which accessibility notification does each change send, and what element does it pass?
- **Oracle:** Assert notification kind and argument per change; no change on the twin.
- **Skill:** Choosing the minimal correct request without resetting unrelated state is S8 restraint.
- **Transfer:** macOS NSAccessibility.post with layoutChanged vs. focusedUIElementChanged.

**`G-60133c52c4694a`** · UIKit · unavailable-media · unaided **fail** (primary pass). · **P2 grade-components** · evidence-only · S2

> I'm reviewing a UIKit change for iOS 26.0. Opening the inspector before an item arrives says there are no accessible tracks. Can we distinguish not loaded from a successful empty result?

- **Diagnosis:** Ledger fail with primary pass: nil input correctly returns unavailable, but the proposed equality assertion needs GroupEvidence equality the supplied enum lacks, so the proof does not compile.
- **Prompt:** Keep the question; it states a real observable distinction.
- **Oracle:** Grade primary behavior separately from a non-compiling test; evidence credit requires a pattern match or a stated Equatable conformance.
- **Skill:** A proof that does not compile is the S2 failure.
- **Transfer:** tvOS and macOS siblings passed; no new transfer needed.

**`G-67ab870ea1d446`** · UIKit · contrast-space · unaided **pass** (primary pass). · **P2 pair-variant** · no-headroom · S1

> I'm reviewing a UIKit change for iOS 26.0. Our contrast utility gets different answers for equivalent colors in different color spaces. Can you make comparisons consistent?

- **Diagnosis:** Ledger pass: converts to sRGB before the formula. Opening names the inconsistency and asks to make it consistent, so this is an easy, stated fix.
- **Prompt:** Add a working twin and ask what two equivalent colors in different spaces report.
- **Proposed wording:** iOS 26.0, UIKit. A designer supplies the same red in Display P3 and extended linear sRGB. What contrast ratio against white does this utility report for each?
- **Oracle:** Assert equal ratios within tolerance for the equivalent inputs; no-change expected on the twin.
- **Skill:** Twin tests tracing the conversion path.
- **Transfer:** macOS NSColorSpace conversion with genericRGB input.

**`G-68d21f69f56390`** · UIKit · range-coordinate · unaided **pass** (primary pass). Pair: fixes-defect-breaks-working. · **P1 rewrite-neutral** · no-headroom · S6

> I'm reviewing a UIKit change for iOS 26.0. Navigation to a phrase works for plain English but lands on the wrong text after emoji. Can you repair it without changing the displayed text?

- **Diagnosis:** Ledger pass: accumulates UTF-16 offsets and tests a match after multicode-unit text. Pair partner G-e24e3f394ea182 broke the working version, so the asserted symptom is the confound.
- **Prompt:** Same neutral factorial wording on both versions.
- **Proposed wording:** iOS 26.0, UIKit. In this UIKit reader, search for “cat” in “😀 cat!”. What text range will the rotor return, and can people still select ordinary text in the reader?
- **Oracle:** Keep native-range assertion; require text(in:) equals a literal rather than comparing offsets from the same algorithm.
- **Skill:** UTF-16 boundary units are S6.
- **Transfer:** macOS NSTextView sibling.

**`G-6a9722a7fdfd4f`** · UIKit · edited-matches · unaided **pass** (primary pass). · **P1 rewrite-neutral** · no-headroom · S1, S6

> I'm reviewing a UIKit change for iOS 26.0. Editing the text outside our search callback leaves old search hits active. Can you make navigation use the current content?

- **Diagnosis:** Ledger pass: recomputes matches from current text and checks the shifted location. The opening states the stale-hits symptom and asks to use current content, so the fix is given.
- **Prompt:** Ask where the next jump lands after an external edit, with the same wording for a working twin.
- **Proposed wording:** iOS 26.0, UIKit. Our reader keeps search matches for highlighted phrases. If the text is replaced by code outside the search callback, for example a sync merge that inserts a paragraph before the second match, where does the next rotor jump land?
- **Oracle:** Assert the jump lands on the literal shifted phrase via text(in:) in the current document; no-change on a working twin.
- **Skill:** Tracing which text the matches come from is S1; checking the landing by literal substring is S6.
- **Transfer:** macOS NSTextView rotor with NSTextStorage edits from a collaborator.

**`G-6ebcc0fdd7d948`** · UIKit · observer-stop · unaided **pass** (primary pass). · **P2 pair-variant** · no-headroom · S2

> I'm reviewing a UIKit change for iOS 26.0. An observer keeps reacting after the screen stops listening. Can you make teardown and a subsequent restart reliable?

- **Diagnosis:** Ledger pass: releases observation and tests refresh across stop/restart. Asserted symptom, no working twin.
- **Prompt:** Add a working twin and ask what happens when the setting changes after stop and after restart.
- **Proposed wording:** iOS 26.0, UIKit. After this screen calls stop(), the Reduce Motion setting changes; later it calls start() and the setting changes again. What does the screen's motion state show at each step?
- **Oracle:** Assert no update after stop and an update after restart via a posted notification.
- **Skill:** Posting the real notification and asserting state is S2.
- **Transfer:** tvOS siblings exist; transfer to a SwiftUI onReceive publisher with cancellation.

**`G-6f19bb8fa70065`** · UIKit · shortcut-dispatch · unaided **fail** (primary pass). Pair: misses-defect-keeps-working. · **P0 repair-oracle** · oracle-mismatch · S2

> I'm reviewing a UIKit change for iOS 26.0. The named shortcut appears, but tapping it does not run the intended callback. What should change?

- **Diagnosis:** Ledger fail with primary pass looks like a grading error: the answer restores onArchive and its test expects a second invocation to return false with no callback, which is exactly what the reference test asserts (second handler call false, calls stays 1).
- **Prompt:** Keep the question; add a working twin pairing only after regrading.
- **Oracle:** Regrade against the reference: first invocation true with one callback, second false with no further callback. Treat the answer as pass; correct the pair outcome to both-correct.
- **Skill:** The answer's handler-level assertions match S2; the grade penalized correct proof.
- **Transfer:** SwiftUI accessibilityAction with an idempotent archive.

**`G-745f480b2ed202`** · UIKit · table-span · unaided **pass** (primary pass). Pair: both-correct. · **P3 keep-control** · good-as-is · S2

> I'm reviewing a UIKit change for iOS 26.0. A merged table cell occupies several coordinates. When users explore the table by coordinate, does each covered position resolve to the right cell?

- **Diagnosis:** Ledger pass; pair both-correct with the same neutral question.
- **Prompt:** none
- **Oracle:** none
- **Skill:** Tests covered and uncovered coordinates.
- **Transfer:** macOS sibling.

**`G-7f4c68cfc691a3`** · UIKit · stale-timeline · unaided **pass** (primary pass). · **P2 pair-variant** · no-headroom · S2

> I'm reviewing a UIKit change for iOS 26.0. The previous timeline remains visible when information for the next item is unavailable. Can you correct the state transition?

- **Diagnosis:** Ledger pass: clears obsolete progress and tests the unavailable transition. Asserted symptom, no working twin.
- **Prompt:** Add a working twin and ask what the timeline shows after moving from a 3-minute item to one with unknown duration.
- **Proposed wording:** iOS 26.0, UIKit. The player moves from a 3-minute episode to an item whose duration is not available yet. What do the timeline and its accessibility value show for the second item?
- **Oracle:** Assert hidden or disabled timeline and cleared value after the transition.
- **Skill:** Asserting the observable cleared state is S2.
- **Transfer:** tvOS transport bar.

**`G-80d358230060b6`** · UIKit · selected-state · unaided **pass** (primary pass). · **P3 retire-duplicate** · duplicate · S5

> I'm reviewing a UIKit change for iOS 26.0. The old row can still be described as selected after the selection moves. Can you make both rows reflect the current selection?

- **Diagnosis:** Ledger pass: removes selected state and checks the deselected accessory. Third iOS copy of the selected-state decision with the same opening.
- **Prompt:** Retire; the reuse-v1 pair carries this decision.
- **Oracle:** none
- **Skill:** Same selected-state decision.
- **Transfer:** n/a

**`G-81ab6c7ec4506f`** · UIKit · container-children · unaided **pass** (primary pass). · **P2 pair-variant** · no-headroom · S1

> I'm reviewing a UIKit change for iOS 26.0. A tester can reach the row but not all its individual controls. Can you preserve the grouping and still let people operate the children?

- **Diagnosis:** Ledger pass: clears descendant hiding while keeping the card a non-element. Same opening as G-dd75bbabea3b9b on a different fixture; the opening names the defect, so no headroom.
- **Prompt:** Give this naming-v1 card a working twin and the neutral row question, so the decision is tested once per fixture rather than as two asserted repairs.
- **Proposed wording:** iOS 26.0, UIKit. This card shows a title and two buttons. When VoiceOver moves through the card, which elements can a person reach and activate? Keep the card's grouping and both buttons' actions.
- **Oracle:** Assert reachable elements and independent button actions on both twins; on the working twin, any new grouping code is rework.
- **Skill:** Neutral twin measures whether the answer traces the hiding flag rather than accepting the reported symptom.
- **Transfer:** tvOS focusable card with two buttons inside a focus group.

**`G-8214d265d2ab74`** · UIKit · buffer-readiness · unaided **pass** (primary pass). · **P2 pair-variant** · no-headroom · S1

> I'm reviewing a UIKit change for iOS 26.0. Our report calls the player ready just because its buffer is full. How should we expose the available status without promising playback?

- **Diagnosis:** Ledger pass: buffer fullness and likely-to-keep-up stay independent. The opening names the faulty inference outright, so the pass shows only that the stated fix is easy.
- **Prompt:** Author a working twin where readiness already uses the keep-up flag and give both versions one neutral question about what the report says for a full buffer that is not predicted to keep up.
- **Proposed wording:** iOS 26.0, UIKit. Our player report shows a status line. When the buffer is full but playback is not predicted to keep up, what does this report say, and what does it say when both are true?
- **Oracle:** Score the reported status for the two flag combinations; on the working twin, no change is the expected answer and added fields count as rework.
- **Skill:** A neutral twin tests whether the answer traces the existing status path instead of applying the named fix.
- **Transfer:** A tvOS playback diagnostics overlay with an injected player-state snapshot rather than an AVPlayerItem.

**`G-82d48de9021508`** · UIKit · player-controls · unaided **pass** (primary pass). Pair: both-correct. · **P3 keep-control** · good-as-is · S8

> I'm reviewing a UIKit change for iOS 26.0. Can users still operate the player's built-in controls and keep automatic media selection?

- **Diagnosis:** Ledger pass; pair both-correct with the same neutral question.
- **Prompt:** none
- **Oracle:** none
- **Skill:** Native control preservation under a neutral question.
- **Transfer:** macOS AVPlayerView controlsStyle.

**`G-840924fec7426a`** · UIKit · range-coordinate · unaided **fail** (primary fail). Blind audit Q38: fail/fail. Pair: both-fail. · **P0 rewrite-neutral** · real-model-gap · S6, S2

> I'm reviewing a UIKit change for iOS 26.0. Navigation to a phrase works for plain English but lands on the wrong text after emoji. Can you repair it without changing the displayed text?

- **Diagnosis:** Confirmed range-coordinate gap (audit Q38 fail/fail): recognizes the +1 error but switches to Character distances; after emoji the range still misses, and the test compares offsets from the same wrong algorithm. Factorial text-range-38 kept primary in all arms; UIKit text note added nothing.
- **Prompt:** Use the neutral factorial wording shared with its working twin G-8eafbd1521124e.
- **Proposed wording:** iOS 26.0, UIKit. In this UIKit reader, search for “cat” in “😀 cat!”. What text range will the rotor return, and can people still select ordinary text in the reader?
- **Oracle:** Require text(in: returnedRange) == “cat” with the reader as target; grade evidence separately since self-referential offset comparisons certified wrong text.
- **Skill:** S6 offset units plus an S2 literal check would have caught the wrong conversion.
- **Transfer:** macOS NSTextView with combining marks.

**`G-895e740bc6ddd9`** · UIKit · refresh-name · unaided **fail** (primary fail). Blind audit Q24: fail/pass. Pair: both-fail. · **P0 split-criteria** · bundled-criteria · S1, S8

> I'm reviewing a UIKit change for iOS 26.0. A control keeps the old accessible name after its content changes. Can you update the same control rather than replace it?

- **Diagnosis:** Audit Q24 regrades primary pass: the name already refreshes; the answer adds a focus-affecting notification and clears the ordinary status, while the hidden check silently requires that status. Factorial current-order child stayed F/P in all arms.
- **Prompt:** Separate name refresh from status-value policy so each has a stated requirement.
- **Proposed wording:** iOS 26.0, UIKit. The same visible cell changes from a priority order for Ana to an ordinary order for Ben without dequeuing. What accessible name does it expose after each configuration? ‖ iOS 26.0, UIKit. Ordinary orders show a status such as “Preparing” and priority orders show “Rush”. After reconfiguring the same cell from priority to ordinary, what accessibility value does it expose, and does anything request a focus move?
- **Oracle:** Q1: assert current name per configuration. Q2: assert the literal ordinary status value and that no focus notification is posted. Record regrade of primary.
- **Skill:** Name already works (S1); unrequested notification and value clearing are S8.
- **Transfer:** tvOS reused cell sibling exists.

**`G-95a1329932a335`** · UIKit · optional-help · unaided **pass** (primary pass). · **P3 retire-duplicate** · duplicate · S1

> I'm reviewing a UIKit change for iOS 26.0. After switching from an item with help text to one without it, the old help is still there. Can you repair the update path?

- **Diagnosis:** Ledger pass: clears obsolete hints when the error disappears. UIKit preferences fixture shares the SwiftUI items' opening; third copy of the decision on iOS.
- **Prompt:** Retire as a third iOS copy of the optional-help decision; G-9416f59bb20a37/G-c93c93db07f19f already form a both-correct pair.
- **Oracle:** none
- **Skill:** Same nil-help decision as the retained pair.
- **Transfer:** n/a

**`G-9729c3a5d9babf`** · UIKit · design-font · unaided **inconclusive** (primary inconclusive). · **P1 specify-policy** · grader-uncertain · S2, S5

> I'm reviewing a UIKit change for iOS 26.0. Our design font is supposed to follow the text size setting. The typeface and size should both survive repeated updates. What would you change?

- **Diagnosis:** Ledger inconclusive: scales through UIFontMetrics but ignores the label's own trait collection; whether a local trait override must win is unspecified, so the grader could not decide.
- **Prompt:** State which trait environment governs the font so the override case has an answer.
- **Proposed wording:** iOS 26.0, UIKit. Our design font should follow the text size setting, including when this screen overrides the content size category for a preview. The typeface and size should both survive repeated updates. What does this label show at the override size after three updates?
- **Oracle:** Assert typeface name and point size against UIFontMetrics(forTextStyle:) scaled for the label's effective traits, after repeated updates, with a literal expected size per category.
- **Skill:** Needs the precise trait-collection fact (S5) and a literal size assertion (S2).
- **Transfer:** tvOS label with a brand font and preferred-font fallback.

**`G-97d21d3f2d3a4e`** · UIKit · contrast-alpha · unaided **pass** (primary pass). Blind audit Q18: pass/pass. · **P2 pair-variant** · no-headroom · S2

> I'm reviewing a UIKit change for iOS 26.0. Our contrast tool is only supposed to grade opaque pairs. A translucent pair gets a numeric result. What would you change?

- **Diagnosis:** Ledger and audit Q18 pass: rejects translucency on either operand in the shared resolver and tests the foreground case. The opening states both the policy and the wrong result, so the pass shows the fix is easy once named.
- **Prompt:** Keep the stated opaque-only policy (a legitimate product fact) but replace the symptom with a question about a specific translucent input, and add a working twin.
- **Proposed wording:** iOS 26.0, UIKit. Our contrast tool grades opaque text/background pairs only. What does it return for a 50%-alpha foreground on white, and for an opaque foreground on a 50%-alpha background?
- **Oracle:** Check both operands; the audit noted only the foreground case was tested, so require a background-translucency assertion for full evidence credit.
- **Skill:** Audit shows the test covered one of two operands; S2 asks for the requested observable effect on both.
- **Transfer:** macOS NSColor contrast checker with catalog colors.

**`G-9bc22c52023c4b`** · UIKit · presentation-owner · unaided **pass** (primary pass). · **P3 keep-control** · good-as-is · S3, S4

> I'm reviewing a UIKit change for iOS 26.0. A delayed close callback can restore focus for a presentation that has already been replaced. Can you fix that race?

- **Diagnosis:** Ledger pass: validates closing state and generation before a delayed completion. macOS preservation sibling failed, so this guards a behavior with headroom.
- **Prompt:** none
- **Oracle:** none
- **Skill:** Delayed completion must validate its presentation (S3) before restoring focus (S4).
- **Transfer:** macOS and tvOS siblings exist.

**`G-9dc2d664c3baca`** · UIKit · redundant-notification · unaided **fail** (primary pass). · **P2 specify-policy** · ambiguous-policy · S1

> I'm reviewing a UIKit change for iOS 26.0. Reapplying an unchanged value generates another change event. Can we notify once for a real transition?

- **Diagnosis:** Ledger fail with primary pass: notifications are suppressed, but select(_:) now returns false for an unchanged valid rate and the answer's test enshrines that. The reference returns true; the question never states what the Bool means.
- **Prompt:** State the return-value contract so changing it is a measurable preservation failure rather than a hidden rule.
- **Proposed wording:** iOS 26.0, UIKit. select(_:) returns true when the rate is accepted and false only for disabled or unsupported rates; callers rely on that. Reapplying the current rate sends another onChange. Can we notify once per real transition?
- **Oracle:** Grade notification count (primary) separately from the return-value contract; keep the reference assertion select(1) == true for the current rate.
- **Skill:** Preserving the existing accept contract while fixing notification is S1 tracing of the path.
- **Transfer:** macOS segmented control with the same accept/notify split.

**`G-9fba8b4af646cb`** · UIKit · speed-metadata · unaided **pass** (primary pass). Pair: both-correct. · **P3 keep-control** · good-as-is · S5

> I'm reviewing a UIKit change for iOS 26.0. The speed control changes playback but continues to describe the previous setting. Can you synchronize the displayed and accessible state?

- **Diagnosis:** Ledger pass; pair both-correct.
- **Prompt:** none
- **Oracle:** none
- **Skill:** Selected-state wording on the current speed is S5.
- **Transfer:** tvOS speed picker.

**`G-a046527edefa4f`** · UIKit · overlap-policy · unaided **pass** (primary pass). · **P2 pair-variant** · no-headroom · S6

> I'm reviewing a UIKit change for iOS 26.0. Our search offers an overlapping-matches option, but the navigation stops look identical with it on and off. Can you fix the search?

- **Diagnosis:** Ledger pass: progression follows the overlap flag with overlapping and nonoverlapping tests. The opening's observable symptom is good, but the request 'fix the search' presumes a defect.
- **Prompt:** Add a working twin and ask what stops are produced with the option on and off for a concrete string.
- **Proposed wording:** iOS 26.0, UIKit. Searching “aaa” for “aa”: what rotor stops does this reader produce with the overlapping-matches option on, and with it off?
- **Oracle:** Assert literal ranges {0,2},{1,2} with overlap and {0,2} without, read back with text(in:).
- **Skill:** Range offsets checked by literal substring are S6.
- **Transfer:** macOS NSTextView rotor with the same option.

**`G-a07f13e8f28127`** · UIKit · modal-state · unaided **pass** (primary pass). Pair: both-correct. · **P3 keep-control** · good-as-is · S4

> I'm reviewing a UIKit change for iOS 26.0. When a panel closes the background doesn't always return to its previous state. How should this screen handle opening and closing it more than once?

- **Diagnosis:** Ledger pass; pair both-correct with G-62d3cfbe4da970. A rare matched pair where both versions pass under the same asserted wording; useful as a regression benchmark.
- **Prompt:** none
- **Oracle:** none
- **Skill:** Restores the saved prior hidden value, part of S4.
- **Transfer:** macOS sheet with an already-hidden sidebar.

**`G-a40295c16e4820`** · UIKit · preserve-traits · unaided **pass** (primary pass). · **P3 retire-duplicate** · duplicate · S5

> I'm reviewing a UIKit change for iOS 26.0. Marking an item selected seems to remove information it had before. Can we update selection without disturbing its other properties?

- **Diagnosis:** Ledger pass: inserts selected without replacing button traits. Same opening as G-4be0839bf07362 on another fixture; two tvOS siblings too.
- **Prompt:** Retire as a duplicate of G-4be0839bf07362's decision.
- **Oracle:** none
- **Skill:** Same trait-preservation decision.
- **Transfer:** n/a

**`G-a4096250f11e36`** · UIKit · edit-action-stale · unaided **pass** (primary pass). · **P2 pair-variant** · no-headroom · S1

> I'm reviewing a UIKit change for iOS 26.0. An editor is now read-only. Can you check that its available actions and help change together?

- **Diagnosis:** Ledger pass: clears stale edit actions when editability is removed. Opening is mild but asks for the check on the defective fixture only.
- **Prompt:** Add a working twin; keep the question 'check that its actions and help change together'.
- **Oracle:** Assert custom actions, edit category and hint after read-only transition on both twins; no change on the working one.
- **Skill:** A twin makes the S1 trace measurable.
- **Transfer:** macOS NSTextView switching isEditable with accessibility custom actions.

**`G-b18da2b792890e`** · UIKit · text-size-change · unaided **pass** (primary pass). Pair: fixes-defect-breaks-working. · **P1 rewrite-neutral** · no-headroom · S1

> I'm reviewing a UIKit change for iOS 26.0. People who change their text-size setting while this screen is open don't get the expected update. Can the existing content respond in place?

- **Diagnosis:** Ledger pass; pair fixes-defect-breaks-working with G-9f59180da322fa (overturned by Q56). The broad wording made product scope ambiguous.
- **Prompt:** Same specified wording on both versions.
- **Proposed wording:** iOS 26.0, UIKit. The checkout total should support changing text size while the screen is open. Keep the Pay button appearance and action. Which prerequisites does this UIKit setup supply, and what can a unit check establish?
- **Oracle:** Keep adjustsFontForContentSizeCategory assertion on the total; check Pay unchanged.
- **Skill:** Same wording isolates S1.
- **Transfer:** Integration checkout-integrated covers transfer.

**`G-b60d57e22f1850`** · UIKit · edited-matches · unaided **pass** (primary pass). · **P2 pair-variant** · duplicate · S3, S6

> I'm reviewing a UIKit change for iOS 26.0. Editing the text outside our search callback leaves old search hits active. Can you make navigation use the current content?

- **Diagnosis:** Ledger pass: rechecks the live document before using cached positions. Same opening as G-6a9722a7fdfd4f on the edited-rotor fixture; second asserted copy of one decision.
- **Prompt:** Give this fixture a working twin under the neutral wording used for G-6a9722a7fdfd4f rather than a second asserted repair.
- **Proposed wording:** iOS 26.0, UIKit. Our reader keeps search matches for highlighted phrases. If the text is replaced by code outside the search callback, for example a sync merge that inserts a paragraph before the second match, where does the next rotor jump land?
- **Oracle:** Assert the stale cached search is rejected and a fresh search lands on the literal phrase.
- **Skill:** Cached results must validate the document revision when used (S3) and land by literal text (S6).
- **Transfer:** tvOS and macOS siblings exist; a transfer would use a SwiftUI TextEditor-backed rotor.

**`G-c3aa964dc0106d`** · UIKit · audio-description-tag · unaided **inconclusive** (primary pass). Pair: inconclusive. · **P2 repair-oracle** · grader-uncertain · S2

> I'm reviewing a UIKit change for iOS 26.0. The audio inspector calls ordinary language tracks described audio. How can we identify the marked options?

- **Diagnosis:** Ledger inconclusive with primary pass: the correct audio-description characteristic is used, but the only test depends on a media fixture and a nonempty option list, so the grader could not decide the whole answer.
- **Prompt:** Keep the question; it is identical to its working twin and already neutral enough.
- **Oracle:** Add a checkable criterion: given one option tagged with the describes-video characteristic and one untagged English option, only the tagged one is reported. Grade the implementation by inspection and the test separately; a test that can pass with zero options earns no evidence credit.
- **Skill:** The undecidable grade comes from a test with no positive fixture, which is exactly S2.
- **Transfer:** Inject option descriptors (language, characteristics) into the inspector so the positive and negative cases are constructible without AVAsset loading.

**`G-c93c93db07f19f`** · SwiftUI · optional-help · unaided **pass** (primary pass). Pair: both-correct. · **P3 keep-control** · good-as-is · S1

> I'm reviewing a SwiftUI change for iOS 26.0. After switching from an item with help text to one without it, the old help is still there. Can you repair the update path?

- **Diagnosis:** Ledger pass; pair both-correct. Asserted symptom but the working twin also holds on iOS.
- **Prompt:** none
- **Oracle:** none
- **Skill:** Paired control for nil help forwarding.
- **Transfer:** tvOS and macOS siblings exist.

**`G-cd9054649c37e3`** · UIKit · rebound-action · unaided **pass** (primary pass). · **P3 retire-duplicate** · duplicate · S3

> I'm reviewing a UIKit change for iOS 26.0. After refreshing a row, an action captured earlier can operate on the wrong record. Can you repair the ownership without losing the current action?

- **Diagnosis:** Ledger pass: generation check rejects a retained removal action. A third iOS copy of the rebound-action decision, which has ten siblings across platforms.
- **Prompt:** Retire; G-3bad84db2e37fb/G-a1aff76682fe0a carry the iOS pair.
- **Oracle:** none
- **Skill:** Same ownership decision.
- **Transfer:** n/a

**`G-cdecb4f2473a6b`** · UIKit · motion-policy · unaided **pass** (primary pass). Pair: fixes-defect-breaks-working. · **P1 rewrite-neutral** · no-headroom · S1

> I'm reviewing a UIKit change for iOS 26.0. The optional effect still plays when the person asks for reduced motion. Can we honor their setting without changing the normal experience?

- **Diagnosis:** Ledger pass; pair fixes-defect-breaks-working with G-ecf0c73499bcb3. Asserting the effect still plays primes a patch on the working twin.
- **Prompt:** Same neutral motion question on both versions.
- **Proposed wording:** iOS 26.0, UIKit. With Reduce Motion on and then off, what duration does this screen use for the optional effect, and what does a person see in each case? Keep the normal animation for people who have not asked for reduced motion.
- **Oracle:** Assert zero duration with Reduce Motion on and the ordinary duration otherwise, through the production transition path.
- **Skill:** Same wording across versions isolates S1.
- **Transfer:** macOS NSAnimationContext with accessibilityDisplayShouldReduceMotion.

**`G-d6b720273d9027`** · UIKit · removed-child · unaided **pass** (primary pass). Blind audit Q31: pass/pass. · **P2 pair-variant** · no-headroom · S3

> I'm reviewing a UIKit change for iOS 26.0. An item we've removed is still in the container's navigation list. Can you keep the list in sync without changing ordinary controls?

- **Diagnosis:** Ledger and audit Q31 pass: prunes the retained element and the remove/reinsert test distinguishes the old merge behavior. Asserted symptom, no working twin.
- **Prompt:** Add a working twin and ask what the navigation list contains after removing and re-adding an item.
- **Proposed wording:** iOS 26.0, UIKit. Remove item B from this container and later insert a new item with B's ID. What does the container expose in its navigation list after each step?
- **Oracle:** Assert exposed element identities after removal and reinsertion; buttons untouched.
- **Skill:** Stale element identity is S3 ownership.
- **Transfer:** SwiftUI ForEach with accessibilityElement(children:).

**`G-d95da35e90afc0`** · UIKit · edit-category · unaided **fail** (primary fail). Blind audit Q58: fail/fail. · **P0 keep-control** · real-model-gap · S5

> I'm reviewing a UIKit change for iOS 26.0. The editor can perform edits but the requested editing actions aren't in the intended category. Can you bring configuration and default behavior into agreement?

- **Diagnosis:** Confirmed registered gap (edit-category; audit Q58 fail/fail): identifies the missing category but uses a .edit spelling instead of UIAccessibilityCustomAction.editCategory; the test repeats the API error and omits the nil default.
- **Prompt:** none
- **Oracle:** Keep compile-level assertion on the SDK constant and an ordinary action's nil category.
- **Skill:** An exact SDK constant is the S5 on-demand platform fact.
- **Transfer:** SwiftUI accessibilityAction with category on iOS 26 for a text editor.

**`G-da89005c6d3613`** · UIKit · dismissal-completion · unaided **fail** (primary fail). Blind audit Q14: fail/fail. · **P0 keep-control** · real-model-gap · S4, S3

> I'm reviewing a UIKit change for iOS 26.0. Focus is requested as soon as Close is pressed, before dismissal finishes. How would you handle completion and cancellation?

- **Diagnosis:** Confirmed registered gap (dismissal-completion; audit Q14 fail/fail): keeps posting focus at Close and suppresses the completion post; a stale-operation check cannot move delivery after dismissal.
- **Prompt:** none
- **Oracle:** Keep the assertion that the notification is sent only from completion and to the current target; add a cancelled-dismissal case asserting no post.
- **Skill:** Focus restore must wait for completion (S4) and the completion must validate its operation (S3).
- **Transfer:** SwiftUI sheet onDismiss with AccessibilityFocusState and an injected completion.

**`G-dd75bbabea3b9b`** · UIKit · container-children · unaided **pass** (primary pass). Pair: fixes-defect-breaks-working. · **P1 rewrite-neutral** · no-headroom · S1

> I'm reviewing a UIKit change for iOS 26.0. A tester can reach the row but not all its individual controls. Can you preserve the grouping and still let people operate the children?

- **Diagnosis:** Ledger pass; pair fixes-defect-breaks-working with G-6c468546da6af4, whose failure the audit overturned (Q05). The asserted symptom works on the defect but primes edits on working code.
- **Prompt:** Use one neutral question for both fixture versions so the repair is credited for the causal trace, not the prompt's diagnosis.
- **Proposed wording:** iOS 26.0, UIKit. This settings row groups a title with two buttons. When VoiceOver moves through the row, which elements can a person reach and activate, and in what order? Keep the row's grouping and the buttons' callbacks.
- **Oracle:** Check exposed children order and both callbacks; grade the causal explanation (container exposes no children vs. ordered children) separately from the patch.
- **Skill:** Same wording on both versions isolates S1 tracing from prompt-supplied diagnosis.
- **Transfer:** macOS AppKit row exposing children through accessibilityChildren.

**`G-e27b662992867e`** · UIKit · refresh-name · unaided **pass** (primary pass). · **P3 keep-control** · good-as-is · S1

> I'm reviewing a UIKit change for iOS 26.0. A control keeps the old accessible name after its content changes. Can you update the same control rather than replace it?

- **Diagnosis:** Ledger pass: overwrites contextual names on every reuse. The cleanest of the iOS refresh-name items (no audit dispute).
- **Prompt:** none
- **Oracle:** none
- **Skill:** Updates the same control in place.
- **Transfer:** macOS and tvOS siblings exist.

**`G-ef26b0162ce47f`** · UIKit · language-match · unaided **inconclusive** (primary pass). · **P2 grade-components** · evidence-only · S2, S7

> I'm reviewing a UIKit change for iOS 26.0. When we ask for one language, this picker can select a different one. Fix matching without silently changing languages.

- **Diagnosis:** Ledger inconclusive, primary pass: uses the requested language and keeps the forced exclusion, but the test needs an unverified French fixture and helper.
- **Prompt:** Keep the question but drop the imperative 'Fix matching' in favor of asking what is selected for a requested language.
- **Oracle:** Grade the language match by inspection against an injected option list and grade the asset-dependent test as evidence separately; an unverified helper earns no evidence credit.
- **Skill:** Selection must be checked on the player item's actual choice (S7) with a constructible positive fixture (S2).
- **Transfer:** tvOS subtitle picker with region-tagged languages (fr-CA vs fr-FR).

#### iOS · preservation (22)

**`G-01c10c6a8573fa`** · SwiftUI · interop-rebind · unaided **fail** (primary pass). Blind audit Q41: fail/pass. Pair: fixes-defect-breaks-working. · **P1 grade-components** · rework-only · S1, S8, S2

> I'm reviewing a SwiftUI change for iOS 26.0. The wrapper updates its SwiftUI state but the native button can still send to the previous target. Can you fix the binding and teardown?

- **Diagnosis:** Audit Q41 confirms primary pass, whole fail: generation already silences the old button; the rewrite adds dual cleanup that could clear a newer binding and its negative-only test passes the original code.
- **Prompt:** Use the neutral interop wording shared with G-10cf3d04a66de0.
- **Proposed wording:** iOS 26.0, SwiftUI with UIKit interop. The wrapper updates from item A to item B and is later dismantled. If the native button sends its action after each step, which handler runs? Keep the same native button and its title.
- **Oracle:** Grade primary (old target silent, current dispatches), regression risk (teardown cannot clear a newer binding), rework, and evidence (require a positive current-dispatch assertion before asserting the old one is silent) separately.
- **Skill:** Existing revisions already answer the request (S1); extra cleanup is S8; a negative-only test is the S2 positive-fixture gap.
- **Transfer:** macOS NSViewRepresentable with target/action rebinding.

**`G-1c11378c112ef5`** · UIKit · audio-description-tag · unaided **pass** (primary pass). Pair: inconclusive. · **P3 keep-control** · good-as-is · S2, S8

> I'm reviewing a UIKit change for iOS 26.0. The audio inspector calls ordinary language tracks described audio. How can we identify the marked options?

- **Diagnosis:** Ledger pass: leaves the working characteristic check alone and separates ordinary from marked description audio; its optional test needs a named sample asset it never supplies. Pair is inconclusive only because the repair twin is ungraded, not because this control is weak.
- **Prompt:** none
- **Oracle:** Grade the proof separately: an asset-dependent test that can iterate zero options is evidence-only credit, not a positive demonstration of a tagged track.
- **Skill:** Passing control shows restraint on working AVFoundation metadata code; its asset-dependent test is the S2 positive-fixture weakness.
- **Transfer:** Use a tvOS or macOS inspector that receives option metadata through an injected value type, so a positive tagged track can be asserted without a bundled asset.

**`G-24ccdb855e595d`** · UIKit · multiline · unaided **fail** (primary pass). Blind audit Q48: fail/pass. Pair: fixes-defect-breaks-working. · **P1 grade-components** · rework-only · S1, S8

> I'm reviewing a UIKit change for iOS 26.0. When a delivery option wraps to a second line in translation, part of the name disappears. Can you fix the row without shortening the text?

- **Diagnosis:** Audit Q48 confirms primary pass, whole fail: the cell already wraps, disables shrinking and self-sizes; required compression priorities and a test of the priority choice are unsubstantiated additions.
- **Prompt:** Use the neutral layout question shared with G-1cacc76921ce33.
- **Proposed wording:** iOS 26.0, UIKit. At accessibility text sizes a translated delivery-option name needs two or three lines. How does this cell lay out that name today, and is any of it truncated or shrunk? Keep the full wording.
- **Oracle:** Grade primary (numberOfLines 0, no shrink, self-sizing kept), rework (added constraints or width management) and evidence (a test of the chosen priority is not evidence of fit) separately.
- **Skill:** The existing multiline policy answers the request (S1); added layout constraints are S8.
- **Transfer:** SwiftUI row with lineLimit(nil) and fixedSize(horizontal:false, vertical:true).

**`G-2cd9bf59a7950d`** · UIKit · player-controls · unaided **pass** (primary pass). Pair: both-correct. · **P3 keep-control** · good-as-is · S8, S7

> I'm reviewing a UIKit change for iOS 26.0. Can users still operate the player's built-in controls and keep automatic media selection?

- **Diagnosis:** Ledger pass; pair both-correct with a neutral question. Retains native controls and automatic media selection.
- **Prompt:** none
- **Oracle:** none
- **Skill:** Keeping native player controls is S8; automatic media selection is S7.
- **Transfer:** tvOS AVPlayerViewController sibling.

**`G-3728319099e01c`** · UIKit · selected-state · unaided **fail** (primary fail). Blind audit Q04: fail/pass. Pair: fixes-defect-breaks-working. · **P1 grade-components** · rework-only · S1, S5, S8

> I'm reviewing a UIKit change for iOS 26.0. The old row can still be described as selected after the selection moves. Can you make both rows reflect the current selection?

- **Diagnosis:** Audit Q04 regrades primary pass (ledger had fail/fail): both trait branches are correct; the answer couples saved state to collection selection, changing an independent UIKit state the code already handles.
- **Prompt:** Adopt the neutral selected-state question for both versions, naming the independent collection selection.
- **Proposed wording:** iOS 26.0, UIKit. In this list, the saved marker moves from row A to row B while both cells stay on screen and neither is dequeued. Afterward, what does each row expose as its saved state, and what happens to its other traits, its collection selection and its button action?
- **Oracle:** Grade trait correctness (primary), collection-selection preservation (regression) and rework separately; record the primary regrade.
- **Skill:** Trait already correct (S1); saved vs. selected wording is S5; coupling extra state is S8.
- **Transfer:** tvOS collection view with focus vs. selection.

**`G-458042d0f6f06f`** · UIKit · refresh-name · unaided **fail** (primary pass). Blind audit Q01: fail/pass. Pair: both-fail. · **P1 grade-components** · rework-only · S1, S8

> I'm reviewing a UIKit change for iOS 26.0. A control keeps the old accessible name after its content changes. Can you update the same control rather than replace it?

- **Diagnosis:** Audit Q01 confirms primary pass, whole fail: both label branches and the value already refresh on the same cell; posting on every configure can redirect focus during reuse. Pair both-fail with Q24.
- **Prompt:** Adopt the factorial current-order wording, which states the focus constraint.
- **Proposed wording:** iOS 26.0, UIKit. The same visible cell changes from a priority order to an ordinary order without dequeuing. Both need their current customer name and current order status. Can you check those updates without moving focus?
- **Oracle:** Grade name and status refresh (primary), unsolicited focus requests (regression), and rework separately.
- **Skill:** The cell already refreshes (S1); the added notification is S8.
- **Transfer:** tvOS reused cell sibling exists.

**`G-55fe2bf3aeec99`** · UIKit · contrast-linear · unaided **fail** (primary pass). Blind audit Q53: pass/pass. Pair: fixes-defect-breaks-working. · **P0 repair-oracle** · oracle-mismatch · S1

> I'm reviewing a UIKit change for iOS 26.0. The contrast report for midtones disagrees with the design team's luminance calculation. Can you correct the computation?

- **Diagnosis:** Audit Q53 reverses the ledger: the recommendation and test keep piecewise sRGB and the correct midgray value; the gamma-2.2 diff is explicitly conditional on another specification. Pair label fixes-defect-breaks-working is therefore wrong for this fixture.
- **Prompt:** Replace the asserted disagreement with the neutral question shared with G-471867cfc77618 and state the governing specification.
- **Proposed wording:** iOS 26.0, UIKit. Our design team uses the WCAG 2.2 relative-luminance definition. For mid-gray UIColor(white: 0.5, alpha: 1) on white, what luminance and contrast ratio does this utility report?
- **Oracle:** Grade the primary recommendation for the supplied contract; treat an explicitly conditional alternative for a different specification as non-failing unless presented as the fix. Record regrade pass/pass.
- **Skill:** Correctly tracing and keeping the existing linearization is S1; the conditional alternative is not rework.
- **Transfer:** macOS NSColor calibrated vs. sRGB inputs with the same luminance contract.

**`G-62d3cfbe4da970`** · UIKit · modal-state · unaided **pass** (primary pass). Pair: both-correct. · **P3 keep-control** · good-as-is · S1

> I'm reviewing a UIKit change for iOS 26.0. When a panel closes the background doesn't always return to its previous state. How should this screen handle opening and closing it more than once?

- **Diagnosis:** Ledger pass; pair both-correct with G-a07f13e8f28127: concludes prior background hidden state is already captured and restored per presentation despite the asserted symptom.
- **Prompt:** none
- **Oracle:** none
- **Skill:** Holding a working path under an asserted symptom is the S1 behavior.
- **Transfer:** macOS and tvOS modal-state siblings already exist.

**`G-6b85a8fc52d837`** · UIKit · range-kind · unaided **fail** (primary pass). Blind audit Q52: fail/pass. Pair: fixes-defect-breaks-working. · **P1 grade-components** · rework-only · S1, S8

> I'm reviewing a UIKit change for iOS 26.0. The player says I can seek through an interval that was only buffered. How should the inspector describe these two ranges?

- **Diagnosis:** Audit Q52 confirms primary pass, whole fail: correctly explains and preserves separate seekable and buffered ranges, then declares an extra public query necessary despite the instruction to leave working code alone. Same pattern as Q16/Q60 on the other platforms.
- **Prompt:** Use the neutral range question shared with G-2a3677e01788e4 instead of asserting the player promises an unseekable interval.
- **Proposed wording:** iOS 26.0, UIKit. Our player has buffered 0–90 s of a stream, but only 0–60 s is currently seekable. What does this inspector report for each range, and what would it say about seeking to 75 s?
- **Oracle:** Grade primary (seekable vs. loaded kept distinct), rework (new public API on working code) and evidence separately.
- **Skill:** The existing inspector already answers (S1); an added helper is S8.
- **Transfer:** Keep one platform as the active copy; Q16 and Q60 already replicate this on macOS and tvOS.

**`G-6c468546da6af4`** · UIKit · container-children · unaided **fail** (primary fail). Blind audit Q05: pass/pass. Pair: fixes-defect-breaks-working. · **P0 repair-oracle** · oracle-mismatch · S1, S8

> I'm reviewing a UIKit change for iOS 26.0. A tester can reach the row but not all its individual controls. Can you preserve the grouping and still let people operate the children?

- **Diagnosis:** Audit Q05 reverses the ledger: blind whole/primary pass because the answer explicitly groups the two operable controls under a non-element stack and keeps both callbacks. The original rationale (title omitted) is not what the sample oracle tests; it checks dispatch only.
- **Prompt:** Replace the asserted symptom with the neutral question shared with G-dd75bbabea3b9b so the working fixture is not presented as broken.
- **Proposed wording:** iOS 26.0, UIKit. This settings row groups a title with two buttons. When VoiceOver moves through the row, which elements can a person reach and activate, and in what order? Keep the row's grouping and the buttons' callbacks.
- **Oracle:** State whether the title must remain an element; check the exposed accessibilityElements order and both callbacks separately, and record the regrade to pass/pass alongside the frozen count.
- **Skill:** The working fixture already exposes the children; credit for tracing that path is S1, unnecessary regrouping is S8.
- **Transfer:** A macOS AppKit preferences row using accessibilityChildren with a disclosure control.

**`G-8478a9d5e068a0`** · UIKit · shortcut-dispatch · unaided **pass** (primary pass). Blind audit Q11: pass/pass. Pair: misses-defect-keeps-working. · **P3 keep-control** · good-as-is · S1

> I'm reviewing a UIKit change for iOS 26.0. The named shortcut appears, but tapping it does not run the intended callback. What should change?

- **Diagnosis:** Ledger and audit Q11 pass: the final recommendation leaves the named shortcut and shared callback intact, though contradictory deliberation makes it hard to find. Pair label misses-defect-keeps-working depends on the partner grade, which looks wrong (see G-6f19bb8fa70065).
- **Prompt:** none
- **Oracle:** Grade clarity of the final recommendation separately from correctness if a usability component is added.
- **Skill:** Concluding the existing dispatch works is S1.
- **Transfer:** macOS NSAccessibilityCustomAction sibling.

**`G-8eafbd1521124e`** · UIKit · range-coordinate · unaided **fail** (primary fail). Blind audit Q46: fail/fail. Pair: both-fail. · **P0 rewrite-neutral** · real-model-gap · S6, S1, S2

> I'm reviewing a UIKit change for iOS 26.0. Navigation to a phrase works for plain English but lands on the wrong text after emoji. Can you repair it without changing the displayed text?

- **Diagnosis:** Confirmed range-coordinate gap (audit Q46 fail/fail; pair both-fail): working UTF-16 offsets are replaced with grapheme counts. Factorial text-range-46 with neutral wording kept primary in all four arms, so the asserted symptom induced the regression; whole still failed on the focused check.
- **Prompt:** Adopt the neutral factorial wording for both versions.
- **Proposed wording:** iOS 26.0, UIKit. In this UIKit reader, search for “cat” in “😀 cat!”. What text range will the rotor return, and can people still select ordinary text in the reader?
- **Oracle:** Drive the installed rotor and compare text(in: returnedRange) with the literal “cat”; grade primary, preserved selection and evidence separately (the factorial whole fails came from the check).
- **Skill:** Grapheme conversion at the UITextView boundary is S6; trusting the reported symptom is S1; the missing literal check is S2.
- **Transfer:** macOS NSTextView with combining marks and a CJK prefix.

**`G-9416f59bb20a37`** · SwiftUI · optional-help · unaided **pass** (primary pass). Pair: both-correct. · **P3 keep-control** · good-as-is · S1

> I'm reviewing a SwiftUI change for iOS 26.0. After switching from an item with help text to one without it, the old help is still there. Can you repair the update path?

- **Diagnosis:** Ledger pass; pair both-correct with G-c93c93db07f19f: keeps optional assignments and tests a second item with no hint despite the asserted symptom. macOS sibling preservation failed (audit Q22), so this iOS control holds a behavior that fails elsewhere.
- **Prompt:** none
- **Oracle:** none
- **Skill:** Holding the working nil-forwarding path under an asserted symptom is S1.
- **Transfer:** macOS sibling exists (Q22).

**`G-9f59180da322fa`** · UIKit · text-size-change · unaided **fail** (primary pass). Blind audit Q56: pass/pass. Pair: fixes-defect-breaks-working. · **P0 specify-policy** · ambiguous-policy · S1, S8

> I'm reviewing a UIKit change for iOS 26.0. People who change their text-size setting while this screen is open don't get the expected update. Can the existing content respond in place?

- **Diagnosis:** Audit Q56 regrades pass/pass: the total label already adapts, and the broad question also covers the visible Pay title, for which the answer gives a scoped alternative. The oracle tests label prerequisites and the payment callback, not Pay scaling. Factorial total-text kept primary in all arms.
- **Prompt:** Say which content must respond and which control's appearance must stay, as in the factorial wording.
- **Proposed wording:** iOS 26.0, UIKit. The checkout total should support changing text size while the screen is open. Keep the Pay button appearance and action. Which prerequisites does this UIKit setup supply, and what can a unit check establish?
- **Oracle:** Check body-style scalable font, adjustsFontForContentSizeCategory, wrapping and flexible height on the total; Pay appearance and callback unchanged; static prerequisites do not prove runtime change. Record regrade.
- **Skill:** Existing adjustment answers the request (S1); Pay typography changes are S8 when appearance is fixed.
- **Transfer:** Integration item checkout-integrated already transfers it.

**`G-9f7f4159ccae60`** · UIKit · table-span · unaided **pass** (primary pass). Pair: both-correct. · **P3 keep-control** · good-as-is · S1

> I'm reviewing a UIKit change for iOS 26.0. A merged table cell occupies several coordinates. When users explore the table by coordinate, does each covered position resolve to the right cell?

- **Diagnosis:** Ledger pass; pair both-correct with an already neutral question about coordinate resolution.
- **Prompt:** none
- **Oracle:** none
- **Skill:** Neutral question, preserved working lookup.
- **Transfer:** macOS NSAccessibility table with column spans.

**`G-a1aff76682fe0a`** · UIKit · rebound-action · unaided **fail** (primary pass). Blind audit Q13: fail/pass. Pair: fixes-defect-breaks-working. · **P1 grade-components** · evidence-only · S2, S1, S8

> I'm reviewing a UIKit change for iOS 26.0. After refreshing a row, an action captured earlier can operate on the wrong record. Can you repair the ownership without losing the current action?

- **Diagnosis:** Audit Q13 keeps fail/pass: the custom action already captures revision and ID; the patch replaces live button dispatch and its test calls an unsupported getter and conditionally skips invoking the stale UIAction. Factorial captured-action stayed F/P in all arms, so the remaining gap is the proof.
- **Prompt:** Adopt the factorial captured-action wording for both versions.
- **Proposed wording:** iOS 26.0, UIKit. After the same view is reconfigured, what happens if a client retains and invokes the old accessibility shortcut? The ordinary buttons should operate on the currently displayed item.
- **Oracle:** Grade primary, ordinary-button preservation, rework, and evidence separately; evidence requires invoking the actual installed shortcut and pressing the real buttons, with no conditional skip.
- **Skill:** Skipped invocation and test-only handlers are the S2 defect; replacing working dispatch is S1/S8.
- **Transfer:** macOS NSAccessibilityCustomAction on a reused table cell view.

**`G-aa6d10b04b1594`** · UIKit · speed-metadata · unaided **pass** (primary pass). Pair: both-correct. · **P3 keep-control** · good-as-is · S1

> I'm reviewing a UIKit change for iOS 26.0. The speed control changes playback but continues to describe the previous setting. Can you synchronize the displayed and accessible state?

- **Diagnosis:** Ledger pass; pair both-correct: concludes render already synchronizes selection, display and accessible speed.
- **Prompt:** none
- **Oracle:** none
- **Skill:** Holds a working path under an asserted symptom.
- **Transfer:** macOS speed menu.

**`G-b3e3789d10b0ed`** · UIKit · decorative-element · unaided **fail** (primary pass). Blind audit Q39: fail/pass. Pair: fixes-defect-breaks-working. · **P1 grade-components** · rework-only · S1, S8

> I'm reviewing a UIKit change for iOS 26.0. A decorative part of this view is getting its own navigation stop. Can you remove just that stop?

- **Diagnosis:** Audit Q39 confirms primary pass, whole fail: the leaf decoration is already excluded on each configure; the answer adds a subtree-hiding flag and a test requiring that detail. Pure avoidable rework prompted by the asserted symptom.
- **Prompt:** Use the neutral wording shared with G-0f5d8b65a4920e instead of asserting a stop exists.
- **Proposed wording:** iOS 26.0, UIKit. This card shows a decorative star beside a title and two buttons. Which navigation stops does VoiceOver get on this card today? Keep the title and both buttons reachable.
- **Oracle:** Grade primary (star excluded, three elements kept), rework (new flags or tests of implementation detail) and evidence separately; extra flag that preserves navigation is rework, not regression.
- **Skill:** The existing exclusion already answers the request (S1); the added flag is unneeded boilerplate (S8).
- **Transfer:** macOS AppKit card with an NSImageView decoration and accessibilityElement false.

**`G-c9829b24aa0b35`** · UIKit · motion-notification · unaided **pass** (primary pass). Pair: both-correct. · **P3 keep-control** · good-as-is · S1

> I'm reviewing a UIKit change for iOS 26.0. Does this observer refresh the motion setting when that setting actually changes?

- **Diagnosis:** Ledger pass; pair both-correct. The question is already neutral ('Does this observer refresh...?') and the working version is kept.
- **Prompt:** none
- **Oracle:** none
- **Skill:** Neutral question with a preserved working path shows S1.
- **Transfer:** tvOS lifecycle observer for reduce-motion changes.

**`G-e24e3f394ea182`** · UIKit · range-coordinate · unaided **fail** (primary fail). Blind audit Q47: fail/fail. Pair: fixes-defect-breaks-working. · **P0 rewrite-neutral** · real-model-gap · S6, S2

> I'm reviewing a UIKit change for iOS 26.0. Navigation to a phrase works for plain English but lands on the wrong text after emoji. Can you repair it without changing the displayed text?

- **Diagnosis:** Confirmed range-coordinate gap (audit Q47 fail/fail): a valid UTF-16 offset is mapped into grapheme units, and reverse lookup uses the wrong units too. Factorial text-range-47 kept primary in all arms under neutral wording; whole failed on the check.
- **Prompt:** Adopt the neutral factorial wording for both edited-rotor versions.
- **Proposed wording:** iOS 26.0, UIKit. In this UIKit reader, search for “cat” in “😀 cat!”. What text range will the rotor return, and can people still select ordinary text in the reader?
- **Oracle:** Drive the installed rotor; compare returned text with the literal substring; grade evidence separately.
- **Skill:** UTF-16 units and a literal substring check are S6 and S2.
- **Transfer:** macOS NSTextView reader with emoji and flags.

**`G-ecf0c73499bcb3`** · UIKit · motion-policy · unaided **fail** (primary pass). Blind audit Q20: fail/pass. Pair: fixes-defect-breaks-working. · **P1 grade-components** · rework-only · S1, S8

> I'm reviewing a UIKit change for iOS 26.0. The optional effect still plays when the person asks for reduced motion. Can we honor their setting without changing the normal experience?

- **Diagnosis:** Audit Q20 confirms primary pass, whole fail: the existing duration policy already maps reduced motion to zero; the answer adds an uncalled helper for an animation absent from the source.
- **Prompt:** Use the neutral motion question shared with G-cdecb4f2473a6b.
- **Proposed wording:** iOS 26.0, UIKit. With Reduce Motion on and then off, what duration does this screen use for the optional effect, and what does a person see in each case? Keep the normal animation for people who have not asked for reduced motion.
- **Oracle:** Grade primary (zero duration under reduced motion, normal otherwise), rework (new API without a call site) and evidence separately; an uncalled helper is rework, not regression.
- **Skill:** The existing policy answers the request (S1); the uncalled helper is S8.
- **Transfer:** SwiftUI view reading accessibilityReduceMotion with an explicit withAnimation call.

**`G-edc45504aead03`** · UIKit · request-generation · unaided **pass** (primary pass). Pair: both-correct. · **P3 keep-control** · good-as-is · S3, S1

> I'm reviewing a UIKit change for iOS 26.0. A late response from an earlier request overwrites a newer result. Can you give the current request ownership of the update?

- **Diagnosis:** Ledger pass; pair both-correct: identifies the active-ticket guard and keeps it, with reverse-order completion tests.
- **Prompt:** none
- **Oracle:** none
- **Skill:** Keeps an existing ownership guard under an asserted symptom.
- **Transfer:** Nine siblings exist; no further transfer needed.

#### iOS · implementation (26)

**`G-02690558762670`** · SwiftUI · open rubric · unaided **pass** (primary inconclusive). · **P3 keep-control** · good-as-is · S3

> Target iOS26, SwiftUI with UIKit interop.

- **Diagnosis:** Implementation pass: reuses the native control with the updated callback, validates sender identity and stops dispatch after dismantling.
- **Prompt:** none
- **Oracle:** Record primary from the interop rubric's stale/current/dismantled checks.
- **Skill:** Sender identity and dismantle are S3.
- **Transfer:** macOS NSViewRepresentable wrapper.

**`G-1079cff7faaab5`** · UIKit · open rubric · unaided **fail** (primary inconclusive). · **P1 grade-components** · real-model-gap · S3, S2

> I'm building reusable UIKit cards for invoices, supporting iOS 26 and later. Each card shows a decorative star, an invoice title, and separate Open and Save buttons. Every card has the same visible button titles. The same card instance can 

- **Diagnosis:** Implementation fail, critical: star excluded and names update, but each configure adds a new UIAction with no removal, so one tap after rebinding can call both the old and current invoice handlers; the stale-action test asserts zero calls despite that accumulation. Four criteria share one verdict.
- **Prompt:** Keep the question; it ends at an observable behavior (which invoice each button acts on).
- **Oracle:** Grade decoration, contextual names, single dispatch to the current invoice after rebind, and test validity separately; single dispatch is the critical component.
- **Skill:** Accumulated actions capture old owners (S3); the test asserted a count the code could not produce (S2).
- **Transfer:** tvOS reusable card with primaryActionTriggered handlers.

**`G-1d5d9e020d7249`** · UIKit · open rubric · unaided **inconclusive** (primary inconclusive). · **P1 repair-oracle** · grader-uncertain · S2, S7

> Our UIKit video player needs a diagnostic view showing which audio tracks declare audio description, which captions and audio are currently selected, and the asset duration. It must not change the user's selections or start playback. Some i

- **Diagnosis:** Implementation inconclusive: exercises a nil item and empty groups, but never demonstrates extraction of a positively tagged selected track, so the grader could not establish the main claim.
- **Prompt:** Keep the request; it asks for what metadata establishes, a good endpoint.
- **Oracle:** Require a positive fixture: one injected option tagged as audio description and selected, asserting it is reported as described and selected; grade nil/empty cases separately.
- **Skill:** Absence-only tests are the S2 positive-fixture gap; reading actual selection is S7.
- **Transfer:** tvOS inspector with injected media-option descriptors.

**`G-2136bae371f01f`** · SwiftUI · open rubric · unaided **inconclusive** (primary inconclusive). · **P2 repair-oracle** · grader-uncertain · S2, S3

> Target iOS26, SwiftUI with UIKit.

- **Diagnosis:** Implementation inconclusive: current-item, disabled and teardown checks exist, but shortcut tests depend on reading actionHandler and were never executed.
- **Prompt:** Keep the request.
- **Oracle:** Compile and run the submitted tests on the forwarding-ios fixture; accept invoking the installed UIAccessibilityCustomAction.actionHandler as the production path, and grade old-shortcut rejection after rebind as its own criterion.
- **Skill:** Driving the installed handler is S2; rebind rejection is S3.
- **Transfer:** macOS NSAccessibilityCustomAction wrapper.

**`G-2711a4e66fe603`** · UIKit · open rubric · unaided **pass** (primary inconclusive). · **P3 keep-control** · good-as-is · S5

> Our UIKit player offers normal and faster playback speeds. People need to see the current choice and change it without depending on a special gesture. Show a small iOS 26+ control with ordinary actions and useful accessibility metadata, plu

- **Diagnosis:** Implementation pass: ordinary rate selection, current-choice presentation, disabled and duplicate guards.
- **Prompt:** none
- **Oracle:** none
- **Skill:** Current-choice wording is S5.
- **Transfer:** tvOS speed picker.

**`G-27926d3f994473`** · SwiftUI · open rubric · unaided **pass** (primary inconclusive). · **P3 keep-control** · good-as-is · S5

> Target iOS26, SwiftUI with UIKit.

- **Diagnosis:** Implementation pass: heading, status and separate controls with stale metadata cleared. The iOS prompt carries a TV26/TV27 clause irrelevant to this platform.
- **Prompt:** none
- **Oracle:** Grade the five rubric fields (names, selected readout, value, optional help clearing, trait preservation) separately when recorded.
- **Skill:** Selected-state wording and no unsupported TV claims are S5.
- **Transfer:** tvOS native card wrapper.

**`G-2865458d46b0d1`** · SwiftUI · open rubric · unaided **fail** (primary inconclusive). · **P1 grade-components** · real-model-gap · S7

> # iOS developer request

- **Diagnosis:** Implementation fail: updates the selected value before validating the native group and clears captions without checking the group's empty-selection policy.
- **Prompt:** Keep; it already ends at the player item reflecting the choice.
- **Oracle:** Grade actual item selection, preserved audio selection, full-only offering, and Off against allowsEmptySelection separately.
- **Skill:** Writing the actual player item and handling Off is S7.
- **Transfer:** tvOS AVPlayerViewController caption menu.

**`G-2ef8d48e375dbc`** · SwiftUI · open rubric · unaided **pass** (primary inconclusive). · **P1 raise-to-integration** · weak-endpoint · S7, S3

> Target iOS26, SwiftUI.

- **Diagnosis:** Implementation pass, but the task stops before the developer-observable result: it records a preference ID and explicitly excludes applying AVMediaSelection, the step FIRST-ITERATION names as the needed endpoint.
- **Prompt:** Extend the task to the player item's actual selection while keeping the browser contract.
- **Proposed wording:** iOS 26.0, SwiftUI. Our player keeps the supplied AVPlayer and native controls. The caption browser lists options with stable IDs and localized names, distinguishes not-yet-loaded from an empty result, and can receive old option-list replies. When someone picks a caption choice or Off, the video should show that choice without changing the viewer's audio, volume or mute. Provide code and focused unit tests; no UI automation.
- **Oracle:** Assert the player item's selected legible option (or none for Off) after a choice, preserved audio selection, stale reply ignored, and selection kept through reordering.
- **Skill:** Applying the choice to the actual item is S7; old replies are S3.
- **Transfer:** tvOS caption menu applying to the AVPlayerItem.

**`G-34541ce79ee3d5`** · UIKit · open rubric · unaided **fail** (primary inconclusive). · **P1 grade-components** · real-model-gap · S4, S5

> Our UIKit app has a custom panel with a heading, Apply and Cancel buttons. Cancel animates the panel away asynchronously. Sometimes closing it leaves the background unavailable, or a late callback from an earlier opening affects the reopene

- **Diagnosis:** Implementation fail: saves and restores the dimming view's isHidden, a visual property, instead of the background's accessibilityElementsHidden, so a pre-hidden background is not restored for VoiceOver.
- **Prompt:** Keep the request; it already states the pre-hidden background and replaced target.
- **Oracle:** Grade background accessibility restoration, stale-callback rejection, eligible return target with fallback, escape support and teardown separately.
- **Skill:** Restoring the right property and destination after completion is S4; visual vs. accessibility hiding is an S5 fact.
- **Transfer:** macOS sheet with an already-hidden sidebar.

**`G-3c54c7b993ec89`** · SwiftUI · open rubric · unaided **pass** (primary inconclusive). · **P3 keep-control** · good-as-is · S3

> Target iOS26, SwiftUI.

- **Diagnosis:** Implementation pass: distinguishes empty service errors and invalidates obsolete requests on edit, duplicate or cancel.
- **Prompt:** none
- **Oracle:** none
- **Skill:** Obsolete reply rejection is S3.
- **Transfer:** UIKit form version exists.

**`G-4ec92962591872`** · SwiftUI · open rubric · unaided **fail** (primary inconclusive). · **P1 grade-components** · real-model-gap · S7, S2

> # iOS developer question

- **Diagnosis:** Implementation fail: the missing-item test expects an empty option list, so the implementation conflates no player item with a successful empty load, one of the four states the request asks to distinguish.
- **Prompt:** Keep the request.
- **Oracle:** Grade each state (missing item, loading, empty, failure) and retry separately, plus the real selection shown from the player item.
- **Skill:** Real selection is S7; a test asserting the conflated value is S2.
- **Transfer:** tvOS diagnostics with nil currentItem.

**`G-5cac0e1c6c3058`** · UIKit · open rubric · unaided **pass** (primary inconclusive). · **P3 keep-control** · good-as-is · S3

> Our iOS app uses AVPlayer. We asynchronously load a short description of its current AVPlayerItem through an injected callback on the main actor. Items can be replaced externally, the same item can be inspected again, and results can arrive

- **Diagnosis:** Implementation pass: request ID plus current-item check; duplicate delivery and same-item inspection covered.
- **Prompt:** none
- **Oracle:** none
- **Skill:** Validating actual current item at callback time is S3.
- **Transfer:** Integration now-playing-late-title transfers it.

**`G-61f7850a2f1701`** · UIKit · open rubric · unaided **pass** (primary inconclusive). · **P3 keep-control** · good-as-is · S3

> Our UIKit iOS form has editable name and email fields. Validation is supplied as a callback-based service that takes a snapshot of both strings and eventually returns a dictionary of field IDs to nonempty error messages; an empty dictionary

- **Diagnosis:** Implementation pass: checks submission ownership and current field values with immediate, duplicate, obsolete and cancelled responses.
- **Prompt:** none
- **Oracle:** none
- **Skill:** Snapshot ownership is S3.
- **Transfer:** SwiftUI form version exists.

**`G-6d2dd61c5ac4ab`** · SwiftUI · open rubric · unaided **fail** (primary inconclusive). · **P1 grade-components** · real-model-gap · S7, S5

> # iOS developer question

- **Diagnosis:** Implementation fail: Off calls a deselect API instead of the supported AVPlayerItem selection of nil for the legible group.
- **Prompt:** Keep the request.
- **Oracle:** Grade full-only offering, actual item selection, Off via supported API, preserved audio, and out-of-list current choice separately.
- **Skill:** Off on the actual item is S7 with an exact supported API (S5).
- **Transfer:** tvOS caption menu.

**`G-7310de6a5160a4`** · SwiftUI · open rubric · unaided **pass** (primary inconclusive). · **P3 keep-control** · good-as-is · S3

> Target iOS26, SwiftUI.

- **Diagnosis:** Implementation pass: ordinary row actions with a captured revision check for important-article navigation.
- **Prompt:** none
- **Oracle:** none
- **Skill:** Revision captured with the action is S3.
- **Transfer:** UIKit table with a custom rotor.

**`G-7331721435c052`** · SwiftUI · open rubric · unaided **pass** (primary inconclusive). · **P3 keep-control** · good-as-is · S5

> Target iOS26, SwiftUI.

- **Diagnosis:** Implementation pass: selected wording, accessibility-size layout and reduced-motion final state tested. The prompt's TV26 clause adds noise on iOS.
- **Prompt:** none
- **Oracle:** none
- **Skill:** Availability boundaries are S5.
- **Transfer:** tvOS status area.

**`G-74d04592641f2f`** · SwiftUI · open rubric · unaided **pass** (primary inconclusive). · **P3 keep-control** · good-as-is · S8

> Target iOS26, SwiftUI.

- **Diagnosis:** Implementation pass: ordinary controls kept, bounded accessible adjustment with duplicate-write checks.
- **Prompt:** none
- **Oracle:** none
- **Skill:** Preserves a valid native Toggle.
- **Transfer:** UIKit settings area.

**`G-894e307c535879`** · UIKit · open rubric · unaided **pass** (primary inconclusive). · **P3 keep-control** · good-as-is · S5

> Our UIKit delivery-options table supports iOS 26 and later. Each row has an option name and a short status. Long translated names get cut off at large text sizes, and we currently distinguish the chosen option only by color. A row can be co

- **Diagnosis:** Implementation pass: scalable multiline row and textual chosen state restored across reuse.
- **Prompt:** none
- **Oracle:** none
- **Skill:** Non-color selected-state wording is S5.
- **Transfer:** tvOS delivery-choice list.

**`G-90629dd9d60ff9`** · SwiftUI · open rubric · unaided **fail** (primary inconclusive). · **P1 grade-components** · real-model-gap · S3, S4

> Target iOS26, SwiftUI.

- **Diagnosis:** Implementation fail: creates a synthetic sheet context with a fresh origin when no sheet is active, so a duplicate finish can choose a false fallback.
- **Prompt:** Keep the request.
- **Oracle:** Grade completion ownership (duplicate and stale ignored), eligible target at completion, fallback, and reentrant open separately.
- **Skill:** Duplicate completion must not fabricate ownership (S3) or a destination (S4).
- **Transfer:** UIKit modal with generation tokens.

**`G-918e20d33a7ec3`** · SwiftUI · open rubric · unaided **fail** (primary inconclusive). · **P2 retire-duplicate** · duplicate · S3, S7

> # iOS developer request

- **Diagnosis:** Implementation fail: task cancellation protects loading, but choose carries no originating request or item, so a stale Off still applies. Same mechanism as G-c04cc5d4aa6f82 on the shorter v2 wording.
- **Prompt:** Retire the longer v1 wording; keep G-c04cc5d4aa6f82 as the active copy and this answer as replication evidence.
- **Oracle:** none
- **Skill:** Old option callbacks must validate their item (S3) before writing selection (S7).
- **Transfer:** n/a

**`G-abbd59371b0491`** · SwiftUI · open rubric · unaided **pass** (primary inconclusive). · **P3 keep-control** · good-as-is · S3

> Target iOS26, SwiftUI with UIKit.

- **Diagnosis:** Implementation pass: snapshot updated before the animation callback; reduced motion, duplicate selection and reentrant changes covered.
- **Prompt:** none
- **Oracle:** none
- **Skill:** Reentrant ordering is S3.
- **Transfer:** tvOS card state.

**`G-abc3c19f3ec5a0`** · UIKit · open rubric · unaided **inconclusive** (primary inconclusive). · **P1 repair-oracle** · grader-uncertain · S3, S6

> Our UIKit document reader lets people jump between highlighted phrases using a custom rotor. The document and search phrase can change while a previous result is still held. Jumps sometimes point to the wrong text after an edit, especially 

- **Diagnosis:** Implementation inconclusive: rebuilds ranges after edits and tests direction, but whether a retained old result is rejected after a query-only change is unresolved.
- **Prompt:** Keep the request.
- **Oracle:** Add explicit criteria: a result held from query A returns nothing after a query change with unchanged text; ranges after emoji are checked with text(in:) against a literal.
- **Skill:** Query revision validation is S3; literal substring check is S6.
- **Transfer:** macOS NSTextView reader.

**`G-bceba81f4bd8dd`** · UIKit · open rubric · unaided **pass** (primary inconclusive). · **P3 keep-control** · good-as-is · S2

> I want a unit-testable contrast checker for text colors in our UIKit app, supporting iOS 26 and later. We use semantic UIColors and some custom colors, so the values can change in dark mode and with Increase Contrast. Some callers may also 

- **Diagnosis:** Implementation pass: resolves dynamic colors, converts color space and handles translucent and pattern colors.
- **Prompt:** none
- **Oracle:** none
- **Skill:** Explicit unsupported-input results are checkable.
- **Transfer:** macOS NSColor checker.

**`G-be83d8c94dea14`** · UIKit · open rubric · unaided **inconclusive** (primary inconclusive). · **P2 repair-oracle** · grader-uncertain · S2

> I am adding a diagnostic panel to a UIKit video player on iOS 26 and later. It should report duration, the parts we can seek to versus the parts already buffered, and why playback might be waiting. Sometimes there is no current item; some s

- **Diagnosis:** Implementation inconclusive: separates item absence, ranges and waiting reason, but stream-kind classification with indefinite duration has no evidence.
- **Prompt:** Keep the request.
- **Oracle:** Add a criterion: an indefinite-duration item with a supplied non-live kind reports that kind, and absence is reported distinctly from zero duration.
- **Skill:** A positive indefinite-duration fixture is S2.
- **Transfer:** tvOS diagnostics overlay.

**`G-c04cc5d4aa6f82`** · SwiftUI · open rubric · unaided **fail** (primary inconclusive). · **P1 grade-components** · real-model-gap · S3, S7

> # iOS developer question

- **Diagnosis:** Implementation fail: choose takes only the nullable choice, so an old Off callback after reload acts on the new selection despite cancelled loads; replicates G-918e20d33a7ec3.
- **Prompt:** Keep the request.
- **Oracle:** Grade separately: old load results ignored, old option callback (including Off) rejected after reload or item change, current choice applied to the item, and cancellation semantics.
- **Skill:** Stale Off is the S3/S7 intersection.
- **Transfer:** tvOS caption menu with item replacement.

**`G-d4bd274c3a3456`** · SwiftUI · open rubric · unaided **fail** (primary inconclusive). · **P1 grade-components** · real-model-gap · S7

> # iOS developer request

- **Diagnosis:** Implementation fail: shares the player but selection changes local option state without applying AVPlayerItem selection, the exact weak endpoint FIRST-ITERATION names.
- **Prompt:** Keep; the request asks for the same player and selection state.
- **Oracle:** Grade the four states and retry separately from actual item selection; local-state-only selection fails the selection component.
- **Skill:** Writing the actual item's selection is S7.
- **Transfer:** tvOS picker.

#### iOS · historical (23)

**`G-01d940885a29d8`** · UIKit · open rubric · unaided **pass** (primary inconclusive). · **P3 keep-control** · good-as-is · S3

> I am using UIKit on iOS 26 deployment target; available validation anchor iOS 26.5.

- **Diagnosis:** Historical pass under the dev7 scoring row: render-token ownership, cleared optional fields and Open against the current file. Primary inconclusive because no registered decision maps to this design question.
- **Prompt:** none
- **Oracle:** Map the scoring row to discrete checks (B shows no status/help; late A result ignored; Open targets B) so a primary verdict is recordable.
- **Skill:** Late metadata for A must validate the render token (S3).
- **Transfer:** n/a

**`G-0e48c179493510`** · SwiftUI · open rubric · unaided **pass** (primary inconclusive). · **P3 keep-control** · good-as-is

> Our Toggle edits an existing setting. Return a binding that reads the live value and ignores duplicate writes and writes while the setting is locked.

- **Diagnosis:** Historical rc.1 pass: binding reads the live value and guards locked and duplicate writes. Ends at a compilable function contract.
- **Prompt:** none
- **Oracle:** none
- **Skill:** none
- **Transfer:** n/a

**`G-164aedc058c069`** · UIKit · open rubric · unaided **pass** (primary inconclusive). · **P3 keep-control** · good-as-is · S2

> iOS 26.0, UIKit.

- **Diagnosis:** Historical GP26-09 pass: drag and adjustable actions share one clamped setter and suppress duplicate callbacks.
- **Prompt:** none
- **Oracle:** Record primary from the GP26-09 acceptance checks (step 5, clamp, exactly one onChange per change) instead of inconclusive.
- **Skill:** Exact callback counts are S2 evidence.
- **Transfer:** n/a

**`G-2a184c4680bf73`** · UIKit · open rubric · unaided **pass** (primary inconclusive). · **P3 keep-control** · good-as-is · S8

> My standard UISwitch has meaningful nearby naming configured by the app, working state and no reported accessibility defect. Should we replace it with a custom view?

- **Diagnosis:** Historical pass: keeps the native switch and naming with no reported defect. Short no-change control.
- **Prompt:** none
- **Oracle:** none
- **Skill:** Rejecting a custom replacement is S8.
- **Transfer:** n/a

**`G-35ee522327907b`** · SwiftUI · open rubric · unaided **fail** (primary inconclusive). · **P2 grade-components** · rework-only · S8, S1

> iOS 26.0, SwiftUI.

- **Diagnosis:** Historical GP26-11 fail: asserts a working labeled native Slider needs an explicit percent value. For a 0–100 range the change is close to the integration task's accepted alternative-matching-value, so the verdict mixes an unsupported claim with a possibly harmless edit.
- **Prompt:** Leave the frozen historical prompt unchanged; the change is in grading only.
- **Oracle:** Grade separately: binding/range/step preserved, unsupported defect claim, and whether the added value changes what VoiceOver reports versus the default.
- **Skill:** Inventing a native-control defect is the S8 pattern; tracing the default value is S1.
- **Transfer:** n/a

**`G-563886f9342980`** · UIKit · open rubric · unaided **pass** (primary inconclusive). · **P3 keep-control** · good-as-is · S4

> iOS 26.0, UIKit.

- **Diagnosis:** Historical GP26-08 pass: retains prior background hiding across guarded presentations and restores it on close.
- **Prompt:** none
- **Oracle:** none
- **Skill:** Restoring the prior state on close is part of S4.
- **Transfer:** n/a

**`G-63e10b06dd993c`** · SwiftUI · open rubric · unaided **pass** (primary inconclusive). · **P3 keep-control** · good-as-is · S8

> I am using SwiftUI on iOS 26 deployment target; available validation anchor iOS 26.5.

- **Diagnosis:** Historical pass: leaves the labeled native toggle intact and explains why a duplicate label is unneeded.
- **Prompt:** none
- **Oracle:** none
- **Skill:** Restraint against a generic review demand is S8.
- **Transfer:** n/a

**`G-64e4c578d3e7ef`** · SwiftUI · open rubric · unaided **pass** (primary inconclusive). · **P3 keep-control** · no-headroom

> Our custom volume control moves by five. Compute the next percent for a SwiftUI accessibility adjustment and stop at 0 and 100. Inputs are in range.

- **Diagnosis:** Historical rc.1 pass: clamps five-point adjustments. Trivial function contract with no headroom.
- **Prompt:** none
- **Oracle:** none
- **Skill:** none
- **Transfer:** n/a

**`G-702058f370f817`** · SwiftUI · open rubric · unaided **pass** (primary inconclusive). · **P3 retire-duplicate** · duplicate · S8

> My standard Toggle("Download on Wi-Fi", isOn: $enabled) is bound correctly. No accessibility issue has been reported. Must I add a custom role and label?

- **Diagnosis:** Historical pass: keeps the bound Toggle. Same decision and visible text as G-63e10b06dd993c in a shorter form.
- **Prompt:** Retire for new comparisons; G-63e10b06dd993c covers the same no-change Toggle decision.
- **Oracle:** none
- **Skill:** Same restraint decision.
- **Transfer:** n/a

**`G-7c78d80e047b92`** · any · open rubric · unaided **pass** (primary inconclusive). · **P3 keep-control** · good-as-is

> The referenced accessibility guideline cannot be opened in this session. Can you tell me whether you consulted it, and what you would need before relying on its exact API claim?

- **Diagnosis:** Historical pass: states the guideline was unread and asks for text and version before attributing an API claim. Meta control for read reporting, not accessibility behavior.
- **Prompt:** none
- **Oracle:** none
- **Skill:** none
- **Transfer:** n/a

**`G-817e7c3dcd689d`** · UIKit · open rubric · unaided **pass** (primary inconclusive). · **P3 keep-control** · good-as-is · S5

> Apply our supplied, unscaled design font to this description label at the given text-size setting. Use body scaling, let the description wrap without shrinking, and leave its contents alone.

- **Diagnosis:** Historical rc.1 checkout-font pass: body metrics applied to supplied base and traits; description unrestricted.
- **Prompt:** none
- **Oracle:** none
- **Skill:** Scaling with the supplied traits is the precise UIFontMetrics fact.
- **Transfer:** n/a

**`G-96a828dd7e79b7`** · SwiftUI · open rubric · unaided **fail** (primary inconclusive). · **P2 raise-to-integration** · rework-only · S8, S1

> iOS 26.0, SwiftUI.

- **Diagnosis:** Historical GP26-06 fail: adds a replacement label and generic hint to an already labeled bound toggle. Open-ended 'make any changes that are needed' with no defect; a clean overreach probe without executable variants.
- **Prompt:** Rebuild as an intact-code integration task with accepted alternatives and mutants, like volume-slider-intact.
- **Proposed wording:** iOS 26.0, SwiftUI. Our release checklist has an accessibility pass for every settings screen, and Notifications is next. The toggle saves through the existing preference store. Can you go over it for VoiceOver and make whatever changes it needs? Paste the complete resulting Swift file.
- **Oracle:** Executable test: same Toggle, binding and label; an optional matching value is accepted; an added hint or replacement label is flagged as rework, a changed binding as regression.
- **Skill:** Adding labels and hints to a working native control is S8.
- **Transfer:** n/a

**`G-9afcc6a91cfcbb`** · UIKit · open rubric · unaided **fail** (primary inconclusive). · **P2 grade-components** · rework-only · S8, S1

> I am using UIKit on iOS 26 deployment target; available validation anchor iOS 26.5.

- **Diagnosis:** Historical dev7 ios-uikit-text fail: builds a new Pay button, action and constraints instead of integrating text changes with the existing control.
- **Prompt:** Leave the frozen historical prompt unchanged; the change is in grading only.
- **Oracle:** Grade text scaling and wrapping, Pay identity and callback preservation, and evidence claims separately.
- **Skill:** Replacing a working control is S8; integrating with the supplied owner is S1.
- **Transfer:** n/a

**`G-a32f106f0aa1cc`** · SwiftUI · open rubric · unaided **fail** (primary inconclusive). · **P2 grade-components** · rework-only · S1, S8

> iOS 26.0, SwiftUI.

- **Diagnosis:** Historical GP26-12 fail: calls a slide transition under Reduce Motion a defect and switches it to opacity, though with a nil animation the change is inert. Mixes an unsupported judgment with a harmless edit; the derived FAQ task accepts a crossfade.
- **Prompt:** Leave the frozen historical prompt unchanged; the change is in grading only.
- **Oracle:** Grade separately: selected page and next-page behavior preserved, motion under the current preference, unsupported claim, and inert rework.
- **Skill:** The existing nil animation already answers (S1); the claimed defect is S8.
- **Transfer:** n/a

**`G-a731d4c7461228`** · UIKit · open rubric · unaided **pass** (primary inconclusive). · **P3 keep-control** · good-as-is · S4

> iOS 26.0, UIKit.

- **Diagnosis:** Historical GP26-07 pass: resolves the row button by stable ID in dismissal completion with the Pay fallback.
- **Prompt:** none
- **Oracle:** none
- **Skill:** Completion-time eligible target with fallback is S4.
- **Transfer:** n/a

**`G-b12c69f62639d3`** · SwiftUI · open rubric · unaided **fail** (primary inconclusive). · **P1 grade-components** · real-model-gap · S7

> I am using SwiftUI on iOS 26 deployment target; available validation anchor iOS 26.5.

- **Diagnosis:** Historical dev7 ios-swiftui-media fail: applies stored preferences with select during metadata inspection, changing the user's actual player selection.
- **Prompt:** Leave the frozen historical prompt unchanged; the change is in grading only.
- **Oracle:** Grade metadata state (loading, empty, failure, item change) separately from selection preservation; any write to the player item during inspection is a regression.
- **Skill:** Inspection must not write the player item's selection (S7).
- **Transfer:** n/a

**`G-b32973d721c21d`** · UIKit · open rubric · unaided **pass** (primary inconclusive). · **P3 retire-duplicate** · duplicate · S1

> iOS 26.0, UIKit.

- **Diagnosis:** Historical GP26-03 pass: scalable wrapping total with flexible layout. Same decision as integration checkout-integrated, which has executable variants.
- **Prompt:** Retire for new comparisons in favor of checkout-integrated.
- **Oracle:** none
- **Skill:** Same integrated text-size decision.
- **Transfer:** n/a

**`G-ddf8bad3cbd8d0`** · UIKit · open rubric · unaided **fail** (primary inconclusive). · **P1 grade-components** · real-model-gap · S3

> I am using UIKit on iOS 26 deployment target; available validation anchor iOS 26.5.

- **Diagnosis:** Historical dev7 ios-uikit-actions fail: the retained Delete shortcut calls a stored closure without checking the current button's enabled state when invoked.
- **Prompt:** Leave the frozen historical prompt unchanged; the change is in grading only.
- **Oracle:** Grade shortcut addition, ordinary buttons preserved, invocation-time validation (current file, enabled) and tests separately.
- **Skill:** Validating owner and enabled state when the action runs is S3.
- **Transfer:** n/a

**`G-debf8047cd9f4e`** · UIKit · open rubric · unaided **fail** (primary inconclusive). · **P1 grade-components** · real-model-gap · S3

> iOS 26.0, UIKit.

- **Diagnosis:** Historical GP26-10 fail: the finished-state guard rejects terminal repeats but lets progress through, so late progress can replace the terminal accessibility value.
- **Prompt:** Leave the frozen historical prompt unchanged; the change is in grading only.
- **Oracle:** Grade per-ID stale rejection, post-terminal progress rejection, single announcement, and value preservation as separate checks.
- **Skill:** Callbacks must validate the operation's current phase when they run (S3).
- **Transfer:** n/a

**`G-e9d082b712f90b`** · UIKit · open rubric · unaided **pass** (primary inconclusive). · **P3 keep-control** · good-as-is · S1

> iOS 26.0, UIKit.

- **Diagnosis:** Historical GP26-02 pass: reassigns priority/ordinary name and refreshes optional status on reuse.
- **Prompt:** none
- **Oracle:** none
- **Skill:** In-place refresh.
- **Transfer:** n/a

**`G-f25c0e60d13675`** · UIKit · open rubric · unaided **pass** (primary inconclusive). · **P3 keep-control** · good-as-is

> iOS 26.0, UIKit.

- **Diagnosis:** Historical GP26-01 pass: makes the row a container, restores reachable children and names the switch.
- **Prompt:** none
- **Oracle:** none
- **Skill:** none
- **Transfer:** n/a

**`G-f4a732e8350b5c`** · UIKit · open rubric · unaided **pass** (primary inconclusive). · **P3 keep-control** · good-as-is · S8

> This existing switch works. On reuse only its accessible name changes; pass the very same switch back, without resetting its state, traits or help.

- **Diagnosis:** Historical rc.1 pass: the supplied code already satisfies the contract and the answer returns the same switch with only its label changed.
- **Prompt:** none
- **Oracle:** none
- **Skill:** Keeping correct code as-is is S8 restraint.
- **Transfer:** n/a

**`G-f981e62bcf7bd1`** · SwiftUI · open rubric · unaided **pass** (primary inconclusive). · **P3 keep-control** · good-as-is · S3, S4

> I am using SwiftUI on iOS 26 deployment target; available validation anchor iOS 26.5.

- **Diagnosis:** Historical dev7 SwiftUI lifecycle pass: token validated, ownership consumed and a current eligible target resolved before the focus request.
- **Prompt:** none
- **Oracle:** none
- **Skill:** Completion ownership and eligible destination are S3/S4.
- **Transfer:** n/a

#### iOS · integration (5)

**`G-8b4c2893964bfe`** · UIKit · open rubric · unaided **fail** (primary inconclusive). · **P1 grade-components** · rework-only · S8, S1

> iOS 26.0, UIKit.

- **Diagnosis:** Integration fail: changes the Pay title font and enables Dynamic Type on it despite the explicit requirement to keep its appearance; matches the mutant-pay-rewired failure class.
- **Prompt:** Keep the prompt.
- **Oracle:** Run the executable test; grade total wrapping/scaling, row growth, and Pay appearance plus action as separate components.
- **Skill:** Touching the working Pay control is S8.
- **Transfer:** SwiftUI checkout with a fixed-style Pay button.

**`G-d7b1d47b70ec1b`** · SwiftUI · open rubric · unaided **fail** (primary inconclusive). · **P0 repair-oracle** · oracle-mismatch · S1, S8

> iOS 26.0, SwiftUI.

- **Diagnosis:** Integration fail looks like a grading error: the answer changes the Reduce Motion path to a short easeInOut with an opacity transition and keeps the spring and toggle state, which matches the task's registered alternative-crossfade (expected pass).
- **Prompt:** Keep the prompt; it is a good symptom-as-fact probe.
- **Oracle:** Run test.swift on the submission; accept the crossfade alternative as harmless and grade the unsupported HIG claim separately as rework, not as a contract failure.
- **Skill:** The existing nil path is correct (S1); a crossfade is optional refinement, not required work (S8).
- **Transfer:** UIKit expandable rows with UIView.animate gated by isReduceMotionEnabled.

**`G-e505d95d8bc6f7`** · SwiftUI · open rubric · unaided **fail** (primary inconclusive). · **P1 grade-components** · rework-only · S8, S1

> iOS 26.0, SwiftUI.

- **Diagnosis:** Integration fail: wraps a working native Slider in a combined adjustable element and duplicates the native adjustment path; the decision is 'needs no change'.
- **Prompt:** Keep the prompt; the release-checklist framing is a natural overreach probe.
- **Oracle:** Run the test; accept alternative-matching-value; grade binding/range/step/readout preservation separately from added wrappers.
- **Skill:** Replacing a working native control's semantics is S8.
- **Transfer:** UIKit UISlider with an existing value label.

**`G-f3c17aa88dbf7b`** · UIKit · open rubric · unaided **inconclusive** (primary inconclusive). · **P2 repair-oracle** · grader-uncertain · S3, S2

> iOS 26.0, UIKit.

- **Diagnosis:** Integration inconclusive: observes currentItem and rejects an obsolete result by identity, which matches alternative-observe-current-item, but KVO delivery timing against the harness was not verified.
- **Prompt:** Keep the prompt.
- **Oracle:** Compile and run test.swift with the submission; if KVO timing is the only issue, grade identity-at-delivery separately from harness registration timing.
- **Skill:** Validating the actual current item at delivery is S3; an executed check is S2.
- **Transfer:** tvOS now-playing overlay with shared AVPlayer.

**`G-f776360cf78dd3`** · UIKit · open rubric · unaided **pass** (primary inconclusive). · **P3 keep-control** · good-as-is · S5

> iOS 26.0, UIKit.

- **Diagnosis:** Integration pass: scales the brand font against the preview traits and lets the full text wrap.
- **Prompt:** none
- **Oracle:** none
- **Skill:** Scaling with the supplied traits rather than ambient ones is S5.
- **Transfer:** tvOS receipt preview.

#### iOS · workflow (6)

**`G-0f2de6751163e9`** · SwiftUI · form-error-association · unaided **pass** (primary pass). · **P3 keep-control** · good-as-is · S8

> iOS, SwiftUI. Two text fields can both fail validation with the same message. When the form updates, a user cannot tell which field the error belongs to. How would you fix this while preserving the text and editing position?

- **Diagnosis:** Workflow pass: keeps both fields stable with field-specific errors. Design question with a stated, real defect and no fixture; a useful control of non-merging and non-announcing behavior.
- **Prompt:** none
- **Oracle:** none
- **Skill:** The criterion rejects announcing every keystroke or merging fields, the S8 restraint concern.
- **Transfer:** UIKit form with two UITextFields and inline error labels.

**`G-18fda1e5d3c168`** · SwiftUI · custom-control-increments · unaided **pass** (primary pass). Blind audit Q19: fail/fail. · **P0 specify-policy** · real-model-gap · S2

> iOS, SwiftUI. Our custom scrubber has discrete chapters of different lengths, plus a plain tap to play. Dragging works but people using an adjustable action can land between chapters. How should adjustment behave at either end?

- **Diagnosis:** Ledger pass, but audit Q19 grades fail/fail: seeks to media end at the last chapter, assumes a nonempty list and never shows ordinary play. Factorial chapter-boundaries child failed whole and primary in all four arms, so the gap holds with an explicit policy.
- **Prompt:** Supply uneven chapter starts, terminal and empty behavior so the oracle can detect the end-of-media seek.
- **Proposed wording:** iOS, SwiftUI. Our episode has chapters starting at 0, 35 and 107 seconds and ends at 160. When positioned at a chapter start, an accessibility adjustment should move by one chapter, staying at a boundary when there is no next step. Episodes can also have no chapters. How would you handle those cases while keeping tap to play and ordinary dragging?
- **Oracle:** Assert resulting chapter positions from 35 (forward 107, backward 0), no movement past 0 or 107, defined empty behavior, and preserved Play; comparing clamped times alone misses the error. Record the regrade of the original pass.
- **Skill:** The original pass compared only clamped times; S2 requires the literal resulting chapter as the asserted effect.
- **Transfer:** UIKit custom scrubber with accessibilityIncrement over unevenly spaced markers.

**`G-49f0342d6263c1`** · UIKit · visible-name-alignment · unaided **pass** (primary pass). · **P3 keep-control** · good-as-is · S5

> iOS, UIKit. Our button visibly says Continue, but its accessible name is Step 3 of 4. Voice Control users try saying the displayed word. We still need to communicate progress. How should these pieces be represented?

- **Diagnosis:** Workflow pass: keeps the visible word in the name and exposes progress separately. Guards the visible-title fact that failed on tvOS (audit Q21).
- **Prompt:** none
- **Oracle:** none
- **Skill:** Visible title vs. accessible name is S5.
- **Transfer:** SwiftUI button with accessibilityInputLabels.

**`G-5688b48b9cac5f`** · UIKit · progress-bucketing · unaided **pass** (primary pass). · **P3 keep-control** · good-as-is · S8

> iOS, UIKit. A download screen receives 30 updates per second. People want to inspect the current percentage whenever they visit, but speech keeps interrupting the rest of the screen. What would you expose and when would you notify?

- **Diagnosis:** Workflow pass: value inspectable on demand with bounded milestone notifications. Natural design question without a fixture.
- **Prompt:** none
- **Oracle:** none
- **Skill:** Rejecting announcements for every tick is S8 restraint.
- **Transfer:** SwiftUI ProgressView with accessibilityValue and milestone announcements.

**`G-6593f55798f788`** · UIKit · rotor-fallback · unaided **pass** (primary pass). · **P3 keep-control** · good-as-is · S8

> iOS, UIKit. The legal viewer ships with a shortcut for jumping between warnings. First-time VoiceOver users who haven't learned the rotor still need to find the warnings, and some chapters have none. How should the page behave?

- **Diagnosis:** Workflow pass: keeps warnings in ordinary reading and adds jumps that reflect whether warnings exist. Natural, neutral design question.
- **Prompt:** none
- **Oracle:** none
- **Skill:** Supplementing rather than replacing ordinary navigation is S8 restraint.
- **Transfer:** SwiftUI document with accessibilityRotor and a no-match chapter.

**`G-e4cb63936dea3a`** · SwiftUI · redundant-hint · unaided **pass** (primary pass). Blind audit Q26: pass/pass. · **P3 keep-control** · good-as-is · S8

> iOS, SwiftUI. Each row says Play, button, double tap to activate. One row streams over mobile data when activated. Which information belongs in its name or hint, and what should be left to the system?

- **Diagnosis:** Workflow and audit Q26 pass: separates item name, cellular consequence, role and system gesture. Exact final utterance can vary with VoiceOver settings, which the criterion should not grade.
- **Prompt:** none
- **Oracle:** Do not grade a quoted VoiceOver utterance; grade the name/hint content only.
- **Skill:** Omitting redundant gesture hints is S8.
- **Transfer:** UIKit table rows with accessibilityHint only on the cellular row.

### macOS

#### macOS · repair (57)

**`G-01eb362b156ad6`** · SwiftUI · interop-rebind · unaided **pass** (primary pass). Pair: fixes-defect-breaks-working. · **P2 pair-variant** · no-headroom · S3

> I'm reviewing a SwiftUI change for macOS 26.0. The wrapper updates its SwiftUI state but the native button can still send to the previous target. Can you fix the binding and teardown?

- **Diagnosis:** Defective half passes by unbinding the previous AppKit button first. Pair signal comes from the working twin, which fails on rework.
- **Prompt:** Use the neutral update/dismantle wording of G-5c8c9ba78d4db8 for both halves.
- **Oracle:** Same dispatch assertions as the twin.
- **Skill:** Target/action captured at install must be replaced on rebind.
- **Transfer:** Same as twin.

**`G-0efc69b6139819`** · AppKit · audio-description-tag · unaided **fail** (primary pass). Pair: both-fail. · **P1 grade-components** · evidence-only · S2

> I'm reviewing a AppKit change for macOS 26.0. The audio inspector calls ordinary language tracks described audio. How can we identify the marked options?

- **Diagnosis:** Defective half: primary pass (unconditional true replaced by the AVFoundation characteristic). The whole fail comes only from the test, which wraps every assertion in a loaded-state branch over options, so an empty or absent group passes vacuously.
- **Prompt:** Use the same neutral wording as the working twin G-be8ab365c3ca77 so the pair isolates whether the model can tell broken from working code.
- **Oracle:** Report primary and evidence separately. The evidence criterion requires a positive fixture: assert the group has at least one untagged audio option before asserting it is not described, and fail when loading never completes.
- **Skill:** The defect fix was right; only the vacuous conditional test failed the answer.
- **Transfer:** Same decision with a different loader shape, e.g. synchronous injected option list versus async asset load.

**`G-16de77ef3240aa`** · SwiftUI · presentation-owner · unaided **pass** (primary pass). Pair: fixes-defect-breaks-working. · **P1 repair-oracle** · oracle-mismatch · S3, S2

> I'm reviewing a SwiftUI change for macOS 26.0. A delayed close callback can restore focus for a presentation that has already been replaced. Can you fix that race?

- **Diagnosis:** Defective half passes by tying restoration to the current generation, but the working twin (Q10) showed the same family can pass a hand-supplied ticket while the view callback reads mutable state, so this pass may be shallow.
- **Prompt:** Use the neutral wording of G-79fa7510bdf4bc for both halves.
- **Oracle:** Re-grade with the factorial criterion: drive A's retained dismissal through the view's installed callback after B opens; a pass on a model-only test with the old ticket supplied manually is evidence-insufficient.
- **Skill:** Callback ownership must be proven through the installed closure.
- **Transfer:** Same as twin.

**`G-253ef47608e3c6`** · SwiftUI · rebound-action · unaided **pass** (primary pass). · **P3 reserve-transfer** · duplicate · S3

> I'm reviewing a SwiftUI change for macOS 26.0. After refreshing a row, an action captured earlier can operate on the wrong record. Can you repair the ownership without losing the current action?

- **Diagnosis:** Pass on the forwarding package: checks surface identity and generation before retained actions run. Same wording as nine sibling copies.
- **Prompt:** Reserve the native-surface shortcut shape as transfer for rebound-action.
- **Oracle:** none
- **Skill:** Retained shortcut ownership.
- **Transfer:** Accessibility shortcut on an NSView-backed card reused across items.

**`G-2cf913ca90235b`** · SwiftUI · motion-policy · unaided **pass** (primary pass). Blind audit Q08: pass/pass. Pair: fixes-defect-breaks-working. · **P2 pair-variant** · no-headroom · S1

> I'm reviewing a SwiftUI change for macOS 26.0. The optional effect still plays when the person asks for reduced motion. Can we honor their setting without changing the normal experience?

- **Diagnosis:** Defective half passes; audit Q08 confirms it gates only the optional callback. Pair fails only on the working twin.
- **Prompt:** Use the neutral per-setting wording of G-6d5107426a2b49 for both halves.
- **Oracle:** Same as twin.
- **Skill:** Pair isolates detection of a missing gate.
- **Transfer:** Same as twin.

**`G-2fa3929697b8e1`** · AppKit · key-link-teardown · unaided **pass** (primary pass). · **P2 pair-variant** · no-headroom

> I'm reviewing a AppKit change for macOS 26.0. Removing a field leaves a stale key-view link. Can you undo links owned by this component?

- **Diagnosis:** Pass with no headroom: asserts a stale link and asks to undo owned links, which states the fix.
- **Prompt:** Add a working twin with correct teardown and ask both what nextKeyView values remain after removing a field and stopping the helper.
- **Oracle:** Assert links owned by the helper are cleared and links it did not create are preserved.
- **Skill:** none
- **Transfer:** Dynamic list of address fields that are removed one at a time.

**`G-30434d38abe656`** · AppKit · missing-choice · unaided **pass** (primary pass). · **P2 pair-variant** · no-headroom · S7

> I'm reviewing a AppKit change for macOS 26.0. A requested option isn't in the available list. Can the picker leave the current choice intact instead of silently picking a replacement?

- **Diagnosis:** Pass with no headroom: the question names the expected behavior ('leave the current choice intact'). tvOS sibling also passes.
- **Prompt:** Add a working twin and ask both what the selected option is after requesting a language the item lacks.
- **Oracle:** Assert the previous selection is unchanged and no select call is made for a missing language.
- **Skill:** Media selection preserved on a missing request.
- **Transfer:** Audio language request in a podcast app with a single-language feed.

**`G-352803701b8f4a`** · AppKit · stale-tree-node · unaided **fail** (primary fail). Blind audit Q34: pass/pass. · **P0 split-criteria** · oracle-mismatch · S2, S3

> I'm reviewing a AppKit change for macOS 26.0. Our refreshed outline can still be queried through an old node object. How can we avoid showing obsolete children?

- **Diagnosis:** Audit Q34 reverses the fail (pass/pass): the answer resolves against the active map and reports zero children after removal; the original grade penalized ID reuse, which the check does not cover. Factorial split: node-removal fails whole in all arms on the focused check, node-replacement passes in all arms.
- **Prompt:** Split removal and same-ID replacement into separate questions and state whether IDs are reused.
- **Proposed wording:** macOS 26.0, AppKit. After an outline node is removed, a delayed query still passes the old object. What children does that query see? IDs are never reused in this workflow. ‖ macOS 26.0, AppKit. An outline group disappears, then a different group reuses its ID. What child counts, expandability and children should delayed callers see through the old handle and the new one?
- **Oracle:** Removal: retain a populated parent, remove it, query count and expandability through the data source; expect 0/false, no indexing after zero. Replacement: old handle 0/false, new handle expandable with its new child. Grade each separately.
- **Skill:** The old handle must be validated when queried; tests must use positive populated fixtures.
- **Transfer:** Bookmarks outline whose folders are deleted and recreated by sync.

**`G-35b2cc77323520`** · AppKit · presentation-owner · unaided **pass** (primary pass). · **P3 reserve-transfer** · duplicate · S3, S4

> I'm reviewing a AppKit change for macOS 26.0. A delayed close callback can restore focus for a presentation that has already been replaced. Can you fix that race?

- **Diagnosis:** Pass on the AppKit lifecycle package with the same wording as the SwiftUI pair; unpaired.
- **Prompt:** Reserve the AppKit stale-completion shape as transfer for presentation-owner.
- **Oracle:** none
- **Skill:** Completion ownership with focus restoration.
- **Transfer:** NSWindow sheet with beginSheet completion handlers from two documents.

**`G-3d9c583f1d2a12`** · AppKit · reentrant-submit · unaided **pass** (primary pass). · **P3 pair-variant** · no-headroom

> I'm reviewing a AppKit change for macOS 26.0. The save callback can trigger another submit before the first finishes. Can you prevent duplicate submission?

- **Diagnosis:** Pass with no headroom: opening states the reentrant submit and asks to prevent it. tvOS sibling also passes.
- **Prompt:** Add a working twin and ask both how many saves occur when the save callback submits again.
- **Oracle:** Assert the save count is 1 for a reentrant callback and a later deliberate submit still saves.
- **Skill:** none
- **Transfer:** Save callback that triggers sync, which calls submit again.

**`G-45c27326f33a54`** · AppKit · duplicate-id · unaided **pass** (primary pass). · **P3 reserve-transfer** · duplicate · S1

> I'm reviewing a AppKit change for macOS 26.0. The server returned duplicate IDs. Can you reject the ambiguous update without leaving a partially updated screen?

- **Diagnosis:** Pass on the navigation package (table, not outline) with the same wording as the structure pair; unpaired, so it measures only the stated fix.
- **Prompt:** Reserve the NSTableView shape as transfer for duplicate-id; keep the outline pair for development.
- **Oracle:** none
- **Skill:** Same atomic-reject decision on a different AppKit container.
- **Transfer:** Flat NSTableView refresh with a duplicate row ID.

**`G-4659339897f098`** · AppKit · external-key-link · unaided **pass** (primary pass). · **P1 rewrite-neutral** · no-headroom

> I'm reviewing a AppKit change for macOS 26.0. After eligibility changes, one Tab path still leads to a disabled button. Check the incoming links as well as the outgoing loop.

- **Diagnosis:** Pass with no headroom: the opening tells the model to check incoming links as well as the outgoing loop, which is the fix.
- **Prompt:** Remove the instruction naming incoming links; ask which views Tab can reach after eligibility changes.
- **Proposed wording:** macOS 26.0, AppKit. After the Export button becomes disabled, which views can reach Export with Tab or Shift-Tab, including views outside this helper's list? Please check the supplied code.
- **Oracle:** Assert nextKeyView of every view in the window, including a pre-existing external view linked to the disabled button, no longer reaches it; enabled buttons stay in the loop.
- **Skill:** none
- **Transfer:** Preferences pane where a checkbox outside the group links into the group.

**`G-4c1f429b3189e5`** · AppKit · modal-state · unaided **pass** (primary pass). · **P3 retire-duplicate** · duplicate

> I'm reviewing a AppKit change for macOS 26.0. When a panel closes the background doesn't always return to its previous state. How should this screen handle opening and closing it more than once?

- **Diagnosis:** Pass; three iOS copies and one tvOS copy of the same modal-flag restore also pass. The AppKit window modal attribute adds no distinct decision here.
- **Prompt:** Retire the macOS copy for development; keep one iOS pair as the control.
- **Oracle:** none
- **Skill:** none
- **Transfer:** n/a

**`G-4cc95f7f4b6eda`** · AppKit · invalid-submit · unaided **pass** (primary pass). Pair: both-correct. · **P3 keep-control** · good-as-is · S2

> I'm reviewing a AppKit change for macOS 26.0. An invalid entry still reaches Save. Can you show the validation result and keep the user's input without submitting it?

- **Diagnosis:** Defective half of a both-correct pair; passes with error text, retained input and no save asserted. The request states the outcome the developer needs, which is the requirement rather than the fix.
- **Prompt:** none
- **Oracle:** none
- **Skill:** Literal assertions of error text, retained input and absent save.
- **Transfer:** Same as twin.

**`G-4d6441bda8046f`** · AppKit · stable-selection · unaided **pass** (primary pass). Pair: both-correct. · **P3 keep-control** · good-as-is · S2

> I'm reviewing a AppKit change for macOS 26.0. A rename or reorder moves the selection to a different item. Can you preserve identity and clear a selection only if its item is gone?

- **Diagnosis:** Defective half of a both-correct pair; saves the selected ID and checks reorder and removal.
- **Prompt:** none
- **Oracle:** none
- **Skill:** Checks both reorder and removal.
- **Transfer:** Same as twin.

**`G-535c760550d0f4`** · AppKit · conflicting-state-text · unaided **pass** (primary pass). Pair: fixes-defect-breaks-working. · **P2 pair-variant** · no-headroom · S1, S5

> I'm reviewing a AppKit change for macOS 26.0. The control state changes but its status text tells a different story. Can you keep the two consistent on successive updates?

- **Diagnosis:** Defective half passes: adds a textual selected cue and checks status. Pair: fixes defect, breaks working, so the pair's signal comes from the working twin. tvOS siblings (Q49) are audit-confirmed failures on this key.
- **Prompt:** Send the same neutral wording as G-d408fed70240bf; score the pair as one unit (both-correct or not).
- **Oracle:** Same per-control assertions as the twin; no notification required.
- **Skill:** Selected-state wording is a precise platform fact; the pair tests whether the model distinguishes broken from working.
- **Transfer:** AppKit segmented filter with a text cue instead of a toggle.

**`G-56290054a4fad7`** · SwiftUI · cancel-owner · unaided **pass** (primary pass). · **P2 pair-variant** · no-headroom · S3, S1

> I'm reviewing a SwiftUI change for macOS 26.0. An older cancelled load can cancel the current load. Can you keep cancellation local to its request?

- **Diagnosis:** Pass with no headroom: the opening states that an old cancelled load can cancel the current one and asks to keep cancellation local, which describes the fix.
- **Prompt:** Author a working twin where cancellation is already ticket-scoped and send both with one neutral question about what a late cancel of load A does to load B.
- **Oracle:** Drive cancel of the first request after the second starts; assert the second still completes and publishes. Grade unnecessary edits on the working twin separately.
- **Skill:** Cancellation ownership is a capture-at-install question; the working twin tests restraint.
- **Transfer:** Thumbnail or metadata loader with Task cancellation instead of callback tickets.

**`G-58194b84fb2eb3`** · AppKit · player-item-owner · unaided **pass** (primary pass). · **P3 retire-duplicate** · duplicate · S3

> I'm reviewing a AppKit change for macOS 26.0. The player can replace its item from outside this view. Can you prevent an old lookup from updating the new item's details?

- **Diagnosis:** Pass; the opening describes the external replacement and asks for the guard. iOS and tvOS copies of the same current-item check also pass.
- **Prompt:** Retire the macOS copy for development.
- **Oracle:** none
- **Skill:** Validate the current player item when the result arrives.
- **Transfer:** n/a

**`G-59d23c765e4fa1`** · SwiftUI · request-generation · unaided **pass** (primary pass). Pair: both-correct. · **P3 keep-control** · good-as-is · S3

> I'm reviewing a SwiftUI change for macOS 26.0. A late response from an earlier request overwrites a newer result. Can you give the current request ownership of the update?

- **Diagnosis:** Defective half of a both-correct pair; passes by validating the current form request. Nine copies of this decision exist across platforms, all passing.
- **Prompt:** none
- **Oracle:** none
- **Skill:** Pair member for the both-correct count.
- **Transfer:** Same as twin.

**`G-60eafa8ee757b1`** · AppKit · refresh-name · unaided **pass** (primary pass). · **P2 pair-variant** · no-headroom · S8, S1

> I'm reviewing a AppKit change for macOS 26.0. A control keeps the old accessible name after its content changes. Can you update the same control rather than replace it?

- **Diagnosis:** AppKit pass: applies distinct contextual names to Open and Save on the same controls. iOS/tvOS preservation siblings (Q01, Q17, Q24) fail on unneeded notifications and overrides, so a working twin here would test restraint.
- **Prompt:** Add a working twin that already refreshes names, and ask both what each button's accessible name is after configuring the row twice.
- **Oracle:** Assert the label of the same NSButton instances after two configurations; grade added notifications or replaced controls as rework.
- **Skill:** Sibling evidence shows rework risk on working name refresh.
- **Transfer:** File row reconfigured from report.pdf to notes.txt in a downloads list.

**`G-61fa82b4463179`** · AppKit · validation-help · unaided **pass** (primary pass). · **P3 pair-variant** · no-headroom

> I'm reviewing a AppKit change for macOS 26.0. Error help remains after the user corrects the field. Can you clear only the transient error and restore the previous help?

- **Diagnosis:** Pass with no headroom: opening asserts error help remains and asks to restore previous help. tvOS sibling passes.
- **Prompt:** Add a working twin; ask both what help the field reports after an invalid save and then an edit.
- **Oracle:** Assert help equals the original literal after editing, input preserved, and no save on edit.
- **Skill:** none
- **Transfer:** Password field with rules help in a sign-up sheet.

**`G-67a4979c4f2e7d`** · AppKit · preference-redelivery · unaided **pass** (primary pass). · **P3 retire-duplicate** · duplicate

> I'm reviewing a AppKit change for macOS 26.0. Receiving the same preference twice restarts work that should only happen on a transition. Can you avoid the repeat?

- **Diagnosis:** Pass; two tvOS copies of preference deduplication also pass. The behavior is platform-neutral.
- **Prompt:** Retire the macOS copy for development.
- **Oracle:** none
- **Skill:** none
- **Transfer:** n/a

**`G-6d1140dc450e0b`** · AppKit · duplicate-id · unaided **pass** (primary pass). Pair: both-correct. · **P2 rewrite-neutral** · no-headroom · S1

> I'm reviewing a AppKit change for macOS 26.0. The server returned duplicate IDs. Can you reject the ambiguous update without leaving a partially updated screen?

- **Diagnosis:** Defective half of a both-correct pair; passes, but the opening states the ambiguity and asks for the rejection, so it does not show the model would find the problem unprompted.
- **Prompt:** Ask what the outline shows after an update with a repeated ID, using the same words for the working twin.
- **Proposed wording:** macOS 26.0, AppKit. An outline refresh arrives with two root entries that share the ID "inbox". What does the outline show, expand and select after this update is applied? Please check the supplied code.
- **Oracle:** Assert the prior tree, expansion and selection are unchanged after the duplicate update, and that a valid update still applies.
- **Skill:** Neutral wording tests tracing the update path rather than following an instruction.
- **Transfer:** Library sidebar with a duplicate nested ID rather than at the root.

**`G-6dfa1eac517b72`** · SwiftUI · request-generation · unaided **pass** (primary pass). · **P3 retire-duplicate** · duplicate

> I'm reviewing a SwiftUI change for macOS 26.0. A late response from an earlier request overwrites a newer result. Can you give the current request ownership of the update?

- **Diagnosis:** Pass; unpaired media copy in the same package as the forms pair, same wording, nine passing siblings.
- **Prompt:** Retire; adds no signal beyond the paired copies.
- **Oracle:** none
- **Skill:** none
- **Transfer:** n/a

**`G-750ac0ab6c5c65`** · AppKit · disabled-action · unaided **pass** (primary pass). Pair: fixes-defect-breaks-working. · **P2 pair-variant** · no-headroom · S1

> I'm reviewing a AppKit change for macOS 26.0. A disabled command can still run through another activation path. Can you make the control respect its current enabled state?

- **Diagnosis:** Defective half passes (checks enabled state and exercises both paths). The pair fails only on the working twin, so this item is useful as the defective member of a pair rather than alone.
- **Prompt:** Adopt the neutral per-path wording of G-ca3035351f5e93 for both halves.
- **Oracle:** Same per-path assertions as the twin.
- **Skill:** Pair tests whether the model distinguishes a missing guard from a present one.
- **Transfer:** Keyboard-only path on a different control type.

**`G-765c7c64047507`** · SwiftUI · duplicate-binding · unaided **pass** (primary pass). Blind audit Q40: pass/pass. Pair: both-correct. · **P3 keep-control** · good-as-is · S2

> I'm reviewing a SwiftUI change for macOS 26.0. Setting the same value through the toggle binding twice should not run its change action twice. Can you check both repeated and changed writes?

- **Diagnosis:** Defective half of a both-correct pair; audit Q40 confirms pass with repeated writes interleaved with real transitions. Policy-stated question, no giveaway beyond the requirement.
- **Prompt:** none
- **Oracle:** none
- **Skill:** The test exercises repeated and changed writes with literal counts, a model for S2.
- **Transfer:** A Picker binding that writes the same selection twice.

**`G-785b435936f8de`** · SwiftUI · stale-off · unaided **pass** (primary pass). Pair: fixes-defect-breaks-working. · **P1 pair-variant** · no-headroom · S3, S7

> I'm reviewing a SwiftUI change for macOS 26.0. Choosing Off from an out-of-date menu clears captions on the replacement item. Can you prevent that?

- **Diagnosis:** Defective half passes by checking generation and ownership in a captured binding. Implementation answers on the same package (G-f48375292f98ee, G-5f436c17e0c488) let a retained Off reach the new item, so the pass reflects the stated defect.
- **Prompt:** Send both halves a neutral question: after the item is replaced, what does choosing Off from the earlier menu do to the new item's captions?
- **Oracle:** Assert the new item's legible selection is unchanged after a retained Off, and a current Off clears it when allowed.
- **Skill:** Capture the owning item when the binding is installed.
- **Transfer:** Episode autoplay replacing the item while a captions menu is open.

**`G-79b7f3ea3d3866`** · SwiftUI · rebound-action · unaided **pass** (primary pass). Pair: fixes-defect-breaks-working. · **P2 pair-variant** · no-headroom · S3

> I'm reviewing a SwiftUI change for macOS 26.0. After refreshing a row, an action captured earlier can operate on the wrong record. Can you repair the ownership without losing the current action?

- **Diagnosis:** Defective half passes: rejects an old closure after rebinding and verifies only the new action deletes. Pair: fixes defect, breaks working (twin Q35).
- **Prompt:** Use the neutral recycled-ID wording of G-32019e51844cc7 for both halves.
- **Oracle:** Same as twin.
- **Skill:** Pair tests whether the model keeps a deliberate revision guard.
- **Transfer:** Same as twin.

**`G-7ec34f4655de19`** · AppKit · off-permission · unaided **pass** (primary pass). · **P1 rewrite-neutral** · no-headroom · S7

> I'm reviewing a AppKit change for macOS 26.0. Off is shown even for a group that requires a selection. Can you honor the actual group's permission?

- **Diagnosis:** Pass with no headroom: the opening names the group's permission. Implementation answer G-917744c4992bd8 called select(nil) without checking permission, so the gap appears when unprompted.
- **Prompt:** Ask what the picker offers and does for a group that disallows empty selection, without naming the permission.
- **Proposed wording:** macOS 26.0, AppKit. This item's subtitle group doesn't allow an empty selection. What does our picker list for it, and what happens to the current subtitle if someone chooses Off? Please check the supplied code.
- **Oracle:** Assert Off is not offered (or is rejected) and the selected option and select call count are unchanged; also assert Off still works for a group that allows empty selection.
- **Skill:** Product policy on Off and the actual group's allowsEmptySelection.
- **Transfer:** Audio group (never empty) versus legible group in a lecture player.

**`G-7ffece0e97f65c`** · AppKit · edited-matches · unaided **inconclusive** (primary inconclusive). · **P2 specify-policy** · grader-uncertain · S6, S2

> I'm reviewing a AppKit change for macOS 26.0. Editing the text outside our search callback leaves old search hits active. Can you make navigation use the current content?

- **Diagnosis:** Inconclusive: the answer rebuilds matches on external edits instead of rejecting stale ranges; the grader could not establish the new delegate wiring or end-to-end ranges from source. iOS/tvOS siblings pass.
- **Prompt:** State whether an edit invalidates results or triggers a fresh search, so either design can be graded against one observable outcome.
- **Proposed wording:** macOS 26.0, AppKit. The reader's NSTextView can be edited directly or by sync while search results are shown. Product decision: after any text change the previous results are discarded and the user searches again. What does Next Match select after an edit made directly in the text view? Please check the supplied code.
- **Oracle:** Mutate textStorage without the search callback, then call next; assert no stale range is selected (or, if rebuilding is accepted, the selected substring equals the literal query). Accept either policy only if stated.
- **Skill:** Range validity after edits needs a literal substring check.
- **Transfer:** A code editor's find bar with edits from an undo operation.

**`G-809a500fb86938`** · AppKit · duplicate-completion · unaided **pass** (primary pass). · **P3 retire-duplicate** · duplicate · S3

> I'm reviewing a AppKit change for macOS 26.0. A service sometimes delivers its completion twice. Can you apply the first valid result only?

- **Diagnosis:** Pass; the prompt describes a double completion and asks to apply the first, which is the fix. iOS and tvOS copies of the same platform-neutral token logic also pass.
- **Prompt:** Retire the macOS copy; the decision is not AppKit-specific and three passing copies add no information.
- **Oracle:** none
- **Skill:** Generic completion ownership already covered elsewhere.
- **Transfer:** n/a

**`G-84ceaa1fed1f5a`** · AppKit · input-snapshot · unaided **fail** (primary pass). · **P1 specify-policy** · ambiguous-policy · S3, S2

> I'm reviewing a AppKit change for macOS 26.0. The text has changed since validation started, but the old result is still applied. Can you preserve edits and reject that reply?

- **Diagnosis:** Unlike tvOS Q54 (audit-confirmed input-snapshot miss), this answer does add a snapshot comparison and rejects the reply, so primary passes. The whole fail is that its bare return leaves the validation busy with 'Checking' status after a native-field edit; the prompt never says what state should follow a discarded reply.
- **Prompt:** State what the form should show after a stale reply is discarded, so the post-rejection state is an explicit requirement rather than a hidden one.
- **Proposed wording:** macOS 26.0, AppKit. Someone types into the name field directly while validation of the earlier text is pending, and the old reply then arrives. Product decision: a reply for text that no longer matches is ignored, and the form returns to an idle, unvalidated state so Save can be pressed again. What does the form show afterward? Please check the supplied code.
- **Oracle:** Grade rejection (no errors or acceptance from the old snapshot) and the resulting state (busy false, status not 'Checking', new submit possible) as separate criteria; edit the field through NSTextField.stringValue, not edit().
- **Skill:** The reply must validate the captured snapshot when it runs and leave the owner in a defined state.
- **Transfer:** Async username availability check in a sign-up sheet edited through field binding.

**`G-85ba67b0de42ba`** · AppKit · request-generation · unaided **pass** (primary pass). Pair: both-correct. · **P3 keep-control** · good-as-is · S3

> I'm reviewing a AppKit change for macOS 26.0. A late response from an earlier request overwrites a newer result. Can you give the current request ownership of the update?

- **Diagnosis:** Defective half of a both-correct pair (AppKit closure package); passes by checking ticket ownership and verifying the newer error survives.
- **Prompt:** none
- **Oracle:** none
- **Skill:** Pair member for the both-correct count.
- **Transfer:** Same as twin.

**`G-85f4f173cd1f69`** · AppKit · stable-selection · unaided **pass** (primary pass). · **P3 reserve-transfer** · duplicate

> I'm reviewing a AppKit change for macOS 26.0. A rename or reorder moves the selection to a different item. Can you preserve identity and clear a selection only if its item is gone?

- **Diagnosis:** Pass on the outline package (rename keeps node identity); unpaired copy of the stable-selection wording.
- **Prompt:** Reserve the outline rename shape as transfer.
- **Oracle:** none
- **Skill:** none
- **Transfer:** Renamed folder in a nested NSOutlineView library.

**`G-8effc67ffe5eaf`** · SwiftUI · unlisted-selection · unaided **pass** (primary pass). · **P2 pair-variant** · no-headroom · S7

> I'm reviewing a SwiftUI change for macOS 26.0. The player has a selection that isn't listed in our menu, and we show it as Off. Can you distinguish the states?

- **Diagnosis:** Pass with no headroom: opening asserts the unlisted selection shows as Off and asks to distinguish.
- **Prompt:** Add a working twin and ask both what the menu shows when the item's current legible selection is a forced-only track the menu does not list.
- **Oracle:** Assert the menu state is not Off and the native selection is unchanged by opening the menu.
- **Skill:** Distinguish forced, full and Off.
- **Transfer:** System-selected forced track after a language change.

**`G-9aab175a86cc9b`** · SwiftUI · optional-help · unaided **inconclusive** (primary pass). Pair: inconclusive. · **P2 grade-components** · evidence-only · S5, S2

> I'm reviewing a SwiftUI change for macOS 26.0. After switching from an item with help text to one without it, the old help is still there. Can you repair the update path?

- **Diagnosis:** Inconclusive with primary pass: correctly clears NSAccessibility help on nil, but adds an assertion of accessibilityHint, an iOS-style API with no applicable AppKit counterpart, so the evidence cannot compile as written.
- **Prompt:** Use the neutral wording of G-288d76b52153df.
- **Oracle:** Grade primary (help nil after B) separately from evidence; an iOS-only API in an AppKit test is an evidence defect, not a primary failure.
- **Skill:** AppKit help vs UIKit hint is an on-demand platform fact.
- **Transfer:** Same as twin.

**`G-a12b5e1af9ae26`** · AppKit · ordinary-action · unaided **pass** (primary pass). Pair: fixes-defect-breaks-working. · **P2 pair-variant** · no-headroom · S2

> I'm reviewing a AppKit change for macOS 26.0. The added shortcut works but the ordinary action no longer does. Can you keep both paths working on the current item?

- **Diagnosis:** Defective half passes: connects the native save target and selector and checks dispatch.
- **Prompt:** Send with the same neutral per-path question as the working twin G-488bc12a7f090e.
- **Oracle:** Assert performClick on the native button reaches the current item once, and the shortcut too.
- **Skill:** Exercise the installed native action.
- **Transfer:** Same as twin.

**`G-a29555e4cd763e`** · AppKit · description-selection · unaided **pass** (primary pass). · **P2 pair-variant** · no-headroom · S7, S1

> I'm reviewing a AppKit change for macOS 26.0. When someone asks for described audio and no matching track exists, keep the previous choice. Does the picker do that?

- **Diagnosis:** Pass; the prompt already states the policy and asks whether the code honors it, a near-neutral form. tvOS sibling G-7cc5d89371a12a fails on the same decision, so the macOS pass shows the task is learnable rather than easy everywhere.
- **Prompt:** Keep the wording; add a working twin of DescriptionIgnored so a 'does it do that?' question also has a correct no-change answer.
- **Oracle:** Assert the previous selected option is unchanged when no described match exists, and that a described match is selected when one exists.
- **Skill:** Media selection policy with a preserved previous choice.
- **Transfer:** A language-plus-description request in an audiobook app with a single described track in another language.

**`G-a978e18a8f821c`** · AppKit · forced-vs-full · unaided **inconclusive** (primary pass). Pair: inconclusive. · **P2 repair-oracle** · grader-uncertain · S7, S2

> I'm reviewing a AppKit change for macOS 26.0. Our captions menu offers a forced-only translation as if it were full subtitles. Can you keep those choices distinct?

- **Diagnosis:** Inconclusive with primary pass: separates forced, full and described selection, but verification depends on unconfirmed doubles of AVFoundation option objects. Pair with G-c4d71a0f3c4363 is inconclusive.
- **Prompt:** Use the neutral wording of the working twin.
- **Oracle:** Supply the real-group fixture approach (tagged silent local asset) in the controller so the grader can check selection against actual AVMediaSelectionOption values; grade double-based tests as unverified evidence, not as failure.
- **Skill:** Media selection evidence must come from the actual item's group.
- **Transfer:** Same decision with a group loaded from a different asset composition.

**`G-aa17ddeb7ea6b0`** · SwiftUI · binding-disconnect · unaided **pass** (primary pass). · **P1 rewrite-neutral** · no-headroom · S7, S2

> I'm reviewing a SwiftUI change for macOS 26.0. A change in the track picker doesn't reach the current player item. Can you connect the existing control to the actual selection?

- **Diagnosis:** Pass with no headroom: the prompt names the missing connection and asks for it. Implementation tasks on the same media package (G-9cb4d6bc27fab4, G-917744c4992bd8) fail on exactly this native write, so the gap appears once the request is not spelled out.
- **Prompt:** Replace the stated defect and fix with a question about the observable selection on the player item; pair with a working-binding fixture.
- **Proposed wording:** macOS 26.0, SwiftUI. When someone picks a caption track in this menu, what does the current AVPlayerItem's legible selection become, and what does the menu show afterward? Please check it against the supplied code.
- **Oracle:** Assert the actual item's legible-group selection after the binding set, using a tagged local asset; also assert the audio selection is unchanged.
- **Skill:** Writing the real player item's selection is the behavior that implementation tasks miss.
- **Transfer:** A different picker host (inspector popover or menu bar extra) driving an injected selection writer.

**`G-aa1b31a67804d8`** · AppKit · key-eligibility · unaided **pass** (primary pass). · **P2 pair-variant** · no-headroom

> I'm reviewing a AppKit change for macOS 26.0. Tab navigation takes users to an unavailable control. Can you repair the chain when eligibility changes?

- **Diagnosis:** Pass with no headroom: the opening names the symptom and asks to repair the chain; no working twin exists for this macOS-specific key-view behavior.
- **Prompt:** Add a working twin whose helper already recomputes eligibility, and ask both which controls Tab visits after a button becomes unavailable.
- **Oracle:** Assert the nextKeyView cycle after toggling isEnabled and isHidden, for both twins; grade edits on the working twin as rework.
- **Skill:** none
- **Transfer:** Inspector form where a field becomes hidden by a disclosure rather than disabled.

**`G-acfc996c4937b6`** · AppKit · range-kind · unaided **pass** (primary pass). Pair: fixes-defect-breaks-working. · **P2 pair-variant** · no-headroom · S1

> I'm reviewing a AppKit change for macOS 26.0. The player says I can seek through an interval that was only buffered. How should the inspector describe these two ranges?

- **Diagnosis:** Defective half passes by using seekable intervals and checking a buffered-only time.
- **Prompt:** Use the concrete-range neutral wording of G-2eae2be1113db6 for both halves.
- **Oracle:** Same as twin.
- **Skill:** Pair isolates detection.
- **Transfer:** Same as twin.

**`G-b1a04db3512aad`** · AppKit · disabled-action · unaided **pass** (primary pass). · **P3 reserve-transfer** · duplicate · S1

> I'm reviewing a AppKit change for macOS 26.0. A disabled command can still run through another activation path. Can you make the control respect its current enabled state?

- **Diagnosis:** Pass on a different package (macos-appkit-v1 DisabledShortcut) with the same wording as the closure-details pair; it adds no distinct evidence while unpaired.
- **Prompt:** Hold this fixture shape out as an AppKit transfer for disabled-action once the neutral wording is frozen; do not use it for development.
- **Oracle:** none
- **Skill:** Same disabled-path decision with a shortcut shape.
- **Transfer:** Accessibility shortcut on a Save button in a file list instead of a toggle.

**`G-b70bfe64ddd372`** · AppKit · grapheme-boundary · unaided **pass** (primary pass). Pair: both-correct. · **P3 keep-control** · good-as-is · S6

> I'm reviewing a AppKit change for macOS 26.0. A match covering only part of a composed character should not be offered as a navigation destination. Does this code enforce that?

- **Diagnosis:** Defective half of a both-correct pair; the question is already neutral ('Does this code enforce that?') and the answer requires both boundaries and rejects an isolated combining mark.
- **Prompt:** none
- **Oracle:** none
- **Skill:** Tests literal grapheme-boundary rejection.
- **Transfer:** Combining accent on a Latin base in a rotor search over a long document.

**`G-b804b26131dda0`** · SwiftUI · forced-vs-full · unaided **inconclusive** (primary inconclusive). Pair: inconclusive. · **P1 specify-policy** · ambiguous-policy · S7

> I'm reviewing a SwiftUI change for macOS 26.0. Our captions menu offers a forced-only translation as if it were full subtitles. Can you keep those choices distinct?

- **Diagnosis:** Inconclusive: distinguishes forced options by name but still lists them; the grader notes the outcome depends on whether the picker admits separate forced choices, which the prompt does not say (same ambiguity as audit Q03).
- **Prompt:** State the full-only menu policy, matching the working twin's revised wording.
- **Proposed wording:** macOS 26.0, SwiftUI. This macOS SwiftUI menu offers full subtitles only. If a forced-only track is already active, opening the menu must leave it active. Does this code preserve that policy?
- **Oracle:** Same as G-65558ea85abec1: full offered, forced excluded, native selection unchanged through production refresh.
- **Skill:** Product policy for subtitle menus.
- **Transfer:** Same as twin.

**`G-be25d510c5ffe5`** · AppKit · eligible-target · unaided **fail** (primary fail). Blind audit Q07: fail/fail. · **P0 pair-variant** · real-model-gap · S4, S2

> I'm reviewing a AppKit change for macOS 26.0. After a refresh the original focus target may no longer belong here. Can you restore only to a usable target or fallback?

- **Diagnosis:** Audit Q07 confirmed eligible-target gap: an enabled visible original can refuse first responder; the answer claims it is eligible, consumes the token on it and misses the fallback. Its tests cover a removed primary instead.
- **Prompt:** Keep the wording and add a working twin that already checks acceptsFirstResponder, so the pair measures detection of the refusal case.
- **Oracle:** Fixture: original attached, visible, enabled but acceptsFirstResponder false; assert the request goes once to the eligible fallback. A test with a removed original does not count as evidence for this case.
- **Skill:** Restoration must check eligibility of the destination at completion; the test exercised the wrong condition.
- **Transfer:** A sheet whose opener becomes a non-editable label, or a collection item view that refuses first responder.

**`G-c002311bfa9f2d`** · AppKit · rebound-action · unaided **pass** (primary pass). · **P3 reserve-transfer** · duplicate · S3

> I'm reviewing a AppKit change for macOS 26.0. After refreshing a row, an action captured earlier can operate on the wrong record. Can you repair the ownership without losing the current action?

- **Diagnosis:** AppKit pass: captured revision and enabled state guard stale shortcuts with literal false/true results. Unpaired, same wording as the SwiftUI pair.
- **Prompt:** Reserve as the AppKit transfer for rebound-action.
- **Oracle:** none
- **Skill:** Retained AppKit custom action ownership.
- **Transfer:** NSAccessibilityCustomAction on a reused NSTableCellView.

**`G-c3bf6cb5f65bd5`** · AppKit · eligible-target · unaided **pass** (primary pass). Pair: both-correct. · **P3 keep-control** · good-as-is · S4

> I'm reviewing a AppKit change for macOS 26.0. After a refresh the original focus target may no longer belong here. Can you restore only to a usable target or fallback?

- **Diagnosis:** Defective half of a both-correct pair; passes by checking membership and usability. Guards the foreign-target branch of an audit-confirmed key.
- **Prompt:** none
- **Oracle:** none
- **Skill:** Membership check of the destination owner.
- **Transfer:** Target moved into a different window's view hierarchy.

**`G-c3d45de5f9f91e`** · SwiftUI · request-generation · unaided **pass** (primary pass). · **P2 pair-variant** · no-headroom · S3

> I'm reviewing a SwiftUI change for macOS 26.0. After reloading track choices, a late error from the previous load sometimes replaces a successful result. Is this handled?

- **Diagnosis:** Pass on a question that is already near-neutral ('Is this handled?'); compares the active ticket and item identity. No working twin.
- **Prompt:** Keep the wording; add a working twin of this media-macos-v1 fixture.
- **Oracle:** Assert a late earlier failure cannot replace the later success, and the later success is shown.
- **Skill:** Ticket and item validation at completion.
- **Transfer:** Thumbnail reload with a late error from an earlier folder.

**`G-cd41da12692601`** · AppKit · unavailable-media · unaided **pass** (primary pass). · **P2 pair-variant** · no-headroom · S2

> I'm reviewing a AppKit change for macOS 26.0. Opening the inspector before an item arrives says there are no accessible tracks. Can we distinguish not loaded from a successful empty result?

- **Diagnosis:** Pass with no headroom: opening names both states to distinguish. iOS sibling fails, so a twin could show headroom.
- **Prompt:** Add a working twin and ask both what the inspector reports when opened with no current item and with an item that has no accessible tracks.
- **Oracle:** Assert distinct literal states for no item and loaded-empty.
- **Skill:** Positive fixture for each state before asserting absence.
- **Transfer:** Chapter inspector opened before the asset loads.

**`G-d7c0029e469f04`** · AppKit · observer-stop · unaided **pass** (primary pass). · **P2 pair-variant** · no-headroom · S3

> I'm reviewing a AppKit change for macOS 26.0. An observer keeps reacting after the screen stops listening. Can you make teardown and a subsequent restart reliable?

- **Diagnosis:** Pass with no headroom: opening asserts the observer keeps reacting and asks to make teardown reliable.
- **Prompt:** Add a working twin and ask both what a delivery queued before stop does after stop and after restart.
- **Oracle:** Assert zero applications after stop and exactly the new generation's after restart.
- **Skill:** Captured revision checked when queued work runs.
- **Transfer:** Pasteboard or appearance observer in a menu bar app.

**`G-df44d427667921`** · AppKit · stable-selection · unaided **pass** (primary pass). · **P3 retire-duplicate** · duplicate

> I'm reviewing a AppKit change for macOS 26.0. A rename or reorder moves the selection to a different item. Can you preserve identity and clear a selection only if its item is gone?

- **Diagnosis:** Pass; third macOS copy of the same wording, same outline package as G-85f4f173cd1f69.
- **Prompt:** Retire; redundant with the paired navigation copy and the reserved outline copy.
- **Oracle:** none
- **Skill:** none
- **Transfer:** n/a

**`G-e2f418e34deaed`** · SwiftUI · interop-rebind · unaided **pass** (primary pass). · **P3 reserve-transfer** · duplicate · S3

> I'm reviewing a SwiftUI change for macOS 26.0. The wrapper updates its SwiftUI state but the native button can still send to the previous target. Can you fix the binding and teardown?

- **Diagnosis:** Pass on a different package (macos-v1 coordinator ticket) with the same wording; iOS and tvOS preservation siblings fail on rework (Q41, Q43), so the wording itself provokes edits.
- **Prompt:** Reserve this coordinator shape as transfer for interop-rebind after the neutral wording is frozen.
- **Oracle:** none
- **Skill:** Coordinator ownership of native callbacks.
- **Transfer:** Coordinator rebound to a different NSButton instance rather than a new target.

**`G-e3e80d94c9386e`** · AppKit · row-role · unaided **pass** (primary pass). Pair: fixes-defect-breaks-working. · **P2 pair-variant** · no-headroom · S5

> I'm reviewing a AppKit change for macOS 26.0. Can the table row describe its role and selection without swallowing its actionable children?

- **Diagnosis:** Defective half passes: forwards selected into the row setter and keeps the child button. Pair: fixes defect, breaks working.
- **Prompt:** Keep the same question for both halves; it is already neutral.
- **Oracle:** Same exposure assertions as the twin.
- **Skill:** Pair isolates the row-element fact.
- **Transfer:** Same as twin.

**`G-e44302507e2dc9`** · AppKit · observer-restart · unaided **inconclusive** (primary pass). · **P2 repair-oracle** · oracle-mismatch · S2, S3

> I'm reviewing a AppKit change for macOS 26.0. After stopping and restarting preference observation, queued work from the old subscription must not change this screen. Does the code handle that?

- **Diagnosis:** Inconclusive with primary pass: guards queued work by subscription revision, but deduplication can mask a stale read if the test's stale value equals the current one, so the grader could not see the guard act.
- **Prompt:** none for wording.
- **Oracle:** Make the queued old-generation value differ from the current setting (e.g. old reduceMotion true, new false) and assert the screen keeps the new value; the guard is then observable apart from deduplication.
- **Skill:** A positive fixture is needed before a 'nothing changed' assertion means anything.
- **Transfer:** Accessibility display options observer restarted by window reattach.

**`G-f957660ac921ec`** · SwiftUI · motion-policy · unaided **pass** (primary pass). Pair: both-correct. · **P3 retire-duplicate** · duplicate

> I'm reviewing a SwiftUI change for macOS 26.0. The optional effect still plays when the person asks for reduced motion. Can we honor their setting without changing the normal experience?

- **Diagnosis:** Defective half of a both-correct pair (macos-v1 Preferences); passes by deriving permission from Reduce Motion. A second motion pair on macOS duplicates the decision.
- **Prompt:** Retire this defective copy; keep its working twin G-99daa9542b74b4 as a no-change control and use the forwarding-macos-v1 pair (G-2cf913ca90235b/G-6d5107426a2b49) for the discriminating signal.
- **Oracle:** none
- **Skill:** none
- **Transfer:** n/a

**`G-fc281c11932789`** · AppKit · redundant-notification · unaided **pass** (primary pass). · **P2 pair-variant** · no-headroom · S8

> I'm reviewing a AppKit change for macOS 26.0. Reapplying an unchanged value generates another change event. Can we notify once for a real transition?

- **Diagnosis:** Pass with no headroom: opening asserts a duplicate change event and asks to notify once. iOS sibling G-9dc2d66 fails, so the decision has cross-platform headroom.
- **Prompt:** Add a working twin that already posts once, and ask both how many notifications reapplying an unchanged status produces.
- **Oracle:** Assert notification count 1 for a change and 0 for a repeat via an injected poster; grade added notifications on the twin as rework.
- **Skill:** Don't add notifications where the existing path already posts once.
- **Transfer:** Progress label updated by a timer with repeated identical text.

#### macOS · preservation (23)

**`G-0b3af5810782d2`** · SwiftUI · request-generation · unaided **pass** (primary pass). Pair: both-correct. · **P3 keep-control** · good-as-is · S1, S3

> I'm reviewing a SwiftUI change for macOS 26.0. A late response from an earlier request overwrites a newer result. Can you give the current request ownership of the update?

- **Diagnosis:** Working half of a both-correct pair: preserves request checks and exercises stale validation and media delivery.
- **Prompt:** none
- **Oracle:** none
- **Skill:** No-change control for request ownership.
- **Transfer:** Search-as-you-type results in a sidebar.

**`G-288d76b52153df`** · SwiftUI · optional-help · unaided **fail** (primary fail). Blind audit Q22: fail/fail. Pair: inconclusive. · **P1 rewrite-neutral** · real-model-gap · S1, S5

> I'm reviewing a SwiftUI change for macOS 26.0. After switching from an item with help text to one without it, the old help is still there. Can you repair the update path?

- **Diagnosis:** Audit Q22 confirms a preservation regression: the update already forwards the optional hint unconditionally, but the answer maps absent help to an empty string, hides the difference in its assertion, and claims without support that AppKit ignores nil.
- **Prompt:** The opening asserts that old help persists on working code; ask what the hosted view reports after an in-place update instead.
- **Proposed wording:** macOS 26.0, SwiftUI. Our wrapper shows item A with help "Opens offline" and is then updated in place to item B, which has no help. What does the hosted NSView report for its accessibility help after the update? Please check the supplied code.
- **Oracle:** Assert accessibilityHelp() is nil (not empty) after B; grade unsupported API claims as evidence errors separate from primary.
- **Skill:** Accepting a false symptom led to a regression; nil vs empty help is a precise AppKit fact.
- **Transfer:** Tooltip-backed help on a toolbar item reused for different documents.

**`G-2ce035ce792599`** · AppKit · eligible-target · unaided **pass** (primary pass). Blind audit Q06: pass/pass. Pair: both-correct. · **P3 keep-control** · good-as-is · S4, S1

> I'm reviewing a AppKit change for macOS 26.0. After a refresh the original focus target may no longer belong here. Can you restore only to a usable target or fallback?

- **Diagnosis:** Working half of a both-correct pair; audit Q06 confirms it checks hierarchy, visibility, responder eligibility and enabled status at completion and leaves code intact.
- **Prompt:** none
- **Oracle:** Optionally assert the actual restored view, not only request identity.
- **Skill:** A preserved eligible-target control for restoration.
- **Transfer:** Popover dismissal in a different window owner.

**`G-2eae2be1113db6`** · AppKit · range-kind · unaided **fail** (primary pass). Blind audit Q60: fail/pass. Pair: fixes-defect-breaks-working. · **P1 rewrite-neutral** · symptom-as-fact · S1, S8

> I'm reviewing a AppKit change for macOS 26.0. The player says I can seek through an interval that was only buffered. How should the inspector describe these two ranges?

- **Diagnosis:** Audit Q60: correctly distinguishes seekable from buffered, but adds a query to an inspector whose public loaded ranges and seekable-only check already answer the question. Pair: fixes defect, breaks working.
- **Prompt:** The opening asserts the player claims an unbuffered interval is seekable; give concrete ranges and ask what the inspector reports.
- **Proposed wording:** macOS 26.0, AppKit. The item has loaded 0-40 s and a seekable range of 0-20 s. What does our inspector report for 30 s, and would it allow a seek there? Please check the supplied code.
- **Oracle:** Assert 30 s is reported buffered but not seekable, and 10 s both; grade an added public query as rework.
- **Skill:** The existing inspector already answered the request.
- **Transfer:** Live stream with a sliding seekable window in a sports app.

**`G-32019e51844cc7`** · SwiftUI · rebound-action · unaided **fail** (primary fail). Blind audit Q35: fail/fail. Pair: fixes-defect-breaks-working. · **P0 rewrite-neutral** · real-model-gap · S3, S1, S2

> I'm reviewing a SwiftUI change for macOS 26.0. After refreshing a row, an action captured earlier can operate on the wrong record. Can you repair the ownership without losing the current action?

- **Diagnosis:** Audit Q35 confirms a preservation regression: removing the deliberate revision check lets a retained action select or delete a replacement with a recycled ID, and the answer's test explicitly expects the stale action to succeed. The asserted symptom on working code invited the change.
- **Prompt:** Ask which record a retained action affects after a refresh that reuses the ID, instead of asserting it hits the wrong record and asking for repair.
- **Proposed wording:** macOS 26.0, SwiftUI. A row's Delete action is captured, then the list refreshes and a different document now uses that row's ID. Which document, if any, does the earlier Delete affect, and which does the current row's Delete affect? Please check the supplied code.
- **Oracle:** Assert the retained action is a no-op on the replacement and the current action deletes once. A test expecting the stale action to succeed is an evidence failure that reverses the contract.
- **Skill:** The captured revision must be validated when the action runs; the answer removed it and certified the wrong behavior.
- **Transfer:** AppKit table row menu action retained by a menu that stays open across refresh.

**`G-33543d74420875`** · SwiftUI · duplicate-binding · unaided **pass** (primary pass). Pair: both-correct. · **P3 keep-control** · good-as-is · S1

> I'm reviewing a SwiftUI change for macOS 26.0. Setting the same value through the toggle binding twice should not run its change action twice. Can you check both repeated and changed writes?

- **Diagnosis:** Working half of a both-correct pair: recognizes and verifies the existing duplicate and disabled guard. The prompt states the policy neutrally.
- **Prompt:** none
- **Oracle:** none
- **Skill:** Shows the model can leave a working binding guard alone.
- **Transfer:** Slider or stepper binding with repeated identical writes.

**`G-488bc12a7f090e`** · AppKit · ordinary-action · unaided **fail** (primary fail). Blind audit Q09: fail/pass. Pair: fixes-defect-breaks-working. · **P1 grade-components** · rework-only · S8, S2, S1

> I'm reviewing a AppKit change for macOS 26.0. The added shortcut works but the ordinary action no longer does. Can you keep both paths working on the current item?

- **Diagnosis:** Audit Q09 reverses the primary: native Open and Save still work (blind primary pass), but duplicating Open in the custom action list changes the menu, and the test calls two custom handlers without pressing the ordinary button. Pair: fixes defect, breaks working.
- **Prompt:** Also replace the asserted symptom ('the ordinary action no longer does') with a question about what each path invokes.
- **Oracle:** Grade primary (ordinary press and shortcut both reach the current item), rework (extra custom actions) and evidence (the test must perform the native button's action) separately.
- **Skill:** The model added a custom action that a native button already answered and never exercised the ordinary path.
- **Transfer:** Toolbar button plus keyboard shortcut in a mail viewer.

**`G-49d48cb3a1f089`** · AppKit · duplicate-id · unaided **pass** (primary pass). Pair: both-correct. · **P3 keep-control** · good-as-is · S1

> I'm reviewing a AppKit change for macOS 26.0. The server returned duplicate IDs. Can you reject the ambiguous update without leaving a partially updated screen?

- **Diagnosis:** Working half of a both-correct pair: identifies the preflight duplicate-ID guard and checks the outline is unchanged.
- **Prompt:** none
- **Oracle:** none
- **Skill:** A no-change control for an atomic outline update.
- **Transfer:** Nested sidebar sections with duplicate child IDs.

**`G-53503b19ad4b70`** · AppKit · grapheme-boundary · unaided **pass** (primary pass). Pair: both-correct. · **P3 keep-control** · good-as-is · S6, S1

> I'm reviewing a AppKit change for macOS 26.0. A match covering only part of a composed character should not be offered as a navigation destination. Does this code enforce that?

- **Diagnosis:** Working half of a both-correct pair: uses the existing start/end boundary checks to explain exclusion of partial matches and leaves the code alone.
- **Prompt:** none
- **Oracle:** none
- **Skill:** Composed-character boundaries at the NSString boundary; preserved working code.
- **Transfer:** Search over a family emoji or flag sequence in an NSTextView-backed notes app.

**`G-5c8c9ba78d4db8`** · SwiftUI · interop-rebind · unaided **fail** (primary pass). Blind audit Q27: fail/pass. Pair: fixes-defect-breaks-working. · **P1 rewrite-neutral** · symptom-as-fact · S1, S8, S3

> I'm reviewing a SwiftUI change for macOS 26.0. The wrapper updates its SwiftUI state but the native button can still send to the previous target. Can you fix the binding and teardown?

- **Diagnosis:** Audit Q27: configure already detaches the old target and stop clears target, action and handler; the answer repeats cleanup and tests teardown alone. Pair: fixes defect, breaks working.
- **Prompt:** The opening asserts that the native button still sends to the previous target and asks to fix it; ask what each button reaches after update and dismantle.
- **Proposed wording:** macOS 26.0, SwiftUI. Our NSViewRepresentable button is updated with a new item's action, and later dismantled. After each step, which handler does a click on the earlier NSButton reach, and which does the current one reach? Please check the supplied code.
- **Oracle:** Drive update then dismantle through the representable's coordinator; assert old sends nothing, current sends once, none after dismantle. Grade duplicated cleanup as rework only.
- **Skill:** The supplied lifecycle already satisfied the request.
- **Transfer:** NSPopUpButton or NSSegmentedControl wrapper rebound to a different document.

**`G-65558ea85abec1`** · SwiftUI · forced-vs-full · unaided **fail** (primary fail). Blind audit Q03: fail/pass. Pair: inconclusive. · **P0 specify-policy** · ambiguous-policy · S7, S1, S2

> I'm reviewing a SwiftUI change for macOS 26.0. Our captions menu offers a forced-only translation as if it were full subtitles. Can you keep those choices distinct?

- **Diagnosis:** Audit Q03: labeling a forced option distinctly is a plausible reading, so the original primary fail does not hold (blind primary pass); its test never completes loading. Factorial full-captions: the review sentence turned primary pass in 2 of 4 arms but no arm passed whole.
- **Prompt:** State the menu policy (full subtitles only; a pre-selected forced track remains active) as the factorial child does.
- **Proposed wording:** macOS 26.0, SwiftUI. This macOS SwiftUI menu offers full subtitles only. If a forced-only track is already active, opening the menu must leave it active. Does this code preserve that policy?
- **Oracle:** Use a known full option and a different forced-only option already selected; through production refresh assert full is offered, forced excluded and the native selection unchanged. Do not infer Off from a nil display ID. Grade the loading-never-completes test as evidence.
- **Skill:** Forced vs full is a product-policy distinction; the review sentence helped primary behavior here.
- **Transfer:** Audiobook or lecture player with a forced-only sign-language caption track.

**`G-6d5107426a2b49`** · SwiftUI · motion-policy · unaided **fail** (primary pass). Blind audit Q33: fail/pass. Pair: fixes-defect-breaks-working. · **P1 rewrite-neutral** · symptom-as-fact · S1, S8

> I'm reviewing a SwiftUI change for macOS 26.0. The optional effect still plays when the person asks for reduced motion. Can we honor their setting without changing the normal experience?

- **Diagnosis:** Audit Q33: the button reads the current environment at action time and the store already guards the effect; the answer requires view-level synchronization for an invented external caller. Pair: fixes defect, breaks working.
- **Prompt:** The opening asserts the effect still plays under reduced motion; ask what happens with each setting.
- **Proposed wording:** macOS 26.0, SwiftUI. With Reduce Motion on, someone presses Highlight. What final state does the store record, and does the optional pulse effect run? What happens with Reduce Motion off? Please check the supplied code.
- **Oracle:** Assert final state recorded in both settings and the effect callback count (0 vs 1); grade new preference forwarding as rework.
- **Skill:** The existing path already honored the setting.
- **Transfer:** A celebratory confetti effect on task completion in a to-do app.

**`G-79fa7510bdf4bc`** · SwiftUI · presentation-owner · unaided **fail** (primary pass). Blind audit Q10: fail/fail. Pair: fixes-defect-breaks-working. · **P0 rewrite-neutral** · real-model-gap · S3, S2, S4

> I'm reviewing a SwiftUI change for macOS 26.0. A delayed close callback can restore focus for a presentation that has already been replaced. Can you fix that race?

- **Diagnosis:** Audit Q10 flips the original primary pass: the view callback still reads mutable ticket state, so a late A dismissal can present B's ticket to a guard that accepts it; the test supplies the old ticket by hand. Factorial dismiss-owner: all four arms fail whole and primary.
- **Prompt:** Ask the delayed-dismissal question directly, as the factorial child does, rather than asserting a race and asking to fix it.
- **Proposed wording:** macOS 26.0, SwiftUI. Sheet A starts closing, then this view presents B. A delayed dismissal from A arrives. Can it change focus or close B?
- **Oracle:** Exercise a retained A dismissal from the view wiring (or its production-used seam) after B opens: A cannot close B, alter focus or request restoration; a valid B completion restores once. A model test passing the old ticket by hand is not evidence.
- **Skill:** The callback must capture its own presentation when installed; the proof must run the installed closure.
- **Transfer:** AppKit sheet or popover replaced from a toolbar while the first is dismissing.

**`G-7fed584f0f2a04`** · SwiftUI · stale-off · unaided **fail** (primary pass). Blind audit Q36: fail/pass. Pair: fixes-defect-breaks-working. · **P1 grade-components** · rework-only · S1, S8, S7, S2

> I'm reviewing a SwiftUI change for macOS 26.0. Choosing Off from an out-of-date menu clears captions on the replacement item. Can you prevent that?

- **Diagnosis:** Audit Q36: primary pass, but generation-tagged Off changes the current choose(nil) contract on code whose binding already rejects old writes; TestMediaGroup is undefined and the test never selects and verifies replacement captions.
- **Prompt:** Replace the asserted symptom with a question about what a stale Off does to the replacement item.
- **Oracle:** Grade primary (old Off leaves replacement captions selected), rework (changed public contract) and evidence (compilable fixture that selects replacement captions then asserts they remain) separately.
- **Skill:** The binding already captured the item; the answer rebuilt it and proved nothing about the replacement.
- **Transfer:** Stale audio-track menu after switching episodes.

**`G-81142f68b0d10b`** · AppKit · stable-selection · unaided **pass** (primary pass). Pair: both-correct. · **P3 keep-control** · good-as-is · S1

> I'm reviewing a AppKit change for macOS 26.0. A rename or reorder moves the selection to a different item. Can you preserve identity and clear a selection only if its item is gone?

- **Diagnosis:** Working half of a both-correct pair: concludes the reload/reselect sequence already preserves the item by ID.
- **Prompt:** none
- **Oracle:** none
- **Skill:** No-change control for stable selection.
- **Transfer:** Mail list reordered by date.

**`G-99daa9542b74b4`** · SwiftUI · motion-policy · unaided **pass** (primary pass). Blind audit Q15: pass/pass. Pair: both-correct. · **P3 keep-control** · good-as-is · S1

> I'm reviewing a SwiftUI change for macOS 26.0. The optional effect still plays when the person asks for reduced motion. Can we honor their setting without changing the normal experience?

- **Diagnosis:** Working half of a both-correct pair; audit Q15 confirms it traces the environment into the animation policy and leaves normal animation alone.
- **Prompt:** none
- **Oracle:** none
- **Skill:** Restraint on a working reduced-motion policy.
- **Transfer:** Same as G-6d5107426a2b49.

**`G-9ce845a566d425`** · AppKit · row-role · unaided **fail** (primary fail). Blind audit Q12: fail/fail. Pair: fixes-defect-breaks-working. · **P0 repair-oracle** · real-model-gap · S5, S1

> I'm reviewing a AppKit change for macOS 26.0. Can the table row describe its role and selection without swallowing its actionable children?

- **Diagnosis:** Audit Q12 confirms the fail: the answer marks the row not an accessibility element, flattening the requested row semantics, and its test checks getters on an ignored object. An AppKit row can be an element and have children, so the supplied code (role row, children [open]) was working.
- **Prompt:** Keep the neutral question; add the reminder that the row and its Open button are both required, already implied.
- **Oracle:** Assert isAccessibilityElement() is true, role is .row, selected and expanded reflect configure, and accessibilityChildren contains the Open button with its contextual label. Getter values on an ignored element do not establish exposure.
- **Skill:** AppKit row element-with-children is a precise platform fact; iOS container intuitions do not transfer.
- **Transfer:** NSOutlineView group row with a Show/Hide button child.

**`G-b98a54650bda64`** · AppKit · invalid-submit · unaided **pass** (primary pass). Pair: both-correct. · **P3 keep-control** · good-as-is · S1

> I'm reviewing a AppKit change for macOS 26.0. An invalid entry still reaches Save. Can you show the validation result and keep the user's input without submitting it?

- **Diagnosis:** Working half of a both-correct pair: explains the validation-before-save path and verifies input survives.
- **Prompt:** none
- **Oracle:** none
- **Skill:** No-change control for invalid submission.
- **Transfer:** Preferences field with a numeric range validator.

**`G-be8ab365c3ca77`** · AppKit · audio-description-tag · unaided **fail** (primary pass). Blind audit Q50: fail/pass. Pair: both-fail. · **P1 rewrite-neutral** · symptom-as-fact · S1, S8, S2

> I'm reviewing a AppKit change for macOS 26.0. The audio inspector calls ordinary language tracks described audio. How can we identify the marked options?

- **Diagnosis:** Working-code half of the audio-description fixture. Audit Q50 confirms primary pass (characteristic check kept) but the answer adds public conformances and initializer changes, and its test infers ground truth from English display names; pair: both halves fail, for different reasons.
- **Prompt:** The opening asserts that ordinary tracks are called described, which is false for this code and invites a rewrite. Ask what the inspector reports for named tracks instead.
- **Proposed wording:** macOS 26.0, AppKit. Our audio inspector lists an English main track, a Spanish dub and an English track tagged for audio description. Which of these does it report as described audio, and how could a unit test confirm that?
- **Oracle:** Grade primary (only the tagged option reports described; forced/selected fields unchanged), rework (public API or initializer changes) and evidence (truth taken from the media characteristic, not display names) separately.
- **Skill:** The answer kept the correct characteristic check but rewrote a working model and proved it with name-derived ground truth.
- **Transfer:** Use a different metadata consumer, e.g. a podcast chapter inspector or a menu builder, with a tagged non-English described track.

**`G-c4d71a0f3c4363`** · AppKit · forced-vs-full · unaided **fail** (primary pass). Blind audit Q59: fail/pass. Pair: inconclusive. · **P1 rewrite-neutral** · rework-only · S1, S8, S7

> I'm reviewing a AppKit change for macOS 26.0. Our captions menu offers a forced-only translation as if it were full subtitles. Can you keep those choices distinct?

- **Diagnosis:** Audit Q59: default full-subtitle selection already excludes forced-only tracks; the answer adds a public selection mode and fake AVFoundation option doubles that presuppose a usable super.init. Primary pass, whole fail on rework and evidence.
- **Prompt:** Replace the asserted symptom with a question about which option English selection writes.
- **Proposed wording:** macOS 26.0, AppKit. The asset has English full subtitles and an English forced-only track. When a viewer chooses English from our subtitle menu, which option becomes selected in the item's legible group? Please check the supplied code.
- **Oracle:** Assert the selected legible option is the full one using a real tagged local asset; grade added public API as rework and fake framework subclasses as invalid evidence.
- **Skill:** The answer added an API to a working selection path.
- **Transfer:** A language picker in a lecture app with forced-only translation of on-screen text.

**`G-ca3035351f5e93`** · AppKit · disabled-action · unaided **fail** (primary pass). Blind audit Q42: fail/pass. Pair: fixes-defect-breaks-working. · **P1 rewrite-neutral** · symptom-as-fact · S1, S8

> I'm reviewing a AppKit change for macOS 26.0. A disabled command can still run through another activation path. Can you make the control respect its current enabled state?

- **Diagnosis:** Audit Q42: keyboard, mouse and accessibility paths already call the guarded activate method; the answer adds a performClick override inventing new enabled behavior. Pair: fixes defect, breaks working.
- **Prompt:** The opening asserts that a disabled command still runs; ask what each activation path does while disabled.
- **Proposed wording:** macOS 26.0, AppKit. This custom toggle can be operated by click, Space/Return and the accessibility press action. With isEnabled set to false, what does each path do to its state and callback? Please check the supplied code.
- **Oracle:** Assert state and callback count for each path with enabled false and true. Score an added override on the working twin as rework, not regression, unless it changes enabled behavior.
- **Skill:** The existing guarded path already answered the request; the override was unneeded.
- **Transfer:** A disabled menu-backed command or toolbar item rather than a checkbox.

**`G-d408fed70240bf`** · AppKit · conflicting-state-text · unaided **fail** (primary pass). Blind audit Q29: fail/pass. Pair: fixes-defect-breaks-working. · **P1 rewrite-neutral** · symptom-as-fact · S1, S8

> I'm reviewing a AppKit change for macOS 26.0. The control state changes but its status text tells a different story. Can you keep the two consistent on successive updates?

- **Diagnosis:** Audit Q29: both supplied controls already derive status from state; the answer refactors SemanticToggle and adds a notification. Pair: fixes defect, breaks working. The nominated assertion concerns RegionState, a control the question never names.
- **Prompt:** Ask what each named control exposes after successive transitions instead of asserting conflicting text, and name both controls so the oracle and question match.
- **Proposed wording:** macOS 26.0, AppKit. This view has a region selector and a semantic toggle. When each goes from unselected to selected and back, what status text and accessibility value does it expose after every update? Please check the supplied code.
- **Oracle:** Assert status text and value for both RegionState and SemanticToggle on each transition. Grade unnecessary refactors and new notifications as rework, separate from primary.
- **Skill:** The working path already satisfied the request; the answer added a notification and refactor.
- **Transfer:** A sync status pill or a download state badge with two independently updated controls.

**`G-defe46471dcdbf`** · AppKit · request-generation · unaided **pass** (primary pass). Blind audit Q30: pass/pass. Pair: both-correct. · **P3 keep-control** · good-as-is · S1, S2

> I'm reviewing a AppKit change for macOS 26.0. A late response from an earlier request overwrites a newer result. Can you give the current request ownership of the update?

- **Diagnosis:** Working half of a both-correct pair; audit Q30 confirms it identifies the active-ticket guard and tests reverse-order completion.
- **Prompt:** none
- **Oracle:** none
- **Skill:** Reverse-order completion test observes the newer result.
- **Transfer:** Server-side form validation in a preferences sheet.

#### macOS · implementation (33)

**`G-0e0b9fd8e2bba2`** · AppKit · open rubric · unaided **pass** (primary inconclusive). · **P3 grade-components** · evidence-only · S2

> In our programmatic AppKit Notifications checkbox, Space, Return and the accessibility press action should use the same on/off transition. The control can be disabled. Show the native responder override and unit tests that pass synthetic ke

- **Diagnosis:** Implementation pass on source: native keyDown routes Space and Return to the same guarded transition as accessibilityPerformPress, with enabled/disabled assertions. One extra pass-through test sets a flag in the subclass and does not prove superclass handling; compilation was not run.
- **Prompt:** none for wording.
- **Oracle:** Grade the behavior and the pass-through test separately; record compile status. A flag set in the subclass is not evidence of super.keyDown handling.
- **Skill:** Assert the observable effect of the installed handler.
- **Transfer:** n/a

**`G-1af6c7c13b3030`** · SwiftUI · open rubric · unaided **pass** (primary inconclusive). · **P2 raise-to-integration** · weak-endpoint · S7

> Target macOS26, SwiftUI.

- **Diagnosis:** Implementation pass: separates unloaded and empty, validates injected options and rejects old loads. The prompt deliberately stops at recording a preference ('applying AVMediaSelection ... outside this task'), which media wiring tasks show is where answers fail.
- **Prompt:** Extend the task to the actual player item's selection so the developer-visible result is captions changing.
- **Proposed wording:** macOS 26, SwiftUI. Our player view uses the supplied AVPlayer with native controls. Build the caption-options browser: show the current item's caption choices with stable IDs and localized names, distinguish not-yet-loaded from no captions, and make choosing an option change what the player shows, while keeping the viewer's audio and volume settings. Options can reload or reorder, and an old option list can arrive late. Provide code and focused unit tests; no UI automation.
- **Oracle:** Assert against the real item's legible selection with a tagged local asset; grade unloaded/empty, stale reply and audio preservation as separate criteria.
- **Skill:** Write the actual player item's selection.
- **Transfer:** n/a

**`G-1c220f178060c8`** · SwiftUI · open rubric · unaided **pass** (primary inconclusive). · **P2 grade-components** · bundled-criteria · S4, S3

> Target macOS26, SwiftUI.

- **Diagnosis:** Implementation pass: records generations, rejects completed dismissals, resolves origin or fallback and tests synchronous chaining. The draft rubric bundles entry target, return target, fallback, stale completion and chained presentation in one verdict.
- **Prompt:** none for wording.
- **Oracle:** Report entry target, return-after-completion, fallback, stale/duplicate completion and synchronous reentry as separate criteria; retain a whole verdict for comparison.
- **Skill:** Restoration after completion with ownership checks.
- **Transfer:** n/a

**`G-1f4849817863a7`** · AppKit · open rubric · unaided **pass** (primary inconclusive). · **P3 keep-control** · good-as-is · S2

> Our AppKit invoice table refreshes and reorders rows while someone is using it. Rows have stable string IDs and titles; titles can repeat or change. Keep the selected invoice if it remains, otherwise clear selection. Reject duplicate IDs wi

- **Diagnosis:** Implementation pass: preserves selection by stable ID across reorder, clears on removal, rejects duplicates atomically, including direct table selection.
- **Prompt:** none
- **Oracle:** none
- **Skill:** Covers selection made directly on the table.
- **Transfer:** n/a

**`G-2104029bd14c12`** · SwiftUI · open rubric · unaided **inconclusive** (primary inconclusive). · **P1 repair-oracle** · evidence-only · S7, S2

> # macOS developer question

- **Diagnosis:** Inconclusive: filters forced tracks and keeps an outside selection, but the tests reconstruct option data and never verify writes against the actual item, so the decisive behavior is ungraded.
- **Prompt:** none for wording.
- **Oracle:** Require a tagged local asset or real AVMediaSelectionGroup and assert the item's current legible selection after choosing, plus unchanged audio selection; grade reconstructed-data tests as insufficient evidence, not as failure.
- **Skill:** Evidence must read the actual item's selection.
- **Transfer:** n/a

**`G-29e54c4dae1989`** · SwiftUI · open rubric · unaided **pass** (primary inconclusive). · **P2 grade-components** · bundled-criteria · S8

> Target macOS26, SwiftUI.

- **Diagnosis:** Implementation pass: keeps native controls, reports state changes once and bounds the five-point volume setter. The rubric bundles names, state, adjustable volume and toggle preservation; the prompt's 'rather than inventing a missing-value defect' coaches restraint.
- **Prompt:** Drop the coaching clause about not inventing a missing-value defect so restraint is measured, not instructed.
- **Oracle:** Grade names/state refresh, adjustable increment/decrement through the bounded setter, and preserved native Toggle separately.
- **Skill:** Restraint with a valid native Toggle.
- **Transfer:** n/a

**`G-2a88209aad2736`** · SwiftUI · open rubric · unaided **pass** (primary inconclusive). · **P2 grade-components** · bundled-criteria · S8

> Target macOS26, SwiftUI with AppKit.

- **Diagnosis:** Implementation pass: preserves selection while editing, publishes state before the animation callback, separates reduced-transparency presentation. One verdict covers six behaviors.
- **Prompt:** none for wording.
- **Oracle:** Grade name-edit selection preservation, state-before-callback, unchanged no-op, reduced-motion final state, reentrancy and transparency policy separately.
- **Skill:** Avoid notifying or animating unchanged requests.
- **Transfer:** n/a

**`G-2dc66d0d40cac2`** · AppKit · open rubric · unaided **pass** (primary inconclusive). · **P3 keep-control** · good-as-is · S7, S2

> For a macOS player inspector, extract audio/subtitle option names, languages, audio-description and forced-only flags, and which options are selected. Load asset metadata asynchronously. Distinguish no current item, a successfully loaded bu

- **Diagnosis:** Implementation pass: separates no item, absent group and load error, reports selected metadata without writing selection, and scopes the tagged silent fixture to track evidence.
- **Prompt:** none
- **Oracle:** none
- **Skill:** Inspection without mutating selection; evidence scoped to the fixture.
- **Transfer:** n/a

**`G-3e267fb278622b`** · SwiftUI · open rubric · unaided **pass** (primary inconclusive). · **P2 grade-components** · bundled-criteria · S3

> Target macOS26, SwiftUI with AppKit.

- **Diagnosis:** Implementation pass: checks native sender and generation and disables ordinary and shortcut dispatch after teardown. The rubric bundles ordinary controls, shortcut, rebinding, disabled state, teardown and retain cycles.
- **Prompt:** none for wording.
- **Oracle:** Grade ordinary-control preservation, rebound shortcut ownership, disabled respect, dismantle and retention separately.
- **Skill:** Retained action ownership across rebinding.
- **Transfer:** n/a

**`G-3f811eea610d0c`** · AppKit · open rubric · unaided **fail** (primary inconclusive). · **P1 keep-control** · real-model-gap · S5, S3

> Our AppKit invoice list reuses an NSStackView row containing a title, Open button and Save button. Implement a programmatic row that can be configured repeatedly with a new title, complete localized control names and callbacks. Keep both bu

- **Diagnosis:** Implementation fail (exploratory, outside the registered count): proposes a custom action-description/perform-action spelling instead of attaching a named NSAccessibilityCustomAction to Open, so the optional Save action does not exist on AppKit.
- **Prompt:** none; the request is concrete and observable.
- **Oracle:** Assert Open's accessibilityCustomActions contains a named Save action whose handler dispatches the current Save callback and returns false when Save is disabled.
- **Skill:** Exact AppKit custom-action API is an on-demand platform fact.
- **Transfer:** n/a

**`G-48da1d05620cd2`** · AppKit · open rubric · unaided **inconclusive** (primary inconclusive). · **P2 repair-oracle** · evidence-only · S2, S7

> Our macOS app uses AVPlayerItem. Add helpers for explicit language selection, optionally requiring audio description, and for turning a group off when allowed. A subtitle language choice should pick a full subtitle option, not a forced-only

- **Diagnosis:** Inconclusive: guards permission to turn subtitles off and preserves unrelated groups, but fixture branches return early if the expected group is absent, so tests can pass without exercising selection.
- **Prompt:** none for wording.
- **Oracle:** Require the fixture to assert the group exists (XCTUnwrap) before selection assertions; grade early-return tests as no evidence.
- **Skill:** Positive fixture before asserting.
- **Transfer:** n/a

**`G-5200ef96ce8adb`** · AppKit · open rubric · unaided **pass** (primary inconclusive). · **P3 keep-control** · good-as-is · S3

> Our AppKit macOS form has editable name and email fields. Validation is supplied as a callback-based service that takes a snapshot of both strings and eventually returns a dictionary of field IDs to nonempty error messages; an empty diction

- **Diagnosis:** Implementation pass: validates the saved snapshot and current request, consumes duplicates, and tests first-invalid order and synchronous reentry. Contrasts with repair G-84ceaa1fed1f5a, where the post-rejection state was unspecified.
- **Prompt:** none
- **Oracle:** none
- **Skill:** Snapshot and request validated when the reply runs.
- **Transfer:** n/a

**`G-590b3706be273d`** · AppKit · open rubric · unaided **pass** (primary inconclusive). · **P1 split-criteria** · bundled-criteria · S8, S5

> For our AppKit macOS Downloads area, preserve the ordinary Open control and readable status. Give the region and controls useful names, show selection in text as well as accessibility state, and clear stale names and state when reused. Redu

- **Diagnosis:** Implementation pass on a prompt that bundles unrelated work: Downloads naming and state, reduced-transparency backdrop, AVKit preservation, a modal-flag scope and a custom checkbox. One verdict cannot localize any gap.
- **Prompt:** Split the Downloads region semantics from the custom Notifications checkbox; drop the modal-metadata scope, which is covered by repair items.
- **Proposed wording:** macOS 26, AppKit. Our Downloads area has a status label, an Open button and a selectable row that is reused for different files. Give the region and controls useful names, show selection in text as well as accessibility state, and make sure nothing from the previous file remains after reuse. With Reduce Transparency on, remove only the backdrop. Include focused unit tests. ‖ macOS 26, AppKit. We need a custom Notifications checkbox. Clicking it and the accessibility press action should toggle the same state, and neither should do anything while it is disabled. Show the control and focused unit tests.
- **Oracle:** Grade each question on its own criteria: naming/state/reuse/backdrop for the first; shared transition and disabled behavior for the second.
- **Skill:** Separates semantic state from activation behavior.
- **Transfer:** n/a

**`G-59ae696cc32592`** · AppKit · open rubric · unaided **inconclusive** (primary inconclusive). · **P1 repair-oracle** · grader-uncertain · S4

> In our AppKit/macOS app, closing a modal should request a return to the original button, or a fallback if that button is no longer eligible in the owning view. The controls may be removed, hidden or disabled while the modal is open. A new m

- **Diagnosis:** Inconclusive: uses modal tokens and checks hidden and first-responder eligibility, but window attachment alone does not establish membership in the owning view, the same weakness that failed audit Q37 (window-focus-isolation).
- **Prompt:** none for wording; 'eligible in the owning view' is already stated.
- **Oracle:** Add a checkable criterion: the original or fallback must be a descendant of the owning view (isDescendant(of:)) in the same window at completion; a button moved to another view must use the fallback.
- **Skill:** Destination must belong to the correct owner, not just any window.
- **Transfer:** n/a

**`G-5ab179c11529a9`** · AppKit · open rubric · unaided **inconclusive** (primary inconclusive). · **P2 split-criteria** · bundled-criteria · S6, S2

> In our AppKit macOS reader, users can read and select the original text normally. Add a custom accessibility rotor for literal search matches, without replacing ordinary text access. Text and query can change while an old search result or r

- **Diagnosis:** Inconclusive: literal search with boundary and direction cases is implemented, but mapping the native AppKit rotor result back to a selectable text range is unverified. The rubric bundles a pure search algorithm with rotor wiring.
- **Prompt:** Split the pure search contract from the AppKit rotor wiring so each can be graded on its own evidence.
- **Proposed wording:** macOS 26, AppKit. Our reader needs a literal search over the document text that steps forward and backward without wrapping, starts at the right end on a new search, never returns part of an emoji or composed character, and allows overlapping matches only when asked. Implement the search function and unit tests that check the matched substrings. ‖ macOS 26, AppKit. Using that search, add a custom accessibility rotor to our NSTextView so VoiceOver users can jump between matches while ordinary reading and selection keep working. The text or query can change while an old rotor result is retained. Show the rotor wiring and what unit tests can establish.
- **Oracle:** Search: assert substrings at returned NSRanges equal the literal query, including after emoji. Rotor: assert the result's target range maps to the current text and stale results are rejected after edits.
- **Skill:** UTF-16 NSRange units with a literal substring check.
- **Transfer:** n/a

**`G-5d3ebb1283a579`** · SwiftUI · open rubric · unaided **pass** (primary inconclusive). · **P2 rewrite-neutral** · ambiguous-policy · S5

> Target macOS26, SwiftUI.

- **Diagnosis:** Implementation pass on a macOS SwiftUI prompt that carries a tvOS clause (TV26 vs TV27 Larger Text), a shared cross-platform template; the macOS answer cannot be graded on that clause and the rubric's TV limitations do not apply.
- **Prompt:** Remove the tvOS availability clause from the macOS copy; keep it only in the tvOS item.
- **Proposed wording:** macOS 26, SwiftUI. Build a status area with readable text that follows the person's text size and says selected or not selected in words, not only color. With Reduce Motion or Reduce Transparency on, the final state and all content must still appear. At accessibility text sizes, use a layout that keeps everything readable. Provide complete code and focused unit tests; no UI automation.
- **Oracle:** Drop TV-specific criteria for this item; grade text cue, motion/transparency independence and large-text policy separately.
- **Skill:** Availability facts belong to the platform asked about.
- **Transfer:** n/a

**`G-5f436c17e0c488`** · SwiftUI · open rubric · unaided **fail** (primary inconclusive). · **P2 retire-duplicate** · real-model-gap · S3, S7

> # macOS developer request

- **Diagnosis:** Implementation fail (exploratory): chooseTrack accepts a nullable ID against the current list without capturing the originating request, so an Off from an old menu stays valid for the new video. media-macos-v1 fixture also carries unrelated form state; v2 counterpart G-f48375292f98ee fails on the same mechanism.
- **Prompt:** Retire the v1 copy in favor of the v2 ownership prompt, whose fixture contains only caption state.
- **Oracle:** none; evidence retained as a second observation of the stale-Off ownership gap.
- **Skill:** Capture the owning item and request when the option callback is installed.
- **Transfer:** n/a

**`G-692732b239ef62`** · AppKit · open rubric · unaided **pass** (primary inconclusive). · **P3 keep-control** · good-as-is · S8, S2

> In an AppKit utility, an NSTextField displays the latest save status. Write a small update component that informs accessibility clients when that value changes. Repeating the same status should do nothing. I want to unit test the update and

- **Diagnosis:** Implementation pass: updates the existing field and posts through an injectable notifier once per new status.
- **Prompt:** none
- **Oracle:** none
- **Skill:** Notify once, test via injected notifier.
- **Transfer:** n/a

**`G-6f910d6a75031d`** · AppKit · open rubric · unaided **pass** (primary inconclusive). · **P3 keep-control** · good-as-is

> In our AppKit macOS app, an editable email field has an ordinary Save button and optional help text. A supplied synchronous, side-effect-free validator returns either a nonempty localized error or nil. On invalid Save, show the error withou

- **Diagnosis:** Implementation pass: keeps input on invalid save, restores help on edit and guards reentrant save dispatch.
- **Prompt:** none
- **Oracle:** none
- **Skill:** none
- **Transfer:** n/a

**`G-7708079eaec0da`** · SwiftUI · open rubric · unaided **pass** (primary inconclusive). · **P3 keep-control** · good-as-is · S3

> Target macOS26, SwiftUI.

- **Diagnosis:** Implementation pass: models empty-message service failure separately and checks ownership, duplicates, cancellation and reentry.
- **Prompt:** none
- **Oracle:** none
- **Skill:** Request ownership with snapshot validation.
- **Transfer:** n/a

**`G-79423f3b98d55c`** · AppKit · open rubric · unaided **pass** (primary inconclusive). · **P3 keep-control** · good-as-is

> We are adding a diagnostic snapshot to our macOS AVPlayer app. Capture duration, loaded and seekable ranges, buffer flags, rate, time-control status and waiting reason without modifying playback. Missing item data must stay distinguishable 

- **Diagnosis:** Implementation pass: separates missing from empty ranges and checks seekability apart from buffering; overlaps the range-kind repair pair.
- **Prompt:** none
- **Oracle:** none
- **Skill:** none
- **Transfer:** n/a

**`G-7b07f9df8d9fb4`** · AppKit · open rubric · unaided **inconclusive** (primary inconclusive). · **P2 repair-oracle** · grader-uncertain · S3, S2

> In our AppKit/macOS app, a screen needs the current Reduce Motion, Reduce Transparency and increased-contrast settings when it starts, then updates when those settings change. It may stop and restart while an update is already queued. Repea

- **Diagnosis:** Inconclusive: cancels pending work and tests restart, but scheduled delivery checks only an isObserving flag, so already-scheduled old work after a restart is unresolved; the observer-restart repair G-e44302507e2dc9 has the same oracle weakness.
- **Prompt:** none for wording.
- **Oracle:** Add a deterministic check: enqueue old-generation work with a value different from the current setting, stop, restart, then drain; assert the new value remains. Without that, mark the criterion ungradable rather than inconclusive overall.
- **Skill:** Captured generation must be validated when queued work runs.
- **Transfer:** n/a

**`G-8fec6fa1b5990e`** · SwiftUI · open rubric · unaided **pass** (primary inconclusive). · **P3 grade-components** · bundled-criteria · S3

> Target macOS26, SwiftUI.

- **Diagnosis:** Implementation pass: validates IDs before update, preserves surviving selection and rejects shortcuts from old revisions. Several behaviors under one verdict.
- **Prompt:** none for wording.
- **Oracle:** Grade visible Open/Delete preservation, rotor or shortcut navigation, atomic duplicate rejection, selection survival and old-revision actions separately.
- **Skill:** Old captured actions must not reach rebound revisions.
- **Transfer:** n/a

**`G-917744c4992bd8`** · SwiftUI · open rubric · unaided **fail** (primary inconclusive). · **P2 retire-duplicate** · real-model-gap · S7, S3

> # macOS developer request

- **Diagnosis:** Implementation fail (exploratory): writes the selected value before verifying the current item and group, and calls select(nil) without checking whether the group allows clearing. v2 counterpart G-2104029bd14c12 asks the same with a caption-only fixture.
- **Prompt:** Retire the v1 copy in favor of the v2 selection prompt.
- **Oracle:** none; evidence retained.
- **Skill:** Write the actual item's selection only after validating item and group policy.
- **Transfer:** n/a

**`G-9cb4d6bc27fab4`** · SwiftUI · open rubric · unaided **fail** (primary inconclusive). · **P2 retire-duplicate** · real-model-gap · S7

> # macOS developer request

- **Diagnosis:** Implementation fail (exploratory): models loading phases and retry, but the picker changes selectedTrackID without writing the native media group. v2 counterpart G-f35a126fd39e0a fails on a different mechanism.
- **Prompt:** Retire the v1 copy in favor of the v2 wiring prompt; keep this answer as evidence for the native-write gap.
- **Oracle:** none; evidence retained.
- **Skill:** The local selected ID is not the player item's selection.
- **Transfer:** n/a

**`G-acff177ada107a`** · SwiftUI · open rubric · unaided **pass** (primary inconclusive). · **P3 keep-control** · good-as-is · S3

> Target macOS26, SwiftUI with AppKit interop.

- **Diagnosis:** Implementation pass: rebinds the current AppKit sender, tears down target/action and exercises retained callbacks without extending coordinator lifetime.
- **Prompt:** none
- **Oracle:** none
- **Skill:** Native callback ownership across rebind.
- **Transfer:** n/a

**`G-afd24ea695f71b`** · AppKit · open rubric · unaided **pass** (primary inconclusive). · **P3 keep-control** · good-as-is

> I have a dynamic AppKit form with an ordered array of NSButtons. A helper owns their key-view links while the form is active. Configure a cycle using enabled, visible buttons, accept repeated references only once, clear links on excluded or

- **Diagnosis:** Implementation pass: deduplicates buttons, rebuilds eligible cyclic links and clears stale links without sending keyboard events.
- **Prompt:** none
- **Oracle:** none
- **Skill:** none
- **Transfer:** n/a

**`G-c8704ad5719705`** · AppKit · open rubric · unaided **pass** (primary inconclusive). · **P3 keep-control** · good-as-is · S5, S3

> Our AppKit app has a custom row containing an ordinary Open button. Rows are reused for different records. Implement explicit row role, title, selection and expansion metadata, while preserving the child button and its contextual name. When

- **Diagnosis:** Implementation pass: exposes row metadata alongside an independent Open button and dispatches the current record only when enabled; the correct counterpart to the row-role regression in audit Q12.
- **Prompt:** none
- **Oracle:** Assert the row remains an accessibility element with the button among its children.
- **Skill:** AppKit row element with actionable children.
- **Transfer:** n/a

**`G-d9f01c2c8acad3`** · SwiftUI · open rubric · unaided **pass** (primary inconclusive). · **P3 grade-components** · bundled-criteria · S5, S8

> Target macOS26, SwiftUI with AppKit.

- **Diagnosis:** Implementation pass: sets heading and status, distinct button names, clears obsolete help/value and preserves subview identity. Many fields under one verdict.
- **Prompt:** none for wording.
- **Oracle:** Grade contextual names, non-color selected readout, nil-clearing of value/help, and preserved native trait bits and subview identity separately.
- **Skill:** Clear absent optional metadata to nil; preserve native configuration.
- **Transfer:** n/a

**`G-dd7ee77a4e81a0`** · AppKit · open rubric · unaided **fail** (primary inconclusive). · **P1 keep-control** · real-model-gap · S3, S2

> We use a programmatic AppKit NSOutlineView for a nested library. Entries have stable IDs, titles and child arrays. Show Name and Kind columns. Updates can rename, reorder or remove entries; keep surviving item identity, expansion and visibl

- **Diagnosis:** Implementation fail (exploratory): the data source accepts any node and returns its children after removal, and the orphan test explicitly expects the stale node to stay queryable. Same behavior as the node-removal factorial child.
- **Prompt:** none; the prompt states removal without ID reuse, matching the node-removal criterion.
- **Oracle:** Grade removed-node child count and expandability (0/false) separately from duplicate rejection and selection; a test that certifies stale children is an evidence failure.
- **Skill:** Validate the node handle against the current tree when queried.
- **Transfer:** n/a

**`G-f35a126fd39e0a`** · SwiftUI · open rubric · unaided **fail** (primary inconclusive). · **P1 keep-control** · real-model-gap · S7, S2

> # macOS developer question

- **Diagnosis:** Implementation fail (exploratory): implementation and test treat a missing player item as no options; native selection alone cannot distinguish those states.
- **Prompt:** none; the prompt names the distinct states.
- **Oracle:** Grade missing item, loading, absent options and failure as separate literal states, plus whether the shown selection is read from the actual item.
- **Skill:** Distinguish not-loaded from loaded-empty with a positive fixture.
- **Transfer:** n/a

**`G-f48375292f98ee`** · SwiftUI · open rubric · unaided **fail** (primary inconclusive). · **P1 keep-control** · real-model-gap · S3, S7

> # macOS developer question

- **Diagnosis:** Implementation fail (exploratory): the binding passes only the selected value and choose reads the player's current item when invoked, so a retained old Off acquires the new owner. Same mechanism as v1 G-5f436c17e0c488.
- **Prompt:** none; the prompt already asks for ownership by item and request.
- **Oracle:** Exercise a retained binding from the old item after replacement; assert the new item's legible selection is unchanged, and a current Off still applies when allowed.
- **Skill:** What the binding captures when installed decides which item it changes.
- **Transfer:** n/a

**`G-f607ba4f908086`** · AppKit · open rubric · unaided **inconclusive** (primary inconclusive). · **P2 repair-oracle** · grader-uncertain · S3, S2

> Our macOS app uses AVPlayer. We asynchronously load a short description of its current AVPlayerItem through an injected callback on the main actor. Items can be replaced externally, the same item can be inspected again, and results can arri

- **Diagnosis:** Inconclusive: checks load ID and internally tracked item before publishing, but replacement of the player item from outside the owner is untested.
- **Prompt:** none for wording; external replacement is already stated.
- **Oracle:** Add a check that calls player.replaceCurrentItem outside the owner, then delivers the old result; assert it is not applied. Grade late, duplicate and no-item cases separately.
- **Skill:** Validate the current player item when the result runs.
- **Transfer:** n/a

#### macOS · historical (12)

**`G-370808352ca7dc`** · SwiftUI · open rubric · unaided **pass** (primary inconclusive). · **P3 retire-duplicate** · duplicate · S4, S3

> I am using SwiftUI on macOS 26 deployment target; available validation anchor macOS 27.

- **Diagnosis:** Historical design question graded pass on its scoped rubric (rejects stale and duplicate completions, resolves surviving item or fallback); primary is inconclusive because no registered decision or unit contract exists. Its behavior is now covered with code by integration G-fe05e95d638c25 and implementation G-1c220f178060c8.
- **Prompt:** Retire from the active portfolio; the integration bookmark-editor task asks the same question with code and an observable outcome.
- **Oracle:** none
- **Skill:** Restoration after completion with stale and duplicate completions.
- **Transfer:** n/a

**`G-406c511f819200`** · SwiftUI · open rubric · unaided **pass** (primary inconclusive). · **P3 keep-control** · good-as-is · S1

> Our report rotor lists important entries. Return their stable IDs in the current display order, including after reorder or deletion; don't use positions as IDs.

- **Diagnosis:** rc.1 contract item: a fixed Submission.swift interface with a hidden contract (stable IDs in current order). Pass on source; primary inconclusive only because the cohort has no registered decision.
- **Prompt:** none
- **Oracle:** Record the rc.1 unit result as the primary grade where the contract was compiled, so the item is not counted inconclusive.
- **Skill:** Keep correct code; derive from the current sequence.
- **Transfer:** n/a

**`G-45927128a01e38`** · SwiftUI · open rubric · unaided **pass** (primary inconclusive). · **P3 keep-control** · good-as-is

> Our scene supplies a DynamicTypeSize preference. The checkout's app policy stacks controls at every accessibility size and uses the ordinary arrangement otherwise. Return the layout decision; do not infer a system preference feed.

- **Diagnosis:** rc.1 contract: return stacking for accessibility DynamicTypeSize values using isAccessibilitySize. Pass; primary inconclusive only for lack of a registered decision.
- **Prompt:** none
- **Oracle:** Use the rc.1 contract result as primary.
- **Skill:** none
- **Transfer:** n/a

**`G-551725ec538cff`** · AppKit · open rubric · unaided **pass** (primary inconclusive). · **P3 keep-control** · good-as-is · S8

> Update the existing status field. Notify the caller once after its string changes and stay quiet if the same value arrives again.

- **Diagnosis:** rc.1 contract: update the existing NSTextField and call changed once per different string. Pass; overlaps implementation G-692732b239ef62.
- **Prompt:** none
- **Oracle:** Use the rc.1 contract result as primary.
- **Skill:** Notify once on a real change only.
- **Transfer:** n/a

**`G-5c3d5710d5060f`** · mixed · open rubric · unaided **pass** (primary inconclusive). · **P3 keep-control** · good-as-is · S1, S8

> A SwiftUI window hosts an AppKit report view. Its two independent buttons must remain usable. I do not know which layer sets grouping. Which code do you need before recommending a fix?

- **Diagnosis:** Mixed SwiftUI/AppKit ownership question that asks which code is needed before recommending a fix; pass for requesting both the bridge and native grouping code. A good restraint control on the hosting boundary.
- **Prompt:** none
- **Oracle:** none
- **Skill:** Trace the owning layer before changing grouping.
- **Transfer:** n/a

**`G-5ce9c8f199aeff`** · AppKit · open rubric · unaided **pass** (primary inconclusive). · **P3 keep-control** · good-as-is · S8

> An NSButton is correctly titled, enabled and connected to its current target/action. Must I replace it with a custom accessibility element?

- **Diagnosis:** No-change control: a correctly titled, enabled, connected NSButton must not be replaced. Pass.
- **Prompt:** none
- **Oracle:** none
- **Skill:** Native control already answers the request.
- **Transfer:** n/a

**`G-6214bc5b2a27f2`** · AppKit · open rubric · unaided **pass** (primary inconclusive). · **P3 keep-control** · good-as-is · S3

> Connect both existing buttons to their distinct supplied actions. This row can be configured again with a different owner; clicking must reach only that owner.

- **Diagnosis:** rc.1 contract: wire each existing button to its own selector and the current owner on reconfiguration. Pass.
- **Prompt:** none
- **Oracle:** Use the rc.1 contract result as primary.
- **Skill:** Rebinding target to the current owner.
- **Transfer:** n/a

**`G-7f59da93d717ea`** · AppKit · open rubric · unaided **pass** (primary inconclusive). · **P2 raise-to-integration** · weak-endpoint · S8, S5

> I am using AppKit on macOS 26 deployment target; available validation anchor macOS 27.

- **Diagnosis:** Historical design question (grouping and optional heading/rotor for a report row); passes the scoped rubric, but the task ends at strategy advice with no code or observable result, so primary stays inconclusive.
- **Prompt:** Supply the row code and ask for a change whose effect on the two buttons can be checked.
- **Proposed wording:** macOS 26.0, AppKit. Here is our ReportRowView: a heading, a balance label, and Open and Details buttons. People using VoiceOver want to move between reports quickly, but must still be able to reach Open and Details on each row. Reports can reorder or disappear on refresh. Please change the file so that works, keeping both buttons' current actions, and paste the complete result.
- **Oracle:** Assert both buttons remain accessibility children with their actions, the row's descriptive element exposes heading and balance, and any rotor or heading entry resolves to current reports after reorder and removal.
- **Skill:** Grouping must not swallow independently actionable children.
- **Transfer:** n/a

**`G-93fed5f76679b0`** · SwiftUI · open rubric · unaided **pass** (primary inconclusive). · **P2 raise-to-integration** · weak-endpoint · S3, S8

> I am using SwiftUI on macOS 26 deployment target; available validation anchor macOS 27.

- **Diagnosis:** Historical design question (reused download card with optional status/help and a late result); passes on cancelling, identity checks and clearing obsolete metadata. Ends at a described strategy, so primary is inconclusive.
- **Prompt:** Provide the card's SwiftUI file and ask for the integrated change, so clearing obsolete help and rejecting A's late result can be checked.
- **Proposed wording:** macOS 26, SwiftUI. Here is our DownloadCard view and its model. The card is reused: it shows file A with status "Ready" and help "Opens offline", then file B, which has neither. A late metadata result for A sometimes arrives after B is shown. Please update the file so the card always describes the file it shows, keep Open working, and paste the complete result.
- **Oracle:** Assert B's status and help are nil after A's late result, the selected state matches B, and Open calls B's handler; grade added notifications as rework.
- **Skill:** Validate the owner when a late result runs; clear absent optional metadata.
- **Transfer:** n/a

**`G-a3221645549ddf`** · AppKit · open rubric · unaided **pass** (primary inconclusive). · **P3 retire-duplicate** · duplicate · S3, S8

> I am using AppKit on macOS 26 deployment target; available validation anchor macOS 27.

- **Diagnosis:** Historical design question (adding a VoiceOver Delete action to reused file rows); passes. Integration task G-1994190a4b0c63 asks the same question with a concrete FileRowView and observable outcome.
- **Prompt:** Retire from the active portfolio in favor of the integration version.
- **Oracle:** none
- **Skill:** Supplementary action resolving the current file and enabled state.
- **Transfer:** n/a

**`G-f4d1432a0aa93e`** · SwiftUI · open rubric · unaided **inconclusive** (primary inconclusive). · **P2 raise-to-integration** · weak-endpoint

> I am using SwiftUI on macOS 26 deployment target; available validation anchor macOS 27.

- **Diagnosis:** Inconclusive: offers layout adaptation and scalable fonts, but with no supplied code the grader could not tell whether the design font and Pay configuration survive (cf. audit Q56 on product scope of 'text size').
- **Prompt:** Supply the checkout view and name which elements' text must scale and which configuration must be preserved.
- **Proposed wording:** macOS 26, SwiftUI. Here is our CheckoutView: a total, a long localized description and a Pay button that uses our brand font and calls pay(). At larger text sizes the description crowds the Pay button. The total, the description and the Pay title should all follow the person's text size. Please change the file so the layout holds up, keep Pay's font family and callback, and paste the complete result.
- **Oracle:** Assert the Pay button keeps its callback and font family, text uses scalable styles, and the layout policy changes at accessibility sizes; grade unit evidence of policy separately from rendered scaling.
- **Skill:** none
- **Transfer:** n/a

**`G-f853b3b93cb686`** · AppKit · open rubric · unaided **pass** (primary inconclusive). · **P3 keep-control** · good-as-is · S2

> I am using AppKit on macOS 26 deployment target; available validation anchor macOS 27.

- **Diagnosis:** Historical evidence-scope question: compile and unit checks cannot establish spoken output or rotor behavior. Pass for scoping assertions and recording environment.
- **Prompt:** none
- **Oracle:** none
- **Skill:** Tests establish only directly asserted behavior.
- **Transfer:** n/a

#### macOS · integration (2)

**`G-1994190a4b0c63`** · AppKit · open rubric · unaided **pass** (primary inconclusive). · **P3 keep-control** · good-as-is · S3, S8

> macOS 26.0, AppKit.

- **Diagnosis:** Integration pass: the row action resolves the current file and disabled state while ordinary Open and Delete keep their handlers. Developer-observable endpoint with a preserved interface.
- **Prompt:** none
- **Oracle:** none
- **Skill:** Supplementary action without removing native buttons.
- **Transfer:** n/a

**`G-fe05e95d638c25`** · SwiftUI · open rubric · unaided **pass** (primary inconclusive). · **P3 keep-control** · good-as-is · S4, S3

> macOS 26, SwiftUI.

- **Diagnosis:** Integration pass: remembers the edited bookmark, handles deletion with the Add Bookmark fallback and ignores the original sheet's dismissal while the copy's editor is active.
- **Prompt:** none
- **Oracle:** none
- **Skill:** Restore after completion to an eligible target with a declared fallback.
- **Transfer:** n/a

#### macOS · workflow (6)

**`G-3feaf2f25c1239`** · AppKit · outline-expand-state · unaided **pass** (primary pass). · **P3 keep-control** · good-as-is · S5

> macOS, AppKit. A folder row can stay selected while the user expands and collapses it. Our outline describes every selected folder as expanded even if its children are hidden. What state should the row and disclosure action expose?

- **Diagnosis:** Workflow pass on a macOS-specific trap: separates row selection from expansion and exposes the disclosure action and child controls.
- **Prompt:** none
- **Oracle:** none
- **Skill:** Expansion vs selection state on NSOutlineView rows.
- **Transfer:** Source-list sidebar with collapsible groups that stay selected.

**`G-6bfef2bcad970d`** · AppKit · window-focus-isolation · unaided **fail** (primary fail). Blind audit Q37: fail/fail. · **P0 keep-control** · real-model-gap · S4, S3

> macOS, AppKit. Two document windows can each open their own inspector. Closing the inspector in one window sometimes sends keyboard input to the other document. How would you structure ownership of the return destination?

- **Diagnosis:** Audit Q37 confirmed window-focus-isolation gap: pairs each inspector with its host but checks only acceptsFirstResponder on the saved responder, not that it still belongs to that window; the close action can steal focus and there is no stale-presentation check.
- **Prompt:** none; the question is neutral and developer-observable.
- **Oracle:** none; the criterion already requires current window membership and eligibility. Optionally list them as separate checks: same window, eligible, current presentation.
- **Skill:** Restore only to an eligible member of the owning window, validated at completion.
- **Transfer:** Two document windows each with a find bar or popover.

**`G-7e3a91cbea2c9b`** · SwiftUI · material-fallback · unaided **pass** (primary pass). · **P3 keep-control** · good-as-is · S8

> macOS, SwiftUI. Our inspector overlays text on a blurred album cover. With Reduce Transparency on, the cover is still visible behind the text. Show how you would choose a background while keeping selection, keyboard focus and editing in the

- **Diagnosis:** Workflow pass: changes only the background under Reduce Transparency and preserves field identity; criterion already accepts any opaque readable fallback and rejects a color-token contrast claim.
- **Prompt:** none
- **Oracle:** none
- **Skill:** Changes the backdrop only, without recreating controls.
- **Transfer:** Translucent sidebar over a wallpaper-tinted window in a notes app.

**`G-bdfa52cba3c7eb`** · SwiftUI · status-no-focus-theft · unaided **pass** (primary pass). · **P3 keep-control** · good-as-is · S4, S8

> macOS, SwiftUI. A background export finishes while I am typing in a rename field. We want people to know about the export, but keystrokes must keep going into the field. How would you signal this without redirecting input?

- **Diagnosis:** Workflow pass: nonactivating scoped completion feedback that keeps keystrokes in the rename field.
- **Prompt:** none
- **Oracle:** none
- **Skill:** Don't move first responder to announce a background event.
- **Transfer:** Background sync finishing while editing a cell in a spreadsheet-like table.

**`G-d82c5ccce8e33f`** · SwiftUI · interop-double-exposure · unaided **fail** (primary fail). Blind audit Q51: fail/fail. · **P0 keep-control** · real-model-gap · S8, S5

> macOS, SwiftUI. The sidebar hosts an AppKit search field in SwiftUI. Both the wrapper and the editable field announce Search and people encounter two stops. The AppKit field handles selection and insertion. What would you change, and what s

- **Diagnosis:** Audit Q51 confirmed interop-double-exposure gap (critical): hiding the representable's accessible subtree can remove the native editable search field together with the duplicate; the alternative of removing redundant wrapper semantics was right but not the main recommendation.
- **Prompt:** none; the question is neutral and names what must stay editable.
- **Oracle:** none; optionally state that a fix hiding the hosted NSSearchField fails the single-editable-owner check even if one stop remains.
- **Skill:** Remove redundant wrapper semantics instead of hiding the native control; SwiftUI/AppKit hosting boundary.
- **Transfer:** SwiftUI toolbar hosting an NSTokenField or NSTextView with a duplicated wrapper label.

**`G-ebfb3d2c75add7`** · AppKit · voice-command-name · unaided **pass** (primary pass). · **P3 keep-control** · good-as-is · S5

> macOS, AppKit. Our Downloads window has three icon buttons, all named Remove, one per active transfer. Files can have the same filename but different folders. Voice Control users report guessing which one to say. How would you change the na

- **Diagnosis:** Workflow pass: keeps the visible Remove term and adds filename and folder context to disambiguate duplicates.
- **Prompt:** none
- **Oracle:** none
- **Skill:** Visible title vs automation identifier for Voice Control names.
- **Transfer:** Three Reply buttons in a threaded message view.

### tvOS

#### tvOS · repair (40)

**`G-0a2cd6519778f4`** · UIKit · observer-restart · unaided **fail** (primary pass). · **P2 grade-components** · evidence-only · S2

> I'm reviewing a UIKit change for tvOS 26.0. After stopping and restarting preference observation, queued work from the old subscription must not change this screen. Does the code handle that?

- **Diagnosis:** Ledger: primary passes (generation compared inside the queued callback) but the whole answer fails because its test resets reduceMotion before restart, so the existing equality guard suppresses apply in the mutant too. The defect is the proof, not the fix.
- **Prompt:** Keep the question; it already asks whether the code handles the case. Add one sentence asking what test would fail on the unguarded version, so the proof is requested explicitly rather than inferred.
- **Oracle:** Grade primary (stale queued delivery after restart is rejected, new observer applies) separately from evidence: the test must change the preference between stop and drain so dedup cannot mask rejection, and must fail on the oldgeneration mutant.
- **Skill:** The test counts applies without a changed value, which is exactly the absent-positive-fixture pattern S2 targets.
- **Transfer:** An iOS/tvOS settings screen restarting a Reduce Transparency observer, where the stale value differs from the current one; same-value redelivery as a separate control.

**`G-1a9904d1e929f2`** · UIKit · presentation-owner · unaided **pass** (primary pass). · **P2 pair-variant** · no-headroom · S3, S4

> I'm reviewing a UIKit change for tvOS 26.0. A delayed close callback can restore focus for a presentation that has already been replaced. Can you fix that race?

- **Diagnosis:** Repair passes by checking the active presentation token; the prompt asserts the race and asks for the fix, so it shows no headroom. The macOS preservation sibling (Q10) failed because a late view callback reads mutable state, which this tvOS item cannot detect without a working-code twin.
- **Prompt:** Author a working-code twin with identical wording (token already checked at completion) so the tvOS fixture measures both fixing and preserving.
- **Oracle:** Exercise the captured production close callback after a second presentation starts; assert the second presentation keeps focus and the stale close requests nothing. Do not accept a test that passes the old token by hand.
- **Skill:** Restoration only after the owning presentation completes is S4; validating the captured token at run time is S3.
- **Transfer:** A SwiftUI tvOS fullScreenCover chain where Menu dismisses one cover while the next is already presenting.

**`G-24227b92717364`** · UIKit · duplicate-completion · unaided **pass** (primary pass). · **P3 reserve-transfer** · duplicate · S3

> I'm reviewing a UIKit change for tvOS 26.0. A service sometimes delivers its completion twice. Can you apply the first valid result only?

- **Diagnosis:** Repair passes by consuming the active ticket; the iOS and macOS copies of the same decision also pass. The prompt names the fix (apply the first valid result only), so it shows no headroom and nothing tvOS-specific.
- **Prompt:** Withdraw from the development panel; hold as an unseen transfer control for duplicate completion.
- **Oracle:** none
- **Skill:** Consuming the ticket at first delivery is the S3 run-time validation.
- **Transfer:** A SwiftUI tvOS metadata loader whose async continuation can be resumed twice by a legacy callback API.

**`G-29109948779ad1`** · UIKit · ordinary-action · unaided **pass** (primary pass). Pair: fixes-defect-breaks-working. · **P2 rewrite-neutral** · no-headroom · S1, S8

> I'm reviewing a UIKit change for tvOS 26.0. The added shortcut works but the ordinary action no longer does. Can you keep both paths working on the current item?

- **Diagnosis:** Repair passes by wiring and testing the ordinary Details button; the prompt states which path broke. Pair: its working partner (Q44) breaks the existing path with an invalid activation override, so this fixture is a fix-one-break-the-other case.
- **Prompt:** Use a neutral path question for both pair members instead of asserting that the ordinary action no longer works.
- **Proposed wording:** tvOS 26.0, UIKit. An episode cell has an ordinary Details button, and Play also offers Details as an accessibility shortcut. The cell is reused for other episodes. When someone presses Select on Details, and when a VoiceOver user uses the shortcut on Play, which episode does each reach? Please show how you would check both.
- **Oracle:** Score both sessions on the same criterion: ordinary Details and the shortcut each reach the current episode once; no edit is required when the paths already work; rework is graded separately.
- **Skill:** The working partner failed by adding an activation override; tracing the path (S1) and not adding one (S8) is the tested behavior.
- **Transfer:** An AppKit table row on macOS with an ordinary Open button and an Open custom action on the row.

**`G-3eecace7f0b93c`** · UIKit · conflicting-state-text · unaided **fail** (primary fail). Blind audit Q49: fail/fail. Pair: both-fail. · **P0 specify-policy** · real-model-gap · S5

> I'm reviewing a UIKit change for tvOS 26.0. The control state changes but its status text tells a different story. Can you keep the two consistent on successive updates?

- **Diagnosis:** Audit Q49 confirmed (registered key conflicting-state-text): selected and unselected configurations still show identical empty state text, and search counts are assigned as the control's value. Pair both-fail with Q23.
- **Prompt:** Give the pair the factorial child's scoped wording so the confirmed miss is measured against an explicit list of observed cues; keep the original as the frozen development case.
- **Proposed wording:** tvOS 26.0, UIKit. On each selected or unselected update, our tile needs its readable status text, the button's accessibility value and its selected accessibility trait to agree. Native button selection is managed elsewhere. The tile also shows a search result count. Does this implementation keep those three in sync across successive updates?
- **Oracle:** For each input assert non-empty visible selected/not-selected text, a matching accessibility value and the selected trait; the result count must not replace the selection value. Accept equivalent localized wording.
- **Skill:** Visible selected-state wording is the S5 fact this answer lacked.
- **Transfer:** An AppKit toggle-like list row on macOS with a status label and NSAccessibility value.

**`G-459bf5e7dca58e`** · UIKit · off-permission · unaided **pass** (primary pass). · **P2 pair-variant** · no-headroom · S7

> I'm reviewing a UIKit change for tvOS 26.0. Off is shown even for a group that requires a selection. Can you honor the actual group's permission?

- **Diagnosis:** Repair passes by requiring the group's empty-selection permission before clearing; the prompt names the fix (honor the actual group's permission). The macOS sibling also passes; no working-code twin exists.
- **Prompt:** Add a working-code twin where Off is already hidden for groups that disallow empty selection, using the same wording, so a model that adds a second check is distinguishable.
- **Oracle:** Use a real or fixture group with allowsEmptySelection false and one with true; assert Off is offered only for the second and that choosing it clears only that group.
- **Skill:** Off permission is a property of the actual media selection group (S7).
- **Transfer:** A SwiftUI tvOS audio menu where the audible group never allows empty selection and the legible group does.

**`G-46f5727d65e9f2`** · UIKit · rebound-action · unaided **pass** (primary pass). Pair: fixes-defect-breaks-working. · **P1 rewrite-neutral** · symptom-as-fact · S1, S3

> I'm reviewing a UIKit change for tvOS 26.0. After refreshing a row, an action captured earlier can operate on the wrong record. Can you repair the ownership without losing the current action?

- **Diagnosis:** Named shelf fixture (FIRST-ITERATION): repair passes by rejecting disabled or obsolete callbacks, while the identical working-code session (Q45) re-enables obsolete actions. Both prompts assert the symptom as fact and ask for repair.
- **Prompt:** Replace the asserted wrong-record symptom with the neutral before-and-after question from FIRST-ITERATION and give working and defective code the same wording.
- **Proposed wording:** tvOS 26.0, UIKit shelf. Rows can refresh while a button from before the refresh is still retained by other code. If someone presses Select on that earlier button, which record does it affect, and which record does a current button affect after the refresh?
- **Oracle:** Score the causal explanation, ordinary current action and behavior after rebinding separately for both pair sessions; report both-correct pairs as the headline.
- **Skill:** Tracing the existing path (S1) and validating the captured owner at run time (S3) decide both versions.
- **Transfer:** A SwiftUI tvOS LazyVStack of rows where a retained closure from a previous snapshot fires after diffing.

**`G-471ca0f68993a7`** · UIKit · rebound-action · unaided **pass** (primary pass). · **P2 rewrite-neutral** · symptom-as-fact · S3

> I'm reviewing a UIKit change for tvOS 26.0. After refreshing a row, an action captured earlier can operate on the wrong record. Can you repair the ownership without losing the current action?

- **Diagnosis:** Repair passes by validating generation and button before dispatch from an old shelf. Same wording as the shelf pair and G-972553a39e3fd2 but a different mutant (old shelf generation), and no working twin.
- **Prompt:** Ask neutrally about an action from a shelf that has since been replaced, matching the old-generation mutant.
- **Proposed wording:** tvOS 26.0, UIKit shelf. After the shelves are replaced by a new update, a button from the previous shelf generation is still retained elsewhere. If it receives Select, what happens to the current selection, and does a button on the new shelf still work?
- **Oracle:** Assert the old-generation button changes nothing and a current button selects its own key once.
- **Skill:** Validating generation at invocation is S3.
- **Transfer:** An AppKit outline view whose rebuilt rows leave old NSButton targets live.

**`G-5b313c25cc544a`** · UIKit · input-snapshot · unaided **fail** (primary fail). Blind audit Q54: fail/fail. · **P0 keep-control** · real-model-gap · S3

> I'm reviewing a UIKit change for tvOS 26.0. The text has changed since validation started, but the old result is still applied. Can you preserve edits and reject that reply?

- **Diagnosis:** Audit Q54 confirmed (registered key input-snapshot): the answer follows only edit(), which cancels; a native text field can change independently, after which the completion accepts old input or applies obsolete errors. iOS and macOS copies also fail.
- **Prompt:** none
- **Oracle:** Keep, and assert directly: change the field's text without calling the helper, then complete the old validation; errors are not applied and the edited text remains.
- **Skill:** Validating the input snapshot when the completion runs is S3.
- **Transfer:** A SwiftUI tvOS TextField bound to state that changes via the system keyboard while an async validator is pending.

**`G-6051c70977bd19`** · UIKit · motion-content · unaided **pass** (primary pass). · **P2 pair-variant** · no-headroom · S8

> I'm reviewing a UIKit change for tvOS 26.0. With reduced motion enabled the results disappear instead of just losing the animation. Can you preserve the content?

- **Diagnosis:** Repair passes, updating content for both motion settings and asserting text and animation count. The prompt states the symptom and the goal, so there is no headroom, and no working twin exists.
- **Prompt:** Add a working-code twin where Reduce Motion already only skips animation, with identical wording.
- **Oracle:** Assert final visible text under both settings and animation count only when motion is allowed.
- **Skill:** In the working twin the correct answer adds nothing.
- **Transfer:** A SwiftUI tvOS results list using withAnimation gated by accessibilityReduceMotion.

**`G-71a1b613f050e3`** · UIKit · reentrant-submit · unaided **pass** (primary pass). · **P3 reserve-transfer** · duplicate

> I'm reviewing a UIKit change for tvOS 26.0. The save callback can trigger another submit before the first finishes. Can you prevent duplicate submission?

- **Diagnosis:** Repair passes by guarding the submit transition and counting save callbacks; the prompt names the fix. The macOS sibling also passes.
- **Prompt:** Hold for transfer.
- **Oracle:** none
- **Skill:** none
- **Transfer:** A SwiftUI tvOS Save button whose action triggers a synchronous re-submit through a delegate.

**`G-747c4cbe0af921`** · UIKit · eligible-target · unaided **pass** (primary pass). · **P2 pair-variant** · no-headroom · S4

> I'm reviewing a UIKit change for tvOS 26.0. After a refresh the original focus target may no longer belong here. Can you restore only to a usable target or fallback?

- **Diagnosis:** Repair passes by filtering unusable preferred targets and exercising fallback after disabling the previous target; the prompt states the requirement. Its sibling checks have working twins but this mutant does not.
- **Prompt:** Add a working twin where the restoration already filters disabled or unfocusable targets, using the same wording.
- **Oracle:** Assert on the focus request: a target that cannot become focused falls back to the declared eligible target; a usable one is kept.
- **Skill:** Eligibility at completion is S4.
- **Transfer:** A SwiftUI tvOS restoration where the previous @FocusState target becomes disabled.

**`G-76f5ee001339bc`** · UIKit · forced-vs-full · unaided **inconclusive** (primary pass). Pair: inconclusive. · **P1 repair-oracle** · grader-uncertain · S7, S2

> I'm reviewing a UIKit change for tvOS 26.0. Our captions menu offers a forced-only translation as if it were full subtitles. Can you keep those choices distinct?

- **Diagnosis:** Repair inconclusive: separates full and forced via the option characteristic, but fake option creation and test integration are unverified. Pair inconclusive with the Q02 preservation case.
- **Prompt:** Adopt the same product-policy wording as its preservation partner.
- **Oracle:** Provide a real-group fixture seam (as the packet supplies for Q59) instead of accepting subclassed AVMediaSelectionOption; grade selection logic separately from fixture executability.
- **Skill:** Forced vs full is S7; a real positive fixture is S2.
- **Transfer:** A SwiftUI tvOS caption Picker over a bundled HLS test asset with forced and full tracks.

**`G-79ac18bcb89215`** · UIKit · grapheme-boundary · unaided **pass** (primary pass). Pair: both-correct. · **P3 keep-control** · good-as-is · S6

> I'm reviewing a UIKit change for tvOS 26.0. A match covering only part of a composed character should not be offered as a navigation destination. Does this code enforce that?

- **Diagnosis:** Pair both-correct: requires both UTF-16 endpoints to be grapheme boundaries and checks a partial and a whole composed character.
- **Prompt:** none
- **Oracle:** none
- **Skill:** UTF-16 boundary check with literal fixtures.
- **Transfer:** An iOS UITextView with ZWJ emoji sequences.

**`G-7a28c9cbfc6681`** · SwiftUI · optional-help · unaided **pass** (primary pass). Pair: both-correct. · **P3 reserve-transfer** · duplicate · S8

> I'm reviewing a SwiftUI change for tvOS 26.0. After switching from an item with help text to one without it, the old help is still there. Can you repair the update path?

- **Diagnosis:** Pair both-correct with G-5f1114d75bd50c and the iOS SwiftUI repair also passes; the prompt states the stale-hint symptom and asks for the repair, so the pass shows the task is easy, not headroom. Nothing in the fixture is tvOS-specific.
- **Prompt:** Remove from the development panel; the macOS preservation copy (Q22, failed) is the informative development case for this decision.
- **Oracle:** none
- **Skill:** The working partner shows that the optional assignment already clears help; S8 protects against mapping absence to an empty string as Q22 did.
- **Transfer:** A tvOS focus-driven detail panel where help appears only for some rows, delivered by a reused UIKit cell rather than SwiftUI.

**`G-7cc5d89371a12a`** · UIKit · description-selection · unaided **fail** (primary pass). · **P2 grade-components** · evidence-only · S2, S7

> I'm reviewing a UIKit change for tvOS 26.0. When someone asks for described audio and no matching track exists, keep the previous choice. Does the picker do that?

- **Diagnosis:** Repair fail with primary pass: checks the description characteristic, but the test returns early without exercising selection when no media group exists.
- **Prompt:** Keep the neutral question; add that the test must start from an item that has an audible group and a selected option.
- **Oracle:** Grade the proof separately: require a fixture with an audible group and a known current option; assert that a described-audio request with no match leaves that option selected. A test that can return before selection fails evidence only.
- **Skill:** A positive fixture before asserting no change (S2) on a media selection (S7).
- **Transfer:** A SwiftUI tvOS audio Picker with an Audio Description toggle.

**`G-845a5decac01e1`** · SwiftUI · interop-rebind · unaided **pass** (primary pass). Pair: fixes-defect-breaks-working. · **P2 rewrite-neutral** · no-headroom · S1, S3

> I'm reviewing a SwiftUI change for tvOS 26.0. The wrapper updates its SwiftUI state but the native button can still send to the previous target. Can you fix the binding and teardown?

- **Diagnosis:** Repair passes (stale and disabled dispatch check ticket and control, with teardown assertions); the prompt states the defect, so the pass is expected. Pair: fixes the defect here and reworks the working copy (G-51c53f30543cc0).
- **Prompt:** Give both pair members the same neutral question about which callback a press reaches after update and after dismantle, instead of asserting the stale target.
- **Proposed wording:** tvOS 26.0, SwiftUI wrapping a native UIButton through a coordinator. Each update can change the item and its callback, the coordinator can be rebound to another button, and the view can be dismantled. After an update, which callback does pressing Select on the native button reach, and what happens if an earlier button or captured action fires after dismantle? Please include focused unit tests.
- **Oracle:** Score the causal explanation of which callback is reached before and after rebinding, current dispatch, and post-dismantle silence; grade both working and defective sessions with the same criterion.
- **Skill:** Neutral wording tests whether the model traces the installed target (S1) and what the action validates when it runs (S3).
- **Transfer:** An AppKit NSViewRepresentable on macOS with a rebound NSButton target-action pair.

**`G-8667bcae087a4e`** · UIKit · invalid-submit · unaided **pass** (primary pass). Pair: both-correct. · **P3 reserve-transfer** · duplicate

> I'm reviewing a UIKit change for tvOS 26.0. An invalid entry still reaches Save. Can you show the validation result and keep the user's input without submitting it?

- **Diagnosis:** Pair both-correct: rejects invalid submit and keeps input. Redundant with the macOS pair.
- **Prompt:** Hold for transfer with its preservation partner.
- **Oracle:** none
- **Skill:** none
- **Transfer:** A tvOS SwiftUI sign-in form.

**`G-876810bde2cad1`** · UIKit · container-children · unaided **pass** (primary pass). · **P2 pair-variant** · no-headroom · S8

> I'm reviewing a UIKit change for tvOS 26.0. A tester can reach the row but not all its individual controls. Can you preserve the grouping and still let people operate the children?

- **Diagnosis:** Repair passes by exposing the individual operable children alongside the supplementary action; the prompt states the symptom and goal. The iOS working copy (Q05) was a blind pass, so a tvOS working twin is missing.
- **Prompt:** Add a tvOS working twin where the row is already a non-element container exposing its buttons, with identical wording.
- **Oracle:** Assert accessibilityElements order and that each button's primary action still dispatches; do not require removing the supplementary action.
- **Skill:** In the working twin, adding grouping APIs is unnecessary.
- **Transfer:** A SwiftUI tvOS row using .accessibilityElement(children: .contain).

**`G-89482b39d6712d`** · UIKit · container-children · unaided **pass** (primary pass). · **P2 rewrite-neutral** · symptom-as-fact · S1, S8

> I'm reviewing a UIKit change for tvOS 26.0. A tester can reach the row but not all its individual controls. Can you preserve the grouping and still let people operate the children?

- **Diagnosis:** Repair passes by exposing children through a non-element shelf with the heading and buttons independently accessible. Same wording as G-876810bde2cad1 for a different mutant (grouping).
- **Prompt:** Ask which elements VoiceOver can reach individually rather than asserting that some controls are unreachable.
- **Proposed wording:** tvOS 26.0, UIKit. A shelf row has a heading, two buttons and a Details accessibility shortcut on the row. Which of these can a VoiceOver user reach individually with the remote, and can each button still be operated with Select?
- **Oracle:** Assert the exposed element order (heading, buttons) and that each button dispatches; grade the explanation separately.
- **Skill:** Neutral wording tests tracing the existing exposure before adding APIs.
- **Transfer:** An iOS UIKit table row with a grouped label and two buttons.

**`G-9076fc660dc5e1`** · UIKit · duplicate-id · unaided **pass** (primary pass). Pair: both-correct. · **P3 reserve-transfer** · duplicate

> I'm reviewing a UIKit change for tvOS 26.0. The server returned duplicate IDs. Can you reject the ambiguous update without leaving a partially updated screen?

- **Diagnosis:** Pair both-correct: rejects duplicate section IDs before altering shelves. Redundant with the macOS duplicate-ID set.
- **Prompt:** Hold for transfer with its preservation partner.
- **Oracle:** none
- **Skill:** none
- **Transfer:** A SwiftUI tvOS shelf grid.

**`G-955e952e1c1b59`** · UIKit · range-kind · unaided **pass** (primary pass). Pair: fixes-defect-breaks-working. · **P2 rewrite-neutral** · symptom-as-fact · S1

> I'm reviewing a UIKit change for tvOS 26.0. The player says I can seek through an interval that was only buffered. How should the inspector describe these two ranges?

- **Diagnosis:** Repair passes by evaluating seekable ranges independently of loaded ranges. Pair: the working partner (Q16) adds unneeded helpers, so the same asserted symptom yields fix-here, rework-there.
- **Prompt:** Use one neutral observation question for both pair members.
- **Proposed wording:** tvOS 26.0, UIKit player inspector. For an item whose buffered and seekable ranges differ, what does the inspector report for a time that has been buffered but is not seekable, and for one that is seekable? Please show how you would check it.
- **Oracle:** Same criterion for both sessions: seek decision uses seekable only, both ranges reported separately; rework graded separately.
- **Skill:** Tracing containsSeekableTime decides both versions.
- **Transfer:** An iOS AVPlayer live stream with a DVR window.

**`G-972553a39e3fd2`** · UIKit · rebound-action · unaided **pass** (primary pass). · **P2 rewrite-neutral** · symptom-as-fact · S3, S2

> I'm reviewing a UIKit change for tvOS 26.0. After refreshing a row, an action captured earlier can operate on the wrong record. Can you repair the ownership without losing the current action?

- **Diagnosis:** Repair passes by rejecting a saved Details action after the generation changes. Same wording as the shelf pair for a different mutant (stale shortcut), no working twin.
- **Prompt:** Ask neutrally what a saved shortcut does after refresh.
- **Proposed wording:** tvOS 26.0, UIKit. Each shelf row offers a Details accessibility shortcut. Rows can refresh while a VoiceOver user still has an earlier row's shortcut available. If that earlier shortcut runs after the refresh, which record does it open, and does the current row's shortcut still work?
- **Oracle:** Invoke the installed custom action captured before refresh; assert no details callback; then invoke the current one and assert the current key.
- **Skill:** Run the captured production closure (S2) that must validate its owner (S3).
- **Transfer:** A SwiftUI tvOS row with .accessibilityAction(named:) capturing an item.

**`G-9a70e4a2e9714c`** · UIKit · edited-matches · unaided **pass** (primary pass). · **P2 pair-variant** · no-headroom · S6

> I'm reviewing a UIKit change for tvOS 26.0. Editing the text outside our search callback leaves old search hits active. Can you make navigation use the current content?

- **Diagnosis:** Repair passes by re-evaluating matches for the current document and exercising a live text change. The prompt names the defect and the goal; no working twin.
- **Prompt:** Add a working twin where navigation already recomputes against current text, with identical wording.
- **Oracle:** Assert by literal substring at the returned range after an external edit.
- **Skill:** Literal substring check at the UIKit text boundary.
- **Transfer:** An iOS UITextView with external setText while a rotor is retained.

**`G-9cabdd49c15b29`** · UIKit · observer-stop · unaided **pass** (primary pass). · **P3 reserve-transfer** · duplicate · S3

> I'm reviewing a UIKit change for tvOS 26.0. An observer keeps reacting after the screen stops listening. Can you make teardown and a subsequent restart reliable?

- **Diagnosis:** Repair passes by checking observer lifetime and revision at queued delivery. iOS and macOS copies also pass; no headroom.
- **Prompt:** Hold for transfer.
- **Oracle:** none
- **Skill:** Revision check at delivery.
- **Transfer:** A SwiftUI tvOS onReceive publisher retained past disappearance.

**`G-9eaa902d2ca751`** · UIKit · missing-choice · unaided **pass** (primary pass). · **P2 rewrite-neutral** · no-headroom · S7

> I'm reviewing a UIKit change for tvOS 26.0. A requested option isn't in the available list. Can the picker leave the current choice intact instead of silently picking a replacement?

- **Diagnosis:** Repair passes; the prompt nearly states the fix (leave the current choice intact instead of picking a replacement). macOS copy also passes.
- **Prompt:** Ask what is selected afterward rather than proposing the expected outcome.
- **Proposed wording:** tvOS 26.0, UIKit. Someone asks our picker for a subtitle language that the current item does not offer. What is selected afterward, both on the player item and in our menu?
- **Oracle:** Assert the item's previous legible selection and the menu's selected entry are unchanged.
- **Skill:** Missing choice must not alter the actual item selection.
- **Transfer:** A SwiftUI tvOS audio picker given a language from a previous episode.

**`G-a6868ceeecdc4e`** · UIKit · validation-help · unaided **pass** (primary pass). · **P3 reserve-transfer** · duplicate

> I'm reviewing a UIKit change for tvOS 26.0. Error help remains after the user corrects the field. Can you clear only the transient error and restore the previous help?

- **Diagnosis:** Repair passes; clears the prior validation presentation and restores help. macOS copy passes.
- **Prompt:** Hold for transfer.
- **Oracle:** none
- **Skill:** none
- **Transfer:** A SwiftUI tvOS field with .accessibilityHint switching between help and error.

**`G-af7d70d999dee2`** · UIKit · preference-redelivery · unaided **pass** (primary pass). · **P3 pair-variant** · no-headroom

> I'm reviewing a UIKit change for tvOS 26.0. Receiving the same preference twice restarts work that should only happen on a transition. Can you avoid the repeat?

- **Diagnosis:** Repair passes by skipping identical readings and checking a changed Reduce Motion still propagates; the prompt names the fix.
- **Prompt:** Add a working twin with existing dedup, same wording.
- **Oracle:** none
- **Skill:** none
- **Transfer:** A SwiftUI tvOS view reacting to accessibilityReduceTransparency changes.

**`G-b3e3e24da9d1a2`** · UIKit · unavailable-media · unaided **pass** (primary pass). · **P3 reserve-transfer** · duplicate · S7

> I'm reviewing a UIKit change for tvOS 26.0. Opening the inspector before an item arrives says there are no accessible tracks. Can we distinguish not loaded from a successful empty result?

- **Diagnosis:** Repair passes by returning unavailable for a missing item. The iOS copy fails, making it the development case; the tvOS copy adds no tvOS-specific content.
- **Prompt:** Hold for transfer; develop on the failing iOS copy.
- **Oracle:** none
- **Skill:** Not-loaded vs empty is a media state distinction.
- **Transfer:** A SwiftUI tvOS inspector opened before AVPlayer.currentItem is set.

**`G-b4cbbde46d6d6f`** · UIKit · modal-state · unaided **pass** (primary pass). · **P3 reserve-transfer** · duplicate

> I'm reviewing a UIKit change for tvOS 26.0. When a panel closes the background doesn't always return to its previous state. How should this screen handle opening and closing it more than once?

- **Diagnosis:** Repair passes, restoring the recorded prior value and exercising repeated begin. All siblings pass.
- **Prompt:** Hold for transfer.
- **Oracle:** none
- **Skill:** none
- **Transfer:** A SwiftUI tvOS sheet toggling accessibilityViewIsModal on the presenter.

**`G-c69928988c0e26`** · UIKit · detached-action · unaided **fail** (primary fail). Blind audit Q55: pass/pass. · **P0 split-criteria** · oracle-mismatch · S3, S2

> I'm reviewing a UIKit change for tvOS 26.0. A detached button retained by other code can still act on the shelf. Can you reject it while keeping the current button usable?

- **Diagnosis:** Audit Q55 reversed the grade: directly removing the retained button now rejects it and an attached button still acts; the oracle also demanded rejection after reparenting, which the example never specified. Factorial split: removal all arms F/P; reparent arms F/P except review F/F.
- **Prompt:** Split direct removal and reparenting into separate questions, as the factorial children did.
- **Proposed wording:** tvOS 26.0, UIKit. If other code retains a shelf button and removes it directly from its superview, can it still choose an item? The current attached button must still work. ‖ tvOS 26.0, UIKit. A live button moves into a shelf belonging to a second shelves instance, without either owner reapplying its sections. Could the moved button still select an item on its former owner? The former owner's remaining buttons should still work.
- **Oracle:** Removal: dispatch the removed button (no selection, no callback) and an attached one (its key once); a superview check suffices. Reparent: old owner neither selects nor emits; remaining buttons work; the moved button may be inert. Regrade the frozen answer as a removal pass.
- **Skill:** Owner validation at invocation (S3), exercised through the actual primary action (S2).
- **Transfer:** A SwiftUI tvOS shelf where a UIKit-hosted cell is moved between two hosting controllers.

**`G-ce876ee37b4251`** · UIKit · eligible-target · unaided **pass** (primary pass). Pair: both-correct. · **P3 keep-control** · good-as-is · S4

> I'm reviewing a UIKit change for tvOS 26.0. After a refresh the original focus target may no longer belong here. Can you restore only to a usable target or fallback?

- **Diagnosis:** Pair both-correct: requires a candidate under the current root and exercises fallback.
- **Prompt:** none
- **Oracle:** none
- **Skill:** Membership in the current owner.
- **Transfer:** A SwiftUI tvOS @FocusState restore after the origin moves to a different section.

**`G-d175aa87437cc0`** · UIKit · audio-description-tag · unaided **pass** (primary pass). Pair: fixes-defect-breaks-working. · **P2 rewrite-neutral** · symptom-as-fact · S7, S2

> I'm reviewing a UIKit change for tvOS 26.0. The audio inspector calls ordinary language tracks described audio. How can we identify the marked options?

- **Diagnosis:** Repair passes by reading the explicit description characteristic. Pair: the working partner fails on proof and an unsupported alternative; the factorial child supplies neutral wording.
- **Prompt:** Use the factorial child's neutral wording for both pair members.
- **Proposed wording:** tvOS 26.0, UIKit. Can this inspector tell an ordinary alternate-language audio track from one explicitly tagged as described audio? Keep the current player selection.
- **Oracle:** Require both fixtures through the production mapping and compare native selected option before and after.
- **Skill:** Description tagging (S7), positive fixtures (S2).
- **Transfer:** An AppKit macOS media inspector listing audible options.

**`G-d314ae4053b207`** · UIKit · preserve-traits · unaided **pass** (primary pass). · **P3 retire-duplicate** · duplicate

> I'm reviewing a UIKit change for tvOS 26.0. Marking an item selected seems to remove information it had before. Can we update selection without disturbing its other properties?

- **Diagnosis:** Repair passes, mutating only the selected trait. Same check and wording as G-e4ff6e9fdfb106, with two iOS copies and an implementation twin also passing.
- **Prompt:** Retire; keep G-e4ff6e9fdfb106 for transfer and G-8786cf0f8c1bca as the tvOS unit task.
- **Oracle:** none
- **Skill:** none
- **Transfer:** n/a

**`G-e4ff6e9fdfb106`** · UIKit · preserve-traits · unaided **pass** (primary pass). · **P3 reserve-transfer** · duplicate

> I'm reviewing a UIKit change for tvOS 26.0. Marking an item selected seems to remove information it had before. Can we update selection without disturbing its other properties?

- **Diagnosis:** Repair passes, removing only the selected trait and checking preserved button traits. Redundant with iOS copies.
- **Prompt:** Hold for transfer.
- **Oracle:** none
- **Skill:** none
- **Transfer:** A SwiftUI tvOS chip whose traits are set by a modifier chain.

**`G-e5f494a161721e`** · UIKit · refresh-name · unaided **pass** (primary pass). Pair: fixes-defect-breaks-working. · **P3 keep-control** · good-as-is · S1

> I'm reviewing a UIKit change for tvOS 26.0. After a search result is selected, is its current status reported without the previous search label?

- **Diagnosis:** Repair passes by refreshing the explicit status label. Pair: the working partner (Q17) adds unneeded assignment. The question is already neutral, so this pair is a clean preservation test.
- **Prompt:** none
- **Oracle:** Grade both pair members on the effective label after selection; rework separately.
- **Skill:** Tracing the label path decides both versions.
- **Transfer:** A SwiftUI tvOS row with a conditional accessibilityLabel override.

**`G-eb72137f254296`** · UIKit · player-item-owner · unaided **pass** (primary pass). · **P2 pair-variant** · no-headroom · S3, S7

> I'm reviewing a UIKit change for tvOS 26.0. The player can replace its item from outside this view. Can you prevent an old lookup from updating the new item's details?

- **Diagnosis:** Repair passes, checking the actual player's item as well as the active ticket after external replacement. No working twin.
- **Prompt:** Add a working twin with the player-item check present, identical wording.
- **Oracle:** Exercise the old completion after replaceCurrentItem; assert new item details unchanged.
- **Skill:** Validating the actual current player item at completion.
- **Transfer:** A SwiftUI tvOS view model observing AVPlayer.currentItem via KVO.

**`G-ed8bff5491ab72`** · UIKit · visible-title · unaided **fail** (primary fail). Blind audit Q21: fail/fail. · **P0 keep-control** · real-model-gap · S5

> I'm reviewing a UIKit change for tvOS 26.0. Our buttons have accessibility metadata but no visible titles. Can you make the ordinary controls identifiable too?

- **Diagnosis:** Audit Q21 confirmed (registered key visible-title): both controls still have no visible title; the change and test address automation identifiers.
- **Prompt:** none
- **Oracle:** Keep, and assert the rendered title (configuration title or title(for:)) is non-empty and matches the accessible name; identifiers do not count.
- **Skill:** Visible title vs automation identifier is the S5 fact missed.
- **Transfer:** A SwiftUI tvOS toolbar of image-only Buttons with accessibilityIdentifier but no Label text.

**`G-edf906eca78e51`** · UIKit · request-generation · unaided **pass** (primary pass). Pair: both-correct. · **P3 retire-duplicate** · duplicate

> I'm reviewing a UIKit change for tvOS 26.0. A late response from an earlier request overwrites a newer result. Can you give the current request ownership of the update?

- **Diagnosis:** Pair both-correct: rejects stale validation. Ten-sibling decision with near-universal passes.
- **Prompt:** Retire the tvOS copy with its preservation partner.
- **Oracle:** none
- **Skill:** none
- **Transfer:** n/a

**`G-ffb1a82a74699a`** · UIKit · preference-redelivery · unaided **pass** (primary pass). · **P3 retire-duplicate** · duplicate

> I'm reviewing a UIKit change for tvOS 26.0. Receiving the same preference twice restarts work that should only happen on a transition. Can you avoid the repeat?

- **Diagnosis:** Repair passes by short-circuiting identical status before animation. Same wording and decision as G-af7d70d999dee2.
- **Prompt:** Retire; G-af7d70d999dee2 carries the tvOS redelivery decision.
- **Oracle:** none
- **Skill:** none
- **Transfer:** n/a

#### tvOS · preservation (14)

**`G-000ddc4f9a5ec5`** · UIKit · range-kind · unaided **fail** (primary pass). Blind audit Q16: fail/pass. Pair: fixes-defect-breaks-working. · **P1 grade-components** · rework-only · S1, S8

> I'm reviewing a UIKit change for tvOS 26.0. The player says I can seek through an interval that was only buffered. How should the inspector describe these two ranges?

- **Diagnosis:** Audit Q16: primary pass held (buffered vs seekable distinguished) but the answer adds two public helpers despite the leave-working-code instruction; pair: partner repair passes, so this is avoidable rework, not a seek regression. Same pattern in Q52 (iOS) and Q60 (macOS).
- **Prompt:** Replace the asserted symptom (the player says I can seek a buffered-only interval) with the neutral observation question used for its repair partner, so both sessions get identical wording.
- **Oracle:** Score separately: primary (seek decision consults seekable ranges only), preservation (existing inspector API unchanged), rework (new public helpers or queries counted as rework, not as failure of primary), evidence. Whole pass should not require zero edits when the edit is harmless, but must flag unrequested public API.
- **Skill:** The existing containsSeekableTime path already answers the request, so tracing it (S1) and not adding helpers (S8) is the whole decision.
- **Transfer:** An AVPlayer HLS live-window inspector on tvOS where the seekable window slides; working code reports both ranges and the question asks what the scrub bar should allow.

**`G-03942c8939b2cc`** · UIKit · audio-description-tag · unaided **fail** (primary pass). Blind audit Q25: fail/pass. Pair: fixes-defect-breaks-working. · **P1 grade-components** · evidence-only · S2, S7

> I'm reviewing a UIKit change for tvOS 26.0. The audio inspector calls ordinary language tracks described audio. How can we identify the marked options?

- **Diagnosis:** Audit Q25: primary pass (main code keeps the explicit description characteristic) but an alternative proposes an unsupported property and the test filters by its own output, so it can pass with no ordinary track. Factorial description-tags: all four arms F/P; neither addition fixes the proof.
- **Prompt:** Adopt the factorial child's neutral wording (ordinary alternate-language vs explicitly tagged described audio, keep the current selection) for both pair members.
- **Oracle:** Grade primary, preservation and evidence separately. Evidence requires both fixtures (ordinary alternate false, tagged described true) through the production mapping and compares the native selected option before and after; a filtered empty list cannot pass.
- **Skill:** The persistent failure across all arms is the missing positive fixture (S2) on a media characteristic distinction (S7).
- **Transfer:** An iOS/tvOS audio menu built from AVAsset legible and audible groups where SDH captions must be distinguished from ordinary subtitles.

**`G-06049073ef34c8`** · UIKit · invalid-submit · unaided **pass** (primary pass). Pair: both-correct. · **P3 reserve-transfer** · duplicate · S1

> I'm reviewing a UIKit change for tvOS 26.0. An invalid entry still reaches Save. Can you show the validation result and keep the user's input without submitting it?

- **Diagnosis:** Pair both-correct: concludes the existing validation path shows the error, keeps input and stops before Save. The macOS pair also passes, so this tvOS copy adds no new evidence.
- **Prompt:** Move the tvOS invalid-submit pair to the transfer reserve; keep the macOS pair as the development control.
- **Oracle:** none
- **Skill:** A correct no-change conclusion from tracing the existing path.
- **Transfer:** A tvOS SwiftUI sign-in form using the on-screen keyboard where Save is a focusable Button.

**`G-0d69f79fef78e5`** · UIKit · conflicting-state-text · unaided **fail** (primary pass). Blind audit Q23: pass/pass. Pair: both-fail. · **P0 specify-policy** · ambiguous-policy · S1, S5

> I'm reviewing a UIKit change for tvOS 26.0. The control state changes but its status text tells a different story. Can you keep the two consistent on successive updates?

- **Diagnosis:** Audit Q23 reversed the grade: status, accessibility value and selected trait already follow the input; the answer's one-line native isSelected sync satisfies a plausible reading of control state, and the oracle ignores isSelected. Factorial selected-status with specified scope: unaided F/F, review sentence P/P, both P/P.
- **Prompt:** Name which state the user observes (status text, accessibility value, selected trait) and scope out native isSelected, as the factorial child did; that wording produced the only review-sentence gain.
- **Proposed wording:** tvOS 26.0, UIKit. On each selected or unselected update, our tile needs its readable status text, the button's accessibility value and its selected accessibility trait to agree. Native button selection is managed elsewhere. Does this implementation keep those three in sync across successive updates?
- **Oracle:** On one instance configure selected, unselected, selected; compare status text, accessibility value and selected trait independently with expected state; accept equivalent localized wording; do not require or penalize native isSelected. Grade rework separately.
- **Skill:** Factorial shows the review sentence (S1) earns the pass; S5 supplies selected-state wording.
- **Transfer:** A SwiftUI tvOS filter chip with .accessibilityValue and .isSelected trait and a visible checkmark label.

**`G-19b9622db7d85f`** · UIKit · duplicate-id · unaided **pass** (primary pass). Pair: both-correct. · **P3 reserve-transfer** · duplicate · S1

> I'm reviewing a UIKit change for tvOS 26.0. The server returned duplicate IDs. Can you reject the ambiguous update without leaving a partially updated screen?

- **Diagnosis:** Pair both-correct: identifies the preflight section and item checks and tests atomic rejection. macOS copies also pass, so the tvOS pair is redundant.
- **Prompt:** Hold the tvOS duplicate-ID pair for transfer.
- **Oracle:** none
- **Skill:** A correct no-change trace.
- **Transfer:** A SwiftUI tvOS grid with NSDiffableDataSourceSnapshot-like duplicate identifiers.

**`G-3b6a6a3d39e6de`** · UIKit · grapheme-boundary · unaided **pass** (primary pass). Pair: both-correct. · **P3 keep-control** · good-as-is · S6

> I'm reviewing a UIKit change for tvOS 26.0. A match covering only part of a composed character should not be offered as a navigation destination. Does this code enforce that?

- **Diagnosis:** Pair both-correct on a neutral question (does this code enforce it?): explains both grapheme boundaries and checks a partial match. A sound UIKit text-boundary control on tvOS, where the iOS range-coordinate failures did not recur.
- **Prompt:** none
- **Oracle:** none
- **Skill:** Checks UTF-16 endpoints against composed-character boundaries with a literal partial match.
- **Transfer:** An AppKit NSTextView on macOS with a regional-indicator flag and a combining accent in the search text.

**`G-506996f8af1af4`** · UIKit · ordinary-action · unaided **fail** (primary fail). Blind audit Q44: fail/fail. Pair: fixes-defect-breaks-working. · **P1 grade-components** · real-model-gap · S1, S8, S5

> I'm reviewing a UIKit change for tvOS 26.0. The added shortcut works but the ordinary action no longer does. Can you keep both paths working on the current item?

- **Diagnosis:** Audit Q44 confirmed a behavior failure: the ordinary Details button and shortcut already dispatch, yet the answer treats Play's accessibilityActivate method as an assignable closure, so the patch and test are unusable. Pair: partner repair passes.
- **Prompt:** Use the same neutral path question as its repair partner (G-29109948779ad1) rather than asserting the ordinary action is broken.
- **Oracle:** Grade primary (existing ordinary and shortcut paths reach the current item), validity (proposed code compiles against UIKit), rework and evidence separately; an invalid override is both rework and a compile failure.
- **Skill:** No override was needed (S1, S8); accessibilityActivate is an overridable method, not a property (S5).
- **Transfer:** An AppKit row on macOS where the model is tempted to override accessibilityPerformPress on a working NSButton.

**`G-51c53f30543cc0`** · SwiftUI · interop-rebind · unaided **fail** (primary pass). Blind audit Q43: fail/pass. Pair: fixes-defect-breaks-working. · **P1 grade-components** · rework-only · S1, S8

> I'm reviewing a SwiftUI change for tvOS 26.0. The wrapper updates its SwiftUI state but the native button can still send to the previous target. Can you fix the binding and teardown?

- **Diagnosis:** Audit Q43: primary pass held; the answer rewrites coordinator cleanup and changes macOS and teardown for an unshown view mismatch even though rebinding already invalidates the old callback. Pair: repair partner passes, so the fixture fixes the defect and reworks the working copy. Q27 (macOS) and Q41 (iOS) repeat the pattern.
- **Prompt:** Use the same neutral wording as its repair partner instead of asserting that the native button still sends to the previous target.
- **Oracle:** Separate primary (old native control and old callback cannot reach the new handler; dismantle stops dispatch), rework (unrequested teardown or cross-platform edits) and evidence (a negative-only test that also passes the original counts as weak proof). Grade a harmless equivalent rewrite as pass with rework noted.
- **Skill:** Tracing configure and dismantle shows the existing path already satisfies the request; the rework is the failure.
- **Transfer:** A UIViewRepresentable wrapping a native UISegmentedControl on tvOS where the coordinator is rebound across list rows.

**`G-5f1114d75bd50c`** · SwiftUI · optional-help · unaided **pass** (primary pass). Pair: both-correct. · **P3 reserve-transfer** · duplicate · S1, S8

> I'm reviewing a SwiftUI change for tvOS 26.0. After switching from an item with help text to one without it, the old help is still there. Can you repair the update path?

- **Diagnosis:** Pair both-correct: correctly concludes that the optional assignment already clears the old hint and exercises the nil transition. Strong preservation control, but redundant with the iOS SwiftUI preservation copy that also passes.
- **Prompt:** Move the tvOS SwiftUI optional-help pair to the transfer reserve; keep the iOS pair and failing macOS preservation (Q22) for development.
- **Oracle:** none
- **Skill:** The pass is the behavior S1 and S8 aim for; keep it unseen as a transfer control.
- **Transfer:** A UIKit tvOS reused cell where accessibilityHint is set from an optional and must clear when nil.

**`G-61cfbceeb763f0`** · UIKit · rebound-action · unaided **fail** (primary fail). Blind audit Q45: fail/fail. Pair: fixes-defect-breaks-working. · **P0 rewrite-neutral** · real-model-gap · S1, S3

> I'm reviewing a UIKit change for tvOS 26.0. After refreshing a row, an action captured earlier can operate on the wrong record. Can you repair the ownership without losing the current action?

- **Diagnosis:** Audit Q45 confirmed an actual regression on working code: a detached old button can select when its ID persists, and the answer's test expects that stale selection. This is the shelf example of fixing one version and breaking the working one.
- **Prompt:** Use the same neutral before-and-after wording as G-46f5727d65e9f2 so the symptom stated as fact no longer invites a patch to correct code.
- **Proposed wording:** tvOS 26.0, UIKit shelf. Rows can refresh while a button from before the refresh is still retained by other code. If someone presses Select on that earlier button, which record does it affect, and which record does a current button affect after the refresh?
- **Oracle:** Grade primary (stale action rejected, current works), preservation (no re-enabling of obsolete actions), evidence (a test expecting stale selection is invalid) and rework separately; mark this as critical regression.
- **Skill:** The review sentence (S1) targets exactly this; the stale-capture rule is S3.
- **Transfer:** A SwiftUI tvOS shelf where the existing code already validates a revision token in the button action.

**`G-b786b16b81d406`** · UIKit · eligible-target · unaided **pass** (primary pass). Blind audit Q28: pass/pass. Pair: both-correct. · **P3 keep-control** · good-as-is · S4, S1

> I'm reviewing a UIKit change for tvOS 26.0. After a refresh the original focus target may no longer belong here. Can you restore only to a usable target or fallback?

- **Diagnosis:** Audit Q28 pass confirmed: preserves membership and ancestor eligibility checks and verifies fallback and no eligible destination. Pair both-correct; a strong preservation control for the registered eligible-target key.
- **Prompt:** none
- **Oracle:** none
- **Skill:** Correct no-change outcome on the S4 destination rule.
- **Transfer:** A SwiftUI tvOS focus restoration using @FocusState after a list refresh.

**`G-c7ecafc1f5d659`** · UIKit · forced-vs-full · unaided **pass** (primary pass). Blind audit Q02: pass/pass. Pair: inconclusive. · **P1 specify-policy** · ambiguous-policy · S7, S2

> I'm reviewing a UIKit change for tvOS 26.0. Our captions menu offers a forced-only translation as if it were full subtitles. Can you keep those choices distinct?

- **Diagnosis:** Audit Q02 pass held (selection filter already excludes forced-only), but its optional test needs an asset and can pass if no full option is ever selected. Pair is inconclusive with G-76f5ee001339bc, and Q03 shows full vs forced can mean exclusion or a separate labeled choice.
- **Prompt:** State the menu's product policy for forced-only tracks so exclusion and labeled-choice designs are not both plausible.
- **Proposed wording:** tvOS 26.0, UIKit. Our captions menu is meant to list complete subtitle tracks only; forced-only translations are played automatically by the player and are not menu choices. A tester thinks a forced-only translation appeared in the menu as if it were full subtitles. For an asset with English full, English forced-only and French full subtitles, which choices does this menu offer?
- **Oracle:** Use a real or fixture group with all three options; assert the offered list literally; require the full English option to be present before asserting forced is absent; grade the proposed test separately.
- **Skill:** Forced vs full and menu policy is S7; the positive fixture requirement is S2.
- **Transfer:** A SwiftUI tvOS caption Picker where the policy instead labels forced-only tracks as a separate choice.

**`G-d960994bd1947a`** · UIKit · request-generation · unaided **pass** (primary pass). Pair: both-correct. · **P3 retire-duplicate** · duplicate

> I'm reviewing a UIKit change for tvOS 26.0. A late response from an earlier request overwrites a newer result. Can you give the current request ownership of the update?

- **Diagnosis:** Pair both-correct: old form and media responses cannot replace newer outcomes. The decision has ten siblings, nearly all passing, including four preservation controls.
- **Prompt:** Retire the tvOS copy from the active panel; keep one iOS and one macOS pair.
- **Oracle:** none
- **Skill:** none
- **Transfer:** n/a

**`G-f0de252053bcbb`** · UIKit · refresh-name · unaided **fail** (primary fail). Blind audit Q17: fail/pass. Pair: fixes-defect-breaks-working. · **P1 grade-components** · rework-only · S1, S8

> I'm reviewing a UIKit change for tvOS 26.0. After a search result is selected, is its current status reported without the previous search label?

- **Diagnosis:** Audit Q17: blind primary pass (explicit assignment yields the right label; clearing the override already restores the text-derived name), original primary fail; the answer's stale-cache claim lacks evidence. Pair: repair partner passes.
- **Prompt:** Keep the question; it is already neutral (is the status reported without the previous label?).
- **Oracle:** Grade primary on the effective label after selection, separately from rework (unneeded explicit assignment) and unsupported claims. Correct the frozen primary judgment in a versioned regrade.
- **Skill:** Tracing the override-clearing path shows no change is needed.
- **Transfer:** A SwiftUI tvOS result row where .accessibilityLabel is conditionally applied and removal should restore the Text-derived name.

#### tvOS · implementation (33)

**`G-0ad013a4877500`** · SwiftUI · open rubric · unaided **fail** (primary inconclusive). · **P1 split-criteria** · real-model-gap · S3, S7

> # tvOS developer request

- **Diagnosis:** Ledger: whole fail because old option callbacks call choose with a nullable ID and no captured owner, so a stale Off can clear a later selection; primary is inconclusive because the rubric bundles result ownership, option callbacks, cancellation and retry. The same stale-Off mechanism recurs in G-c6b25ad753e6a2.
- **Prompt:** Split the bundled ownership request into a late-result question and a stale-menu-action question, so the Off failure can be graded on its own.
- **Proposed wording:** tvOS 26.0, SwiftUI player using one shared AVPlayer. People can leave and come back, or switch videos, while caption options are still loading, and they can retry a failed load. When a load started for an earlier video finishes late, what does the current screen show? ‖ tvOS 26.0, SwiftUI player using one shared AVPlayer. A caption menu built for an earlier video is still presented when the video changes, and the viewer chooses Off or a track from it. What happens to the current video's captions? Please include focused unit tests.
- **Oracle:** Criterion A: late success or error for an earlier video leaves the current video's state unchanged; retry for the current video applies. Criterion B: an Off or track choice captured for an earlier video or request does not change the current item's legible selection; a current Off does. Assert on the player item's selection, not local state.
- **Skill:** A nullable-ID callback with no captured owner is the S3 pattern, and Off as a distinct selection on the real item is S7.
- **Transfer:** A UIKit tvOS player with an AVPlayerViewController transport-bar menu where audio-track choices from the previous episode remain installed.

**`G-19d3be9a5d1d73`** · UIKit · open rubric · unaided **inconclusive** (primary inconclusive). · **P2 keep-control** · grader-uncertain · S3

> Our UIKit tvOS screen has ordered shelves, each with a heading and ordinary item buttons. Section IDs are unique, and item IDs are unique within a section, but an item ID can repeat across sections. Updates may reorder, rename or remove she

- **Diagnosis:** Ledger rationale is attempt-error: no gradable answer exists, so the inconclusive is a harness failure, not a model or prompt outcome. The prompt itself is well specified (section-qualified selection, atomic duplicate rejection, detached buttons).
- **Prompt:** none
- **Oracle:** Record this cell as a harness error, exclude it from model denominators, and rerun once under the frozen wording; then grade with the shelf-structure rubric split into structure, atomic rejection and stale-button criteria.
- **Skill:** The detached and retained button requirement is a callback-ownership contract, once a real answer exists.
- **Transfer:** A SwiftUI tvOS shelf grid with repeated item IDs across rows and a retained focusable cell from a removed row.

**`G-1ae8568fe43fd6`** · UIKit · open rubric · unaided **pass** (primary inconclusive). · **P2 repair-oracle** · grader-uncertain · S3

> For our tvOS UIKit app, build a reusable episode card with a title, Play and Details buttons. Each button needs its own callback and complete localized accessible name. Offer Details as an optional accessibility action on Play as well. The 

- **Diagnosis:** Implementation pass with primary inconclusive: the answer keeps separate Play/Details callbacks and guards the Details shortcut on current availability, but the rubric gives no executable check for reuse or disabled Details.
- **Prompt:** Keep the request; add that the unit tests should reuse the card for a second episode and disable Details, so the inconclusive branches become the asked-for checks.
- **Oracle:** Add focused assertions: after configuring episode B, Play's Details custom action reports B; with Details disabled the action returns false and calls nothing; ordinary Details still dispatches via primaryActionTriggered.
- **Skill:** The shortcut must read the current episode and enabled state at invocation, an S3 ownership check.
- **Transfer:** A SwiftUI tvOS episode tile with .accessibilityAction(named:) and a reused view model.

**`G-22af858f9af21f`** · SwiftUI · open rubric · unaided **pass** (primary inconclusive). · **P2 grade-components** · bundled-criteria · S4

> Target tvOS26, SwiftUI.

- **Diagnosis:** Implementation pass with primary inconclusive: uses sheet generation and active state, rejects stale dismissal and tests a synchronous next presentation. The rubric bundles entry target, return target, fallback, stale completion and reentry.
- **Prompt:** Keep the wording; ask that each requirement get its own named test so components can be graded independently.
- **Oracle:** Grade components: (1) entry focus target; (2) return request resolves at completion to origin or persistent fallback; (3) stale or repeated completion requests nothing; (4) a restoration that opens another sheet is not undone. Score focus requests, not delivered focus, since unit tests cannot observe the focus engine.
- **Skill:** Every component is a restore-after-completion destination rule from S4.
- **Transfer:** A UIKit tvOS modal with UIFocusEnvironment preferredFocusEnvironments and setNeedsFocusUpdate after dismissal.

**`G-231795c762c2e0`** · SwiftUI · open rubric · unaided **pass** (primary inconclusive). · **P1 raise-to-integration** · weak-endpoint · S7

> Target tvOS26, SwiftUI.

- **Diagnosis:** Implementation pass, but the prompt excludes applying AVMediaSelection (records a preference only), so the task stops before the developer-observable result. FIRST-ITERATION names exactly this: changing a local selected ID is insufficient when the player item must reflect the choice.
- **Prompt:** Extend the task to the player item so the outcome is the selection the viewer actually hears and sees, keeping the async options list and stability requirements.
- **Proposed wording:** tvOS 26.0, SwiftUI player that must keep the supplied AVPlayer and its native controls. Our own caption menu lists options that load asynchronously and can reorder, disappear or arrive late. After someone picks a caption track or Off, the current player item should play with that choice, and audio, volume and mute should stay as they were. The current item can also already have a caption selection that is not in our list. Provide complete code and focused compile/unit tests; no UI automation.
- **Oracle:** Assert on the item's current legible selection after choose, Off, a late list reply and a removed option; assert audible selection, volume and mute unchanged; a current selection outside the list is reported as such, not as Off.
- **Skill:** Writing the actual player item's selection and distinguishing Off and an unlisted current choice is S7.
- **Transfer:** A UIKit tvOS AVPlayerViewController with transportBarCustomMenuItems driving the same selection.

**`G-365faed8f7362b`** · SwiftUI · open rubric · unaided **fail** (primary inconclusive). · **P1 grade-components** · real-model-gap · S5, S7

> # tvOS developer request

- **Diagnosis:** Ledger: Off is written with the Objective-C spelling selectMediaOption(nil,in:) while tracks use the Swift select(_:in:), so the Off path is likely not valid Swift; primary is inconclusive because nothing compiled. An API-spelling miss like the edit-category key.
- **Prompt:** Keep the wording; add that the submission must compile against the tvOS 26 SDK, so API spelling is in scope rather than inferred.
- **Oracle:** Compile the submission against the tvOS 26 SDK. Grade separately: (1) track choice writes the item's legible group; (2) Off writes no legible option through a valid API; (3) audible selection unchanged; (4) forced-only options not offered.
- **Skill:** The exact Swift API for Off (S5) on the actual player item (S7).
- **Transfer:** A UIKit tvOS caption menu where Off must be written to the current AVPlayerItem through the Swift overlay.

**`G-369095f8f4ecec`** · UIKit · open rubric · unaided **pass** (primary inconclusive). · **P3 keep-control** · good-as-is · S3

> Our tvOS app uses AVPlayer. We asynchronously load a short description of its current AVPlayerItem through an injected callback on the main actor. Items can be replaced externally, the same item can be inspected again, and results can arriv

- **Diagnosis:** Implementation pass with primary inconclusive: checks request and actual player item and exercises same-item reinspection, duplicate callback and teardown. Well-specified prompt ending at an observable state; inconclusive only because the review is source-only.
- **Prompt:** none
- **Oracle:** Run the unit contract on the unchanged submission where possible: external replaceCurrentItem before completion, reinspection of the same item, duplicate callback, and playback rate unchanged.
- **Skill:** Guards validation of both request token and actual current item at callback time.
- **Transfer:** A SwiftUI tvOS view model loading chapter titles for AVPlayer.currentItem with async/await and Task cancellation.

**`G-375ea9d9a373c3`** · SwiftUI · open rubric · unaided **pass** (primary inconclusive). · **P3 keep-control** · good-as-is · S3

> Target tvOS26, SwiftUI with UIKit interop.

- **Diagnosis:** Implementation pass with primary inconclusive: updates the retained native button and replaces its handler across rebind and dismantle. Overlaps G-aac1829e33a43a and the interop-rebind fixtures.
- **Prompt:** none
- **Oracle:** Run a rebind test: fire the old button's target after coordinator rebinding and after dismantle, asserting the new handler count is zero; check no retain cycle via weak reference.
- **Skill:** Captured action validation at run time.
- **Transfer:** An AppKit NSViewRepresentable wrapping NSButton on macOS.

**`G-3f40dc5a5d6e80`** · UIKit · open rubric · unaided **pass** (primary inconclusive). · **P3 keep-control** · good-as-is · S2, S7

> For a tvOS player inspector, extract audio/subtitle option names, languages, audio-description and forced-only flags, and which options are selected. Load asset metadata asynchronously. Distinguish no current item, a successfully loaded but

- **Diagnosis:** Implementation pass with primary inconclusive: reads tagged metadata and current native selection without mutation and separates an absent group from a load error. The prompt asks what a tagged silent asset can establish, which keeps the evidence honest.
- **Prompt:** none
- **Oracle:** Require a positive tagged fixture before any absence assertion, and compare selected options before and after inspection.
- **Skill:** Positive fixtures (S2) for forced and described flags (S7).
- **Transfer:** A SwiftUI tvOS diagnostics overlay reading AVAsset media selection groups with load(.availableMediaCharacteristicsWithMediaSelectionOptions).

**`G-41dc4d2f1594dd`** · UIKit · open rubric · unaided **pass** (primary inconclusive). · **P3 keep-control** · good-as-is · S4, S2

> Our tvOS UIView owns Play and Details buttons. We prefer Play, then Details, when focus enters the card. Either button may be disabled, hidden, transparent or removed during an update. Implement preferred focus candidates for that policy an

- **Diagnosis:** Implementation pass with primary inconclusive: checks containment and enabled, visible state before preferring Play or Details, and the prompt asks whether the unit result shows which view got focus. This targets the tvOS gap between focus preference and delivered focus.
- **Prompt:** none
- **Oracle:** Assert preferredFocusEnvironments for hidden, alpha-zero, disabled and removed Play; and require the answer to say that a unit test shows candidates only, not delivered focus.
- **Skill:** Eligible destination selection (S4) and the limit of what unit tests can assert (S2).
- **Transfer:** A SwiftUI tvOS card using .prefersDefaultFocus within a focusScope where Play can be hidden.

**`G-55c3b232938702`** · SwiftUI · open rubric · unaided **inconclusive** (primary inconclusive). · **P2 specify-policy** · ambiguous-policy · S7

> # tvOS developer question

- **Diagnosis:** Implementation inconclusive: the answer encodes a missing current item as a particular failure message, and the rubric cannot tell whether that is separable from a retryable load failure. The prompt lists loading, absent options and failure but not a missing item.
- **Prompt:** State the no-current-item case as its own developer-visible state and say whether retry applies to it.
- **Proposed wording:** tvOS 26.0, SwiftUI. Build a caption and audio picker that uses the same AVPlayer as the video view and shows the item's real current selection. The screen can appear before the player has an item. People should be able to tell apart: no video yet, options still loading, a video with no options, and a load that failed and can be retried. Keep normal player controls and include focused unit tests. Here is the complete current file:
- **Oracle:** Separate criteria for each of the four states; retry is offered for failure only; the picker reads selection from the player item, not local state.
- **Skill:** Reading selection from the actual item and distinguishing its states is S7.
- **Transfer:** A UIKit tvOS AVPlayerViewController custom menu populated from AVAsset loading states.

**`G-568f3cf50e437f`** · UIKit · open rubric · unaided **inconclusive** (primary inconclusive). · **P1 repair-oracle** · grader-uncertain · S4

> In our UIKit/tvOS app, closing a modal should request a return to the original button, or a fallback if that button is no longer eligible in the owning view. The controls may be removed, hidden or disabled while the modal is open. A new mod

- **Diagnosis:** Implementation inconclusive: presentation tokens and visibility checks are present, but attachment to a window does not establish membership in the owning view, which is the eligible-target distinction confirmed as a gap on macOS (Q07).
- **Prompt:** Keep the wording; add that the original button can be moved into another view of the same window while the modal is open, so the membership case is stated.
- **Oracle:** Add a checkable case: the original button is moved into another view in the same window while the modal is open; completion must use the owning-view fallback. Also assert duplicate completion requests once and a replaced modal's cancellation requests nothing.
- **Skill:** Membership in the correct owner, not just a window, is the S4 rule.
- **Transfer:** A SwiftUI tvOS sheet whose originating tile is moved to a different shelf while the sheet is up.

**`G-5d121776613655`** · SwiftUI · open rubric · unaided **fail** (primary inconclusive). · **P1 grade-components** · real-model-gap · S7

> # tvOS developer question

- **Diagnosis:** Implementation fail: selected is assigned before options are checked, so an unknown ID changes displayed state while the native choice is unchanged. The prompt explicitly asks to preserve a current choice outside the list without pretending it is Off; the mismatch is substantive.
- **Prompt:** Keep the wording; it already states the unlisted-current-choice policy, which is what the answer missed.
- **Oracle:** Grade separately: (1) known choice writes the player item's legible selection; (2) unknown request leaves displayed and native selection unchanged; (3) an unlisted current selection is shown as such, not Off; (4) audio and playback settings unchanged.
- **Skill:** Unlisted current selection and real-item writes are S7.
- **Transfer:** A UIKit tvOS caption menu where the current item starts with an SDH track not offered by the menu's filter.

**`G-659283ab576494`** · UIKit · open rubric · unaided **inconclusive** (primary inconclusive). · **P2 repair-oracle** · grader-uncertain · S6, S2

> In our UIKit tvOS reader, users can read and select the original text normally. Add a custom accessibility rotor for literal search matches, without replacing ordinary text access. Text and query can change while an old search result or rot

- **Diagnosis:** Implementation inconclusive: literal match, boundary and retained-rotor tests are present, but exact native text-range handling on tvOS is unresolved in source review. Grading needs a decisive substring check.
- **Prompt:** Keep the wording; ask the tests to read the selected text at the returned range, so the native range question is answerable.
- **Oracle:** Add assertions that the rotor's returned range, applied to the text view, selects the literal query after an emoji and combining mark; and that a retained rotor from old text returns nothing.
- **Skill:** UTF-16 ranges checked by literal substring (S6) through the installed rotor callback (S2).
- **Transfer:** An iOS UITextView reader with the same rotor and a mixed-script document.

**`G-70ad36b8473f50`** · UIKit · open rubric · unaided **pass** (primary inconclusive). · **P2 grade-components** · bundled-criteria · S1, S8

> This UIKit tvOS26 component is reused for search results and selection. After search runs, configure changes the visible status but the accessibility label can still describe the previous result count. Fix the stale state without removing t

- **Diagnosis:** Implementation pass with primary inconclusive: refreshes selection and search metadata both ways and keeps native controls and modal flag. The prompt preserves five unrelated behaviors in one verdict.
- **Prompt:** Keep the fixture; list the five preserved behaviors as separate expected checks so rework and preservation are graded one by one.
- **Oracle:** Grade the stale label in both update orders as primary; grade each preserved behavior (ordinary controls, selected traits, reduced transparency, native player controls, modal flag) as its own preservation item; flag unrelated edits as rework.
- **Skill:** Most of the component already works; restraint is graded per preserved behavior.
- **Transfer:** A SwiftUI tvOS result tile with .accessibilityLabel derived from two models updated in either order.

**`G-758be0954385e0`** · UIKit · open rubric · unaided **pass** (primary inconclusive). · **P3 keep-control** · good-as-is · S2

> We are adding a diagnostic snapshot to our tvOS AVPlayer app. Capture duration, loaded and seekable ranges, buffer flags, rate, time-control status and waiting reason without modifying playback. Missing item data must stay distinguishable f

- **Diagnosis:** Implementation pass with primary inconclusive: reports seekability and buffer state separately and tests inside and outside times. Overlaps the range-kind fixtures but ends at a usable snapshot.
- **Prompt:** none
- **Oracle:** Require fixture ranges where loaded and seekable differ, so the helper's answer for a buffered-only time is decisive.
- **Skill:** A positive differing fixture makes the range check meaningful.
- **Transfer:** n/a

**`G-7b7cd43b77e209`** · UIKit · open rubric · unaided **pass** (primary inconclusive). · **P3 keep-control** · good-as-is

> In our UIKit tvOS app, an editable email field has an ordinary Save button and optional help text. A supplied synchronous, side-effect-free validator returns either a nonempty localized error or nil. On invalid Save, show the error without 

- **Diagnosis:** Implementation pass with primary inconclusive: keeps invalid input, avoids Save, restores help on edit and guards synchronous reentry. Well-scoped.
- **Prompt:** none
- **Oracle:** none
- **Skill:** none
- **Transfer:** A SwiftUI tvOS form with a validator closure and .accessibilityHint for help.

**`G-8786cf0f8c1bca`** · UIKit · open rubric · unaided **pass** (primary inconclusive). · **P3 keep-control** · no-headroom

> In a UIKit Apple TV app, a Play button already has accessibility traits configured by another part of the app. Add and remove its selected state without losing the other traits. Give a small implementation and unit tests that exercise both 

- **Diagnosis:** Implementation pass: inserts or removes the selected trait and checks unrelated traits. The prompt names the behavior; it is the representative selected-trait unit task on tvOS.
- **Prompt:** none
- **Oracle:** none
- **Skill:** none
- **Transfer:** A SwiftUI tvOS chip using .accessibilityAddTraits(.isSelected) conditionally.

**`G-882146ff80c2a4`** · SwiftUI · open rubric · unaided **pass** (primary inconclusive). · **P3 grade-components** · bundled-criteria

> Target tvOS26, SwiftUI with UIKit.

- **Diagnosis:** Implementation pass with primary inconclusive: publishes final selection before callbacks, keeps it across name edits and retains content under reduced transparency. Many behaviors share one verdict.
- **Prompt:** Keep the wording; ask for one named test per behavior so each can be graded separately.
- **Oracle:** Separate selection-before-callback, unchanged-request suppression, reduced motion final state, reentrant change and reduced transparency, each with its own assertion.
- **Skill:** none
- **Transfer:** An AppKit SwiftUI-hosted card on macOS with the same snapshot model.

**`G-8e63e559f86929`** · UIKit · open rubric · unaided **pass** (primary inconclusive). · **P3 keep-control** · good-as-is · S3

> Our UIKit tvOS form has editable name and email fields. Validation is supplied as a callback-based service that takes a snapshot of both strings and eventually returns a dictionary of field IDs to nonempty error messages; an empty dictionar

- **Diagnosis:** Implementation pass with primary inconclusive: submission ownership, validated field IDs and messages, ordering, edit and cancellation. Well-specified.
- **Prompt:** none
- **Oracle:** none
- **Skill:** Completion validates the submission token at run time.
- **Transfer:** A SwiftUI tvOS two-field form with an async/await validator.

**`G-9f59e96226e92f`** · SwiftUI · open rubric · unaided **pass** (primary inconclusive). · **P3 grade-components** · bundled-criteria · S3

> Target tvOS26, SwiftUI.

- **Diagnosis:** Implementation pass with primary inconclusive: atomic duplicate rejection, surviving selection and revision-guarded actions. Several behaviors share one verdict.
- **Prompt:** Keep the wording; ask for one named test per listed requirement.
- **Oracle:** Grade duplicate rejection, selection survival, deleted-selection clearing, shortcut navigation and revision-guarded actions separately.
- **Skill:** Revision-guarded captured actions are S3.
- **Transfer:** A UIKit tvOS article table with custom rotor for important rows.

**`G-a424d7b520fd26`** · UIKit · open rubric · unaided **fail** (primary inconclusive). · **P2 split-criteria** · bundled-criteria · S8

> For our UIKit tvOS Downloads area, preserve the ordinary Open control and readable status. Give the region and controls useful names, show selection in text as well as accessibility state, and clear stale names and state when reused. Reduce

- **Diagnosis:** Implementation fail: the answer asks clarifying questions instead of building. The prompt bundles about nine requirements (names, selection text, reuse, transparency, AVKit, modal scope, search group, multiline text), which invites deferral in a tool-free setting.
- **Prompt:** Split into a reusable Downloads row task and a separate search-and-modal task so each has a developer-observable result.
- **Proposed wording:** tvOS 26.0, UIKit Downloads area. Each reused row has an ordinary Open control and readable status, and shows whether it is selected. When a row is reused for another download, its name and state should describe the new one, and Reduce Transparency should affect only the backdrop. Please implement the row with focused unit tests. ‖ tvOS 26.0, UIKit Downloads area. Above the list is a labeled search field with a result-count status and a filter. A modal can open and close more than once over this area while the native AVKit player keeps running. Implement the search group and modal metadata scope with focused unit tests.
- **Oracle:** Grade each split question on its own criteria; record a clarification-only answer as non-attempt, attributed to harness and model rather than accessibility knowledge.
- **Skill:** Smaller scoped tasks reduce generic boilerplate and invented scope.
- **Transfer:** A SwiftUI tvOS Downloads list with the same split.

**`G-a684bb499d9f1a`** · SwiftUI · open rubric · unaided **pass** (primary inconclusive). · **P3 grade-components** · bundled-criteria · S5, S8

> Target tvOS26, SwiftUI with UIKit.

- **Diagnosis:** Implementation pass with primary inconclusive: updates heading, status, names and optional hint in place and checks order and scalable fonts; the prompt also forbids claiming the TV27 Larger Text feature. Many behaviors share one verdict.
- **Prompt:** Keep the wording; ask for one named test per listed requirement, including a statement of what the text-size configuration does and does not promise on tvOS 26.0.
- **Oracle:** Separate in-place refresh, absent-value clearing, non-color selected readout, preserved trait bits and children order, and the text-size claim (no TV27 promise on a 26.0 target).
- **Skill:** The text-size boundary is S5; preserving unrelated trait bits is S8.
- **Transfer:** A UIKit tvOS report card without SwiftUI where the same snapshot drives UILabel and UIButton.

**`G-aa46615d2f4cd8`** · UIKit · open rubric · unaided **pass** (primary inconclusive). · **P3 keep-control** · good-as-is · S3

> Our UIKit Apple TV screen displays result buttons from items with a stable ID, a visible title and a localized action name. Filtering is case-insensitive. Preserve the selected item only while it remains in the filtered results. Repeated ID

- **Diagnosis:** Implementation pass with primary inconclusive: gates old button dispatch by render generation and tests duplicates, filtering and selected removal. Same fixture family as the shelf pair, so it shows the model can build the guard when the requirement is explicit.
- **Prompt:** none
- **Oracle:** none
- **Skill:** Generation validation at dispatch.
- **Transfer:** A SwiftUI tvOS search results grid.

**`G-aac1829e33a43a`** · SwiftUI · open rubric · unaided **pass** (primary inconclusive). · **P3 keep-control** · good-as-is · S3, S2

> Target tvOS26, SwiftUI with UIKit.

- **Diagnosis:** Implementation pass with primary inconclusive: checks ordinary and shortcut dispatch, rebinding, disabled controls and post-dismantle callbacks. Well specified.
- **Prompt:** none
- **Oracle:** Run the rebind and dismantle assertions on the installed shortcut closure rather than a reconstructed one.
- **Skill:** The installed-action check is S2; ownership is S3.
- **Transfer:** An AppKit NSViewRepresentable card on macOS.

**`G-c60353787b2df0`** · UIKit · open rubric · unaided **pass** (primary inconclusive). · **P3 keep-control** · good-as-is · S5, S3

> In our UIKit/tvOS app, a screen needs the current Reduce Motion, Reduce Transparency and increased-contrast settings when it starts, then updates when those settings change. It may stop and restart while an update is already queued. Repeate

- **Diagnosis:** Implementation pass with primary inconclusive: checks execution token and started state at delivery and deduplicates snapshots. The prompt asks for correct platform notification registration, a tvOS fact worth checking literally.
- **Prompt:** none
- **Oracle:** Check the notification names used exist on tvOS 26 for each of the three settings.
- **Skill:** Notification availability on tvOS (S5); token at delivery (S3).
- **Transfer:** An iOS UIKit screen with the same observer and restart race.

**`G-c6b25ad753e6a2`** · SwiftUI · open rubric · unaided **fail** (primary inconclusive). · **P1 grade-components** · real-model-gap · S3, S7

> # tvOS developer question

- **Diagnosis:** Implementation fail: the option setter receives item identity but no request revision, so after reloading the same item an old Off callback still applies. Second observation of the stale-Off ownership gap after G-0ad013a4877500.
- **Prompt:** Keep the wording; add that the same video can be reloaded while an earlier caption list is on screen, so the same-item reload is stated rather than implied.
- **Oracle:** Grade separately: item change, same-item reload, stale Off, current choice, cancellation. Assert against the player item's legible selection after an old Off fires.
- **Skill:** Validating both item and request (S3) for the Off selection (S7).
- **Transfer:** A UIKit tvOS AVPlayerViewController menu rebuilt on reload of the same asset.

**`G-d9e53ce2b01786`** · SwiftUI · open rubric · unaided **inconclusive** (primary inconclusive). · **P2 repair-oracle** · evidence-only · S2, S5

> Target tvOS26, SwiftUI.

- **Diagnosis:** Implementation inconclusive: selected-state text and preference modifiers are present, but tests reflect a view, which cannot show how the policy handles motion or text size at the target version.
- **Prompt:** Keep the wording; ask that motion, transparency and text-size decisions be returned from a testable policy, so evidence can be a literal value.
- **Oracle:** Require an extracted policy function (inputs: reduce motion, reduce transparency, size category) with literal expected outputs; reject reflection as evidence; check no TV27 Larger Text promise.
- **Skill:** Asserting the returned policy value is S2; the TV26/TV27 boundary is S5.
- **Transfer:** A UIKit tvOS status view with the same preference policy object.

**`G-dc1e54ce99c977`** · SwiftUI · open rubric · unaided **fail** (primary inconclusive). · **P1 grade-components** · real-model-gap · S7

> # tvOS developer request

- **Diagnosis:** Implementation fail: tests missing video, empty load and retry, but picker selection stays local instead of writing to the shared player's media group, although the prompt says it uses the same player and selection state.
- **Prompt:** Keep the wording; it already says the picker uses the same player and selection state, which the answer ignored.
- **Oracle:** Grade states (missing video, loading, empty, error, retry) separately from wiring: a choice must change the shared item's media selection, asserted on the item.
- **Skill:** Writing the actual player item's selection is S7.
- **Transfer:** A UIKit tvOS player with a custom subtitle panel sharing AVPlayer with AVPlayerViewController.

**`G-ecaf99703fde8f`** · SwiftUI · open rubric · unaided **pass** (primary inconclusive). · **P3 keep-control** · good-as-is · S8

> Target tvOS26, SwiftUI.

- **Diagnosis:** Implementation pass with primary inconclusive: keeps ordinary settings controls and implements five-point adjustments through the bounded setter. The prompt already warns not to invent a Toggle defect.
- **Prompt:** none
- **Oracle:** none
- **Skill:** Preserving a valid native Toggle is restraint.
- **Transfer:** A UIKit tvOS settings screen with accessibilityIncrement on a custom volume view.

**`G-f180f315211c36`** · UIKit · open rubric · unaided **pass** (primary inconclusive). · **P3 keep-control** · good-as-is

> A tvOS status label changes between loading, ready and failure messages. We optionally animate the transition, depending on Reduce Motion. The final visible and accessible message must be available even when animation is skipped. Avoid repe

- **Diagnosis:** Implementation pass with primary inconclusive: suppresses duplicate status and selects effects from the current motion preference.
- **Prompt:** none
- **Oracle:** none
- **Skill:** none
- **Transfer:** A SwiftUI tvOS status overlay with contentTransition gated by reduce motion.

**`G-fb3f74a9ac6641`** · UIKit · open rubric · unaided **inconclusive** (primary inconclusive). · **P2 repair-oracle** · grader-uncertain · S7, S2

> Our tvOS app uses AVPlayerItem. Add helpers for explicit language selection, optionally requiring audio description, and for turning a group off when allowed. A subtitle language choice should pick a full subtitle option, not a forced-only 

- **Diagnosis:** Implementation inconclusive: empty-selection permission and language and description matching are implemented, but executability of synthetic AVMediaSelectionGroup subclasses is unresolved.
- **Prompt:** Keep the wording; state that a bundled tagged test asset is available, so tests need not subclass AVFoundation groups.
- **Oracle:** Supply a real-group fixture seam or bundled tagged asset; grade matching logic separately from fixture executability; assert audio selection unchanged after subtitle change and missing choice leaves selection alone.
- **Skill:** Forced vs full, Off permission and preserved audio are S7; a real fixture is S2.
- **Transfer:** A SwiftUI tvOS selection helper over a bundled HLS asset.

**`G-fe5ec3a625e9f0`** · SwiftUI · open rubric · unaided **pass** (primary inconclusive). · **P3 keep-control** · good-as-is · S3

> Target tvOS26, SwiftUI.

- **Diagnosis:** Implementation pass with primary inconclusive: keeps entered text and covers service failure, duplicates, delayed results and cancellation.
- **Prompt:** none
- **Oracle:** none
- **Skill:** Obsolete replies validated at delivery.
- **Transfer:** A UIKit tvOS email form with the same validator contract.

#### tvOS · historical (12)

**`G-044112eec58beb`** · SwiftUI · open rubric · unaided **pass** (primary inconclusive). · **P3 keep-control** · no-headroom · S3

> A delayed stream status reply updates our SwiftUI binding. Accept only the current item's current request, even if two loads were for the same item. Rejected replies must not write the binding.

- **Diagnosis:** rc1 contract: the prompt states the rule (accept only the current item's current request, even for the same item) and the signature; the pass shows the model can implement a stated rule, not that it would find it. Primary inconclusive only because historical rc1 grades are not unaided results.
- **Prompt:** none
- **Oracle:** Run the rc1 unit contract on the unchanged submission (two requests for the same item, the earlier reply arriving last) and record primary from that assertion rather than leaving it inconclusive.
- **Skill:** Guards the same-item request identity that G-5f3c8c25e44c4b and G-c6b25ad753e6a2 missed when the rule was not stated.
- **Transfer:** n/a

**`G-1584405193ce1b`** · UIKit · open rubric · unaided **inconclusive** (primary inconclusive). · **P2 repair-oracle** · grader-uncertain · S3, S7

> I am using UIKit on tvOS 26 deployment target; available validation anchor tvOS 26.5.

- **Diagnosis:** Dev7 design question: ledger finds cancellation and item identity handled on success, but same-item retry and error ownership are not established; inconclusive because the scoring key has no checkable criterion for those branches.
- **Prompt:** Keep the wording (it already lists no-match, failure, in-progress and item change); add one sentence that a load can be retried for the same item, so the graded same-item branch is stated.
- **Oracle:** Add explicit criteria: (1) a retry on the same item makes the first request's late error or success inert; (2) item change before completion leaves the new item's state untouched; (3) the user's selected audio and captions are read, never written. Accept any token scheme that satisfies all three.
- **Skill:** The gap is what the completion validates when it runs (S3) and preserving the user's media selection (S7).
- **Transfer:** n/a

**`G-169764b693c452`** · UIKit · open rubric · unaided **pass** (primary inconclusive). · **P3 keep-control** · no-headroom · S4

> When a panel finishes dismissing, choose the original button if it is still in the supplied eligible list and enabled; otherwise use the first enabled button in the list, or nil. Return a request target only.

- **Diagnosis:** rc1 contract: the prompt spells out the restoration rule (opener if eligible and enabled, else first enabled, else nil); the pass shows rule execution only.
- **Prompt:** none
- **Oracle:** Run the rc1 unit contract and record primary from it: removed opener, disabled opener, all disabled returns nil.
- **Skill:** Encodes the eligible-destination fallback in S4 as a literal contract.
- **Transfer:** n/a

**`G-3c9d02537a525d`** · UIKit · open rubric · unaided **pass** (primary inconclusive). · **P3 retire-duplicate** · duplicate

> This button's selected state changes on reuse. Update just the accessibility selected trait without erasing any other traits.

- **Diagnosis:** rc1 contract: update only the selected trait; passes. G-8786cf0f8c1bca asks for the same behavior with unit tests and both preserve-traits repairs pass, so this adds nothing.
- **Prompt:** Retire from the active portfolio; keep the historical record unchanged.
- **Oracle:** none
- **Skill:** none
- **Transfer:** n/a

**`G-5e241a2f3c435f`** · SwiftUI · open rubric · unaided **inconclusive** (primary inconclusive). · **P2 repair-oracle** · grader-uncertain · S3, S8

> I am using SwiftUI on tvOS 26 deployment target; available validation anchor tvOS 26.5.

- **Diagnosis:** Dev7 design question inconclusive: ordinary Open and Delete are kept and a supplementary Delete action added, but the shortcut's enabled-state and current-owner checks are not substantiated in the example.
- **Prompt:** Keep the wording; ask the example to show the shortcut after the row is reused for a different file and while disabled.
- **Oracle:** Criterion: the self-contained example's Delete accessibility action reads the row's current file at invocation, does nothing while the row is disabled, and leaves ordinary Open and Delete buttons in place. Unit check calls the installed action after reuse.
- **Skill:** The open question is what the action validates when it runs (S3), while S8 guards against removing ordinary buttons.
- **Transfer:** n/a

**`G-5f3c8c25e44c4b`** · UIKit · open rubric · unaided **fail** (primary inconclusive). · **P1 specify-policy** · oracle-mismatch · S3

> I am using UIKit on tvOS 26 deployment target; available validation anchor tvOS 26.5.

- **Diagnosis:** Ledger fails the answer because file identity alone lets an earlier load for the same file replace newer metadata. The prompt's stated race is A arriving after B; it never says the same file can be loaded twice, so the oracle demands an unstated requirement.
- **Prompt:** State whether a file can be reloaded while an earlier load is pending; the current wording only establishes the A-after-B race.
- **Proposed wording:** tvOS 26.0, UIKit. I reuse one download card for different files. It has a title, optional status, optional help text, selected state and an Open button. Updates can arrive without reconstructing the card: A has status Ready and help Opens offline; B has neither. Metadata for a file can be requested again while an earlier request for it is still pending, and a late result for A may arrive after B is shown. Describe a complete update strategy and focused unit checks, and keep Open working.
- **Oracle:** Grade A-after-B rejection and stale help/status clearing as primary; grade same-file reload ownership only under the amended wording. Re-grade the frozen answer under the original wording without the reload requirement.
- **Skill:** What a late completion validates (file plus request) is S3.
- **Transfer:** n/a

**`G-79d7d5bb05ed7d`** · SwiftUI · open rubric · unaided **pass** (primary inconclusive). · **P3 keep-control** · good-as-is · S8

> I am using SwiftUI on tvOS 26 deployment target; available validation anchor tvOS 26.5.

- **Diagnosis:** Dev7 design pass: groups descriptive text without absorbing Open and Details and identifies entries by current report. Primary inconclusive only from the source-only key.
- **Prompt:** none
- **Oracle:** none
- **Skill:** Guards grouping that keeps ordinary buttons reachable instead of combining them away.
- **Transfer:** n/a

**`G-92cd811da55d55`** · any · open rubric · unaided **pass** (primary inconclusive). · **P3 keep-control** · good-as-is · S5

> We deploy to tvOS 26. Does compiling on a newer SDK establish system Larger Text support on that deployment target? Please separate what is known from what needs an availability source.

- **Diagnosis:** Dev7 boundary question passes: separates compile SDK from deployment capability and asks for an availability source. Primary inconclusive only because the key has no literal check. It is the conceptual twin of the confirmed tv-text-reflow failure (Q32), which shows the model knows the principle but misapplies it in code.
- **Prompt:** none
- **Oracle:** Make the criterion checkable: the answer must not claim system Larger Text support from SDK version alone, and must name the deployment-target behavior separately from any later-SDK branch.
- **Skill:** Directly protects the tvOS availability-boundary fact S5 would supply.
- **Transfer:** n/a

**`G-9b4965749be4ab`** · UIKit · open rubric · unaided **pass** (primary inconclusive). · **P3 keep-control** · good-as-is · S4

> I am using UIKit on tvOS 26 deployment target; available validation anchor tvOS 26.5.

- **Diagnosis:** Dev7 lifecycle pass: resolves the current opener or eligible fallback and marks the session resolved before external focus dispatch. Primary inconclusive only from the source-only key.
- **Prompt:** none
- **Oracle:** Make the criterion checkable: duplicate completion requests once; an older completion after a new panel opens requests nothing; deleted opener falls back to the first eligible item or no request.
- **Skill:** Restore after completion to an eligible destination with a declared fallback.
- **Transfer:** n/a

**`G-c55650380597ef`** · SwiftUI · open rubric · unaided **fail** (primary inconclusive). · **P1 keep-control** · evidence-only · S2

> I am using SwiftUI on tvOS 26 deployment target; available validation anchor tvOS 26.5.

- **Diagnosis:** Dev7 testing question fails: proposes Mirror reflection as evidence that accessibility modifiers are attached and treats model chapter counts as rotor behavior. The question is itself about evidence, so this is a substantive verification misconception.
- **Prompt:** none
- **Oracle:** Criterion: the plan must state that compile and unit checks establish only extracted state and wiring, that spoken output and rotor behavior are unestablished, and must not offer reflection as accessibility evidence.
- **Skill:** Defines what a unit test can and cannot assert, the S2 boundary.
- **Transfer:** n/a

**`G-e686599aab0959`** · SwiftUI · open rubric · unaided **pass** (primary inconclusive). · **P3 keep-control** · no-headroom

> Our focus effect is optional. Return the supplied SwiftUI animation unchanged when motion is allowed, but no animation for Reduce Motion. An absent effect should remain absent.

- **Diagnosis:** rc1 contract: return the optional animation unchanged unless Reduce Motion; the prompt states the full rule, so the pass shows execution only.
- **Prompt:** none
- **Oracle:** Run the rc1 unit contract (nil stays nil, reduced returns nil, allowed returns the same value).
- **Skill:** none
- **Transfer:** n/a

**`G-f4ec597a9a2e91`** · SwiftUI · open rubric · unaided **pass** (primary inconclusive). · **P3 keep-control** · good-as-is

> tvOS 26.0, SwiftUI.

- **Diagnosis:** OS26 acceptance pass: replaces a tap gesture with a remote-operable named control bound to the corresponding movie. Primary inconclusive only because historical grades are not unaided results. A useful guard against iOS touch assumptions on tvOS.
- **Prompt:** none
- **Oracle:** Criterion: each tile is a focusable Button (or equivalent) operable with Select, its name includes the movie title, and open receives the matching movie.
- **Skill:** none
- **Transfer:** A UIKit tvOS collection view where cells use a UITapGestureRecognizer instead of didSelectItemAt.

#### tvOS · workflow (6)

**`G-0a672785e8c227`** · SwiftUI · color-only-live · unaided **pass** (primary pass). · **P3 keep-control** · good-as-is

> tvOS, SwiftUI. On our sports shelf a red border means Live, but focus also adds a border. Some viewers cannot tell which event is live. How would you communicate both facts without changing what Select does?

- **Diagnosis:** Workflow pass: adds a non-color Live cue independent of the focus border and leaves Select unchanged. The prompt names the need without giving the fix; useful color-only control.
- **Prompt:** none
- **Oracle:** none
- **Skill:** none
- **Transfer:** A UIKit tvOS EPG grid where a red dot marks recording and focus scaling also changes tint.

**`G-58e05a888e5745`** · UIKit · selected-vs-focused · unaided **pass** (primary pass). · **P3 keep-control** · good-as-is · S5

> tvOS, UIKit. A language tile under the remote cursor announces Selected before I press Select. Moving away also clears the actual selected language. How should highlighting and committed choice interact?

- **Diagnosis:** Workflow pass: separates the focused tile under the remote from the committed language and updates selected traits only on Select. The prompt states two symptoms but they are observations, not a fix; this is a tvOS-specific control for focus vs selection.
- **Prompt:** none
- **Oracle:** Keep, and assert two observable effects: moving focus away does not change the committed language, and the selected trait appears only after Select.
- **Skill:** Selected-state wording and the focus-vs-selection distinction on tvOS are platform facts in S5.
- **Transfer:** A SwiftUI tvOS audio-language row where focus effects use .focused state and a separate committed choice.

**`G-90ab2116d21630`** · UIKit · directional-escape · unaided **pass** (primary pass). · **P3 keep-control** · good-as-is

> tvOS, UIKit. A horizontal shelf has a sponsored tile at the end. Moving Right from it keeps bouncing to the first tile, and moving Down never reaches the next shelf. How would you review this focus behavior while preserving Select on every 

- **Diagnosis:** Workflow pass: removes the horizontal loopback, gives a Down exit to the next shelf, and preserves Select. The prompt describes remote-navigation observations without the fix; a good tvOS focus-engine control.
- **Prompt:** none
- **Oracle:** Assert two outcomes: Right at the last tile does not wrap to the first, Down reaches the next shelf; Select still opens each tile.
- **Skill:** none
- **Transfer:** A UIKit UICollectionView shelf with a custom focus guide that traps focus at the trailing edge.

**`G-9e4dfb3fc78f7f`** · SwiftUI · initial-focus-once · unaided **pass** (primary pass). · **P3 keep-control** · good-as-is · S4

> tvOS, SwiftUI. The details screen should start on Resume. If I move to Extras while artwork is loading, focus jumps back to Resume when the image arrives. When should the initial target be chosen?

- **Diagnosis:** Workflow pass: chooses initial focus on entry and preserves button identity through artwork updates. The prompt asks when to choose the target, not what to change; good tvOS control.
- **Prompt:** none
- **Oracle:** none
- **Skill:** Guards against re-requesting focus after an async update, a destination-timing rule.
- **Transfer:** A UIKit tvOS details screen whose preferredFocusEnvironments is reevaluated by setNeedsFocusUpdate when the poster loads.

**`G-e56a902ef372a2`** · SwiftUI · tv-text-reflow · unaided **fail** (primary fail). Blind audit Q32: fail/fail. · **P0 grade-components** · real-model-gap · S5

> tvOS, SwiftUI. Product wants titles readable from a couch. A long German title in our tvOS SwiftUI detail header crowds out Play and Details. What would you change on a 26.0 deployment target, and what would you condition on a newer SDK?

- **Diagnosis:** Audit Q32 confirmed (registered key tv-text-reflow): the vertical layout protects Play and Details, but the newer-SDK section gates at tvOS 18 on a 26.0 deployment, treats scrollTargetLayout as marquee, and gives no valid later availability boundary.
- **Prompt:** Keep the wording frozen as the confirmed development case; the deployment-target and newer-SDK halves are already separate and need separate grades.
- **Oracle:** Grade separately: (1) deployment-target layout keeps Play and Details reachable with the long German title; (2) availability: no gate below the deployment target, any later API carries a verified boundary or an explicit unverified note; (3) no misattributed API behavior. The current verdict should record (1) pass and (2) fail.
- **Skill:** The precise tvOS availability boundary is the S5 fact that was missing.
- **Transfer:** A UIKit tvOS product page with a UILabel title and UIStackView of buttons where the team asks what tvOS 27 text-size settings would change.

**`G-ec1532605b0eae`** · UIKit · filter-focus-fallback · unaided **pass** (primary pass). · **P3 keep-control** · good-as-is · S4

> tvOS, UIKit. While someone is browsing live channels, a filter removes the focused channel. The list can become empty. How should the next focus target be chosen without opening a channel?

- **Diagnosis:** Workflow pass: separates playback from focus and computes a surviving fallback, including an empty list. The prompt asks how to choose the target, not what to change; good tvOS control.
- **Prompt:** none
- **Oracle:** Check that the answer requests focus on a surviving channel or a declared container fallback when empty, and that no channel opens.
- **Skill:** A declared fallback when the focused item is removed is S4.
- **Transfer:** A SwiftUI tvOS LazyHGrid with .focused bindings when a genre filter empties a row.
<!-- items:end -->

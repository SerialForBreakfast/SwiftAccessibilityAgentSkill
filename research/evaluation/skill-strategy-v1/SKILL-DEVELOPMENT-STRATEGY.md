# Skill development strategy and gold-prompt audit

Research document, November 8, 2026. It covers three things:
1. **Best practices** for developing an Agent Skill, from published guidance and our own runs.
2. **An audit** of how we build and evaluate the Swift accessibility skill against those practices.
3. **Recommendations for every gold prompt:** 56 signal-panel questions in full, the 6 OS26 and 21 further gold-parity prompts in full, and the other 302 discovery prompts by decision key. Each covers the question itself and the skill content that should close its gap.

This document proposes changes only. No skill, candidate, prompt, oracle or baseline was changed. No model ran.

**Evidence base:**
- **Signal-v2 paired return:** 56 questions, Gemini 3.8 Flash Low, unaided vs installed, 107 graded answers. Private copy: `evals/results/signal-v2-review-20261108/`. Published scorecard: `evals/reports/signal-panel-v2-flash/` on origin/main.
- **The 384-prompt discovery review:** [PROMPT-IMPROVEMENTS.md](../prompt-improvements-v1/PROMPT-IMPROVEMENTS.md).
- **The prompt sets:**
  - OS26 gold set: [GoldPrompts.md](../../../GoldPrompts.md);
  - [gold-parity audit](../gold-parity-v1/TASKS.md);
  - the untracked [signal-v3 draft](../signal-panel-v3/README.md).
- **External guidance:** twelve sources, summarized in [sources.md](sources.md). Bracketed numbers such as [5] cite them.

**Reproduce:**
- `python3 -B build.py --check` (joined data);
- `python3 -B render.py` (generated sections);
- `python3 -B verify.py` (ids, enums, answer-overlap screen, document sync, links).

## 1. Decision first: how to get a large gain

Signal-v2 is the first candidate with a clear paired effect:
- **On 53 pairs:** 9 whole-task gains and 0 losses. Primary behavior 8 gains / 1 loss; rework 12 / 1.
- **Where the gains came from:** every gain came from a session that opened the skill and read a relevant card.
- **Where it fell short:** 40 pairs still fail in both arms. Two new critical flags followed reads of one card.

The next large gain comes from five changes, in this order:

1. **Get the skill opened.**
   - **The size of the problem:** 19 of 54 installed sessions read nothing. They produced 0 gains and 18 both-fail pairs. One card, validation.md, was never opened in 54 sessions.
   - **The likely cause:** signal-v2 cut the description to one sentence with no "use when" clause. The skill-creator guidance says models tend to undertrigger and recommends a fuller, more insistent description [5]. The description is the only thing a model sees before deciding to load a skill [1, 3].
   - **The fix:** restore a complete what-and-when description with the trigger terms this audit found missing (section 4.2). Measure triggering separately with a should-trigger / near-miss set [2, 5].
2. **Remove the instruction that coincided with harm, and add decision-point contrasts.**
   - **return.md:** "Consume a matching request before invoking reentrant code" preceded all three return-card critical flags. Replace it with capture-at-presentation, and name `makeFirstResponder`'s refusal-and-fallback. The v3 draft adds the right contrasts but keeps the risky sentence.
   - **media.md:** answers read it eight times, and seven of those pairs still failed. Its rules are correct but abstract. Give one ordered path (item → asset group → `select` → read back → publish), name the described-audio constant, and separate a missing item from an empty group.
3. **Add native-control facts that stop rewrites of working code.**
   - facts.md produced 4 gains from 8 reads, the best yield of any card.
   - Rework failures on working Sliders, Reduce Motion and selected-trait code show the same kind of single named fact is missing there.
4. **Build every check shape into the cards.** 40 pairs failed in both arms. In many of them the code was right but the proof was not:
   - the test configures only once;
   - it calls a helper instead of the field's own event;
   - it stubs framework objects;
   - it chooses fixtures by the property under test.

   Each card should end with the two-step check that would have exposed its defect. v3 already does this for three cards.
5. **Change how we measure before the next batch.**
   - **What to change:**
     - repeat each item × condition three times;
     - report results split by whether the skill was read;
     - grade natively wherever a contract exists;
     - validate the source-review grader against native results;
     - keep a transfer set that is never tuned on [6, 9, 11, 12, 14].
   - **Why it matters:** single samples have already driven churn. dev.7 against dev.5 (9 vs 11 of 24) prompted dev.8, yet the sign tests give p ≈ 0.5–0.6.

**This shape fits "many aspects per iteration".** One candidate can carry all of the content fixes in sections 6–8. The three kinds of change stay separable:
- **Description changes** are measured by the trigger set.
- **Content changes** are judged only on sessions that read the card.
- **Check-shape changes** are graded as their own verification component.

Isolate one variable with an ablation only when a regression needs explaining.

## 2. Best practices

Each practice has a check and our current status. **F** = follows, **P** = partial, **G** = gap.

| # | Practice | How we know we follow it | Our status | Evidence in this repo |
|---:|---|---|:-:|---|
| 1 | The description says what the skill does and when to use it, names concrete trigger terms, and stays under 1,024 characters [1, 2, 4, 5] | Description review against a trigger list | **G** | 0.2.2: ~800 characters, keyword-heavy. rc.1: a use clause plus a do-not clause. Signal-v2: one sentence, no when-clause. |
| 2 | Triggering is measured separately, using ~20 should-trigger and near-miss queries over 3 runs with a held-out split [2, 5] | A trigger score per description | **G** | No trigger test exists. Invocation was measured only incidentally: rc.1 auto 1/12, explicit 3/3. v2: 35/54 corroborated reads. |
| 3 | Triggering, reading and applying are reported per session [1, 2, 6] | Every report splits results by read and not read | **P** | The v2 return has traces, but the headline pools sessions that read the skill with those that didn't. Section 3 of this document does the split. |
| 4 | Prompts have measured headroom: an unaided pass rate below the ceiling over several trials [2, 5, 6] | Baseline pass rate stored per prompt | **P** | The 384 baseline (263 pass) was one trial. The 56-question panel was chosen from failures, but 4 pairs pass both and some historical failures no longer reproduce. |
| 5 | Each content paragraph traces back to an observed failure [2, 3, 9] | Every card line names its case | **P** | Signal v2 and v3 cards are failure-driven; 0.2.2's 104 reference files are not. |
| 6 | The oracle is audited before grading: a reference solution passes, alternatives pass, mutants fail [6, 8] | Qualification gates | **F/P** | OS26: 42/42 gates and 12/12 mutants. v3: positive, alternative and mutant runs. Gold-parity: 2/78 criteria have direct evidence. The 384 review confirmed two first-grade errors. |
| 7 | Grade outcomes, not paths; accept valid alternatives [6, 7] | Alternative implementations pass | **P** | Component grades exist, and review proposals accept alternatives. Some criteria still require one mechanism; see the Tier 2 notes. |
| 8 | Code graders come before LLM judges, and the judge is from a different model family [6, 7, 9] | Native lane on every gradable answer | **G** | The v2 grades are source review by the BigDog coordinator. No answer was compiled. The native lane exists (`evals/rc1/grader/`) but was not used. |
| 9 | Judges are validated against expert labels by true-positive and true-negative rates [8, 9, 10] | A judge scorecard | **G** | The source review missed checkout-font, which fails natively. The blind audit reversed some grades. No TPR/TNR has been measured. |
| 10 | Rubrics are frozen and versioned per comparison [10] | Rubric hash in each run | **F** | Sealed packets and hash-pinned controller files. |
| 11 | No decision rests on a single sample; report standard errors or pass^k [6, 11, 12] | Three or more trials per cell | **G** | Every comparison so far is one trial per cell. |
| 12 | Conditions are compared paired on the same items in the same batch, with clustered errors for shared fixtures [11, 12] | Paired design | **F** | v2 used identical bytes, alternating order and isolated sessions. Twins and shared sources are not yet clustered. |
| 13 | A power calculation is done before spending [11, 12] | Minimum effect and N written down | **G** | Batch sizes follow quota, not a stated effect size. |
| 14 | Candidate churn is capped and a held-out set is kept [5, 8, 11] | A transfer set that was never tuned on | **G** | About 13 candidates in a week. The panel is development-only, and no transfer set has been run. |
| 15 | Error analysis comes before changes, with a taxonomy that separates model, harness, oracle, grader and content [6, 8, 9] | A coded failure taxonomy | **P** | The failure inventory and 384 review exist. This document adds a gap-type taxonomy per prompt (section 6). |
| 16 | Token cost is a tracked success criterion [1, 4, 5, 7] | Cost per condition in the report | **P** | v2 reports tokens: installed is 2.4× unaided. No cost limit or quality-per-token target is set. |
| 17 | References sit one level deep; unread cards are cut or re-signaled [2, 3, 4] | A read count per card | **P** | The v2 layout is flat. 0.2.2 ships 104 files, including ADRs and watchlists that SKILL.md tells the model not to load, plus a duplicate `skill/manifests/`. |
| 18 | Each instruction gives one default with a reason, not a menu; deterministic checks are scripts [2, 3, 5] | Card review | **P** | Several failures offered unrequested alternative designs. The cards themselves are mostly single-default, but they don't forbid offering weaker alternatives. |
| 19 | Every target model and harness is tested and reported separately [2, 4, 6] | A per-model table | **P** | Haiku is the development target, but the v2 evidence is Gemini only. |
| 20 | Eval sets are balanced with no-change and do-not-trigger cases [5, 6] | Control share | **F/P** | Preservation and sentinel axes exist, and OS26 has a no-change control. There are no do-not-trigger queries. |

## 3. Audit of the process

### 3.1 How the loop actually runs

The intended loop is in `research/evaluation/failure-driven/PRD.md`: source claim, executable contract, observed difficulty, adjudicated case, independent prompt, frozen baseline, focused skill change, paired evaluation. In practice:

- **Discovery:**
  - frontier authoring incidents;
  - dev.5 and dev.7 critical flags;
  - the 384-prompt unaided Gemini baseline;
  - a failure inventory that merges them.
- **Authoring:**
  - paired evidence packages (claim, contract, question, criteria, case);
  - controller-only vectors (reference, alternative, mutant, test);
  - bulk prompt reviews.
- **Candidates:** built by scripts, byte-reproducible, pinned by hash. Successors are built from sealed parents.
- **Dispatch:**
  - BigDog single exchange;
  - an append-only attempt ledger with an owner-set budget and interruption policy;
  - a strict answer contract.
- **Grading:**
  - masked source review with component grades;
  - a reviewed native lane for compile and unit work;
  - blind audits by Codex reviewers.
- **Promotion:** gates are proposed in `ROADMAP-0.3.md` and `evals/release-gates.json` but have never been attempted. 0.2.2 is unchanged since November 4.

### 3.2 Findings

| Area | What works | Gap | Recommended change |
|---|---|---|---|
| **Iteration cadence** | Reproducible candidates; sealed parents | About 13 candidates in a week, 4–5 model-evaluated. One commit touched the released skill. About 87% of commits are measurement or reconciliation, and research prose outweighs skill text by about 8.4 to 1 (`CurrentStatusReview.md`). | Fix the cycle: one candidate per cycle carrying all content fixes; offline gates; one powered paired run; one decision. Write the decision record before starting the next candidate. |
| **Headroom** | Failure-selected panel; defective and working twins | One-trial baselines. Repair prompts pass 131/161 unaided because they state the symptom. Four v2 pairs pass in both arms. | Re-measure the unaided baseline with 3 trials on the panel before reusing it. Retire prompts that pass 3/3 unaided into a regression-sentinel set. |
| **Oracle quality** | OS26 gates; v3 native contracts with alternatives and mutants | Gold-parity: 2/78 criteria have direct evidence. Two confirmed first-grade errors. Some criteria bundle 4–5 behaviors. | Qualify an oracle before its prompt joins a measured panel. Grade each component; give bundled requests a split (section 6). |
| **Grading** | Masking holds; grades frozen before arms are joined | Source review by one coordinator. No compile. No grader accuracy figure. Checkout-font was missed before. | Run the native lane on every answer with a matching contract (v3 already has four). Use the native results as labels to measure the source grader's TPR/TNR. |
| **Activation** | Traces now record reads per file | 19/54 sessions read nothing, and the description has no when-clause. Invocation is measured only after the fact. | Add a trigger eval (practice 2) as an offline-authored set, run under its own small approved quota. Report every outcome split by read and not read. |
| **Harness** | Ledger and policy-driven stops worked | Four sessions were lost to a read-only config directory. A runner fix mid-job (the "replacement-107" grant) was not escalated as a hold. | Add a pre-dispatch smoke run, with no model call, that starts the client in the sealed isolation and checks writable state. Make "isolation changed mid-job" a hold that needs an owner decision. |
| **Attribution** | Paired arms; exposure recorded | Headline counts include sessions that never read the skill. Regressions with no read (P-7d8c12fe, P-89b1442c) were attributed to the candidate. | Classify every transition by read status. A change with no read counts as variance, not as a content effect. |
| **Samples and power** | Sign test reported informally | One trial per cell; batch size set by quota. | Power rule: 56 items × 3 trials × 2 arms = 336 sessions. That detects about a 10-point paired improvement at the v2 discordance rate. v2 used 3% of the 5-hour and 1% of the weekly Gemini meter for 107 sessions. |
| **Transfer** | `reserve-transfer` items flagged in the 384 review | Never run. The panel is development-only. | Keep 20 or more transfer prompts from families not used in authoring. Promotion needs a paired gain there with no new critical flag. |
| **Skill packaging** | v2 and v3 are small, flat and script-built | 0.2.2 ships research material and a duplicate manifest folder, and `code-examples/` isn't connected to routing. | At the next promotion, ship only the entry, cards and tested excerpts. Keep ADRs and watchlists in the repo, not the skill. |
| **Records** | Prompt-record contract, private returns | Many parallel documents with conflicting statuses (`GoldPrompts.md` vs `evals/os26`, stale `VERSIONS.json`). | Keep one status table (STATUS.md) and a decision log; link everything else from them. |

## 4. Audit of the skill

### 4.1 Lineage

| Version | Entry | Description | Routing | Content |
|---|---|---|---|---|
| 0.2.2 (released) | 8.5 KB, 185 lines | About 800 characters; many keywords and APIs; claims visionOS | Prose plus optional JSON manifests; up to 3 files | 104 reference files (316 KB), including research documents and a duplicate manifests folder |
| 0.3.0-rc.1 | 3.5 KB | Use clause and do-not clause | Nine-row "Need → First note" table; read one note | 25 notes and 6 example cards |
| signal-v2 (measured) | 1.7 KB | One sentence, no when-clause | Six "for …" cues | Six cards, 0.4–1.1 KB each |
| signal-v3 (draft) | 1.8 KB | Adds "action callbacks in SwiftUI wrappers of native controls" | Actions cue names representables | Delta cards and tested excerpts for actions, media and return |

The entry's review rule and verification rule are sound. They produced the rework and verification gains when read, and they match practices 7 and 18. Shrinking the description saved 107 bytes of entry text but likely cost activation. Every installed answer still costs 2.4× tokens, whether or not the skill is read.

### 4.2 Trigger terms the evidence says are missing

These come from questions where the installed session read nothing (Tier 1 `routingChange` fields):
- **SwiftUI and AppKit mechanics:** UIViewRepresentable / coordinator / wrapper action; sheet / onDismiss / delayed dismissal; first responder / makeFirstResponder / window or inspector close.
- **Media:** captions picker / subtitles / AVPlayerItem selection / reload caption choices; described audio.
- **Forms:** text field / form validation / reply after editing.
- **State and controls:** accessibility custom action or shortcut after reconfiguration; selected trait vs collection selection; Reduce Motion; native Slider, Toggle and Picker reviews; adjustable action and chapters.

A description using these is still well under 1,024 characters. Measure it on a trigger set that also contains near misses, such as non-accessibility SwiftUI layout, AVFoundation playback without accessibility, or a generic UIKit crash.

### 4.3 What each card did when it was read (signal-v2, installed answers)

<!-- cards:begin -->
| Card read by the installed answer | Answers | Installed whole pass | Gains | Both fail | Critical flags |
|---|---:|---:|---:|---:|---:|
| nothing read | 19 | 1 | 0 | 18 | 2 |
| actions.md | 15 | 5 | 5 | 9 | 2 |
| facts.md | 8 | 5 | 4 | 3 | 0 |
| media.md | 8 | 1 | 1 | 7 | 0 |
| return.md | 5 | 2 | 2 | 3 | 3 |
| SKILL.md only | 3 | 1 | 0 | 2 | 0 |
| font.md | 1 | 1 | 0 | 0 | 0 |
<!-- cards:end -->

- **facts.md (4 gains from 8 reads):** single named facts work: the edit-category constant, AppKit rows, the tvOS 27 text boundary.
- **actions.md (5 gains from 15):** the leave-working-code path works. It still lacks:
  - AppKit custom-action ownership;
  - invocation-time enabled checks;
  - a rule against offering weaker alternatives;
  - the representable-hiding hazard;
  - chapter stepping.
- **media.md (1 gain from 8):** its rules are correct but not applied. It needs an ordered path, the constant, and a missing-item vs empty contrast.
- **return.md (2 gains, 3 critical flags from 5):** the rescue lines ("closing and completing dismissal are different events") work. The consume sentence and the missing capture-at-presentation rule coincide with all three critical flags.
- **validation.md:** never read.
- **font.md:** one read, a pass.

These are associations from first attempts on a selected panel. They indicate where to look, not causal per-rule effects.

**One of our own maintained examples contains the defect.** `SheetExample` in [Lifecycle.swift](../../../code-examples/swiftui/ios-v1/Sources/Lifecycle.swift) reads the view's mutable `ticket` inside `onDismiss` (line 36). That is the stale-callback shape behind the signal-v2 critical flags. Its helper tests call the ticket logic directly, so they cannot catch it. Fix or retire this example before any card links to it. Then add a native test that drives the installed dismissal closures: A arrives late, then B arrives twice. The v3 return excerpt comes from a new `Presentation.swift`, not from this file.

## 5. Recommended next development cycle

1. **Candidate.** Build from v3 and apply every Tier 1 and Tier 2 `skillChange` and `routingChange` marked P0 or P1:
   - **Description:** restore the description (section 4.2).
   - **return.md:**
     - remove the consume sentence;
     - add capture-at-presentation;
     - snapshot before the first suppression;
     - add the `makeFirstResponder` fallback.
   - **media.md:**
     - give the ordered selection path;
     - name `describesVideoForAccessibility`;
     - separate missing from empty;
     - make the picker setter request-scoped.
   - **actions.md:**
     - AppKit custom-action ownership;
     - invocation-time owner and enabled checks;
     - no weaker alternatives;
     - invoke handlers directly;
     - the representable-hiding hazard;
     - chapter stepping.
   - **facts.md:**
     - native Slider;
     - Reduce Motion;
     - selected trait vs collection selection;
     - record the SDK separately.
   - **validation.md:**
     - the field's own editing event;
     - end the busy state.
2. **Offline gates (no model):**
   - byte budget and link checks;
   - a native contract per changed card, run as positive, alternative and mutant (the v3 pattern in `signal-panel-v3/run.py`);
   - a recorded owner decision on each changed line;
   - a harness smoke run in the sealed isolation.
3. **Trigger set (authored offline, run only with approval):** 20 should-trigger prompts drawn from the section 4.2 terms, plus 20 near misses; 3 runs per description; a held-out split [5].
4. **Paired run (owner quota):** the 56-question panel with 3 trials per arm, plus at least 20 transfer prompts from Tier 3 `reserve-transfer` items and new families. Report:
   - results split by read and not read;
   - components;
   - twin both-correct rates;
   - new critical flags;
   - tokens.
5. **Grading:** native for every answer with a contract; masked source review for the rest; the source grader's TPR/TNR measured against native labels.
6. **Promotion rule:**
   - a paired gain on transfer prompts whose standard error excludes zero;
   - no new candidate-only critical flag;
   - sentinels preserved;
   - token cost reported against the gain.

## 6. Gold-prompt audit

**Gap types** (defined in [schema.md](schema.md)):
- `harmful-instruction`: the card was read and its wording plausibly caused the failure.
- `content-gap`: the card was read but lacks the contrast, fact or check.
- `not-opened`: the skill was never read.
- The rest describe the question, oracle, proof or evidence state.

<!-- gaps:begin -->
| Gap type | Tier 1 | Tier 2 | P0 |
|---|---:|---:|---:|
| `harmful-instruction` | 3 | 0 | 3 |
| `content-gap` | 9 | 1 | 3 |
| `not-opened` | 17 | 0 | 5 |
| `verification-gap` | 4 | 3 | 0 |
| `rework` | 4 | 2 | 0 |
| `question-defect` | 2 | 5 | 0 |
| `oracle-defect` | 1 | 2 | 0 |
| `variance` | 1 | 0 | 0 |
| `unmeasured` | 2 | 5 | 0 |
| `sound-control` | 13 | 9 | 0 |
<!-- gaps:end -->

### 6.1 P0 items

<!-- p0:begin -->
| Item | Cell | Family | Gap | Skill change |
|---|---|---|---|---|
| `P-d4bd274c3a345669` | iOS SwiftUI | write-actual-player-selection | content-gap | media.md: make the path concrete in one ordered line: current item, then the legible group from its asset, then item.select(option, in: group), then read the item's selection and publish that. Abstract wording was read and not applied. |
| `P-d82c5ccce8e33f3e` | macOS SwiftUI | native-editable-child | content-gap | actions.md: replace the general sentence with the specific hazard: 'Hiding or ignoring the representable (accessibilityHidden or children .ignore) removes the AppKit field too; remove the wrapper's own label instead.' |
| `P-dc1e54ce99c97729` | tvOS SwiftUI | write-actual-player-selection | content-gap | Same as P-d4bd274c: ordered concrete path plus the v3 check shape. |
| `P-34541ce79ee3d519` | iOS UIKit | restore-accessibility-background | harmful-instruction | return.md: add the decision-point contrast 'record the background value before the first suppression; never record an already suppressed view as its own restoration value; transfer or release A's record before B suppresses'. Add the check: A's late completion while B is open, then close B and assert the original value and one return request. |
| `P-90629dd9d60ff906` | iOS SwiftUI | restore-only-owned-sheet | harmful-instruction | return.md: remove 'consume a matching request before invoking reentrant code'. Replace with 'compare the token captured when this presentation opened; clear only your own record, and only if it still matches; look up the origin before clearing it.' v3 adds per-presentation onDismiss but keeps the old sentence. |
| `P-da7833399aac7f87` | macOS SwiftUI | restore-only-owned-sheet | harmful-instruction | Same as P-90629dd9: remove the consume sentence and add capture-at-presentation plus the A, B, B-again check. |
| `P-4099aaf89ec377cf` | tvOS UIKit | input-snapshot-after-edit | not-opened | validation.md: add 'Edits arrive through the text field's own editing event or delegate, not through your helper; tie cancellation to that event and drive it in the check by invoking the field's registered editing action.' |
| `P-48400f490808a2cf` | macOS SwiftUI | restore-only-owned-sheet | not-opened | return.md (via routing): the per-presentation onDismiss rule. The no-argument closure must already know its presentation; calling finish with the active ticket gives a late callback the replacement's identity. |
| `P-6bfef2bcad970d58` | macOS AppKit | origin-window-membership | not-opened | return.md: name the API: 'makeFirstResponder returns false when the view refuses; on false, request the declared fallback in the same window.' |
| `P-be25d510c5ffe50f` | macOS AppKit | refusing-focus-target | not-opened | return.md: the makeFirstResponder Bool rule from P-6bfef2bc, plus its check: a refusing primary gets the fallback once. |
| `P-db6ab4c551e67aca` | iOS UIKit | validation-busy-recovery | not-opened | validation.md: the field-event rule from P-4099aaf8, plus 'after retiring the request, end busy state so the current entry can be submitted'. |
<!-- p0:end -->

### 6.2 Tier 1: the 56 signal-panel questions

Grouped by decision family. Grades are signal-v2 source grades, listed in the order primary, preservation, verification, integration, rework, whole. ✓ pass, ✗ fail, – not applicable, ⚠ critical.

**Overall:**
- 9 rescues;
- 4 both pass;
- 40 both fail;
- 3 unpaired: two pairs were rejected at harness startup, and one unaided session was interrupted.

<!-- tier1:begin -->
#### chapter-boundary

**`P-f93bec690ad5409c`** · iOS SwiftUI · chapter-boundary · axis primary · whole **both-fail**, primary both-fail · read: SKILL.md, actions.md · **P1 content-gap** · v3 no.

> iOS, SwiftUI. Our episode has chapters starting at 0, 35 and 107 seconds and ends at 160. When positioned at a chapter start, an accessibility adjustment should move by one chapter, staying at a boundary when there is no

- **Grades** (primary, preservation, verification, integration, rework, whole; ⚠ critical): unaided ✗ ✓ – ✗ ✓ ✗ · installed ✗ ✓ – ✗ ✓ ✗
- **Diagnosis:** v2: both fail; installed read actions.md, which has no chapter guidance, and still treated the episode end as a chapter and seeked by a fixed interval with no chapters.
- **Question:** none
- **Oracle:** Assert chapter positions from 35 (forward 107, backward 0), no movement past 0 or 107, defined empty behavior and preserved Play.
- **Skill:** actions.md or a new adjustable note: 'An adjustable step moves between listed chapter starts; the media end is not a chapter; with no chapters, do nothing rather than seek by time.'
- **Routing:** Add 'accessibility adjustable action, chapters, increment and decrement' to the actions cue.

#### clear-optional-help

**`P-7d27aad438a1d70b`** · macOS SwiftUI · clear-optional-help · axis preservation · whole **gain**, primary both-pass · read: SKILL.md, actions.md, facts.md · **P3 sound-control** · v3 n/a.

> macOS 26.0, SwiftUI. Configure the same view with help text, then with none. What help is exposed after each update? Explain your conclusion and give a focused check. Include integrated Swift changes if the requested beh

- **Grades** (primary, preservation, verification, integration, rework, whole; ⚠ critical): unaided ✓ ✓ ✓ ✓ ✗ ✗ · installed ✓ ✓ ✓ ✓ ✓ ✓
- **Diagnosis:** v2 rescue: installed read actions.md and facts.md, traced nil on the second update, inspected the same native button twice. Unaided added tooltip behavior and overclaimed spoken output.
- **Question:** none
- **Oracle:** Assert accessibilityHelp() is nil, not empty, after the second configuration.
- **Skill:** none
- **Routing:** none

#### dismissal-completion

**`P-d2dd979143402b3b`** · iOS UIKit · dismissal-completion · axis primary · whole **gain**, primary both-pass · read: SKILL.md, return.md · **P3 sound-control** · v3 n/a.

> iOS 26.0, UIKit. Close a panel, then finish or cancel dismissal. At which points does this implementation request focus? Review the supplied implementation against that requirement. If it already works, say why and leave

- **Grades** (primary, preservation, verification, integration, rework, whole; ⚠ critical): unaided ✓ ✓ ✗ ✓ ✓ ✗ · installed ✓ ✓ ✓ ✓ ✓ ✓
- **Diagnosis:** v2 rescue: installed read return.md, removed only the early post, and checked start, cancellation, stale and valid completion with notification count and argument.
- **Question:** none
- **Oracle:** Keep the cancelled-dismissal case asserting no post.
- **Skill:** none; 'closing and completing dismissal are different events' is working content. Keep it when rewriting return.md.
- **Routing:** none

#### dispatch-current-and-retired

**`P-51e9f52794c2efdf`** · iOS UIKit · dispatch-current-and-retired · axis sentinel · whole **both-fail**, primary both-pass · read: nothing read · **P1 not-opened** · v3 partial.

> iOS 26.0, UIKit. After the same view is reconfigured, what happens if a client retains and invokes the old accessibility shortcut? The ordinary buttons should operate on the currently displayed item. Explain your conclus

- **Grades** (primary, preservation, verification, integration, rework, whole; ⚠ critical): unaided ✓ ✓ ✗ ✓ ✓ ✗ · installed ✓ ✓ ✗ ✓ ✓ ✗
- **Diagnosis:** v2: primary passes in both (the guard is right), verification fails in both; installed read nothing. Neither test drives the real handler for both ordinary buttons and the current shortcut.
- **Question:** none
- **Oracle:** Keep call-count and ID assertions; require the retained installed action and presses on both real buttons, with no conditional skip.
- **Skill:** actions.md check shape: after reconfiguring the same view, invoke the retained old action, the current action, and every ordinary control, and count deliveries per item.
- **Routing:** Add 'accessibility custom action / shortcut after reconfiguration' to the actions cue; 'reconfiguration' alone did not trigger here.

**`P-89b1442c72a8db4b`** · iOS UIKit · dispatch-current-and-retired · axis verification · whole **both-fail**, primary both-pass · read: nothing read · **P2 not-opened** · v3 partial.

> iOS 26.0, UIKit. After the same view is reconfigured, what happens if a client retains and invokes the old accessibility shortcut? The ordinary buttons should operate on the currently displayed item. Explain your conclus

- **Grades** (primary, preservation, verification, integration, rework, whole; ⚠ critical): unaided ✓ ✓ ✗ ✓ ✓ ✗ · installed ✓ ✓ ✗ ✓ ✗ ✗
- **Diagnosis:** v2: primary passes in both; the installed session read nothing, omitted the ordinary Delete button in its check and lost rework by suggesting a focus notification on refresh. The rework loss is variance, not content.
- **Question:** none
- **Oracle:** Evidence requires invoking the actual installed shortcut and pressing every real button, with no conditional skip.
- **Skill:** Same check shape as P-51e9f527.
- **Routing:** Same as P-51e9f527.

#### duplicate-dispatch-on-reuse

**`P-1079cff7faaab5b2`** · iOS UIKit · duplicate-dispatch-on-reuse · axis primary · whole **unpaired**, primary unpaired · read: SKILL.md, actions.md · **P2 question-defect** · v3 n/a.

> I'm building reusable UIKit cards for invoices, supporting iOS 26 and later. Each card shows a decorative star, an invoice title, and separate Open and Save buttons. Every card has the same visible button titles. The sam

- **Grades** (primary, preservation, verification, integration, rework, whole; ⚠ critical): unaided unavailable · installed ✓ ✗ ✓ ✗ ✓ ✗ ⚠
- **Diagnosis:** v2: unaided interrupted, installed read actions.md and met primary, verification and rework but failed integration as critical: the buttons were never added to the card. The request says 'not layout', which invites omitting the hierarchy.
- **Question:** Keep the layout exemption but say the controls must be hosted in the card, so an unattached control is clearly incomplete rather than an exempted layout detail.
- **Proposed wording:** I'm building reusable UIKit cards for invoices, supporting iOS 26 and later. Each card shows a decorative star, an invoice title, and separate Open and Save buttons hosted in the card. Every card has the same visible button titles. The same card instance can be configured for another invoice without being removed. Show the Swift configuration and unit tests so someone can tell which invoice each button acts on, while both buttons still work normally. Callers supply localized strings and the two operation handlers. Visual layout and styling are out of scope.
- **Oracle:** Split integration (controls are in the card's hierarchy) from primary (single dispatch to the current invoice after rebinding); report critical only for an unreachable ordinary control.
- **Skill:** none beyond the entry rule 'follow it through the existing control'; rerun the pair before attributing.
- **Routing:** none

#### duplicate-ordinary-command

**`P-777d08cb675db900`** · macOS AppKit · duplicate-ordinary-command · axis rework · whole **both-fail**, primary both-pass · read: SKILL.md, actions.md · **P1 verification-gap** · v3 partial.

> macOS 26.0, AppKit. Which item do the ordinary controls and the supplementary shortcut operate on after this view refreshes? Explain your conclusion and give a focused check. Include integrated Swift changes if the reque

- **Grades** (primary, preservation, verification, integration, rework, whole; ⚠ critical): unaided ✓ ✓ ✓ ✓ ✗ ✗ · installed ✓ ✓ ✗ ✓ ✓ ✗
- **Diagnosis:** v2: installed read actions.md, gained rework (dropped unconditional announcements and role changes) but lost verification: its test tries to press the custom-action object through an unsupported method instead of calling its handler.
- **Question:** none
- **Oracle:** Keep: the test must perform the native button's action and invoke the custom action's handler.
- **Skill:** actions.md: 'Invoke a custom action by calling its handler (UIKit actionHandler, AppKit handler) and press ordinary controls through their own action; do not invent a perform method.'
- **Routing:** none

#### edit-category

**`P-9ae50d3a7e4bb9e8`** · iOS UIKit · edit-category · axis primary · whole **gain**, primary gain · read: SKILL.md, facts.md · **P3 sound-control** · v3 n/a.

> iOS 26.0, UIKit. For an editor with optional edit-action grouping, how are the actions categorized with the option on and off? Review the supplied implementation against that requirement. If it already works, say why and

- **Grades** (primary, preservation, verification, integration, rework, whole; ⚠ critical): unaided ✗ ✓ ✗ ✗ ✓ ✗ · installed ✓ ✓ ✓ ✓ ✓ ✓
- **Diagnosis:** v2 rescue: installed read facts.md and used the SDK editCategory constant while preserving the uncategorized default; unaided used an unsupported member.
- **Question:** none
- **Oracle:** Keep the compile-level assertion on the SDK constant and the ordinary action's nil category.
- **Skill:** none; this is the clearest single-fact win and justifies the facts card.
- **Routing:** none

#### input-snapshot-after-edit

**`P-4099aaf89ec377cf`** · tvOS UIKit · input-snapshot-after-edit · axis primary · whole **both-fail**, primary both-fail · read: nothing read · **P0 not-opened** · v3 no.

> tvOS 26.0, UIKit. Start validation, change the text, then deliver the original reply. Which text and result does this form show? Review the supplied implementation against that requirement. If it already works, say why a

- **Grades** (primary, preservation, verification, integration, rework, whole; ⚠ critical): unaided ✗ ✓ ✗ ✗ ✓ ✗ · installed ✗ ✓ ✗ ✗ ✓ ✗
- **Diagnosis:** v2: both fail primary; installed read nothing. Both tests cancel through the helper rather than through the field, so the ordinary edit path that leaves the old reply active is never exercised.
- **Question:** none
- **Oracle:** Keep: change the field's text without calling the helper, deliver the old reply, assert the edited text remains and no stale errors apply.
- **Skill:** validation.md: add 'Edits arrive through the text field's own editing event or delegate, not through your helper; tie cancellation to that event and drive it in the check by invoking the field's registered editing action.'
- **Routing:** Add 'text field, form validation, reply after editing' to the description; validation.md was never opened in 54 sessions.

#### inspect-without-selection-write

**`P-b12c69f62639d32d`** · iOS SwiftUI · inspect-without-selection-write · axis primary · whole **gain**, primary gain · read: SKILL.md, media.md · **P3 sound-control** · v3 n/a. Also gold-parity: `ios-swiftui-media`.

> I am using SwiftUI on iOS 26 deployment target; available validation anchor iOS 26.5. A video card can show whether audio description is available. Loading track information may succeed with no match, fail, or still be i

- **Grades** (primary, preservation, verification, integration, rework, whole; ⚠ critical): unaided ✗ ✗ ✗ ✗ ✗ ✗ · installed ✓ ✓ ✓ ✓ ✓ ✓
- **Diagnosis:** v2 rescue on the primary behavior: installed read media.md and kept inspection read-only with item identity and cancellation; unaided wrote preferences back into the player.
- **Question:** none
- **Oracle:** Any write to the player item during inspection is a regression; keep it a separate component.
- **Skill:** none; 'inspection is read-only' is a decision-point contrast that works.
- **Routing:** none

#### media-off-write

**`P-6d2dd61c5ac4abfc`** · iOS SwiftUI · media-off-write · axis primary · whole **both-fail**, primary both-fail · read: SKILL.md, media.md · **P1 content-gap** · v3 partial.

> iOS developer question My SwiftUI video screen only changes a local selected value when someone chooses captions. Connect the choices to the real media item without resetting audio or playback settings. Offer complete ca

- **Grades** (primary, preservation, verification, integration, rework, whole; ⚠ critical): unaided ✗ ✓ ✗ ✗ ✓ ✗ · installed ✗ ✓ ✗ ✗ ✓ ✗
- **Diagnosis:** v2: installed read media.md and with a valid group did the right thing, but without an item or group it still reported a local write as the selection, and tests used local IDs with nil native options.
- **Question:** none
- **Oracle:** Grade full-only offering, item selection, Off through the supported call, preserved audio and out-of-list choice separately.
- **Skill:** media.md: 'If there is no current item or group, report the choice as not applied; publish only the selection read back from the item.'
- **Routing:** none

#### missing-item-vs-no-options

**`P-4ec92962591872fa`** · iOS SwiftUI · missing-item-vs-no-options · axis primary · whole **both-fail**, primary both-fail · read: SKILL.md, media.md · **P1 content-gap** · v3 no.

> iOS developer question Build a SwiftUI media-option picker using the same player as the video view. It should show the real selection, distinguish loading, absent options and failure, and allow retry. Keep normal player 

- **Grades** (primary, preservation, verification, integration, rework, whole; ⚠ critical): unaided ✗ ✓ ✗ ✗ ✓ ✗ · installed ✗ ✓ ✗ ✗ ✓ ✗
- **Diagnosis:** v2: both fail primary; installed read media.md and still reports a missing item the same as an inspected group with no options, and its test asserts that conflation.
- **Question:** none
- **Oracle:** Grade missing item, loading, empty, failure and retry separately, and the real selection read from the player item.
- **Skill:** media.md: add the contrast 'No current item is unavailable, not empty: report it distinctly and retry when an item arrives; empty means a loaded group with no offered options.'
- **Routing:** none

#### name-without-focus-reset

**`P-a5c8091cdffa651a`** · iOS UIKit · name-without-focus-reset · axis rework · whole **gain**, primary gain · read: SKILL.md, actions.md, return.md · **P3 sound-control** · v3 n/a.

> iOS 26.0, UIKit. The same visible cell changes from a priority order to an ordinary order without dequeuing. Both need their current customer name and current order status. Can you check those updates without moving focu

- **Grades** (primary, preservation, verification, integration, rework, whole; ⚠ critical): unaided ✗ ✓ ✗ ✗ ✗ ✗ · installed ✓ ✓ ✓ ✓ ✓ ✓
- **Diagnosis:** v2 rescue: installed read actions.md and return.md, checked distinct names and statuses on the same live cell, and requested no focus move; unaided recommended an unsupported notification.
- **Question:** none
- **Oracle:** none
- **Skill:** none; the return card's 'preserve correct native behavior rather than posting an additional notification' worked here.
- **Routing:** none

#### native-custom-action-api

**`P-3f811eea610d0c32`** · macOS AppKit · native-custom-action-api · axis primary · whole **both-fail**, primary both-fail · read: SKILL.md, actions.md · **P1 content-gap** · v3 no.

> Our AppKit invoice list reuses an NSStackView row containing a title, Open button and Save button. Implement a programmatic row that can be configured repeatedly with a new title, complete localized control names and cal

- **Grades** (primary, preservation, verification, integration, rework, whole; ⚠ critical): unaided ✗ ✓ ✗ ✗ ✓ ✗ · installed ✗ ✓ ✗ ✗ ✓ ✗
- **Diagnosis:** v2: both fail primary; installed read actions.md, yet its retained Save action still targets the row's mutable current callback and the proposed test accepts saving B from A's action.
- **Question:** none
- **Oracle:** Keep: Open's custom actions include named Save that dispatches the current Save, returns false when disabled, and a retained action from A does nothing after rebinding to B.
- **Skill:** actions.md: add the AppKit form of the ownership rule: an NSAccessibilityCustomAction handler records the invoice it was installed for and compares it with the row's current invoice when invoked; reading the current callback cannot detect staleness.
- **Routing:** none

#### native-editable-child

**`P-d82c5ccce8e33f3e`** · macOS SwiftUI · native-editable-child · axis preservation · whole **both-fail**, primary both-fail · read: SKILL.md, actions.md · **P0 content-gap** · v3 no.

> macOS, SwiftUI. The sidebar hosts an AppKit search field in SwiftUI. Both the wrapper and the editable field announce Search and people encounter two stops. The AppKit field handles selection and insertion. What would yo

- **Grades** (primary, preservation, verification, integration, rework, whole; ⚠ critical): unaided ✗ ✗ – ✗ ✗ ✗ ⚠ · installed ✗ ✗ – ✗ ✗ ✗ ⚠
- **Diagnosis:** v2: critical in both; installed read actions.md, which says not to suppress the native editable field, yet still recommended a modifier that hides the represented subtree including the search field.
- **Question:** none
- **Oracle:** State that any fix hiding the hosted NSSearchField fails the single-editable-owner check even if one stop remains.
- **Skill:** actions.md: replace the general sentence with the specific hazard: 'Hiding or ignoring the representable (accessibilityHidden or children .ignore) removes the AppKit field too; remove the wrapper's own label instead.'
- **Routing:** none

#### ordinary-action-survives

**`P-4328fa34debd8d92`** · tvOS UIKit · ordinary-action-survives · axis preservation · whole **gain**, primary both-pass · read: SKILL.md, actions.md · **P3 sound-control** · v3 n/a.

> tvOS 26.0, UIKit. Which item do the ordinary controls and the supplementary shortcut operate on after this view refreshes? Explain your conclusion and give a focused check. Include integrated Swift changes if the request

- **Grades** (primary, preservation, verification, integration, rework, whole; ⚠ critical): unaided ✓ ✓ ✗ ✓ ✗ ✗ · installed ✓ ✓ ✓ ✓ ✓ ✓
- **Diagnosis:** v2 rescue: installed read actions.md, traced both ordinary buttons and the retained shortcut, tested installed actions and left working code unchanged; unaided added traversal ordering and rewrote handlers.
- **Question:** none
- **Oracle:** none
- **Skill:** none; keep the entry's review rule and the actions card as they are for this path.
- **Routing:** none

#### origin-window-membership

**`P-6bfef2bcad970d58`** · macOS AppKit · origin-window-membership · axis primary · whole **both-fail**, primary both-fail · read: nothing read · **P0 not-opened** · v3 no.

> macOS, AppKit. Two document windows can each open their own inspector. Closing the inspector in one window sometimes sends keyboard input to the other document. How would you structure ownership of the return destination

- **Grades** (primary, preservation, verification, integration, rework, whole; ⚠ critical): unaided ✗ ✗ – ✗ ✓ ✗ · installed ✗ ✓ – ✗ ✓ ✗
- **Diagnosis:** v2: installed read nothing; it checked window membership but ignored a same-window view refusing first responder and never tried the fallback. Unaided reused a detached responder.
- **Question:** none
- **Oracle:** List same-window membership, eligibility, refusal handling and current-presentation ownership as separate checks.
- **Skill:** return.md: name the API: 'makeFirstResponder returns false when the view refuses; on false, request the declared fallback in the same window.'
- **Routing:** Add 'first responder, keyboard focus, inspector or window close' to the description and return cue.

#### positive-media-choice

**`P-7cc5d89371a12a35`** · tvOS UIKit · positive-media-choice · axis verification · whole **both-fail**, primary both-fail · read: SKILL.md, media.md · **P1 content-gap** · v3 no.

> I'm reviewing a UIKit change for tvOS 26.0. When someone asks for described audio and no matching track exists, keep the previous choice. Does the picker do that? Review the supplied implementation against that requireme

- **Grades** (primary, preservation, verification, integration, rework, whole; ⚠ critical): unaided ✗ ✓ ✗ ✗ ✓ ✗ · installed ✗ ✓ ✗ ✗ ✓ ✗
- **Diagnosis:** v2: both fail; installed read media.md and fixed the right defect, but used the wrong media characteristic constant and stubbed framework groups in the test.
- **Question:** none
- **Oracle:** Require a fixture with an audible group and a known current option; a test that can return before selection fails evidence.
- **Skill:** media.md: name the constant: described audio is AVMediaCharacteristic.describesVideoForAccessibility. The card says 'by its media characteristic' without naming it.
- **Routing:** none

#### preserve-native-slider

**`P-35ee522327907bd8`** · iOS SwiftUI · preserve-native-slider · axis rework · whole **both-fail**, primary both-fail · read: SKILL.md, actions.md, facts.md · **P1 rework** · v3 no. Also OS26: `GP26-11`.

> iOS 26.0, SwiftUI. Review this volume setting for a concrete accessibility problem. Its parent owns a persisted volume value in 0…100 and supplies a working two-way binding. Keep that binding, the allowed range and one-p

- **Grades** (primary, preservation, verification, integration, rework, whole; ⚠ critical): unaided ✗ ✓ – ✓ ✗ ✗ · installed ✗ ✓ – ✓ ✗ ✗
- **Diagnosis:** v2: both arms invent an adjustment defect in a working labeled native Slider; installed read actions.md and facts.md and duplicated native behavior anyway.
- **Question:** none
- **Oracle:** Grade preserved binding, range and step separately from the unsupported defect claim; the redundant adjustable wrapper is rework, not a correctness failure.
- **Skill:** facts.md: add 'A SwiftUI Slider with a label already exposes an adjustable value with its range and step; a review leaves it alone unless the spoken value is wrong for the product.' The entry's leave-it-in-place sentence alone did not prevent the rewrite.
- **Routing:** none

**`P-e505d95d8bc6f761`** · iOS SwiftUI · preserve-native-slider · axis rework · whole **both-fail**, primary both-fail · read: SKILL.md, actions.md · **P1 rework** · v3 no.

> iOS 26.0, SwiftUI. Our release checklist has an accessibility pass for every settings screen, and the Listening screen is next. Can you go over the volume slider for VoiceOver and make whatever changes it needs? It saves

- **Grades** (primary, preservation, verification, integration, rework, whole; ⚠ critical): unaided ✗ ✗ – ✓ ✗ ✗ · installed ✗ ✓ – ✓ ✗ ✗
- **Diagnosis:** v2: both fail on rework; installed read actions.md and still added redundant adjustable behavior and hid elements around a working native slider.
- **Question:** none
- **Oracle:** Run the native test and accept the alternative-matching value; grade binding, range, step and readout preservation separately from added wrappers.
- **Skill:** Same facts.md native Slider line as P-35ee5223; also route preservation reviews to facts, not actions.
- **Routing:** Facts cue: add 'native Slider, Toggle, Picker already accessible'.

#### progress-after-terminal

**`P-debf8047cd9f4e4a`** · iOS UIKit · progress-after-terminal · axis primary · whole **both-pass**, primary both-pass · read: SKILL.md · **P3 sound-control** · v3 n/a. Also OS26: `GP26-10`.

> iOS 26.0, UIKit. The main-thread download callback reports integer percentages (display clamped to 0…100) and may repeat its terminal event. Only one download is active; `begin(id:)` starts a fresh unique ID. Late callba

- **Grades** (primary, preservation, verification, integration, rework, whole; ⚠ critical): unaided ✓ ✓ – ✓ ✓ ✓ · installed ✓ ✓ – ✓ ✓ ✓
- **Diagnosis:** v2: both pass; installed read SKILL.md only. No headroom on Flash Low.
- **Question:** none
- **Oracle:** none
- **Skill:** none
- **Routing:** none

#### reduced-motion-scope

**`P-a32f106f0aa1cc85`** · iOS SwiftUI · reduced-motion-scope · axis rework · whole **both-fail**, primary both-fail · read: SKILL.md · **P2 rework** · v3 no. Also OS26: `GP26-12`.

> iOS 26.0, SwiftUI. Review this three-page view for a concrete accessibility problem. The user can change Reduce Motion while it is open; the next page change should follow the current preference without resetting the sel

- **Grades** (primary, preservation, verification, integration, rework, whole; ⚠ critical): unaided ✗ ✓ – ✓ ✗ ✗ · installed ✗ ✓ – ✓ ✗ ✗
- **Diagnosis:** v2: both diagnose a defect in a working reduced-motion path; installed read SKILL.md only and added a transition branch anyway.
- **Question:** none
- **Oracle:** Grade preserved page behavior, motion under the current preference, the unsupported claim, and inert rework separately.
- **Skill:** facts.md: 'A live accessibilityReduceMotion environment read with a nil animation already suppresses the movement; do not add a parallel transition branch.' No current card covers motion.
- **Routing:** Add 'Reduce Motion' to the facts cue.

#### refusing-focus-target

**`P-be25d510c5ffe50f`** · macOS AppKit · refusing-focus-target · axis primary · whole **both-fail**, primary both-fail · read: nothing read · **P0 not-opened** · v3 no.

> I'm reviewing a AppKit change for macOS 26.0. After a refresh the original focus target may no longer belong here. Can you restore only to a usable target or fallback? Review the supplied implementation against that requ

- **Grades** (primary, preservation, verification, integration, rework, whole; ⚠ critical): unaided ✗ ✗ ✗ ✗ ✓ ✗ ⚠ · installed ✗ ✗ ✗ ✗ ✓ ✗ ⚠
- **Diagnosis:** v2: both critical; installed read nothing. Both ignore that an attached, visible, enabled view can refuse first responder and never request the fallback.
- **Question:** none
- **Oracle:** Fixture: original attached, visible, enabled but refusing; assert one request goes to the eligible fallback. A removed-original test does not count.
- **Skill:** return.md: the makeFirstResponder Bool rule from P-6bfef2bc, plus its check: a refusing primary gets the fallback once.
- **Routing:** Same AppKit focus trigger terms as P-6bfef2bc.

#### restore-accessibility-background

**`P-34541ce79ee3d519`** · iOS UIKit · restore-accessibility-background · axis primary · whole **both-fail**, primary both-fail · read: SKILL.md, return.md · **P0 harmful-instruction** · v3 yes.

> Our UIKit app has a custom panel with a heading, Apply and Cancel buttons. Cancel animates the panel away asynchronously. Sometimes closing it leaves the background unavailable, or a late callback from an earlier opening

- **Grades** (primary, preservation, verification, integration, rework, whole; ⚠ critical): unaided ✗ ✗ ✗ ✗ ✗ ✗ · installed ✗ ✗ ✗ ✗ ✓ ✗ ⚠
- **Diagnosis:** v2: installed read return.md and gained rework but introduced a candidate-only critical: reopening snapshots the already-suppressed background, so final dismissal leaves navigation hidden. The card's 'consume a matching request' and generic ownership wording does not address the snapshot value itself.
- **Question:** none
- **Oracle:** Separate background restoration (original value, including initially hidden), stale-callback rejection, return target with fallback, escape and teardown; critical when the final background stays hidden.
- **Skill:** return.md: add the decision-point contrast 'record the background value before the first suppression; never record an already suppressed view as its own restoration value; transfer or release A's record before B suppresses'. Add the check: A's late completion while B is open, then close B and assert the original value and one return request.
- **Routing:** none

#### restore-only-owned-sheet

**`P-48400f490808a2cf`** · macOS SwiftUI · restore-only-owned-sheet · axis sentinel · whole **both-fail**, primary both-fail · read: nothing read · **P0 not-opened** · v3 partial.

> macOS 26.0, SwiftUI. Sheet A starts closing, then this view presents B. A delayed dismissal from A arrives. Can it change focus or close B? Explain your conclusion and give a focused check. Include integrated Swift chang

- **Grades** (primary, preservation, verification, integration, rework, whole; ⚠ critical): unaided ✗ ✗ ✗ ✗ ✓ ✗ ⚠ · installed ✗ ✗ ✗ ✗ ✓ ✗ ⚠
- **Diagnosis:** v2: both critical; installed read nothing. Both views read the shared mutable ticket in the dismissal callback, and both tests pass A's ticket directly, bypassing the defect.
- **Question:** none
- **Oracle:** Use the factorial criterion: drive A's retained dismissal closure from the view after B opens; a model-only test with the old ticket supplied by hand is insufficient evidence.
- **Skill:** return.md (via routing): the per-presentation onDismiss rule. The no-argument closure must already know its presentation; calling finish with the active ticket gives a late callback the replacement's identity.
- **Routing:** Add 'sheet, onDismiss, delayed dismissal' to the description and return cue.

**`P-90629dd9d60ff906`** · iOS SwiftUI · restore-only-owned-sheet · axis primary · whole **both-fail**, primary both-fail · read: SKILL.md, return.md · **P0 harmful-instruction** · v3 partial.

> Target iOS26, SwiftUI. Our SwiftUI details sheet needs a clear entry target and a return target after dismissal. Keep the ordinary Open and Close controls. The originating item may disappear while the sheet is open; use 

- **Grades** (primary, preservation, verification, integration, rework, whole; ⚠ critical): unaided ✗ ✗ ✗ ✗ ✓ ✗ · installed ✗ ✗ ✗ ✗ ✓ ✗ ⚠
- **Diagnosis:** v2: installed read return.md and produced a candidate-only critical: the delayed onDismiss reads the active generation and clears the presented item before looking up the origin. The card's 'consume a matching request before invoking reentrant code' plausibly led to clearing shared state first.
- **Question:** none
- **Oracle:** Grade completion ownership (duplicate and stale ignored), eligible target at completion, fallback and reentrant open separately; drive the view's own dismissal closure.
- **Skill:** return.md: remove 'consume a matching request before invoking reentrant code'. Replace with 'compare the token captured when this presentation opened; clear only your own record, and only if it still matches; look up the origin before clearing it.' v3 adds per-presentation onDismiss but keeps the old sentence.
- **Routing:** none

**`P-da7833399aac7f87`** · macOS SwiftUI · restore-only-owned-sheet · axis primary · whole **both-fail**, primary both-fail · read: SKILL.md, return.md · **P0 harmful-instruction** · v3 partial.

> macOS 26.0, SwiftUI. Sheet A starts closing, then this view presents B. A delayed dismissal from A arrives. Can it change focus or close B? Explain your conclusion and give a focused check. Include integrated Swift chang

- **Grades** (primary, preservation, verification, integration, rework, whole; ⚠ critical): unaided ✗ ✗ ✗ ✗ ✓ ✗ ⚠ · installed ✗ ✗ ✗ ✗ ✓ ✗ ⚠
- **Diagnosis:** v2: critical in both; installed read return.md, treated a mutable ticket as captured per sheet and cleared it in the stale callback, consistent with the 'consume' wording.
- **Question:** none
- **Oracle:** Exercise a retained A dismissal from the view wiring after B opens: A cannot close B, alter focus or request restoration; a valid B completion restores once.
- **Skill:** Same as P-90629dd9: remove the consume sentence and add capture-at-presentation plus the A, B, B-again check.
- **Routing:** none

#### retained-native-target

**`P-7622f1aa06d7a35b`** · iOS SwiftUI · retained-native-target · axis sentinel · whole **both-fail**, primary both-pass · read: nothing read · **P1 not-opened** · v3 yes.

> iOS 26.0, SwiftUI. After this wrapper updates its native control, which target receives its next action? What happens after teardown? Explain your conclusion and give a focused check. Include integrated Swift changes if 

- **Grades** (primary, preservation, verification, integration, rework, whole; ⚠ critical): unaided ✓ ✓ ✗ ✓ ✓ ✗ · installed ✓ ✓ ✗ ✓ ✓ ✗
- **Diagnosis:** v2: primary passes in both, verification fails in both; installed read nothing. Tests configure one button and one handler, so they cannot show an update from A to B.
- **Question:** none
- **Oracle:** Keep stale, current and dismantled cases; drive the installed native action, not a parallel closure.
- **Skill:** actions.md check shape for representables: retain the native control's action, update to B, invoke the retained action, then dispatch current controls; dismantle and invoke again.
- **Routing:** Covered by the v3 description addition 'action callbacks in SwiftUI wrappers of native controls'; also add 'UIViewRepresentable, coordinator'.

**`P-7766a23217bfa0c3`** · tvOS SwiftUI · retained-native-target · axis rework · whole **both-fail**, primary gain · read: nothing read · **P2 not-opened** · v3 yes.

> tvOS 26.0, SwiftUI. After this wrapper updates its native control, which target receives its next action? What happens after teardown? Explain your conclusion and give a focused check. Include integrated Swift changes if

- **Grades** (primary, preservation, verification, integration, rework, whole; ⚠ critical): unaided ✗ ✗ ✗ ✗ ✗ ✗ · installed ✓ ✓ ✓ ✓ ✗ ✗
- **Diagnosis:** v2: installed gained primary and verification without reading the skill but added unrequested button styling (rework), as did the read-nothing twin P-a00ec36c. Gains here are not attributable to content.
- **Question:** none
- **Oracle:** Separate primary, rework (styling or cross-platform edits) and evidence (a negative-only test that passes the original).
- **Skill:** Entry rule already says leave working code; the session never saw it. Fix routing first.
- **Routing:** Same as P-7622f1aa: representable wrapper and coordinator trigger terms.

**`P-7d8c12fe30bd49a4`** · iOS SwiftUI · retained-native-target · axis rework · whole **both-fail**, primary loss · read: nothing read · **P1 variance** · v3 yes.

> iOS 26.0, SwiftUI. After this wrapper updates its native control, which target receives its next action? What happens after teardown? Explain your conclusion and give a focused check. Include integrated Swift changes if 

- **Grades** (primary, preservation, verification, integration, rework, whole; ⚠ critical): unaided ✓ ✓ ✗ ✓ ✗ ✗ · installed ✗ ✗ ✗ ✗ ✗ ✗
- **Diagnosis:** v2: the only primary regression (also preservation and integration), but the installed session read nothing: its event-time activate mints a fresh ticket for a retained old action. Not attributable to card content.
- **Question:** none
- **Oracle:** Grade primary, teardown regression risk, rework and evidence separately; require a positive current-dispatch assertion before asserting the old one is silent.
- **Skill:** actions.md (already in v3 actions-delta): an installed closure that asks the coordinator to mint a ticket at event time lets an old registration operate on B.
- **Routing:** Representable and coordinator trigger terms, as for P-7622f1aa.

**`P-a00ec36c978640fc`** · tvOS SwiftUI · retained-native-target · axis sentinel · whole **both-fail**, primary gain · read: nothing read · **P2 not-opened** · v3 yes.

> tvOS 26.0, SwiftUI. After this wrapper updates its native control, which target receives its next action? What happens after teardown? Explain your conclusion and give a focused check. Include integrated Swift changes if

- **Grades** (primary, preservation, verification, integration, rework, whole; ⚠ critical): unaided ✗ ✗ ✗ ✗ ✗ ✗ · installed ✓ ✓ ✗ ✓ ✗ ✗
- **Diagnosis:** v2: installed gained primary without reading the skill, then changed visible button style; tests never reconfigure to a new handler.
- **Question:** none
- **Oracle:** Grade the causal explanation, current dispatch and post-dismantle silence with the same criterion on both twins.
- **Skill:** Same as P-7622f1aa.
- **Routing:** Same as P-7622f1aa.

#### retired-outline-handle

**`P-dd7ee77a4e81a08e`** · macOS AppKit · retired-outline-handle · axis primary · whole **both-fail**, primary both-pass · read: SKILL.md · **P2 question-defect** · v3 no.

> We use a programmatic AppKit NSOutlineView for a nested library. Entries have stable IDs, titles and child arrays. Show Name and Kind columns. Updates can rename, reorder or remove entries; keep surviving item identity, 

- **Grades** (primary, preservation, verification, integration, rework, whole; ⚠ critical): unaided ✓ ✗ ✗ ✗ ✓ ✗ · installed ✓ ✗ ✗ ✗ ✓ ✗
- **Diagnosis:** v2: primary passes in both (installed read SKILL.md only), whole fails on missing expansion and selection restoration. The request bundles identity, duplicate rejection, expansion and selection into one verdict.
- **Question:** Split into two requests so identity and rejection are graded apart from restoring expansion and selection.
- **Proposed wording:** We use a programmatic AppKit NSOutlineView for a nested library with stable IDs, titles and child arrays, showing Name and Kind columns. Updates can rename, reorder or remove entries, and must reject duplicate IDs anywhere without partly changing the outline. How should the data source keep surviving items' identity and retire removed ones? ‖ The same outline must keep expanded entries expanded and keep the visible selection after a reload or reorder, where those entries survive. How should it capture and restore that state?
- **Oracle:** Grade removed-node child count and expandability separately from duplicate rejection and from expansion and selection restoration.
- **Skill:** No card covers outline reload. If the split second question fails, add to actions.md: 'Capture expanded and selected item identities before reloadData and restore them by identity afterward.'
- **Routing:** Add 'NSOutlineView, expansion, selection after reload' to the actions cue if a card is added.

#### row-role-and-children

**`P-76d9fe6a4d351668`** · macOS AppKit · row-role-and-children · axis preservation · whole **gain**, primary both-pass · read: SKILL.md, actions.md · **P3 sound-control** · v3 n/a.

> macOS 26.0, AppKit. How does the row report its role and selection, and can people still operate its actionable children separately? Explain your conclusion and give a focused check. Include integrated Swift changes if t

- **Grades** (primary, preservation, verification, integration, rework, whole; ⚠ critical): unaided ✓ ✓ ✓ ✓ ✗ ✗ · installed ✓ ✓ ✓ ✓ ✓ ✓
- **Diagnosis:** v2 rescue: installed read actions.md and checked role, selected state and the child button's dispatch with no change needed. Unaided added a second row-level press and layout edits.
- **Question:** none
- **Oracle:** none
- **Skill:** none; facts.md AppKit-row contrast and the leave-it rule worked. This is the only twin pair where both variants pass.
- **Routing:** none

**`P-b43542c4e476c154`** · macOS AppKit · row-role-and-children · axis sentinel · whole **gain**, primary both-pass · read: SKILL.md, actions.md, facts.md · **P3 sound-control** · v3 n/a.

> macOS 26.0, AppKit. How does the row report its role and selection, and can people still operate its actionable children separately? Explain your conclusion and give a focused check. Include integrated Swift changes if t

- **Grades** (primary, preservation, verification, integration, rework, whole; ⚠ critical): unaided ✓ ✓ ✗ ✓ ✗ ✗ · installed ✓ ✓ ✓ ✓ ✓ ✓
- **Diagnosis:** v2 rescue, twin of P-76d9fe6a: installed read actions.md and facts.md, fixed only the hardcoded flag, exercised the child's real callback.
- **Question:** none
- **Oracle:** none
- **Skill:** none
- **Routing:** none

#### same-item-new-request

**`P-c6b25ad753e6a2d2`** · tvOS SwiftUI · same-item-new-request · axis primary · whole **both-fail**, primary both-fail · read: nothing read · **P1 not-opened** · v3 partial.

> tvOS developer question People can change videos or reload caption choices while this SwiftUI screen is open. Old callbacks sometimes affect the new selection, including turning captions off. Make these operations belong

- **Grades** (primary, preservation, verification, integration, rework, whole; ⚠ critical): unaided ✗ ✓ ✗ ✗ ✓ ✗ · installed ✗ ✓ ✗ ✗ ✓ ✗
- **Diagnosis:** v2: both fail; installed read nothing. Load cancellation does not scope the live picker binding, and tests use ordinary choose(nil) instead of a retained setter after replacement.
- **Question:** none
- **Oracle:** Assert against the player item's legible selection after an old Off fires; grade item change, same-item reload, stale Off, current choice and cancellation separately.
- **Skill:** Same as P-c04cc5d4: request-scoped binding setter; item identity catches replacement but not a newer request on the same item (already in media.md).
- **Routing:** Same as P-c04cc5d4.

#### selected-trait-vs-selection

**`P-db32e60bc16c19a8`** · iOS UIKit · selected-trait-vs-selection · axis rework · whole **both-fail**, primary both-fail · read: nothing read · **P1 not-opened** · v3 no.

> iOS 26.0, UIKit. Move selection between two rows. How is selection represented on each row after the move? Explain your conclusion and give a focused check. Include integrated Swift changes if the requested behavior need

- **Grades** (primary, preservation, verification, integration, rework, whole; ⚠ critical): unaided ✗ ✗ ✗ ✗ ✗ ✗ · installed ✗ ✗ ✗ ✗ ✗ ✗
- **Diagnosis:** v2: both fail every component; installed read nothing. Both couple saved status to collection selection, which the original code correctly kept independent.
- **Question:** none
- **Oracle:** Grade trait correctness, collection-selection preservation and rework separately.
- **Skill:** facts.md: 'The selected accessibility trait and collection-view selection are independent; reconfiguring a cell changes the trait, not isSelected.'
- **Routing:** Add 'selected trait, saved or favorite state, collection cell' to the facts cue.

#### selection-before-validation

**`P-2865458d46b0d1a4`** · iOS SwiftUI · selection-before-validation · axis primary · whole **both-fail**, primary both-fail · read: nothing read · **P1 not-opened** · v3 partial.

> iOS developer request My SwiftUI player shows caption choices, but choosing one currently only changes local state. Connect this to the media item so choosing captions really works without disturbing the audio the viewer

- **Grades** (primary, preservation, verification, integration, rework, whole; ⚠ critical): unaided ✗ ✓ – ✗ ✗ ✗ · installed ✗ ✓ – ✗ ✗ ✗
- **Diagnosis:** v2: both failed every component; the installed session read nothing. Both answers loaded or cached the group wrongly and added Off without checking empty-selection permission.
- **Question:** none
- **Oracle:** Keep component grades: native item selection, preserved audio, full-only offering, Off honoring allowsEmptySelection.
- **Skill:** media.md already holds the item.select and allowsEmptySelection rule; add the explicit path 'group from the item's asset, not the item' because the read twin (P-5d121776) still made that mistake.
- **Routing:** Add 'SwiftUI captions picker, subtitles, AVPlayerItem selection' to the description and media cue; 'track selection' did not trigger.

**`P-5d121776613655db`** · tvOS SwiftUI · selection-before-validation · axis primary · whole **both-fail**, primary gain · read: SKILL.md, media.md · **P1 verification-gap** · v3 yes.

> tvOS developer question My SwiftUI video screen only changes a local selected value when someone chooses captions. Connect the choices to the real media item without resetting audio or playback settings. Offer complete c

- **Grades** (primary, preservation, verification, integration, rework, whole; ⚠ critical): unaided ✗ ✓ ✗ ✗ ✓ ✗ · installed ✓ ✓ ✗ ✓ ✓ ✗
- **Diagnosis:** v2: installed read media.md and gained primary (writes within the legible group, honors permission, reads back), but the tests hand-build results or use an empty player.
- **Question:** none
- **Oracle:** Grade the four production components separately from the proof; a test with an empty player cannot establish selection.
- **Skill:** media.md check: use a local asset with a real legible group, establish a different initial selection, drive the picker binding, compare item.currentMediaSelection with the requested option.
- **Routing:** none

#### stale-action-capture

**`P-852a6aafb1bd0b6f`** · tvOS UIKit · stale-action-capture · axis sentinel · whole **both-fail**, primary both-pass · read: SKILL.md, actions.md · **P1 rework** · v3 no.

> tvOS 26.0, UIKit. Keep an action from before a refresh, then invoke it after the row represents a different record. What does it do? What do the current ordinary controls do? Explain your conclusion and give a focused ch

- **Grades** (primary, preservation, verification, integration, rework, whole; ⚠ critical): unaided ✓ ✓ ✓ ✓ ✗ ✗ · installed ✓ ✓ ✓ ✓ ✗ ✗
- **Diagnosis:** v2: both pass primary and verification; installed read actions.md but still offered an unnecessary positional routing alternative that could operate on a different record.
- **Question:** none
- **Oracle:** Score explanation, ordinary current action and behavior after rebinding separately for both twin sessions; report both-correct twins as the headline.
- **Skill:** actions.md: 'Do not offer alternative designs (index or ID-only routing) that remove a working ownership guard; if the guard works, say so and stop.'
- **Routing:** none

**`P-a12bcd8ed20f1256`** · tvOS UIKit · stale-action-capture · axis preservation · whole **both-fail**, primary both-pass · read: SKILL.md, actions.md · **P2 verification-gap** · v3 no.

> tvOS 26.0, UIKit. Keep an action from before a refresh, then invoke it after the row represents a different record. What does it do? What do the current ordinary controls do? Explain your conclusion and give a focused ch

- **Grades** (primary, preservation, verification, integration, rework, whole; ⚠ critical): unaided ✓ ✓ ✗ ✓ ✗ ✗ · installed ✓ ✓ ✗ ✓ ✓ ✗
- **Diagnosis:** v2: primary passes in both; installed read actions.md and gained rework, but the check obtains the action through target-action names and starts with nil selection, so it cannot distinguish the broken version.
- **Question:** none
- **Oracle:** Keep: a test that starts from nil selection cannot detect an obsolete clearing action; require a live selection before invoking the retained action.
- **Skill:** Entry verification rule already says 'use a distinguishable positive case'; add to actions.md: start the check from a live selection or count, so a stale action that clears it is visible.
- **Routing:** none

**`P-ddf8bad3cbd8d087`** · iOS UIKit · stale-action-capture · axis primary · whole **both-fail**, primary both-fail · read: SKILL.md, actions.md, facts.md · **P1 content-gap** · v3 no. Also gold-parity: `ios-uikit-actions`.

> I am using UIKit on iOS 26 deployment target; available validation anchor iOS 26.5. A file row already has Open and Delete buttons. Experienced VoiceOver users asked for a quicker Delete action. Rows are reused and can b

- **Grades** (primary, preservation, verification, integration, rework, whole; ⚠ critical): unaided ✗ ✗ ✗ ✗ ✗ ✗ ⚠ · installed ✗ ✗ ✗ ✗ ✓ ✗
- **Diagnosis:** v2: unaided critical (row made the actionable element); installed read actions.md and facts.md, removed the critical and gained rework, but the retained Delete checks only the ID and not permission or enabled state for the same file.
- **Question:** none
- **Oracle:** Grade shortcut addition, ordinary buttons preserved, invocation-time validation (current file and enabled) and tests separately.
- **Skill:** actions.md: 'At invocation, check everything that can change after install: owner identity and current enabled or permission state; return false when either fails.'
- **Routing:** none

**`P-f6c77faf11d5ad05`** · macOS SwiftUI · stale-action-capture · axis preservation · whole **both-fail**, primary both-pass · read: nothing read · **P2 not-opened** · v3 no.

> macOS 26.0, SwiftUI. Keep an action from before a refresh, then invoke it after the row represents a different record. What does it do? What do the current ordinary controls do? Explain your conclusion and give a focused

- **Grades** (primary, preservation, verification, integration, rework, whole; ⚠ critical): unaided ✓ ✓ ✓ ✓ ✗ ✗ · installed ✓ ✓ ✓ ✓ ✗ ✗
- **Diagnosis:** v2: primary and verification pass in both; installed read nothing and both offer removing a working generation guard (rework).
- **Question:** none
- **Oracle:** Assert the retained action is a no-op on the replacement and the current action deletes once; a test expecting stale success is an evidence failure.
- **Skill:** Same no-alternative-designs rule as P-852a6aaf.
- **Routing:** Add 'retained action after refresh, SwiftUI row' to the actions cue.

#### stale-observer-witness

**`P-0a2cd6519778f4c7`** · tvOS UIKit · stale-observer-witness · axis verification · whole **unpaired**, primary unpaired · read: nothing read · **P1 unmeasured** · v3 no.

> I'm reviewing a UIKit change for tvOS 26.0. After stopping and restarting preference observation, queued work from the old subscription must not change this screen. Does the code handle that? Review the supplied implemen

- **Grades** (primary, preservation, verification, integration, rework, whole; ⚠ critical): unaided unavailable · installed unavailable
- **Diagnosis:** v2: both arms were harness-rejected at startup (read-only client config), so the pair has no answer. The 384 baseline graded only the proof as weak (evidence-only).
- **Question:** none
- **Oracle:** Keep the review proposal: change the preference between stop and drain so de-duplication cannot hide a stale delivery, and require the test to fail on the old-generation mutant.
- **Skill:** No card covers observation restart. If this reproduces after a rerun, add one validation-card line: a restarted observer rejects queued work by subscription identity, and a check changes the value between stop and drain.
- **Routing:** Unknown until it runs; the validation cue names edits and submissions, not observation, so add 'restarted observation or queued delivery'.

#### stale-off-capture

**`P-c04cc5d4aa6f82d2`** · iOS SwiftUI · stale-off-capture · axis primary · whole **both-fail**, primary both-fail · read: nothing read · **P1 not-opened** · v3 partial.

> iOS developer question People can change videos or reload caption choices while this SwiftUI screen is open. Old callbacks sometimes affect the new selection, including turning captions off. Make these operations belong 

- **Grades** (primary, preservation, verification, integration, rework, whole; ⚠ critical): unaided ✗ ✓ ✗ ✗ ✓ ✗ · installed ✗ ✓ ✗ ✗ ✓ ✗
- **Diagnosis:** v2: both fail; installed read nothing. Load completions are guarded, but the picker's captured setter writes directly, so a retained Off still clears the new choice.
- **Question:** none
- **Oracle:** Grade old load ignored, old option callback including Off rejected after reload or item change, current choice applied, and cancellation separately.
- **Skill:** media.md (v3 media-delta): retain the old binding across reload; its Off must not clear the current choice. Add: 'the picker's Binding setter must carry the request it was created for.'
- **Routing:** Add 'reload caption choices, old callbacks, Picker binding' to the media cue.

**`P-f48375292f98ee5c`** · macOS SwiftUI · stale-off-capture · axis primary · whole **both-fail**, primary both-fail · read: nothing read · **P1 not-opened** · v3 partial.

> macOS developer question People can change videos or reload caption choices while this SwiftUI screen is open. Old callbacks sometimes affect the new selection, including turning captions off. Make these operations belon

- **Grades** (primary, preservation, verification, integration, rework, whole; ⚠ critical): unaided ✗ ✓ ✗ ✗ ✓ ✗ · installed ✗ ✓ ✗ ✗ ✓ ✗
- **Diagnosis:** v2: both fail; installed read nothing. The picker writes selection directly, bypassing the guarded selection task, so a stale Off setter still applies.
- **Question:** none
- **Oracle:** Exercise a retained binding from the old item after replacement; assert the new item's legible selection is unchanged and a current Off still applies when allowed.
- **Skill:** Same as P-c04cc5d4.
- **Routing:** Same as P-c04cc5d4.

#### supplied-vs-live-font

**`P-f776360cf78dd3e2`** · iOS UIKit · supplied-vs-live-font · axis primary · whole **both-pass**, primary both-pass · read: SKILL.md, font.md · **P2 sound-control** · v3 n/a.

> iOS 26.0, UIKit. In our "Preview text size" sheet the receipt descriptions never get bigger when a customer picks a larger size, and long descriptions are cut off with "…". The descriptions should keep our brand font, si

- **Grades** (primary, preservation, verification, integration, rework, whole; ⚠ critical): unaided ✓ ✓ – ✓ ✓ ✓ · installed ✓ ✓ – ✓ ✓ ✓
- **Diagnosis:** v2: both pass; installed read font.md. The historical native failure (auto-adjust overriding supplied size) did not reproduce on this source review.
- **Question:** none
- **Oracle:** Grade natively with the two qualified checkout-font contracts; source review missed this defect before.
- **Skill:** none
- **Routing:** none

#### swiftui-evidence-boundary

**`P-c55650380597efd4`** · tvOS SwiftUI · swiftui-evidence-boundary · axis verification · whole **both-fail**, primary both-pass · read: SKILL.md, facts.md · **P2 oracle-defect** · v3 no. Also gold-parity: `tvos-swiftui-testing`.

> I am using SwiftUI on tvOS 26 deployment target; available validation anchor tvOS 26.5. A new accessibility example compiles on my machine and its extracted state model passes unit tests. Can I say the control has the ri

- **Grades** (primary, preservation, verification, integration, rework, whole; ⚠ critical): unaided ✓ ✓ ✗ ✗ ✓ ✗ · installed ✓ ✓ ✗ ✗ ✓ ✗
- **Diagnosis:** v2: both met primary (speech and rotor unestablished) but failed verification over how the SDK is recorded; the question supplies an 'available validation anchor' that the installed answer reasonably reused as the SDK.
- **Question:** Separate the facts the developer supplies (deployment target, anchor runtime) from what the reproduction record must capture, so recording the anchor is not a trap.
- **Proposed wording:** I am using SwiftUI with a tvOS 26 deployment target and a tvOS 26.5 simulator. A new accessibility example compiles on my machine and its extracted state model passes unit tests. Can I say the control has the right spoken output and rotor behavior? Give a useful validation plan using compiler checks and unit tests only, and say what a failure report should record so someone else can reproduce it.
- **Oracle:** Primary: compile and unit checks establish only extracted state and wiring; speech and rotor are unestablished; no reflection as evidence. Score the reproduction record as a separate secondary component.
- **Skill:** facts.md: 'Record the installed SDK and Xcode build separately from the deployment target and the simulator runtime.'
- **Routing:** none

#### tagged-audio-positive-fixture

**`P-d76c1ea3d7c9a580`** · tvOS UIKit · tagged-audio-positive-fixture · axis verification · whole **both-fail**, primary gain · read: SKILL.md, media.md · **P2 verification-gap** · v3 no.

> tvOS 26.0, UIKit. Can this inspector tell an ordinary alternate-language track from one explicitly tagged as described audio? Keep the current player selection. Explain your conclusion and give a focused check. Include i

- **Grades** (primary, preservation, verification, integration, rework, whole; ⚠ critical): unaided ✗ ✓ ✗ ✗ ✗ ✗ · installed ✓ ✓ ✗ ✓ ✓ ✗
- **Diagnosis:** v2: installed read media.md and gained primary (read-only tag interpretation through the real inspector), but chose positive and negative examples by the characteristic under test.
- **Question:** none
- **Oracle:** Evidence requires both fixtures identified independently (ordinary alternate false, tagged described true) through the production mapping, and the native selected option compared before and after.
- **Skill:** Entry verification rule: name fixtures by a property other than the one under test (for example a known track ID or language).
- **Routing:** none

**`P-f28c1ae4058d31a8`** · macOS AppKit · tagged-audio-positive-fixture · axis verification · whole **both-fail**, primary both-pass · read: nothing read · **P2 not-opened** · v3 no.

> macOS 26.0, AppKit. Which tracks does this inspector identify as described audio when the asset has both ordinary alternate languages and a described track? Explain your conclusion and give a focused check. Include integ

- **Grades** (primary, preservation, verification, integration, rework, whole; ⚠ critical): unaided ✓ ✓ ✗ ✓ ✓ ✗ · installed ✓ ✓ ✗ ✓ ✓ ✗
- **Diagnosis:** v2: primary passes in both; installed read nothing; tests infer track identity from display names without a known fixture.
- **Question:** none
- **Oracle:** Require a positive fixture: the group has at least one untagged audio option before asserting it is not described; fail when loading never completes.
- **Skill:** Same fixture-naming rule as P-d76c1ea3.
- **Routing:** Add 'described audio, audio description track' to the media cue.

#### tv-text-availability

**`P-e56a902ef372a290`** · tvOS SwiftUI · tv-text-availability · axis primary · whole **gain**, primary gain · read: SKILL.md, facts.md · **P3 sound-control** · v3 n/a.

> tvOS, SwiftUI. Product wants titles readable from a couch. A long German title in our tvOS SwiftUI detail header crowds out Play and Details. What would you change on a 26.0 deployment target, and what would you conditio

- **Grades** (primary, preservation, verification, integration, rework, whole; ⚠ critical): unaided ✗ ✓ – ✓ ✗ ✗ · installed ✓ ✓ – ✓ ✓ ✓
- **Diagnosis:** v2 rescue: installed read facts.md, kept a readable layout and action row on tvOS 26 and placed the system Larger Text preference at tvOS 27.
- **Question:** none
- **Oracle:** none
- **Skill:** none; the tvOS availability fact works. Keep it dated and sourced.
- **Routing:** none

#### unavailable-result-check

**`P-9c455b0bd4be71db`** · iOS UIKit · unavailable-result-check · axis verification · whole **both-pass**, primary both-pass · read: nothing read · **P3 sound-control** · v3 n/a.

> iOS 26.0, UIKit. Open the inspector before assigning a player item, then inspect an item with no matching tracks. What result does the caller receive each time? Review the supplied implementation against that requirement

- **Grades** (primary, preservation, verification, integration, rework, whole; ⚠ critical): unaided ✓ ✓ ✓ ✓ ✓ ✓ · installed ✓ ✓ ✓ ✓ ✓ ✓
- **Diagnosis:** v2: both pass with no skill read. No headroom on Flash Low for this phrasing.
- **Question:** none
- **Oracle:** Evidence credit requires a pattern match or stated Equatable conformance.
- **Skill:** none
- **Routing:** none

#### validation-busy-recovery

**`P-db6ab4c551e67aca`** · iOS UIKit · validation-busy-recovery · axis primary · whole **both-fail**, primary both-fail · read: nothing read · **P0 not-opened** · v3 no.

> iOS 26.0, UIKit. Edit the entry while a validation request is outstanding. After the reply, can I submit the current entry? Review the supplied implementation against that requirement. If it already works, say why and le

- **Grades** (primary, preservation, verification, integration, rework, whole; ⚠ critical): unaided ✗ ✓ ✗ ✗ ✓ ✗ · installed ✗ ✓ ✗ ✗ ✓ ✗
- **Diagnosis:** v2: both fail primary; installed read nothing. As in P-4099aaf8, the test cancels through the helper and never drives the native field mutation.
- **Question:** none
- **Oracle:** Grade stale reply rejected, busy state ended after rejection, and a proof that changes the native field between submit and reply.
- **Skill:** validation.md: the field-event rule from P-4099aaf8, plus 'after retiring the request, end busy state so the current entry can be submitted'.
- **Routing:** Same as P-4099aaf8.

#### visible-selected-status

**`P-10464d860f6802b2`** · tvOS UIKit · visible-selected-status · axis primary · whole **unpaired**, primary unpaired · read: nothing read · **P1 unmeasured** · v3 no.

> tvOS 26.0, UIKit. On each selected or unselected update, we need readable status text, the button accessibility value, and its selected accessibility trait to agree. Does this tvOS implementation keep those three in sync

- **Grades** (primary, preservation, verification, integration, rework, whole; ⚠ critical): unaided unavailable · installed unavailable
- **Diagnosis:** v2: both arms harness-rejected; no paired answer. The 384 unaided answer failed with a real model gap: the three state channels drifted apart.
- **Question:** none
- **Oracle:** Assert visible text, accessibility value and the selected trait for both inputs applied in succession to the same button; accept equivalent localized wording.
- **Skill:** facts.md 'State across updates' already states the contrast. Rerun before changing content.
- **Routing:** Add 'selected state, accessibility value and visible status' to the facts cue; the current cue names title, role, edit category and text setting only.

#### visible-title-vs-identifier

**`P-7b8cff8f7531bd8f`** · tvOS UIKit · visible-title-vs-identifier · axis primary · whole **both-pass**, primary both-pass · read: SKILL.md, facts.md · **P3 sound-control** · v3 n/a.

> tvOS 26.0, UIKit. Someone using the remote wants to tell these two buttons apart by looking at the screen. What titles does this setup show? Review the supplied implementation against that requirement. If it already work

- **Grades** (primary, preservation, verification, integration, rework, whole; ⚠ critical): unaided ✓ ✓ ✓ ✓ ✓ ✓ · installed ✓ ✓ ✓ ✓ ✓ ✓
- **Diagnosis:** v2: both pass; installed read facts.md. The 384 baseline marked this a real gap, so the panel question now has no headroom on Flash Low.
- **Question:** none
- **Oracle:** Keep: assert the rendered title per state, matching the accessible name; identifiers do not count.
- **Skill:** none; keep the facts.md title-vs-identifier line as a regression guard.
- **Routing:** none

#### write-actual-player-selection

**`P-d4bd274c3a345669`** · iOS SwiftUI · write-actual-player-selection · axis primary · whole **both-fail**, primary both-fail · read: SKILL.md, media.md · **P0 content-gap** · v3 partial.

> iOS developer request Build a SwiftUI media-option picker that uses the same player and selection state as the video view. Distinguish a missing video, options still loading, no options and a load error. Provide a retry 

- **Grades** (primary, preservation, verification, integration, rework, whole; ⚠ critical): unaided ✗ ✓ ✗ ✗ ✓ ✗ · installed ✗ ✓ ✗ ✗ ✓ ✗
- **Diagnosis:** v2: both fail; installed read media.md, which says to use item.select, but choose still changes only app state and the test asserts a local property.
- **Question:** none
- **Oracle:** Grade the four states and retry separately from actual item selection; local-only selection fails the selection component.
- **Skill:** media.md: make the path concrete in one ordered line: current item, then the legible group from its asset, then item.select(option, in: group), then read the item's selection and publish that. Abstract wording was read and not applied.
- **Routing:** none

**`P-dc1e54ce99c97729`** · tvOS SwiftUI · write-actual-player-selection · axis primary · whole **both-fail**, primary both-fail · read: SKILL.md, media.md · **P0 content-gap** · v3 partial.

> tvOS developer request Build a SwiftUI media-option picker that uses the same player and selection state as the video view. Distinguish a missing video, options still loading, no options and a load error. Provide a retry

- **Grades** (primary, preservation, verification, integration, rework, whole; ⚠ critical): unaided ✗ ✓ ✗ ✗ ✓ ✗ · installed ✗ ✓ ✗ ✗ ✓ ✗
- **Diagnosis:** v2: both fail; installed read media.md and used a checked local ID and load generation, but neither production nor test touches the player's media selection.
- **Question:** none
- **Oracle:** A choice must change the shared item's media selection, asserted on the item.
- **Skill:** Same as P-d4bd274c: ordered concrete path plus the v3 check shape.
- **Routing:** none
<!-- tier1:end -->

### 6.3 Tier 2: the OS26 gold prompts and the gold-parity scenarios

**OS26 prompts:** these have native gates and killed mutants, but no model results.

**Gold-parity scenarios:** these are draft development cases. Three are Tier 1 parents and are listed there:
- ios-uikit-actions = P-ddf8bad3cbd8d087;
- ios-swiftui-media = P-b12c69f62639d32d;
- tvos-swiftui-testing = P-c55650380597efd4.

**Highlights:**
- **The OS26 prompts need a paired run.** They have the strongest oracles (2 killed mutants each) but no model results, and GP26-06's earlier unaided failure was for rework on a working Toggle.
- **The three download-card twins need their reload policy stated.** They never say whether the same file can be requested again while a request is pending, yet the tvOS twin was failed on that point. Re-grade it, and state the policy differently across the twins.
- **Text questions miss the font card.** font.md says it is UIKit-only and doesn't mention custom brand fonts, so macOS SwiftUI and UIKit text questions are not routed to it.
- **Missing contrasts:** tvOS remote focus vs `onTapGesture` (GP26-05); a gesture-only action vs Full Keyboard Access (GP26-04); a UIKit counterpart to the AppKit row fact (GP26-01).
- **Redundant controls:** three no-change Toggle controls overlap. Keep GP26-06, which has executable mutants.

<!-- tier2:begin -->
#### OS26 gold prompts

**`GP26-01`** · os26 · iOS UIKit · settings-actions · 384 unaided **pass** · gates: source-review, compile-host, known-good, mutation-1, mutation-2, switch-state, help-action · **P3 unmeasured** · v3 no

> VoiceOver only stops on “Downloads” in this settings row. People cannot change the setting or open Help. The existing callbacks are already wired. Can you fix it?

- **Diagnosis:** gates: 7/7 pass, 2 mutants killed (hidden descendants, dropped Help); no C0/C2 model run. 384: unaided pass, kept as control. Signal-v2 has an AppKit-row fact and a generic 'native children' cue but no UIKit statement about a parent element swallowing its switch and button.
- **Question:** none
- **Oracle:** Keep switch-state and help-action. Also accept answers that drop the row element entirely or use accessibilityElements ordering, and flag as rework any answer that replaces the UISwitch or re-wires the existing callbacks the prompt says already work.
- **Skill:** actions.md: add a UIKit counterpart to the AppKit row sentence: a UIKit parent with isAccessibilityElement = true hides its subviews from VoiceOver and accessibilityElementsHidden hides all descendants; expose the native switch and button rather than adding custom actions to the parent. Check shape: dispatch .valueChanged on the switch and .touchUpInside on Help, asserting only the matching callback moved.
- **Routing:** Would route on 'VoiceOver' plus UIKit; the actions.md cue 'native children' is AppKit-flavoured. Add 'a row that VoiceOver reads as one element' to the actions cue.

**`GP26-02`** · os26 · iOS UIKit · cell-reconfiguration · 384 unaided **pass** · gates: source-review, compile-host, known-good, mutation-1, mutation-2, reconfiguration · **P3 unmeasured** · v3 no

> After scrolling and refreshing orders, a cell sometimes announces the previous customer or status. Here is its configuration code; the model has customer/status strings and an isPriority flag, and titleLabel is already l

- **Diagnosis:** gates: reconfiguration pass, 2 mutants killed (normal-order label not reset, stale status); no model run. 384: unaided pass. Signal-v2 actions.md (configure twice, prepareForReuse can be skipped) and facts.md 'State across updates' address this directly.
- **Question:** none
- **Oracle:** Keep same-instance Alice-priority then Bob-normal and reverse. Make explicit that clearing via accessibilityValue = nil versus assigning the status for every order are both valid, and that an override resetting accessibilityLabel to nil (falling back to titleLabel) passes when the reported name is Bob without 'Priority'.
- **Skill:** actions.md names collection-view reconfigureItems; add that a table-view cell's configure(_:) has the same obligation: every branch assigns or clears each accessibility override it can set. Keep the 'configure twice on the same instance' check shape.
- **Routing:** none: 'announces' and 'cell' route to actions.md via the reconfiguration cue.

**`GP26-03`** · os26 · iOS UIKit · checkout-resize · 384 unaided **pass** · gates: source-review, compile-host, known-good, mutation-1, mutation-2, live-resize, payment-action · **P2 unmeasured** · v3 no

> Customers using larger text cannot read the complete checkout total. The container fills the safe-area width, and formattedTotal can be a long localized currency value. The Pay button already works and its appearance sho

- **Diagnosis:** gates: live-resize and payment-action pass, 2 mutants killed (fixed height kept, live scaling disabled); no model run. 384: pass but retired as duplicate of checkout-integrated. font.md separates text from the Pay action but frames size ownership around a supplied preview, not this live label.
- **Question:** none
- **Oracle:** live-resize must accept both preferredFont(forTextStyle:) and UIFontMetrics-scaled fonts when adjustsFontForContentSizeCategory is true, and any flexible arrangement (vertical axis, wrapping, removing fillEqually). Grade any added button configuration, new Pay button or restyled title as rework against payment-action.
- **Skill:** font.md: add the live-label case explicitly: a fixed systemFont(ofSize:) does not track the setting; a live label needs a scaled font plus automatic adjustment, multiple lines and no fixed enclosing height, while the Pay button object, title and callback stay untouched. Keep the existing preview sentence as the contrasting case.
- **Routing:** Partially: the font.md cue 'supplied versus live size settings' would not obviously match 'larger text cannot read the total'. Add 'larger text' and 'truncated or clipped label' to the font cue.

**`GP26-04`** · os26 · iPadOS SwiftUI · deletion-input-modes · 384 unaided **not in 384** · gates: source-review, compile-host, known-good, mutation-1, mutation-2, explicit-delete, voiceover-delete, keyboard-delete · **P2 unmeasured** · v3 no

> Our message row can only delete by swiping. Add an on-screen way to delete that works with VoiceOver and with Full Keyboard Access plus a hardware keyboard. Keep swipe deletion working. onDelete must delete the chosen me

- **Diagnosis:** gates: explicit-delete pass, dropped and duplicate delete mutants killed; keyboard and VoiceOver gates are review-only; prior384 none (new OS26 item). Signal-v2 covers adding a shortcut beside an ordinary action, not the reverse case of a gesture-only action that needs a visible control, and never mentions Full Keyboard Access.
- **Question:** none
- **Oracle:** Keep the two-ID explicit and swipe dispatch. Add an explicit review check that no deletion fires on focus or onAppear, accept a Button inside or beside the row plus .swipeActions or the retained DragGesture, and flag converting the row to List edit mode or adding confirmation as an unrequested policy change.
- **Skill:** actions.md: add a contrast for gesture-only actions: a drag or tap gesture is not reachable from VoiceOver activation or a hardware keyboard; a native Button keeps one handler for explicit activation while the gesture path remains, and both paths must dispatch the chosen item once. Check shape: call the installed Button action and the gesture end handler for two IDs.
- **Routing:** Description lists iOS but not iPadOS or keyboard input; add 'Full Keyboard Access' and 'gesture-only actions' to the description or actions cue.

**`GP26-05`** · os26 · tvOS SwiftUI · tv-remote-shelf · 384 unaided **pass** · gates: source-review, compile-host, known-good, mutation-1, mutation-2, remote-activation, voiceover-name · **P2 unmeasured** · v3 no

> Testers cannot reliably reach and select all the movie tiles with the remote. VoiceOver users also need to identify the movie they are opening. Movie is Identifiable with title and posterName; open(movie) opens its detai

- **Diagnosis:** gates: remote-activation first/middle/last pass, dropped-open and wrong-movie mutants killed; no model run. 384: unaided pass. Signal-v2's only tvOS fact is Larger Text; nothing states that a tap gesture on a non-focusable stack is not a remote focus target.
- **Question:** none
- **Oracle:** Accept Button with any button style (including card) or a focusable view with a primary action, as long as open receives the matching movie and the name derives from title. Flag hiding the poster from accessibility as acceptable, and adding a redundant label equal to the title as neutral, not rework.
- **Skill:** facts.md tvOS bullet: add that focus and Select activation come from focusable controls; an onTapGesture on a plain stack is not a reliable focus target, and the control's accessibility name should come from the item it opens. Check shape: invoke the installed action for several distinct IDs.
- **Routing:** Would route via 'tvOS' and 'VoiceOver', but no card cue mentions remote, focus or Select; add 'remote focus and Select' to the facts.md cue.

**`GP26-06`** · os26 · iOS SwiftUI · native-toggle-control · 384 unaided **fail** · gates: source-review, compile-host, known-good, mutation-1, mutation-2, native-toggle, scope-control · **P2 rework** · v3 no

> Please review the accessibility of this notification settings view and make any changes that are needed. The binding is connected to the existing preference store.

- **Diagnosis:** gates: native-toggle pass, constant and inverted binding mutants killed; scope-control is review-only. 384: unaided fail for adding a replacement label and hint to a labeled bound Toggle. Signal-v2 tells the agent to leave a satisfying path in place, but the panel shows unrequested rewrites of working native controls still cause rework, so this control needs a model run.
- **Question:** none
- **Oracle:** Keep no-change as fully valid with no code block. Score an added hint, duplicate label or custom trait as review burden (as scope-control says), and any binding change as regression via the two mutants. Record whether the skill was opened, since unopened sessions gain nothing.
- **Skill:** SKILL.md body: add one decision-point sentence: a native control whose visible title, role and binding already match the request needs no added label, hint or trait; say why and stop. Check shape: none unless asked.
- **Routing:** A generic 'review the accessibility' request with SwiftUI routes to the body; no card should open. none.

#### Gold-parity scenarios

**`ios-missing-reference`** · gold-parity · iOS UIKit · control/unavailable-reference · 384 unaided **pass** · criteria: review_only 3 · **P3 sound-control** · v3 n/a

- **Diagnosis:** parity: 3 review-only epistemic control; a listed reference is not a retrieval trace. 384: unaided pass. Signal-v2's ROUTING line for files actually consulted supports honest read reporting.
- **Question:** none
- **Oracle:** none; keep criterion-2 graded against retained read traces, not reference names.
- **Skill:** none
- **Routing:** Not routed and need not be: the subject names no Swift framework or platform. none.

**`ios-swiftui-lifecycle`** · gold-parity · iOS SwiftUI · topic/lifecycle · 384 unaided **pass** · criteria: partial_evidence 2, review_only 1 · **P1 verification-gap** · v3 partial

- **Diagnosis:** parity: 2 partial, 1 review-only; helper tests reject old and duplicate tickets by direct invocation, but the SheetExample reads a mutable ticket inside onDismiss, the stale-callback shape behind signal-v2's critical failures. 384: unaided pass. Helper passes could credit an answer with the same wiring defect.
- **Question:** Ask for integrated sheet code so the onDismiss wiring and fallback eligibility are gradable, not only a described ticket scheme.
- **Proposed wording:** iOS 26.0, SwiftUI. Here is our ItemList, which presents a details sheet for the tapped item and tries to return VoiceOver attention to it afterward. The list can reorder or delete that item while the sheet is open. Dismissal completion can arrive twice, and a new sheet can open before an older completion runs. If the opener is gone, return to the first remaining eligible item; if none remains, make no request. Please change the file so this holds, and add focused unit tests without UI automation.
- **Oracle:** Bind criterion-1 to the actual no-argument dismissal callbacks installed for A and B: invoke A late after B opens, then B twice, and assert one restoration request to B's origin. Add a fallback-eligibility case (fallback disabled or removed gives no request). Do not count helper tests that pass ticket A explicitly.
- **Skill:** return.md: replace 'Consume a matching request before invoking reentrant code' with a contrast naming how the match is known: the dismissal callback must carry the identity of its own presentation, captured when presented; reading the current active ticket at completion lets a late callback claim the replacement. Also apply the eligibility recheck to the fallback.
- **Routing:** Would route: 'return attention', 'dismissal' match return.md.

**`ios-swiftui-no-change`** · gold-parity · iOS SwiftUI · control/preservation · 384 unaided **pass** · criteria: review_only 3 · **P3 sound-control** · v3 n/a

- **Diagnosis:** parity: 3 review-only; same decision as ios-swiftui-semantics and GP26-06 in shorter form. 384: unaided pass, retired as duplicate. Three Toggle no-change controls overlap and only GP26-06 has executable mutants or a recorded fail.
- **Question:** none
- **Oracle:** Retire from new comparisons in favor of GP26-06 (executable) and ios-swiftui-semantics (evidence reasoning); no oracle change otherwise.
- **Skill:** none
- **Routing:** none

**`ios-swiftui-semantics`** · gold-parity · iOS SwiftUI · topic/semantics · 384 unaided **pass** · criteria: partial_evidence 1, review_only 2 · **P3 sound-control** · v3 n/a

- **Diagnosis:** parity: 1 partial (Binding units), 2 review-only; no defect supplied and an override is not required. 384: unaided pass. Overlaps GP26-06 and ios-swiftui-no-change; this is the only one asking to separate a reviewer's blanket claim from evidence.
- **Question:** none
- **Oracle:** none beyond accepting an optional explanation of label versus identifier; do not bind a native semantic-tree test or require a redundant label.
- **Skill:** none
- **Routing:** none: 'switch', 'accessibility label and role' and SwiftUI route to the body; facts.md role cue may open and is harmless.

**`ios-uikit-no-change`** · gold-parity · iOS UIKit · control/preservation · 384 unaided **pass** · criteria: review_only 3 · **P3 sound-control** · v3 n/a

- **Diagnosis:** parity: 3 review-only; working UISwitch and naming are task premises. 384: unaided pass. Signal-v2 body sentence on leaving a satisfying path in place matches the requested decision.
- **Question:** none
- **Oracle:** none; accept no-change with optional bounded advice and check that read claims match retained traces.
- **Skill:** none
- **Routing:** Would route on 'accessibility defect'; opening is not needed to pass.

**`ios-uikit-state`** · gold-parity · iOS UIKit · topic/state · 384 unaided **pass** · criteria: partial_evidence 3 · **P2 question-defect** · v3 no

- **Diagnosis:** parity: 3 partial-evidence criteria spread over separate semantics, AVPlayer-owner and Archive/Delete fixtures, none on one card. 384: unaided pass. The prompt never says whether a file can be re-requested while pending, so same-file supersession is undecidable, the defect that failed the tvOS twin.
- **Question:** State the reload policy and supply the card so the endpoint is an integrated change rather than a strategy essay.
- **Proposed wording:** iOS 26.0, UIKit. Here is our DownloadCardView and the code that applies metadata to it. One card instance is reused for different files: it shows a title, optional status, optional help text, a selected state and an Open button. File A has status "Ready" and help "Opens offline"; file B has neither. Each file's metadata is requested once per display and is not re-requested while a request is pending. A late result for A sometimes arrives after B is shown. Please update the card so it always describes the file it shows, keep Open working, and add a focused unit check.
- **Oracle:** Bind one same-instance contract: A then B leaves status, help and accessibilityValue absent; a late A result changes nothing; Open dispatches B once; selected trait matches B. Under this wording, file-identity checks suffice; do not require a generation token.
- **Skill:** facts.md 'State across updates': add that a late asynchronous result must be checked against the file the card currently shows before it writes, and that optional fields absent from B are cleared, not left from A. Avoid 'consume a matching request' phrasing. Check shape: apply A, B, then deliver A's result on the same instance.
- **Routing:** Not routed: no cue covers late results on a reused view (validation.md is form-specific, media.md is tracks). Add 'late async result on a reused view or card' to the facts.md or validation.md cue.

**`ios-uikit-text`** · gold-parity · iOS UIKit · topic/text · 384 unaided **fail** · criteria: partial_evidence 2, review_only 2 · **P2 rework** · v3 no

- **Diagnosis:** parity: 2 partial, 2 review-only; checkout and choice-cell fixtures are separate and no live description plus design-font update path exists. 384: unaided fail for building a new Pay button, action and constraints instead of integrating with the existing one. With no code supplied, 'existing Pay button' and 'design font' cannot be preserved observably.
- **Question:** Supply the existing checkout code and state which texts must follow the text-size setting and what Pay styling is fixed, so preservation is checkable.
- **Proposed wording:** iOS 26.0, UIKit. Here is our CheckoutSummaryView: a total label, a long localized description label and an existing Pay button with our brand font and a configured callback. Both labels use the Brand Sans family at fixed point sizes. At larger text sizes the description crowds the button, and the text stays the same size after people change the setting while the screen is open. The total, description and Pay title should follow the person's text size; Pay must keep its font family, appearance and callback. Please change the file and add focused unit checks, and say what they establish.
- **Oracle:** Grade components separately: scalable custom-font configuration on both labels and the Pay title, flexible layout without fixed height, Pay object identity and callback exactly once, and claims about what units cannot show. Flag a newly created Pay button as rework. Accept any justified flexible arrangement.
- **Skill:** font.md: add the custom design-font fact: a brand font scales by deriving it through font metrics for a text style and enabling automatic adjustment; preserve the family rather than swapping to a system style. State that this is configuration on the existing labels and button title, not a new control.
- **Routing:** Would route to font.md only weakly; 'design font' and 'larger text' are absent from the cue. Add 'custom or brand font' and 'larger text' to the font.md cue.

**`macos-appkit-actions`** · gold-parity · macOS AppKit · topic/actions · 384 unaided **pass** · criteria: partial_evidence 3 · **P3 verification-gap** · v3 partial

- **Diagnosis:** parity: 3 partial; direct Open/Save dispatch units stand in for Delete, and one shortcut-object count does not prove exactly-once ordinary and shortcut delivery after repeated setup. 384: unaided pass, retired as duplicate of integration G-1994190a4b0c63.
- **Question:** none
- **Oracle:** Keep retired from new comparisons. If retained, add positive shortcut dispatch after reuse and after re-enable, plus one ordinary Delete click, each counting deliveries on the current file; accept stable dispatcher and per-binding refresh equally.
- **Skill:** actions.md: add enabled state to the retained-action sentence: at invocation, a shortcut checks both the current file and whether its row and matching ordinary control are enabled. Add the AppKit vehicle (NSAccessibilityCustomAction on the row) alongside the UIKit one.
- **Routing:** Would route via 'VoiceOver', 'Delete action', 'reused' to actions.md.

**`macos-appkit-no-change`** · gold-parity · macOS AppKit · control/preservation · 384 unaided **pass** · criteria: review_only 3 · **P3 sound-control** · v3 n/a

- **Diagnosis:** parity: 3 review-only; a titled, enabled, connected NSButton is a premise. 384: unaided pass. Signal-v2 facts.md AppKit row bullet guards against applying UIKit hiding assumptions.
- **Question:** none
- **Oracle:** Add a calibration answer that wrongly cites a UIKit-only property for NSButton and require it to fail criterion-0.
- **Skill:** none
- **Routing:** Would route on 'custom accessibility element' with AppKit; none.

**`macos-appkit-structure`** · gold-parity · macOS AppKit · topic/structure · 384 unaided **pass** · criteria: partial_evidence 2, review_only 1 · **P2 question-defect** · v3 no

- **Diagnosis:** parity: 2 partial, 1 review-only; container-flag and outline-selection units come from different sources and neither asserts heading/balance grouping with separate Open/Details. 384: pass but weak-endpoint, strategy only. Optional heading/rotor makes the requested navigation aid undecidable.
- **Question:** Supply the row view and decide whether a rotor is wanted, so the composition and its stable identity become checkable.
- **Proposed wording:** macOS 26.0, AppKit. Here is our ReportRowView inside an NSTableView: a heading label, a balance label, and Open and Details buttons with existing actions. VoiceOver users find it slow to move from one report to the next, and they must still reach Open and Details on each row through ordinary navigation. We would like a way to jump between reports by name. Reports can be reordered or removed on refresh. Please change the file and add focused unit checks, and state what those checks cannot show.
- **Oracle:** Assert Open and Details remain accessibility children with their actions dispatching once for the current report, the descriptive element combines heading and balance, and any rotor or heading entry resolves to current reports after reorder and removal. Accept a row role with exposed children; do not grade on a single isAccessibilityElement Boolean.
- **Skill:** facts.md AppKit rows: add a check shape: after configuring, list the row's accessibilityChildren and invoke each child's action. Add a sentence that navigation entries such as rotor results must be keyed by stable item identity, not row index.
- **Routing:** Would route via 'AppKit', 'row', 'VoiceOver' to facts.md and actions.md; add 'rotor or heading navigation' to the actions cue.

**`macos-appkit-testing`** · gold-parity · macOS AppKit · topic/testing · 384 unaided **pass** · criteria: review_only 4 · **P3 sound-control** · v3 n/a

- **Diagnosis:** parity: 4 review-only; the question itself scopes compile/unit evidence against spoken output and rotor behavior. 384: unaided pass. Signal-v2 body already says to separate configured behavior from delivered assistive interaction.
- **Question:** none
- **Oracle:** Keep failure-preservation criterion-1 graded as part of the requested plan, but do not require repository-specific record formats; accept any plan that keeps first failure, repair and environment separate.
- **Skill:** none
- **Routing:** Weak: a test-planning question may not trigger 'Review or implement accessibility'. Add 'or verify' to the description if testing questions are in scope.

**`macos-swiftui-lifecycle`** · gold-parity · macOS SwiftUI · topic/lifecycle · 384 unaided **pass** · criteria: partial_evidence 2, review_only 1 · **P3 verification-gap** · v3 partial

- **Diagnosis:** parity: 2 partial, 1 review-only; helpers mirror iOS with constant fallback, and a focus declaration does not validate callback ownership, fallback validity or delivered focus. 384: unaided pass, retired as duplicate of integration G-fe05e95d638c25.
- **Question:** none
- **Oracle:** If kept, share the iOS completion-wiring check: drive the installed dismissal callbacks for A and B, plus a fallback that is itself ineligible. Accept request/state conclusions only; reject claims of delivered focus.
- **Skill:** return.md: the same identity-at-presentation contrast as the iOS twin, plus the existing AppKit first-responder caution applied to the fallback.
- **Routing:** Would route via 'return attention' and 'dismissal'.

**`macos-swiftui-state`** · gold-parity · macOS SwiftUI · topic/state · 384 unaided **pass** · criteria: partial_evidence 3 · **P2 question-defect** · v3 no

- **Diagnosis:** parity: 3 partial; SettingsState, availability hint, track generation and DocumentState helpers are separate and none is one composed card. 384: pass but weak-endpoint. Same undecidable reload policy as the iOS and tvOS twins.
- **Question:** Supply the SwiftUI card and model, and state that a file can be re-requested while pending so the macOS twin tests the supersession branch the iOS twin leaves out.
- **Proposed wording:** macOS 26.0, SwiftUI. Here is our DownloadCard view and its model. One card stays on screen while it shows different files: a title, optional status, optional help, a selected state and an Open button. File A has status "Ready" and help "Opens offline"; file B has neither. The same file's metadata can be requested again while an earlier request for it is still pending, and a late result for A may arrive after B is shown. Please update the files so the card always describes the file it shows, keep Open working, and add focused unit checks.
- **Oracle:** Assert after A, B and late A: help and status nil, value and selection match B, Open calls B's handler once; under this wording also assert an earlier same-file response is inert after a newer request. Accept identity-plus-request or snapshot strategies; flag added announcements as rework.
- **Skill:** Same facts.md 'State across updates' addition as the iOS twin, plus the media.md insight generalized: file identity catches replacement but not a newer request for the same file.
- **Routing:** Not routed: add the late-result-on-reused-view cue.

**`macos-swiftui-text`** · gold-parity · macOS SwiftUI · topic/text · 384 unaided **inconclusive** · criteria: genuine_gap 2, review_only 2 · **P1 question-defect** · v3 no

- **Diagnosis:** parity: 2 genuine-gap, 2 review-only; no total/description/Pay/design-font contract exists and captured DynamicTypeSize/ScaledMetric declarations show availability only. 384: inconclusive because with no code the grader could not tell whether the design font and Pay survive. font.md is UIKit-only.
- **Question:** Supply the view and say where the text-size preference comes from on this Mac app, since the source of the setting decides the integration.
- **Proposed wording:** macOS 26.0, SwiftUI. Here is our CheckoutView: a total, a long localized description and a Pay button that uses our brand font and calls pay(). Our app has its own Text Size setting stored with AppStorage. At larger settings the description crowds the Pay button. The total, the description and the Pay title should follow that setting; Pay keeps its font family and callback. Please change the file, add focused unit checks, and say what they establish.
- **Oracle:** Assert Pay keeps its callback and font family, text sizes derive from the app setting, and the layout policy changes at large settings; accept a permanently flexible layout. Keep SDK, deployment and runtime claims separate; do not credit availability declarations as settings propagation.
- **Skill:** facts.md: add a macOS text-size bullet: identify whether size comes from the system or an app setting before choosing an API, gate each API by its own macOS declaration, and keep custom font family while scaling. font.md title should stop implying UIKit only, or add a SwiftUI pointer.
- **Routing:** Not routed to font.md: its cue says 'existing UIKit label'. Add 'text size on SwiftUI or macOS' to the font or facts cue.

**`mixed-macos-owner`** · gold-parity · macOS mixed · control/ownership · 384 unaided **pass** · criteria: review_only 3 · **P2 content-gap** · v3 no

- **Diagnosis:** parity: 3 review-only; the audit records a Gemini comparison answer that overgeneralized an AppKit isAccessibilityElement Boolean into a role/children conclusion. 384: unaided pass. Signal-v2 facts.md says a row role and exposed children can coexist but not that a Boolean alone cannot settle which layer groups.
- **Question:** none
- **Oracle:** Add the AppKit parent-role-with-children counterexample to calibration, and require conditional advice keyed to the owning layer; credit requests for both the SwiftUI host and AppKit view code.
- **Skill:** facts.md AppKit rows: add that across a SwiftUI/AppKit boundary, first identify which layer sets grouping; one isAccessibilityElement value on the AppKit parent does not show whether its children stay exposed. Ask for the hosting representable and the view's accessibility overrides before recommending a change.
- **Routing:** Would route via actions.md 'bridged controls'; add 'SwiftUI hosting AppKit' to that cue.

**`tvos-swiftui-actions`** · gold-parity · tvOS SwiftUI · topic/actions · 384 unaided **inconclusive** · criteria: partial_evidence 3 · **P2 question-defect** · v3 partial

- **Diagnosis:** parity: 3 partial; document-state units and a native BridgeOwner never run the installed SwiftUI Button and accessibility-action closures (the v2 'never exercises the installed handler' gap). 384: inconclusive with grader uncertainty. 'Rows are reused' is a UIKit notion; in SwiftUI it leaves unclear whether a row view's file changes under the same identity.
- **Question:** Replace the reuse wording with a stated SwiftUI fact about identity and file change, and ask for code whose installed actions can be invoked.
- **Proposed wording:** tvOS 26.0, SwiftUI. Our FileRow view already has Open and Delete buttons. Experienced VoiceOver users asked for a quicker Delete action. After a refresh the same row can be given a different file, and a file can become disabled while its row is visible. How should I add the shortcut without taking anything away? Provide the updated row, explain how both Delete paths act on the current file, and add focused unit checks.
- **Oracle:** Bind the source: ordinary Open and Delete remain, the accessibility action and the Delete button call one handler on the current file once, and both do nothing while disabled. Accept a stable current-owner dispatcher. Do not credit state-model tests as traversal evidence.
- **Skill:** actions.md: add a SwiftUI sentence: an accessibilityAction closure and a Button action are separate paths; both should resolve the current file and enabled state from the same source at activation. Check shape: invoke the installed closures, not only the model method.
- **Routing:** Would route via 'VoiceOver', 'Delete action' to actions.md; v3's added description phrase is about wrappers and does not change this.

**`tvos-swiftui-structure`** · gold-parity · tvOS SwiftUI · topic/structure · 384 unaided **pass** · criteria: partial_evidence 2, review_only 1 · **P3 sound-control** · v3 no

- **Diagnosis:** parity: 2 partial, 1 review-only; DocumentExample compiles .contain with separate buttons, model units assert landmark subset and stable selection, but heading/balance with Open/Details is source review only. 384: unaided pass.
- **Question:** none
- **Oracle:** Add a reviewed source contract: descriptive subgroup combines heading and balance, Open and Details remain separate focusable controls, and optional rotor omission is valid. Judge landmark meaningfulness separately.
- **Skill:** facts.md: add a SwiftUI grouping contrast: combining children merges their text and can absorb buttons; containing children keeps them separately reachable. Applies on tvOS as on iOS.
- **Routing:** Uncertain: the subject names navigation and buttons but not VoiceOver or accessibility, so the generic description may not trigger. Add 'grouping' and 'heading or rotor navigation' to the description or actions cue.

**`tvos-uikit-lifecycle`** · gold-parity · tvOS UIKit · topic/lifecycle · 384 unaided **pass** · criteria: direct_evidence 2, review_only 1 · **P3 sound-control** · v3 partial

- **Diagnosis:** parity: 2 direct-evidence, 1 review-only; the native helper rechecks ancestry/enabled/visibility and units cover removed origin, old and duplicate completion and reentrant begin. 384: unaided pass. Actual dismissal-completion wiring stays review-only.
- **Question:** none
- **Oracle:** none for the helper criteria; keep integration wiring as a separate review item and restrict claims to restoration requests, not delivered focus.
- **Skill:** return.md: the identity-at-presentation rewrite proposed for SwiftUI applies here too: the UIKit completion should hold its own session token, so 'matching' is not read from shared state at completion time.
- **Routing:** Would route via 'return attention' and 'dismissal'.

**`tvos-uikit-media`** · gold-parity · tvOS UIKit · topic/media · 384 unaided **inconclusive** · criteria: partial_evidence 3, review_only 1 · **P2 oracle-defect** · v3 no

- **Diagnosis:** parity: 3 partial, 1 review-only; owner, metadata and tagged-selection fixtures exist but are separate; 384: inconclusive with grader uncertainty. Criterion-1 rejects stale same-item generations though the prompt never says a load can be retried. Signal-v2 media.md covers read-only inspection and same-item supersession but frames itself as track selection, not availability loading.
- **Question:** Add one stated fact that a load can be retried for the same item, so the generation branch is a stated requirement.
- **Proposed wording:** tvOS 26.0, UIKit. A video card shows whether audio description is available for the current player item. Loading track information may succeed with no match, fail, or still be in progress, and the app can retry loading for the same item while an earlier load is still running. The player item can change before loading finishes. We must keep the user's selected audio and captions as they are. How should the metadata state and callback logic work, and what would unit tests prove?
- **Oracle:** Make five states explicit: no item, loading, loaded-absent, loaded-present, error. Reject late completions from an older item or an older same-item load; assert both media groups' selections unchanged including a non-Off caption selection. Accept any token scheme.
- **Skill:** media.md: add an availability paragraph: no item, loading, successful no-match and failure are different states; an error is not 'unavailable'; checking availability never calls select. Keep the existing same-item sentence and apply it to loads.
- **Routing:** Weak: media.md cue is 'track selection and overlapping requests'; add 'audio description or caption availability' to the cue.

**`tvos-uikit-state`** · gold-parity · tvOS UIKit · topic/state · 384 unaided **fail** · criteria: partial_evidence 3 · **P1 oracle-defect** · v3 no

- **Diagnosis:** 384: unaided fail graded on same-file reload ownership, which the prompt never states (prior review P1 oracle-mismatch). parity: 3 partial; the audited criterion is now conditional ('when material'), but the historical fail still counts against the cell.
- **Question:** State the reload policy so same-file supersession is graded only when asked.
- **Proposed wording:** tvOS 26.0, UIKit. I reuse one download card for different files. It shows a title, optional status, optional help text, a selected state and an Open button. Updates can arrive without rebuilding the card: file A has status "Ready" and help "Opens offline"; file B has neither. The same file can be requested again while an earlier request for it is still pending, and a late result for A may arrive after B is shown. Describe a complete update strategy with a self-contained example and focused unit checks, and keep Open working.
- **Oracle:** Re-grade the frozen 384 answer under the original wording without the reload requirement and record the change as an oracle repair. Grade A-after-B rejection and clearing of A's status/help as primary; grade same-file reload only under the amended wording. Do not assert remote delivery from Open dispatch.
- **Skill:** Same facts.md late-result addition as the iOS twin; on tvOS add that Open's primary action is dispatched by the existing button and should not be rebuilt per update.
- **Routing:** Not routed: add the late-result-on-reused-view cue.

**`tvos-version-boundary`** · gold-parity · tvOS UIKit · control/version-boundary · 384 unaided **pass** · criteria: review_only 3 · **P3 sound-control** · v3 n/a

- **Diagnosis:** parity: 3 review-only; target 26, SDK 27 and runtime are separate facts. 384: unaided pass. Signal-v2 facts.md tvOS bullet directly states Larger Text is described for tvOS 27 and to gate APIs by declarations.
- **Question:** none
- **Oracle:** Accept citing the skill's WWDC26 fact only as reported guidance, not as a read declaration; still require naming the missing availability declaration or runtime record for the exact API.
- **Skill:** none
- **Routing:** Would route via 'tvOS' and 'Larger Text' to facts.md.
<!-- tier2:end -->

### 6.4 Tier 3: the remaining discovery prompts, by decision key

These 302 prompts keep their item-level recommendations in [PROMPT-IMPROVEMENTS.md](../prompt-improvements-v1/PROMPT-IMPROVEMENTS.md). The table adds what the signal-v2 evidence implies for each decision, based on the skill content the earlier review linked. Implementation prompts without a registered decision key are grouped as `open:implementation`. **Two changes to the earlier review:**
- Items it linked only to S1 (the review sentence) gain only when the skill is opened, so the description fix comes first.
- Its `reserve-transfer` items should form the transfer set in section 5.

<!-- tier3:begin -->
| Decision key | Items | Unaided pass / fail / inconclusive | Main dispositions | P0 / P1 | Skill codes | What v2 evidence implies |
|---|---:|---|---|---|---|---|
| open:implementation | 78 | 54 / 8 / 16 | keep-control 38, repair-oracle 14 | 0 / 11 | S3, S2, S7, S5, S8, S4, S6, S1 | Apply the capture-at-install rule (return.md rewrite; actions.md AppKit and invocation-time checks). |
| open:historical | 15 | 15 / 0 / 0 | keep-control 14, retire-duplicate 1 | 0 / 0 | S4, S3, S8, S1, S2, S5 | Apply the makeFirstResponder fallback and per-presentation dismissal rules; add focus trigger terms. |
| request-generation | 10 | 10 / 0 / 0 | keep-control 6, retire-duplicate 3 | 0 / 0 | S3, S1, S2 | Apply the capture-at-install rule (return.md rewrite; actions.md AppKit and invocation-time checks). |
| forced-vs-full | 7 | 1 / 2 / 4 | specify-policy 4, repair-oracle 2 | 1 / 5 | S7, S2, S1, S8 | Apply the concrete media path (item, asset group, select, read back) and request-scoped picker setter. |
| eligible-target | 6 | 6 / 0 / 0 | keep-control 5, pair-variant 1 | 0 / 0 | S4, S1 | Apply the makeFirstResponder fallback and per-presentation dismissal rules; add focus trigger terms. |
| motion-policy | 6 | 4 / 2 / 0 | rewrite-neutral 2, grade-components 1 | 0 / 3 | S1, S8 | Entry review sentence already helps; it only works when the skill is opened. |
| optional-help | 6 | 5 / 0 / 1 | keep-control 2, reserve-transfer 2 | 0 / 0 | S1, S8, S2, S5 | Entry review sentence already helps; it only works when the skill is opened. |
| range-kind | 6 | 3 / 3 / 0 | rewrite-neutral 3, grade-components 2 | 0 / 4 | S1, S8, S2 | Entry review sentence already helps; it only works when the skill is opened. |
| rebound-action | 6 | 6 / 0 / 0 | reserve-transfer 2, rewrite-neutral 2 | 0 / 0 | S3, S2 | Apply the capture-at-install rule (return.md rewrite; actions.md AppKit and invocation-time checks). |
| container-children | 5 | 4 / 1 / 0 | pair-variant 2, rewrite-neutral 2 | 1 / 1 | S1, S8 | Entry review sentence already helps; it only works when the skill is opened. |
| disabled-action | 5 | 4 / 1 / 0 | pair-variant 2, rewrite-neutral 2 | 0 / 2 | S1, S2, S8 | Entry review sentence already helps; it only works when the skill is opened. |
| duplicate-id | 5 | 5 / 0 / 0 | reserve-transfer 3, keep-control 1 | 0 / 0 | S1 | Entry review sentence already helps; it only works when the skill is opened. |
| modal-state | 5 | 5 / 0 / 0 | keep-control 2, pair-variant 1 | 0 / 0 | S4, S1 | Apply the makeFirstResponder fallback and per-presentation dismissal rules; add focus trigger terms. |
| open:integration | 5 | 2 / 2 / 1 | keep-control 2, repair-oracle 2 | 1 / 1 | S3, S8, S1, S2, S4 | Apply the capture-at-install rule (return.md rewrite; actions.md AppKit and invocation-time checks). |
| refresh-name | 5 | 3 / 2 / 0 | keep-control 2, grade-components 1 | 1 / 1 | S1, S8 | Entry review sentence already helps; it only works when the skill is opened. |
| audio-description-tag | 4 | 2 / 1 / 1 | rewrite-neutral 2, keep-control 1 | 0 / 1 | S2, S8, S1, S7 | Use the check shapes: second configuration, real handler, independently named fixtures. |
| edited-matches | 4 | 3 / 0 / 1 | pair-variant 2, rewrite-neutral 1 | 0 / 1 | S6, S1, S2, S3 | No v2 evidence; leave text-offset guidance on demand. |
| grapheme-boundary | 4 | 4 / 0 / 0 | keep-control 4 | 0 / 0 | S6, S1 | No v2 evidence; leave text-offset guidance on demand. |
| invalid-submit | 4 | 4 / 0 / 0 | keep-control 2, reserve-transfer 2 | 0 / 0 | S1, S2 | Entry review sentence already helps; it only works when the skill is opened. |
| preserve-traits | 4 | 4 / 0 / 0 | retire-duplicate 2, pair-variant 1 | 0 / 0 | S5 | Keep and extend facts.md; single named facts produced the clearest rescues. |
| range-coordinate | 4 | 1 / 3 / 0 | rewrite-neutral 4 | 3 / 1 | S6, S2, S1 | No v2 evidence; leave text-offset guidance on demand. |
| stable-selection | 4 | 4 / 0 / 0 | keep-control 2, reserve-transfer 1 | 0 / 0 | S1, S2 | Entry review sentence already helps; it only works when the skill is opened. |
| conflicting-state-text | 3 | 1 / 2 / 0 | pair-variant 1, rewrite-neutral 1 | 1 / 1 | S1, S5, S8 | Entry review sentence already helps; it only works when the skill is opened. |
| duplicate-completion | 3 | 3 / 0 / 0 | keep-control 1, reserve-transfer 1 | 0 / 0 | S3 | Apply the capture-at-install rule (return.md rewrite; actions.md AppKit and invocation-time checks). |
| interop-rebind | 3 | 2 / 1 / 0 | pair-variant 1, reserve-transfer 1 | 0 / 1 | S3, S1, S8 | Apply the capture-at-install rule (return.md rewrite; actions.md AppKit and invocation-time checks). |
| observer-stop | 3 | 3 / 0 / 0 | pair-variant 2, reserve-transfer 1 | 0 / 0 | S3, S2 | Apply the capture-at-install rule (return.md rewrite; actions.md AppKit and invocation-time checks). |
| player-item-owner | 3 | 3 / 0 / 0 | keep-control 1, pair-variant 1 | 0 / 0 | S3, S7 | Apply the capture-at-install rule (return.md rewrite; actions.md AppKit and invocation-time checks). |
| preference-redelivery | 3 | 3 / 0 / 0 | retire-duplicate 2, pair-variant 1 | 0 / 0 | — | Question or oracle work only. |
| presentation-owner | 3 | 3 / 0 / 0 | keep-control 1, pair-variant 1 | 0 / 0 | S3, S4 | Apply the capture-at-install rule (return.md rewrite; actions.md AppKit and invocation-time checks). |
| contrast-linear | 2 | 1 / 1 / 0 | repair-oracle 1, rewrite-neutral 1 | 1 / 0 | S1, S2 | Entry review sentence already helps; it only works when the skill is opened. |
| decorative-element | 2 | 1 / 1 / 0 | grade-components 1, rewrite-neutral 1 | 0 / 2 | S1, S8 | Entry review sentence already helps; it only works when the skill is opened. |
| duplicate-binding | 2 | 2 / 0 / 0 | keep-control 2 | 0 / 0 | S1, S2 | Entry review sentence already helps; it only works when the skill is opened. |
| missing-choice | 2 | 2 / 0 / 0 | pair-variant 1, rewrite-neutral 1 | 0 / 0 | S7 | Apply the concrete media path (item, asset group, select, read back) and request-scoped picker setter. |
| motion-notification | 2 | 2 / 0 / 0 | keep-control 2 | 0 / 0 | S1 | Entry review sentence already helps; it only works when the skill is opened. |
| multiline | 2 | 1 / 1 / 0 | grade-components 1, rewrite-neutral 1 | 0 / 2 | S1, S8 | Entry review sentence already helps; it only works when the skill is opened. |
| off-permission | 2 | 2 / 0 / 0 | pair-variant 1, rewrite-neutral 1 | 0 / 1 | S7 | Apply the concrete media path (item, asset group, select, read back) and request-scoped picker setter. |
| ordinary-action | 2 | 2 / 0 / 0 | pair-variant 1, rewrite-neutral 1 | 0 / 0 | S1, S2, S8 | Entry review sentence already helps; it only works when the skill is opened. |
| player-controls | 2 | 2 / 0 / 0 | keep-control 2 | 0 / 0 | S8, S7 | Add native-control facts (Slider, Reduce Motion, selected trait) to stop rewrites of working code. |
| redundant-notification | 2 | 1 / 1 / 0 | pair-variant 1, specify-policy 1 | 0 / 0 | S1, S8 | Entry review sentence already helps; it only works when the skill is opened. |
| reentrant-submit | 2 | 2 / 0 / 0 | pair-variant 1, reserve-transfer 1 | 0 / 0 | — | Question or oracle work only. |
| selected-state | 2 | 2 / 0 / 0 | retire-duplicate 1, rewrite-neutral 1 | 0 / 1 | S1, S5 | Entry review sentence already helps; it only works when the skill is opened. |
| shortcut-dispatch | 2 | 1 / 1 / 0 | keep-control 1, repair-oracle 1 | 1 / 0 | S1, S2 | Entry review sentence already helps; it only works when the skill is opened. |
| speed-metadata | 2 | 2 / 0 / 0 | keep-control 2 | 0 / 0 | S1, S5 | Entry review sentence already helps; it only works when the skill is opened. |
| stale-off | 2 | 1 / 1 / 0 | grade-components 1, pair-variant 1 | 0 / 2 | S7, S1, S2, S3, S8 | Apply the concrete media path (item, asset group, select, read back) and request-scoped picker setter. |
| table-span | 2 | 2 / 0 / 0 | keep-control 2 | 0 / 0 | S1, S2 | Entry review sentence already helps; it only works when the skill is opened. |
| text-size-change | 2 | 1 / 1 / 0 | rewrite-neutral 1, specify-policy 1 | 1 / 1 | S1, S8 | Entry review sentence already helps; it only works when the skill is opened. |
| unavailable-media | 2 | 2 / 0 / 0 | pair-variant 1, reserve-transfer 1 | 0 / 0 | S2, S7 | Use the check shapes: second configuration, real handler, independently named fixtures. |
| validation-help | 2 | 2 / 0 / 0 | pair-variant 1, reserve-transfer 1 | 0 / 0 | — | Question or oracle work only. |
| binding-disconnect | 1 | 1 / 0 / 0 | rewrite-neutral 1 | 0 / 1 | S2, S7 | Use the check shapes: second configuration, real handler, independently named fixtures. |
| buffer-readiness | 1 | 1 / 0 / 0 | pair-variant 1 | 0 / 0 | S1 | Entry review sentence already helps; it only works when the skill is opened. |
| cancel-owner | 1 | 1 / 0 / 0 | pair-variant 1 | 0 / 0 | S1, S3 | Entry review sentence already helps; it only works when the skill is opened. |
| color-only-live | 1 | 1 / 0 / 0 | keep-control 1 | 0 / 0 | — | Question or oracle work only. |
| container-order | 1 | 1 / 0 / 0 | pair-variant 1 | 0 / 0 | S1 | Entry review sentence already helps; it only works when the skill is opened. |
| contrast-alpha | 1 | 1 / 0 / 0 | pair-variant 1 | 0 / 0 | S2 | Use the check shapes: second configuration, real handler, independently named fixtures. |
| contrast-appearance | 1 | 1 / 0 / 0 | pair-variant 1 | 0 / 0 | S1 | Entry review sentence already helps; it only works when the skill is opened. |
| contrast-space | 1 | 1 / 0 / 0 | pair-variant 1 | 0 / 0 | S1 | Entry review sentence already helps; it only works when the skill is opened. |
| cursor-restart | 1 | 1 / 0 / 0 | pair-variant 1 | 0 / 0 | S3, S6 | Apply the capture-at-install rule (return.md rewrite; actions.md AppKit and invocation-time checks). |
| custom-action-name | 1 | 1 / 0 / 0 | pair-variant 1 | 0 / 0 | S1, S2 | Entry review sentence already helps; it only works when the skill is opened. |
| description-selection | 1 | 1 / 0 / 0 | pair-variant 1 | 0 / 0 | S1, S7 | Entry review sentence already helps; it only works when the skill is opened. |
| design-font | 1 | 0 / 0 / 1 | specify-policy 1 | 0 / 1 | S2, S5 | Use the check shapes: second configuration, real handler, independently named fixtures. |
| detached-action | 1 | 0 / 1 / 0 | split-criteria 1 | 1 / 0 | S2, S3 | Use the check shapes: second configuration, real handler, independently named fixtures. |
| directional-escape | 1 | 1 / 0 / 0 | keep-control 1 | 0 / 0 | — | Question or oracle work only. |
| dismiss-reentry | 1 | 0 / 1 / 0 | split-criteria 1 | 1 / 0 | S1, S4 | Entry review sentence already helps; it only works when the skill is opened. |
| edit-action-stale | 1 | 1 / 0 / 0 | pair-variant 1 | 0 / 0 | S1 | Entry review sentence already helps; it only works when the skill is opened. |
| external-key-link | 1 | 1 / 0 / 0 | rewrite-neutral 1 | 0 / 1 | — | Question or oracle work only. |
| filter-focus-fallback | 1 | 1 / 0 / 0 | keep-control 1 | 0 / 0 | S4 | Apply the makeFirstResponder fallback and per-presentation dismissal rules; add focus trigger terms. |
| form-error-association | 1 | 1 / 0 / 0 | keep-control 1 | 0 / 0 | S8 | Add native-control facts (Slider, Reduce Motion, selected trait) to stop rewrites of working code. |
| initial-focus-once | 1 | 1 / 0 / 0 | keep-control 1 | 0 / 0 | S4 | Apply the makeFirstResponder fallback and per-presentation dismissal rules; add focus trigger terms. |
| input-snapshot | 1 | 0 / 1 / 0 | specify-policy 1 | 0 / 1 | S2, S3 | Use the check shapes: second configuration, real handler, independently named fixtures. |
| inspection-preserves-selection | 1 | 1 / 0 / 0 | pair-variant 1 | 0 / 0 | S7 | Apply the concrete media path (item, asset group, select, read back) and request-scoped picker setter. |
| key-eligibility | 1 | 1 / 0 / 0 | pair-variant 1 | 0 / 0 | — | Question or oracle work only. |
| key-link-teardown | 1 | 1 / 0 / 0 | pair-variant 1 | 0 / 0 | — | Question or oracle work only. |
| language-match | 1 | 0 / 0 / 1 | grade-components 1 | 0 / 0 | S2, S7 | Use the check shapes: second configuration, real handler, independently named fixtures. |
| live-inference | 1 | 1 / 0 / 0 | pair-variant 1 | 0 / 0 | S1 | Entry review sentence already helps; it only works when the skill is opened. |
| material-fallback | 1 | 1 / 0 / 0 | keep-control 1 | 0 / 0 | S8 | Add native-control facts (Slider, Reduce Motion, selected trait) to stop rewrites of working code. |
| motion-content | 1 | 1 / 0 / 0 | pair-variant 1 | 0 / 0 | S8 | Add native-control facts (Slider, Reduce Motion, selected trait) to stop rewrites of working code. |
| notification-kind | 1 | 1 / 0 / 0 | pair-variant 1 | 0 / 0 | S8 | Add native-control facts (Slider, Reduce Motion, selected trait) to stop rewrites of working code. |
| observer-restart | 1 | 0 / 0 / 1 | repair-oracle 1 | 0 / 0 | S2, S3 | Use the check shapes: second configuration, real handler, independently named fixtures. |
| obsolete-rotor | 1 | 1 / 0 / 0 | pair-variant 1 | 0 / 0 | S3 | Apply the capture-at-install rule (return.md rewrite; actions.md AppKit and invocation-time checks). |
| outline-expand-state | 1 | 1 / 0 / 0 | keep-control 1 | 0 / 0 | S5 | Keep and extend facts.md; single named facts produced the clearest rescues. |
| overlap-policy | 1 | 1 / 0 / 0 | pair-variant 1 | 0 / 0 | S6 | No v2 evidence; leave text-offset guidance on demand. |
| progress-bucketing | 1 | 1 / 0 / 0 | keep-control 1 | 0 / 0 | S8 | Add native-control facts (Slider, Reduce Motion, selected trait) to stop rewrites of working code. |
| redundant-hint | 1 | 1 / 0 / 0 | keep-control 1 | 0 / 0 | S8 | Add native-control facts (Slider, Reduce Motion, selected trait) to stop rewrites of working code. |
| removed-child | 1 | 1 / 0 / 0 | pair-variant 1 | 0 / 0 | S3 | Apply the capture-at-install rule (return.md rewrite; actions.md AppKit and invocation-time checks). |
| rotor-direction | 1 | 0 / 0 / 1 | repair-oracle 1 | 0 / 0 | S2 | Use the check shapes: second configuration, real handler, independently named fixtures. |
| rotor-fallback | 1 | 1 / 0 / 0 | keep-control 1 | 0 / 0 | S8 | Add native-control facts (Slider, Reduce Motion, selected trait) to stop rewrites of working code. |
| selected-vs-focused | 1 | 1 / 0 / 0 | keep-control 1 | 0 / 0 | S5 | Keep and extend facts.md; single named facts produced the clearest rescues. |
| stale-timeline | 1 | 1 / 0 / 0 | pair-variant 1 | 0 / 0 | S2 | Use the check shapes: second configuration, real handler, independently named fixtures. |
| stale-tree-node | 1 | 0 / 1 / 0 | split-criteria 1 | 1 / 0 | S2, S3 | Use the check shapes: second configuration, real handler, independently named fixtures. |
| status-no-focus-theft | 1 | 1 / 0 / 0 | keep-control 1 | 0 / 0 | S4, S8 | Apply the makeFirstResponder fallback and per-presentation dismissal rules; add focus trigger terms. |
| unlisted-selection | 1 | 1 / 0 / 0 | pair-variant 1 | 0 / 0 | S7 | Apply the concrete media path (item, asset group, select, read back) and request-scoped picker setter. |
| visible-name-alignment | 1 | 1 / 0 / 0 | keep-control 1 | 0 / 0 | S5 | Keep and extend facts.md; single named facts produced the clearest rescues. |
| voice-command-name | 1 | 1 / 0 / 0 | keep-control 1 | 0 / 0 | S5 | Keep and extend facts.md; single named facts produced the clearest rescues. |
<!-- tier3:end -->

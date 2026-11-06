# Claude Haiku versus AGY — same frozen accessibility baseline

**The skill improved gold and evidence scores, but cost 2.90× the tokens and slightly reduced exploratory-code scores. All 84 Claude conversations completed.** C0 = no skill; C2 = frozen skill 0.2.2 plus evaluator-selected reference. Claude model `claude-haiku-5-5`, low effort, subscription CLI. AGY: `gemini-3.8-flash-low`, low effort. Same 84 serialized prompts, three samples per code case, same source-review rubric. No model judge or native generated-code execution.

## Results at a glance

| Source-review measure | AGY C0 | AGY C2 | Haiku C0 | Haiku C2 |
|---|---:|---:|---:|---:|
| Existing gold code | 13/18 | 15/18 | 13/18 | 16/18 |
| Exploratory code | 12/18 | 13/18 | 15/18 | 14/18 |
| Evidence questions | 4/6 | 4/6 | 4/6 | 6/6 |

A core pass is not a flawless answer: optional incorrect recommendations and unnecessary changes are separately flagged. Passing fixtures do not qualify generated answers. These are single-reviewer, unblinded source assessments; independent calibration and native checks remain pending.

## Tokens — all 84 conversations for each model

The earlier AGY report showed tokens for 72 new calls. This table also includes its 12 earlier gold calls so the comparison has equal sample counts.

| Token measure | AGY C0 | AGY C2 | Haiku C0 | Haiku C2 |
|---|---:|---:|---:|---:|
| Logical input | 95,515 | 199,704 | 41,230 | 205,046 |
| Output, including reported thinking | 19,104 | 25,751 | 64,830 | 102,710 |
| Total | 114,619 | 225,455 | 106,060 | 307,756 |


**Latency:** C0 mean 9.56s, median 9.07s; C2 mean 12.48s, median 12.62s. Summed call duration: 925.73s (15m26s).

### Claude cache accounting

| Measure | C0 | C2 |
|---|---:|---:|
| Uncached input | 84 | 84 |
| Cache read | 14,738 | 105,086 |
| Cache write | 26,408 | 99,876 |
| Output | 64,830 | 102,710 |
| Thinking (already included in output) | 33,922 | 61,070 |

Logical input = uncached input + cache read + cache write. Total = logical input + output. Thinking is a subset of output and is **not added again**. These are provider-reported categories, not independently tokenized counts. Cache reuse and different CLI wrappers limit cross-provider cost conclusions. No actual dollar charge is inferred from an API-equivalent estimate. The account quota snapshot is recorded privately; a matched final quota observation is unavailable, so quota debit remains unknown.

### Tokens per source-review pass

This divides **all tokens in the lane, including failed answers**, by the number meeting its criteria. It measures this sample, not expected production cost.

| Lane | AGY C0 | AGY C2 | Haiku C0 | Haiku C2 |
|---|---:|---:|---:|---:|
| Gold | 3,726 | 6,269 | 3,250 | 7,833 |
| Exploratory | 4,298 | 7,555 | 3,680 | 10,029 |
| Evidence | 3,649 | 8,304 | 2,152 | 7,004 |

## Each code task

| Task | AGY C0 | AGY C2 | Haiku C0 | Haiku C2 |
|---|---:|---:|---:|---:|
| GP26-01 · Settings switch and Help | 3/3 | 3/3 | 3/3 | 3/3 |
| GP26-02 · Reused-cell customer/status | 3/3 | 3/3 | 2/3 | 3/3 |
| GP26-03 · Large text with Pay appearance preserved | 1/3 | 0/3 | 0/3 | 1/3 |
| GP26-04 · Deletion without swipe | 3/3 | 3/3 | 2/3 | 3/3 |
| GP26-05 · tvOS tile navigation | 3/3 | 3/3 | 3/3 | 3/3 |
| GP26-06 · Already-correct Toggle | 0/3 | 3/3 | 3/3 | 3/3 |
| GP26-07 · Asynchronous dismissal focus target | 3/3 | 3/3 | 3/3 | 3/3 |
| GP26-08 · Popup state restoration | 3/3 | 3/3 | 3/3 | 3/3 |
| GP26-09 · Adjustable custom knob | 3/3 | 3/3 | 3/3 | 3/3 |
| GP26-10 · Progress and terminal-event deduplication | 3/3 | 3/3 | 3/3 | 3/3 |
| GP26-11 · Already-correct Slider | 0/3 | 1/3 | 0/3 | 0/3 |
| GP26-12 · Existing reduced-motion behavior | 0/3 | 0/3 | 3/3 | 2/3 |

[Actual gold prompts and code](../../../GoldPrompts.md) · [Exploratory prompts and code](../../os26/expansion-1/PROMPTS.md) · [Earlier AGY report](../agy-expanded-20261105/README.md)


## Evidence questions at a glance

Each answer needs all four frozen checklist items to pass.

| Question | Haiku C0 | Haiku C2 |
|---|---:|---:|
| Can a screenshot prove a Pay button works with VoiceOver? | 4/4 | 4/4 |
| Do 12 clean label/contrast checks justify fully accessible release notes? | 3/4 | 4/4 |
| Can unavailable documentation establish exactly-once activation? | 4/4 | 4/4 |
| Can a forum post justify removing a payment workaround? | 4/4 | 4/4 |
| Does testing simulator26.5 establish26.0 and all later versions? | 4/4 | 4/4 |
| Does a direct delete-handler test prove keyboard/VoiceOver activation? | 3/4 | 4/4 |

<details>
<summary>Expand per-answer reviewer findings (all 84 answers; full responses remain private)</summary>

Summaries below are reviewer findings, not generated transcripts.

### GP26-01

- **C0 r1 · meets** — Restores both controls, preserves callbacks, optional help hint marked adjustable; explicitly requires actual VoiceOver verification.
- **C2 r1 · meets** — Minimal container/name fix preserves distinct actions; predicted speech sequence and causal explanation exceed what snippet alone establishes.
- **C0 r2 · meets** — Replacement removes hidden flag and retains independent controls; default false works for newly constructed stack. Optional title stop accepted.
- **C2 r2 · meets** — Restores container exposure, labels switch, preserves callbacks and explicitly says native interaction untested.
- **C2 r3 · meets** — Restores both controls, names switch, keeps callbacks. Separate-title alternative allowed, despite unnecessary wording preference.
- **C0 r3 · meets** — Restores both controls and current name; optional hint adds little; no interaction run claimed.

### GP26-02

- **C2 r1 · meets** — Unconditional current label/value with supplemental reset. Explicitly distinguishes guideline support and UIKit inference.
- **C0 r1 · meets** — Writes current label/value on every configure; prepareForReuse is supplemental, not substitute.
- **C2 r2 · meets** — Unconditionally sets current customer/status; supplemental reset, no stale branch.
- **C0 r2 · material-gap** — Primary nonpriority branch clears status instead of exposing current processing value required by frozen reconfiguration criterion. Mentions optional current status but primary fix drops it; subview fallback not demonstrated.
- **C0 r3 · meets** — Unconditional current label/value; reset explicitly defensive, repeated configure works.
- **C2 r3 · meets** — Unconditional current label/value; extra init overrides are unnecessary and categorical placement advice overstates requirement, but primary core preserved.

### GP26-03

- **C0 r1 · material-gap** — Correct scaling/wrapping intent but local summary/updateSummaryAxis then self.updateSummaryAxis in registered callback is inconsistent scope, as in AGY failure. Notes also confuse distribution fill with alignment despite center set. No silent member-property repair.
- **C2 r1 · material-gap** — Keeps Pay styling and fixes label, but local summary in replacement and separate controller member updateSummaryAxis referencing summary require undeclared storage/integration. Same frozen no-silent-repair standard; not a native compiler result.
- **C0 r2 · material-gap** — Keeps Pay appearance and enables wrapping/scaling, but offers font shrinking for long unbroken totals instead of a usable reflow path; largest-size/long-total requirement remains unresolved.
- **C2 r2 · material-gap** — Provides dynamic axis callback but local summary and separate controller methods have undeclared storage integration; stretches Pay full-width and adds height constraint despite appearance preservation.
- **C2 r3 · meets** — Explicit stored summary reference, initial apply and trait callback resolve prior scope problem; Pay font/config unchanged. Vertical fill can change button width, so rendered appearance still needs validation; unused arranged-subview removal unnecessary.
- **C0 r3 · material-gap** — Scaling/wrapping primary still horizontal; optional trait handler references local summary and has no initial accessibility-size update. Largest-size requirement not concretely integrated.

### GP26-04

- **C2 r1 · meets** — Button and retained drag satisfy core. Blanket gesture no-double-delete guarantees and claim a row action would necessarily duplicate button semantics are unsupported.
- **C0 r1 · meets** — Native delete button retains callback message and drag threshold; no focus activation. Exact Tab/Space/Return behavior predicted, not tested.
- **C2 r2 · meets** — Native button and same message callback/drag satisfy core. Unverified guarantees for gesture mutual exclusion and Tab/Space/Return; blanket custom-action duplication reasoning.
- **C0 r2 · material-gap** — Primary iPadOS snippet adds onDeleteCommand, which Apple documentation lists macOS10.15+ only; no availability guard. Optional removal of visible button would also lose requested keyboard path. Apple source saved privately; no compile run.
- **C0 r3 · meets** — Explicit button and named action plus same drag callback meet source core. Optional unscoped Delete shortcut repeated per row risks ambiguous targeting; model flags conflicts but no validation.
- **C2 r3 · meets** — Explicit button with message callback preserves deletion and drag; wrongly equates separate-element custom action with duplicate same-element action. VoiceOver left-swipe test is not evidence of app drag delivery.

### GP26-05

- **C0 r1 · meets** — Uses native button and same movie callback/title; adds layout/style changes and broad reachability guarantee without native test.
- **C2 r1 · meets** — Native button preserves movie action/title and correctly separates requested runtime verification from repository guidance. Additional image sizing optional.
- **C0 r2 · meets** — Native button with same movie/title meets core; unrelated LazyHStack/layout/line limit changes increase burden. No actual native claim.
- **C2 r2 · meets** — Native button/correct movie/title core; adds line limit/style/layout without necessity and predicts universal reachability.
- **C2 r3 · meets** — Native button correct movie/title, optional first-tile focus sample is explicitly contextual and requires SDK verification; no actual remote run claimed.
- **C0 r3 · meets** — Native button correct movie/title meets core. Extra layout and line limit; blanket LazyHStack no-focus-impact claim not established.

### GP26-06

- **C2 r1 · meets** — Preserves valid native Toggle and store binding; no invented defect. Opening accessible as written is broader than source-only evidence but verification is requested.
- **C0 r1 · meets** — Recognizes native Toggle already accessible and preserves binding. Optional footer asserts unprovided notification scope in example but explicitly says adjust to actual preference; unnecessary review burden rather than automatic core failure under equivalent-implementation rule. Borderline for independent review.
- **C2 r2 · meets** — Explicit no-change answer preserves native state semantics and binding; distinguishes optional polish and asks verification.
- **C0 r2 · meets** — Acknowledges native Toggle already accessible and preserves binding. Footer/title are unnecessary polish with parent uncertainty, not automatic core failure; no redundant semantic override.
- **C0 r3 · meets** — Recognizes valid native semantics and unchanged binding. Optional redundant hint/footer/title and assumed notification scope explicitly caveated; burden not automatic core failure.
- **C2 r3 · meets** — No semantic changes; optional hint conditional on actual non-obvious behavior, avoids fabricated app facts.

### GP26-07

- **C2 r1 · meets** — Resolves current ID in dismissal completion with fallback; no guessed delay/payment change. Extra visibility checks redundant under supplied map contract; actual focus not verified.
- **C0 r1 · meets** — Current-ID lookup in dismissal completion, fallback and weak captures; no delay or payment change. Distinguishes notification choice from proven focus.
- **C0 r2 · meets** — Resolves map in dismissal completion, fallback and no guessed delay/payment change. Scoped Done-only behavior explicit.
- **C2 r2 · meets** — Clears closure and resolves current map/fallback inside dismissal completion; no guessed delay. Focus outcome remains proposed verification.
- **C2 r3 · meets** — Current-ID helper called only at dismissal completion, persistent fallback and no guessed delay; no payment edits. Containment implications still need actual verification.
- **C0 r3 · meets** — Current map/fallback inside actual dismissal completion, weak captures, no delay/payment change. Post-dismiss focus phrasing not runtime evidence.

### GP26-08

- **C0 r1 · meets** — Optional Bool sentinel preserves false/true state, idempotent lifecycle and modal popup descendants. Notification target not proven actual focus.
- **C2 r1 · meets** — Idempotent show/close saves and restores prior hidden state, modal container preserves children. Focus notifications are assumptions, not evidence; code correct for scoped flag contract.
- **C2 r2 · meets** — Correct idempotent save/restore and modal state, preserves descendants/Close. Explicitly does not invent focus anchor.
- **C0 r2 · meets** — Explicit open guard preserves pre-open hidden flag including true, leaves Close/container intact. Container notification can target hidden content after restore; not proof of focus.
- **C0 r3 · meets** — Optional Bool sentinel preserves pre-open flag and repeated calls harmless; modal container/Close unchanged. Some cleanup before close guard remains idempotent under supplied ownership.
- **C2 r3 · meets** — Guarded show/close restores exact prior flag, modal descendants/Close preserved; generic notification is not proof of requested focus and verification should allow prior hidden true.

### GP26-09

- **C2 r1 · meets** — Real increment/decrement overrides use common clamped setter; computed current value covers initial state, no-change callbacks suppressed, drag and no announcements preserved.
- **C0 r1 · meets** — Real adjustment overrides step5 via shared clamped setter; initial/current value, changed-only callback, drag and no announcements preserved.
- **C0 r2 · meets** — Computed label/value/traits and real adjustment hooks preserve step/clamp/callback contract and drag. Empty property setters acceptable scoped alternative; native compile pending.
- **C2 r2 · meets** — Correct initial and changed value, shared clamped setter and real hooks; boundary prose broadly says increment or decrement at either bound, but code and verification specify correct directions.
- **C2 r3 · meets** — Computed current value, real adjustment hooks, step5/clamping/changed-only callback and original drag preserved; app posts no announcements.
- **C0 r3 · meets** — Correct actual adjustment overrides, common clamp/no-change setter and initial/current values; extra gesture hint redundant, no announcements or drag regression.

### GP26-10

- **C0 r1 · meets** — Active-ID/terminal guards, begin reset, clamped accessible progress and first-terminal-only announcements. MainActor appropriate to supplied main-thread context.
- **C2 r1 · meets** — Correct ID/terminal guards, reset, clamp, silent progress and first terminal announcement; explicitly recognizes manually supplied SwiftUI reference for UIKit.
- **C2 r2 · meets** — Terminal-text sentinel correctly gates duplicate/late callbacks; new begin resets, progress clamped and silent, shared displayed/value state.
- **C0 r2 · meets** — Correct ID and first-terminal guards, reset, clamped value updates and terminal-only announcement. Explicit source-only qualification.
- **C0 r3 · meets** — Correct current-ID and per-branch terminal guards, reset/clamp/value updates, terminal-only announcement. Absolute statement about spontaneous value speech exceeds tested evidence; no code failure.
- **C2 r3 · meets** — Correct ID/terminal guards, reset/clamp/silent progress. Invents an extra defect about terminal value replacing percent, then keeps same behavior; code meets actual requirements.

### GP26-11

- **C2 r1 · material-gap** — Invents explicit-value requirement for native Slider and asserts default lacks useful state without evidence. Later admits default and percent are assumptions; does not retract unsupported finding.
- **C0 r1 · material-gap** — Fabricates native Slider bare-number deficiency and mandatory safe fix; additionally false claim rounded avoids Int conversion failure for nonfinite values.
- **C0 r2 · material-gap** — Calls unobserved native value output a concrete bare-number defect and asserts unit without evidence. Preserves binding/range but fails requested defect grounding.
- **C2 r2 · material-gap** — Asserts native Slider lacks meaningful value, then admits assumed bare-number output is unsupported by SwiftUI source. Verification request does not establish claimed concrete defect.
- **C2 r3 · material-gap** — Treats absent explicit accessibilityValue as defect for native Slider, despite acknowledging default output undocumented. Preserves controls but fails evidence-grounded no-defect criterion.
- **C0 r3 · material-gap** — Calls unverified native Slider bare-number output an accessibility problem; hard-coded percent fix without demonstrated defect. Later uncertainty does not establish the finding.

### GP26-12

- **C0 r1 · meets** — Correctly recognizes nil animation under supplied no-ambient-transaction assumption; preserves live preference/page/content and recommends no change. Distinguishes optional fade design from defect.
- **C2 r1 · meets** — Correct no-change conclusion preserves supplied nil-animation behavior and state. Optional explanation confuses identity with fade and claims conditional identity would change motion-enabled slide; no such change actually recommended.
- **C2 r2 · material-gap** — Invents hard-cut/no-transition as concrete accessibility defect despite supplied guidance explicitly allowing immediate state updates. Replaces valid nil animation with fade; live state preserved but no demonstrated defect.
- **C0 r2 · meets** — Correct no-change core, live preference/state explained. Optional opacity-only snippet still uses nil animation and would not create proposed fade; explicitly optional design rather than defect.
- **C0 r3 · meets** — Correct no-change core: live environment, preserved page, nil animation and unchanged navigation. Distinguishes possible external issue from supplied snippet.
- **C2 r3 · meets** — Correct no-change core explicitly applies supplied no-parent-animation assumptions, preserves live preference/page/content; optional polish is not framed as defect.

### EV01

- **C0 r1 · meets** — Rejects screenshot proof and specifically requires both semantics and actual VoiceOver activation evidence; no absent evidence inspection claimed.
- **C2 r1 · meets** — Requires hierarchy semantics plus a VoiceOver reach/announce/activate pass; unsupported screenshot claims remain unverified.

### EV02

- **C2 r1 · meets** — Accurate spot-check wording preserves12elements/two checks/zero findings and names untested areas without invented work.
- **C0 r1 · material-gap** — Correctly bounds 12-element label/contrast audit and names missing checks, but proposed release note invents accessibility improvements in this release; report only states checks/no findings.

### EV03

- **C0 r1 · meets** — Does not claim missing document access; exactly-once behavior remains unverified and requests source/docs/actual invocation test.
- **C2 r1 · meets** — Leaves missing-doc claim unverified; requests source and one-activation cardinality with no focus/navigation invocation.

### EV04

- **C2 r1 · meets** — Requires exact build/reproduction, supported range and payment activation evidence; no fabricated fix. Long workflow record beyond minimal plan.
- **C0 r1 · meets** — Rejects anecdote, asks exact builds/reproducer and payment regression, no invented official fix. Every build plus one/two releases exceeds smallest plan; Inspector/XCUITest not equivalent to actual VoiceOver interaction.

### EV05

- **C0 r1 · meets** — Distinguishes SDK/deployment/runtime and selected unit scope; correctly rejects26.0/alllater claim. Rewrite later versions is ambiguous because26.5 was tested; should say other untested versions.
- **C2 r1 · meets** — Preserves selected tests on26.5 and separates deployment/SDK/noUI. Rewrite26.0 and later versions unverified needs other untested versions qualifier to avoid implying26.5 had no test.

### EV06

- **C2 r1 · meets** — Preserves compile/directB-once result and explicitly distinguishes UI wiring, semantic discovery and actual keyboard/VoiceOver input evidence.
- **C0 r1 · material-gap** — Correctly distinguishes handler and UI wiring, requests actual keyboard activation, but proposed VoiceOver evidence is audit/hierarchy ideally enabled plus reachability, not an explicit activation-path test. Same interaction-evidence standard as screenshot case.

</details>

## Interpretation

- **Gold:** the skill helped with cell state and deletion, and one checkout answer supplied the missing stored view reference. Haiku still has no native generated-code validation.
- **Valid controls:** both conditions preserved the Toggle core in all three samples; C0 added optional footer/hint/title changes, marked as burden rather than automatic failure because they were qualified. Both invented a Slider defect in all three samples.
- **Reduced motion:** C0 correctly recommended no change in 3/3; C2 did so in 2/3 and invented a need for a fade once.
- **Evidence:** C2 met all six checklists. C0 invented release improvements in one audit summary and omitted an explicit VoiceOver activation check in another. Borderline wording is retained in the notes.
- **Efficiency:** the larger C2 prompt and longer output—including measured thinking—did not buy a uniform quality improvement. Candidate work should prioritize grounded no-change decisions, platform availability, scope preservation and a smaller instruction/reference payload.

The wrong-platform deletion modifier was checked against [Apple’s onDeleteCommand reference](https://developer.apple.com/documentation/swiftui/view/ondeletecommand(perform:)), which lists macOS availability. No local Apple compiler result is claimed.

## Qualification and next steps

No application retries, fallback models, tool use or extra provider experiments were requested. All84original prompt/output hashes and receipts were checked. CLI-internal transport retries are not independently measured. Every call reported the pinned Haiku model and one turn. Output length was a 1024-token target, not a hard cap; measured output includes reasoning-token counts when supplied. No reasoning text is reproduced.

The skill/reference condition tests manual injection, not autonomous retrieval. Primary code may meet core while optional advice is wrong. Borderline judgments are marked for independent review. New cases remain exploratory. This is a baseline for developing a compact candidate; it does not qualify release quality or establish statistical superiority.

**Assistant next:** obtain independent/native validation of disputed outputs and prepare one focused skill revision with a fresh heldout comparison plan. **Owner next:** review the summary; any further subscription campaign needs explicit approval. No additional calls are started by this report.

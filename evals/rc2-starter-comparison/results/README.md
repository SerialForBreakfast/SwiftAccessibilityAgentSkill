# Local grading: receipt 1531

**Diagnostic development comparison, not a promotion gate.** The expected first return was partial (receipt 1533, one answer). Receipt 1534 supplied the consolidated 16-answer bundle. The earlier stop was an AGY executable change, a stop condition in the handoff. The worker used a pinned 1.5.5 binary to continue; the first session logged version 1.5.5 but not its executable hash. No new authorization is evidenced in these returns. Treat the full panel as diagnostic rather than a strictly uninterrupted, transport-qualified run. Only the original first cell predates the stop; by itself it makes no pair.

Local checks: both outer SHA-256s match coordinator notices; every indexed archive member matches its hash; all original cell-1 artifacts are byte-identical; the embedded held ZIP equals the published packet. All 16 installed trees (including project files), prompt bytes, skill hashes, first-answer freezes and masked Swift fences matched the scheduled cells. One attempt per cell; worker reported zero incremental spend. Skill reads: 16/16; starter source reads: 15/16 (missing: rc.2 Mac media). One sample per arm on eight related development cases. Not an independent blinded panel: local review used returned source and toolchain diagnostics. No new model calls.

## Rubric decisions

P = meets this question's primary requirement; F = material failure; ? = unestablished. Columns separate primary, ordinary-path preservation, integration, requested verification, and unnecessary rework. Whole pass requires all material requested outcomes. Grading is against the **revised question**, including its explicit fixture instructions. A passing suite does not compensate for unconnected screen wiring. Preservation refers to the identified interaction, not every possible app behavior.

| Case / arm | Primary | Preserve | Integrate | Verify | Rework | Whole | Decisive evidence |
|---|---|---|---|---|---|---|---|
| 4840 release | P | P | P | P | P | Pass | Registration passes its captured ticket; installed A late then B twice produces only B. |
| 4840 rc.2 | P | P | P | F | P | Fail | Same ownership fix, but the separate test file uses SwiftUI Binding without importing SwiftUI. |
| 4ec9 release | P | P | P | P | P | Pass | Mounted task loads actual group, picker selects on the item, reports absent versus failed, Retry reloads and answer identifies external reload triggers. Missing item is reported as a failure with its own message; an invalid non-nil ID also falls through to Off (robustness risk, not a requested ordinary choice). |
| 4ec9 rc.2 | F | ? | F | F | P | Fail | Media option is optional but its extendedLanguageTag and displayName are accessed without unwrapping; no usable integrated picker. Nil item and absent group both map to empty. |
| 5d12 release | F | F | F | F | P | Fail | Picker binds directly to writable selection, not choose; manual test calls bypass it. Uses unavailable mediaSelectionGroup(for:) spelling in the source. |
| 5d12 rc.2 | P | F | F | P | P | Fail | Correct native writes, unlisted forced option and stale binding checks once load() is called. Neither CaptionScreen nor initialization starts that load. The ordinary picker cannot present loaded choices as supplied. |
| 6d2d release | F | F | F | ? | P | Fail | Init only stores the player; the supplied screen never calls load(). Tests do. choose assigns the displayed ID before validating membership. |
| 6d2d rc.2 | P | P | P | F | P | Fail | Screen actually loads and writes to the item, preserves unlisted choice, checks Off. Both tests open the forced seed; the expressly requested independent ordinarily seeded item is missing. This is a partial rescue, not a whole pass. |
| c04c release | F | F | F | F | P | Fail | Load generation is guarded but the installed picker setter calls choose on current state; stale Off can clear the replacement. |
| c04c rc.2 | F | F | F | F | P | Fail | Captures item and request in currentBinding, a real improvement after explicit reload. choose and isCurrent compare against cached currentItem, not player.currentItem; only the test couples external replacement to reload. Neither an unreloaded replacement nor a superseded same-item request is demonstrated by the submitted tests. |
| c6b2 release | F | F | F | F | P | Fail | Installed setter calls choose($0) without the issuing request. Replacing the item in a test does not exercise a retained Off from before a same-item reload. |
| c6b2 rc.2 | F | F | F | F | P | Fail | Provides optional item/request arguments but the installed setter omits both. Supplying an explicitly wrong UUID in the cancellation test bypasses the faulty ordinary wiring. |
| da78 release | P | P | P | P | P | Pass | Installed callbacks retained separately; old A and repeated B cannot make a second restoration request. |
| da78 rc.2 | P | P | P | P | P | Pass | Replaces only SheetHost, captures ticket at presentation, and relies on this starter's existing generation guard; the submitted Swift Testing test uses actual registrations. |
| f483 release | F | ? | F | F | P | Fail | Async call in synchronous context prevents integration. Installed setter also routes through current state. |
| f483 rc.2 | P | ? | P | F | P | Fail | Better binding captures the emitting item and generation. Submitted tests invent CaptionFixture.makeItem instead of the packaged open(selected:) API. No native stale-Off proof. |

No new source-level loss of the ordinary Open/Close actions, player controls, or ordinary audio selection versus a working release counterpart was established. The rc.2 iOS picker compile regression *does* make an otherwise available caption-selection interface unusable as submitted. Distinguish that from observing loss of playback, touch delivery, or focus in a running UI.

One fixed-seed pair per question, not eight independent measures of transfer. Reported tokens: release 279,726; rc.2 215,901 (22.8% fewer). Private raw answers and controller evidence remain under evals/results/1531-review; no published frozen skill or prior grades were edited.

**Result:** 0.2.2 passed 3/8 and rc.2 passed 1/8. Zero whole-task gains, two losses, one preserved pass and five persistent failures. Seven submitted suites ran locally on the project fixtures: all 14 executed methods passed. Other cells were settled by target compiler diagnostics or material source-level omissions. The direct compiler’s Swift Testing plugin diagnostic is not a submission error: Xcode ran cell 14 successfully. Cell 15 independently references a nonexistent fixture method. [Per-cell grades, hashes and native observations](grades.json).

# rc.1 vs 0.2.2: return intake, November 7, 2026

**Status:** received and verified. The sealed comparison is **partial**.
- **Quality:** no measured difference between versions. Native grading found one task, checkout-font, that both versions fail; the source review had passed it.
- **Invocation:** rare for both versions.

Every number below is checked by `python3 -B evals/rc1-comparison/verify_return.py` against private copies of the bundles in ignored `evals/results/rc1-return-20261107/bundles/`.

## What arrived

BigDog delivered three bundles to the shared return folder (`SharedStatusFile/joe-big-dog/`). The receipt cursor (1450) was not checked against the coordinator; no coordinator call was made.

| Bundle | SHA-256 | What it is |
|---|---|---|
| `rc1-release-native-36-v1-return.zip` | `77f942cd…80fa` | **The sealed run.** All 36 prompt hashes match [packet.json](packet.json). Status partial: 9 completed, 1 attempt error, 26 unattempted. |
| `rc1-release-native-chat-36-v2-return.zip` | `9f7d0cea…4cad` | **A second job.** 36/36 completed, but 0/36 prompt hashes match the sealed packet. BigDog's derived `controller/packet.json` (`46d576c8…`) names our packet (`496c51e0…`) as parent. |
| `rc1-failure-replay-handoff-return.zip` | `4f08fcc6…bae8` | A **proposal**, not results: 7 explicit rc.1 replays of historical unaided-Haiku failures. Received, not dispatched. |

All internal checksums match.

## Protocol deviation

The [handoff](HANDOFF.md) asked for one job and one return, with no retries, and said an attempted cell consumes its slot.

**What happened in v1:**
- Cell C10 tried a `Write` in the read-only session. The sealed task wording "Return only Submission.swift" invites writing the file.
- The harness then stopped on "Unsupported tool call".

**What v2 changed:**
- BigDog rewrote the reply instruction to "Paste only the complete Swift source in your final chat response. Leave all files unchanged…".
- It reran **all 36 cells in new sessions**, including the 9 completed in v1.
- v2 itself stopped after 9 sessions on a quota-read error. The other 27 ran as a "continuation".

**Consequences:**
- v1's 9 completed cells are the sealed first attempts.
- v2 is a separately prompted cohort, so it is development evidence rather than the sealed comparison.
- It is still internally paired: same prompts for both arms, no cell repeated within v2.
- The prompt change is a real fix to the task interface. It should be adopted in the next packet, not repeated as an unplanned rerun.

## Answer quality

| Cohort | Automatic pairs | Both pass | Gains | Losses | Incomplete |
|---|---:|---:|---:|---:|---:|
| v1 (sealed) | 12 | 4 | 0 | 0 | 8 |
| v2 (rewritten prompt) | 12 | 12 | 0 | 0 | 0 |

**Other quality observations:**
- In v2, every cell meets the source contract in both arms and in the explicit lane.
- The six fresh 0.2.2 repeats all agree with their first verdicts.
- No critical losses.
- 0/36 answers follow the raw-Swift output format. Each wraps the code in a Markdown fence with prose.
- 36 answers reduce to only 22 distinct Swift files.

**These tasks have no headroom.** Each is a 3–15-line function, and the prompt states the rule. For example, checkout-layout's prompt says to stack "at every accessibility size". The answer is `size.isAccessibilitySize`, written in about 4 seconds without loading the skill. A suite every arm passes can't show whether the skill helps.

What models have actually failed are realistic tasks. Unaided Haiku failed GP26-03 (checkout layout with Pay appearance preserved) in 4/4 graded attempts and GP26-11 (an already-working Slider) in 4/4. The failure-replay bundle lists those.

## Invocation, separately from quality

| v2 lane | 0.2.2 invoked | rc.1 invoked | rc.1 extra once invoked |
|---|---:|---:|---|
| Automatic first answer | 1/12 | 1/12 | reference read 1/1, announced and routed 1/1 |
| Automatic repeat (0.2.2 only) | 0/6 | – | – |
| Explicit ("Use the installed … skill") | 3/3 | 3/3 | reference reads 3/3 (0.2.2: 0/3); announced and routed 3/3 |

- **The sealed run:** v1 auto-invoked 0 of 9 completed sessions.
- **checkout-font is the only task that ever auto-invoked.** Across both jobs, 0.2.2 invoked on it 1 of 3 times and rc.1 1 of 2 times.
- **No other task invoked automatically,** in either arm.

So:
1. The developer's normal workflow almost never loads either version on these prompts.
2. When asked explicitly, both always load.
3. Only rc.1 then retrieves its references and reports its route.

rc.1's content routing works. Neither description triggers.

Because the skill isn't loaded, most automatic sessions test the base model, not the skill. That gives a second reason the automatic pairs tie.

## Grading limits

**How v2 was graded:**
- One coordinator reviewed masked, shuffled source.
- The coordinator has prior exposure to the protocol.
- There was no second rater, and BigDog executed no Swift (its host is Linux). The native grades below were run here afterwards.

## Native grading (reviewed local lane, this Mac)

**Setup:**
- Each answer's Swift block was extracted unchanged and read before running: 22 distinct files across 36 cells.
- Each file was approved by hash and passed the screen.
- All 36 were graded through the [reviewed local lane](../rc1/README.md) with [native_lane.py](native_lane.py).
- Environment: iOS and tvOS 26.5 unit simulators, macOS host, deployment target 26.0.
- Outcomes are in ignored `evals/results/rc1-return-20261107/native.json` with one scorecard per cell.

**Run record:**
- The first lane invocation crashed after grading C01. Its scorecard parser couldn't handle the space in the repo path.
- C01's attempt directory is kept.
- The full lane was then run once.

| Task | Cells | Native | Source review |
|---|---|---|---|
| checkout-font (iOS UIKit) | C01 0.2.2, C02 rc.1, C25 0.2.2 repeat | **contract failure 3/3** | meets 3/3 |
| other 11 tasks | 33 | pass 33/33 | meets 33/33 |

**Why checkout-font fails:**
- All three answers scale the supplied font for the supplied traits *and* set `adjustsFontForContentSizeCategory = true`.
- With that flag, UIKit rescales the font to the label's own trait environment and drops the requested size.
- A probe in `evals/results/rc1-return-20261107/probe-checkout-font/` shows it on the iOS 26.5 simulator: 17.0 pt where accessibility XL should be 37.0 pt. The reference and the accepted alternative don't set the flag.

**Classification:** a real contract failure, not an oracle defect. The prompt asks for the font "at the given text-size setting", and the label ignores that setting.
- The source reviewer missed it. That supports making native outcomes the primary grade.
- Both versions fail, including C01 and C02, where the skill **was** invoked. In C02, rc.1 also read `checkout-uikit.md`. Neither skill version warns against combining explicit trait scaling with automatic adjustment.
- That makes this a measured content gap with headroom: 3/3 failed.

**Paired result with native grades:** checkout-font is both-fail, and the other 11 automatic pairs are both-pass. Still no gains or losses between versions.

**Grader check after the gate change:**
- Fixture qualification on a warm simulator passed: 24 references and alternatives pass, 12 mutants fail.
- `verify.py --receipt` accepts it (`evals/results/rc1-grader/attempt-59pnz5d5/`).
- Two earlier qualification attempts stopped on the first post-boot iOS launch, which exceeded the 40-second timeout. The fixture binary later took 2 min 46 s cold and 8–16 s warm. That is infrastructure, not a grade.

## What can and cannot be concluded

**Supported:**
- rc.1 shows no answer-quality difference from 0.2.2 on these 12 tasks.
- Both versions miss the checkout-font contract. In both, the auto-adjust flag overrides the supplied traits.
- rc.1 retrieves references when loaded; 0.2.2 doesn't.
- Automatic invocation is rare for both.

**Not supported:**
- Whether either version improves on unaided Haiku. Neither run had an unaided arm.
- Noise between repeated runs. The six agreeing repeats all sit at the ceiling.
- Rendered behavior. Units check properties, not the screen.
- Results on realistic tasks or other models.
- Any release decision.

**Recommendation:** don't promote rc.1, and don't start a dev.9 on this result. The next steps are in [ROADMAP-0.3.md](../../ROADMAP-0.3.md).

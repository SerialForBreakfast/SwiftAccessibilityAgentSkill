# Recommendation schema: one record per Tier 1 or Tier 2 prompt

`shards/tier1.json` and `shards/tier2.json` are JSON arrays with exactly one object per item in `items.json` of that tier. Each recommendation has two sides: the **question** (and its oracle) and the **skill** (what content, routing or check would close the gap). Ground every field in the item's evidence; no generic advice.

| Field | Type | Contents |
|---|---|---|
| `id` | string | P-… for Tier 1; GP26-0N or the gold-parity scenario id for Tier 2 |
| `gapType` | enum | The main reason the developer outcome is wrong or unmeasured (below) |
| `diagnosis` | string, 1–3 sentences | What the evidence shows. Cite it: "v2: unaided fail/skill pass, read actions.md", "384: pass with no headroom", "gates: 2 mutants killed", "parity: 3 review-only criteria". |
| `questionChange` | string | What to change in the developer request and why; "none" when the question is sound. |
| `proposedWording` | string or null | Required when `questionChange` is not "none". Replacement developer request (opening plus stated policy facts). Never states the rule under test or the expected fix. |
| `oracleChange` | string | What the criterion, rubric or hidden test should check differently; "none" if right. Name observable effects and components. |
| `skillChange` | string | The content change that would close the gap: card name and the decision-point contrast, check shape or fact to add, or the sentence to remove. "none" for a sound control. |
| `routingChange` | string | Description or routing-cue change needed for the skill to be opened on this question; "none" if it was opened or would be. |
| `v3Covers` | enum | `yes`, `partial`, `no`, `n/a`: whether the untracked signal-v3 draft already makes this skill change. |
| `priority` | `P0`–`P3` | P0: a critical or harmful-instruction finding, or an oracle defect that corrupts counts. P1: a high-reach content or routing fix. P2: useful. P3: keep. |
| `confidence` | `high`, `medium`, `low` | |

**`gapType` values:**

| Value | Meaning |
|---|---|
| `harmful-instruction` | The skill was read and its wording plausibly caused or endorsed the failure |
| `content-gap` | The skill was read but lacks the decision-point contrast, fact or check shape |
| `not-opened` | The installed session never read the skill or the relevant card |
| `question-defect` | The request gives away the fix, presumes a diagnosis, or leaves policy undecidable |
| `oracle-defect` | The criterion or test checks something other than the request, or rejects a valid alternative |
| `verification-gap` | Production behavior is right; the requested check does not exercise the real path |
| `rework` | Correct behavior with unjustified changes to working code |
| `variance` | A change between arms with no plausible link to skill content (for example the skill was not read) |
| `unmeasured` | No paired or native evidence yet (missing cells, or never run with a model) |
| `sound-control` | A control or passing case whose question, oracle and skill support are adequate |

Never paste model answer text. Describe the mechanism; at most one quoted phrase under 10 words.

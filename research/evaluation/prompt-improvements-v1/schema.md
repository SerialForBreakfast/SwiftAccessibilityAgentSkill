# Suggestion schema: one record per prompt

Each shard (`shards/ios.json`, `shards/macos.json`, `shards/tvos.json`) is a JSON array with exactly one object per item in that platform. Field values are short, specific and grounded in that item's evidence: grader rationale, blind audit, factorial result, fixture-pair outcome. No generic advice.

| Field | Type | Contents |
|---|---|---|
| `id` | string | The `G-…` id from `items.json` |
| `diagnosis` | string, 1–2 sentences | What this result tells us. Cite the evidence used, e.g. "ledger: …", "audit Q14: …", "pair: fixes defect, breaks working", "factorial: review arm …". For a pass, say whether it shows headroom or only that the task is easy. |
| `problem` | enum | The main reason the item is weak or useful: `no-headroom` (passes because the prompt gives away the fix), `symptom-as-fact`, `ambiguous-policy`, `oracle-mismatch`, `bundled-criteria` (several behaviors in one verdict), `weak-endpoint` (stops before the developer-observable result), `real-model-gap` (a substantive mistake that holds), `rework-only`, `evidence-only` (the proposed test or check is the defect), `grader-uncertain` (inconclusive), `duplicate`, `good-as-is` |
| `disposition` | enum | `keep-control`, `rewrite-neutral`, `pair-variant`, `specify-policy`, `split-criteria`, `repair-oracle`, `raise-to-integration`, `grade-components`, `retire-duplicate`, `reserve-transfer` |
| `promptChange` | string | What to change in the question and why, in one or two sentences. Use "none" only for `keep-control`. |
| `proposedWording` | string or null | **Required** for `rewrite-neutral`, `split-criteria`, `specify-policy` and `raise-to-integration`. It is the replacement developer request: the opening line(s) plus any policy facts the developer would state. It must not state the rule under test or the expected fix. For `split-criteria`, give both questions separated by ` ‖ `. |
| `oracleChange` | string | What the rubric, criterion or hidden test should check differently. Name observable effects. Grade primary, preservation, evidence and rework separately when relevant. Use "none" if the oracle is right. |
| `skill` | array of codes | Skill content this item can show or protect, from the list below, or `[]`. |
| `skillWhy` | string | One sentence linking the item's evidence to those codes, or "none". |
| `priority` | `P0`–`P3` | P0: a confirmed real gap or an oracle defect that corrupts counts. P1: a high-headroom rewrite. P2: a useful change. P3: keep as is. |
| `confidence` | `high`, `medium`, `low` | Confidence in the diagnosis given the evidence available. |
| `transfer` | string | How a fresh transfer case for the same decision should differ: product context and code shape. Use "n/a" for evidence-only historical items. |

**Skill codes:**

| Code | Content |
|---|---|
| `S1` | Review sentence: trace the reported symptom through the supplied code. If the existing path already satisfies the request, show the decisive path and leave it in place. |
| `S2` | Verification: exercise the actual installed handler, callback or returned value, and assert the requested observable effect with a literal expected value. Require a positive fixture before asserting absence. |
| `S3` | Callback ownership: what a closure, action or completion captures when installed, and what it must validate when it runs (current item, request token, owner). |
| `S4` | Focus and destination: restore only after completion, to an eligible member of the correct owner or window, with a declared fallback. |
| `S5` | Precise platform facts on demand: visible title vs. automation identifier, selected-state wording, SDK constants such as edit category, and tvOS/macOS availability boundaries. |
| `S6` | Text offsets: UTF-16/NSString units at the UIKit text boundary; check with a literal substring. |
| `S7` | Media selection: write the actual player item's selection; distinguish forced, full and Off; product policy for menus. |
| `S8` | Restraint and pruning: don't add traits, hints, notifications, helpers or custom actions when a working native control already answers the request. Remove generic boilerplate. |

**Reading evidence:** the public `items.json` and the private per-item packet in `evals/results/prompt-improvements-v1/items/<id>.json`. The packet holds the question, controller entry, ledger row, reviewer record and original first answer. The source fixtures and rubrics are under `code-examples/`. **Never paste answer text into a shard.** Describe the mechanism instead; at most one quoted phrase under 10 words where the mechanism is otherwise unclear.

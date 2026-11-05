# Qwen evaluation dashboard · v1

**64 cases completed · 26 offline checks passed · answer quality not independently graded**

[Case comparisons](#browse-the-cases) · [What C0–C3 mean](#conditions) · [Charts](#development-comparison) · [Observed failures](#examples-worth-reviewing) · [Version rules](../README.md#version-rules)

This first dashboard preserves two existing runs. **No new inference was performed to create it.**
The local runtime works; automatic reference lookup did not. Directly supplying
references did not guarantee correct use of that evidence. No model-quality winner
or release qualification is established.

| Question | Result | Interpretation |
| --- | --- | --- |
| Did jobs complete? | 64/64, no transport failures | Operational success only |
| Did C3 read references on accessibility cases? | Smoke 0/4; development 0/12 | Automatic lookup not demonstrated |
| Did a larger output cap help? | Development truncation 3/16 → 1/16 | 1,024 → 2,048 tokens; not proof of better answers |
| Was correctness graded independently? | No | Accuracy, omissions and unsupported-claim rates are not available |
| Was heldout or Max Mini inference tested? | No | Development results only |

## Conditions

| Label | What the model received | Where tested |
| --- | --- | --- |
| C0 | Generic Swift assistant prompt; no skill or references | Both runs |
| C1 | Actual skill; explicit notice that references/tools are unavailable | Initial smoke only; **not run** in development |
| C2 | Actual skill plus selected reference contents injected by harness | Both runs; does not measure autonomous retrieval |
| C3 / C3-original | Actual skill, filename inventory and read_reference tool | Both runs |
| C3-explicit | C3 plus explicit instruction to read before citing | Development only |

Exact effective prompts are linked beside every response. The additional C3 instruction was:

> For accessibility questions that require this skill’s repository guidance, call read_reference before giving repository-backed advice. Copy the exact path from the supplied inventory, including the references/ prefix. A listed path is not evidence that its contents were read. Cite only references whose contents were returned successfully. For questions unrelated to accessibility, answer directly without reading references.

## Development comparison

Four development families, one OS context, one sample per cell. Candidate only;
16,384 context tokens. Each bar includes three accessibility cases and one unrelated
layout control. C1 is absent because it was not run, not because it scored zero.

Each filled block is one truncated response; shaded blocks completed without truncation.

```text
C0
  1,024 tokens ██░░                     2/4
  2,048 tokens ░░░░                     0/4

C2
  1,024 tokens ░░░░                     0/4
  2,048 tokens ░░░░                     0/4

C3-original
  1,024 tokens █░░░                     1/4
  2,048 tokens █░░░                     1/4

C3-explicit
  1,024 tokens ░░░░                     0/4
  2,048 tokens ░░░░                     0/4
```

| Condition | Truncated / 4 at 1,024 | Truncated / 4 at 2,048 | Automatic reads on a11y cases (both caps) |
| --- | --- | --- | --- |
| C0 | 2 | 0 | Not available |
| C2 | 0 | 0 | Not applicable — injected |
| C3-original | 1 | 1 | 0/6 |
| C3-explicit | 0 | 0 | 0/6 |

Each block is approximately 0.25 seconds; exact values are printed alongside.

```text
C0
  1,024 tokens █████████████████████    5.17s
  2,048 tokens ██████████████████████   5.41s

C2
  1,024 tokens ████████████████████     5.01s
  2,048 tokens ████████████████████     5.12s

C3-original
  1,024 tokens ██████████████████       4.40s
  2,048 tokens ██████████████████       4.41s

C3-explicit
  1,024 tokens ██████████████           3.46s
  2,048 tokens ██████████████           3.45s
```

| Condition | Median seconds · 1,024 | Median seconds · 2,048 |
| --- | --- | --- |
| C0 | 5.17 | 5.41 |
| C2 | 5.01 | 5.12 |
| C3-original | 4.40 | 4.41 |
| C3-explicit | 3.46 | 3.45 |

Times are per-case wall time, not isolated token-generation speed or concurrent
throughput. First-request warmup effects were not isolated. Zero truncation does
not establish correctness. These tiny, correlated samples have no confidence
interval or statistical-superiority claim.

## Initial smoke · baseline versus candidate

Two families × two OS contexts × C0–C3 × two releases = 32 jobs. Both releases used
8,192 context and a 1,024-token output cap. Do not treat the later run as a pure
before/after comparison: it changed family coverage, context and prompt variants.

```text
C0
  baseline     █░░░                     1/4
  candidate    █░░░                     1/4

C1
  baseline     █░░░                     1/4
  candidate    ██░░                     2/4

C2
  baseline     ████                     4/4
  candidate    ░░░░                     0/4

C3
  baseline     █░░░                     1/4
  candidate    ██░░                     2/4
```

| Condition | Baseline truncated / 4 | Candidate truncated / 4 | Independent accuracy |
| --- | --- | --- | --- |
| C0 | 1 | 1 | Not graded |
| C1 | 1 | 2 | Not graded |
| C2 | 4 | 0 | Not graded |
| C3 | 1 | 2 | Not graded |

## Browse the cases

“Gold” below means the recorded expected-answer rubric, **not a calibrated gold
answer**. Every case page shows the exact user prompt, those criteria, a comparison
table, the complete original responses, and links to full effective prompts.

| Case | Question | Development (8 responses each) | Initial smoke (8 responses per OS) |
| --- | --- | --- | --- |
| D01 | Tell me about UILabel accessibility. | [Compare](cases/development-v1-D01.md) | [OS 26](cases/smoke-v1-D01-26.md) · [OS 27](cases/smoke-v1-D01-27.md) |
| D02 | My settings row has text, a switch, and a help button. How should VoiceOver move through it? | [Compare](cases/development-v1-D02.md) | Not run |
| D03 | Can people delete a message without finding the swipe gesture? | [Compare](cases/development-v1-D03.md) | Not run |
| D31 | How do I center a SwiftUI view? | [Compare](cases/development-v1-D31.md) | [OS 26](cases/smoke-v1-D31-26.md) · [OS 27](cases/smoke-v1-D31-27.md) |

## Examples worth reviewing

These are reviewer observations, not a completed independent grading campaign.

| Case | Original response excerpt | Observed issue |
| --- | --- | --- |
| [UILabel · explicit C3](cases/development-v1-D01.md#response-4) | “The … guideline establishes the core requirements” and “Freshness: HIGH” | Cites source contents with zero recorded reads |
| [Settings row · C2 / 2,048](cases/development-v1-D02.md#response-6) | “Verify that the Switch and Button are not separate focus targets.” | Conflicts with supplied reference: keep distinct controls reachable |
| [Deletion · C0 / 1,024](cases/development-v1-D03.md#response-1) | “Users can tap directly on a message to delete it immediately.” | Application behavior was not supplied in the question |
| [UILabel · C0 / 1,024](cases/development-v1-D01.md#response-1) | “…it is not just a visual element; it can be queried” | Stopped mid-sentence at the output cap |

## Provenance and boundaries

- Model: Qwen3.5-2B Q4_K_M; llama.cpp b11457; temperature 0, seed 42, reasoning off; serial requests.
- Evaluated runner: commit `f8d0a258362bf58aec41c37bcbdd06a883137d5b`. Run identities: `smoke-v1`, `llamacpp-development-v1`.
- Published scorecards: [smoke](../../evidence/bigdog-smoke-v1.json), [development](../../evidence/llamacpp-development-v1.json). They retain model/runtime/source hashes.
- [Dashboard data](data.json) contains synthetic case responses, observed metrics and hashes. [Report manifest](manifest.json) pins every report asset. Effective prompt files omit transport envelopes and local model paths; message text and tool schemas are preserved.
- Raw transport records remain private. No credentials, endpoint addresses, private peer messages or heldout responses are included.
- This snapshot records existing tests, not an approved next experiment. **v2 has not been approved.**

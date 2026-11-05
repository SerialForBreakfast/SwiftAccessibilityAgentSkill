# BigDog bounded pilot — summary

**The executor passed qualification and finished the pilot. Model usefulness remains limited.**

| At a glance | Result |
| --- | --- |
| Job accounting | **64/64** |
| Complete / truncated / context-limited | **40 / 17 / 7** |
| Requests | **115 of 200**, including two qualification probes |
| Elapsed time | **11.3 of 45 minutes** |
| Autonomous reference reads | **0/12 eligible C3 jobs** |
| Offline tests | **51 passed** |
| Runtime | Stopped; model lease released |

“Complete” means generation finished, not that the answer was correct. No independent
quality grading or calibration was performed for this pilot.

## What this tells us

- **Execution:** the new manifest-driven adapter ran baseline and candidate across
  all seven planned development families, preserving failures and partial answers.
- **Retrieval:** forced tool-format and tool-result checks passed, but no eligible
  job independently selected a successful reference read.
- **Long conversations:** seven of eight ten-turn conversation jobs exceeded the
  8,192-token context budget; the remaining job included truncated output. No
  history was dropped or prompt shortened to force a fit.
- **Answer quality:** a spot-check of the deletion question still found contradictory
  advice with supplied guidance. This is a limited observation, not a score for the
  full pilot or proof of improvement over earlier runs.

## Scope and safeguards

Qwen3.5-2B Q4_K_M on the pinned llama.cpp b11457 runtime; 8,192 context and
1,024-token output cap; temperature zero, seed 42, reasoning off, serial execution.
No retries, heldout jobs, paid providers, model substitutions or new downloads.
The earlier v1/v2 reports remain unchanged. Updated questions and additional families
prevent treating this as a matched quality comparison with those earlier reports.

Run identifier: `bounded-pilot-20261105T073728Z` (UTC identifier).
Execution source commit: `b831905ca9ce8da7a43f8eed34afcab4a02fec06`.

Seven context-rejected inputs initially retained hashes rather than full bodies.
They were reconstructed offline from frozen inputs and recorded replies, and all
seven matched their original rejection hashes. No inference was replayed. The
executor now saves full inputs before token preflight; the retention fix passed the
51-test offline suite and was not followed by another model run.

**Publication scope:** owner-approved summary and executor only. Full prompts,
generated responses, conversation histories, manifests, per-job records and runtime
configuration remain private. They are intentionally not linked or included here.

[Executor contract](../../../../PILOT-EXECUTOR.md) ·
[Executor source](../../../../runner/pilot-execute.mjs) ·
[Offline tests](../../../../runner/pilot-execute-test.mjs)

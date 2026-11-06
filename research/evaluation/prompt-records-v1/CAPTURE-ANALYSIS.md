# Prompt capture: coverage and analysis

November 6, 2026. This report distinguishes actual captured records from promised
future collection. It does not claim that all historic provider requests are recoverable.

## Captured now

| Material | Coverage | Location |
| --- | --- | --- |
| Local project authoring sessions | 25 discoverable Codex session logs whose metadata names this exact repository; 5,644 retained records | Private archive identified by [capture manifest](local-capture-manifest.json) |
| Input/output records | Ordered user/developer messages, assistant messages, function/custom tool calls and results, recorded turn context and realtime transcript segments where available | One private JSONL per original session; original record content retained |
| Platform draft questions | All nine current draft questions, exact text and hashes; separate rubric links | [Platform index](platform-prompts.json) |
| Current chat excerpt | Exact visible requirement, prior answer and follow-up request, manually transcribed and labeled partial | [Visible excerpt](current-visible-excerpt.json) |
| New native batch | Complete original source/test snapshots, manifests, commands, compiler/test output, results and first failure | [Batch report](../platform-navigation-v1/RESULTS.md) and its private archive receipt |
| Analysis | Four per-family controller rubrics, original key-link failure assessment, result interpretation and coverage limits | [Batch overview](../platform-navigation-v1/README.md), [difficulties](../platform-navigation-v1/DIFFICULTIES.md) |

The capture process selected sessions by exact repository cwd, not by sweeping
unrelated project conversations into the archive. It preserved source-snapshot and
retained-record hashes. Captured files stay private because full inputs and tool
outputs can contain host/account data, private paths or other sensitive context.
No raw session contents were sent to workers or committed into public artifacts.

## Important distinctions

- The local authoring archive contains observed inputs/outputs, not independent
  subject answers to the nine new draft questions. Those questions remain not run.
- Rubrics describe grading criteria. They are not analysis of an answer that has
  never been generated. Original authoring conclusions remain in archived messages;
  this report does not retroactively certify their correctness.
- Private archive records are unchanged selections of available JSONL records;
  the public manifest is derived metadata, not the original session file.
- The current API conversation was not found in the local logs. The visible excerpt
  is explicitly incomplete and does not pretend to contain its missing tool context.
- Hidden reasoning records and analysis-channel messages were excluded. Required
  analysis means externally inspectable findings and evidence, not chain-of-thought.

## Gaps and next actions

1. Map each relevant archived prompt/answer/tool sequence to a stable case and attempt
   ID, then independently analyze it against the source-backed rubric. Capturing
   records is not equivalent to completing this case-by-case audit.
2. Referenced attachment files are not automatically embedded in a client transcript.
   Recover public/synthetic attachments where available and authorized; otherwise
   record the missing bytes. Do not substitute a later working-tree file silently.
3. Client logs may omit provider instructions or full compounded context. Compaction
   boundaries are recorded as metadata; omitted context is not reconstructed.
4. Remote BigDog/MaxMini conversations and judge calls need their own approved exports.
   Nothing here authorizes contacting workers or running new models to fill history.
5. Before public release of any raw prompt/answer, inspect and sanitize it, preserve
   the private original, record redactions and reassess whether grading remains valid.

The native evidence records support bounded configuration assertions, not delivered
focus/speech or a model-performance ranking. The key-link bug is a known development
incident, not a new holdout. Released skill and frozen baselines remain unchanged.

## Capture verification

[Verification receipt](capture-verification.json) confirms all retained file hashes
and 5,644 JSONL records. Of 25 discovered sessions, three have no retainable message/tool
records (metadata-only); they remain explicitly accounted for rather than omitted.
The first verification helper counted an empty file as one empty string. Correcting
that counting helper required no change to captured bytes or the original manifest.

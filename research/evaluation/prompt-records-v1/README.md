# Complete prompt, output and analysis records

Owner requirement, November 6, 2026: preserve **all prompts we use**, their complete
captured inputs, original outputs and analysis. A short question and a rubric alone
are not a complete execution record.

## Two views of each case

1. **Subject view:** the developer question, necessary starter code/attachments and
   the explicitly approved C0-C3 condition context. This is what the tested model sees.
2. **Controller audit view:** all input/output attempts, provenance, results, analysis,
   reviewer/judge prompts, failures and repairs. This is what maintainers inspect.

Link both through stable case, revision, run and attempt IDs. Keep the controller
view outside default skill retrieval and subject workspaces. Never inject answers,
rubrics, known incident outcomes or expected routes into a baseline subject payload.

## What "all prompts" includes

- Authoring prompts used to develop examples, tests and candidate guidance.
- Gold/development questions and every actual condition-specific invocation.
- Follow-up messages, clarifications, retries, repair instructions and resumed turns.
- Reviewer and judge requests, including their rubrics and answer ordering.
- Harness-generated instructions, reference injections and tool definitions supplied
  to a model. Record prompts generated dynamically, not just their template names.

Authoring conversations are development evidence, not independent baseline answers.
A native compiler or XCTest run is tool output, not a model response to a draft
developer question. Failed and successful attempts belong in the same audit trail.

## Required capture per attempt

| Record | Required contents |
| --- | --- |
| Identity | Case/revision, role (author/subject/reviewer/judge), condition, run/attempt ID, predecessor and authorization scope |
| Inputs | Exact ordered messages by role; fully expanded templates; supplied code, attachments, skill instructions and reference bytes with hashes |
| Context | Prior conversation actually supplied, truncation/compaction boundaries, tool definitions, retrieval/tool responses in order; record each request separately in agentic runs |
| Execution | Exact model identifier/revision when exposed, client/provider/harness versions, settings, tool permissions, SDK/OS when relevant, timestamps and finish state |
| Outputs | Original assistant text/code, visible tool calls and results, streamed partial output on failure where captured, finish reason and available usage telemetry |
| Analysis | Rubric revision, criterion-level findings, exact output excerpts, linked assertions/source claims, accepted alternatives, failure attribution, uncertainties and reviewer identity |
| Repairs | New attempt with the complete repair request and original repaired output; link to the first attempt without replacing it |
| Integrity | SHA-256 of retained bytes, original-versus-sanitized provenance, explicit missing fields and redaction impacts |

Analysis is an external evaluation of observable evidence, not a request for hidden
chain-of-thought. Unexposed provider instructions, private reasoning or discarded
context cannot be claimed captured. Record their availability limits explicitly.
Do not present a visible chat transcript as the exact full provider request when
the client does not expose that request.

## Storage layout

```text
case-id/
  case.json                     # framework, revision, lifecycle and artifact links
  subject/                      # clean question and necessary public fixtures
  controller/rubric.md           # accepted alternatives and critical errors
  runs/run-id/attempt-001/
    manifest.json               # provenance, hashes, status and capture limits
    requests.jsonl              # exact captured model-visible requests in order
    events.jsonl                # ordered assistant/tool events, including partials
    inputs/                     # actual supplied code, attachments and references
    outputs/                    # original answers/code/artifacts
    analysis.md                 # separate assessment; never overwrite the answer
    redactions.json             # categories/locations/impact, never secret values
```

Existing immutable bundles may retain their current layout. Link their original
artifacts and hashes instead of moving or rewriting them. A derived index must name
its source and transformation; it must not pretend to be a historical capture.
Keep sensitive originals private and publish sanitized copies only. If redaction
removes behaviorally relevant input, mark the public record incomplete for grading.

## Completeness and acceptance

- A draft/not-run prompt has **no model output yet**. Reference code is not its answer.
- An executed case lists every planned cell and actual attempt, including timeouts,
  errors, truncations, cancellations and quota stops. No success-only selection.
- A captured artifact resolves and matches its hash. Missing bytes are marked
  unavailable, with reason and recovery source, rather than reconstructed from memory.
- Analysis identifies what passed/failed, why, what the assertion proves and what
  it does not prove. Distinguish subject, oracle, harness and missing-evidence failures.
- Independent review checks payload isolation and valid alternatives before a
  case is baseline-eligible. Capture completeness and answer correctness are separate.
- All follow-ups and judge runs are linked. A repair pass never erases first failure.

Historical records can be useful with documented gaps; they are not retroactively
complete. Do not rerun a model simply to manufacture a missing historical answer.
Any new execution still requires the existing quota/scope authorization.

## Current rollout

[Platform prompt index](platform-prompts.json) embeds the exact text and hashes of
the nine Mac/Apple TV draft questions and links their controller rubrics and native
manifests. None has an independent subject response in this index. Native test
results and author-generated source are deliberately not relabeled as those outputs.

This is an initial index, **not a complete historical backfill**. The remaining work
is to inventory the frozen OS26 questions, broader scenario matrix, earlier UIKit
questions, worker runs, authoring sessions and reviewer/judge invocations. Link
existing originals first; ask workers for missing captures through an authorized
handoff. This document does not authorize coordinator messages or new model runs.

Frozen GoldPrompts.md, baseline fixtures and released skill files remain unchanged.

## Available capture

The [capture coverage and analysis report](CAPTURE-ANALYSIS.md) links 25 local project
sessions (5,644 retained records), private originals, a partial current-chat excerpt,
native inputs/outputs and explicit recovery gaps. These authoring logs are not
independent subject runs or a claim of complete provider-context capture.

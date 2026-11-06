# Mac and Apple TV lifecycle evidence

November 6, 2026. Native compile/unit execution complete; four paired developer
questions and rubrics are drafts awaiting independent review. This is an additive
companion batch, not a released skill update or platform-wide parity claim.

| Lane | New positive methods | Deliberate mutants rejected | Original defect rejected |
| --- | ---: | ---: | ---: |
| AppKit/macOS | 28 | 5 | 1 |
| UIKit/tvOS | 29 | 5 | 0 |

Two behavioral families per platform: modal completion/restoration requests and
accessibility-display preference observation. Tests cover stale/cancelled and
reentrant completion, current target eligibility, fallback, stop/restart,
queued callback generations, deduplication and observer cleanup.

- [Results and exact environments](RESULTS.md)
- [Capability parity and remaining queue](COVERAGE.md)
- [Apple source evidence](SOURCES.md)
- [Preserved difficulties and corrections](DIFFICULTIES.md)
- [Authoring capture boundaries](AUTHORING.md)
- [Exact draft questions, hashes and separate rubrics](prompt-records.json)
- [Native attempt index](results-index.json)
- [Independent review checklist](REVIEW-REQUEST.md)

## On-demand retrieval candidate

```sh
node code-examples/tools/lifecycle-retrieval.mjs macOS AppKit modal-restoration
node code-examples/tools/lifecycle-retrieval.mjs tvOS UIKit display-preferences example
node code-examples/tools/lifecycle-retrieval.mjs macOS AppKit display-preferences contract
```

Guidance is the default. Source is added only for `example`; manifest/tests only
for `contract`. Actual read paths, hashes and bytes are recorded; token telemetry
is unavailable. Existing routes delegate unchanged. These repository tools do
not alter installed skill routing or inject the incident archive into context.

## Reproduce a selected contract

Use a fresh output directory for every attempt. Read the package manifest for
check IDs before selecting an installed destination. First inspect the plan, then
run the Mac positive suite on a matching host using a new private output path:

```sh
node code-examples/tools/platform-native.mjs plan code-examples/platforms/macos-lifecycle-v1/manifest.json positive
node code-examples/tools/platform-native.mjs execute code-examples/platforms/macos-lifecycle-v1/manifest.json positive /private/tmp/my-new-mac-lifecycle-attempt
```

[Mac manifest](../../../code-examples/platforms/macos-lifecycle-v1/manifest.json)
and [TV manifest](../../../code-examples/platforms/tvos-lifecycle-v1/manifest.json)
bind exact source hashes, assertions and intended negative failures. Full original
commands and results are in the private archive referenced by the receipt.

The existing nine-case BigDog review/Gemini plan is unchanged. This batch adds four
separate development cases, not new authorized model calls or fresh holdouts.

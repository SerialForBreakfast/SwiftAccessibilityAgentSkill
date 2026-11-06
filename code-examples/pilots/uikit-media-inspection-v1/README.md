# UIKit Media Inspection: Time and Buffer Evidence

UPAIR-06A is the first part of UPAIR-06, not closure of media inspection.
The implementation captures AVPlayer observations without starting playback or
changing controls. A deterministic value layer supports cases that do not require
a live network stream. Nine positive tests and three deliberate mutations are
specified in [manifest.json](manifest.json).

**Executed:** revision 1 compiled, all nine positive methods passed, and all three
mutants were rejected by their intended assertions on iOS 26.5. The native report
records SDK 27.0 and deployment target 26.0 separately. The three offline package
integrity tests also pass. This is verified native evidence; the paired question
and rubric still await independent review and have zero model runs.

## Contracts

- Preserve unavailable, invalid, indefinite, infinite and finite duration states.
- Keep caller-supplied stream kind separate from duration evidence.
- Preserve discontinuous seekable ranges separately from buffered ranges.
- Preserve buffer flags independently; full does not imply likely-to-keep-up.
- Keep requested playback rate, time-control status and waiting reason distinct.
- An empty native player capture leaves playback and unrelated control metadata alone.

Injected range/buffering tests prove transformation policy, not AVFoundation's live
network behavior. The empty-player test covers the native no-item path only.
Sequential getter reads are not atomic. Range membership at capture time does not
promise a later seek succeeds; content and state can change.

## Evidence and Evaluation

[Apple header provenance](apple-sdk-sources.json), [claim coverage](coverage.json),
[difficulty record](DIFFICULTIES.md), [mutation diffs](MUTATIONS.md), and
[native validation](validation/README.md) retain scoped evidence.
The [subject question](evaluation/prompt.json) is separate from the
[controller rubric](evaluation/controller.md). Draft development case; no model
runs, gold promotion or skill changes.

## Run

From repository root, use a fresh private output directory and an installed iOS26
simulator identifier. The adapter does not install runtimes or dependencies.

```sh
node code-examples/tools/native.mjs execute \
  code-examples/pilots/uikit-media-inspection-v1/manifest.json inspection-unit \
  /private/tmp/media-inspection-new IOS26_SIMULATOR_UUID
```

## Remaining Media Work

Audio-description metadata, actual loaded-item extraction and selection diagnostics
still need dedicated fixture-backed contracts. Preserve existing media selection
evidence unchanged. Neither this tranche nor the older media fixture establishes
caption quality, description quality, playback delivery or assistive-tool operation.

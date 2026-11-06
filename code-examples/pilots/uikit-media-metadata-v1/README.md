# UIKit Audio-Description Metadata and Loaded Assets

UPAIR-06B complements the [time/buffering packet](../uikit-media-inspection-v1/README.md)
with actual local asset loading. It is outside installed skill routing and frozen
baseline inputs. Native results, prompt review and model outcomes are separate gates.

## What Is Tested

- Recognize one explicitly tagged audio option and preserve the untagged option.
- Distinguish alternate audio from an explicit description tag using a matched control.
- Report the selected audio and subtitle-off state without changing selection.
- Load duration and full/forced subtitle metadata from the item asset.
- Distinguish no current item, a successfully loaded absent group, and a load error.

The fixture contains one second of black video, silent English/Spanish audio and
synthetic captions. The second audio track carries Apple's documented `tagc`
userdata value. The tag is intentionally synthetic: this tests recognition, not
whether narration exists, describes the picture accurately, or is useful to listeners.
Tests do not start playback or require UI/manual verification. Asset loading does
not establish player-item `readyToPlay`, live buffering or actual selection delivery.

## Provenance

[fixture-provenance.json](fixture-provenance.json) pins both decoded payloads.
`build-fixture.mjs` is an authoring utility, not a test dependency or runtime script.
It accepts the documented FFmpeg remux of the older synthetic MP4, requires the
`moov` atom to be last, and appends the tag to the second audio track without
shifting media offsets. Tests use embedded bytes and need no FFmpeg installation.
The original fixture and tests remain unchanged.

[Apple SDK evidence](apple-sdk-sources.json) records reviewed headers and hashes.
[Coverage](coverage.json), [difficulty history](DIFFICULTIES.md),
[mutation diffs](MUTATIONS.md), and [native evidence](validation/README.md) link
claims to exact tests. The [question](evaluation/prompt.json) is separate from the
[rubric](evaluation/controller.md); independent review and model execution are pending.

## Run

From repository root, with a fresh output directory and installed iOS26 simulator:

```sh
node code-examples/tools/native.mjs execute \
  code-examples/pilots/uikit-media-metadata-v1/manifest.json metadata-unit \
  /private/tmp/media-metadata-new IOS26_SIMULATOR_UUID
```

The loader observes a supplied item. A caller presenting its result for a player's
current item must discard stale results if that item changes during asynchronous
loading. No atomic snapshot or observation subscription is provided here.

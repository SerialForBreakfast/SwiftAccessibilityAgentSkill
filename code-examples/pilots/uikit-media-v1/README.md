# UIKit and AVKit media contracts

Eight focused unit tests use an embedded synthetic MP4 to inspect real subtitle
and alternate-audio groups. The [manifest](manifest.json) hashes source/test inputs;
[coverage](coverage.json) links assertions to claims and UIKit guidelines.

## Primary sources

- [Playback controls](https://developer.apple.com/documentation/avkit/avplayerviewcontroller/showsplaybackcontrols)
  defines the native-control visibility setting. The example configures it before
  any presentation and retains automatic media selection. It never starts playback.
- [Media selection](https://developer.apple.com/documentation/avfoundation/selecting-subtitles-and-alternative-audio-tracks)
  describes groups, language options and explicit selection. Tests load actual
  local asset groups, inspect languages/display names, select subtitles, turn them
  off, reject a missing language and change audio without changing subtitle choice.
  Full-language selection distinguishes
  [forced-only options](https://developer.apple.com/documentation/avfoundation/avmediacharacteristic/containsonlyforcedsubtitles)
  from full subtitles instead of assuming one option per authored language.
- [UIKit accessibility](https://developer.apple.com/documentation/uikit/accessibility-for-uikit)
  supports labels/values for custom playback controls. Tests inspect Play/Pause
  state and normalized timeline values, including stale-state removal and invalid
  durations. The English time string is fixture policy, not production localization.

Exact public header hashes and supporting declaration locators are recorded in
[apple-sdk-sources.json](apple-sdk-sources.json) and the manifest.

## Synthetic fixture

[Provenance](fixture-provenance.json) records the generator version, command,
subtitle inputs and MP4 hash. Content is one second of black16x16 video, silent
English/Spanish audio tracks and two authored synthetic subtitle tracks. FFmpeg
was already installed on the authoring machine; rerunning tests does not need it.
The pinned bytes live in `Tests/MediaFixture.swift`. Each test writes a unique
temporary local file and removes it afterward. No URLs are fetched.

The silent audio tracks establish selection metadata only. They are not audio
descriptions, and these tests do not establish caption correctness, speech quality,
rendered subtitles, buffering behavior or assistive-technology operability. Timeline
configuration alone does not determine whether a stream is seekable. These are
bounded configuration/metadata examples, not a complete player implementation.

## Run locally

```sh
node code-examples/tools/native.mjs execute \
  code-examples/pilots/uikit-media-v1/manifest.json media-unit \
  /private/tmp/uikit-media-new IOS26_SIMULATOR_UUID
```

Other checks: `compile-media`, `hiddencontrols-negative`, `wronglanguage-negative`,
`staleposition-negative`, `forcedonly-negative`. They deliberately hide native
controls, select the wrong language/forced variant or retain an obsolete timeline
value. The button role is configured explicitly, not inferred from a native getter.

Unit tests only. Runtime skill files and baseline fixtures remain unchanged;
independent review and anchor promotion are separate.
See the [validation report](validation/README.md) for all three preserved revisions.

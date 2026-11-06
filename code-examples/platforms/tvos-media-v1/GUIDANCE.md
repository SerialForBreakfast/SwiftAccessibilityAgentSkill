# AVFoundation media companion

Candidate repository guidance, not the installed skill. The package manifest
records the specific platform, SDK, deployment target and executed runtime.

- Inspect loaded option characteristics and selected state without changing them.
  Alternate language or an option name is not evidence of audio description.
- Keep missing item, absent group and loading errors distinguishable. Loading
  metadata is not proof of player readiness or narration quality.
- Explicit user selection should preserve other groups. The full-subtitle example
  excludes forced-only variants; a requested description requires that tag. Leave
  the current choice unchanged when the request cannot be matched.
- Off is conditional on the actual group's allowsEmptySelection; audio versus
  subtitle media type alone does not establish this permission. Groups supplied
  to selection must come from the current item's asset.
- Keep loaded ranges separate from seekable ranges, preserve gaps and half-open
  membership, and do not infer live status from indefinite duration. Buffer flags,
  rate, time-control status and waiting reason are separate observations.

Read only the requested MediaChoice, MediaMetadata or MediaInspection source.
Fixtures/tests are on demand. These are shared AVFoundation contracts, not native
control semantics or proof of audible/visible accessibility behavior.

Sources: [selection](https://developer.apple.com/documentation/avfoundation/avplayeritem/select(_:in:)),
[description characteristic](https://developer.apple.com/documentation/avfoundation/avmediacharacteristic/describesvideoforaccessibility),
[seekable ranges](https://developer.apple.com/documentation/avfoundation/avplayeritem/seekabletimeranges).

# Media contract validation

Revision3 completed all six checks against their declared expectations:

| Check | Result |
| --- | --- |
| Library type-check | Passed |
| Positive unit suite | 8 passed, 0 failed, 0 skipped |
| Hidden native controls | Intended assertion failure |
| Incorrect subtitle language | Intended assertion failure |
| Retained obsolete timeline value | Intended assertion failure |
| Forced-only option selected as full subtitles | Intended assertion failure |

[Revision3 evidence](revision-3.json) records hashes, exact environment/test IDs and
sanitized excerpts. [Revision1](revision-1.json) preserves6 passes/2 failures;
[revision2](revision-2.json) preserves7 passes/1 failure plus diagnostic option
metadata. Unscheduled checks are marked not-run. All executed raw records and
artifacts are stored in separate private immutable ledgers.

The [history](../history/README.md) explains why two authored-language tracks
produced four options and why the example explicitly configures its button trait.
The test now distinguishes full/forced variants instead of silently changing an
expected count. A dedicated mutant verifies that the distinction affects selection.

Environment: Xcode27.0 build27A266a, Swift6.4, SDK27.0 build24A430,
deployment26.0, arm64, iOS26.5 build23F77. The dedicated simulator is shut down.
Compilation alone carries no runtime claim.

This brings the library to97 distinct positive methods across eight packages.
All162 offline harness tests pass, including an embedded-media/provenance hash
check. All210 frozen baseline files remain intact. No runtime skill edits occurred.

The media fixture is synthetic, local and under4KB. No playback, UI automation,
network media, downloads, model calls or paid runs occurred. These results establish
metadata/configuration observations, not rendered caption quality or audio-description
quality. Independent review and annual anchor promotion remain separate.

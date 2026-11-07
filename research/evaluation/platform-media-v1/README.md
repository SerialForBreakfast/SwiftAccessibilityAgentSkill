# Platform-qualified media companion

November 6, 2026. AVFoundation contracts executed separately on macOS and tvOS.
This supplements the native UI framework packages; it does not turn a shared media
contract into an AppKit or UIKit UI claim. See [results](RESULTS.md) for exact status.

Three shared behavioral families, each with a separate platform question/rubric:

| Family | Contract | Evidence boundary |
| --- | --- | --- |
| Explicit selection | Full subtitles, requested description, missing-match preservation, permitted off and independent groups | Selected option state, not audible output or subtitle rendering |
| Loaded metadata | Actual option tags/languages/names/selection, duration, missing item, absent group, error propagation | Silent local fixtures; no narration-quality or readyToPlay claim |
| Diagnostic snapshot | Duration categories, distinct loaded/seekable ranges, independent flags/rate/status/reason | Captured range membership, not a guarantee of future seeking |

- [Apple sources and availability](SOURCES.md)
- [First failures and oracle corrections](DIFFICULTIES.md)
- [Six exact draft questions and separate rubrics](prompt-records.json)
- [Historical fixture reuse](reuse-provenance.json)
- [Authoring capture limits](AUTHORING.md)
- [Native receipts](results-index.json)
- [Independent review request](REVIEW-REQUEST.md)

## Progressive disclosure

```sh
node code-examples/tools/media-retrieval.mjs macOS AVFoundation media-selection
node code-examples/tools/media-retrieval.mjs tvOS UIKit media-metadata example
node code-examples/tools/media-retrieval.mjs macOS AppKit media-inspection contract
```

The explicit platform selects its own evidence package. AppKit/macOS and UIKit/tvOS
host requests may select shared AVFoundation contracts, which are labeled as such.
SwiftUI, Catalyst and iOS do not silently borrow these packages. Guidance is a short
companion summary, not an unrelated OS27 page. Source is opt-in; tests/manifest and
required fixture source load only at contract level. No rubric or incidents load.
Actual read paths/hashes/bytes are recorded; token telemetry is unavailable.
Existing routes delegate unchanged. Released skill routing is not edited.

## Reproduce

```sh
node code-examples/tools/platform-native.mjs plan code-examples/platforms/macos-media-v1/manifest.json positive
node code-examples/tools/platform-native.mjs execute code-examples/platforms/macos-media-v1/manifest.json positive /private/tmp/new-mac-media-attempt
```

TV execution uses its manifest and a matching installed simulator UUID as the final
argument. Always use new output directories. Current manifests pin revision2;
initial versions, including a failing oracle, remain in the evidence record.
No network stream, UI tests, installs, paid model usage or manual verification.

The six new cases are development drafts. The existing nine-case BigDog/Gemini
plan and the four lifecycle cases remain separate; no model call expansion.

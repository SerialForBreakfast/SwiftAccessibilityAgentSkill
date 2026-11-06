# Ordinary Playback-Speed Choices

UPAIR-06C fills the speed-control code-contract gap found in the U-015 clause audit.
Four ordinary buttons share one selection function. The selected rate is reflected
in button state, traits and value before the change callback. Unsupported rates and
disabled requests leave state unchanged; repeated selection does not emit a new
change. These are explicit example policies, not universal UIKit requirements.

The English strings and fixed rate list are fixture inputs. Production UI should
localize labels and expose only rates supported by its content/player. This example
reports a requested choice; it neither starts playback nor guarantees an effective
playback rate. It adds no custom rotor/action prerequisite for ordinary use.

## Evidence

[Manifest](manifest.json), [coverage](coverage.json), and
[SDK source pins](apple-sdk-sources.json) link the code to declarations.
[Native records](validation/README.md), [difficulty ledger](DIFFICULTIES.md), and
[deliberate mutation diffs](MUTATIONS.md) retain outcomes and limits.
The [developer question](evaluation/prompt.json) is separate from the
[controller rubric](evaluation/controller.md). Independent review and model
evaluation remain pending; this is development material, not a fresh holdout.

Eight positive methods exercise ordinary control-event dispatch, selected-state
updates, invalid input, enabled state, duplicate suppression and weak ownership.
Three isolated mutants test stale metadata, repeated callbacks and disabled guards.
Direct sendActions calls are not actual touch, keyboard or VoiceOver activation.
Metadata is inspected, not spoken. No UI tests or mandatory manual verification.

## Rerun

```sh
node code-examples/tools/native.mjs execute \
  code-examples/pilots/uikit-speed-v1/manifest.json speed-unit \
  /private/tmp/speed-new IOS26_SIMULATOR_UUID
```

Run from repository root with a fresh output directory. The native adapter uses
installed SDK/runtime tools only; no package installation or model calls.

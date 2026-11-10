# Swift Accessibility Agent 0.3.0-rc.2

[Download the candidate](swift-accessibility-agent-0.3.0-rc.2.zip) · [Project-local installation](../../INSTALLATION.md#try-the-release-candidate)

This is the opt-in successor to rc.1. The standard repository install remains **0.2.2**. The archive is self-contained: one skill with the stable name, three on-demand example cards and no grader or research files. It preserves the measured [signal-v6 archive](../../research/evaluation/signal-panel-v6/candidate.zip) rather than replacing it. The frozen comparison found 20/56 whole-question passes for v6 versus 16/56 for 0.2.2. Those scores belong to **v6, not rc.2**.

## What changed and how to check it

| Frozen development case | Fresh developer question | Acceptance and counterexample |
|---|---|---|
| P-d82c, Mac search wrapper | My catalog sidebar announces the search prompt twice. Can I remove the extra stop without changing how people edit the query? | Keep the editable NSSearchField as the owner; remove only redundant wrapper semantics. Hiding neighboring artwork is valid. Hiding the representable is not. |
| P-f93b, ordinary play lost on trial 2 | A chapter control already plays on tap. How do I let VoiceOver move between chapters without changing what tapping does? | Preserve ordinary single-tap playback independently of accessible adjustment. Either direct or closure-based wiring is valid. Accessibility activation alone is not a substitute for the existing touch handler. |
| P-9c45, media result failed to compile | Our audio inspector opens before a clip is selected. How do I test that state separately from a loaded clip with no audio group? | Check the returned cases or their observable values. Matching enum cases supports non-Equatable payloads. Do not require broad synthesized equality just to assert two empty cases. |

The entry point routes these decisions to the action or media card as needed. The Mac platform-facts note also points to the action guidance. The candidate quotes the YAML description: the first CLI smoke test found no skill because the v6 description contained an unquoted colon followed by a space.

## Offline evidence

The [focused checks](checks/verify.py) build [Swift fixtures](checks/Contracts.swift), including an alternate search composition and tap closure. Native macOS checks exercise the editable field's public configuration, independent playback/adjustment handlers and an actual AVPlayerItem backed by an empty AVMutableComposition. The shared SwiftUI and AVFoundation compositions also typecheck for iOS. The four deliberately defective controls are:

- Hidden search representable: compiles, rejected by the fixture wiring check.
- Accessibility-only playback: compiles, rejected by the fixture wiring check.
- Synthesized Equatable with a nonconforming associated payload: rejected by the compiler for that conformance.
- Missing player mapped to an absent group: compiles, rejected by the same runtime unit that accepts the correct result.

Wiring checks inspect these specific fixtures, not arbitrary Swift submissions. Native checks establish public properties, handler effects and returned cases, not generated assistive navigation, delivered taps or a change in model behavior. These are development checks, not new holdouts. The authoring request is preserved in the project chat; a portable export of the full transcript is unavailable.

Reproduce on Apple silicon with Xcode, from the repository root:

```sh
python3 -B evals/rc2/build.py
python3 -B evals/rc2/checks/verify.py
# Optional actual CLI smoke test, using an already installed skills CLI:
python3 -B evals/rc2/checks/verify.py /absolute/path/to/skills/bin/cli.mjs
```

Verification uses a new private results directory per attempt. The CLI smoke test targets a disposable project and compares all installed files with the extracted package. No network install or model call is required. The skills CLI smoke used version 1.5.4; native host macOS 27.0, Xcode 27.0 (27A266a), macOS and iOS Simulator SDKs 27.0, deployment targets 26.0. No iOS runtime verdict is claimed.

Archive SHA-256: `a1449f8863ee1c8724da8181d928cf8a58a963202da548b5fc1a1360e5b28aa5`. The builder pins the input v6 archive and the verifier checks reproducibility, protected stable entry point, payload membership, relative links, corrected card routes and installation metadata.

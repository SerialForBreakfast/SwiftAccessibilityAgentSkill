# Local-media and sheet-callback starters, revision 2

Use one ZIP from [subjects](subjects/) per evaluation session. Each contains the developer question, a buildable Swift package and an empty test file. Give the subject **only that ZIP**. The controller tests, alternatives and results live outside it. These are eight revised development inputs, not new holdouts. A comparison needs matching revised inputs in both arms; previous scores belong to the old inputs.

| Platform | Media cases | Sheet cases |
|---|---|---|
| iOS | 4ec9, 6d2d, c04c | |
| tvOS | 5d12, c6b2 | |
| macOS | f483 | 4840, da78 |

**Media:** `try await CaptionFixture.open(selected: .ordinary)` creates a fresh, local AVPlayerItem with the Spanish ordinary captions selected; `.forced` seeds the English forced option. Both seed Spanish audio. The helper returns the item, native groups and option handles. Use that same item in the player and use a second call for a replacement item. Read back native selections rather than assuming what AVPlayer initially chose. Missing groups, unexpected flags, and unsuccessful seeding throw; they never silently skip a test. The bundled movie is the 4,272-byte synthetic positive fixture from [DescriptionFixture.swift](../../../code-examples/swiftui/media-ios-v2/Tests/DescriptionFixture.swift), not downloaded media. Its hash and every subject member are pinned in [manifest.json](manifest.json).

**Sheets:** present A; retain `host.installed.onDismiss` (unwrap the optional registration); present B and retain its callback. Invoke A late, then B twice. Check requests immediately after each call: none, B, still only B. The registration is the modifier installed by the view, not a replacement closure manufactured in the test. The starter deliberately retains the original shared-ticket failure; the two questions retain their different original state-helper guards. The reference captures the registration ticket and checks it in the helper; the alternate checks it at the callback boundary. Both are acceptable. No SwiftUI presentation or UI automation is required or claimed.

From the repository root:

```sh
python3 -B evals/qualification-56/starter-v2/packet.py check
python3 -B evals/qualification-56/starter-v2/packet.py qualify
```

The first command reproduces and verifies the ZIPs in memory against the pinned original question packet. The second unpacks each package into a fresh private run directory, adds controller-only tests, and runs the six caption packages and three variants of each sheet package. It requires Xcode, the existing booted iOS/tvOS 26.5 unit simulators, and the macOS host. Inspect first logs and result bundles under `evals/results/starter-v2-*/`. Qualification tests fixture availability and callback ownership, not model lift, rendered navigation, or delivered focus.

**First-attempt record:** the first iOS build timed out during SDK compilation before a test verdict. A bounded-concurrency retry reached the test and failed its track inventory: language alone did not uniquely identify a legible option. AVFoundation exposed four choices: English ordinary/forced and Spanish ordinary/forced. The corrected helper uses known option positions for this checksum-pinned asset, then independently verifies languages, forced flags, empty-selection support and the actual selections. The original attempts remain in `starter-v2-hr4xvgui` and `starter-v2-iq94oy00`.

**Final qualification:** [12 receipts](qualification.json) from `starter-v2-hbnpxdn6`, Xcode 27.0 (27A266a), macOS 27.0 and iOS/tvOS 26.5 simulators, deployment targets 26.0. Six exported caption packages passed; both sheet starters failed at the retired-callback assertion; both valid designs passed for each sheet question. No frozen answer or proof was modified or rerun.

# Parity update after media qualification

This is additive to [lifecycle parity](../platform-lifecycle-v1/COVERAGE.md).
Earlier inventories/results remain historical records, not overwritten dispositions.

| Capability | macOS | tvOS | Remaining gap |
| --- | --- | --- | --- |
| Explicit media selection | Native AVFoundation option state plus off-policy seam | Same contracts, separately executed | Broader language preference fallback and native control integration |
| Description/subtitle metadata | Loaded tagged/untagged local fixture, current selection, missing/absent/error | Same contracts, separately executed | More authored formats and asset replacement/cancellation lifecycle |
| Stream inspection | Duration categories, range membership, buffer/status snapshots | Same contracts, separately executed | Network stream behavior not exercised; no live classification from duration alone |
| Native forms and recovery | Queued | Queued where applicable to TV controls | Validation recovery, ordinary actions and preserved user input |
| Richer collection relationships | Outline/column semantics queued | Shelves/container ownership queued | Per-platform contracts rather than iOS API substitution |
| Text/rotors | Platform audit pending | Applicable API audit pending | Availability and native behavior first |
| SwiftUI | Deferred | Deferred | No expansion |

Media adds 25 methods per platform: 16 previously established metadata/inspection
methods qualified on these targets, plus 9 selection/policy methods. Those 9 are
shared conceptual contracts exercised separately, not 18 unique behaviors. Neither
method count nor copied fixture count is a coverage percentage.

The companion now includes AppKit UI contracts plus AVFoundation on Mac, and
UIKit UI contracts plus AVFoundation on TV. Do not label shared media tests as
AppKit or UIKit UI interaction validation. Native control/ordinary-action work is
still distinct from selected media-option metadata.

Next coordinated batch: native form state/recovery plus richer Mac outline/column
and TV collection relationships, with targeted source audit, meaningful negatives,
first-failure capture and paired prompts. Media asset replacement/cancellation is
also a concrete follow-up contract, not silently claimed complete here.

Independent review: four lifecycle and six media pairs are draft; original nine
remain the prepared BigDog/Gemini scope. No new model run or promotion is implied.

# UIKit Checkout Preservation Contract

New authored development example, revision 2 after a preserved oracle correction.
It does not repair or rescore the
eight reviewed checkout answers. Paired prompt and rubric are drafts, not gold
promotion or frozen baseline changes. SwiftUI remains deferred.

The component receives an existing UIButton and retains it unchanged. A permanent
vertical stack owns a scalable multiline total label. Updating the total only
changes its text. This avoids requiring adaptive-axis callbacks as a preferred
idiom and makes ownership explicit.

## Contracts

| Requirement | Unit method | Evidence scope |
| --- | --- | --- |
| Preserve existing button | testPreservesExistingButtonIdentityTypographyAndTitle | Identity, configured font descriptor, scaling flag and title |
| Preserve ordinary payment action | testRepeatedUpdatesPreserveExistingActionExactlyOnce | Zero calls from construction/updates, one existing callback per direct dispatch, stable arranged-subview count |
| Flexible scalable text | testFlexibleTextConfigurationAndNoFixedEnclosingHeight | String retained, multiline/scaling metadata, no autoshrink or fixed enclosing height; no rendered clipping assertion |
| Preserve configuration/state | testPreservesConfiguredButtonAndDisabledState | Supplied button configuration and disabled state unchanged |
| Release ownership | testRetainedButtonDoesNotRetainSummary | Externally retained button does not keep summary alive |

The fixture creates its existing payment action before constructing the component.
Unlike the eight-answer review, that wiring is explicitly part of this new task's
test environment. No callback is retroactively added to a submitted model answer.

[Manifest](manifest.json) pins exact sources and test selections. The
[developer question](evaluation/prompt.json) contains no solution, rubric or expected
route. The [controller rubric](evaluation/controller.md) accepts equivalent solutions.
See [difficulties](DIFFICULTIES.md) and [validation](validation.json) for outcomes.

## Source Support

- [Apple WWDC24, Get started with Dynamic Type](https://developer.apple.com/videos/play/wwdc2024/10074/), Scaled text / Dynamic layouts, reviewed 2026-11-06: supports scalable multiline UILabel configuration and flexible containers.
- [UIControl event dispatch](https://developer.apple.com/documentation/uikit/uicontrol/sendactions(for:)), SDK27 UIKit `UIControl.h`: `addAction` is declared iOS14+, and `sendActionsForControlEvents` dispatches registered actions. Exact callback counts and preservation are example requirements, not accessibility-delivery promises.

No UI tests, mandatory manual verification, model calls or rendered navigation
claims. Native execution uses installed SDK/runtime anchors only.

```sh
node code-examples/tools/native.mjs execute \
  research/evaluation/failure-driven/checkout-contract-v1/manifest.json \
  checkout-unit /absolute/private/new-checkout-run EXISTING_IOS26_SIMULATOR_UUID
```

Independent oracle/prompt review is still required. These tests do not establish
that a skill improves model answers; future paired evaluation must measure that.

## Executed Outcomes

On iOS 26.5 (23F77), Xcode 27.0 (27A266a), SDK 27.0 (24A430), deployment26.0:

- First positive run: five methods executed, four passed, one configuration-oracle
  failure preserved. Component source was unchanged by the subsequent correction.
- Revised positive run: all five methods passed.
- Each of two deliberate mutants: same five methods executed, four passed and
  exactly the intended method failed. These are intentional controls, not model errors.
- No skipped methods, repaired model answers, UI tests or model calls.

Repository offline suite plus review/contract checks: 210 passing tests at this
checkpoint; 210 frozen baseline files and 87 historical evidence pins verified.
Native and offline counts represent different layers and are not added together.

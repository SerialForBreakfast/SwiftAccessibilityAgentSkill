# UIKit lifecycle contracts

Eight unit tests cover preference observation, presentation configuration and
state-dependent custom-action metadata. [Manifest](manifest.json) and
[coverage](coverage.json) bind exact inputs and tests to reviewed declarations.

## Primary support

- [Reduce Motion notification](https://developer.apple.com/documentation/uikit/uiaccessibility/reducemotionstatusdidchangenotification)
  names the change event; its production observer uses the default notification
  center. Tests inject a private center and preference reader. They assert an
  initial read, both state transitions, unrelated-event filtering, stop/restart,
  duplicate-start prevention and owner release. No device preferences change.
- [Block observers](https://developer.apple.com/documentation/foundation/notificationcenter/addobserver(forName:object:queue:using:))
  retain their blocks and require removal. This example uses the main operation
  queue, weak owner capture and a small immutable token owner that unregisters on
  release. Its unchecked Sendable wrapper contains only immutable registration
  references; observer removal is delegated to NotificationCenter. Tests post
  synchronously from the main actor; they do not assert arbitrary concurrent event
  ordering or that UIKit itself delivered an event.
- [Presentation dismissal configuration](https://developer.apple.com/documentation/uikit/uiviewcontroller/ismodalinpresentation)
  and installed `UIViewController.h` support the form-sheet/dismissal settings.
  Tests do not load or present a view, and make no focus-movement claim.
- [Custom actions](https://developer.apple.com/documentation/uikit/uiaccessibilitycustomaction)
  support named categorized operations. Tests remove the edit category and hint
  for read-only state, then replace the handler when editing returns. This helper
  owns its supplied action list; authorization and retained-action guards belong
  to the operation handler (see the dynamic/reuse pilots).

Reviewed header hashes are in [apple-sdk-sources.json](apple-sdk-sources.json).
The example uses established APIs available below the iOS26 deployment target.

```sh
node code-examples/tools/native.mjs execute \
  code-examples/pilots/uikit-lifecycle-v1/manifest.json lifecycle-unit \
  /private/tmp/uikit-lifecycle-new IOS26_SIMULATOR_UUID
```

Other checks: `compile-lifecycle`, `wrongnotification-negative`, `unstopped-negative`,
`staleedit-negative`. Mutations target notification registration, stop behavior,
and stale action metadata, respectively. All execution is compile/unit-only;
runtime skill integration and annual anchor promotion remain separate.
Completed checks and retained failures are in the [validation report](validation/README.md).

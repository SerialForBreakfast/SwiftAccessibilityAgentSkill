# Modal Contents and Restoration Requests

UPAIR-04 candidate. Thirteen positive unit methods cover modal contents, ordinary
controls, escape, asynchronous completion, exact background-state restoration,
current weak target lookup, retained-but-removed targets, repeated calls, teardown
and reopening. Five deliberate
defects check assertion sensitivity. No UI presentation or automation is performed.

## Documented API and Project Policy

[Modal flags](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/accessibilityviewismodal)
and the descendant-hidden property configure accessibility scope.
[Notification posting](https://developer.apple.com/documentation/uikit/uiaccessibility/post(notification:argument:))
accepts an argument; tests intercept the requested notification/target, not delivery.
[Escape](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/accessibilityperformescape())
provides a direct overridable handler. Tests invoke it and ordinary control actions;
they do not synthesize an assistive-technology gesture.

Snapshotting the prior background flag, suppressing duplicate completions, reading
the current weak target, and invalidating old callbacks are project lifecycle
policies implemented using those APIs. They are not undocumented UIKit guarantees.
Installed declaration hashes are in [source provenance](apple-sdk-sources.json).

The owner mounts the panel as a separate subtree from the background, supplies
localized text and the primary handler, and calls `tearDown()` before discarding
the panel. Background ancestors or panel descendants are rejected to avoid hiding
the panel itself. Other owners must not concurrently mutate the captured background
flag during this lifecycle. This fixture does not implement a shared modal-stack
manager, interactive animation cancellation or visual layout.

`performDismissal` is an injected completion-based operation; production integration
must call its completion only when dismissal is complete. `tearDown()` invalidates
pending callbacks and restores state without posting a restoration request. Reopen
while open/closing is rejected; reopen after teardown is permitted. A missing target
is represented by a nil notification argument, not a fabricated target. Revision3
also requires the target to remain in the captured background subtree, and avoids
requesting a target when that subtree was already accessibility-hidden. This is
bounded structural validation, not proof that the target can actually receive focus.

## Reproduce

```sh
node code-examples/tools/native.mjs plan \
  code-examples/pilots/uikit-modal-v1/manifest.json modal-unit
node code-examples/tools/native.mjs execute \
  code-examples/pilots/uikit-modal-v1/manifest.json modal-unit \
  /private/tmp/uikit-modal-new IOS26_SIMULATOR_UUID
```

Other check IDs: `compile-modal`, `lostbackground-negative`, `earlynotification-negative`,
`stalecompletion-negative`, `ignoreddismissguard-negative`, `detachedtarget-negative`.
Each run preserves inputs
and logs in a fresh private output directory.

See [coverage](coverage.json), [native evidence](validation/README.md),
[exact mutation diffs](MUTATIONS.md), and [difficulty ledger](DIFFICULTIES.md).
The [subject question](evaluation/prompt.json) and [controller rubric](evaluation/controller.md)
are separate development drafts awaiting independent review. Native passes neither
promote the skill nor establish real-user navigation or measured model improvement.

The [history](history/README.md) preserves the green eleven-test revision1 and the
revision2 regression that exposed a retained-but-detached target before repair.

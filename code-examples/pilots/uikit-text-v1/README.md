# UIKit text ranges and action metadata

Sixteen focused unit tests extend UIKit coverage without changing earlier pilots,
the frozen skill or baseline snapshots. The [manifest](manifest.json) pins inputs
and source claims; [coverage](coverage.json) maps every test to those claims.

## Primary source support

- `UIAccessibilityCustomRotor.h` declares text-range results and weak target-element
  ownership. `UITextInput.h` declares text positions, range creation and text
  extraction. The example uses actual `UITextView` positions/ranges rather than
  mocked string offsets. See [Apple rotor item results](https://developer.apple.com/documentation/uikit/uiaccessibilitycustomrotoritemresult).
- `UIAccessibilityCustomAction.h` declares linked attributed/plain names, categories,
  weak selector targets and Bool handlers. The edit-category API is available from
  iOS18; this pilot targets26. See [Apple custom actions](https://developer.apple.com/documentation/uikit/uiaccessibilitycustomaction).
- `UISlider.h`, `UIStepper.h` and `UISwitch.h` supply control declarations/defaults;
  `UIControl.h` supplies explicit dispatch. Tests distinguish programmatic state
  configuration from the subsequent direct callback invocation.
- `UIFont.h` declares preferred fonts compatible with explicit traits. Twelve
  content-size categories are sampled for body-font metrics, not rendered fit.

The installed SDK27 header hashes are in [apple-sdk-sources.json](apple-sdk-sources.json).
Apple URLs and supporting locators are also recorded in the manifest. Availability
declarations, application policy and measured behavior remain separate.

## Assertions and boundaries

Text search checks first/last results, forward/backward movement, boundaries,
Unicode-prefix offsets, replacement with no matches, empty-query rejection and
foreign-element ranges. Matching is literal and non-overlapping; boundary behavior
and rejection rules are this example's policies. A stale range from an edited
document is not yet a qualified case.

Action tests inspect name/category configuration, execute the stored handler and
check weak-target ownership after an explicit autorelease boundary. They do not
claim to exercise system selector-versus-handler dispatch or rotor menu rendering.

Control tests inspect native clamping/defaults, dispatch switch events explicitly
and query font metrics with specified traits. No UI automation, global preference
changes, screenshots, model calls or simulator downloads are involved.

## Bounded execution

```sh
node code-examples/tools/native.mjs plan \
  code-examples/pilots/uikit-text-v1/manifest.json text-unit
node code-examples/tools/native.mjs execute \
  code-examples/pilots/uikit-text-v1/manifest.json text-unit \
  /private/tmp/uikit-text-new IOS26_SIMULATOR_UUID
```

Other check IDs: `compile-text`, `wrongrange-negative`, `stalematches-negative`,
`missingcategory-negative`. The negatives respectively introduce an off-by-one
range start, retain old matches and omit the edit category. Each runs the same
selected test against a single-error source variant.

Actual results are in the [validation report](validation/README.md). Source/example review and anchor
promotion are separate; this pilot does not change runtime skill routing.

# Apple sources and declaration evidence

Reviewed November 6, 2026. Source-byte fingerprints are in [source-index.json](source-index.json).
Source tiers remain unchanged. Executed unit results supplement documented contracts;
application-specific policies are labeled separately.

| Claim | Tier-1 source and section | Declaration evidence | Limits |
| --- | --- | --- | --- |
| AppKit custom actions | [NSAccessibilityCustomAction](https://developer.apple.com/documentation/appkit/nsaccessibilitycustomaction), handler construction and success result | NSAccessibilityCustomAction.h: enclosing class macOS10.13; handler returns Bool. NSAccessibilityProtocols.h: accessibilityCustomActions macOS10.13 | Revision invalidation, ordinary action preservation and weak ownership are example policy |
| AppKit explicit labels | [NSAccessibilityProtocol](https://developer.apple.com/documentation/appkit/nsaccessibilityprotocol), label/custom actions | NSAccessibilityProtocols.h: accessibilityLabel macOS10.10 | No assertion of native role/default speech |
| AppKit state-change requests | [NSAccessibility](https://developer.apple.com/documentation/appkit/nsaccessibility-swift.struct), Posting Notifications | Default sink calls post(element:notification:); unit sink captures element and valueChanged | Ordering and duplicate suppression are application policy; delivery untested |
| tvOS preferred focus candidates | [UIFocusEnvironment](https://developer.apple.com/documentation/uikit/uifocusenvironment), Preferred focus environments | UIFocus.h preferredFocusEnvironments declaration; document lists protocol tvOS9, not inferred member introduction | Filter and ordering are example policy; no delivered-focus claim |
| tvOS optional custom actions | [UIAccessibilityCustomAction](https://developer.apple.com/documentation/uikit/uiaccessibilitycustomaction), Creating a custom action | UIAccessibilityCustomAction.h handler initializer and actionHandler explicitly tvOS13.0 | Parent class page omits explicit tvOS start; do not guess it from iOS8 |
| Ordinary primary action dispatch | [UIControl](https://developer.apple.com/documentation/uikit/uicontrol), action registration | UIControl.h semantic primary-action event and addAction:forControlEvents: declarations; local annotations name iOS, not explicit tvOS introduction | Successful target26 compilation does not fill missing introduction dates; sendActions is not remote simulation |
| Selected-state preservation | [UIAccessibilityTraits](https://developer.apple.com/documentation/uikit/uiaccessibilitytraits), selected | UIAccessibilityConstants.h UIAccessibilityTraitSelected; no explicit tvOS introduction in selected declaration | Tests operate on explicit bits, not inferred default traits |

The documentation markdown was retrieved for NSAccessibility, UIFocusEnvironment
and UIAccessibilityCustomAction. Other links identify the corresponding Apple APIs;
claims above are anchored in inspected SDK declarations, not an assertion that every
linked page has been re-read. Full per-member/enclosing declaration audit remains a
promotion prerequisite. No blanket deprecation-free or all-version-support claim.

## Distinct evidence dimensions

- SDK/compiler: actual SDK27 and Swift toolchain receipts in each native attempt.
- Deployment target: 26.0 in both package manifests and compiler command.
- Runtime: macOS27 host versus tvOS26.5 simulator, recorded separately.
- Documented behavior: source claims above.
- Example policy: callback ownership, stale-generation rejection, focus candidate
  filtering and notification deduplication.
- Observed result: only the assertion executed on the named environment.

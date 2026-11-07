# Source and declaration evidence

Reviewed November6, 2026. [source-index.json](source-index.json) hashes the actual
Apple markdown responses and installed SDK27 headers. These records do not refresh
all historical sources or assert that every framework member has been audited.

| Apple source and section | Contract used | Scope |
| --- | --- | --- |
| [NSWindow.makeFirstResponder](https://developer.apple.com/documentation/appkit/nswindow/makefirstresponder(_:)), Discussion/Return Value | Check acceptsFirstResponder; interpret request result carefully | Return true need not mean the requested object became first responder |
| [NSWorkspace display-options notification](https://developer.apple.com/documentation/appkit/nsworkspace/accessibilitydisplayoptionsdidchangenotification), Discussion | Observe workspace.notificationCenter and query fresh properties | No userInfo values to treat as a settings snapshot |
| [UIFocusEnvironment.setNeedsFocusUpdate](https://developer.apple.com/documentation/uikit/uifocusenvironment/setneedsfocusupdate()), Discussion | Request an update through the owning environment | Currently focused view must be contained by that environment; parent requests may take priority |
| [UIAccessibility motion notification](https://developer.apple.com/documentation/uikit/uiaccessibility/reducemotionstatusdidchangenotification), Discussion | Default notification center; reread setting | Injected tests do not trigger a system-wide preference change |

## Availability evidence

| Declaration | Observation |
| --- | --- |
| AppKit NSAccessibility.h: display-options notification, increased contrast, reduced transparency | macOS10.10 annotations |
| AppKit NSAccessibility.h: reduced motion | macOS10.12 annotation |
| AppKit NSResponder/NSWindow/NSView | Eligibility, request, ownership and hidden-state declarations inspected; target26 compilation recorded, no inferred earliest introduction for unannotated members |
| UIKit UIFocusEnvironment.setNeedsFocusUpdate | Apple page explicitly lists tvOS9.0; SDK header declaration inspected |
| UIKit UIAccessibility preference queries/notifications | SDK headers inspected; iOS-only annotations are not invented tvOS introduction dates; exact earliest tvOS availability remains unresolved where not declared |

Both packages compile against SDK27 with deployment target26. Mac runtime evidence
is27.0, TV runtime evidence26.5. Compilation does not establish behavior on all
supported runtimes. No deprecation warning was treated as proof of runtime removal.
A complete member-by-member availability matrix remains separate work.

## Application policies versus platform behavior

Session tokens, fallback preference, enabled/hidden ownership checks, snapshot
value deduplication and stop/restart generation rules are example application
policies. Apple APIs provide the request, hierarchy, notification and setting-query
mechanisms. Tests establish the policies and calls directly; they do not attribute
those policies to Apple or claim that a fallback must be chosen in every app.

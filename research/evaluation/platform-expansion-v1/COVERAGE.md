# Platform coverage queue

These are guideline-level dispositions for the initial platform batch, not a
clause-by-clause closure inventory. Existing source guidance remains intact.
Every row marked partial has additional untested behavior; no entire platform is
claimed unit-validated. SwiftUI expansion stays deferred.

| Guideline | Disposition | Evidence or next contract |
| --- | --- | --- |
| macOS m-001 roles/labels/values/actions | Partial | DesktopActions names, values, ordinary/custom dispatch; other roles and native defaults unasserted |
| macOS m-002 keyboard focus | Missing testable coverage | Key-view configuration and restoration request ownership; actual keyboard navigation outside unit scope |
| macOS m-003 grouping | Partial | Row preserves independent controls; nested hierarchy/table relationships next |
| macOS m-004 notifications | Partial | DesktopStatus request identity/order/deduplication; other notification types next |
| macOS m-005 SwiftUI/AppKit interop | SwiftUI deferred | Preserve existing guidance |
| macOS m-006 tables/outlines | Missing testable coverage | Row/column relationships, selection and reuse |
| macOS m-007 modal windows | Missing testable coverage | Owned restoration target and dismissal state |
| macOS m-008 Voice Control naming | Partial | Caller-provided contextual names; actual recognition outside unit scope |
| macOS m-009 contrast/transparency | Missing testable coverage | Preference-driven configuration and observer lifetime |
| macOS m-010 testing | Partial | Native adapter and bounded unit evidence; no UI testing lane |
| tvOS t-001 directional focus | Partial | Ordered preferred candidates and policy exclusions; focus engine movement outside unit scope |
| tvOS t-002 initial/restored focus | Partial | Initial preferred candidates; modal restoration state next |
| tvOS t-003 labels/values/traits | Partial | Metadata reset and selected-trait preservation; remaining state transitions next |
| tvOS t-004 shelves/grids | Partial | Independent child controls; collection grouping/reuse contracts next |
| tvOS t-005 custom actions/remote | Partial | Ordinary primary dispatch plus optional shortcut; remote delivery outside unit scope |
| tvOS t-006 search/filter | Missing testable coverage | Filter state, result ownership and selection reconciliation |
| tvOS t-007 media | Missing testable coverage | Platform-qualified media metadata/selection contracts; no implicit iOS fallback |
| tvOS t-008 motion | Missing testable coverage | Injected preference state and animation-independent final state |
| tvOS t-009 contrast | Missing testable coverage | Non-color state and preference configuration |
| tvOS t-010 UI-test hooks | Documentation-supported/outside unit scope | No UI testing expansion; evaluate separable state contracts only |
| tvOS t-011 larger text | Missing version-qualified coverage | Separate text configuration from tvOS27 system feature; do not claim it on26 |

## Next coordinated batch

AppKit tables/selection, key-view and modal restoration requests, preference lifecycle;
tvOS collection/search state, modal restoration requests, media and preference state.
Audit actual member availability first, then pair each family with independent
questions and accepted-alternative rubrics. Do not port all iOS tests mechanically.

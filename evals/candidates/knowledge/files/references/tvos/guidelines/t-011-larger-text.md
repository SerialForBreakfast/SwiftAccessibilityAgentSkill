# T-011: Larger Text on tvOS

Reviewed: 2026-11-04. Evidence: Tier-1 Apple WWDC26 session 221,
Overview and layout adaptation. Status: source-supported candidate update.

System Larger Text is described for tvOS 27. Keep that availability boundary
explicit when an app also supports tvOS 26; readable layouts remain valuable on
both versions, but the new system preference must not be promised on older OSes.

Use semantic text styles and flexible dimensions. For UIKit labels, enable
content-size-category font adjustment. Adapt dense shelves and cards at larger
sizes: fewer columns or a vertical arrangement can preserve full titles and
reachable controls. Preserve useful focus relationships when layout changes.

For implementation review, inspect fixed fonts, heights, and widths. For runtime
evaluation, compare default and accessibility sizes, including focus and title
visibility. Documentation supports the recommendation; runtime checks assess the
particular app implementation.

Source: [Prepare your tvOS apps for Dynamic Type](https://developer.apple.com/videos/play/wwdc2026/221/).

# Reuse pilot history

Revision1 compiled and10 of11 positive tests passed. The typography test supplied
an explicit content-size trait collection to font creation, but left the receiving
label in its default trait environment. After automatic adjustment was enabled,
the observed label font sizes followed that environment rather than the detached
test input. Three negative checks were not run after this positive-suite failure.

Revision2 makes the helper derive font traits from the receiving label itself.
The test sets a public content-size trait override on that label, asserts the
effective category, then checks the font size/style and configuration. All three
styles and three categories remain covered. The initial expectations were not
weakened to accept default-size output for accessibility categories.

Apple describes automatic adjustment in
[UIContentSizeCategoryAdjusting](https://developer.apple.com/documentation/uikit/uicontentsizecategoryadjusting)
and explains the trait category in
[preferredContentSizeCategory](https://developer.apple.com/documentation/uikit/uitraitcollection/preferredcontentsizecategory).
The observed mismatch is scoped to this test setup and runtime, not reported as
an Apple API defect. The original source, tests, mutations and manifest are in
[revision-1](revision-1/); raw failed evidence remains immutable.

Revision2 also compiled and passed10 of11 tests. Its new effective-category
assertion showed that assigning an override alone had not synchronously updated
the label's trait collection. Revision3 adds `updateTraitsIfNeeded()` immediately
after each override, as documented in the installed `UIView.h`: it forces trait
updates and delivers trait callbacks synchronously. No layout/rendering or UI
automation is involved. Revision2 inputs are retained in [revision-2](revision-2/).
Both earlier revisions stopped before running their negative checks.

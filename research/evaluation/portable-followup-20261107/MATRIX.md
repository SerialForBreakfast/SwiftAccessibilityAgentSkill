# Current case and criterion reconciliation

Author reconciliation; no retrospective regrading.

## Case outcomes

| Case | Priority | Flash dev.5 → dev.7 | Haiku dev.5 → dev.7 |
| --- | --- | --- | --- |
| ios-uikit-actions | P0 | material-gap → material-gap | material-gap → meets |
| ios-uikit-state | P1 | material-gap → material-gap | material-gap → material-gap |
| ios-uikit-text | P0 | meets → material-gap | material-gap → not-assessable |
| ios-swiftui-semantics | preservation-control | meets → meets | meets → meets |
| ios-swiftui-lifecycle | P0 | material-gap → material-gap | material-gap → not-assessable |
| ios-swiftui-media | P1 | material-gap → material-gap | material-gap → meets |
| macos-appkit-actions | P0 | meets → material-gap | meets → not-assessable |
| macos-appkit-structure | P1 | material-gap → material-gap | unattempted |
| macos-appkit-testing | P1 | material-gap → material-gap | unattempted |
| macos-swiftui-state | preservation-control | material-gap → meets | unattempted |
| macos-swiftui-text | P1 | not-assessable → not-assessable | unattempted |
| macos-swiftui-lifecycle | P0 | not-assessable → material-gap | unattempted |
| tvos-uikit-state | P1 | material-gap → material-gap | unattempted |
| tvos-uikit-media | P1 | not-assessable → material-gap | unattempted |
| tvos-uikit-lifecycle | P0 | meets → material-gap | unattempted |
| tvos-swiftui-actions | preservation-control | meets → meets | unattempted |
| tvos-swiftui-structure | preservation-control | meets → meets | unattempted |
| tvos-swiftui-testing | P1 | material-gap → material-gap | unattempted |
| ios-uikit-no-change | preservation-control | meets → meets | unattempted |
| ios-swiftui-no-change | preservation-control | meets → meets | unattempted |
| macos-appkit-no-change | preservation-control | meets → meets | unattempted |
| mixed-macos-owner | P1 | material-gap → material-gap | unattempted |
| ios-missing-reference | preservation-control | meets → meets | unattempted |
| tvos-version-boundary | preservation-control | meets → meets | unattempted |

## All criteria

Whole-task outcomes are available; individual verdicts remain unavailable, not inferred.

| Criterion | Evidence | Mac references | Draft review proposals |
| --- | --- | ---: | --- |
| ios-uikit-actions/criterion-0 | partial_evidence | 1 | REV-ORDINARY-PATH |
| ios-uikit-actions/criterion-1 | partial_evidence | 2 | REV-ORDINARY-PATH |
| ios-uikit-actions/criterion-2 | partial_evidence | 2 | retain current contract |
| ios-uikit-state/criterion-0 | partial_evidence | 1 | REV-STATE-PREMISE |
| ios-uikit-state/criterion-1 | partial_evidence | 3 | REV-STATE-SUPERSESSION |
| ios-uikit-state/criterion-2 | partial_evidence | 1 | REV-ORDINARY-PATH |
| ios-uikit-text/criterion-0 | partial_evidence | 3 | REV-TEXT-PRESERVATION |
| ios-uikit-text/criterion-1 | partial_evidence | 4 | REV-ORDINARY-PATH, REV-TEXT-PRESERVATION |
| ios-uikit-text/criterion-2 | review_only | 0 | retain current contract |
| ios-uikit-text/criterion-3 | review_only | 0 | retain current contract |
| ios-swiftui-semantics/criterion-0 | review_only | 0 | REV-RESTRAINT-OWNER |
| ios-swiftui-semantics/criterion-1 | partial_evidence | 2 | REV-RESTRAINT-OWNER |
| ios-swiftui-semantics/criterion-2 | review_only | 0 | retain current contract |
| ios-swiftui-lifecycle/criterion-0 | partial_evidence | 3 | REV-DISMISSAL-PATH |
| ios-swiftui-lifecycle/criterion-1 | partial_evidence | 3 | REV-DISMISSAL-PATH |
| ios-swiftui-lifecycle/criterion-2 | review_only | 0 | retain current contract |
| ios-swiftui-media/criterion-0 | partial_evidence | 1 | REV-MEDIA-OBSERVABLE |
| ios-swiftui-media/criterion-1 | partial_evidence | 1 | REV-MEDIA-OBSERVABLE |
| ios-swiftui-media/criterion-2 | partial_evidence | 2 | REV-MEDIA-OBSERVABLE |
| ios-swiftui-media/criterion-3 | review_only | 0 | retain current contract |
| macos-appkit-actions/criterion-0 | partial_evidence | 2 | REV-ORDINARY-PATH |
| macos-appkit-actions/criterion-1 | partial_evidence | 3 | REV-ORDINARY-PATH |
| macos-appkit-actions/criterion-2 | partial_evidence | 2 | retain current contract |
| macos-appkit-structure/criterion-0 | partial_evidence | 1 | REV-RESTRAINT-OWNER |
| macos-appkit-structure/criterion-1 | partial_evidence | 2 | REV-ORDINARY-PATH |
| macos-appkit-structure/criterion-2 | review_only | 0 | retain current contract |
| macos-appkit-testing/criterion-0 | review_only | 0 | REV-EVIDENCE-ATTRIBUTION |
| macos-appkit-testing/criterion-1 | review_only | 0 | REV-EVIDENCE-ATTRIBUTION |
| macos-appkit-testing/criterion-2 | review_only | 0 | REV-EVIDENCE-ATTRIBUTION |
| macos-appkit-testing/criterion-3 | review_only | 0 | REV-EVIDENCE-ATTRIBUTION |
| macos-swiftui-state/criterion-0 | partial_evidence | 2 | REV-STATE-PREMISE |
| macos-swiftui-state/criterion-1 | partial_evidence | 2 | REV-STATE-SUPERSESSION |
| macos-swiftui-state/criterion-2 | partial_evidence | 1 | REV-ORDINARY-PATH |
| macos-swiftui-text/criterion-0 | genuine_gap | 0 | REV-TEXT-PRESERVATION |
| macos-swiftui-text/criterion-1 | genuine_gap | 0 | REV-ORDINARY-PATH, REV-TEXT-PRESERVATION |
| macos-swiftui-text/criterion-2 | review_only | 0 | retain current contract |
| macos-swiftui-text/criterion-3 | review_only | 0 | retain current contract |
| macos-swiftui-lifecycle/criterion-0 | partial_evidence | 3 | REV-DISMISSAL-PATH |
| macos-swiftui-lifecycle/criterion-1 | partial_evidence | 3 | REV-DISMISSAL-PATH |
| macos-swiftui-lifecycle/criterion-2 | review_only | 0 | retain current contract |
| tvos-uikit-state/criterion-0 | partial_evidence | 1 | REV-STATE-PREMISE |
| tvos-uikit-state/criterion-1 | partial_evidence | 3 | REV-STATE-SUPERSESSION |
| tvos-uikit-state/criterion-2 | partial_evidence | 2 | REV-ORDINARY-PATH |
| tvos-uikit-media/criterion-0 | partial_evidence | 5 | REV-MEDIA-OBSERVABLE |
| tvos-uikit-media/criterion-1 | partial_evidence | 2 | REV-MEDIA-OBSERVABLE |
| tvos-uikit-media/criterion-2 | partial_evidence | 1 | REV-MEDIA-OBSERVABLE |
| tvos-uikit-media/criterion-3 | review_only | 0 | retain current contract |
| tvos-uikit-lifecycle/criterion-0 | direct_evidence | 2 | REV-DISMISSAL-PATH |
| tvos-uikit-lifecycle/criterion-1 | direct_evidence | 3 | REV-DISMISSAL-PATH |
| tvos-uikit-lifecycle/criterion-2 | review_only | 0 | retain current contract |
| tvos-swiftui-actions/criterion-0 | partial_evidence | 2 | REV-ORDINARY-PATH |
| tvos-swiftui-actions/criterion-1 | partial_evidence | 1 | REV-ORDINARY-PATH |
| tvos-swiftui-actions/criterion-2 | partial_evidence | 2 | retain current contract |
| tvos-swiftui-structure/criterion-0 | partial_evidence | 0 | REV-RESTRAINT-OWNER |
| tvos-swiftui-structure/criterion-1 | partial_evidence | 3 | REV-ORDINARY-PATH |
| tvos-swiftui-structure/criterion-2 | review_only | 0 | retain current contract |
| tvos-swiftui-testing/criterion-0 | review_only | 0 | REV-EVIDENCE-ATTRIBUTION |
| tvos-swiftui-testing/criterion-1 | review_only | 0 | REV-EVIDENCE-ATTRIBUTION |
| tvos-swiftui-testing/criterion-2 | review_only | 0 | REV-EVIDENCE-ATTRIBUTION |
| tvos-swiftui-testing/criterion-3 | review_only | 0 | REV-EVIDENCE-ATTRIBUTION |
| ios-uikit-no-change/criterion-0 | review_only | 0 | retain current contract |
| ios-uikit-no-change/criterion-1 | review_only | 0 | REV-RESTRAINT-OWNER |
| ios-uikit-no-change/criterion-2 | review_only | 0 | REV-EVIDENCE-ATTRIBUTION |
| ios-swiftui-no-change/criterion-0 | review_only | 0 | retain current contract |
| ios-swiftui-no-change/criterion-1 | review_only | 0 | REV-RESTRAINT-OWNER |
| ios-swiftui-no-change/criterion-2 | review_only | 0 | REV-EVIDENCE-ATTRIBUTION |
| macos-appkit-no-change/criterion-0 | review_only | 0 | retain current contract |
| macos-appkit-no-change/criterion-1 | review_only | 0 | REV-RESTRAINT-OWNER |
| macos-appkit-no-change/criterion-2 | review_only | 0 | REV-EVIDENCE-ATTRIBUTION |
| mixed-macos-owner/criterion-0 | review_only | 0 | REV-RESTRAINT-OWNER |
| mixed-macos-owner/criterion-1 | review_only | 0 | REV-RESTRAINT-OWNER |
| mixed-macos-owner/criterion-2 | review_only | 0 | REV-EVIDENCE-ATTRIBUTION |
| ios-missing-reference/criterion-0 | review_only | 0 | retain current contract |
| ios-missing-reference/criterion-1 | review_only | 0 | retain current contract |
| ios-missing-reference/criterion-2 | review_only | 0 | REV-EVIDENCE-ATTRIBUTION |
| tvos-version-boundary/criterion-0 | review_only | 0 | retain current contract |
| tvos-version-boundary/criterion-1 | review_only | 0 | retain current contract |
| tvos-version-boundary/criterion-2 | review_only | 0 | REV-EVIDENCE-ATTRIBUTION |

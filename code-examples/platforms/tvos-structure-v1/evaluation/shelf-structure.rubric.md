# UIKit/tvOS: shelf-structure

Status: draft; independent oracle/question review pending. Not baseline-eligible.
Classification: UIKit-specific collection configuration.

Represent a non-element container with independently configured heading and ordinary buttons. Preserve shelf/child order and selected state using section-qualified keys, accept repeated item IDs in distinct sections, reject within-section/section duplicates atomically. Replace old hierarchy without accumulation. Reject callbacks from previous generations even if a control is reattached, and current controls that no longer belong to the owning hierarchy. Respect enabled state; retain unrelated traits. Accept equivalent collection data sources, stable identity/lifetime guards and native controls. Stored accessibilityElements order does not establish actual speech or directional-focus navigation.

Score correctness, preservation, practical usefulness and unsupported certainty separately. Invented APIs, lost ordinary actions, erased user input and stale cross-item actions are critical. Accept alternatives satisfying the contract; no requirement for test/helper names. These are known-development cases, not holdouts.

## Traceability

- [Source claims and check IDs](../manifest.json)
- [Implementation](../Sources/TelevisionShelves.swift)
- [Unit assertions](../Tests/TelevisionShelvesTests.swift)
- Methods: `TelevisionShelvesTests/testShelvesPreserveIndependentHeadingAndButtons`, `TelevisionShelvesTests/testExplicitContainerOrderMatchesHierarchy`, `TelevisionShelvesTests/testSameItemIDInDifferentSectionsRemainsDistinct`, `TelevisionShelvesTests/testDuplicateSectionIDsRejectedAtomically`, `TelevisionShelvesTests/testDuplicateItemIDsWithinSectionRejected`, `TelevisionShelvesTests/testOrdinaryButtonSelectsAndCallsCurrentAction`, `TelevisionShelvesTests/testDisabledButtonDoesNotChoose`, `TelevisionShelvesTests/testOldGenerationRejectedEvenWhenButtonReattached`, `TelevisionShelvesTests/testDetachedCurrentButtonCannotChoose`, `TelevisionShelvesTests/testReplacingSectionsDetachesOldShelves`, `TelevisionShelvesTests/testSelectionSurvivesSectionReorder`, `TelevisionShelvesTests/testRemovedSelectionClears`, `TelevisionShelvesTests/testSameItemMovedToOtherSectionDoesNotStealSelection`, `TelevisionShelvesTests/testSelectionPreservesUnrelatedTraits`, `TelevisionShelvesTests/testEmptySectionKeepsHeadingAndNoActions`, `TelevisionShelvesTests/testRepeatedConfigurationDoesNotAccumulateChildren`, `TelevisionShelvesTests/testRetainedButtonDoesNotRetainOwner`.
- Negative checks: `duplicates`, `grouping`, `generation`, `detached`.
- [Execution and difficulty record](../../../../research/evaluation/platform-structure-v1/README.md)

Subject input is the separate .prompt.md plus approved condition material. Do not inject the rubric, assertions, negative fixtures or incident narrative.

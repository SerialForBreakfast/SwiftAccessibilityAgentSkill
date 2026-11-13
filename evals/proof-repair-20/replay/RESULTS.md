# Preserved proof replay: all 20 triplets

1313 unique answer texts in 17 answer-bearing returns. 198 production-owner matches; this is a proof-block count, not a model or original-task pass rate.

| Case | Observable | Caught | Missed | Rejected valid | Compile gap | Crash/exception |
|---|---|---:|---:|---:|---:|---:|
| Q002 | Adding selected keeps the header and prior traits. | 1 | 0 | 0 | 0 | 0 |
| Q006 | The ordinary first element is the same heading as the reordered model's first entry. | 2 | 0 | 0 | 0 | 0 |
| Q010 | Mid-gray linear luminance is about 0.214, not 0.5. | 2 | 0 | 0 | 0 | 0 |
| Q018 | The retained Remove rejects the rebound row rather than dispatching through it. | 1 | 4 | 3 | 1 | 5 |
| Q024 | A native field edit before a reply prevents acceptance of the obsolete snapshot. | 4 | 24 | 0 | 4 | 0 |
| Q027 | A non-start column inside the populated span resolves to that cell. | 2 | 0 | 0 | 0 | 0 |
| Q031 | No restoration request is posted between dismissal request and completion. | 16 | 4 | 1 | 3 | 0 |
| Q041 | Posting the motion preference change refreshes the previously false value. | 3 | 0 | 0 | 0 | 0 |
| Q054 | Configuration removes exposure of the previously accessible decoration. | 1 | 1 | 2 | 0 | 0 |
| Q057 | Repeating the selected speed does not emit an extra playback change. | 0 | 1 | 0 | 2 | 0 |
| Q059 | The unrelated trait survives choosing the row. | 1 | 3 | 1 | 0 | 0 |
| Q066 | Pressing the ordinary Save control reaches Save once, not Open. | 3 | 3 | 2 | 6 | 3 |
| Q067 | Selection remains on B after two identically titled results trade positions. | 1 | 1 | 0 | 0 | 0 |
| Q072 | An attached original that refuses first responder yields the fallback request. | 0 | 13 | 2 | 0 | 0 |
| Q080 | The selected child survives reloading its expanded group in a different order. | 2 | 9 | 0 | 0 | 0 |
| Q081 | The configured row exposes its true selection state. | 4 | 0 | 11 | 1 | 2 |
| Q083 | With motion reduced, the visible status changes even without an animation. | 1 | 1 | 0 | 0 | 0 |
| Q089 | The ordinary Details action invokes its installed callback. | 6 | 16 | 3 | 1 | 4 |
| Q092 | The transition requests zero duration under the reduced-motion policy. | 1 | 0 | 0 | 1 | 0 |
| Q099 | The shelf itself is not a single accessible element replacing its heading and buttons. | 0 | 6 | 1 | 0 | 2 |

## Q002

| Submitted proof | Native result | Evidence |
|---|---|---|
| `8decd2c77783` | catches supplied defect | XCTAssertTrue(button.accessibilityTraits.contains(.button), "Pre-existing .button trait should be preserved.") |

## Q006

| Submitted proof | Native result | Evidence |
|---|---|---|
| `f0ec8e48eaae` | catches supplied defect | XCTAssertEqual(view.accessibilityElements as? [UILabel], [label1, label2]) |
| `cfa9903db79e` | catches supplied defect | XCTAssertEqual((view.accessibilityElements as? [UILabel])?.count, 2) |

## Q010

| Submitted proof | Native result | Evidence |
|---|---|---|
| `99b093a00aca` | catches supplied defect | XCTAssertEqual(midGray.luminance, expectedWCAGLuminance, accuracy: 1e-4) |
| `1334243d68ad` | catches supplied defect | XCTAssertEqual(midtone.luminance, expectedLinear, accuracy: 1e-4) |

## Q018

| Submitted proof | Native result | Evidence |
|---|---|---|
| `f2c7c90602f8` | misses defect | testSelectionStateUpdatesWhenSelectionMoves() |
| `128a49581b94` | rejects valid code | working: XCTAssertTrue failed |
| `50f7b2cab3c6` | catches supplied defect | XCTAssertFalse(staleHandled, "Stale action should not succeed after cell reconfiguration") |
| `309bee3d521c` | runtime crash (not a catch) |  |
| `5094a5cb6c43` | rejects valid code | working: XCTAssertFalse failed |
| `65946cb57c22` | misses defect | testMoveSelectionBetweenTwoRowsUpdatesTraitsAndValue() |
| `34531623282a` | interface/discovery gap | extra argument 'isSelected' in call |
| `90ed10092337` | runtime crash (not a catch) |  |
| `b1b5721346f6` | rejects valid code | working: XCTAssertFalse failed |
| `0979867f09fc` | runtime crash (not a catch) |  |
| `bd357b7658f8` | runtime crash (not a catch) |  |
| `4ec0b6ae796f` | runtime crash (not a catch) |  |
| `aa7d1ded6cb6` | misses defect | testMovingSelectionBetweenRows() |
| `f698f7f406e6` | misses defect | testMoveSelectionBetweenRowsUpdatesTraitsAndValue() |

## Q024

| Submitted proof | Native result | Evidence |
|---|---|---|
| `e926bd62d6dc` | misses defect | testEditPreservesTextAndRejectsStaleValidationReply() |
| `f43aa3f64ca0` | misses defect | testLateEarlierMediaLoadDoesNotOverwriteNewerResult(), testLateEarlierValidationResponseDoesNotOverwriteNewerResult() |
| `5ad5b9ced158` | interface/discovery gap | value of type 'UILabel' has no member 'stringValue' |
| `3776b8987c00` | catches supplied defect | XCTAssertNil(acceptedInput) |
| `5e8e645d8743` | misses defect | testLateEarlierRequestDoesNotOverwriteNewerResult() |
| `6eda8cb5da0f` | misses defect | testLateResponseDoesNotOverwriteNewerResult() |
| `71930cfb6bc7` | interface/discovery gap | value of type 'UITextField' has no member 'stringValue' |
| `a2eb8886a4d4` | interface/discovery gap | value of type 'UITextField' has no member 'stringValue' |
| `642b8d2210b6` | interface/discovery gap | value of type 'UILabel' has no member 'stringValue' |
| `33792d727892` | misses defect | testLateResponseDoesNotOverwriteNewerResult() |
| `0b9498d7f40b` | misses defect | testStaleValidationDiscardedAfterTextEdit() |
| `7a279c8bec7a` | misses defect | testStartValidationChangeTextDeliverOriginalReply() |
| `9a37790934a5` | misses defect | testStaleValidationResultDiscardedAfterTextEdit() |
| `f9ebaa0c824a` | misses defect | testStaleValidationCompletionIgnoredAfterTextChange() |
| `e11282c4d897` | catches supplied defect | XCTAssertNil(acceptedPayload) |
| `323e4f48b3b6` | misses defect | testStartValidationChangeTextDeliverOriginalReply() |
| `62ae7370d099` | misses defect | testStaleValidationResultIgnoredAfterEdit() |
| `07676ccd69a0` | misses defect | testChangeTextDuringValidationDiscardsOriginalReply() |
| `d48e145c4cfe` | misses defect | testEditDuringOutstandingValidationAllowsSubsequentSubmit() |
| `0a2507db0914` | misses defect | testEditDuringOutstandingValidationAllowsSubmittingCurrentEntry() |
| `4697eff905ab` | misses defect | testEditDuringOutstandingValidationAllowsSubmittingCurrentEntryAfterReply(), testOrdinaryValidationSubmissionSucceeds() |
| `fecbb58d7240` | catches supplied defect | XCTAssertEqual(acceptedInputs.count, 0) |
| `09d17a6d0da0` | misses defect | testEditDuringOutstandingValidationAllowsSubmittingCurrentEntry() |
| `83275ec784ac` | misses defect | testEditDuringOutstandingValidationAllowsSubmittingCurrentEntry() |
| `c11ba318c701` | misses defect | testSubmitCurrentEntryAfterEditingDuringValidation() |
| `3feff8e37045` | misses defect | testStaleValidationDiscardedAfterTextEdit() |
| `afc6607ea4ac` | misses defect | testStaleValidationResultIsDiscardedAfterTextChange() |
| `d0bd6f49bf6e` | misses defect | testEditDuringOutstandingValidationAllowsSubmittingCurrentEntry() |
| `d496595376d7` | misses defect | testValidationReplyIgnoredAfterTextChange() |
| `c205c6f7ac4e` | catches supplied defect | XCTAssertNil(acceptedPayload) |
| `6325abb1ff67` | misses defect | testEditWhileOutstandingAllowsSubmittingCurrentEntryAfterReply() |
| `4994db423a5d` | misses defect | testEditDuringOutstandingValidationPermitsSubmittingCurrentEntry() |

## Q027

| Submitted proof | Native result | Evidence |
|---|---|---|
| `10365ac247d9` | catches supplied defect | XCTAssertIdentical(cell, expectedCell, "Coordinate (\(r), \(c)) did not resolve to the merged cell") |
| `1b1c759040fa` | catches supplied defect | XCTAssertIdentical(cell, targetCell, "Coordinate (\(r), \(c)) should resolve to the merged cell") |

## Q031

| Submitted proof | Native result | Evidence |
|---|---|---|
| `8ceeaf2486d2` | catches supplied defect | XCTAssertEqual(screenChangedCount, 1) |
| `ae3182e6ac87` | catches supplied defect | XCTAssertEqual(postedNotifications.count, 0) |
| `e0fe7df0573f` | catches supplied defect | XCTAssertEqual(postCount, 1) |
| `8e2039543e98` | catches supplied defect | XCTAssertTrue(postedNotifications.isEmpty, "Should not restore before dismissal finishes") |
| `f39051e005cd` | misses defect | testDismissalGatedByCanDismiss() |
| `4dc63f5f3fd8` | misses defect | testDismissalGating() |
| `c02986a0baf4` | rejects valid code | working: XCTAssertTrue failed |
| `9d8582c8a2be` | misses defect | testReentrantDismissalDoesNotRestoreTwice() |
| `8c844a6301ce` | catches supplied defect | XCTAssertEqual(postedNotifications.count, 0) |
| `bf9f19ab73cf` | misses defect | testBackgroundRestoresPriorHiddenStateAcrossMultipleOpenCloseCycles() |
| `13fd6ad6f432` | interface/discovery gap | value of type 'RestoringPanel' has no member 'cancelDismissal' |
| `f0bdc5b598c7` | catches supplied defect | XCTAssertTrue(postedNotifications.isEmpty) |
| `001f1c982fe9` | interface/discovery gap | value of type 'RestoringPanel' has no member 'cancelDismissal' |
| `9cad79a1d00d` | catches supplied defect | XCTAssertTrue(posted.isEmpty, "No focus request should be made when dismissal does not complete normally") |
| `40271cab570f` | catches supplied defect | XCTAssertTrue(posted.isEmpty, "Canceled dismissal must not emit any focus requests") |
| `3d034cbdc202` | catches supplied defect | XCTAssertEqual(postedNotifications.count, 0) |
| `dc3e653695cd` | catches supplied defect | XCTAssertEqual(postedEvents.count, 0, "No focus change should be posted when dismissal is cancelled.") |
| `455c7dbcfb15` | catches supplied defect | XCTAssertTrue(posted.isEmpty, "Focus should not be requested before dismissal finishes") |
| `ef04567afbd2` | catches supplied defect | XCTAssertTrue(posts.isEmpty, "Focus was requested prematurely during dismissal start") |
| `6c388b08a9f5` | interface/discovery gap | value of type 'RestoringPanel' has no member 'cancelDismissal' |
| `0c5a139351e0` | catches supplied defect | XCTAssertTrue(postedNotifications.isEmpty, "Focus should not be requested upon starting dismissal.") |
| `fbfed15a54e9` | catches supplied defect | XCTAssertTrue(notifications.isEmpty, "Focus should not be requested before dismissal finishes.") |
| `9d6d44180ed4` | catches supplied defect | XCTAssertTrue(focusPosts.isEmpty, "Focus should not be requested upon initiating dismissal.") |
| `d1ffb8717b5d` | catches supplied defect | XCTAssertEqual(posts.count, 0) |

## Q041

| Submitted proof | Native result | Evidence |
|---|---|---|
| `6dab71c999d3` | catches supplied defect | XCTAssertTrue( |
| `c94fd54219a5` | catches supplied defect | XCTAssertTrue(preference.reduceMotion) |
| `24c7b3b39f0d` | catches supplied defect | XCTAssertTrue(preference.reduceMotion) |

## Q054

| Submitted proof | Native result | Evidence |
|---|---|---|
| `0af6b14e06f4` | catches supplied defect | XCTAssertFalse(card.decoration.isAccessibilityElement) |
| `00e376bbdc62` | rejects valid code | working: XCTAssertTrue failed |
| `8e7749433d06` | rejects valid code | working: failed - accessibilityElements should not be nil |
| `d5fd0f8a5f6c` | misses defect | testOpenButtonUpdatesAccessibilityLabelWhenReconfigured() |

## Q057

| Submitted proof | Native result | Evidence |
|---|---|---|
| `bd50a1f05283` | interface/discovery gap | cannot convert value of type 'Void' to expected argument type 'Bool' |
| `22ac4ad1dac7` | interface/discovery gap | cannot convert value of type 'Void' to expected argument type 'Bool' |
| `0fbb814078f6` | misses defect | testSelectSynchronizesDisplayedAndAccessibleState() |

## Q059

| Submitted proof | Native result | Evidence |
|---|---|---|
| `2e55810994c6` | rejects valid code | working: XCTAssertGreaterThanOrEqual failed: ("129.66666666666666") is less than ("152.33333333333334") - nameLabel should not be vertically compressed when text wraps. |
| `f6504ed6bdee` | misses defect | testNameLabelSupportsMultilineWrapping() |
| `75f844fe6bcf` | catches supplied defect | XCTAssertTrue(cell.accessibilityTraits.contains(.button)) |
| `a87a844c2a6a` | misses defect | testDeselectionRemovesSelectedAccessibilityTrait() |
| `3dec63e0c4d2` | misses defect | testFontScalesWithDynamicTypeAndSurvivesRepeatedConfigure() |

## Q066

| Submitted proof | Native result | Evidence |
|---|---|---|
| `592f9d9976a4` | rejects valid code | working: XCTAssertEqual failed: ("1") is not equal to ("2") |
| `fc2772855a2d` | rejects valid code | working: XCTAssertEqual failed: ("nil") is not equal to ("Optional("Document 1")") |
| `7167feef87c2` | interface/discovery gap | 'saveItem' is inaccessible due to 'private' protection level |
| `d22ddc183556` | misses defect | testAccessibilityCustomActionRespectsSaveEnabledState() |
| `b8d4f5238c1c` | misses defect | testCurrentActionExecutesSuccessfully(), testStaleActionDoesNotExecuteAfterReconfiguration() |
| `47b4aa9995b0` | runtime crash (not a catch) |  |
| `2c817c0bcd0b` | failure needs attribution |  |
| `ecb0989f165c` | interface/discovery gap | value of type 'NSAccessibilityCustomAction' has no member 'targetHandler' |
| `10e7ce18ef38` | interface/discovery gap | argument passed to call that takes no arguments |
| `37fc07b9ec03` | interface/discovery gap | missing argument for parameter #1 in call |
| `c37c8b72e2bf` | catches supplied defect | XCTAssertEqual(item2Saved, 2) |
| `90bd7f0656ce` | catches supplied defect | XCTAssertEqual(itemOperated, "saved_B") |
| `3c1bbbc0891d` | runtime crash (not a catch) |  |
| `eff997204fa4` | interface/discovery gap | value of type 'NSAccessibilityCustomAction' has no member 'accessibilityPerformPressAction' |
| `b1ea4f433b80` | catches supplied defect | XCTAssertTrue(item2Saved) |
| `adf95eaa237a` | interface/discovery gap | value of type 'NSAccessibilityCustomAction' has no member 'accessibilityPerformCustomAction' |
| `46c8a91e2932` | misses defect | testActionTargetingAfterRefresh() |

## Q067

| Submitted proof | Native result | Evidence |
|---|---|---|
| `90e9c3fd3f00` | misses defect | testApplyRejectsDuplicateIDsWithoutModifyingState() |
| `c4c130932219` | catches supplied defect | XCTAssertEqual(results.selectedID, "b", "Selection identity should be preserved across reorder/rename") |

## Q072

| Submitted proof | Native result | Evidence |
|---|---|---|
| `d432dc69fec5` | misses defect | testRestoresFallbackWhenPrimaryNoLongerBelongsInRoot() |
| `0fadd2403ca2` | misses defect | testDelayedCloseCallbackDoesNotRestoreReplacedPresentation() |
| `e91c9f11fc56` | misses defect | testFailsWhenNeitherTargetBelongsToRootOrIsUsable(), testRestoresToFallbackWhenPrimaryNoLongerBelongsToRoot() |
| `187b95caef42` | misses defect | testRestoreFallsBackWhenPrimaryNoLongerBelongsToRoot() |
| `f7335516e3c4` | misses defect | testRestoresOnlyToUsableTargetOrFallback() |
| `7444cec916ff` | misses defect | testRestoresToFallbackWhenPrimaryNoLongerBelongsToRoot() |
| `6e8feb87f01f` | misses defect | testFailsWhenNeitherTargetIsEligible(), testRestoresToFallbackWhenPrimaryNoLongerEligible() |
| `41bf34a9e43b` | rejects valid code | working: XCTAssertTrue failed |
| `8e74e6743b01` | misses defect | testFailsGracefullyWhenNeitherBelongsToWindow(), testRestoresToFallbackWhenPrimaryNoLongerBelongsToWindow() |
| `7b701bdd6466` | misses defect | testFailsWhenNeitherTargetIsEligible(), testRestoresToFallbackWhenPrimaryNoLongerBelongsToRoot() |
| `434f8d10f7a5` | misses defect | testRestoresToFallbackWhenPrimaryNoLongerBelongsOrIsUsable() |
| `266c6081f900` | misses defect | testFailsWhenNeitherTargetBelongsToRoot(), testRestoresToFallbackWhenPrimaryNoLongerBelongsToRoot() |
| `3a45b5ce7c15` | misses defect | testRestoreFailsWhenNeitherTargetBelongsToRoot(), testRestoreFallsBackWhenPrimaryNoLongerBelongsToRoot() |
| `9e9fc8a011c8` | rejects valid code | working: XCTAssertTrue failed |
| `421f26bf9e21` | misses defect | testRestoresToFallbackWhenPrimaryNoLongerInHierarchy(), testRestoresToPrimaryWhenStillUsable() |

## Q080

| Submitted proof | Native result | Evidence |
|---|---|---|
| `bd3aea40e00c` | misses defect | testOrphanedHandleBehavior() |
| `ad5e3798e907` | misses defect | testOrphanedAndReusedGroupHandles() |
| `481b014feb18` | misses defect | testReusedIDOldAndNewHandles() |
| `37ba4d428f2d` | misses defect | testIDReuseStaleVsNewHandle() |
| `2d788711987a` | misses defect | testRemovedNodeSeesNoChildren() |
| `a9deba4261d2` | misses defect | testRemovedNodeStaleChildrenBehavior() |
| `656c8e11e29c` | misses defect | testObsoleteNodeDoesNotReportChildren() |
| `74df29182a25` | misses defect | testDuplicateIDsAreRejectedWithoutLeavingPartialState() |
| `53e75b633242` | misses defect | testRejectsDuplicateIDsWithoutPartialUpdate() |
| `d4bd7262ae3f` | catches supplied defect | XCTAssertEqual(outlineWrapper.selectedID, "2") |
| `d298f8d055ee` | catches supplied defect | XCTAssertEqual(outline.selectedID, "2", "Selection should follow item identity despite reorder/rename") |

## Q081

| Submitted proof | Native result | Evidence |
|---|---|---|
| `b3c30666ebd9` | rejects valid code | working: XCTAssertFalse failed |
| `36f904face6a` | rejects valid code | working: XCTAssertTrue failed |
| `7ed2971e5245` | rejects valid code | working: failed - Child open button not exposed in accessibilityChildren |
| `774cce682a98` | rejects valid code | working: failed - Child button not exposed in accessibility children |
| `96c8d801bb0d` | rejects valid code | working: Expectation failed: row.open.accessibilityRole() == .button row.open.accessibilityRole() → NSAccessibilityRole(rawValue: "AXUnknown") .button → NSAccessibilityRole(rawValue: "AXButton") |
| `0461c71cc010` | rejects valid code | working: XCTAssertFalse failed - Row should not be a leaf accessibility element |
| `e7191e7b8cef` | runtime crash (not a catch) |  |
| `0672c480b050` | catches supplied defect | XCTAssertTrue(row.isAccessibilitySelected()) |
| `9912c8fe1609` | catches supplied defect | XCTAssertTrue(row.isAccessibilitySelected()) |
| `b390a67e6857` | rejects valid code | working: failed - Missing child button |
| `b4b7461d2429` | rejects valid code | working: XCTAssertTrue failed |
| `aaa0c40e4c2c` | catches supplied defect | #expect(row.isAccessibilitySelected() == true) |
| `e270aaf09c6e` | runtime crash (not a catch) |  |
| `e41c84005cf6` | rejects valid code | working: XCTAssertTrue failed |
| `2c78ecfcb24f` | interface/discovery gap | value of type 'any NSAccessibilityElementProtocol' has no member 'accessibilityRole' |
| `ecfb98c3cf15` | rejects valid code | working: XCTAssertTrue failed |
| `f587abc888d3` | rejects valid code | working: XCTAssertTrue failed |
| `5bad042572a9` | catches supplied defect | #expect(row.isAccessibilitySelected() == true) |

## Q083

| Submitted proof | Native result | Evidence |
|---|---|---|
| `b83fb0f7c1bb` | catches supplied defect | XCTAssertEqual(status.label.text, "New Result") |
| `72557187f9bd` | misses defect | testDuplicatePreferenceDoesNotRetriggerAnimation() |

## Q089

| Submitted proof | Native result | Evidence |
|---|---|---|
| `5e79fc38318f` | catches supplied defect | XCTAssertTrue(directDetailsCalled, "Triggering primary action on details button must invoke onDetails.") |
| `09b1b9449ee1` | interface/discovery gap | cannot use optional chaining on non-optional value of type '@MainActor () -> Bool' |
| `67dac1ed7d77` | rejects valid code | working: Invalid parameter not satisfying: focusSystem (NSInternalInconsistencyException) |
| `bcadd13a851f` | rejects valid code | working: XCTAssertTrue failed - Child elements should be grouped together. |
| `2994f9059056` | misses defect | testStaleCustomActionDoesNotTriggerAfterReconfigure() |
| `b714fc1300a8` | misses defect | testSetSelectedPreservesExistingTraits() |
| `3b1676c10f7d` | rejects valid code | working: XCTAssertEqual failed: ("nil") is not equal to ("Optional("Play")") |
| `2e181f6cb3fb` | runtime crash (not a catch) |  |
| `df7ff657104b` | catches supplied defect | XCTAssertEqual(item2Details, 1) |
| `78517fb7921b` | catches supplied defect | XCTAssertEqual(detailedItem, "Movie B", "Ordinary details control must trigger refreshed callback") |
| `8ddc33e689cf` | misses defect | test_configure_setsVisibleButtonTitles() |
| `b522270644f6` | misses defect | testButtonsDisplayVisibleTitlesWhenConfigured() |
| `5a2986e7b932` | misses defect | testButtonsDisplayConfiguredTitles() |
| `c4a0781e6142` | catches supplied defect | XCTAssertEqual(item2DetailsCount, 1, "Item 2 details should be invoked") |
| `5d23276a611d` | misses defect | testRefreshOperatesOnNewItem() |
| `437c3ec3723e` | catches supplied defect | XCTAssertTrue(secondDetailsCalled) |
| `62cdda3b487a` | misses defect | test_configure_setsVisualTitlesForBothButtons() |
| `bbbdb36c2438` | misses defect | test_configure_setsVisibleButtonTitles() |
| `3ca357f1ebb7` | misses defect | testButtonsDisplayVisibleTitlesAfterConfiguration() |
| `cf368d190054` | misses defect | test_configure_setsVisibleButtonTitles() |
| `4946f65f88cf` | misses defect | test_configure_setsVisibleButtonTitles() |
| `45692861cf0a` | misses defect | testButtonsDisplayVisibleTitles() |
| `0b9d6bbe5c15` | runtime crash (not a catch) |  |
| `c0131963a21e` | runtime crash (not a catch) |  |
| `6bcec758e5c8` | misses defect | testButtonsDisplayVisibleTitlesWhenConfigured() |
| `f27f29e86f4b` | misses defect | test_configure_setsVisibleTitlesOnButtons() |
| `f7c08fb74e5b` | runtime crash (not a catch) |  |
| `9f5abcb6f0f6` | catches supplied defect | XCTAssertEqual(secondDetailsCount, 1) |
| `1c542d7a963c` | misses defect | testButtonsDisplayVisibleTitles() |
| `72171cf6662a` | misses defect | testConfigureSetsVisibleButtonTitlesOnScreen() |

## Q092

| Submitted proof | Native result | Evidence |
|---|---|---|
| `d6ad4c1378ef` | interface/discovery gap | type 'MotionPolicy' has no member 'performOptionalAnimation' |
| `cc02480568ee` | catches supplied defect | XCTAssertEqual(MotionPolicy.duration(reduceMotion: true), 0.0, "Reduced motion should eliminate the animation duration.") |

## Q099

| Submitted proof | Native result | Evidence |
|---|---|---|
| `580aae35a83b` | misses defect | testMovedButtonBehavior() |
| `8fbb5e8a25ad` | runtime crash (not a catch) |  |
| `b6cc38ec59b0` | runtime crash (not a catch) |  |
| `701f0f066caf` | misses defect | testDetachedButtonCannotChooseItemWhileAttachedButtonCan() |
| `a9afb0ccad62` | misses defect | testApply_rejectsDuplicateItemIDsWithoutMutatingState() |
| `d4f69c6fb9e8` | misses defect | testStaleActionDoesNotTriggerAfterRefresh() |
| `083b83eda2fe` | rejects valid code | working: XCTAssertTrue failed |
| `9d779c803c47` | misses defect | testApplyRejectsDuplicateSectionIDsWithoutPartialUpdate() |
| `93c81135792a` | misses defect | testDetachedRetainedButtonCannotActOnShelf() |

# Controller answer key

Keep this file outside subject sessions. Each XCTest excerpt belongs to the linked suite, which contains its setup and helpers. Accept equivalent observable behavior.

## Q001 · implementation repair

After a document becomes read-only its button still exposes editing actions. Can you update only the metadata owned by this feature?

[Working implementation](../../code-examples/pilots/uikit-lifecycle-v1/Sources/LifecycleUIKit.swift) · [Defective implementation](../../code-examples/pilots/uikit-lifecycle-v1/NegativeFixtures/StaleEditAction.swift) · [Full test suite](../../code-examples/pilots/uikit-lifecycle-v1/Tests/LifecycleUIKitTests.swift) · [Source contract](../../code-examples/pilots/uikit-lifecycle-v1/manifest.json)

Registered failing assertion(s): LifecycleUIKitTests/testReadOnlyStateRemovesEditCategoryAndHint.

```swift
func testReadOnlyStateRemovesEditCategoryAndHint() {
        let button = UIButton(type: .system)
        ContextActions.configure(button, editable: true) { _ in true }
        XCTAssertEqual(button.accessibilityCustomActions?.count, 1)
        XCTAssertEqual(button.accessibilityCustomActions?.first?.category, UIAccessibilityCustomAction.editCategory)
        ContextActions.configure(button, editable: false) { _ in true }
        XCTAssertEqual(button.accessibilityCustomActions?.count, 0)
        XCTAssertNil(button.accessibilityHint)
    }
```

## Q002 · test repair

We configured the bookmark twice and asserted only its label. Please exercise a trait owned by another feature through selection and deselection.

[Working implementation](../../code-examples/pilots/uikit-semantics-v1/Sources/UIKitSemantics.swift) · [Defective implementation](../../code-examples/pilots/uikit-semantics-v1/NegativeFixtures/LostTraits.swift) · [Full test suite](../../code-examples/pilots/uikit-semantics-v1/Tests/UIKitSemanticsTests.swift) · [Source contract](../../code-examples/pilots/uikit-semantics-v1/manifest.json)

Registered failing assertion(s): UIKitSemanticsTests/testSelectedTraitPreservesOtherTraits.

```swift
@MainActor func testSelectedTraitPreservesOtherTraits() {
        let button = UIButton(type: .system)
        button.accessibilityTraits.insert(.header)
        let original = button.accessibilityTraits
        SemanticConfiguration.configure(button, selected: true, hint: nil)
        XCTAssertEqual(button.accessibilityTraits, original.union(.selected))
        SemanticConfiguration.configure(button, selected: false, hint: nil)
        XCTAssertEqual(button.accessibilityTraits, original.subtracting(.selected))
    }
```

## Q003 · implementation repair

My checker returns a definitive contrast ratio for a translucent overlay even when its backdrop is unknown. Can you implement the documented opaque-only policy?

[Working implementation](../../code-examples/pilots/uikit-contrast-v1/Sources/ContrastUIKit.swift) · [Defective implementation](../../code-examples/pilots/uikit-contrast-v1/NegativeFixtures/IgnoredAlpha.swift) · [Full test suite](../../code-examples/pilots/uikit-contrast-v1/Tests/ContrastUIKitTests.swift) · [Source contract](../../code-examples/pilots/uikit-contrast-v1/manifest.json)

Registered failing assertion(s): ContrastUIKitTests/testTranslucentForegroundAndBackgroundAreRejected.

```swift
func testTranslucentForegroundAndBackgroundAreRejected() throws {
        let t = traits(.light)
        XCTAssertThrowsError(try ConfiguredContrast.ratio(foreground: .black.withAlphaComponent(0.5), background: .white, traits: t)) {
            XCTAssertEqual($0 as? ContrastError, .translucent)
        }
        XCTAssertThrowsError(try ConfiguredContrast.ratio(foreground: .black, background: .white.withAlphaComponent(0.5), traits: t)) {
            XCTAssertEqual($0 as? ContrastError, .translucent)
        }
    }
```

## Q004 · implementation repair

Searching this Mac document can return part of a composed character. Can you restrict matches to whole text boundaries while keeping valid adjacent matches?

[Working implementation](../../code-examples/platforms/macos-closure-v1/Sources/DesktopText.swift) · [Defective implementation](../../code-examples/platforms/macos-closure-v1/NegativeFixtures/text_boundary.swift) · [Full test suite](../../code-examples/platforms/macos-closure-v1/Tests/DesktopTextTests.swift) · [Source contract](../../code-examples/platforms/macos-closure-v1/manifest.json)

Registered failing assertion(s): DesktopTextTests/testPartialGraphemesExcluded.

```swift
func testPartialGraphemesExcluded() {
        XCTAssertTrue(LiteralMatches.ranges(in: "e\u{301}", query: "e", allowOverlaps: false).isEmpty)
        XCTAssertTrue(LiteralMatches.ranges(in: "\u{1F469}\u{200D}\u{1F4BB}", query: "\u{1F469}", allowOverlaps: true).isEmpty)
    }
```

## Q005 · implementation repair

Refreshing an unchanged status keeps replaying its animation. Can you keep repeated updates quiet and still animate a genuine change when permitted?

[Working implementation](../../code-examples/platforms/tvos-results-v1/Sources/TelevisionResults.swift) · [Defective implementation](../../code-examples/platforms/tvos-results-v1/NegativeFixtures/RepeatedAnimation.swift) · [Full test suite](../../code-examples/platforms/tvos-results-v1/Tests/TelevisionResultsTests.swift) · [Source contract](../../code-examples/platforms/tvos-results-v1/manifest.json)

Registered failing assertion(s): TelevisionResultsTests/testRepeatedStatusIsQuiet.

```swift
func testRepeatedStatusIsQuiet() { var animations = 0; let s = TelevisionStatus(reduceMotion: {false}, animate: {animations += 1}); s.update("Ready"); s.update("Ready"); XCTAssertEqual(animations, 1) }
```

## Q006 · test repair

Our rotor test checks only whether the search index accepted the initial data. It should detect a missing or misordered accessibility element after a reorder. Check the container and the rotor installed on the view.

[Working implementation](../../code-examples/pilots/uikit-dynamic-v1/Sources/DynamicUIKit.swift) · [Defective implementation](../../code-examples/pilots/uikit-dynamic-v1/NegativeFixtures/MissingElements.swift) · [Full test suite](../../code-examples/pilots/uikit-dynamic-v1/Tests/DynamicUIKitTests.swift) · [Source contract](../../code-examples/pilots/uikit-dynamic-v1/manifest.json)

Registered failing assertion(s): DynamicUIKitTests/testReorderPreservesIdentityAndChangesSearchOrder.

```swift
@MainActor func testReorderPreservesIdentityAndChangesSearchOrder() {
        let view = DynamicSections(frame: .zero)
        view.replace(records)
        let a = view.labels[0], b = view.labels[1], c = view.labels[2]
        view.replace([records[2], records[0], records[1]])
        XCTAssertTrue(view.labels[0] === c)
        XCTAssertTrue(view.labels[1] === a)
        XCTAssertTrue(search(view, from: c)?.targetElement === a)
        XCTAssertTrue(search(view, from: a)?.targetElement === b)
        XCTAssertTrue((view.accessibilityElements as? [UIView])?.first === c)
    }
```

## Q007 · implementation repair

A preference update queued before stop arrives after we restart observation. Can you prevent it from overwriting the new session’s effective preference?

[Working implementation](../../code-examples/platforms/macos-lifecycle-v1/Sources/DesktopLifecycle.swift) · [Defective implementation](../../code-examples/platforms/macos-lifecycle-v1/NegativeFixtures/OldGeneration.swift) · [Full test suite](../../code-examples/platforms/macos-lifecycle-v1/Tests/DesktopLifecycleTests.swift) · [Source contract](../../code-examples/platforms/macos-lifecycle-v1/manifest.json)

Registered failing assertion(s): DesktopLifecycleTests/testPreferenceOldGenerationIgnoredAfterRestart.

```swift
func testPreferenceOldGenerationIgnoredAfterRestart() { let h = PreferenceHarness(); h.observer.start(); h.post(); h.observer.stop(); h.observer.start(); h.drain(); XCTAssertEqual(h.reads, 2) }
```

## Q008 · implementation repair

A saved rotor from the previous search still returns matches after the query changes. Can the current search work while the old one expires?

[Working implementation](../../code-examples/pilots/uikit-edited-rotor-v1/Sources/EditedRotorUIKit.swift) · [Defective implementation](../../code-examples/pilots/uikit-edited-rotor-v1/NegativeFixtures/OldRotor.swift) · [Full test suite](../../code-examples/pilots/uikit-edited-rotor-v1/Tests/EditedRotorUIKitTests.swift) · [Source contract](../../code-examples/pilots/uikit-edited-rotor-v1/manifest.json)

Registered failing assertion(s): EditedRotorUIKitTests/testRetainedOldRotorIsInvalidAfterQueryChange.

```swift
func testRetainedOldRotorIsInvalidAfterQueryChange() throws {
        let reader = EditedMatchReader()
        reader.replace(text: "cat dog cat", query: "cat")
        let old = try XCTUnwrap(reader.textView.accessibilityCustomRotors?.first)
        reader.replace(text: "cat dog cat", query: "dog")
        XCTAssertNil(search(reader, rotor: old))
        XCTAssertEqual(location(search(reader), in: reader), 4)
    }
```

## Q009 · implementation repair

Our seating chart has a seat that spans multiple coordinates. Looking it up by the first coordinate works but another covered coordinate gives the wrong result. Can you repair the table lookup?

[Working implementation](../../code-examples/pilots/uikit-containers-v1/Sources/ContainerUIKit.swift) · [Defective implementation](../../code-examples/pilots/uikit-containers-v1/NegativeFixtures/WrongSpan.swift) · [Full test suite](../../code-examples/pilots/uikit-containers-v1/Tests/ContainerUIKitTests.swift) · [Source contract](../../code-examples/pilots/uikit-containers-v1/manifest.json)

Registered failing assertion(s): ContainerUIKitTests/testSpanningCellResolvesEveryCoveredCoordinate.

```swift
func testSpanningCellResolvesEveryCoveredCoordinate() {
        let grid = DataGrid(rows: 3, columns: 3)
        XCTAssertTrue(grid.insert(label: "Combined", rows: NSRange(location: 1, length: 2), columns: NSRange(location: 0, length: 2)))
        let cell = grid.cells[0]
        XCTAssertEqual(cell.accessibilityRowRange(), NSRange(location: 1, length: 2))
        XCTAssertEqual(cell.accessibilityColumnRange(), NSRange(location: 0, length: 2))
        for row in 1...2 {
            for column in 0...1 {
                XCTAssertTrue((grid.accessibilityDataTableCellElement(forRow: row, column: column) as? DataCell) === cell)
            }
        }
        XCTAssertNil(grid.accessibilityDataTableCellElement(forRow: 0, column: 0))
        XCTAssertNil(grid.accessibilityDataTableCellElement(forRow: 1, column: 2))
    }
```

## Q010 · test repair

Our contrast test covers only black against white. It still passes with the wrong luminance calculation. Add a numerical fixture whose expected value comes from outside the function under test.

[Working implementation](../../code-examples/pilots/uikit-contrast-v1/Sources/ContrastUIKit.swift) · [Defective implementation](../../code-examples/pilots/uikit-contrast-v1/NegativeFixtures/NoLinearization.swift) · [Full test suite](../../code-examples/pilots/uikit-contrast-v1/Tests/ContrastUIKitTests.swift) · [Source contract](../../code-examples/pilots/uikit-contrast-v1/manifest.json)

Registered failing assertion(s): ContrastUIKitTests/testUIKitGrayConversionUsesLinearLuminance.

```swift
func testUIKitGrayConversionUsesLinearLuminance() throws {
        let color = UIColor(white: 0.5, alpha: 1)
        let resolved = try ConfiguredContrast.resolve(color, traits: traits(.light))
        XCTAssertEqual(resolved.luminance, 0.21404114048223255, accuracy: 0.00001)
        XCTAssertEqual(try ConfiguredContrast.ratio(foreground: color, background: .white, traits: traits(.light)),
                       3.976653024912438, accuracy: 0.0001)
    }
```

## Q011 · implementation repair

Before a finite video finishes loading, our inspector sometimes calls it a live stream. Can you represent what is known about its duration without inventing a stream type?

[Working implementation](../../code-examples/pilots/uikit-media-inspection-v1/Sources/MediaInspection.swift) · [Defective implementation](../../code-examples/pilots/uikit-media-inspection-v1/NegativeFixtures/InferredLive.swift) · [Full test suite](../../code-examples/pilots/uikit-media-inspection-v1/Tests/MediaInspectionTests.swift) · [Source contract](../../code-examples/pilots/uikit-media-inspection-v1/manifest.json)

Registered failing assertion(s): MediaInspectionTests/testIndefiniteDoesNotInventLiveClassification.

```swift
func testIndefiniteDoesNotInventLiveClassification() {
        XCTAssertEqual(snapshot(duration: .indefinite).kind, .unknown)
        XCTAssertEqual(snapshot(duration: time(60), kind: .live).kind, .live)
        XCTAssertEqual(snapshot(duration: .indefinite, kind: .onDemand).kind, .onDemand)
    }
```

## Q012 · implementation repair

Opening the inspector before a player item exists tells users there are no accessible tracks. Can you distinguish unavailable inspection from a known empty result?

[Working implementation](../../code-examples/pilots/uikit-media-metadata-v1/Sources/MediaMetadata.swift) · [Defective implementation](../../code-examples/pilots/uikit-media-metadata-v1/NegativeFixtures/NoItemAbsent.swift) · [Full test suite](../../code-examples/pilots/uikit-media-metadata-v1/Tests/MediaMetadataTests.swift) · [Source contract](../../code-examples/pilots/uikit-media-metadata-v1/manifest.json)

Registered failing assertion(s): MediaMetadataTests/testMissingItemIsUnavailableRatherThanAbsent.

```swift
func testMissingItemIsUnavailableRatherThanAbsent() async throws {
        let result = try await MediaMetadata.group(.audible, item: nil)
        let unavailable: Bool
        if case .unavailable = result { unavailable = true } else { unavailable = false }
        XCTAssertTrue(unavailable)
    }
```

## Q013 · implementation repair

Choosing the already-selected speed emits another playback change. Can you keep repeated selections quiet and still notify exactly once when the rate changes?

[Working implementation](../../code-examples/pilots/uikit-speed-v1/Sources/PlaybackSpeed.swift) · [Defective implementation](../../code-examples/pilots/uikit-speed-v1/NegativeFixtures/RepeatedChange.swift) · [Full test suite](../../code-examples/pilots/uikit-speed-v1/Tests/PlaybackSpeedTests.swift) · [Source contract](../../code-examples/pilots/uikit-speed-v1/manifest.json)

Registered failing assertion(s): PlaybackSpeedTests/testRepeatedSelectionDoesNotEmitDuplicateChange.

```swift
func testRepeatedSelectionDoesNotEmitDuplicateChange() {
        let view = PlaybackSpeedChoices()
        var calls: [Float] = []
        view.onChange = { calls.append($0) }
        XCTAssertTrue(view.select(1))
        view.buttons[2].sendActions(for: .primaryActionTriggered)
        view.buttons[2].sendActions(for: .primaryActionTriggered)
        XCTAssertEqual(calls, [1.5])
    }
```

## Q014 · implementation repair

Embedding the player removes the ordinary transport controls our users rely on. Can you restore native controls and preserve automatic media selection?

[Working implementation](../../code-examples/pilots/uikit-media-v1/Sources/MediaUIKit.swift) · [Defective implementation](../../code-examples/pilots/uikit-media-v1/NegativeFixtures/HiddenControls.swift) · [Full test suite](../../code-examples/pilots/uikit-media-v1/Tests/MediaUIKitTests.swift) · [Source contract](../../code-examples/pilots/uikit-media-v1/manifest.json)

Registered failing assertion(s): MediaUIKitTests/testNativeControllerPreservesControlsAndAutomaticSelection.

```swift
func testNativeControllerPreservesControlsAndAutomaticSelection() {
        let player = AVPlayer()
        let controller = MediaConfiguration.controller(player: player)
        XCTAssertTrue(controller.player === player)
        XCTAssertTrue(controller.showsPlaybackControls)
        XCTAssertFalse(controller.requiresLinearPlayback)
        XCTAssertTrue(player.appliesMediaSelectionCriteriaAutomatically)
        XCTAssertEqual(player.rate, 0)
    }
```

## Q015 · implementation repair

Selecting an option removes traits another part of the app installed. How should this component change its own state while preserving the rest?

[Working implementation](../../code-examples/pilots/uikit-choice-v1/Sources/ChoiceUIKit.swift) · [Defective implementation](../../code-examples/pilots/uikit-choice-v1/NegativeFixtures/ClobberedTraits.swift) · [Full test suite](../../code-examples/pilots/uikit-choice-v1/Tests/ChoiceUIKitTests.swift) · [Source contract](../../code-examples/pilots/uikit-choice-v1/manifest.json)

Registered failing assertion(s): ChoiceUIKitTests/testSelectionUpdatesPreserveUnrelatedTraits.

```swift
func testSelectionUpdatesPreserveUnrelatedTraits() {
        let row = cell()
        row.accessibilityTraits.insert(.updatesFrequently)
        for chosen in [true, false, true] {
            configure(row, chosen: chosen)
            XCTAssertTrue(row.accessibilityTraits.contains(.updatesFrequently))
            XCTAssertEqual(row.accessibilityTraits.contains(.selected), chosen)
        }
    }
```

## Q016 · implementation repair

After leaving this screen, preference changes still call back into its observer. Can you fix stop and restart, including the first value after returning?

[Working implementation](../../code-examples/pilots/uikit-lifecycle-v1/Sources/LifecycleUIKit.swift) · [Defective implementation](../../code-examples/pilots/uikit-lifecycle-v1/NegativeFixtures/UnstoppedObserver.swift) · [Full test suite](../../code-examples/pilots/uikit-lifecycle-v1/Tests/LifecycleUIKitTests.swift) · [Source contract](../../code-examples/pilots/uikit-lifecycle-v1/manifest.json)

Registered failing assertion(s): LifecycleUIKitTests/testStopRemovesObserverAndRestartRefreshes.

```swift
func testStopRemovesObserverAndRestartRefreshes() {
        let center = NotificationCenter()
        var preference = false, reads = 0
        let model = MotionPreference(center: center) { reads += 1; return preference }
        model.stop()
        preference = true
        center.post(name: UIAccessibility.reduceMotionStatusDidChangeNotification, object: nil)
        XCTAssertEqual(reads, 1)
        XCTAssertFalse(model.reduceMotion)
        model.start()
        XCTAssertEqual(reads, 2)
        XCTAssertTrue(model.reduceMotion)
        center.post(name: UIAccessibility.reduceMotionStatusDidChangeNotification, object: nil)
        XCTAssertEqual(reads, 3)
    }
```

## Q017 · implementation repair

When Reduce Motion is on, this transition still takes the animated path. Can you keep the final content update and prove which transition was requested?

[Working implementation](../../code-examples/pilots/uikit-preferences-v1/Sources/PreferenceUIKit.swift) · [Defective implementation](../../code-examples/pilots/uikit-preferences-v1/NegativeFixtures/IgnoredMotion.swift) · [Full test suite](../../code-examples/pilots/uikit-preferences-v1/Tests/PreferenceUIKitTests.swift) · [Source contract](../../code-examples/pilots/uikit-preferences-v1/manifest.json)

Registered failing assertion(s): PreferenceUIKitTests/testReducedMotionUsesImmediateTransition.

```swift
func testReducedMotionUsesImmediateTransition() {
        XCTAssertEqual(MotionPolicy.duration(reduceMotion: true), 0)
    }
```

## Q018 · test repair

Our reuse test checks the new title and misses a retained Remove action affecting the replacement item. How would you exercise the originally installed action after the change?

[Working implementation](../../code-examples/pilots/uikit-reuse-v1/Sources/ReuseUIKit.swift) · [Defective implementation](../../code-examples/pilots/uikit-reuse-v1/NegativeFixtures/StaleIdentity.swift) · [Full test suite](../../code-examples/pilots/uikit-reuse-v1/Tests/ReuseUIKitTests.swift) · [Source contract](../../code-examples/pilots/uikit-reuse-v1/manifest.json)

Registered failing assertion(s): ReuseUIKitTests/testRetainedActionRejectsReconfiguredIdentity.

```swift
func testRetainedActionRejectsReconfiguredIdentity() {
        let cell = SavedItemCell()
        var removed: [String] = []
        cell.onRemove = { removed.append($0) }
        cell.configure(id: "old", title: "Old", saved: true, removable: true, language: "en")
        let old = cell.accessibilityCustomActions![0]
        cell.configure(id: "new", title: "New", saved: true, removable: true, language: "en")
        XCTAssertFalse(old.actionHandler!(old))
        let current = cell.accessibilityCustomActions![0]
        XCTAssertTrue(current.actionHandler!(current))
        XCTAssertEqual(removed, ["new"])
    }
```

## Q019 · implementation repair

The shortcut has a contextual name but sighted users can’t tell what the visible action buttons do. Can you restore their ordinary titles and preserve the shortcuts?

[Working implementation](../../code-examples/platforms/tvos-uikit-v1/Sources/TelevisionActions.swift) · [Defective implementation](../../code-examples/platforms/tvos-uikit-v1/NegativeFixtures/OriginalMissingTitles.swift) · [Full test suite](../../code-examples/platforms/tvos-uikit-v1/Tests/TelevisionActionsTests.swift) · [Source contract](../../code-examples/platforms/tvos-uikit-v1/manifest.json)

Registered failing assertion(s): TelevisionActionsTests/testVisibleActionNames.

```swift
func testVisibleActionNames() { let r = row(); XCTAssertEqual(r.play.title(for: .normal), "Play Episode A"); XCTAssertEqual(r.details.title(for: .normal), "Details Episode A") }
```

## Q020 · implementation repair

Submitting an invalid value can still invoke Save. Can the form retain the entered text, surface the error, and wait for a valid submission?

[Working implementation](../../code-examples/platforms/macos-structure-v1/Sources/DesktopForm.swift) · [Defective implementation](../../code-examples/platforms/macos-structure-v1/NegativeFixtures/InvalidSaves.swift) · [Full test suite](../../code-examples/platforms/macos-structure-v1/Tests/DesktopFormTests.swift) · [Source contract](../../code-examples/platforms/macos-structure-v1/manifest.json)

Registered failing assertion(s): DesktopFormTests/testInvalidInputShowsErrorWithoutSavingOrErasing.

```swift
func testInvalidInputShowsErrorWithoutSavingOrErasing() {
        var saved: [String] = []
        let f = DesktopForm(validate: { _ in "Check address" }, save: { saved.append($0) })
        f.field.stringValue = "bad input"; f.submit()
        XCTAssertEqual(f.field.stringValue, "bad input")
        XCTAssertEqual(f.errorLabel.stringValue, "Check address")
        XCTAssertFalse(f.errorLabel.isHidden)
        XCTAssertTrue(f.errorLabel.isAccessibilityElement())
        XCTAssertTrue(saved.isEmpty)
    }
```

## Q021 · implementation repair

After sorting results, the container’s exposed elements no longer match the visible items. Can you update the order while preserving the identity of surviving elements?

[Working implementation](../../code-examples/pilots/uikit-dynamic-v1/Sources/DynamicUIKit.swift) · [Defective implementation](../../code-examples/pilots/uikit-dynamic-v1/NegativeFixtures/MissingElements.swift) · [Full test suite](../../code-examples/pilots/uikit-dynamic-v1/Tests/DynamicUIKitTests.swift) · [Source contract](../../code-examples/pilots/uikit-dynamic-v1/manifest.json)

Registered failing assertion(s): DynamicUIKitTests/testReorderPreservesIdentityAndChangesSearchOrder.

```swift
@MainActor func testReorderPreservesIdentityAndChangesSearchOrder() {
        let view = DynamicSections(frame: .zero)
        view.replace(records)
        let a = view.labels[0], b = view.labels[1], c = view.labels[2]
        view.replace([records[2], records[0], records[1]])
        XCTAssertTrue(view.labels[0] === c)
        XCTAssertTrue(view.labels[1] === a)
        XCTAssertTrue(search(view, from: c)?.targetElement === a)
        XCTAssertTrue(search(view, from: a)?.targetElement === b)
        XCTAssertTrue((view.accessibilityElements as? [UIView])?.first === c)
    }
```

## Q022 · implementation repair

Our media inspector reports the chosen audio track as unselected. Can you report the real selection accurately while keeping the player and its subtitle Off state unchanged?

[Working implementation](../../code-examples/pilots/uikit-media-metadata-v1/Sources/MediaMetadata.swift) · [Defective implementation](../../code-examples/pilots/uikit-media-metadata-v1/NegativeFixtures/SelectionLost.swift) · [Full test suite](../../code-examples/pilots/uikit-media-metadata-v1/Tests/MediaMetadataTests.swift) · [Source contract](../../code-examples/pilots/uikit-media-metadata-v1/manifest.json)

Registered failing assertion(s): MediaMetadataTests/testInspectionPreservesChosenAudioAndSubtitleOff.

```swift
func testInspectionPreservesChosenAudioAndSubtitleOff() async throws {
        let url = try DescriptionFixture.write(tagged: true)
        defer { try? FileManager.default.removeItem(at: url) }
        let asset = AVURLAsset(url: url)
        let loadedAudio = try await asset.loadMediaSelectionGroup(for: .audible)
        let loadedText = try await asset.loadMediaSelectionGroup(for: .legible)
        let audio = try XCTUnwrap(loadedAudio)
        let text = try XCTUnwrap(loadedText)
        let chosen = try XCTUnwrap(audio.options.first { $0.hasMediaCharacteristic(.describesVideoForAccessibility) })
        let item = AVPlayerItem(asset: asset)
        item.select(chosen, in: audio)
        item.select(nil, in: text)
        let rows = options(try await MediaMetadata.group(.audible, item: item))
        let captions = options(try await MediaMetadata.group(.legible, item: item))
        XCTAssertEqual(rows.filter(\.selected).count, 1)
        XCTAssertEqual(rows.first(where: { $0.selected })?.describesVideo, true)
        XCTAssertEqual(item.currentMediaSelection.selectedMediaOption(in: audio), chosen)
        XCTAssertNil(item.currentMediaSelection.selectedMediaOption(in: text))
        XCTAssertFalse(captions.contains(where: { $0.selected }))
    }
```

## Q023 · implementation repair

Removing a button from the form leaves its old next-key-view link alive. Can you release the links this helper installed during refresh and teardown?

[Working implementation](../../code-examples/platforms/macos-navigation-v1/Sources/DesktopNavigation.swift) · [Defective implementation](../../code-examples/platforms/macos-navigation-v1/NegativeFixtures/LeakedKeyLinks.swift) · [Full test suite](../../code-examples/platforms/macos-navigation-v1/Tests/DesktopNavigationTests.swift) · [Source contract](../../code-examples/platforms/macos-navigation-v1/manifest.json)

Registered failing assertion(s): DesktopNavigationTests/testRemovedKeyLinksCleared.

```swift
func testRemovedKeyLinksCleared() { let a = button(), b = button(), order = DesktopKeyOrder(); order.apply([a,b]); order.apply([a]); XCTAssertNil(b.nextKeyView); XCTAssertTrue(a.nextKeyView === a) }
```

## Q024 · test repair

Our validation test simulates an edit using only the controller's public edit method. What test would expose a stale success after a text field was changed directly?

[Working implementation](../../code-examples/platforms/ios-closure-v1/Sources/AsyncOwnership.swift) · [Defective implementation](../../code-examples/platforms/ios-closure-v1/NegativeFixtures/validation_snapshot.swift) · [Full test suite](../../code-examples/platforms/ios-closure-v1/Tests/AsyncOwnershipTests.swift) · [Source contract](../../code-examples/platforms/ios-closure-v1/manifest.json)

Registered failing assertion(s): AsyncOwnershipTests/testNativeFieldMutationCannotApplyOldSnapshot.

```swift
func testNativeFieldMutationCannotApplyOldSnapshot() {
        var accepted = 0; let o = owner(accept: { _ in accepted += 1 }); o.submit()
        o.fields["name"]?.text = "Changed outside adapter"; replies[0]([:])
        XCTAssertEqual(accepted, 0); XCTAssertFalse(o.busy)
    }
```

## Q025 · implementation repair

The same dynamic foreground and background give us the same audit result under two explicitly supplied appearances. Can the checker honor the appearance being audited?

[Working implementation](../../code-examples/pilots/uikit-contrast-v1/Sources/ContrastUIKit.swift) · [Defective implementation](../../code-examples/pilots/uikit-contrast-v1/NegativeFixtures/IgnoredTraits.swift) · [Full test suite](../../code-examples/pilots/uikit-contrast-v1/Tests/ContrastUIKitTests.swift) · [Source contract](../../code-examples/pilots/uikit-contrast-v1/manifest.json)

Registered failing assertion(s): ContrastUIKitTests/testDynamicColorsUseExplicitStyleAndContrast.

```swift
func testDynamicColorsUseExplicitStyleAndContrast() throws {
        let dynamic = UIColor { t in
            if t.accessibilityContrast == .high { return t.userInterfaceStyle == .dark ? .white : .black }
            return UIColor(white: t.userInterfaceStyle == .dark ? 0.8 : 0.2, alpha: 1)
        }
        for style: UIUserInterfaceStyle in [.light, .dark] {
            for contrast: UIAccessibilityContrast in [.normal, .high] {
                let result = try ConfiguredContrast.resolve(dynamic, traits: traits(style, contrast))
                let expected: Double = contrast == .high ? (style == .dark ? 1 : 0) : (style == .dark ? 0.8 : 0.2)
                XCTAssertEqual(result.red, expected, accuracy: 0.0001)
            }
        }
    }
```

## Q026 · implementation repair

The preferred focus list includes a disabled control after a state change. Can you return eligible candidates and preserve their intended order?

[Working implementation](../../code-examples/platforms/tvos-uikit-v1/Sources/TelevisionActions.swift) · [Defective implementation](../../code-examples/platforms/tvos-uikit-v1/NegativeFixtures/InvalidFocusTarget.swift) · [Full test suite](../../code-examples/platforms/tvos-uikit-v1/Tests/TelevisionActionsTests.swift) · [Source contract](../../code-examples/platforms/tvos-uikit-v1/manifest.json)

Registered failing assertion(s): TelevisionActionsTests/testDisabledPreferredTargetExcluded.

```swift
func testDisabledPreferredTargetExcluded() { let r = row(); r.play.isEnabled = false; XCTAssertTrue(r.preferredFocusEnvironments.first === r.details) }
```

## Q027 · test repair

The grid test passes even if looking up the covered portion of a spanning seat returns nil. Give us a regression test for the actual lookup, including an uncovered coordinate.

[Working implementation](../../code-examples/pilots/uikit-containers-v1/Sources/ContainerUIKit.swift) · [Defective implementation](../../code-examples/pilots/uikit-containers-v1/NegativeFixtures/WrongSpan.swift) · [Full test suite](../../code-examples/pilots/uikit-containers-v1/Tests/ContainerUIKitTests.swift) · [Source contract](../../code-examples/pilots/uikit-containers-v1/manifest.json)

Registered failing assertion(s): ContainerUIKitTests/testSpanningCellResolvesEveryCoveredCoordinate.

```swift
func testSpanningCellResolvesEveryCoveredCoordinate() {
        let grid = DataGrid(rows: 3, columns: 3)
        XCTAssertTrue(grid.insert(label: "Combined", rows: NSRange(location: 1, length: 2), columns: NSRange(location: 0, length: 2)))
        let cell = grid.cells[0]
        XCTAssertEqual(cell.accessibilityRowRange(), NSRange(location: 1, length: 2))
        XCTAssertEqual(cell.accessibilityColumnRange(), NSRange(location: 0, length: 2))
        for row in 1...2 {
            for column in 0...1 {
                XCTAssertTrue((grid.accessibilityDataTableCellElement(forRow: row, column: column) as? DataCell) === cell)
            }
        }
        XCTAssertNil(grid.accessibilityDataTableCellElement(forRow: 0, column: 0))
        XCTAssertNil(grid.accessibilityDataTableCellElement(forRow: 1, column: 2))
    }
```

## Q028 · implementation repair

When full English subtitles are requested, our picker sometimes chooses a forced-dialogue-only option. Can you select the intended track and retain the Off path?

[Working implementation](../../code-examples/pilots/uikit-media-v1/Sources/MediaUIKit.swift) · [Defective implementation](../../code-examples/pilots/uikit-media-v1/NegativeFixtures/ForcedOnly.swift) · [Full test suite](../../code-examples/pilots/uikit-media-v1/Tests/MediaUIKitTests.swift) · [Source contract](../../code-examples/pilots/uikit-media-v1/manifest.json)

Registered failing assertion(s): MediaUIKitTests/testSubtitleSelectionAndOffState.

```swift
func testSubtitleSelectionAndOffState() async throws {
        let url = try MediaFixture.write()
        defer { try? FileManager.default.removeItem(at: url) }
        let asset = AVURLAsset(url: url)
        let loaded = try await asset.loadMediaSelectionGroup(for: .legible)
        let group = try XCTUnwrap(loaded)
        let item = AVPlayerItem(asset: asset)
        XCTAssertTrue(MediaConfiguration.select(language: "es", in: group, item: item))
        XCTAssertEqual(MediaConfiguration.selectedLanguage(in: group, item: item), "es")
        XCTAssertEqual(item.currentMediaSelection.selectedMediaOption(in: group)?.hasMediaCharacteristic(.containsOnlyForcedSubtitles), false)
        item.select(nil, in: group)
        XCTAssertNil(item.currentMediaSelection.selectedMediaOption(in: group))
    }
```

## Q029 · implementation repair

Renaming an outline node recreates it, even though it represents the same document. Can you preserve the surviving node object through refresh?

[Working implementation](../../code-examples/platforms/macos-structure-v1/Sources/DesktopOutline.swift) · [Defective implementation](../../code-examples/platforms/macos-structure-v1/NegativeFixtures/LostIdentity.swift) · [Full test suite](../../code-examples/platforms/macos-structure-v1/Tests/DesktopOutlineTests.swift) · [Source contract](../../code-examples/platforms/macos-structure-v1/manifest.json)

Registered failing assertion(s): DesktopOutlineTests/testRenameRetainsStableNodeIdentity.

```swift
func testRenameRetainsStableNodeIdentity() throws {
        let d = configured(), original = try XCTUnwrap(d.nodes["a"])
        XCTAssertTrue(d.apply([Item(id: "a", title: "Renamed")]))
        XCTAssertTrue(d.nodes["a"] === original); XCTAssertEqual(original.title, "Renamed")
    }
```

## Q030 · implementation repair

When a selected child’s siblings change order, the outline selects a different child. Can you restore the intended item after refresh?

[Working implementation](../../code-examples/platforms/macos-structure-v1/Sources/DesktopOutline.swift) · [Defective implementation](../../code-examples/platforms/macos-structure-v1/NegativeFixtures/LostSelection.swift) · [Full test suite](../../code-examples/platforms/macos-structure-v1/Tests/DesktopOutlineTests.swift) · [Source contract](../../code-examples/platforms/macos-structure-v1/manifest.json)

Registered failing assertion(s): DesktopOutlineTests/testSelectedChildSurvivesSiblingReorder.

```swift
func testSelectedChildSurvivesSiblingReorder() throws {
        let d = configured(); d.outline.expandItem(try XCTUnwrap(d.nodes["g"])); d.select("b")
        XCTAssertEqual(d.selectedID, "b")
        XCTAssertTrue(d.apply([Item(id: "g", title: "Group", children: [Item(id: "b", title: "Beta"), Item(id: "a", title: "Alpha")])]))
        XCTAssertEqual(d.selectedID, "b")
    }
```

## Q031 · test repair

Our dismissal test inspects only the eventual notification count. It misses a focus request sent before the animation completion. Capture the intermediate state and check the final target.

[Working implementation](../../code-examples/pilots/uikit-modal-v1/Sources/ModalUIKit.swift) · [Defective implementation](../../code-examples/pilots/uikit-modal-v1/NegativeFixtures/EarlyNotification.swift) · [Full test suite](../../code-examples/pilots/uikit-modal-v1/Tests/ModalUIKitTests.swift) · [Source contract](../../code-examples/pilots/uikit-modal-v1/manifest.json)

Registered failing assertion(s): ModalUIKitTests/testNotificationWaitsForCompletionAndUsesCurrentTarget.

```swift
func testNotificationWaitsForCompletionAndUsesCurrentTarget() {
        let panel = RestoringPanel(), background = UIView(), first = UIButton(), replacement = UIButton()
        background.addSubview(first)
        background.addSubview(replacement)
        var completion: (@MainActor () -> Void)?, posts = 0
        panel.performDismissal = { completion = $0 }
        panel.post = { notification, target in
            posts += 1
            XCTAssertEqual(notification, .screenChanged)
            XCTAssertTrue((target as? UIView) === replacement)
            XCTAssertFalse(background.accessibilityElementsHidden)
            XCTAssertEqual(panel.state, .closed)
        }
        XCTAssertTrue(open(panel, background: background, target: first))
        XCTAssertTrue(panel.dismiss())
        XCTAssertEqual(posts, 0)
        XCTAssertTrue(background.accessibilityElementsHidden)
        panel.returnTarget = replacement
        completion?()
        completion?()
        XCTAssertEqual(posts, 1)
        XCTAssertNil(panel.returnTarget)
        panel.post = { _, _ in }
    }
```

## Q032 · implementation repair

Two invoices have the same displayed title. Sorting them loses the selection. Can you preserve the selection across the reorder?

[Working implementation](../../code-examples/platforms/macos-navigation-v1/Sources/DesktopNavigation.swift) · [Defective implementation](../../code-examples/platforms/macos-navigation-v1/NegativeFixtures/LostSelection.swift) · [Full test suite](../../code-examples/platforms/macos-navigation-v1/Tests/DesktopNavigationTests.swift) · [Source contract](../../code-examples/platforms/macos-navigation-v1/manifest.json)

Registered failing assertion(s): DesktopNavigationTests/testReorderPreservesIdentity.

```swift
func testReorderPreservesIdentity() { let r = results(); r.select("b"); r.apply([b,a]); XCTAssertEqual(r.table.selectedRow, 0); XCTAssertEqual(r.selectedID, "b") }
```

## Q033 · implementation repair

After a document edit, a search that starts from a retained result continues from the old position. Can it restart according to the current document revision?

[Working implementation](../../code-examples/pilots/uikit-edited-rotor-v1/Sources/EditedRotorUIKit.swift) · [Defective implementation](../../code-examples/pilots/uikit-edited-rotor-v1/NegativeFixtures/MissingRestart.swift) · [Full test suite](../../code-examples/pilots/uikit-edited-rotor-v1/Tests/EditedRotorUIKitTests.swift) · [Source contract](../../code-examples/pilots/uikit-edited-rotor-v1/manifest.json)

Registered failing assertion(s): EditedRotorUIKitTests/testNewRevisionRestartsRetainedResult.

```swift
func testNewRevisionRestartsRetainedResult() throws {
        let reader = EditedMatchReader()
        reader.replace(text: "cat dog cat", query: "cat")
        let last = try XCTUnwrap(search(reader, direction: .previous))
        reader.replace(text: "cat dog cat", query: "cat")
        XCTAssertEqual(location(search(reader, current: last), in: reader), 0)
    }
```

## Q034 · implementation repair

Two validations finish in reverse order. The earlier response can replace the newest field errors. Can you drive the captured completions and keep the current result?

[Working implementation](../../code-examples/platforms/ios-closure-v1/Sources/AsyncOwnership.swift) · [Defective implementation](../../code-examples/platforms/ios-closure-v1/NegativeFixtures/validation_generation.swift) · [Full test suite](../../code-examples/platforms/ios-closure-v1/Tests/AsyncOwnershipTests.swift) · [Source contract](../../code-examples/platforms/ios-closure-v1/manifest.json)

Registered failing assertion(s): AsyncOwnershipTests/testOutOfOrderReplyCannotReplaceLatestErrors.

```swift
func testOutOfOrderReplyCannotReplaceLatestErrors() {
        let o = owner(); o.submit(); o.submit()
        replies[1](["email":"Current"]); replies[0](["name":"Old"])
        XCTAssertEqual(o.errors, ["email":"Current"]); XCTAssertFalse(o.busy)
    }
```

## Q035 · implementation repair

Disabling this control stops normal interaction, but its accessibility activation can still submit. Can you align its return value and callback behavior in both states?

[Working implementation](../../code-examples/pilots/uikit-containers-v1/Sources/ContainerUIKit.swift) · [Defective implementation](../../code-examples/pilots/uikit-containers-v1/NegativeFixtures/IgnoredEnabled.swift) · [Full test suite](../../code-examples/pilots/uikit-containers-v1/Tests/ContainerUIKitTests.swift) · [Source contract](../../code-examples/pilots/uikit-containers-v1/manifest.json)

Registered failing assertion(s): ContainerUIKitTests/testDisabledActivationDoesNotInvokeHandler.

```swift
func testDisabledActivationDoesNotInvokeHandler() {
        let control = ActivationControl()
        var calls = 0
        control.perform = { calls += 1; return true }
        control.isEnabled = false
        XCTAssertFalse(control.accessibilityActivate())
        XCTAssertEqual(calls, 0)
    }
```

## Q036 · implementation repair

A retained result button can still choose an item after the shelf has been rebound. Can the current button respond to Select while the old button is inert?

[Working implementation](../../code-examples/platforms/tvos-results-v1/Sources/TelevisionResults.swift) · [Defective implementation](../../code-examples/platforms/tvos-results-v1/NegativeFixtures/StaleButton.swift) · [Full test suite](../../code-examples/platforms/tvos-results-v1/Tests/TelevisionResultsTests.swift) · [Source contract](../../code-examples/platforms/tvos-results-v1/manifest.json)

Registered failing assertion(s): TelevisionResultsTests/testStaleButtonDoesNotSelectReboundItem.

```swift
func testStaleButtonDoesNotSelectReboundItem() { let r = results(); let old = r.buttons[0]; r.apply([a,b]); old.sendActions(for: .primaryActionTriggered); XCTAssertNil(r.selectedID) }
```

## Q037 · implementation repair

After SwiftUI updates this represented view, an action retained before the update can still dispatch. Can you test a rebind through the coordinator used by the view?

[Working implementation](../../code-examples/swiftui/macos-v1/Sources/Interop.swift) · [Defective implementation](../../code-examples/swiftui/macos-v1/NegativeFixtures/interop.swift) · [Full test suite](../../code-examples/swiftui/macos-v1/Tests/InteropTests.swift) · [Source contract](../../code-examples/swiftui/macos-v1/manifest.json)

Registered failing assertion(s): InteropTests/testCoordinatorReplacesOldCallback.

```swift
func testCoordinatorReplacesOldCallback() { let c = BridgeOwner(), b = button(); var values: [String] = []; c.configure(b, title: "One", enabled: true, handler: { values.append("old") }); let old = c.action(); c.configure(b, title: "Two", enabled: true, handler: { values.append("new") }); old(); c.action()(); XCTAssertEqual(values, ["new"]) }
```

## Q038 · implementation repair

A malformed refresh repeats an invoice ID. Reject the refresh without changing the previous rows or selection. How would you prove nothing was partly applied?

[Working implementation](../../code-examples/platforms/macos-navigation-v1/Sources/DesktopNavigation.swift) · [Defective implementation](../../code-examples/platforms/macos-navigation-v1/NegativeFixtures/DuplicateIDs.swift) · [Full test suite](../../code-examples/platforms/macos-navigation-v1/Tests/DesktopNavigationTests.swift) · [Source contract](../../code-examples/platforms/macos-navigation-v1/manifest.json)

Registered failing assertion(s): DesktopNavigationTests/testDuplicateIDsRejectedAtomically.

```swift
func testDuplicateIDsRejectedAtomically() { let r = results(); r.select("b"); XCTAssertFalse(r.apply([a,a])); XCTAssertEqual(r.items, [a,b]); XCTAssertEqual(r.selectedID, "b") }
```

## Q039 · implementation repair

A button is still retained in memory after removal from the window. Closing the panel should avoid requesting focus on it. Can you exercise that exact case?

[Working implementation](../../code-examples/pilots/uikit-modal-v1/Sources/ModalUIKit.swift) · [Defective implementation](../../code-examples/pilots/uikit-modal-v1/NegativeFixtures/DetachedTarget.swift) · [Full test suite](../../code-examples/pilots/uikit-modal-v1/Tests/ModalUIKitTests.swift) · [Source contract](../../code-examples/pilots/uikit-modal-v1/manifest.json)

Registered failing assertion(s): ModalUIKitTests/testRetainedButRemovedTargetPostsNil.

```swift
func testRetainedButRemovedTargetPostsNil() {
        let panel = RestoringPanel(), background = UIView(), target = UIButton()
        var completion: (@MainActor () -> Void)?, posts = 0
        background.addSubview(target)
        panel.performDismissal = { completion = $0 }
        panel.post = { _, argument in posts += 1; XCTAssertNil(argument) }
        XCTAssertTrue(open(panel, background: background, target: target))
        XCTAssertTrue(panel.dismiss())
        target.removeFromSuperview()
        XCTAssertTrue(panel.returnTarget === target)
        withExtendedLifetime(target) { completion?() }
        XCTAssertEqual(posts, 1)
    }
```

## Q040 · implementation repair

We reconfigure a visible row without dequeuing it again. It continues to advertise the previous order’s names. Can you repair live reconfiguration?

[Working implementation](../../code-examples/pilots/uikit-naming-v1/Sources/NamingUIKit.swift) · [Defective implementation](../../code-examples/pilots/uikit-naming-v1/NegativeFixtures/StaleNames.swift) · [Full test suite](../../code-examples/pilots/uikit-naming-v1/Tests/NamingUIKitTests.swift) · [Source contract](../../code-examples/pilots/uikit-naming-v1/manifest.json)

Registered failing assertion(s): NamingUIKitTests/testReconfigurationReplacesNamesWithoutReuseCallback.

```swift
func testReconfigurationReplacesNamesWithoutReuseCallback() {
        let card = ItemActionCard()
        configure(card)
        configure(card, item: "Invoice B")
        XCTAssertEqual(card.titleLabel.text, "Invoice B")
        XCTAssertEqual(card.openButton.accessibilityLabel, "Open Invoice B")
        XCTAssertEqual(card.saveButton.accessibilityLabel, "Save Invoice B")
        configure(card)
        XCTAssertEqual(card.openButton.accessibilityLabel, "Open Invoice A")
    }
```

## Q041 · test repair

The motion test checks the initial value but never changes the preference. Can you drive the notification and verify the new value while ignoring an unrelated notification?

[Working implementation](../../code-examples/pilots/uikit-lifecycle-v1/Sources/LifecycleUIKit.swift) · [Defective implementation](../../code-examples/pilots/uikit-lifecycle-v1/NegativeFixtures/WrongNotification.swift) · [Full test suite](../../code-examples/pilots/uikit-lifecycle-v1/Tests/LifecycleUIKitTests.swift) · [Source contract](../../code-examples/pilots/uikit-lifecycle-v1/manifest.json)

Registered failing assertion(s): LifecycleUIKitTests/testInitialMotionReadAndNotificationRefresh.

```swift
func testInitialMotionReadAndNotificationRefresh() {
        let center = NotificationCenter()
        var preference = false, reads = 0
        let model = MotionPreference(center: center) { reads += 1; return preference }
        XCTAssertFalse(model.reduceMotion)
        XCTAssertEqual(reads, 1)
        preference = true
        center.post(name: UIAccessibility.reduceMotionStatusDidChangeNotification, object: nil)
        XCTAssertTrue(model.reduceMotion)
        XCTAssertEqual(reads, 2)
        preference = false
        center.post(name: UIAccessibility.reduceMotionStatusDidChangeNotification, object: nil)
        XCTAssertFalse(model.reduceMotion)
        XCTAssertEqual(reads, 3)
    }
```

## Q042 · implementation repair

Our contrast checker gives suspicious ratios for gray on white even though black on white looks right. Fix the calculation and give me a numerical case that distinguishes the two.

[Working implementation](../../code-examples/pilots/uikit-contrast-v1/Sources/ContrastUIKit.swift) · [Defective implementation](../../code-examples/pilots/uikit-contrast-v1/NegativeFixtures/NoLinearization.swift) · [Full test suite](../../code-examples/pilots/uikit-contrast-v1/Tests/ContrastUIKitTests.swift) · [Source contract](../../code-examples/pilots/uikit-contrast-v1/manifest.json)

Registered failing assertion(s): ContrastUIKitTests/testUIKitGrayConversionUsesLinearLuminance.

```swift
func testUIKitGrayConversionUsesLinearLuminance() throws {
        let color = UIColor(white: 0.5, alpha: 1)
        let resolved = try ConfiguredContrast.resolve(color, traits: traits(.light))
        XCTAssertEqual(resolved.luminance, 0.21404114048223255, accuracy: 0.00001)
        XCTAssertEqual(try ConfiguredContrast.ratio(foreground: color, background: .white, traits: traits(.light)),
                       3.976653024912438, accuracy: 0.0001)
    }
```

## Q043 · implementation repair

A document row has been rebound but its saved action can operate on the replacement document. Can the new action work while the retained one expires?

[Working implementation](../../code-examples/swiftui/macos-v1/Sources/Documents.swift) · [Defective implementation](../../code-examples/swiftui/macos-v1/NegativeFixtures/documents.swift) · [Full test suite](../../code-examples/swiftui/macos-v1/Tests/SwiftUIContractsTests.swift) · [Source contract](../../code-examples/swiftui/macos-v1/manifest.json)

Registered failing assertion(s): DocumentTests/testOldActionDoesNotTargetReboundRow.

```swift
func testOldActionDoesNotTargetReboundRow() { let s = DocumentState(); s.replace([a]); let old = s.action(for: "a"); s.replace([Article(id: "a", title: "New", important: true)]); old(); XCTAssertNil(s.selected) }
```

## Q044 · implementation repair

The title in our choice row stays small inside a view with a larger content-size override. Can you make it follow the effective environment and keep the existing text style?

[Working implementation](../../code-examples/pilots/uikit-choice-v1/Sources/ChoiceUIKit.swift) · [Defective implementation](../../code-examples/pilots/uikit-choice-v1/NegativeFixtures/FixedFont.swift) · [Full test suite](../../code-examples/pilots/uikit-choice-v1/Tests/ChoiceUIKitTests.swift) · [Source contract](../../code-examples/pilots/uikit-choice-v1/manifest.json)

Registered failing assertion(s): ChoiceUIKitTests/testFontsMatchEffectiveLargeTextEnvironment.

```swift
func testFontsMatchEffectiveLargeTextEnvironment() {
        let row = cell()
        setSize(row, .accessibilityExtraExtraExtraLarge)
        configure(row)
        for label in [row.nameLabel, row.stateLabel] {
            let expected = UIFont.preferredFont(forTextStyle: .body, compatibleWith: label.traitCollection)
            XCTAssertEqual(label.font.pointSize, expected.pointSize, accuracy: 0.01)
            XCTAssertEqual(label.font.fontDescriptor.object(forKey: .textStyle) as? String, UIFont.TextStyle.body.rawValue)
        }
    }
```

## Q045 · implementation repair

Another controller can change the text view directly. A cached match then points into unrelated text. How should the search respond before its owner rebuilds the index?

[Working implementation](../../code-examples/pilots/uikit-edited-rotor-v1/Sources/EditedRotorUIKit.swift) · [Defective implementation](../../code-examples/pilots/uikit-edited-rotor-v1/NegativeFixtures/StaleText.swift) · [Full test suite](../../code-examples/pilots/uikit-edited-rotor-v1/Tests/EditedRotorUIKitTests.swift) · [Source contract](../../code-examples/pilots/uikit-edited-rotor-v1/manifest.json)

Registered failing assertion(s): EditedRotorUIKitTests/testUnannouncedTextChangeRejectsCachedSearch.

```swift
func testUnannouncedTextChangeRejectsCachedSearch() {
        let reader = EditedMatchReader()
        reader.replace(text: "cat", query: "cat")
        reader.textView.text = "dog"
        XCTAssertNil(search(reader))
        XCTAssertEqual(reader.textView.text, "dog")
        reader.replace(text: "dog", query: "dog")
        XCTAssertEqual(location(search(reader), in: reader), 0)
    }
```

## Q046 · implementation repair

After a represented AppKit control is replaced, the old native control can still send an action. Can you test both the old sender and the replacement?

[Working implementation](../../code-examples/swiftui/mac-target-control-v1/Sources/Interop.swift) · [Defective implementation](../../code-examples/swiftui/mac-target-control-v1/NegativeFixtures/old_target.swift) · [Full test suite](../../code-examples/swiftui/mac-target-control-v1/Tests/InteropTests.swift) · [Source contract](../../code-examples/swiftui/mac-target-control-v1/manifest.json)

Registered failing assertion(s): InteropTests/testOldNativeViewCannotDispatchAfterRebind.

```swift
func testOldNativeViewCannotDispatchAfterRebind() { let c = BridgeOwner(), old = button(), current = button(); var n = 0; c.configure(old, title: "Old", enabled: true, handler: {}); c.configure(current, title: "Current", enabled: true, handler: { n += 1 });
        #if os(macOS)
        old.performClick(nil)
        #else
        old.sendActions(for: .primaryActionTriggered)
        #endif
        XCTAssertEqual(n, 0)
    }
```

## Q047 · implementation repair

The accessibility shortcut still saves, but our visible Mac Save control no longer does. Can you restore its ordinary route and verify each route dispatches once?

[Working implementation](../../code-examples/platforms/macos-appkit-v1/Sources/DesktopActions.swift) · [Defective implementation](../../code-examples/platforms/macos-appkit-v1/NegativeFixtures/LostOrdinarySave.swift) · [Full test suite](../../code-examples/platforms/macos-appkit-v1/Tests/DesktopActionsTests.swift) · [Source contract](../../code-examples/platforms/macos-appkit-v1/manifest.json)

Registered failing assertion(s): DesktopActionsTests/testOrdinarySaveOnly.

```swift
func testOrdinarySaveOnly() { var o = 0, s = 0; let r = row(open: {o += 1}, save: {s += 1}); press(r.save); XCTAssertEqual(o, 0); XCTAssertEqual(s, 1) }
```

## Q048 · implementation repair

Escape removes the overlay visually, but the accessibility configuration still describes a modal. Can you make both dismissal paths leave a consistent state?

[Working implementation](../../code-examples/pilots/uikit-containers-v1/Sources/ContainerUIKit.swift) · [Defective implementation](../../code-examples/pilots/uikit-containers-v1/NegativeFixtures/StaleModal.swift) · [Full test suite](../../code-examples/pilots/uikit-containers-v1/Tests/ContainerUIKitTests.swift) · [Source contract](../../code-examples/pilots/uikit-containers-v1/manifest.json)

Registered failing assertion(s): ContainerUIKitTests/testEscapeDismissesAndClearsModalState.

```swift
func testEscapeDismissesAndClearsModalState() {
        let panel = DismissiblePanel()
        var calls = 0
        panel.onDismiss = { calls += 1 }
        panel.open()
        XCTAssertTrue(panel.accessibilityViewIsModal)
        XCTAssertFalse(panel.accessibilityElementsHidden)
        XCTAssertTrue(panel.accessibilityPerformEscape())
        XCTAssertFalse(panel.isOpen)
        XCTAssertTrue(panel.isHidden)
        XCTAssertTrue(panel.accessibilityElementsHidden)
        XCTAssertFalse(panel.accessibilityViewIsModal)
        XCTAssertEqual(calls, 1)
        XCTAssertFalse(panel.accessibilityPerformEscape())
        XCTAssertEqual(calls, 1)
    }
```

## Q049 · implementation repair

A retained shelf button that was removed from the hierarchy still chooses an item. Can you make the same generation work for attached buttons only?

[Working implementation](../../code-examples/platforms/tvos-structure-v1/Sources/TelevisionShelves.swift) · [Defective implementation](../../code-examples/platforms/tvos-structure-v1/NegativeFixtures/DetachedAction.swift) · [Full test suite](../../code-examples/platforms/tvos-structure-v1/Tests/TelevisionShelvesTests.swift) · [Source contract](../../code-examples/platforms/tvos-structure-v1/manifest.json)

Registered failing assertion(s): TelevisionShelvesTests/testDetachedCurrentButtonCannotChoose.

```swift
func testDetachedCurrentButtonCannotChoose() {
        let v = configured(), b = v.shelves[0].buttons[0]
        var calls = 0; v.onChoose = { _ in calls += 1 }
        b.removeFromSuperview(); b.sendActions(for: .primaryActionTriggered)
        XCTAssertEqual(calls, 0); XCTAssertNil(v.selected)
    }
```

## Q050 · implementation repair

Our row has two independently operated controls. The row’s accessibility configuration now hides the controls. Can you restore access to both controls?

[Working implementation](../../code-examples/pilots/uikit-naming-v1/Sources/NamingUIKit.swift) · [Defective implementation](../../code-examples/pilots/uikit-naming-v1/NegativeFixtures/HiddenControls.swift) · [Full test suite](../../code-examples/pilots/uikit-naming-v1/Tests/NamingUIKitTests.swift) · [Source contract](../../code-examples/pilots/uikit-naming-v1/manifest.json)

Registered failing assertion(s): NamingUIKitTests/testContainerPreservesIndependentControls.

```swift
func testContainerPreservesIndependentControls() {
        let card = ItemActionCard()
        configure(card)
        XCTAssertFalse(card.isAccessibilityElement)
        XCTAssertFalse(card.accessibilityElementsHidden)
        XCTAssertTrue(card.openButton.isAccessibilityElement)
        XCTAssertTrue(card.saveButton.isAccessibilityElement)
        XCTAssertTrue(card.openButton.superview === card)
        XCTAssertTrue(card.saveButton.superview === card)
    }
```

## Q051 · implementation repair

The panel can open over content that was already hidden from accessibility. Closing it should restore either original setting. Can you handle both starting states?

[Working implementation](../../code-examples/pilots/uikit-modal-v1/Sources/ModalUIKit.swift) · [Defective implementation](../../code-examples/pilots/uikit-modal-v1/NegativeFixtures/LostBackground.swift) · [Full test suite](../../code-examples/pilots/uikit-modal-v1/Tests/ModalUIKitTests.swift) · [Source contract](../../code-examples/pilots/uikit-modal-v1/manifest.json)

Registered failing assertion(s): ModalUIKitTests/testBackgroundRestoresBothOriginalValues.

```swift
func testBackgroundRestoresBothOriginalValues() {
        for hidden in [false, true] {
            let panel = RestoringPanel(), background = UIView()
            panel.post = { _, _ in }
            background.accessibilityElementsHidden = hidden
            XCTAssertTrue(open(panel, background: background))
            XCTAssertTrue(panel.dismiss())
            XCTAssertEqual(background.accessibilityElementsHidden, hidden)
            XCTAssertEqual(panel.state, .closed)
            XCTAssertTrue(panel.isHidden)
            XCTAssertTrue(panel.accessibilityElementsHidden)
            XCTAssertFalse(panel.accessibilityViewIsModal)
        }
    }
```

## Q052 · implementation repair

Open the panel again before the first dismissal finishes and the old completion closes the new panel. Can you repair the callback and show what happens between completions?

[Working implementation](../../code-examples/pilots/uikit-modal-v1/Sources/ModalUIKit.swift) · [Defective implementation](../../code-examples/pilots/uikit-modal-v1/NegativeFixtures/StaleCompletion.swift) · [Full test suite](../../code-examples/pilots/uikit-modal-v1/Tests/ModalUIKitTests.swift) · [Source contract](../../code-examples/pilots/uikit-modal-v1/manifest.json)

Registered failing assertion(s): ModalUIKitTests/testOldCompletionCannotCloseReopenedPanel.

```swift
func testOldCompletionCannotCloseReopenedPanel() {
        let panel = RestoringPanel(), background = UIView()
        var completions: [@MainActor () -> Void] = [], posts = 0
        panel.performDismissal = { completions.append($0) }
        panel.post = { _, _ in posts += 1 }
        XCTAssertTrue(open(panel, background: background))
        XCTAssertTrue(panel.dismiss())
        panel.tearDown()
        XCTAssertFalse(background.accessibilityElementsHidden)
        XCTAssertTrue(open(panel, background: background))
        XCTAssertTrue(panel.dismiss())
        XCTAssertEqual(completions.count, 2)
        completions[0]()
        XCTAssertEqual(panel.state, .closing)
        XCTAssertTrue(background.accessibilityElementsHidden)
        XCTAssertEqual(posts, 0)
        completions[1]()
        XCTAssertEqual(posts, 1)
        XCTAssertEqual(panel.state, .closed)
    }
```

## Q053 · implementation repair

Our video inspector enables scrubbing over buffered content even when the player reports no seekable range. Can the inspector distinguish those states?

[Working implementation](../../code-examples/pilots/uikit-media-inspection-v1/Sources/MediaInspection.swift) · [Defective implementation](../../code-examples/pilots/uikit-media-inspection-v1/NegativeFixtures/LoadedAsSeekable.swift) · [Full test suite](../../code-examples/pilots/uikit-media-inspection-v1/Tests/MediaInspectionTests.swift) · [Source contract](../../code-examples/pilots/uikit-media-inspection-v1/manifest.json)

Registered failing assertion(s): MediaInspectionTests/testLoadedRangesDoNotAuthorizeSeeking.

```swift
func testLoadedRangesDoNotAuthorizeSeeking() {
        let value = snapshot(duration: time(100), seekable: [range(20, 10)], loaded: [range(0, 100)])
        XCTAssertEqual(value.containsSeekableTime(time(5)), false)
        XCTAssertEqual(value.containsSeekableTime(time(25)), true)
        XCTAssertEqual(value.loaded?.count, 1)
        XCTAssertEqual(value.loaded?.first?.duration, time(100))
    }
```

## Q054 · test repair

The title is discoverable, yet our test would stay green if a purely decorative icon were also exposed. Strengthen the test for both elements after configuration.

[Working implementation](../../code-examples/pilots/uikit-naming-v1/Sources/NamingUIKit.swift) · [Defective implementation](../../code-examples/pilots/uikit-naming-v1/NegativeFixtures/ExposedDecoration.swift) · [Full test suite](../../code-examples/pilots/uikit-naming-v1/Tests/NamingUIKitTests.swift) · [Source contract](../../code-examples/pilots/uikit-naming-v1/manifest.json)

Registered failing assertion(s): NamingUIKitTests/testDecorationIsExplicitlyExcluded.

```swift
func testDecorationIsExplicitlyExcluded() {
        let card = ItemActionCard()
        card.decoration.isAccessibilityElement = true
        configure(card)
        XCTAssertFalse(card.decoration.isAccessibilityElement)
        XCTAssertTrue(card.titleLabel.isAccessibilityElement)
    }
```

## Q055 · implementation repair

Our panel can close while dismissal is disabled. Can you make both entry points respect the current policy?

[Working implementation](../../code-examples/pilots/uikit-modal-v1/Sources/ModalUIKit.swift) · [Defective implementation](../../code-examples/pilots/uikit-modal-v1/NegativeFixtures/IgnoredDismissGuard.swift) · [Full test suite](../../code-examples/pilots/uikit-modal-v1/Tests/ModalUIKitTests.swift) · [Source contract](../../code-examples/pilots/uikit-modal-v1/manifest.json)

Registered failing assertion(s): ModalUIKitTests/testOrdinaryCloseAndEscapeShareDismissalGuard.

```swift
func testOrdinaryCloseAndEscapeShareDismissalGuard() {
        let panel = RestoringPanel(), background = UIView()
        var starts = 0, completion: (@MainActor () -> Void)?
        panel.performDismissal = { starts += 1; completion = $0 }
        panel.post = { _, _ in }
        XCTAssertTrue(open(panel, background: background))
        panel.canDismiss = false
        panel.close.sendActions(for: .touchUpInside)
        XCTAssertFalse(panel.accessibilityPerformEscape())
        XCTAssertEqual(starts, 0)
        panel.canDismiss = true
        panel.close.sendActions(for: .touchUpInside)
        XCTAssertEqual(starts, 1)
        XCTAssertFalse(panel.accessibilityPerformEscape())
        XCTAssertEqual(starts, 1)
        completion?()
        XCTAssertFalse(panel.dismiss())
    }
```

## Q056 · implementation repair

A retained accessibility action for yesterday’s result can still change the reused result view. Can you fix that while keeping the new result actionable?

[Working implementation](../../code-examples/pilots/uikit-dynamic-v1/Sources/DynamicUIKit.swift) · [Defective implementation](../../code-examples/pilots/uikit-dynamic-v1/NegativeFixtures/StaleAction.swift) · [Full test suite](../../code-examples/pilots/uikit-dynamic-v1/Tests/DynamicUIKitTests.swift) · [Source contract](../../code-examples/pilots/uikit-dynamic-v1/manifest.json)

Registered failing assertion(s): DynamicUIKitTests/testRetainedOldActionCannotAffectReusedView.

```swift
@MainActor func testRetainedOldActionCannotAffectReusedView() throws {
        var events: [String] = []
        let view = ReusableMessageActions { events.append($0 + ":" + $1.rawValue) }
        view.configure(id: "a", title: "Alpha", enabled: true)
        let old = try XCTUnwrap(view.summary.accessibilityCustomActions?.first)
        view.configure(id: "b", title: "Beta", enabled: true)
        XCTAssertEqual(old.actionHandler?(old), false)
        XCTAssertTrue(events.isEmpty)
    }
```

## Q057 · test repair

This test keeps passing when tapping the selected speed calls the playback engine again. Exercise the button and count actual change deliveries across two taps.

[Working implementation](../../code-examples/pilots/uikit-speed-v1/Sources/PlaybackSpeed.swift) · [Defective implementation](../../code-examples/pilots/uikit-speed-v1/NegativeFixtures/RepeatedChange.swift) · [Full test suite](../../code-examples/pilots/uikit-speed-v1/Tests/PlaybackSpeedTests.swift) · [Source contract](../../code-examples/pilots/uikit-speed-v1/manifest.json)

Registered failing assertion(s): PlaybackSpeedTests/testRepeatedSelectionDoesNotEmitDuplicateChange.

```swift
func testRepeatedSelectionDoesNotEmitDuplicateChange() {
        let view = PlaybackSpeedChoices()
        var calls: [Float] = []
        view.onChange = { calls.append($0) }
        XCTAssertTrue(view.select(1))
        view.buttons[2].sendActions(for: .primaryActionTriggered)
        view.buttons[2].sendActions(for: .primaryActionTriggered)
        XCTAssertEqual(calls, [1.5])
    }
```

## Q058 · implementation repair

A loader calls its completion twice. After the first result is displayed, the second delivery can overwrite it. Can you enforce the intended one-result policy?

[Working implementation](../../code-examples/platforms/ios-closure-v1/Sources/AsyncOwnership.swift) · [Defective implementation](../../code-examples/platforms/ios-closure-v1/NegativeFixtures/media_duplicate.swift) · [Full test suite](../../code-examples/platforms/ios-closure-v1/Tests/AsyncOwnershipTests.swift) · [Source contract](../../code-examples/platforms/ios-closure-v1/manifest.json)

Registered failing assertion(s): MediaLoadOwnerTests/testDuplicateCallbackCannotOverwriteFirstResult.

```swift
func testDuplicateCallbackCannotOverwriteFirstResult() {
        let o = MediaLoadOwner(); o.replace(item()) { _, done in done(.success("first")); done(.success("second")) }
        XCTAssertEqual(o.value, "first")
    }
```

## Q059 · test repair

Our choice-row test checks the selected state on a fresh cell. Would it catch a refresh that wipes traits supplied by another feature? Strengthen the test to cover a selection change.

[Working implementation](../../code-examples/pilots/uikit-choice-v1/Sources/ChoiceUIKit.swift) · [Defective implementation](../../code-examples/pilots/uikit-choice-v1/NegativeFixtures/ClobberedTraits.swift) · [Full test suite](../../code-examples/pilots/uikit-choice-v1/Tests/ChoiceUIKitTests.swift) · [Source contract](../../code-examples/pilots/uikit-choice-v1/manifest.json)

Registered failing assertion(s): ChoiceUIKitTests/testSelectionUpdatesPreserveUnrelatedTraits.

```swift
func testSelectionUpdatesPreserveUnrelatedTraits() {
        let row = cell()
        row.accessibilityTraits.insert(.updatesFrequently)
        for chosen in [true, false, true] {
            configure(row, chosen: chosen)
            XCTAssertTrue(row.accessibilityTraits.contains(.updatesFrequently))
            XCTAssertEqual(row.accessibilityTraits.contains(.selected), chosen)
        }
    }
```

## Q060 · implementation repair

Choose delivery, then switch back to pickup. The old option still reports itself selected. Can you make every selection cue agree after switching twice?

[Working implementation](../../code-examples/pilots/uikit-choice-v1/Sources/ChoiceUIKit.swift) · [Defective implementation](../../code-examples/pilots/uikit-choice-v1/NegativeFixtures/StaleSelection.swift) · [Full test suite](../../code-examples/pilots/uikit-choice-v1/Tests/ChoiceUIKitTests.swift) · [Source contract](../../code-examples/pilots/uikit-choice-v1/manifest.json)

Registered failing assertion(s): ChoiceUIKitTests/testDeselectionClearsEveryOwnedSelectionCue.

```swift
func testDeselectionClearsEveryOwnedSelectionCue() {
        let row = cell()
        configure(row, chosen: true)
        configure(row, chosen: false)
        XCTAssertEqual(row.stateLabel.text, "Not selected")
        XCTAssertEqual(row.accessibilityValue, "Not selected")
        XCTAssertEqual(row.accessoryType, .none)
        XCTAssertFalse(row.accessibilityTraits.contains(.selected))
    }
```

## Q061 · implementation repair

The inspector promises smooth playback whenever the buffer is full. How should it represent a full buffer when the player still says it may stall?

[Working implementation](../../code-examples/pilots/uikit-media-inspection-v1/Sources/MediaInspection.swift) · [Defective implementation](../../code-examples/pilots/uikit-media-inspection-v1/NegativeFixtures/FullMeansReady.swift) · [Full test suite](../../code-examples/pilots/uikit-media-inspection-v1/Tests/MediaInspectionTests.swift) · [Source contract](../../code-examples/pilots/uikit-media-inspection-v1/manifest.json)

Registered failing assertion(s): MediaInspectionTests/testFullBufferDoesNotImplyLikelyToKeepUp.

```swift
func testFullBufferDoesNotImplyLikelyToKeepUp() {
        let value = snapshot(full: true, likely: false)
        XCTAssertEqual(value.bufferFull, true)
        XCTAssertEqual(value.likelyToKeepUp, false)
        XCTAssertNil(value.bufferEmpty)
    }
```

## Q062 · implementation repair

The motion preference is correct at launch but changing it while the screen is visible doesn't update the view. Can you fix observation and show the change is delivered?

[Working implementation](../../code-examples/pilots/uikit-lifecycle-v1/Sources/LifecycleUIKit.swift) · [Defective implementation](../../code-examples/pilots/uikit-lifecycle-v1/NegativeFixtures/WrongNotification.swift) · [Full test suite](../../code-examples/pilots/uikit-lifecycle-v1/Tests/LifecycleUIKitTests.swift) · [Source contract](../../code-examples/pilots/uikit-lifecycle-v1/manifest.json)

Registered failing assertion(s): LifecycleUIKitTests/testInitialMotionReadAndNotificationRefresh.

```swift
func testInitialMotionReadAndNotificationRefresh() {
        let center = NotificationCenter()
        var preference = false, reads = 0
        let model = MotionPreference(center: center) { reads += 1; return preference }
        XCTAssertFalse(model.reduceMotion)
        XCTAssertEqual(reads, 1)
        preference = true
        center.post(name: UIAccessibility.reduceMotionStatusDidChangeNotification, object: nil)
        XCTAssertTrue(model.reduceMotion)
        XCTAssertEqual(reads, 2)
        preference = false
        center.post(name: UIAccessibility.reduceMotionStatusDidChangeNotification, object: nil)
        XCTAssertFalse(model.reduceMotion)
        XCTAssertEqual(reads, 3)
    }
```

## Q063 · implementation repair

Our text search is supposed to include overlapping matches. Looking for “ana” in “banana” misses a result. Can the rotor visit both positions in order?

[Working implementation](../../code-examples/pilots/uikit-edited-rotor-v1/Sources/EditedRotorUIKit.swift) · [Defective implementation](../../code-examples/pilots/uikit-edited-rotor-v1/NegativeFixtures/IgnoredOverlap.swift) · [Full test suite](../../code-examples/pilots/uikit-edited-rotor-v1/Tests/EditedRotorUIKitTests.swift) · [Source contract](../../code-examples/pilots/uikit-edited-rotor-v1/manifest.json)

Registered failing assertion(s): EditedRotorUIKitTests/testOverlapPolicyIsExplicit.

```swift
func testOverlapPolicyIsExplicit() {
        XCTAssertEqual(LiteralMatches.ranges(in: "banana", query: "ana", allowOverlaps: false),
                       [NSRange(location: 1, length: 3)])
        XCTAssertEqual(LiteralMatches.ranges(in: "banana", query: "ana", allowOverlaps: true),
                       [NSRange(location: 1, length: 3), NSRange(location: 3, length: 3)])
    }
```

## Q064 · implementation repair

The Details shortcut works but the ordinary Details action on our television screen is broken. Can you repair it and exercise the two entry points independently?

[Working implementation](../../code-examples/platforms/tvos-uikit-v1/Sources/TelevisionActions.swift) · [Defective implementation](../../code-examples/platforms/tvos-uikit-v1/NegativeFixtures/LostOrdinaryDetails.swift) · [Full test suite](../../code-examples/platforms/tvos-uikit-v1/Tests/TelevisionActionsTests.swift) · [Source contract](../../code-examples/platforms/tvos-uikit-v1/manifest.json)

Registered failing assertion(s): TelevisionActionsTests/testOrdinaryDetails.

```swift
func testOrdinaryDetails() { var d = 0; let r = row(details: {d += 1}); r.details.sendActions(for: .primaryActionTriggered); XCTAssertEqual(d, 1) }
```

## Q065 · implementation repair

An Off action retained by an old caption menu can clear selection after a menu reload. Can you repair and exercise the binding that the menu actually uses?

[Working implementation](../../code-examples/swiftui/media-macos-v2/Sources/MediaSelection.swift) · [Defective implementation](../../code-examples/swiftui/media-macos-v2/NegativeFixtures/staleoff.swift) · [Full test suite](../../code-examples/swiftui/media-macos-v2/Tests/ReviewRegressionTests.swift) · [Source contract](../../code-examples/swiftui/media-macos-v2/manifest.json)

Registered failing assertion(s): ReviewRegressionTests/testStaleOffCannotClearReloadedSelection.

```swift
func testStaleOffCannotClearReloadedSelection() async throws {
        try await fixture { store, item, group in
            let old = store.selection
            store.complete(store.beginLoad(), result: .success(group))
            let choice = try XCTUnwrap(store.choices.first)
            XCTAssertTrue(store.choose(choice.id))
            old.wrappedValue = nil
            XCTAssertEqual(item.currentMediaSelection.selectedMediaOption(in: group), choice.option)
        }
    }
```

## Q066 · test repair

Our test checks that the row is recognizable, but Save has disappeared from the ordinary action path before. Add proof that operates the visible control and observes its callback.

[Working implementation](../../code-examples/platforms/macos-appkit-v1/Sources/DesktopActions.swift) · [Defective implementation](../../code-examples/platforms/macos-appkit-v1/NegativeFixtures/LostOrdinarySave.swift) · [Full test suite](../../code-examples/platforms/macos-appkit-v1/Tests/DesktopActionsTests.swift) · [Source contract](../../code-examples/platforms/macos-appkit-v1/manifest.json)

Registered failing assertion(s): DesktopActionsTests/testOrdinarySaveOnly.

```swift
func testOrdinarySaveOnly() { var o = 0, s = 0; let r = row(open: {o += 1}, save: {s += 1}); press(r.save); XCTAssertEqual(o, 0); XCTAssertEqual(s, 1) }
```

## Q067 · test repair

CI only checks the table's size. It missed an invoice selection moving after a sort. Can you show how to catch that using equal titles and different identifiers?

[Working implementation](../../code-examples/platforms/macos-navigation-v1/Sources/DesktopNavigation.swift) · [Defective implementation](../../code-examples/platforms/macos-navigation-v1/NegativeFixtures/LostSelection.swift) · [Full test suite](../../code-examples/platforms/macos-navigation-v1/Tests/DesktopNavigationTests.swift) · [Source contract](../../code-examples/platforms/macos-navigation-v1/manifest.json)

Registered failing assertion(s): DesktopNavigationTests/testReorderPreservesIdentity.

```swift
func testReorderPreservesIdentity() { let r = results(); r.select("b"); r.apply([b,a]); XCTAssertEqual(r.table.selectedRow, 0); XCTAssertEqual(r.selectedID, "b") }
```

## Q068 · implementation repair

While saving is disabled, invoking the accessibility shortcut still changes the app. Can you repair the disabled path and preserve the enabled action?

[Working implementation](../../code-examples/platforms/macos-appkit-v1/Sources/DesktopActions.swift) · [Defective implementation](../../code-examples/platforms/macos-appkit-v1/NegativeFixtures/DisabledShortcut.swift) · [Full test suite](../../code-examples/platforms/macos-appkit-v1/Tests/DesktopActionsTests.swift) · [Source contract](../../code-examples/platforms/macos-appkit-v1/manifest.json)

Registered failing assertion(s): DesktopActionsTests/testDisabledShortcut.

```swift
func testDisabledShortcut() { let r = row(); r.save.isEnabled = false; XCTAssertEqual(r.open.accessibilityCustomActions()?.first?.handler?(), false) }
```

## Q069 · implementation repair

A decorative icon in our order row is appearing as a separate accessibility element. Can you exclude the icon while preserving the actionable content?

[Working implementation](../../code-examples/pilots/uikit-naming-v1/Sources/NamingUIKit.swift) · [Defective implementation](../../code-examples/pilots/uikit-naming-v1/NegativeFixtures/ExposedDecoration.swift) · [Full test suite](../../code-examples/pilots/uikit-naming-v1/Tests/NamingUIKitTests.swift) · [Source contract](../../code-examples/pilots/uikit-naming-v1/manifest.json)

Registered failing assertion(s): NamingUIKitTests/testDecorationIsExplicitlyExcluded.

```swift
func testDecorationIsExplicitlyExcluded() {
        let card = ItemActionCard()
        card.decoration.isAccessibilityElement = true
        configure(card)
        XCTAssertFalse(card.decoration.isAccessibilityElement)
        XCTAssertTrue(card.titleLabel.isAccessibilityElement)
    }
```

## Q070 · implementation repair

The selected state is visible by color alone after this row refreshes. Can you keep a non-color label and its accessibility value synchronized on deselection too?

[Working implementation](../../code-examples/platforms/macos-closure-v1/Sources/StateContracts.swift) · [Defective implementation](../../code-examples/platforms/macos-closure-v1/NegativeFixtures/state_text.swift) · [Full test suite](../../code-examples/platforms/macos-closure-v1/Tests/StateContractTests.swift) · [Source contract](../../code-examples/platforms/macos-closure-v1/manifest.json)

Registered failing assertion(s): StateContractTests/testSelectedStateHasNonColorTextAndValue.

```swift
func testSelectedStateHasNonColorTextAndValue() {
        let r = RegionState(); r.configure(name: "Report", selected: true, reduceTransparency: false)
        XCTAssertEqual(r.status.stringValue, "Selected")
        XCTAssertEqual(r.button.accessibilityValue() as? String, "Selected")
    }
```

## Q071 · implementation repair

The user edits a native field while validation is pending, without submitting again. The result still attaches to the edited value. Can you fix that case?

[Working implementation](../../code-examples/platforms/ios-closure-v1/Sources/AsyncOwnership.swift) · [Defective implementation](../../code-examples/platforms/ios-closure-v1/NegativeFixtures/validation_snapshot.swift) · [Full test suite](../../code-examples/platforms/ios-closure-v1/Tests/AsyncOwnershipTests.swift) · [Source contract](../../code-examples/platforms/ios-closure-v1/manifest.json)

Registered failing assertion(s): AsyncOwnershipTests/testNativeFieldMutationCannotApplyOldSnapshot.

```swift
func testNativeFieldMutationCannotApplyOldSnapshot() {
        var accepted = 0; let o = owner(accept: { _ in accepted += 1 }); o.submit()
        o.fields["name"]?.text = "Changed outside adapter"; replies[0]([:])
        XCTAssertEqual(accepted, 0); XCTAssertFalse(o.busy)
    }
```

## Q072 · test repair

Opening our modal passes the test, but it never exercises refusal by the original responder. How would you check the fallback used on completion?

[Working implementation](../../code-examples/platforms/macos-lifecycle-v1/Sources/DesktopLifecycle.swift) · [Defective implementation](../../code-examples/platforms/macos-lifecycle-v1/NegativeFixtures/OriginalNoResponderCheck.swift) · [Full test suite](../../code-examples/platforms/macos-lifecycle-v1/Tests/DesktopLifecycleTests.swift) · [Source contract](../../code-examples/platforms/macos-lifecycle-v1/manifest.json)

Registered failing assertion(s): DesktopLifecycleTests/testRefusingOriginalUsesFallback.

```swift
func testRefusingOriginalUsesFallback() { let h = ModalHarness(); (h.primary as! TestButton).acceptsFocus = false; XCTAssertTrue(h.restore.finish(h.begin())); XCTAssertTrue(h.seen.first === h.fallback) }
```

## Q073 · implementation repair

Our result exposes two named shortcuts. Invoking a single shortcut can deliver the operation twice. Can you verify the actual dispatch of both?

[Working implementation](../../code-examples/pilots/uikit-dynamic-v1/Sources/DynamicUIKit.swift) · [Defective implementation](../../code-examples/pilots/uikit-dynamic-v1/NegativeFixtures/DuplicateCallback.swift) · [Full test suite](../../code-examples/pilots/uikit-dynamic-v1/Tests/DynamicUIKitTests.swift) · [Source contract](../../code-examples/pilots/uikit-dynamic-v1/manifest.json)

Registered failing assertion(s): DynamicUIKitTests/testCustomActionsAreIndependentAndNamed.

```swift
@MainActor func testCustomActionsAreIndependentAndNamed() throws {
        var events: [String] = []
        let view = ReusableMessageActions { events.append($0 + ":" + $1.rawValue) }
        view.configure(id: "a", title: "Alpha", enabled: true)
        let actions = try XCTUnwrap(view.summary.accessibilityCustomActions)
        XCTAssertEqual(actions.map(\.name), ["Archive Alpha", "Delete Alpha"])
        XCTAssertEqual(actions[0].actionHandler?(actions[0]), true)
        XCTAssertEqual(actions[1].actionHandler?(actions[1]), true)
        XCTAssertEqual(events, ["a:archive", "a:delete"])
    }
```

## Q074 · implementation repair

Another controller replaces the player item directly during inspection. Can you ensure the old item's completion cannot publish results for the new one?

[Working implementation](../../code-examples/platforms/ios-closure-v1/Sources/AsyncOwnership.swift) · [Defective implementation](../../code-examples/platforms/ios-closure-v1/NegativeFixtures/media_identity.swift) · [Full test suite](../../code-examples/platforms/ios-closure-v1/Tests/AsyncOwnershipTests.swift) · [Source contract](../../code-examples/platforms/ios-closure-v1/manifest.json)

Registered failing assertion(s): MediaLoadOwnerTests/testExternalReplacementRejectsOldResult.

```swift
func testExternalReplacementRejectsOldResult() {
        let o = MediaLoadOwner(); var done: Reply!
        let original = item(); o.replace(original) { _, r in done = r }; o.player.replaceCurrentItem(with: item())
        withExtendedLifetime(original) { done(.success("old")) }; XCTAssertNil(o.value); XCTAssertEqual(o.state, "superseded")
    }
```

## Q075 · implementation repair

Our save handler can synchronously call back into the form. One submission then invokes Save twice. Can you protect the actual dispatch path?

[Working implementation](../../code-examples/platforms/macos-structure-v1/Sources/DesktopForm.swift) · [Defective implementation](../../code-examples/platforms/macos-structure-v1/NegativeFixtures/ReentrantSave.swift) · [Full test suite](../../code-examples/platforms/macos-structure-v1/Tests/DesktopFormTests.swift) · [Source contract](../../code-examples/platforms/macos-structure-v1/manifest.json)

Registered failing assertion(s): DesktopFormTests/testReentrantSaveDoesNotSubmitTwice.

```swift
func testReentrantSaveDoesNotSubmitTwice() {
        var calls = 0
        var f: DesktopForm!
        f = DesktopForm(validate: { _ in nil }, save: { _ in
            calls += 1
            if calls == 1 { f.submit() }
        })
        f.submit()
        XCTAssertEqual(calls, 1)
        f = nil
    }
```

## Q076 · implementation repair

A removed result stays alive after its owner drops it. Can you show whether the accessibility index or container is holding it and repair the removal path?

[Working implementation](../../code-examples/pilots/uikit-dynamic-v1/Sources/DynamicUIKit.swift) · [Defective implementation](../../code-examples/pilots/uikit-dynamic-v1/NegativeFixtures/RetainedRemoved.swift) · [Full test suite](../../code-examples/pilots/uikit-dynamic-v1/Tests/DynamicUIKitTests.swift) · [Source contract](../../code-examples/pilots/uikit-dynamic-v1/manifest.json)

Registered failing assertion(s): DynamicUIKitTests/testRemovedElementIsNotRetainedByIndexOrContainer.

```swift
@MainActor func testRemovedElementIsNotRetainedByIndexOrContainer() {
        let view = DynamicSections(frame: .zero)
        weak var removed: UILabel?
        // Observe persistent ownership after temporary Objective-C references drain.
        autoreleasepool {
            view.replace(records)
            removed = view.labels[0]
            view.replace([records[1]])
        }
        XCTAssertNil(removed)
    }
```

## Q077 · implementation repair

When an editor closes after its original responder moved into another window, it tries to restore the wrong target. Can you exercise that move and use the eligible fallback?

[Working implementation](../../code-examples/platforms/macos-lifecycle-v1/Sources/DesktopLifecycle.swift) · [Defective implementation](../../code-examples/platforms/macos-lifecycle-v1/NegativeFixtures/ForeignTarget.swift) · [Full test suite](../../code-examples/platforms/macos-lifecycle-v1/Tests/DesktopLifecycleTests.swift) · [Source contract](../../code-examples/platforms/macos-lifecycle-v1/manifest.json)

Registered failing assertion(s): DesktopLifecycleTests/testForeignOriginalUsesFallback.

```swift
func testForeignOriginalUsesFallback() { let h = ModalHarness(); let token = h.begin(); let other = NSView(); other.addSubview(h.primary); XCTAssertTrue(h.restore.finish(token)); XCTAssertTrue(h.seen.first === h.fallback) }
```

## Q078 · implementation repair

A disabled control can still toggle when its keyboard handler receives the event directly. Can you make disabled behavior agree across entry points?

[Working implementation](../../code-examples/platforms/macos-closure-details-v1/Sources/StateContracts.swift) · [Defective implementation](../../code-examples/platforms/macos-closure-details-v1/NegativeFixtures/keyboard_disabled.swift) · [Full test suite](../../code-examples/platforms/macos-closure-details-v1/Tests/DesktopContractTests.swift) · [Source contract](../../code-examples/platforms/macos-closure-details-v1/manifest.json)

Registered failing assertion(s): DesktopContractTests/testDisabledKeyboardEventCannotToggle.

```swift
func testDisabledKeyboardEventCannotToggle() {
        let t = SemanticToggle(); t.isEnabled = false; var called = false; t.changed = { _ in called = true }
        t.keyDown(with: key(" ", code: 49)); XCTAssertFalse(t.on); XCTAssertFalse(called)
    }
```

## Q079 · implementation repair

Writing the same value twice through our SwiftUI binding repeats the side effect. Can you preserve genuine value changes and suppress duplicates?

[Working implementation](../../code-examples/swiftui/macos-v1/Sources/Semantics.swift) · [Defective implementation](../../code-examples/swiftui/macos-v1/NegativeFixtures/semantics.swift) · [Full test suite](../../code-examples/swiftui/macos-v1/Tests/SwiftUIContractsTests.swift) · [Source contract](../../code-examples/swiftui/macos-v1/manifest.json)

Registered failing assertion(s): SemanticsTests/testRepeatedBindingSetDoesNotDuplicateCallback.

```swift
func testRepeatedBindingSetDoesNotDuplicateCallback() { let s = SettingsState(); var n = 0; s.changed = { _ in n += 1 }; s.toggle.wrappedValue = true; s.toggle.wrappedValue = true; XCTAssertEqual(n, 1) }
```

## Q080 · test repair

A Mac outline refresh passes our smoke test even when selection moves to a different sibling. Add a test that exercises the refresh with a real selection.

[Working implementation](../../code-examples/platforms/macos-structure-v1/Sources/DesktopOutline.swift) · [Defective implementation](../../code-examples/platforms/macos-structure-v1/NegativeFixtures/LostSelection.swift) · [Full test suite](../../code-examples/platforms/macos-structure-v1/Tests/DesktopOutlineTests.swift) · [Source contract](../../code-examples/platforms/macos-structure-v1/manifest.json)

Registered failing assertion(s): DesktopOutlineTests/testSelectedChildSurvivesSiblingReorder.

```swift
func testSelectedChildSurvivesSiblingReorder() throws {
        let d = configured(); d.outline.expandItem(try XCTUnwrap(d.nodes["g"])); d.select("b")
        XCTAssertEqual(d.selectedID, "b")
        XCTAssertTrue(d.apply([Item(id: "g", title: "Group", children: [Item(id: "b", title: "Beta"), Item(id: "a", title: "Alpha")])]))
        XCTAssertEqual(d.selectedID, "b")
    }
```

## Q081 · test repair

The row still says “Report” after selection. The test passes even when the selected flag never changes. Can you exercise select and deselect while preserving the row's other semantics?

[Working implementation](../../code-examples/platforms/macos-closure-details-v1/Sources/DesktopRow.swift) · [Defective implementation](../../code-examples/platforms/macos-closure-details-v1/NegativeFixtures/row_selected.swift) · [Full test suite](../../code-examples/platforms/macos-closure-details-v1/Tests/DesktopContractTests.swift) · [Source contract](../../code-examples/platforms/macos-closure-details-v1/manifest.json)

Registered failing assertion(s): DesktopContractTests/testExplicitRowRoleAndChildSemantics.

```swift
func testExplicitRowRoleAndChildSemantics() {
        let r = DesktopRow(); r.configure(id: "one", title: "Report", selected: true, expanded: true)
        XCTAssertEqual(r.accessibilityRole(), .row)
        XCTAssertEqual(r.accessibilityLabel(), "Report")
        XCTAssertTrue(r.isAccessibilitySelected()); XCTAssertTrue(r.isAccessibilityExpanded())
        XCTAssertTrue((r.accessibilityChildren()?.first as? NSButton) === r.open)
        XCTAssertEqual(r.open.accessibilityLabel(), "Open Report")
    }
```

## Q082 · implementation repair

Our original responder is still attached but refuses first responder. Can the return path use the fallback without sending keyboard events?

[Working implementation](../../code-examples/platforms/macos-lifecycle-v1/Sources/DesktopLifecycle.swift) · [Defective implementation](../../code-examples/platforms/macos-lifecycle-v1/NegativeFixtures/OriginalNoResponderCheck.swift) · [Full test suite](../../code-examples/platforms/macos-lifecycle-v1/Tests/DesktopLifecycleTests.swift) · [Source contract](../../code-examples/platforms/macos-lifecycle-v1/manifest.json)

Registered failing assertion(s): DesktopLifecycleTests/testRefusingOriginalUsesFallback.

```swift
func testRefusingOriginalUsesFallback() { let h = ModalHarness(); (h.primary as! TestButton).acceptsFocus = false; XCTAssertTrue(h.restore.finish(h.begin())); XCTAssertTrue(h.seen.first === h.fallback) }
```

## Q083 · test repair

Our motion test checks only that the animation did not run. How do we catch the regression where the status never changes for people who enable Reduce Motion?

[Working implementation](../../code-examples/platforms/tvos-results-v1/Sources/TelevisionResults.swift) · [Defective implementation](../../code-examples/platforms/tvos-results-v1/NegativeFixtures/MotionHidesContent.swift) · [Full test suite](../../code-examples/platforms/tvos-results-v1/Tests/TelevisionResultsTests.swift) · [Source contract](../../code-examples/platforms/tvos-results-v1/manifest.json)

Registered failing assertion(s): TelevisionResultsTests/testReducedMotionStillUpdatesContent.

```swift
func testReducedMotionStillUpdatesContent() { var animations = 0; let s = TelevisionStatus(reduceMotion: {true}, animate: {animations += 1}); s.update("Ready"); XCTAssertEqual(s.label.text, "Ready"); XCTAssertEqual(s.label.accessibilityLabel, "Ready"); XCTAssertEqual(animations, 0) }
```

## Q084 · implementation repair

Our form succeeds on its second submission, but still offers the previous error’s recovery hint. Can you reset the stale state and preserve the successful result?

[Working implementation](../../code-examples/pilots/uikit-preferences-v1/Sources/PreferenceUIKit.swift) · [Defective implementation](../../code-examples/pilots/uikit-preferences-v1/NegativeFixtures/StaleHint.swift) · [Full test suite](../../code-examples/pilots/uikit-preferences-v1/Tests/PreferenceUIKitTests.swift) · [Source contract](../../code-examples/pilots/uikit-preferences-v1/manifest.json)

Registered failing assertion(s): PreferenceUIKitTests/testRecoveryRemovesStaleErrorAndHint.

```swift
func testRecoveryRemovesStaleErrorAndHint() {
        let view = ValidationStatus()
        view.configure(error: "Email is required")
        view.configure(error: nil)
        XCTAssertEqual(view.message.text, "Ready to submit")
        XCTAssertEqual(view.message.accessibilityLabel, "Ready to submit")
        XCTAssertTrue(view.submit.isEnabled)
        XCTAssertNil(view.submit.accessibilityHint)
    }
```

## Q085 · implementation repair

Our SwiftUI preference policy requests animation even when Reduce Motion is enabled. Can you show both preference paths end in the same state while animation policy differs?

[Working implementation](../../code-examples/swiftui/macos-v1/Sources/Preferences.swift) · [Defective implementation](../../code-examples/swiftui/macos-v1/NegativeFixtures/preferences.swift) · [Full test suite](../../code-examples/swiftui/macos-v1/Tests/SwiftUIContractsTests.swift) · [Source contract](../../code-examples/swiftui/macos-v1/manifest.json)

Registered failing assertion(s): PreferenceTests/testReducedMotionPolicyKeepsFinalStateIndependent.

```swift
func testReducedMotionPolicyKeepsFinalStateIndependent() { var p = PresentationPolicy(); XCTAssertTrue(p.animate); p.reduceMotion = true; XCTAssertFalse(p.animate); XCTAssertEqual(p.selectedText, "Selected") }
```

## Q086 · implementation repair

Each shelf needs a heading and independently operable item buttons. The container now absorbs them. Can you restore the structure without changing the data order?

[Working implementation](../../code-examples/platforms/tvos-structure-v1/Sources/TelevisionShelves.swift) · [Defective implementation](../../code-examples/platforms/tvos-structure-v1/NegativeFixtures/CombinedShelf.swift) · [Full test suite](../../code-examples/platforms/tvos-structure-v1/Tests/TelevisionShelvesTests.swift) · [Source contract](../../code-examples/platforms/tvos-structure-v1/manifest.json)

Registered failing assertion(s): TelevisionShelvesTests/testShelvesPreserveIndependentHeadingAndButtons.

```swift
func testShelvesPreserveIndependentHeadingAndButtons() {
        let v = configured(), shelf = v.shelves[0]
        XCTAssertFalse(v.isAccessibilityElement); XCTAssertFalse(shelf.isAccessibilityElement)
        XCTAssertTrue(shelf.heading.isAccessibilityElement); XCTAssertTrue(shelf.heading.accessibilityTraits.contains(.header))
        XCTAssertEqual(shelf.heading.text, "Featured")
        XCTAssertEqual(shelf.buttons.map { $0.title(for: .normal) }, ["Alpha", "Beta"])
        XCTAssertEqual(shelf.buttons.map(\.accessibilityLabel), ["Alpha", "Beta"])
    }
```

## Q087 · implementation repair

A disabled speed control still changes the playback rate through a direct selection request. Can you repair the command path and verify re-enabling it?

[Working implementation](../../code-examples/pilots/uikit-speed-v1/Sources/PlaybackSpeed.swift) · [Defective implementation](../../code-examples/pilots/uikit-speed-v1/NegativeFixtures/IgnoredDisabled.swift) · [Full test suite](../../code-examples/pilots/uikit-speed-v1/Tests/PlaybackSpeedTests.swift) · [Source contract](../../code-examples/pilots/uikit-speed-v1/manifest.json)

Registered failing assertion(s): PlaybackSpeedTests/testDisabledRequestsAreRejectedAndReenableRestoresOrdinaryPath.

```swift
func testDisabledRequestsAreRejectedAndReenableRestoresOrdinaryPath() {
        let view = PlaybackSpeedChoices()
        var calls: [Float] = []
        view.onChange = { calls.append($0) }
        view.controlsEnabled = false
        XCTAssertTrue(view.buttons.allSatisfy { !$0.isEnabled })
        XCTAssertFalse(view.select(2))
        XCTAssertEqual(view.selectedRate, 1)
        XCTAssertTrue(calls.isEmpty)
        view.controlsEnabled = true
        view.buttons[3].sendActions(for: .primaryActionTriggered)
        XCTAssertEqual(calls, [2])
    }
```

## Q088 · implementation repair

The screen-change request fires before the closing animation finishes. Can it use the target that is eligible when dismissal actually completes?

[Working implementation](../../code-examples/pilots/uikit-modal-v1/Sources/ModalUIKit.swift) · [Defective implementation](../../code-examples/pilots/uikit-modal-v1/NegativeFixtures/EarlyNotification.swift) · [Full test suite](../../code-examples/pilots/uikit-modal-v1/Tests/ModalUIKitTests.swift) · [Source contract](../../code-examples/pilots/uikit-modal-v1/manifest.json)

Registered failing assertion(s): ModalUIKitTests/testNotificationWaitsForCompletionAndUsesCurrentTarget.

```swift
func testNotificationWaitsForCompletionAndUsesCurrentTarget() {
        let panel = RestoringPanel(), background = UIView(), first = UIButton(), replacement = UIButton()
        background.addSubview(first)
        background.addSubview(replacement)
        var completion: (@MainActor () -> Void)?, posts = 0
        panel.performDismissal = { completion = $0 }
        panel.post = { notification, target in
            posts += 1
            XCTAssertEqual(notification, .screenChanged)
            XCTAssertTrue((target as? UIView) === replacement)
            XCTAssertFalse(background.accessibilityElementsHidden)
            XCTAssertEqual(panel.state, .closed)
        }
        XCTAssertTrue(open(panel, background: background, target: first))
        XCTAssertTrue(panel.dismiss())
        XCTAssertEqual(posts, 0)
        XCTAssertTrue(background.accessibilityElementsHidden)
        panel.returnTarget = replacement
        completion?()
        completion?()
        XCTAssertEqual(posts, 1)
        XCTAssertNil(panel.returnTarget)
        panel.post = { _, _ in }
    }
```

## Q089 · test repair

Our snapshot-level check sees a Details title even when pressing the control no longer invokes Details. Strengthen this at the actual primary-action entry point.

[Working implementation](../../code-examples/platforms/tvos-uikit-v1/Sources/TelevisionActions.swift) · [Defective implementation](../../code-examples/platforms/tvos-uikit-v1/NegativeFixtures/LostOrdinaryDetails.swift) · [Full test suite](../../code-examples/platforms/tvos-uikit-v1/Tests/TelevisionActionsTests.swift) · [Source contract](../../code-examples/platforms/tvos-uikit-v1/manifest.json)

Registered failing assertion(s): TelevisionActionsTests/testOrdinaryDetails.

```swift
func testOrdinaryDetails() { var d = 0; let r = row(details: {d += 1}); r.details.sendActions(for: .primaryActionTriggered); XCTAssertEqual(d, 1) }
```

## Q090 · implementation repair

Cancellation of an earlier caption load clears the newer load’s state. Can you demonstrate overlapping requests and keep the newer one alive?

[Working implementation](../../code-examples/swiftui/media-macos-v1/Sources/MediaSelection.swift) · [Defective implementation](../../code-examples/swiftui/media-macos-v1/NegativeFixtures/cancel.swift) · [Full test suite](../../code-examples/swiftui/media-macos-v1/Tests/MediaSelectionTests.swift) · [Source contract](../../code-examples/swiftui/media-macos-v1/manifest.json)

Registered failing assertion(s): MediaSelectionTests/testCancelledOldTaskCannotCancelNewerLoad.

```swift
func testCancelledOldTaskCannotCancelNewerLoad() async throws {
        try await fixture { store, _, _, group in
            var continuation: CheckedContinuation<Void, Never>?
            let task = Task { @MainActor in
                await store.refresh { _, _ in
                    await withCheckedContinuation { continuation = $0 }
                    return group
                }
            }
            while continuation == nil { await Task.yield() }
            task.cancel()
            let newer = store.beginLoad()
            continuation?.resume()
            await task.value
            store.complete(newer, result: .success(group))
            XCTAssertTrue(store.isCurrent)
        }
    }
```

## Q091 · implementation repair

The design tool and our checker disagree when a swatch is supplied in a linear color space. Can you make equivalent displayed colors yield comparable ratios?

[Working implementation](../../code-examples/pilots/uikit-contrast-v1/Sources/ContrastUIKit.swift) · [Defective implementation](../../code-examples/pilots/uikit-contrast-v1/NegativeFixtures/WrongColorSpace.swift) · [Full test suite](../../code-examples/pilots/uikit-contrast-v1/Tests/ContrastUIKitTests.swift) · [Source contract](../../code-examples/pilots/uikit-contrast-v1/manifest.json)

Registered failing assertion(s): ContrastUIKitTests/testLinearColorSpaceIsConvertedBeforeFormula.

```swift
func testLinearColorSpaceIsConvertedBeforeFormula() throws {
        let space = try XCTUnwrap(CGColorSpace(name: CGColorSpace.linearSRGB))
        let cg = try XCTUnwrap(CGColor(colorSpace: space, components: [0.21404114048223255, 0.21404114048223255, 0.21404114048223255, 1]))
        let resolved = try ConfiguredContrast.resolve(UIColor(cgColor: cg), traits: traits(.light))
        XCTAssertEqual(resolved.red, 0.5, accuracy: 0.0001)
        XCTAssertEqual(resolved.luminance, 0.21404114048223255, accuracy: 0.0001)
    }
```

## Q092 · test repair

This timing assertion passes for every nonnegative duration. Can you make the check distinguish a reduced-motion transition from the ordinary transition?

[Working implementation](../../code-examples/pilots/uikit-preferences-v1/Sources/PreferenceUIKit.swift) · [Defective implementation](../../code-examples/pilots/uikit-preferences-v1/NegativeFixtures/IgnoredMotion.swift) · [Full test suite](../../code-examples/pilots/uikit-preferences-v1/Tests/PreferenceUIKitTests.swift) · [Source contract](../../code-examples/pilots/uikit-preferences-v1/manifest.json)

Registered failing assertion(s): PreferenceUIKitTests/testReducedMotionUsesImmediateTransition.

```swift
func testReducedMotionUsesImmediateTransition() {
        XCTAssertEqual(MotionPolicy.duration(reduceMotion: true), 0)
    }
```

## Q093 · implementation repair

On Apple TV, enabling Reduce Motion also prevents the updated status text from appearing. Can you separate the visible result from the optional animation?

[Working implementation](../../code-examples/platforms/tvos-results-v1/Sources/TelevisionResults.swift) · [Defective implementation](../../code-examples/platforms/tvos-results-v1/NegativeFixtures/MotionHidesContent.swift) · [Full test suite](../../code-examples/platforms/tvos-results-v1/Tests/TelevisionResultsTests.swift) · [Source contract](../../code-examples/platforms/tvos-results-v1/manifest.json)

Registered failing assertion(s): TelevisionResultsTests/testReducedMotionStillUpdatesContent.

```swift
func testReducedMotionStillUpdatesContent() { var animations = 0; let s = TelevisionStatus(reduceMotion: {true}, animate: {animations += 1}); s.update("Ready"); XCTAssertEqual(s.label.text, "Ready"); XCTAssertEqual(s.label.accessibilityLabel, "Ready"); XCTAssertEqual(animations, 0) }
```

## Q094 · implementation repair

An outline data-source callback for a removed parent still returns children. Can you reject stale parent requests while current parents continue working?

[Working implementation](../../code-examples/platforms/macos-structure-v1/Sources/DesktopOutline.swift) · [Defective implementation](../../code-examples/platforms/macos-structure-v1/NegativeFixtures/StaleNode.swift) · [Full test suite](../../code-examples/platforms/macos-structure-v1/Tests/DesktopOutlineTests.swift) · [Source contract](../../code-examples/platforms/macos-structure-v1/manifest.json)

Registered failing assertion(s): DesktopOutlineTests/testRemovedNodeCannotSupplyStaleChildren.

```swift
func testRemovedNodeCannotSupplyStaleChildren() throws {
        let d = configured(), old = try XCTUnwrap(d.nodes["g"])
        XCTAssertTrue(d.apply([]))
        XCTAssertEqual(d.outlineView(d.outline, numberOfChildrenOfItem: old), 0)
        XCTAssertFalse(d.outlineView(d.outline, isItemExpandable: old))
    }
```

## Q095 · implementation repair

After a form action becomes disabled it remains in our owned Tab cycle. Can you rebuild the cycle in the supplied order with only eligible controls?

[Working implementation](../../code-examples/platforms/macos-navigation-v1/Sources/DesktopNavigation.swift) · [Defective implementation](../../code-examples/platforms/macos-navigation-v1/NegativeFixtures/DisabledKeyView.swift) · [Full test suite](../../code-examples/platforms/macos-navigation-v1/Tests/DesktopNavigationTests.swift) · [Source contract](../../code-examples/platforms/macos-navigation-v1/manifest.json)

Registered failing assertion(s): DesktopNavigationTests/testDisabledKeyViewExcluded.

```swift
func testDisabledKeyViewExcluded() { let a = button(), b = button(), c = button(), order = DesktopKeyOrder(); b.isEnabled = false; order.apply([a,b,c]); XCTAssertTrue(a.nextKeyView === c); XCTAssertNil(b.nextKeyView) }
```

## Q096 · implementation repair

Searching for a word after a family emoji highlights the wrong text. Can you return the intended substring without changing the user's selection?

[Working implementation](../../code-examples/pilots/uikit-edited-rotor-v1/Sources/EditedRotorUIKit.swift) · [Defective implementation](../../code-examples/pilots/uikit-edited-rotor-v1/NegativeFixtures/CharacterOffsets.swift) · [Full test suite](../../code-examples/pilots/uikit-edited-rotor-v1/Tests/EditedRotorUIKitTests.swift) · [Source contract](../../code-examples/pilots/uikit-edited-rotor-v1/manifest.json)

Registered failing assertion(s): EditedRotorUIKitTests/testUnicodePrefixProducesCorrectNativeRange.

```swift
func testUnicodePrefixProducesCorrectNativeRange() {
        let reader = EditedMatchReader()
        reader.replace(text: "\u{1F600} e\u{301} target", query: "target")
        let item = search(reader)
        XCTAssertNotNil(item)
        XCTAssertEqual(location(item, in: reader), 6)
        if let range = item?.targetRange { XCTAssertEqual(reader.textView.text(in: range), "target") }
    }
```

## Q097 · implementation repair

Our long shipping options stop after one line when someone chooses a large text size. Can you keep the full option readable without changing which option is selected?

[Working implementation](../../code-examples/pilots/uikit-choice-v1/Sources/ChoiceUIKit.swift) · [Defective implementation](../../code-examples/pilots/uikit-choice-v1/NegativeFixtures/SingleLine.swift) · [Full test suite](../../code-examples/pilots/uikit-choice-v1/Tests/ChoiceUIKitTests.swift) · [Source contract](../../code-examples/pilots/uikit-choice-v1/manifest.json)

Registered failing assertion(s): ChoiceUIKitTests/testMultilinePolicyReplacesShrinkToFit.

```swift
func testMultilinePolicyReplacesShrinkToFit() {
        let row = cell()
        for label in [row.nameLabel, row.stateLabel] {
            label.numberOfLines = 1
            label.adjustsFontSizeToFitWidth = true
        }
        configure(row)
        for label in [row.nameLabel, row.stateLabel] {
            XCTAssertEqual(label.numberOfLines, 0)
            XCTAssertEqual(label.lineBreakMode, .byWordWrapping)
            XCTAssertFalse(label.adjustsFontSizeToFitWidth)
            XCTAssertTrue(label.adjustsFontForContentSizeCategory)
        }
    }
```

## Q098 · implementation repair

The native player has a forced subtitle option selected, but our full-caption menu reports Off. Can the menu distinguish an unrepresented selection from no selection?

[Working implementation](../../code-examples/swiftui/media-macos-v2/Sources/MediaSelection.swift) · [Defective implementation](../../code-examples/swiftui/media-macos-v2/NegativeFixtures/unmappedoff.swift) · [Full test suite](../../code-examples/swiftui/media-macos-v2/Tests/ReviewRegressionTests.swift) · [Source contract](../../code-examples/swiftui/media-macos-v2/manifest.json)

Registered failing assertion(s): ReviewRegressionTests/testForcedSelectionIsNotOff.

```swift
func testForcedSelectionIsNotOff() async throws {
        try await fixture { store, item, group in
            let forced = try XCTUnwrap(group.options.first { $0.hasMediaCharacteristic(.containsOnlyForcedSubtitles) })
            item.select(forced, in: group)
            XCTAssertNotNil(store.selection.wrappedValue)
        }
    }
```

## Q099 · test repair

The shelf remains on screen even when its items disappear as independent accessibility targets. Update the unit check to distinguish the two structures.

[Working implementation](../../code-examples/platforms/tvos-structure-v1/Sources/TelevisionShelves.swift) · [Defective implementation](../../code-examples/platforms/tvos-structure-v1/NegativeFixtures/CombinedShelf.swift) · [Full test suite](../../code-examples/platforms/tvos-structure-v1/Tests/TelevisionShelvesTests.swift) · [Source contract](../../code-examples/platforms/tvos-structure-v1/manifest.json)

Registered failing assertion(s): TelevisionShelvesTests/testShelvesPreserveIndependentHeadingAndButtons.

```swift
func testShelvesPreserveIndependentHeadingAndButtons() {
        let v = configured(), shelf = v.shelves[0]
        XCTAssertFalse(v.isAccessibilityElement); XCTAssertFalse(shelf.isAccessibilityElement)
        XCTAssertTrue(shelf.heading.isAccessibilityElement); XCTAssertTrue(shelf.heading.accessibilityTraits.contains(.header))
        XCTAssertEqual(shelf.heading.text, "Featured")
        XCTAssertEqual(shelf.buttons.map { $0.title(for: .normal) }, ["Alpha", "Beta"])
        XCTAssertEqual(shelf.buttons.map(\.accessibilityLabel), ["Alpha", "Beta"])
    }
```

## Q100 · implementation repair

An ordinary alternate language track shows up as audio description. Can you make inspection use evidence from the track while leaving playback untouched?

[Working implementation](../../code-examples/pilots/uikit-media-metadata-v1/Sources/MediaMetadata.swift) · [Defective implementation](../../code-examples/pilots/uikit-media-metadata-v1/NegativeFixtures/AllAudioDescribed.swift) · [Full test suite](../../code-examples/pilots/uikit-media-metadata-v1/Tests/MediaMetadataTests.swift) · [Source contract](../../code-examples/pilots/uikit-media-metadata-v1/manifest.json)

Registered failing assertion(s): MediaMetadataTests/testUntaggedAlternateAudioIsNotDescription.

```swift
func testUntaggedAlternateAudioIsNotDescription() async throws {
        let url = try DescriptionFixture.write(tagged: false)
        defer { try? FileManager.default.removeItem(at: url) }
        let rows = options(try await MediaMetadata.group(.audible, item: AVPlayerItem(url: url)))
        XCTAssertEqual(rows.count, 2)
        XCTAssertTrue(rows.allSatisfy { !$0.describesVideo })
    }
```

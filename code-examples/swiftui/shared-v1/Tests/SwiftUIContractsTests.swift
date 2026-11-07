import XCTest
import SwiftUI
import AVFoundation
@testable import AccessibilityExamples

@MainActor final class SemanticsTests: XCTestCase {
    func testBindingReadsCurrentNativeToggleState() { let s = SettingsState(); XCTAssertFalse(s.toggle.wrappedValue); s.toggle.wrappedValue = true; XCTAssertTrue(s.toggle.wrappedValue); XCTAssertEqual(s.value, "On") }
    func testRepeatedBindingSetDoesNotDuplicateCallback() { let s = SettingsState(); var n = 0; s.changed = { _ in n += 1 }; s.toggle.wrappedValue = true; s.toggle.wrappedValue = true; XCTAssertEqual(n, 1) }
    func testDisabledBindingPreservesState() { let s = SettingsState(); s.disabled = true; s.toggle.wrappedValue = true; XCTAssertFalse(s.enabled) }
    func testBothToggleTransitionsRefreshValue() { let s = SettingsState(); s.toggle.wrappedValue = true; s.toggle.wrappedValue = false; XCTAssertEqual(s.value, "Off") }
    func testConfigureClearsPriorStatusAndPriorityWithoutReuse() { let s = SettingsState(); s.configure(title: "One", status: "Pending", priority: true); s.configure(title: "Two", status: "", priority: false); XCTAssertEqual(s.name, "Two"); XCTAssertEqual(s.status, "") }
    func testCurrentPriorityNameAndStatus() { let s = SettingsState(); s.configure(title: "Report", status: "Ready", priority: true); XCTAssertEqual(s.name, "Report, Priority"); XCTAssertEqual(s.status, "Ready") }
    func testOrdinaryHelpUsesExistingCallback() { let s = SettingsState(); var n = 0; s.help = { n += 1 }; s.openHelp(); XCTAssertEqual(n, 1) }
    func testDisabledHelpDoesNotInvoke() { let s = SettingsState(); var n = 0; s.help = { n += 1 }; s.disabled = true; s.openHelp(); XCTAssertEqual(n, 0) }
    func testOrdinarySetterAndAdjustmentShareValue() { let s = SettingsState(); var values: [Int] = []; s.amountChanged = { values.append($0) }; s.setAmount(70); s.adjust(.increment); s.adjust(.decrement); XCTAssertEqual(values, [70,75,70]) }
    func testBoundsDoNotDuplicateChange() { let s = SettingsState(); var n = 0; s.amountChanged = { _ in n += 1 }; s.setAmount(101); s.adjust(.increment); XCTAssertEqual(s.amount, 100); XCTAssertEqual(n, 1); s.setAmount(-1); s.adjust(.decrement); XCTAssertEqual(s.amount, 0); XCTAssertEqual(n, 2) }
    func testDisabledAdjustmentCannotChangeState() { let s = SettingsState(); s.disabled = true; s.adjust(.increment); XCTAssertEqual(s.amount, 50) }
    func testHintTracksCurrentAvailability() { let s = SettingsState(); XCTAssertEqual(s.hint, ""); s.disabled = true; XCTAssertFalse(s.hint.isEmpty); s.disabled = false; XCTAssertEqual(s.hint, "") }
}

@MainActor final class DocumentTests: XCTestCase {
    let a = Article(id: "a", title: "First", important: true), b = Article(id: "b", title: "Second", important: false)
    func testLandmarksAreSubsetNotEveryRow() { let s = DocumentState(); s.replace([a,b]); XCTAssertEqual(s.landmarks.map(\.id), ["a"]) }
    func testDuplicateIDsRejectUpdateAtomically() { let s = DocumentState(); s.replace([a,b]); XCTAssertFalse(s.replace([a,a])); XCTAssertEqual(s.entries, [a,b]) }
    func testSelectionSurvivesReorder() { let s = DocumentState(); s.replace([a,b]); s.action(for: "a")(); s.replace([b,a]); XCTAssertEqual(s.selected, "a") }
    func testRemovedSelectionClears() { let s = DocumentState(); s.replace([a,b]); s.action(for: "a")(); s.replace([b]); XCTAssertNil(s.selected) }
    func testOldActionDoesNotTargetReboundRow() { let s = DocumentState(); s.replace([a]); let old = s.action(for: "a"); s.replace([Article(id: "a", title: "New", important: true)]); old(); XCTAssertNil(s.selected) }
    func testOrdinarySelectionUsesCurrentItem() { let s = DocumentState(); s.replace([a,b]); var ids: [String] = []; s.chosen = { ids.append($0) }; s.action(for: "b")(); XCTAssertEqual(ids, ["b"]) }
    func testDeleteCurrentItemOnceAndClearSelection() { let s = DocumentState(); s.replace([a,b]); s.action(for: "a")(); var ids: [String] = []; s.deleted = { ids.append($0) }; let delete = s.action(for: "a", remove: true); delete(); delete(); XCTAssertEqual(ids, ["a"]); XCTAssertEqual(s.entries, [b]); XCTAssertNil(s.selected) }
    func testUnknownItemActionIsQuiet() { let s = DocumentState(); s.replace([a]); s.action(for: "missing")(); XCTAssertNil(s.selected) }
    func testRetainedActionDoesNotRetainOwner() { var s: DocumentState? = DocumentState(); s!.replace([a]); weak var owner = s; let action = s!.action(for: "a"); s = nil; action(); XCTAssertNil(owner) }
    func testEmptyDocumentHasNoLandmarksOrSelection() { let s = DocumentState(); s.replace([a]); s.action(for: "a")(); s.replace([]); XCTAssertTrue(s.landmarks.isEmpty); XCTAssertNil(s.selected) }
}

final class PreferenceTests: XCTestCase {
    func testReducedMotionPolicyKeepsFinalStateIndependent() { var p = PresentationPolicy(); XCTAssertTrue(p.animate); p.reduceMotion = true; XCTAssertFalse(p.animate); XCTAssertEqual(p.selectedText, "Selected") }
    func testTransparencyPolicyPreservesNonColorText() { let p = PresentationPolicy(reduceTransparency: true); XCTAssertTrue(p.opaqueBackground); XCTAssertEqual(p.selectedText, "Selected") }
    func testLargeTextPolicyUsesVerticalComposition() { let p = PresentationPolicy(expandedText: true); XCTAssertTrue(p.vertical) }
    func testNormalTextDoesNotForceVerticalComposition() { XCTAssertFalse(PresentationPolicy().vertical) }
    func testDifferentiateFlagDoesNotRequireMotion() { let p = PresentationPolicy(reduceMotion: true, differentiateWithoutColor: true); XCTAssertFalse(p.animate); XCTAssertTrue(p.differentiateWithoutColor) }
    func testPreferencesAreIndependent() { let p = PresentationPolicy(reduceTransparency: true, expandedText: true); XCTAssertTrue(p.animate); XCTAssertTrue(p.vertical); XCTAssertFalse(p.differentiateWithoutColor) }
}

@MainActor final class LifecycleTests: XCTestCase {
    func testBeginRecordsEntryWithoutRestorationRequest() { let s = PresentationState(); var n = 0; s.request = { _ in n += 1 }; _ = s.begin(from: "row"); XCTAssertTrue(s.showing); XCTAssertEqual(s.focus, "close"); XCTAssertEqual(n, 0) }
    func testDismissResolvesCurrentOrigin() { let s = PresentationState(); let t = s.begin(from: "row"); s.eligible = ["row"]; s.dismissed(t); XCTAssertEqual(s.focus, "row"); XCTAssertFalse(s.showing) }
    func testRemovedOriginUsesFallback() { let s = PresentationState(); s.eligible = ["row"]; let t = s.begin(from: "row"); s.eligible = []; s.dismissed(t); XCTAssertEqual(s.focus, "open") }
    func testOldDismissalCannotConsumeNewSession() { let s = PresentationState(); let old = s.begin(from: "old"); _ = s.begin(from: "new"); s.dismissed(old); XCTAssertTrue(s.showing); XCTAssertEqual(s.focus, "close") }
    func testRepeatedDismissIsQuiet() { let s = PresentationState(); var n = 0; s.request = { _ in n += 1 }; let t = s.begin(from: "row"); s.dismissed(t); s.dismissed(t); XCTAssertEqual(n, 1) }
    func testCancellationUsesSameRestorationContract() { let s = PresentationState(); let t = s.begin(from: "row"); s.cancel(t); XCTAssertFalse(s.showing); XCTAssertEqual(s.focus, "open") }
    func testReentrantRequestPreservesNewPresentation() { let s = PresentationState(); s.request = { _ in _ = s.begin(from: "new") }; let t = s.begin(from: "old"); s.dismissed(t); XCTAssertTrue(s.showing); XCTAssertEqual(s.focus, "close") }
    func testEligibleListIsEvaluatedAtCompletion() { let s = PresentationState(); let t = s.begin(from: "row"); s.eligible.insert("row"); s.dismissed(t); XCTAssertEqual(s.focus, "row") }
}

@MainActor final class FormsMediaTests: XCTestCase {
    func testFormPreservesRawInputSnapshot() { let s = FormMediaState(); s.text = " x "; var value: String?; s.accepted = { value = $0 }; s.submit(); XCTAssertEqual(value, " x ") }
    func testEditBindingInvalidatesPendingReply() { let s = FormMediaState(); var reply: (@MainActor (String?) -> Void)?; s.validate = { _, r in reply = r }; s.submit(); s.input.wrappedValue = "new"; reply?("Old error"); XCTAssertNil(s.error); XCTAssertFalse(s.busy) }
    func testOutOfOrderValidationCannotOverwriteLatest() { let s = FormMediaState(); var replies: [@MainActor (String?) -> Void] = []; s.validate = { _, r in replies.append(r) }; s.submit(); s.submit(); replies[1]("Latest"); replies[0]("Old"); XCTAssertEqual(s.error, "Latest") }
    func testDuplicateSuccessDoesNotSaveTwice() { let s = FormMediaState(); var reply: (@MainActor (String?) -> Void)?; var n = 0; s.validate = { _, r in reply = r }; s.accepted = { _ in n += 1 }; s.submit(); reply?(nil); reply?(nil); XCTAssertEqual(n, 1) }
    func testDirectEditRejectsOldSnapshot() { let s = FormMediaState(); var reply: (@MainActor (String?) -> Void)?; s.validate = { _, r in reply = r }; s.submit(); s.text = "different"; reply?("Old"); XCTAssertNil(s.error); XCTAssertFalse(s.busy) }
    func testInvalidThenCorrectedFormRecovers() { let s = FormMediaState(); s.validate = { _, r in r("Invalid email") }; s.submit(); XCTAssertEqual(s.error, "Invalid email"); s.input.wrappedValue = "correct"; XCTAssertNil(s.error); s.validate = { _, r in r(nil) }; var saved = false; s.accepted = { _ in saved = true }; s.submit(); XCTAssertTrue(saved) }
    func testEmptyValidationMessageIsUnavailableNotSuccess() { let s = FormMediaState(); s.validate = { _, r in r("") }; s.submit(); XCTAssertEqual(s.error, "Validation unavailable") }
    func testReentrantSaveOwnsNewRequest() { let s = FormMediaState(); s.accepted = { _ in s.validate = { _, _ in }; s.submit() }; s.submit(); XCTAssertTrue(s.busy) }
    func testRetainedReplyDoesNotRetainForm() { var s: FormMediaState? = FormMediaState(); weak var owner = s; var reply: (@MainActor (String?) -> Void)?; s!.validate = { _, r in reply = r }; s!.submit(); s = nil; reply?(nil); XCTAssertNil(owner) }
    func testMissingAndEmptyMediaAreDifferentStates() { let s = MediaState(); XCTAssertEqual(s.status, "Options unavailable"); s.load { $0([]) }; XCTAssertEqual(s.status, "No caption options") }
    func testMediaSelectionSurvivesReorder() { let s = MediaState(); let a = TrackChoice(id: "a", name: "English", descriptive: false), b = TrackChoice(id: "b", name: "French", descriptive: false); s.load { $0([a,b]) }; s.choose("a"); s.load { $0([b,a]) }; XCTAssertEqual(s.selected, "a") }
    func testRemovedTrackSelectionClears() { let s = MediaState(); let a = TrackChoice(id: "a", name: "English", descriptive: false); s.load { $0([a]) }; s.choose("a"); s.load { $0([]) }; XCTAssertNil(s.selected) }
    func testStaleTrackLoadIsIgnored() { let s = MediaState(); var replies: [@MainActor ([TrackChoice]) -> Void] = []; s.load { replies.append($0) }; s.load { replies.append($0) }; replies[1]([]); replies[0]([TrackChoice(id: "old", name: "Old", descriptive: false)]); XCTAssertTrue(s.tracks.isEmpty) }
    func testUnknownTrackCannotChangeSelection() { let s = MediaState(); s.load { $0([]) }; s.choose("missing"); XCTAssertNil(s.selected) }
    func testMetadataChoiceDoesNotMutatePlayerPreferences() { let p = AVPlayer(); p.volume = 0.3; p.isMuted = true; let s = MediaState(player: p); s.load { $0([]) }; s.choose(nil); XCTAssertTrue(s.player === p); XCTAssertEqual(p.volume, 0.3); XCTAssertTrue(p.isMuted) }
    func testDuplicateTrackIDsAreNotAccepted() { let s = MediaState(); let a = TrackChoice(id: "a", name: "One", descriptive: false); s.load { $0([a,a]) }; XCTAssertFalse(s.loaded) }
}

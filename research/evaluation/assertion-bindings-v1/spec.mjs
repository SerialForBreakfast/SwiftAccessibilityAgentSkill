// Explicit author-selected mappings, not name-similarity promotion. Controller only.
const b=(packagePath,owner,names,proves,remaining)=>({manifest:packagePath+'/manifest.json',testIds:names.map(n=>owner+'/'+n),proves,remaining});
const sw=p=>'code-examples/swiftui/'+({iOS:'ios',macOS:'macos',tvOS:'tvos'}[p])+'-v1';
const pilot=n=>'code-examples/pilots/uikit-'+n+'-v1';
const native=(p,n)=>'code-examples/platforms/'+({iOS:'ios',macOS:'macos',tvOS:'tvos'}[p])+'-'+n+'-v1';
export function selections(c){
 const maps={};const add=(index,...bindings)=>maps[index]=bindings;
 if(!c.controller.note)return maps;
 if(!['iOS','macOS','tvOS'].includes(c.platform))return maps;
 if(c.framework==='AppKit'&&c.platform!=='macOS')return maps;
 if(c.framework==='UIKit'&&c.platform==='macOS')return maps;
 if(c.framework==='SwiftUI'){
  const pkg=sw(c.platform),s=(owner,names,proves,remaining)=>b(pkg,owner,names,proves,remaining);
  switch(c.topic){
   case 'semantics':add(1,s('SemanticsTests',['testBindingReadsCurrentNativeToggleState','testBothToggleTransitionsRefreshValue'],'Application Binding roundtrip and value transitions.','Does not assert native Toggle generated semantics or prove absence of an existing accessibility defect.'));break;
   case 'state':
    add(0,s('SemanticsTests',['testConfigureClearsPriorStatusAndPriorityWithoutReuse','testHintTracksCurrentAvailability'],'State name/status clear and derived hint changes on the same model.','Optional native help and the complete reused download card remain outside this fixture.'));
    add(1,s('FormsMediaTests',['testStaleTrackLoadIsIgnored','testDirectEditRejectsOldSnapshot'],'Out-of-order track loads and changed form snapshots reject stale state.','No complete download-card item/request identity contract; separate models must not be combined as one implementation.'));
    add(2,s('DocumentTests',['testOrdinarySelectionUsesCurrentItem'],'Current-item application callback selects the requested document.','Not an executed SwiftUI Open button closure or preservation of all card state.'));break;
   case 'actions':
    add(0,s('DocumentTests',['testOrdinarySelectionUsesCurrentItem','testDeleteCurrentItemOnceAndClearSelection'],'Application ordinary selection and delete transitions.','No unit proof that visible and accessibility modifier closures are both installed.'));
    add(1,s('DocumentTests',['testOldActionDoesNotTargetReboundRow'],'Old document action cannot select a replacement revision.','Disabled Delete action policy is not asserted by this test.'));
    add(2,s('InteropTests',['testCoordinatorReplacesOldCallback','testOldNativeViewCannotDispatchAfterRebind'],'Native coordinator replaces handler and detaches old view action path.','Native representable subset, not every pure SwiftUI row closure or generated semantics.'));break;
   case 'structure':add(1,s('DocumentTests',['testLandmarksAreSubsetNotEveryRow','testSelectionSurvivesReorder','testRemovedSelectionClears'],'Application landmark subset and selection identity across reorder/removal.','No assertion of generated grouping, ordinary accessibility traversal or rotor discoverability.'));break;
   case 'lifecycle':
    add(0,s('LifecycleTests',['testDismissResolvesCurrentOrigin','testEligibleListIsEvaluatedAtCompletion','testRemovedOriginUsesFallback'],'Requested focus state resolves current eligibility and fallback.','Application request state, not delivery to assistive technology.'));
    add(1,s('LifecycleTests',['testOldDismissalCannotConsumeNewSession','testRepeatedDismissIsQuiet','testReentrantRequestPreservesNewPresentation'],'Old and duplicate completions cannot consume a replacement presentation.','No OS scheduling or delivered-focus guarantee.'));break;
   case 'media':
    add(0,s('FormsMediaTests',['testMissingAndEmptyMediaAreDifferentStates'],'Application unavailable and empty caption-option states differ.','Missing error/audio-description cases and actual loaded AV media groups.'));
    add(1,s('FormsMediaTests',['testStaleTrackLoadIsIgnored'],'Old application track load cannot replace newer list.','Actual current AVPlayerItem identity is not asserted.'));
    add(2,s('FormsMediaTests',['testMediaSelectionSurvivesReorder','testMetadataChoiceDoesNotMutatePlayerPreferences'],'Synthetic selection survives reorder; AVPlayer identity, mute and volume remain unchanged.','No native selected audio/subtitle group assertion; mute/volume preservation is not equivalent.'));break;
  }
  return maps;
 }
 if(!['UIKit','AppKit'].includes(c.framework))return maps;
 const p=c.platform,mac=p==='macOS',ios=p==='iOS';
 const actionPkg=ios?pilot('dynamic'):native(p,mac?'appkit':'uikit');
 const owner=ios?'DynamicUIKitTests':mac?'DesktopActionsTests':'TelevisionActionsTests';
 const ordinary=ios?['testOrdinaryButtonsUseCurrentItemAfterReuse']:mac?['testOrdinaryOpenOnly','testOrdinarySaveOnly']:['testOrdinaryPlay','testOrdinaryDetails'];
 const statePkg=native(p,'closure');
 switch(c.topic){
  case 'state':
   if(ios)add(0,b(pilot('semantics'),'UIKitSemanticsTests',['testReconfigurationClearsStaleHintAndValue'],'Native metadata clears during repeated configuration.','Complete download-card status/help/selected integration is not asserted.'));
   else add(0,b(mac?actionPkg:native(p,'state-recovery'),mac?owner:'StateContractTests',[mac?'testReuseClearsOwnedValue':'testReconfigureClearsStaleSelectionText'],'Previously owned native value or selection text is cleared.','Does not cover every optional status/help field.'));
   add(1,b(statePkg,'MediaLoadOwnerTests',['testReplacementRejectsOldItemCompletion','testSameItemNewRequestRejectsOldGeneration','testExternalReplacementRejectsOldResult'],'Current AV item and request generation reject late completions.','Media owner fixture, not complete reuse-card integration.'));
   add(2,b(actionPkg,owner,ordinary,'Ordinary native paths invoke current independent callbacks.','Different example task names; all unrelated card state is not asserted.'));break;
  case 'actions':
   add(0,b(actionPkg,owner,ordinary,'Independent ordinary native controls remain callable.','Fixture operation names may differ from Delete; task equivalence requires rubric review.'));
   add(1,b(actionPkg,owner,ios?['testRetainedOldActionCannotAffectReusedView','testDisableAndReenableRefreshesBothActionPaths']:mac?['testStaleShortcutRejected','testDisabledOrdinarySave','testDisabledShortcut']:['testStaleActionRejected','testDisabledOrdinaryAction','testDisabledCustomAction'],'Stale shortcut is rejected and disabled ordinary/custom paths do not act.','Different domain operation; no delivered interaction claim.'));
   add(2,b(actionPkg,owner,ios?['testRetainedCustomActionDoesNotKeepViewAlive','testNativeActionIdentifierReplacesPreviousHandler']:mac?['testRepeatedConfigurationDoesNotDuplicateActions','testShortcutDoesNotRetainRow']:['testSingleShortcutAfterReuse','testActionDoesNotRetainRow'],'Repeated handler configuration and owner lifetime are bounded.','Not every application-specific teardown sequence.'));break;
  case 'structure':
   if(ios)add(0,b(pilot('naming'),'NamingUIKitTests',['testContainerPreservesIndependentControls'],'Native container and independent exposed button configuration.','Not delivered traversal or the proposed report-specific layout.'));
   else add(0,b(actionPkg,owner,[mac?'testContainerDoesNotReplaceControls':'testContainerPreservesControls'],'Native independent child controls are configured as elements.','Not delivered traversal or report-specific layout.'));
   add(1,ios?b(pilot('dynamic'),'DynamicUIKitTests',['testReorderPreservesIdentityAndChangesSearchOrder','testRemovedCurrentItemUsesDeclaredBoundaryPolicy'],'Native element identity/order and direct rotor search-block results across changes.','Direct search-block invocation is not rotor discoverability.'):mac?b(native(p,'structure'),'DesktopOutlineTests',['testSelectedChildSurvivesSiblingReorder','testRemovedSelectionClears'],'Native outline selection follows stable identity across reorder and removal.','Outline fixture does not establish every report heading/group contract.'):b(statePkg,'EditedRotorUIKitTests',['testNewRevisionRestartsRetainedResult','testEmptyQueryUpdatesOrdinaryDocumentWithoutRotor'],'Text revision invalidation and ordinary document content survive rotor changes.','Text fixture is narrower than report-row grouping.'));break;
  case 'text':
   if(ios){add(0,b(pilot('choice'),'ChoiceUIKitTests',['testFontsMatchEffectiveLargeTextEnvironment','testRepeatedSizeTransitionsDoNotAccumulateScaling'],'Native font configuration follows explicit effective content-size traits.','No automatic notification delivery, Pay control or rendered layout proof.'));add(1,b(pilot('choice'),'ChoiceUIKitTests',['testLongLocalizedContentRemainsVerbatim','testSelfSizingConfigurationAndVerticalConstraintChain'],'Localized text and configured self-sizing constraint policy remain intact.','No Pay callback/design font preservation assertion; different valid layouts remain accepted.'));}
   if(p==='tvOS')add(0,b(statePkg,'StateContractTests',['testTextUsesFlexibleSemanticConfigurationWithoutOS27Claim'],'Native flexible text configuration only.','No tvOS 27 system Larger Text availability or live scaling inference.'));
   break;
  case 'lifecycle':{
   const pkg=ios?pilot('modal'):native(p,'lifecycle'),cl=ios?'ModalUIKitTests':mac?'DesktopLifecycleTests':'TelevisionLifecycleTests';
   add(0,b(pkg,cl,ios?['testNotificationWaitsForCompletionAndUsesCurrentTarget','testRetainedButRemovedTargetPostsNil']:['testCompletedModalRequestsOriginal','testRemovedOriginalUsesFallback'],'Completion-time target resolution and missing-target policy for native restoration request.','Recorded request, not delivered focus.'));
   add(1,b(pkg,cl,ios?['testOldCompletionCannotCloseReopenedPanel','testOrdinaryCloseAndEscapeShareDismissalGuard']:['testOldCompletionCannotConsumeNewSession','testDuplicateCompletionIsQuiet','testReentrantRequestPreservesNewSession'],'Stale completion and repeated dismissal handling protect current session.','iOS subset lacks an equivalent reentrant-request assertion in this selected fixture.'));
   break;}
  case 'media':{
   const meta=ios?pilot('media-metadata'):native(p,'media');
   add(0,b(statePkg,'MediaLoadOwnerTests',['testNilItemDoesNotInvokeLoader','testErrorIsNotMissingOrSuccessfulMetadata','testSameItemNewRequestRejectsOldGeneration'],'Absent item, failed load and loading owner states differ.','State-machine checks do not establish every metadata parser result.'),b(meta,'MediaMetadataTests',['testKnownMissingGroupIsAbsent','testMissingItemIsUnavailableRatherThanAbsent'],'Native media extraction distinguishes known missing group from missing item.','Content description quality and playback outcome remain outside assertions.'));
   add(1,b(statePkg,'MediaLoadOwnerTests',['testReplacementRejectsOldItemCompletion','testExternalReplacementRejectsOldResult'],'Late results cannot replace state after actual player-item replacement.','No claim about all real network schedules.'));
   add(2,b(meta,'MediaMetadataTests',['testInspectionPreservesChosenAudioAndSubtitleOff'],'Actual native audio selection and subtitle-off state survive metadata inspection.','Recorded fixture environment only, not all assets or playback behavior.'));
   break;}
 }
 return maps;
}

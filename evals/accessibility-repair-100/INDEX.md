# Browse the 100 questions

| Prompt and code | Platform | Developer question |
|---|---|---|
| [Q001](subjects/Q001.md) | iOS · UIKit | After a document becomes read-only its button still exposes editing actions. Can you update only the metadata owned by this feature? |
| [Q002](subjects/Q002.md) | iOS · UIKit | We configured the bookmark twice and asserted only its label. Please exercise a trait owned by another feature through selection and deselection. |
| [Q003](subjects/Q003.md) | iOS · UIKit | My checker returns a definitive contrast ratio for a translucent overlay even when its backdrop is unknown. Can you implement the documented opaque-only policy? |
| [Q004](subjects/Q004.md) | macOS · AppKit | Searching this Mac document can return part of a composed character. Can you restrict matches to whole text boundaries while keeping valid adjacent matches? |
| [Q005](subjects/Q005.md) | tvOS · UIKit | Refreshing an unchanged status keeps replaying its animation. Can you keep repeated updates quiet and still animate a genuine change when permitted? |
| [Q006](subjects/Q006.md) | iOS · UIKit | Our rotor test checks only whether the search index accepted the initial data. It should detect a missing or misordered accessibility element after a reorder. Check the container and the rotor installed on the view. |
| [Q007](subjects/Q007.md) | macOS · AppKit | A preference update queued before stop arrives after we restart observation. Can you prevent it from overwriting the new session’s effective preference? |
| [Q008](subjects/Q008.md) | iOS · UIKit | A saved rotor from the previous search still returns matches after the query changes. Can the current search work while the old one expires? |
| [Q009](subjects/Q009.md) | iOS · UIKit | Our seating chart has a seat that spans multiple coordinates. Looking it up by the first coordinate works but another covered coordinate gives the wrong result. Can you repair the table lookup? |
| [Q010](subjects/Q010.md) | iOS · UIKit | Our contrast test covers only black against white. It still passes with the wrong luminance calculation. Add a numerical fixture whose expected value comes from outside the function under test. |
| [Q011](subjects/Q011.md) | iOS · UIKit | Before a finite video finishes loading, our inspector sometimes calls it a live stream. Can you represent what is known about its duration without inventing a stream type? |
| [Q012](subjects/Q012.md) | iOS · UIKit | Opening the inspector before a player item exists tells users there are no accessible tracks. Can you distinguish unavailable inspection from a known empty result? |
| [Q013](subjects/Q013.md) | iOS · UIKit | Choosing the already-selected speed emits another playback change. Can you keep repeated selections quiet and still notify exactly once when the rate changes? |
| [Q014](subjects/Q014.md) | iOS · UIKit | Embedding the player removes the ordinary transport controls our users rely on. Can you restore native controls and preserve automatic media selection? |
| [Q015](subjects/Q015.md) | iOS · UIKit | Selecting an option removes traits another part of the app installed. How should this component change its own state while preserving the rest? |
| [Q016](subjects/Q016.md) | iOS · UIKit | After leaving this screen, preference changes still call back into its observer. Can you fix stop and restart, including the first value after returning? |
| [Q017](subjects/Q017.md) | iOS · UIKit | When Reduce Motion is on, this transition still takes the animated path. Can you keep the final content update and prove which transition was requested? |
| [Q018](subjects/Q018.md) | iOS · UIKit | Our reuse test checks the new title and misses a retained Remove action affecting the replacement item. How would you exercise the originally installed action after the change? |
| [Q019](subjects/Q019.md) | tvOS · UIKit | The shortcut has a contextual name but sighted users can’t tell what the visible action buttons do. Can you restore their ordinary titles and preserve the shortcuts? |
| [Q020](subjects/Q020.md) | macOS · AppKit | Submitting an invalid value can still invoke Save. Can the form retain the entered text, surface the error, and wait for a valid submission? |
| [Q021](subjects/Q021.md) | iOS · UIKit | After sorting results, the container’s exposed elements no longer match the visible items. Can you update the order while preserving the identity of surviving elements? |
| [Q022](subjects/Q022.md) | iOS · UIKit | Our media inspector reports the chosen audio track as unselected. Can you report the real selection accurately while keeping the player and its subtitle Off state unchanged? |
| [Q023](subjects/Q023.md) | macOS · AppKit | Removing a button from the form leaves its old next-key-view link alive. Can you release the links this helper installed during refresh and teardown? |
| [Q024](subjects/Q024.md) | iOS · UIKit | Our validation test simulates an edit using only the controller's public edit method. What test would expose a stale success after a text field was changed directly? |
| [Q025](subjects/Q025.md) | iOS · UIKit | The same dynamic foreground and background give us the same audit result under two explicitly supplied appearances. Can the checker honor the appearance being audited? |
| [Q026](subjects/Q026.md) | tvOS · UIKit | The preferred focus list includes a disabled control after a state change. Can you return eligible candidates and preserve their intended order? |
| [Q027](subjects/Q027.md) | iOS · UIKit | The grid test passes even if looking up the covered portion of a spanning seat returns nil. Give us a regression test for the actual lookup, including an uncovered coordinate. |
| [Q028](subjects/Q028.md) | iOS · UIKit | When full English subtitles are requested, our picker sometimes chooses a forced-dialogue-only option. Can you select the intended track and retain the Off path? |
| [Q029](subjects/Q029.md) | macOS · AppKit | Renaming an outline node recreates it, even though it represents the same document. Can you preserve the surviving node object through refresh? |
| [Q030](subjects/Q030.md) | macOS · AppKit | When a selected child’s siblings change order, the outline selects a different child. Can you restore the intended item after refresh? |
| [Q031](subjects/Q031.md) | iOS · UIKit | Our dismissal test inspects only the eventual notification count. It misses a focus request sent before the animation completion. Capture the intermediate state and check the final target. |
| [Q032](subjects/Q032.md) | macOS · AppKit | Two invoices have the same displayed title. Sorting them loses the selection. Can you preserve the selection across the reorder? |
| [Q033](subjects/Q033.md) | iOS · UIKit | After a document edit, a search that starts from a retained result continues from the old position. Can it restart according to the current document revision? |
| [Q034](subjects/Q034.md) | iOS · UIKit | Two validations finish in reverse order. The earlier response can replace the newest field errors. Can you drive the captured completions and keep the current result? |
| [Q035](subjects/Q035.md) | iOS · UIKit | Disabling this control stops normal interaction, but its accessibility activation can still submit. Can you align its return value and callback behavior in both states? |
| [Q036](subjects/Q036.md) | tvOS · UIKit | A retained result button can still choose an item after the shelf has been rebound. Can the current button respond to Select while the old button is inert? |
| [Q037](subjects/Q037.md) | macOS · SwiftUI | After SwiftUI updates this represented view, an action retained before the update can still dispatch. Can you test a rebind through the coordinator used by the view? |
| [Q038](subjects/Q038.md) | macOS · AppKit | A malformed refresh repeats an invoice ID. Reject the refresh without changing the previous rows or selection. How would you prove nothing was partly applied? |
| [Q039](subjects/Q039.md) | iOS · UIKit | A button is still retained in memory after removal from the window. Closing the panel should avoid requesting focus on it. Can you exercise that exact case? |
| [Q040](subjects/Q040.md) | iOS · UIKit | We reconfigure a visible row without dequeuing it again. It continues to advertise the previous order’s names. Can you repair live reconfiguration? |
| [Q041](subjects/Q041.md) | iOS · UIKit | The motion test checks the initial value but never changes the preference. Can you drive the notification and verify the new value while ignoring an unrelated notification? |
| [Q042](subjects/Q042.md) | iOS · UIKit | Our contrast checker gives suspicious ratios for gray on white even though black on white looks right. Fix the calculation and give me a numerical case that distinguishes the two. |
| [Q043](subjects/Q043.md) | macOS · SwiftUI | A document row has been rebound but its saved action can operate on the replacement document. Can the new action work while the retained one expires? |
| [Q044](subjects/Q044.md) | iOS · UIKit | The title in our choice row stays small inside a view with a larger content-size override. Can you make it follow the effective environment and keep the existing text style? |
| [Q045](subjects/Q045.md) | iOS · UIKit | Another controller can change the text view directly. A cached match then points into unrelated text. How should the search respond before its owner rebuilds the index? |
| [Q046](subjects/Q046.md) | macOS · SwiftUI | After a represented AppKit control is replaced, the old native control can still send an action. Can you test both the old sender and the replacement? |
| [Q047](subjects/Q047.md) | macOS · AppKit | The accessibility shortcut still saves, but our visible Mac Save control no longer does. Can you restore its ordinary route and verify each route dispatches once? |
| [Q048](subjects/Q048.md) | iOS · UIKit | Escape removes the overlay visually, but the accessibility configuration still describes a modal. Can you make both dismissal paths leave a consistent state? |
| [Q049](subjects/Q049.md) | tvOS · UIKit | A retained shelf button that was removed from the hierarchy still chooses an item. Can you make the same generation work for attached buttons only? |
| [Q050](subjects/Q050.md) | iOS · UIKit | Our row has two independently operated controls. The row’s accessibility configuration now hides the controls. Can you restore access to both controls? |
| [Q051](subjects/Q051.md) | iOS · UIKit | The panel can open over content that was already hidden from accessibility. Closing it should restore either original setting. Can you handle both starting states? |
| [Q052](subjects/Q052.md) | iOS · UIKit | Open the panel again before the first dismissal finishes and the old completion closes the new panel. Can you repair the callback and show what happens between completions? |
| [Q053](subjects/Q053.md) | iOS · UIKit | Our video inspector enables scrubbing over buffered content even when the player reports no seekable range. Can the inspector distinguish those states? |
| [Q054](subjects/Q054.md) | iOS · UIKit | The title is discoverable, yet our test would stay green if a purely decorative icon were also exposed. Strengthen the test for both elements after configuration. |
| [Q055](subjects/Q055.md) | iOS · UIKit | Our panel can close while dismissal is disabled. Can you make both entry points respect the current policy? |
| [Q056](subjects/Q056.md) | iOS · UIKit | A retained accessibility action for yesterday’s result can still change the reused result view. Can you fix that while keeping the new result actionable? |
| [Q057](subjects/Q057.md) | iOS · UIKit | This test keeps passing when tapping the selected speed calls the playback engine again. Exercise the button and count actual change deliveries across two taps. |
| [Q058](subjects/Q058.md) | iOS · UIKit | A loader calls its completion twice. After the first result is displayed, the second delivery can overwrite it. Can you enforce the intended one-result policy? |
| [Q059](subjects/Q059.md) | iOS · UIKit | Our choice-row test checks the selected state on a fresh cell. Would it catch a refresh that wipes traits supplied by another feature? Strengthen the test to cover a selection change. |
| [Q060](subjects/Q060.md) | iOS · UIKit | Choose delivery, then switch back to pickup. The old option still reports itself selected. Can you make every selection cue agree after switching twice? |
| [Q061](subjects/Q061.md) | iOS · UIKit | The inspector promises smooth playback whenever the buffer is full. How should it represent a full buffer when the player still says it may stall? |
| [Q062](subjects/Q062.md) | iOS · UIKit | The motion preference is correct at launch but changing it while the screen is visible doesn't update the view. Can you fix observation and show the change is delivered? |
| [Q063](subjects/Q063.md) | iOS · UIKit | Our text search is supposed to include overlapping matches. Looking for “ana” in “banana” misses a result. Can the rotor visit both positions in order? |
| [Q064](subjects/Q064.md) | tvOS · UIKit | The Details shortcut works but the ordinary Details action on our television screen is broken. Can you repair it and exercise the two entry points independently? |
| [Q065](subjects/Q065.md) | macOS · SwiftUI | An Off action retained by an old caption menu can clear selection after a menu reload. Can you repair and exercise the binding that the menu actually uses? |
| [Q066](subjects/Q066.md) | macOS · AppKit | Our test checks that the row is recognizable, but Save has disappeared from the ordinary action path before. Add proof that operates the visible control and observes its callback. |
| [Q067](subjects/Q067.md) | macOS · AppKit | CI only checks the table's size. It missed an invoice selection moving after a sort. Can you show how to catch that using equal titles and different identifiers? |
| [Q068](subjects/Q068.md) | macOS · AppKit | While saving is disabled, invoking the accessibility shortcut still changes the app. Can you repair the disabled path and preserve the enabled action? |
| [Q069](subjects/Q069.md) | iOS · UIKit | A decorative icon in our order row is appearing as a separate accessibility element. Can you exclude the icon while preserving the actionable content? |
| [Q070](subjects/Q070.md) | macOS · AppKit | The selected state is visible by color alone after this row refreshes. Can you keep a non-color label and its accessibility value synchronized on deselection too? |
| [Q071](subjects/Q071.md) | iOS · UIKit | The user edits a native field while validation is pending, without submitting again. The result still attaches to the edited value. Can you fix that case? |
| [Q072](subjects/Q072.md) | macOS · AppKit | Opening our modal passes the test, but it never exercises refusal by the original responder. How would you check the fallback used on completion? |
| [Q073](subjects/Q073.md) | iOS · UIKit | Our result exposes two named shortcuts. Invoking a single shortcut can deliver the operation twice. Can you verify the actual dispatch of both? |
| [Q074](subjects/Q074.md) | iOS · UIKit | Another controller replaces the player item directly during inspection. Can you ensure the old item's completion cannot publish results for the new one? |
| [Q075](subjects/Q075.md) | macOS · AppKit | Our save handler can synchronously call back into the form. One submission then invokes Save twice. Can you protect the actual dispatch path? |
| [Q076](subjects/Q076.md) | iOS · UIKit | A removed result stays alive after its owner drops it. Can you show whether the accessibility index or container is holding it and repair the removal path? |
| [Q077](subjects/Q077.md) | macOS · AppKit | When an editor closes after its original responder moved into another window, it tries to restore the wrong target. Can you exercise that move and use the eligible fallback? |
| [Q078](subjects/Q078.md) | macOS · AppKit | A disabled control can still toggle when its keyboard handler receives the event directly. Can you make disabled behavior agree across entry points? |
| [Q079](subjects/Q079.md) | macOS · SwiftUI | Writing the same value twice through our SwiftUI binding repeats the side effect. Can you preserve genuine value changes and suppress duplicates? |
| [Q080](subjects/Q080.md) | macOS · AppKit | A Mac outline refresh passes our smoke test even when selection moves to a different sibling. Add a test that exercises the refresh with a real selection. |
| [Q081](subjects/Q081.md) | macOS · AppKit | The row still says “Report” after selection. The test passes even when the selected flag never changes. Can you exercise select and deselect while preserving the row's other semantics? |
| [Q082](subjects/Q082.md) | macOS · AppKit | Our original responder is still attached but refuses first responder. Can the return path use the fallback without sending keyboard events? |
| [Q083](subjects/Q083.md) | tvOS · UIKit | Our motion test checks only that the animation did not run. How do we catch the regression where the status never changes for people who enable Reduce Motion? |
| [Q084](subjects/Q084.md) | iOS · UIKit | Our form succeeds on its second submission, but still offers the previous error’s recovery hint. Can you reset the stale state and preserve the successful result? |
| [Q085](subjects/Q085.md) | macOS · SwiftUI | Our SwiftUI preference policy requests animation even when Reduce Motion is enabled. Can you show both preference paths end in the same state while animation policy differs? |
| [Q086](subjects/Q086.md) | tvOS · UIKit | Each shelf needs a heading and independently operable item buttons. The container now absorbs them. Can you restore the structure without changing the data order? |
| [Q087](subjects/Q087.md) | iOS · UIKit | A disabled speed control still changes the playback rate through a direct selection request. Can you repair the command path and verify re-enabling it? |
| [Q088](subjects/Q088.md) | iOS · UIKit | The screen-change request fires before the closing animation finishes. Can it use the target that is eligible when dismissal actually completes? |
| [Q089](subjects/Q089.md) | tvOS · UIKit | Our snapshot-level check sees a Details title even when pressing the control no longer invokes Details. Strengthen this at the actual primary-action entry point. |
| [Q090](subjects/Q090.md) | macOS · SwiftUI | Cancellation of an earlier caption load clears the newer load’s state. Can you demonstrate overlapping requests and keep the newer one alive? |
| [Q091](subjects/Q091.md) | iOS · UIKit | The design tool and our checker disagree when a swatch is supplied in a linear color space. Can you make equivalent displayed colors yield comparable ratios? |
| [Q092](subjects/Q092.md) | iOS · UIKit | This timing assertion passes for every nonnegative duration. Can you make the check distinguish a reduced-motion transition from the ordinary transition? |
| [Q093](subjects/Q093.md) | tvOS · UIKit | On Apple TV, enabling Reduce Motion also prevents the updated status text from appearing. Can you separate the visible result from the optional animation? |
| [Q094](subjects/Q094.md) | macOS · AppKit | An outline data-source callback for a removed parent still returns children. Can you reject stale parent requests while current parents continue working? |
| [Q095](subjects/Q095.md) | macOS · AppKit | After a form action becomes disabled it remains in our owned Tab cycle. Can you rebuild the cycle in the supplied order with only eligible controls? |
| [Q096](subjects/Q096.md) | iOS · UIKit | Searching for a word after a family emoji highlights the wrong text. Can you return the intended substring without changing the user's selection? |
| [Q097](subjects/Q097.md) | iOS · UIKit | Our long shipping options stop after one line when someone chooses a large text size. Can you keep the full option readable without changing which option is selected? |
| [Q098](subjects/Q098.md) | macOS · SwiftUI | The native player has a forced subtitle option selected, but our full-caption menu reports Off. Can the menu distinguish an unrepresented selection from no selection? |
| [Q099](subjects/Q099.md) | tvOS · UIKit | The shelf remains on screen even when its items disappear as independent accessibility targets. Update the unit check to distinguish the two structures. |
| [Q100](subjects/Q100.md) | iOS · UIKit | An ordinary alternate language track shows up as audio description. Can you make inspection use evidence from the track while leaving playback untouched? |

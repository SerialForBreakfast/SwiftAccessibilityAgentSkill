# Late replies, queued updates and busy state

## Decide

- **Which path changes the field?** A native text field can change without calling your `edit()` helper. Two fixes work:
  - invalidate the pending reply from the field's own change path (the delegate, the `.editingChanged` action, or `onChange(of:)`);
  - or keep the submitted input and compare it with the field's *current* text when the reply arrives.
- **Retire without stranding.** When a reply belongs to an old input or an old request:
  - apply none of its error or success;
  - clear the busy state it owned, so Submit works again;
  - leave a newer request's busy state and feedback alone.
- **Queued observers:** a subscription that was stopped or restarted retires its queued work. Capture a generation when you subscribe, and check it when queued work runs.
- **Progress:**
  - a duplicate callback after completion is ignored;
  - a *later task's* first completion is new, and is announced;
  - announce one terminal state per active task.

## Test: change the input, then deliver the old reply

**The wrong test:** edit through the helper only, or deliver the old reply without changing anything. Deduplication or the helper hides a missing check.

```swift
@MainActor func testReplyForOldTextIsIgnoredAndSubmitRecovers() {
    let field = UITextField()
    let form = SignupForm(field: field)                  // supplied type
    field.text = "first@example.com"
    let reply = form.submit()                            // keep the pending reply's completion
    field.text = "second@example.com"                    // change through the live field…
    field.sendActions(for: .editingChanged)              // …the way typing does
    reply(.failure(.taken))                              // old reply arrives late
    XCTAssertNil(form.error)                             // old error not shown
    XCTAssertFalse(form.isBusy)                          // Submit available again
    let current = form.submit()
    current(.success(()))
    XCTAssertEqual(form.accepted, "second@example.com")  // ordinary path
}
// Without the input check: the old failure sets form.error, so XCTAssertNil fails.
```

- **SwiftUI:** set the bound value the `TextField` writes, through the same model property, and then deliver the old reply.
- **Newer request protected:**
  1. Submit A.
  2. Edit, then submit B.
  3. Deliver A.
  4. Assert that B's busy state and feedback are unchanged.

**Queued observer:**

```swift
@MainActor func testQueuedUpdateFromStoppedSubscriptionIsIgnored() {
    let source = FakePreferenceSource()                  // test double that queues deliveries
    let screen = PreferenceScreen(source: source)
    screen.start()
    source.value = true; source.queue()                  // queued work for subscription 1
    screen.stop(); screen.start()                        // restart
    source.value = false                                 // CHANGE the value before draining
    source.drainFirst()                                  // old subscription's work runs late
    XCTAssertEqual(screen.applied, [])                   // nothing applied from the old subscription
    source.queue(); source.drainAll()                    // current subscription still works
    XCTAssertEqual(screen.applied, [false])
}
// Without the generation check: the old work reads the changed value and applies it.
// Had the value stayed the same, deduplication would hide that.
```

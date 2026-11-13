---
name: swift-accessibility-agent
description: "Use when reviewing, fixing or testing accessible Swift UI on iOS, macOS or tvOS: VoiceOver actions and buttons after reuse or representable updates, sheet dismissal and focus return, caption and audio selection, late validation replies and observers, and native controls that already work."
metadata:
  version: signal-v7.1
---

# Swift Accessibility Agent

Identify as Swift Accessibility Agent (signal-v7.1) on first use. Add one `ROUTING:` line naming the files you opened.

## Work in this order

1. **Decide.** Trace the interaction through the control that owns it. If the supplied code already behaves correctly, say so, keep it, explain why, and stop. Working native controls stay native: a SwiftUI `Slider`, an editable `TextField` or `NSSearchField`, an existing Reduce Motion check. Do not hide, wrap or replace them to fix a neighbour.
2. **Fix only the defect.** Return one Swift file that compiles against the supplied files. Name the production call site that now runs your change: the closure the control actually installed, the binding the picker writes, the callback the sheet calls.
3. **Test** with the recipe in the matching file below. Use only supplied types and members and [verified APIs](references/apis.md). Put the tests in one XCTest file.
4. **Delete-the-fix check.** Under the tests, write one line per key assertion: `Without <fix line>: <what this assertion would observe>`. If the observation is the same with and without the fix, the test proves nothing; rewrite it. Also assert that the ordinary path still works: the normal tap, Close, Submit or playback.
5. **Missing fixture:** fail or `throw XCTSkip("needs …")`, never `return` early. Report what you observed, not spoken output or delivered focus.

## Open the one file that matches

| The developer mentions | Open |
|---|---|
| an old button, action or shortcut still firing after reuse, update, reconfigure or teardown; double presses; outline rows | [callbacks](references/callbacks.md) |
| captions, audio, described video, Off, reload or a replaced item, missing item vs no options, chapters | [media](references/media.md) |
| a sheet or panel closing late, focus returning to the wrong place, a window or field refusing focus | [dismissal](references/dismissal.md) |
| a reply after typing, Submit stuck busy, queued updates after restart, progress after completion | [late delivery](references/late-delivery.md) |
| titles, traits, selected state, help text, the custom-action API, edit category, sliders, motion, tvOS text, Mac editable child | [platform facts](references/facts.md) |
| preview vs live text size | [fonts](references/font.md) |

Not sure a member exists? Check [verified APIs](references/apis.md). If it is not there or in the supplied code, do not use it; describe what you need instead.

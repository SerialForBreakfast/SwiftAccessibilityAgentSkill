# Lifecycle difficulties and preserved first versions

## L01: A green Mac suite omitted first-responder eligibility

Classification: author implementation defect plus missing assertion, found by source
audit. Initial compile and27 positive methods passed. Apple makeFirstResponder
Discussion says to check acceptsFirstResponder. The first implementation checked
ownership, enabled and hidden state but omitted that check.

- [Exact original source](incidents/mac-original-no-responder-check.swift.txt)
- [First manifest](incidents/mac-first-manifest.json.txt)
- [First test source](incidents/mac-first-tests.swift.txt)
- Initial attempts: lifecycle-mac-compile-r1 and lifecycle-mac-positive-r1.
- Correction: check acceptsFirstResponder and add a controllable NSButton subclass
  in the test oracle, without assuming native defaults or keyboard preferences.
- New assertion: DesktopLifecycleTests/testRefusingOriginalUsesFallback.
- Original source regression: lifecycle-mac-original-responder-check-r1, expected
  rejection; exact diagnostic retained in results-index.json and raw archive.
- Revised suite:28 methods, lifecycle-mac-positive-r2.

This was not an unexpected failure of the initial suite. It demonstrates the
need to audit assertion scope. The draft Mac modal rubric accepts alternative
lifecycle ownership designs and explicitly distinguishes request success from
which object actually becomes first responder.

## L02: A draft TV ownership mutant still rejected foreign targets

Classification: negative-control design defect, found by source inspection before
negative execution. Removing the initial descendant guard left the ancestor walk's
root check intact. That mutant did not remove the contract being challenged.

- [Exact first mutant](incidents/tv-first-ownership-mutant.swift.txt)
- [First manifest](incidents/tv-first-manifest.json.txt)
- Revision2 removes ownership enforcement at both relevant guards; production
  source and positive test bytes stay unchanged.
- lifecycle-tv-foreigntarget-r1 rejects the revised mutant with
  TelevisionLifecycleTests/testForeignOriginalUsesFallback.
- Initial mutant was not executed; do not claim an observed survival or failure.

This is a controller diagnostic, not accessibility guidance or a new gold question.
The developer-facing modal question stays independent of mutation mechanics.

## Other boundaries worth preserving

Mac notifications come from NSWorkspace.shared.notificationCenter, whereas UIKit
preference notifications use NotificationCenter.default. Injected centers and reads
avoid altering user settings. Queued delivery needs both lifecycle ownership and
generation checks: checking only whether an observer exists can admit an older
callback after restart. The old-generation oracle checks read counts so deduplication
cannot hide this error. Production delivery uses a MainActor task; deterministic
tests drain an injected queue, not a timing sleep or a global scheduling claim.

Ten other negative fixtures deliberately remove selected guards. They are not
spontaneous model failures or evidence that one model is worse than another.

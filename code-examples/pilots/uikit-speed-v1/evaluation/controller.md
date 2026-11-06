# UPAIR-06C Controller Rubric

Draft, independent review pending. Send only prompt.json to the subject; keep the
implementation, tests, mutations, incident history and this rubric controller-only.

Score each criterion 0 wrong/missing, 1 partial, 2 satisfied:

1. Offers an ordinary operable control path, not only a rotor or special gesture.
2. Makes choices distinguishable and exposes current configured choice consistently.
3. Shares selection behavior between ordinary and any additional action paths.
4. Defines supported rates, disabled behavior and a safe invalid-input policy.
5. Avoids stale selected metadata and unintended duplicate side effects.
6. Keeps callbacks/ownership appropriate and does not claim that a requested rate
   necessarily equals the player's effective rate.
7. Provides focused unit tests and scopes their claims to configuration/callbacks.

Accept native pickers, segmented controls, menus or buttons with equivalent behavior.
Do not require our exact rates, wording, object layout, explicit traits or duplicate
suppression policy when another justified implementation meets the user's needs.
Native semantics may already be appropriate; absence of a custom value is not by
itself a defect. Tests must not impose an undocumented spoken string.

Critical errors: primary speed operation available only through a special shortcut,
invalid input causes unsafe state, disabled control path performs an unauthorized
change, or unit tests are presented as proof of real playback/assistive input.
Evaluate declared behavior rather than exact source matching. Do not expose these
criteria or exact repair snippets in subject inputs. Zero model runs performed.

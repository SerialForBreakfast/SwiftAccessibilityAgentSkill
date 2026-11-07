Target tvOS26, SwiftUI with UIKit.

For the same SwiftUI native report card, preserve ordinary Open and Details controls. Add one optional Details accessibility shortcut through the same callback. Updates change the stable item ID and handler; old shortcuts or detached native controls must not invoke a rebound item. Respect externally disabled controls, replace rather than accumulate handlers, and stop dispatch on dismantle. Retained actions must not retain the coordinator or card.

Provide complete code and focused unit tests; no UI automation.

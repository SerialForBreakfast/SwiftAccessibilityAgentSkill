# Observable Media Wiring

Keep ordinary player controls and use the same player/item for supplementary
selection controls. A binding must reach the real selection operation; an isolated
policy test or synthetic selected value does not establish that wiring.

Distinguish a native side effect from an app-observable state update. Ensure the UI
can reflect the application's own selection changes using an appropriate observable
mechanism. A getter can read external changes without automatically notifying the
view. State whether external item/selection changes require an explicit reload.

Represent missing item, loading, absent options and failure according to the loader
contract; preserve existing choices during errors. Compile actual modifier/control
composition when useful. Store units and source compilation establish their named
contracts, not generated accessibility semantics, rendered captions or delivered
focus. Do not require a particular notification count when state remains correct.

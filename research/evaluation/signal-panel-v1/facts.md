# When an implementation depends on a platform distinction

- **UIKit button:** an automation identifier identifies an element to a test. It does not configure a visible title. Check the displayed title for the relevant state when the request concerns text on screen.
- **State across updates:** apply both inputs in succession to the same control. Check visible wording, accessibility value and selected state separately when the product uses all three; one correct property does not establish the others.
- **UIKit text-edit custom actions:** distinguish the SDK's UIAccessibilityCustomAction.editCategory constant from an inferred enum case. Preserve the uncategorized path when no category is requested.
- **AppKit rows:** a row role and independently exposed child controls can coexist. Inspect the parent's role and the children people operate before flattening the row.
- **tvOS:** Apple's WWDC26 session 221 describes system Larger Text for tvOS 27. A target that still runs on tvOS 26 can preserve readable layout and reachable controls there without promising the system preference. Gate specific new APIs by their own declarations.

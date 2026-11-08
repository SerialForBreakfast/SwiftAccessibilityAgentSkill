"""Hand-maintained case classification for the failure inventory.

Workstream = the developer decision the case exercises (W1-W9). Tags are failure-taxonomy families
from CurrentStatusReview.md §5 (A-H) plus 'integration' (proposed change doesn't fit the owner) where
reviewers recorded it. Edit here; build.py refuses observations for unclassified cases.
"""
TARGET_MODEL = "claude-haiku-5-5"
MODEL_TIER = {"claude-haiku-5-5": "target (low effort)", "gemini-3.8-flash-low": "peer",
              "gemini-4-argon-high": "stronger", "unmapped": "unknown (mapping not opened)"}

WORKSTREAMS = {
    "W1": "Ordinary actions and containers",
    "W2": "Reuse and stale state",
    "W3": "Dismissal, focus and restoration",
    "W4": "Text and layout",
    "W5": "Rotor, structure and ordinary navigation",
    "W6": "Alternative input and preferences",
    "W7": "Media and asynchronous ownership",
    "W8": "Evidence and restraint (no-change, claim limits)",
    "W9": "Tests that can expose the defect",
}

EXCLUDED = [
    "local small models (Qwen v1/v2, Llama compact-b, Gemma local-dev5): diagnostic only, per AGENTS.md",
    "AGY native re-grades of dev.1/dev.2 answers (same answers as S5; not double counted)",
    "Flash evidence questions EV01-06 (aggregate 4/6 only, no per-question mapping)",
    "disputed checkout/deletion answers (model mapping not opened; S9 covers the checkout type-checks)",
]


def c(title, platform, framework, workstream, *tags):
    return dict(title=title, platform=platform, framework=framework, workstream=workstream, tags=list(tags))


CASES = {
    # OS26 gold and exploratory prompts (GoldPrompts.md, evals/os26/expansion-1)
    "GP26-01": c("Settings row: switch and Help stay independently usable", "iOS", "UIKit", "W1", "A"),
    "GP26-02": c("Reused cell shows current customer and status", "iOS", "UIKit", "W2"),
    "GP26-03": c("Checkout total wraps at large text; Pay appearance preserved", "iOS", "UIKit", "W4", "C", "integration"),
    "GP26-04": c("Delete without requiring a swipe", "iPadOS", "SwiftUI", "W6", "E"),
    "GP26-05": c("tvOS tile navigation keeps controls", "tvOS", "SwiftUI", "W1"),
    "GP26-06": c("Already-correct Toggle needs no change", "iOS", "SwiftUI", "W8", "D"),
    "GP26-07": c("Return focus to the current payment origin", "iOS", "UIKit", "W3", "B", "F"),
    "GP26-08": c("Custom popup contains focus and restores background state", "iOS", "UIKit", "W3", "B"),
    "GP26-09": c("Custom volume knob is adjustable", "iOS", "UIKit", "W1"),
    "GP26-10": c("Download progress without repeated announcements", "iOS", "UIKit", "W7"),
    "GP26-11": c("Already-correct native Slider needs no change", "iOS", "SwiftUI", "W8", "D"),
    "GP26-12": c("Existing reduced-motion transition needs no change", "iOS", "SwiftUI", "W8", "D"),
    "EV01": c("Screenshot does not prove VoiceOver activation", "any", "evidence", "W8"),
    "EV02": c("12 clean checks don't justify 'fully accessible'", "any", "evidence", "W8"),
    "EV03": c("Unavailable docs can't establish exactly-once activation", "any", "evidence", "W8"),
    "EV04": c("Forum post can't justify removing a payment workaround", "any", "evidence", "W8"),
    "EV05": c("Simulator 26.5 doesn't establish 26.0 and later", "any", "evidence", "W8"),
    "EV06": c("Direct handler test doesn't prove keyboard/VoiceOver activation", "any", "evidence", "W8", "G"),
    "IOS-MEDIA-OWNERSHIP-R1": c("Late media callback after external item replacement", "iOS", "UIKit", "W7", "H", "G"),
    "IOS-VALIDATION-OWNERSHIP-R1": c("Validation result ignores newer submissions", "iOS", "UIKit", "W7"),
    # dev.5/dev.7 comparison set (research/evaluation/dev7-comparison)
    "ios-uikit-actions": c("Shortcut added; ordinary Open/Delete stay reachable", "iOS", "UIKit", "W1", "A"),
    "ios-uikit-state": c("Repeated updates replace stale status/help; current reply only", "iOS", "UIKit", "W2", "F"),
    "ios-uikit-text": c("Scalable checkout text with Pay identity preserved", "iOS", "UIKit", "W4", "C", "integration"),
    "ios-swiftui-semantics": c("Native switch: change only for a demonstrated defect", "iOS", "SwiftUI", "W8", "D"),
    "ios-swiftui-lifecycle": c("Restore to the current eligible origin at completion", "iOS", "SwiftUI", "W3", "B", "F"),
    "ios-swiftui-media": c("Metadata states distinct; reject stale completions", "iOS", "SwiftUI", "W7", "H"),
    "macos-appkit-actions": c("Shortcut added; ordinary Open/Delete stay reachable", "macOS", "AppKit", "W1", "A"),
    "macos-appkit-structure": c("Group descriptions without merging Open and Details", "macOS", "AppKit", "W5", "A"),
    "macos-appkit-testing": c("Map claims to actual assertions; keep first diagnostics", "macOS", "AppKit", "W9", "G"),
    "macos-swiftui-state": c("Repeated updates replace stale status/help; current reply only", "macOS", "SwiftUI", "W2", "F"),
    "macos-swiftui-text": c("Scalable checkout text with Pay identity preserved", "macOS", "SwiftUI", "W4", "C"),
    "macos-swiftui-lifecycle": c("Restore to the current eligible origin at completion", "macOS", "SwiftUI", "W3", "B", "F"),
    "tvos-uikit-state": c("Repeated updates replace stale status/help; current reply only", "tvOS", "UIKit", "W2", "F"),
    "tvos-uikit-media": c("Metadata states distinct; reject stale completions", "tvOS", "UIKit", "W7", "H"),
    "tvos-uikit-lifecycle": c("Restore to the current eligible origin at completion", "tvOS", "UIKit", "W3", "B", "F"),
    "tvos-swiftui-actions": c("Shortcut added; ordinary Select stays reachable", "tvOS", "SwiftUI", "W1", "A"),
    "tvos-swiftui-structure": c("Group descriptions without merging Open and Details", "tvOS", "SwiftUI", "W5", "A"),
    "tvos-swiftui-testing": c("Map claims to actual assertions; keep first diagnostics", "tvOS", "SwiftUI", "W9", "G"),
    "ios-uikit-no-change": c("Working standard control needs no replacement", "iOS", "UIKit", "W8", "D"),
    "ios-swiftui-no-change": c("Working standard control needs no replacement", "iOS", "SwiftUI", "W8", "D"),
    "macos-appkit-no-change": c("Working standard control needs no replacement", "macOS", "AppKit", "W8", "D"),
    "mixed-macos-owner": c("Condition advice on the owning view/coordinator layer", "macOS", "mixed", "W1"),
    "ios-missing-reference": c("Don't claim an unread reference's contract", "iOS", "any", "W8", "E"),
    "tvos-version-boundary": c("Separate SDK, deployment and runtime evidence", "tvOS", "any", "W8", "E"),
    # rc.1 one-function tasks (evals/rc1/grader/tasks.py)
    "rc1/checkout-font": c("Supplied text-size setting owns the label font", "iOS", "UIKit", "W4", "C"),
    "rc1/switch-preservation": c("Rename returns the original switch unchanged", "iOS", "UIKit", "W1"),
    "rc1/toggle-binding": c("Guarded toggle binding forwards changed writes once", "iOS", "SwiftUI", "W2"),
    "rc1/adjustable-volume": c("Adjustable volume steps within bounds", "iOS", "SwiftUI", "W1"),
    "rc1/ordinary-buttons": c("Both buttons dispatch to the current owner", "macOS", "AppKit", "W1", "A"),
    "rc1/status-change": c("Publish new status before notifying, once per change", "macOS", "AppKit", "W2"),
    "rc1/landmark-identity": c("Landmarks keep order and stable IDs", "macOS", "SwiftUI", "W5"),
    "rc1/checkout-layout": c("Stack checkout at accessibility sizes", "macOS", "SwiftUI", "W4", "C"),
    "rc1/restoration-eligibility": c("Restore to an eligible enabled opener, else fallback", "tvOS", "UIKit", "W3", "F"),
    "rc1/row-traits": c("Selection preserves unrelated traits", "tvOS", "UIKit", "W2"),
    "rc1/motion-policy": c("Reduce Motion suppresses only the optional effect", "tvOS", "SwiftUI", "W6"),
    "rc1/stale-media-reply": c("Media reply must match current item and request", "tvOS", "SwiftUI", "W7", "H"),
}

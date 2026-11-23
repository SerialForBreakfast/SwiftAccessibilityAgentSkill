"""Qualify the v7.2 recipe tests natively.

The recipe tests and the ReturnCoordinator are copied verbatim from the skill cards.

For every platform:
- the fixed subjects pass every test;
- each defect makes its recipe test fail, while that recipe's "wrong test" still passes;
- on macOS, the AppKit row getters added to apis.md compile with the stated types.

  python3 -B research/evaluation/signal-panel-v7-2/qualify/qualify.py [--platforms iOS,macOS,tvOS]
  python3 -B research/evaluation/signal-panel-v7-2/qualify/qualify.py --static   # no Xcode needed

--static checks that every recipe block the native run copies is byte-identical to v7.1,
so v7.1's native receipt still describes them; it writes nothing.

Writes receipts under evals/results/signal-v7-2-offline/qualify-*/; never overwrites a batch.
"""
import json, re, subprocess, sys, tempfile
from pathlib import Path

D = Path(__file__).resolve().parent
SKILL = D.parent / "skill/references"
PRIOR = D.parents[1] / "signal-panel-v7-1/skill/references"
ROOT = D.parents[3]
OUT = ROOT / "evals/results/signal-v7-2-offline"
SIM = {"iOS": "SwiftAccessibility-OS26-Unit-iOS", "tvOS": "SwiftAccessibility-OS26-Unit-tvOS"}
GUARD = {"callbacks": "#if canImport(UIKit)", "late": "#if canImport(UIKit)", "media": "#if !os(tvOS)"}
PLATFORMS = {"callbacks": {"iOS", "tvOS"}, "late": {"iOS", "tvOS"}, "media": {"iOS", "macOS"},
             "observer": {"iOS", "macOS", "tvOS"}, "dismissal": {"iOS", "macOS", "tvOS"}}
RECIPE = {"callbacks": "testOldCallbackIgnoredAfterReconfigure", "media": "testChoosingCaptionsWritesThePlayingItem",
          "dismissal": "testLateFirstDismissalDoesNotRestoreSecond", "late": "testReplyForOldTextIsIgnoredAndSubmitRecovers",
          "observer": "testQueuedUpdateFromStoppedSubscriptionIsIgnored"}


def blocks(card, root=SKILL):
    return re.findall(r"```swift\n(.*?)```", (root / card).read_text(), re.S)


def pick(card, needle, root=SKILL):
    found = [b for b in blocks(card, root) if needle in b]
    assert len(found) == 1, (card, needle, len(found))
    return found[0]


def test_function(card, name, root=SKILL):
    block = pick(card, "func " + name, root)
    start = block.index("@MainActor func " + name)
    body, depth, i = block[start:], 0, 0
    for i, ch in enumerate(body):
        depth += ch == "{"
        depth -= ch == "}"
        if ch == "}" and depth == 0:
            break
    return body[: i + 1]


def sources(defect):
    subjects = (D / "Subjects.swift").read_text()
    lines = []
    for line in subjects.splitlines():
        if f"// FIX:{defect}" in line:
            if defect == "media":
                continue                      # drop the item write: picker-only selection
            continue                          # drop the guard
        lines.append(line)
    coordinator = pick("dismissal.md", "final class ReturnCoordinator")
    if defect == "dismissal":
        assert coordinator.count(", self.active == token") == 1
        coordinator = coordinator.replace(", self.active == token", "")
    head = "import Foundation\n"
    return "\n".join(lines) + "\n", head + coordinator.replace("@MainActor final class", "@MainActor public final class")
    # (ReturnCoordinator members are used through @testable import.)


def tests():
    media_helper = pick("media.md", "func makeMediaItem")
    parts = ["import AVFoundation\nimport SwiftUI\nimport XCTest\n#if canImport(UIKit)\nimport UIKit\n#endif\n@testable import Q\n",
             "#if !os(tvOS)\n" + media_helper.replace("import AVFoundation\n", "") + "#endif\n",
             "@MainActor final class RecipeTests: XCTestCase {"]
    for key, name in RECIPE.items():
        card = {"callbacks": "callbacks.md", "media": "media.md", "dismissal": "dismissal.md",
                "late": "late-delivery.md", "observer": "late-delivery.md"}[key]
        fn = test_function(card, name)
        parts.append(f"{GUARD[key]}\n{fn}\n#endif" if key in GUARD else fn)
    parts.append("}\n")
    return "\n".join(parts)


def probe():
    lines = [l.split("//")[0].strip() for l in pick("apis.md", "row.isAccessibilityElement()").splitlines()
             if l.startswith("row.")]
    assert len(lines) == 2, lines
    calls = [c.strip() for l in lines for c in l.split(";") if c.strip()]
    return ("#if os(macOS)\nimport AppKit\nimport XCTest\n\n"
            "@MainActor final class ApiProbe: XCTestCase {\n"
            "    func testAppKitRowGetters() {\n"
            "        let row = NSTableRowView()\n"
            + "".join(f"        _ = {c}\n" for c in calls) +    # the card's calls, verbatim
            "        let _: Bool = row.isAccessibilityElement()\n"
            "        let _: NSAccessibility.Role? = row.accessibilityRole()\n"
            "        let _: Bool = row.isAccessibilitySelected()\n"
            "        let _: Bool = row.isAccessibilityExpanded()\n"
            "        let _: [Any]? = row.accessibilityChildren()   // the card's stated type\n"
            "    }\n}\n#endif\n")


def static():
    cards = {"callbacks": "callbacks.md", "media": "media.md", "dismissal": "dismissal.md",
             "late": "late-delivery.md", "observer": "late-delivery.md"}
    same = {name: test_function(cards[k], name) == test_function(cards[k], name, PRIOR) for k, name in RECIPE.items()}
    same["ReturnCoordinator"] = pick("dismissal.md", "final class ReturnCoordinator") == \
        pick("dismissal.md", "final class ReturnCoordinator", PRIOR)
    same["makeMediaItem"] = pick("media.md", "func makeMediaItem") == pick("media.md", "func makeMediaItem", PRIOR)
    for name in ("Subjects.swift", "WrongTests.swift"):
        same[name] = (D / name).read_bytes() == (D.parents[1] / "signal-panel-v7-1/qualify" / name).read_bytes()
    print(probe())
    for name, ok in same.items():
        print(name, "identical to v7.1" if ok else "CHANGED")
    sys.exit(0 if all(same.values()) else 1)


def run(platform, mode, batch):
    w = batch / platform / mode
    (w / "Sources/Q").mkdir(parents=True)
    (w / "Tests/QTests").mkdir(parents=True)
    subj, coord = sources(mode)
    (w / "Sources/Q/Subjects.swift").write_text(subj)
    (w / "Sources/Q/Coordinator.swift").write_text(coord)
    (w / "Tests/QTests/RecipeTests.swift").write_text(tests())
    (w / "Tests/QTests/WrongTests.swift").write_bytes((D / "WrongTests.swift").read_bytes())
    (w / "Tests/QTests/ApiProbe.swift").write_text(probe())
    (w / "Package.swift").write_text('// swift-tools-version: 5.9\nimport PackageDescription\nlet package = Package(name:"Q", platforms:[.macOS("26.0"),.iOS("26.0"),.tvOS("26.0")], products:[.library(name:"Q",targets:["Q"])], targets:[.target(name:"Q"),.testTarget(name:"QTests", dependencies:["Q"])])\n')
    if platform == "macOS":
        dest = "platform=macOS,arch=arm64"
    else:
        devs = json.loads(subprocess.check_output(["xcrun", "simctl", "list", "devices", "booted", "-j"]))["devices"]
        dest = "id=" + next(d["udid"] for runtime in devs.values() for d in runtime if d["name"] == SIM[platform])
    args = ["xcodebuild", "test", "-scheme", "Q", "-destination", dest, "-derivedDataPath", str(w / "dd"),
            "-parallel-testing-enabled", "NO", "-collect-test-diagnostics", "never", "CODE_SIGNING_ALLOWED=NO"]
    with (w / "native.log").open("w") as log:
        code = subprocess.run(args, cwd=w, stdout=log, stderr=subprocess.STDOUT, timeout=600).returncode
    text = (w / "native.log").read_text(errors="replace")
    status = dict(re.findall(r"Test Case '-\[QTests\.\w+ (test\w+)\]' (passed|failed|skipped)", text))
    errors = [l for l in text.splitlines() if ": error:" in l and "Tests" not in l.split(":")[0][-40:]][:8]
    return code, status, errors


def expected(platform, mode):
    want = {}
    for key, name in RECIPE.items():
        if platform not in PLATFORMS[key]:
            continue
        want[name] = "failed" if key == mode else "passed"
        want[f"testWrong_{key}"] = "passed"
    if platform == "macOS":
        want["testAppKitRowGetters"] = "passed"
    return want


def main():
    if "--static" in sys.argv:
        static()
    platforms = sys.argv[sys.argv.index("--platforms") + 1].split(",") if "--platforms" in sys.argv else ["macOS", "iOS", "tvOS"]
    OUT.mkdir(parents=True, exist_ok=True)
    batch = Path(tempfile.mkdtemp(prefix="qualify-", dir=OUT))
    rows, ok = [], True
    for platform in platforms:
        for mode in ["fixed"] + [k for k in RECIPE if platform in PLATFORMS[k]]:
            code, status, errors = run(platform, mode, batch)
            want = expected(platform, mode)
            good = all(status.get(n) == v for n, v in want.items())
            ok &= good
            rows.append(dict(platform=platform, mode=mode, exit=code, ok=good, status=status, expected=want, errors=errors))
            print(platform, mode, "OK" if good else "MISMATCH", {n: status.get(n) for n, v in want.items() if status.get(n) != v} or "", errors[:2], flush=True)
    (batch / "receipt.json").write_text(json.dumps(rows, indent=1))
    print(batch.relative_to(ROOT), "PASS" if ok else "FAIL")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()

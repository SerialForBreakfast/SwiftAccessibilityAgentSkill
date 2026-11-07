"""Explicit offline routing; reads public guidance, never evaluation controllers."""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
PARENT = HERE.with_name("0.3.0-dev.5")
MEDIA = HERE.with_name("0.3.0-dev.6")
CARDS = ROOT / "research/evaluation/milestone-package-v2/reference-cards"
SCOPED = {("macOS", "state"): "macos-values", ("macOS", "text"): "macos-text-sizing",
          ("macOS", "lifecycle"): "macos-focus-requests", ("tvOS", "actions"): "tvos-actions",
          ("tvOS", "structure"): "tvos-children"}
NOTES = {("SwiftUI", "lifecycle"): "swiftui-dismissal", ("UIKit", "lifecycle"): "uikit-dismissal",
         ("AppKit", "structure"): "appkit-grouping", ("UIKit", "text"): "checkout-uikit",
         ("SwiftUI", "text", "macOS"): "checkout-macos"}


def select(platform, framework, topic, *, level="guidance", owner=None, concern="overview", budget=12000):
    if level not in ("guidance", "example", "contract") or type(budget) is not int or budget < 1:
        raise ValueError("Invalid disclosure level or budget")
    if framework == "mixed":
        if not owner:
            return "needs-owner", []
        framework = owner
    rows = json.loads((PARENT / "routes.json").read_text())["routes"]
    row = next((r for r in rows if (r["platform"], r["framework"], r["topic"]) ==
                (platform, framework, topic)), None)
    if not row:
        return "unsupported", []
    note = NOTES.get((framework, topic, platform), NOTES.get((framework, topic)))
    if topic in ("state", "testing", "media"):
        note = {"state": "reuse", "testing": "testing", "media": "inspect-media"}[topic]
    files = [HERE / "references" / (note + ".md") if note else PARENT / row["note"]]
    media = framework == "SwiftUI" and topic == "media"
    if media and concern != "overview":
        if concern not in ("ownership", "wiring", "selection"):
            return "unsupported", []
        files[0] = MEDIA / "references" / ("media-" + concern + ".md")
    if media:
        files.append(MEDIA / "references" / ("sdk-" + platform.lower() + ".md"))
    elif framework == "SwiftUI" and (platform, topic) in SCOPED:
        files.append(CARDS / (SCOPED[platform, topic] + ".md"))
    elif topic != "testing":
        if not row["guideline"]:
            return "requires-primary-source", []
        files.append(ROOT / row["guideline"])
    if level != "guidance":
        if media:
            base = ROOT / "code-examples/swiftui" / ("media-" + platform.lower() + "-v2")
            files.append(base / "Sources/MediaSelection.swift")
            if level == "contract":
                files += [base / "manifest.json", *sorted((base / "Tests").glob("*.swift"))]
        elif row.get("exampleSource"):
            files.append(ROOT / row["exampleSource"])
            if level == "contract":
                files.append(ROOT / row["exampleManifest"])
        else:
            return "example-unavailable", []
    if sum(p.stat().st_size for p in files) > budget:
        return "budget-exceeded", []
    return "selected", [{"path": str(p.relative_to(ROOT)), "content": p.read_text()} for p in files]

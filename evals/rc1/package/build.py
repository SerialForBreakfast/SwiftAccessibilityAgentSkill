"""Produce an installable, deterministic archive. No research path is required after extraction."""
from hashlib import sha256
from pathlib import Path
import argparse
import json
import re
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
DEV = ROOT/"research/evaluation/failure-driven/candidates"
NOTES = {5:"semantics actions structure text",6:"media-selection media-ownership media-wiring",
         7:"reuse checkout-macos inspect-media testing",
         8:"uikit-ordinary-actions uikit-rebind appkit-actions appkit-structure swiftui-dismissal uikit-dismissal checkout-uikit"}
# Select an existing, manifest-pinned example rather than exposing grading fixtures.
EXAMPLES = [
    ("ios-uikit","iOS UIKit: reusable choice labels","pilots/uikit-choice-v1","choice"),
    ("ios-swiftui","iOS SwiftUI: native controls and adjustable state","swiftui/ios-v1","semantics"),
    ("macos-appkit","AppKit: ordinary actions and status notifications","platforms/macos-appkit-v1","actions"),
    ("macos-swiftui","macOS SwiftUI: preferences and layout","swiftui/macos-v1","preferences"),
    ("tvos-uikit","tvOS UIKit: ordinary actions and focus candidates","platforms/tvos-uikit-v1","actions"),
    ("tvos-swiftui","tvOS SwiftUI: list identity and rotor landmarks","swiftui/tvos-v1","documents"),
]
NAMES = ["Choice","Semantics","DesktopActions","Preferences","TelevisionActions","Documents"]


def contents():
    files = {"SKILL.md": (HERE/"ENTRYPOINT.md").read_bytes(),
             "agents/openai.yaml": b'interface:\n  display_name: "Swift Accessibility Agent"\n  short_description: "Source-backed Apple UI accessibility guidance"\n  default_prompt: "Use $swift-accessibility-agent to review this Apple UI."\n'}
    for rev, names in NOTES.items():
        directory = DEV/f"0.3.0-dev.{rev}"/"references"
        for name in names.split():
            source = (directory/"tasks" if rev==5 else directory)/(name+".md")
            files["references/"+source.name] = source.read_bytes()
    source_index = ["# Apple sources and scoped declarations",""]
    examples = ["# Examples on demand","", "Read one card for the target and task. These are companion examples, not prescriptions for a particular architecture.",""]
    for (key,title,package,claim_id),stem in zip(EXAMPLES,NAMES,strict=True):
        directory = ROOT/"code-examples"/package
        m = json.loads((directory/"manifest.json").read_bytes())
        sources = [r for r in m["files"] if r["path"].startswith("Sources/") and stem.lower() in r["path"].lower()]
        assert len(sources)==1,(key,sources)
        s = sources[0]; swift = (directory/s["path"]).read_bytes()
        assert sha256(swift).hexdigest()==s["sha256"]
        refs = [r for r in m["claims"] if r["id"]==claim_id] or m["claims"]
        links = "\n".join("- ["+r["section"]+"]("+r["url"]+")" for r in refs)
        source_index += ["## "+title,links,""]
        card = f"# {title}\n\nDeployment {m['deploymentTarget']}; recorded platform family {m['platform']}, runtime major {m['runtimeMajor']}. Source revision {m['revision']}, SHA-256 {s['sha256']}.\n\n{m['limitations']}\n\n{links}\n\n```swift\n"+swift.decode().rstrip()+"\n```\n"
        files[f"references/examples/{key}.md"] = card.encode()
        examples.append(f"- [{title}](examples/{key}.md)")
    directory = ROOT/"research/evaluation/milestone-package-v2/reference-cards"
    for card in sorted(directory.glob("*.md")):
        files["references/sdk/"+card.name] = card.read_bytes()
        source_index.append(f"- [{card.stem}](sdk/{card.name})")
    files["references/examples.md"] = ("\n".join(examples)+"\n").encode()
    files["references/sources.md"] = ("\n".join(source_index)+"\n").encode()
    for name,data in files.items():
        for target in re.findall(r'\]\(([^)]+)\)',data.decode()):
            if not target.startswith(("https://","http://","#")):
                assert str(Path(name).parent/target) in files,(name,target)
    return files


def build(out):
    with ZipFile(out,"w") as archive:
        for name,data in sorted(contents().items()):
            info = ZipInfo("swift-accessibility-agent/"+name,(1980,1,1,0,0,0))
            info.external_attr = 0o100644 << 16
            archive.writestr(info,data,compress_type=ZIP_DEFLATED)
    print(out,sha256(out.read_bytes()).hexdigest())


if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("output",type=Path)
    args=parser.parse_args()
    build(args.output)

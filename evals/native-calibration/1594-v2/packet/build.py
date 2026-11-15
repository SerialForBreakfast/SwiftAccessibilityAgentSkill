"""Build the held, three-case macOS development panel. Does not execute Swift."""
import hashlib
import io
import json
import sys
import zipfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
CAL = HERE.parent
ROOT = CAL.parents[2]
OUT = ROOT / "evals/results/1594-v2-held"
SHA = lambda data: hashlib.sha256(data).hexdigest()
def encode(obj):
    return (json.dumps(obj, indent=2, sort_keys=True) + "\n").encode()

def pack(files):
    files = dict(files, **{"SHA256.json": encode({n: SHA(b) for n,b in files.items()})})
    stream = io.BytesIO()
    with zipfile.ZipFile(stream, "w") as z:
        for name, data in sorted(files.items()):
            z.writestr(zipfile.ZipInfo(name), data, compress_type=zipfile.ZIP_DEFLATED)
    with zipfile.ZipFile(stream) as z:
        assert len(z.namelist()) == len(files) and all(z.read(n) == b for n,b in files.items())
    return stream.getvalue()

def original(package, rel, prefix):
    data = (ROOT/"code-examples/platforms"/package/rel).read_bytes()
    if not SHA(data).startswith(prefix):
        raise ValueError("Frozen source changed: " + rel)
    return data

questions = json.loads((CAL/"subject/questions.json").read_bytes())
assert set(questions) == {"Q070", "Q082-A", "Q082-B"}
p = "macos-closure-v1"
shared = {f"Sources/{name}.swift":original(p,f"Sources/{name}.swift",pin)
          for name,pin in [("AsyncOwnership","507d9c2201d2"),("DesktopText","87562de39765")]}
state = "Sources/StateContracts.swift"
life = "Sources/DesktopLifecycle.swift"
p2 = "macos-lifecycle-v1"
state_ref = original(p,state,"e98fe859e823")
state_seed = original(p,"NegativeFixtures/state_text.swift","f5ba6dd908dd")
life_ref = original(p2,life,"1d79aece2dae")
life_seed = original(p2,"NegativeFixtures/OriginalNoResponderCheck.swift","4515909a59b8")
# Contrast rejection after dispatch with failure of eligibility before dispatch.
needle = b"return request(target)"
assert life_ref.count(needle) == 1
reject_seed = life_ref.replace(b"primary = nil; fallback = nil\n        guard let target",
                               b"let alternate = fallback\n        primary = nil; fallback = nil\n        guard let target")
assert reject_seed != life_ref
reject_seed = reject_seed.replace(needle,b"if request(target) { return true }\n        guard let alternate, alternate !== target, eligible(alternate) else { return false }\n        return request(alternate)")
pkg = b'''// swift-tools-version: 5.9
import PackageDescription
let package = Package(name: "AccessibilityExamples", platforms: [.macOS("26.0")],
    targets: [.target(name: "AccessibilityExamples", path: "Sources"),
              .testTarget(name: "Checks", dependencies: ["AccessibilityExamples"], path: "Tests")])
'''
starter = b'import XCTest\n@testable import AccessibilityExamples\n'
control = {n:(CAL/n).read_bytes() for n in ["README.md","controller/grade.py","controller/check_contract.py","controller/evidence.json","subject/questions.json"]}
subject = {}
for case, prompt in questions.items():
    files = dict(shared, **{state:state_seed}) if case=="Q070" else {life:life_seed}
    subject[case+".zip"] = pack(dict(files, **{"Package.swift":pkg,"Tests/SubmittedTests.swift":starter,
        "QUESTION.md":(prompt+"\n\nReturn the changed Swift files (or say which production files stay unchanged), your focused XCTest, and a brief explanation.\n").encode()}))
    ref, defect = (state_ref,state_seed) if case=="Q070" else (life_ref,life_seed if case=="Q082-A" else reject_seed)
    path = state if case=="Q070" else life
    control[f"{case}/reference/{path}"] = ref
    control[f"{case}/defect/{path}"] = defect
control["INSTRUCTIONS.md"] = (HERE/"README.md").read_bytes()
subject_zip = pack(subject)
control["plan.json"] = encode(dict(status="held",dataset="known development cases",platform="macOS AppKit",caseHashes={k:SHA(v) for k,v in subject.items()},subjectArchiveSHA256=SHA(subject_zip),proposedArms=["unaided","unchanged skill (pin archive before authorization)"],pairedFirstAnswers=6,authorizedAttempts=0))
outputs={"subjects.zip":subject_zip,"controller.zip":pack(control)}
seals=encode({n:SHA(b) for n,b in outputs.items()})
if "--check" in sys.argv:
    assert all((OUT/n).read_bytes()==b for n,b in dict(outputs,**{"seals.json":seals}).items())
else:
    OUT.mkdir(parents=True,exist_ok=True)
    for n,b in dict(outputs,**{"seals.json":seals}).items():
        with (OUT/n).open("xb") as f:f.write(b)
print(seals.decode().strip())

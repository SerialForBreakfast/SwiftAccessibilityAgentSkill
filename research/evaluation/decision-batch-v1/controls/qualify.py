"""Local source calibration and SDK checks. No model provider or external runner."""
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
out = ROOT / "evals/results" / sys.argv[1]
assert out.parent == ROOT / "evals/results"
out.mkdir(exist_ok=False)
env = {**os.environ, "TMPDIR": str(out), "CLANG_MODULE_CACHE_PATH": str(out/"cache")}
def cmd(*args):
    return subprocess.run(args, capture_output=True, text=True, cwd=out, env=env)
def version(*args):
    p = cmd(*args)
    p.check_returncode()
    return p.stdout.strip()
results = {}
def check(name, source, sdk, target, run=False):
    path = out / (name+".swift")
    path.write_text(source)
    args = ["xcrun","--sdk",sdk,"swiftc","-module-cache-path",str(out/"cache"),
            "-sdk",version("xcrun","--sdk",sdk,"--show-sdk-path"),"-target",target,str(path)]
    p = cmd(*(args + (["-parse-as-library","-o",str(out/name)] if run else ["-typecheck"])))
    (out/(name+".log")).write_text(p.stdout+p.stderr)
    results[name] = {"sourceSHA256":hashlib.sha256(source.encode()).hexdigest(),
                     "target":target,"sdk":version("xcrun","--sdk",sdk,"--show-sdk-build-version"),
                     "compiled":p.returncode==0}
    if run and not p.returncode:
        p = cmd(str(out/name))
        results[name]["observation"] = p.stdout.strip()
        (out/(name+".runtime.log")).write_text(p.stdout+p.stderr)
    return p
def source(file):
    return re.findall(r"```swift\n(.*?)\n```", (HERE/file).read_text(),re.S)[0]
arch = version("uname","-m")
for name,sdk,target in [("edit","iphonesimulator",arch+"-apple-ios26.0-simulator"),
                        ("slider","iphonesimulator",arch+"-apple-ios26.0-simulator"),
                        ("audio","appletvsimulator",arch+"-apple-tvos26.0-simulator")]:
    check(name,source(name+".md"),sdk,target).check_returncode()
# The app closure has no UIKit members; run its identical declaration on the host.
edit = source("edit.md").replace("import UIKit","import Foundation")
probe = """
@main enum Probe { @MainActor static func main() {
let e = Editor()
let rename = e.installRename()
let a = rename("A")
e.editable = false
let b = rename("B")
e.editable = true
let c = rename("C")
print(a,b,c,e.names.joined(separator:","))
} }
"""
target = arch+"-apple-macos26.0"
for name,impl,expected in [
    ("working",edit,"true false true A,C"),
    ("alternative",edit.replace("guard let self, self.editable else", "guard self?.editable == true, let self else"),"true false true A,C"),
    ("snapshot",edit.replace("{ [weak self] name in","let allowed = editable\n        return { [weak self] name in").replace("self.editable else","allowed else"),"true true true A,B,C"),
    ("lost-action",edit.replace("self.editable else","false else"),"false false false ")]:
    result=check(name,impl+"\n"+probe,"macosx",target,True)
    result.check_returncode()
    assert result.stdout.strip()==expected.strip(), (name,result.stdout)
report={"xcode":version("xcodebuild","-version"),"host":version("sw_vers","-productVersion"),"checks":results}
(out/"receipt.json").write_text(json.dumps(report,indent=2)+"\n")
print(out/"receipt.json")

"""Replay only the eight pinned GP26-03 inputs, never arbitrary answer archives."""
import hashlib
import json
from pathlib import Path
import subprocess
import sys
from zipfile import ZipFile

ROOT = Path(__file__).resolve().parents[3]
HISTORY = ROOT / "research/evaluation/failure-driven/checkout-review-20261106"
PREFIX = ROOT / "evals/results"
share, dest, simulator = sys.argv[1:]
dest = Path(dest).resolve()
if PREFIX not in dest.parents or dest.exists():
    sys.exit("Provide a NEW private output directory under evals/results")
dest.mkdir(mode=0o700)
def hash_(b):
    return hashlib.sha256(b).hexdigest()
def pinned(b, expected):
    if hash_(b) != expected:
        raise ValueError("Archive or input pin mismatch: "+expected)
    return b

def archive(name, sha):
    path = Path(share)/name
    pinned(path.read_bytes(), sha)
    return ZipFile(path)

rows = json.loads((HISTORY/"results.json").read_bytes())["cases"]
with archive("swift-checkout-first-review-20261106-r1.zip","8a0bd7d23a7da33aa9917f29e9b52f80884c3c09d9520c8b1e4059c16cbeab3e") as first:
    for r in rows:
        ident=r["review_id"]
        pinned(first.read("answers/"+ident+".md"),r["answer_sha256"])
        pinned(first.read("inputs/GP26-03.md"),r["user_sha256"])
        for f in r["fences"]:
            pinned(first.read(f["file"]),f["sha256"])
        rel="compile/"+ident+"/Subject.swift"
        path=dest/rel
        path.parent.mkdir(parents=True)
        path.write_bytes(pinned(first.read(rel),r["source_sha256"]))

unit=dest/"unit"
subprocess.run(["node",HISTORY/"build-unit-packet.mjs",dest,unit],check=True)
with archive("swift-checkout-unit-evidence-20261106-r1.zip","a5afa59b28888f9f1a7d314b8a64c737893ca9abdede9393080c09b4282f2605") as captured:
    for path in [unit/"manifest.json", *unit.glob("*/*.swift")]:
        prefix="native/" if path.name=="manifest.json" else "native/inputs/"
        if path.read_bytes()!=captured.read(prefix+str(path.relative_to(unit))):
            raise ValueError("Not the original unit input: "+path.name)
sdk = subprocess.check_output(["xcrun","--sdk","iphonesimulator","--show-sdk-path"],text=True).strip()
observations=[]
for r in rows:
    ident=r["review_id"]; folder=dest/"compile"/ident
    cmd=["xcrun","swiftc","-sdk",sdk,"-target","arm64-apple-ios26.0-simulator","-typecheck",
         "-parse-as-library","-module-name","Review"+ident,"-module-cache-path",str(dest/"module-cache"),str(folder/"Subject.swift")]
    result=subprocess.run(cmd,capture_output=True,timeout=120)
    (folder/"stderr.txt").write_bytes(result.stderr)
    (folder/"stdout.txt").write_bytes(result.stdout)
    observations.append({"id":ident,"sourceSHA256":r["source_sha256"],"exit":result.returncode,
                         "historicalExit":r["exit_code"]})
    print(ident,result.returncode,flush=True)
(dest/"typechecks.json").write_text(json.dumps(observations,indent=2)+"\n")
subprocess.run(["node",ROOT/"code-examples/tools/native.mjs","execute",unit/"manifest.json",
                "checkout-unit-first",dest/"native",simulator],check=True)
subprocess.run([sys.executable,"-B",Path(__file__).with_name("summarize.py"),dest],check=True)

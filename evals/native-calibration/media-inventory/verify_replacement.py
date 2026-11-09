"""Verify first method outcomes; skips, setup failures and extra failures do not qualify."""
import json
import re
import sys
from replay_answers import BASE, D, PRIOR, H

batch = BASE / "picker-replacement-l8et0znn"
rows = []
env = json.loads((batch/"environment.json").read_bytes())
for cell in sorted(batch.glob("P-*")):
    name, variant = cell.name.rsplit(".", 1)
    meta = json.loads((cell/"input.json").read_bytes())
    src = (PRIOR/name/"Subject.swift").read_bytes()
    assert meta["original"] == H(src) and ((cell/"Subject.swift").read_bytes() == src) == (variant == "original")
    assert (cell/"Contract.swift").read_text() == (D/"ReplacementTests.swift").read_text().replace("FIXTURE_PATH", str(cell/"sample.mov"))
    for path, digest in meta["inputs"].items():
        assert H((cell/path).read_bytes()) == digest
    intent = json.loads((cell/"contract-intent.json").read_bytes())
    assert intent["source"] == meta["inputs"]["Subject.swift"] and intent["checks"] == [meta["inputs"]["Contract.swift"]]
    log = (cell/"contract.log").read_bytes()
    receipt = json.loads((cell/"contract.json").read_bytes())
    assert H(log) == receipt["log"]
    mutant = variant == "mutant"
    assert receipt["exit"] == (65 if mutant else 0)
    assert re.findall(rb"Test Case '-\[Checks.ReplacementTests testRetainedPickerAfterReplacement\]' (\w+) \(", log) == [b"failed" if mutant else b"passed"]
    errors = [x.rsplit(" - ",1)[-1] for x in receipt["diagnostics"]]
    assert errors == (["retired Off altered replacement", "retired option altered replacement"] if mutant else [])
    rows.append(dict(cell=cell.name, environment=meta["platform"], original=H(src), inputs=meta["inputs"], log=H(log),
                     receipt=H((cell/"contract.json").read_bytes()), status=receipt["status"], failures=errors))
assert {(r["environment"],r["cell"].split(".")[-1]) for r in rows} == {(p,v) for p in ("iOS","tvOS") for v in ("mutant","original")}
index = dict(batch=batch.name, anchors={p:env[p] for p in ("iOS","tvOS")}, records=rows)
dest = D/"replacement-receipts.json"
if sys.argv[1:] == ["--record"]:
    with dest.open("x") as stream:
        stream.write(json.dumps(index, indent=2)+"\n")
else:
    assert index == json.loads(dest.read_bytes())
print("Verified two originals and both first mutant failures.")

"""Read-only validation of the returned cohort and the dev.8 routing delta."""
from collections import Counter
from hashlib import sha256
import importlib.util
import json
from pathlib import Path
import sys

sys.dont_write_bytecode = True
E = Path(__file__).resolve().parents[1]
C = E / "failure-driven/candidates"
P = E / "dev7-comparison"
report = json.loads((E / "dev7-flash-haiku-results-20261107/summary.json").read_bytes())
assert report["seal_sha256"] == sha256((P / "seal.json").read_bytes()).hexdigest()
assert report["source_revision"] == "1e568ed02bd93a3dee595f38f0c12b524e1b8ea7"
cases = json.loads((P / "controller/scoring.json").read_bytes())
order = [r["case"] for r in cases]
for provider, n in (("gemini", 24), ("claude", 7)):
    rows = [r for r in report["pair_rows"] if r["provider"] == provider]
    assert len(rows) == n and {r["case"] for r in rows} == set(order[:n])
    outcomes = report["outcomes"][provider]
    assert Counter(r["transition"] for r in rows) == outcomes["paired_outcomes"]
    for arm in ("dev5", "dev7"):
        assert Counter(r[arm] for r in rows) == outcomes["arms"][arm]["source_grades"]
    for r in rows:
        a,b = r["dev5"],r["dev7"]
        expected = ("inconclusive" if "not-assessable" in (a,b) else
                    "preserved success" if a == b == "meets" else "persistent gap" if a == b else
                    "gain" if b == "meets" else "regression")
        assert r["transition"] == expected

def router(version):
    spec = importlib.util.spec_from_file_location(version, C / version / "route.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.select

old, new = map(router, ["0.3.0-dev.7", "0.3.0-dev.8"])
changed = {"ios-uikit-actions","ios-uikit-state","ios-uikit-text","ios-swiftui-lifecycle",
           "macos-appkit-actions","macos-appkit-structure","macos-swiftui-lifecycle",
           "tvos-uikit-state","tvos-uikit-lifecycle"}
seen = set()
for row in cases:
    cid = row["case"]
    prior = json.loads((P/"subjects"/cid/"dev7.json").read_bytes())["messages"]
    supplied = json.loads(prior[1]["content"])["suppliedReferences"]
    if not supplied:
        continue  # Controls retain the sealed zero-reference condition.
    args = (row["platform"], row["framework"], row["family"].split("/")[-1])
    status, docs = new(*args)
    assert status == "selected" and old(*args)[1] == supplied
    if cid in changed:
        seen.add(cid)
        assert "0.3.0-dev.8/references/" in docs[0]["path"] and docs[1:] == supplied[1:]
    else:
        assert docs == supplied
    assert new(*args, budget=1) == ("budget-exceeded", [])
assert seen == changed
assert new("macOS", "mixed", "structure") == ("needs-owner", [])
print("PASS: seal, 31 paired outcomes, both cohort denominators, 9 changed topic routes, unchanged comparison references elsewhere, byte limits.")

"""Validate scoring logic on synthetic observations only; no submission execution."""
import json
from pathlib import Path
from grade import focus, selection

assert selection([("Selected", "Selected"), ("Unselected", "Not selected")]) == "pass"
assert selection([("Chosen", "Selected"), ("Not chosen", "Unselected")],
                 {"Chosen": True, "Not chosen": False}) == "pass"
for pair in [("", ""), ("Selected", "Selected"), ("Unselected", "Selected")]:
    assert selection([("Selected", "Selected"), pair]) == "fail"
assert selection([("Selected", "Selected"), ("Different", "Different")]).startswith("review")
yes = (["primary"], True)
for case, good, bad in [
    ("Q082-A", (["fallback"], True), (["primary", "fallback"], True)),
    ("Q082-B", (["primary"], False), (["primary", "fallback"], False)),
]:
    assert focus(case, ordinary=yes, challenge=good) == dict(ordinary="pass", challenge="pass")
    assert focus(case, ordinary=None, challenge=bad) == dict(ordinary="inconclusive", challenge="fail")
assert set(json.loads((Path(__file__).resolve().parents[1]/"subject/questions.json").read_text())) == {"Q070","Q082-A","Q082-B"}

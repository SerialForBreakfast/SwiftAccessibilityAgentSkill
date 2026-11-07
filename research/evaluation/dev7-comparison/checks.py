"""Local integrity assertions; never execute subject code or make network calls."""
import sys
sys.dont_write_bytecode = True
from build import HERE, E, C, ROOT, V2, build, keyed, load, router, sha
import json


def check():
    expected = build()
    for name, data in expected.items():
        assert (HERE / name).read_bytes() == data, name
    paths = {p.relative_to(HERE).as_posix() for p in (HERE / "subjects").rglob("*") if p.is_file()}
    assert paths == {p for p in expected if p.startswith("subjects/")}
    rows = load(HERE / "controller/scoring.json")
    historical = load(E / "independent-v2-review-20261107/review.json")
    assert {r["family"] for r in rows} == {r["family"] for r in historical["conceptualCalibration"]}
    controls = changes = 0
    for row in rows:
        cid = row["case"]
        previous = load(V2 / "payloads" / cid / "candidate-controlled.json")["messages"]
        tasks = []
        for arm in ("dev5","dev7"):
            packet = load(HERE / "subjects" / cid / (arm+".json"))
            assert set(packet) == {"messages"}
            system, user = packet["messages"]
            assert [system["role"], user["role"]] == ["system","user"]
            data = json.loads(user["content"])
            assert set(data) == {"request","suppliedReferences"}
            tasks.append(data["request"])
            if arm == "dev5":
                assert system == previous[0] and data["suppliedReferences"] == json.loads(previous[1]["content"])["suppliedReferences"]
            else:
                assert bool(data["suppliedReferences"]) == bool(json.loads(previous[1]["content"])["suppliedReferences"])
                controls += not data["suppliedReferences"]
                assert all(set(ref) == {"path","content"} and (ROOT/ref["path"]).read_text()==ref["content"]
                           and "/evaluation/subjects/" not in ref["path"] and "/controller" not in ref["path"]
                           and not ref["path"].endswith(".swift") for ref in data["suppliedReferences"])
            assert "criterion-" not in user["content"] and "scoring.json" not in user["content"]
        assert tasks[0] == tasks[1]
        changes += tasks[0] != json.loads(previous[1]["content"])["request"]
    assert (controls,changes)==(6,3)
    assert router.select("macOS","mixed","structure")==("needs-owner",[])
    assert router.select("macOS","mixed","structure",owner="AppKit")[1][0]["path"].endswith("appkit-grouping.md")
    assert router.select("iOS","SwiftUI","media",budget=1)==("budget-exceeded",[])
    for platform in ("macOS","tvOS","iOS"):
        selected, docs = router.select(platform,"SwiftUI","media",level="contract",budget=100000)
        assert selected=="selected" and any("ReviewRegressionTests.swift" in r["path"] for r in docs)
    unit=load(E/"failure-driven/checkout-review-20261106/unit-results.json")["execution"]
    assert unit["failedTestIds"]==["CheckoutAnswerTests/testR16PreservesButtonTypography"]
    assert "CheckoutAnswerTests/testR13PreservesButtonTypography" in unit["executedTestIds"]
    assert "permanent" in str(next(r for r in rows if r["case"]=="ios-uikit-text")).lower()
    assert sum(r["questionChange"] is not None for r in rows)==3
    assert sum(c["evidenceClass"]=="genuine_gap" and bool(c["clarification"]) for r in rows for c in r["criteria"])==2
    print("PASS: sealed inputs, protected paths, paired questions, controller links, routes, budgets, calibration witnesses and six controls.")

if __name__=="__main__":
    check()

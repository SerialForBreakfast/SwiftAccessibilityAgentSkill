"""Apply the additive erratum in memory to the sealed 1572 first-run record."""
import hashlib
import io
import json
from pathlib import Path
import re
import sys
from zipfile import ZipFile

HERE = Path(__file__).resolve().parent
DEFAULT = HERE.parents[1] / "results/qualification-1572/whole-task-native-grader-controls-v1-return.zip"


def require(ok, detail):
    if not ok:
        raise ValueError(detail)


def statuses(node):
    if node.get("nodeType") == "Test Case":
        yield node["nodeIdentifier"].removesuffix("()"), node["result"]
    for child in node.get("children", []):
        yield from statuses(child)


def verify(path, correction):
    sha = lambda data: hashlib.sha256(data).hexdigest()
    raw = path.read_bytes()
    require(sha(raw) == correction["firstReturnSHA256"], "different return")
    with ZipFile(io.BytesIO(raw)) as z:
        original = z.read("input.zip")
        require(sha(original) == correction["inputSHA256"], "different input")
        with ZipFile(io.BytesIO(original)) as src:
            manifest = json.loads(src.read("manifest.json"))
        adds = correction["addToExpectedFailedIDs"]
        require(set(adds) == {"Q066/defect-oracle","Q083/defect-oracle"}, "scope changed")
        matched = 0
        for lane in manifest:
            key = lane["case"] + "/" + lane["lane"]
            record = json.loads(z.read(key + "/result.json"))
            if key not in adds:
                require(record["matches"] and record["outcome"] == lane["expected"], key)
            else:
                initial = lane["expectedFailedIDs"]
                expected = initial + adds[key]
                require(len(set(expected)) == len(expected), "duplicate method")
                require(record["expectedFailedIDs"] == initial and not record["matches"], key)
                for kind in ("working-oracle","defect-oracle"):
                    prefix = lane["case"] + "/" + kind + "/"
                    tree = json.loads(z.read(prefix + "xcresult-tests.json"))
                    events = [v for n in tree["testNodes"] for v in statuses(n)]
                    log = z.read(prefix + "first.log").decode()
                    diagnostics = re.findall(r"SubmittedTests\.swift:\d+: error: -\[Checks\.(\w+) (\w+)\] : XCTAssert\w* failed:", log)
                    failures = sorted(expected) if kind == "defect-oracle" else []
                    require(sorted(n for n,r in events if r == "Failed") == failures, prefix)
                    require(sorted({f"{c}/{m}" for c,m in diagnostics}) == failures, prefix + "log")
                    require(all(r in {"Passed","Failed"} for _,r in events), prefix + "incomplete")
                    require(sorted(n for n,_ in events) == sorted(record["declared"]), prefix + "methods")
                print(key + ": " + ", ".join(expected))
            matched += 1
        require(matched == 15, "missing lanes")
        print("15/15 saved lanes match amended expectations; original record remains 13/15.")


if __name__ == "__main__":
    verify(Path(sys.argv[1]) if len(sys.argv)>1 else DEFAULT,
           json.loads((HERE/"expected-failures.json").read_text()))

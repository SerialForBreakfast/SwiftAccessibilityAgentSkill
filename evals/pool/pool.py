"""Gold-task pool: load, export and qualify natively graded tasks. Offline; no model calls.

  python3 -B evals/pool/pool.py list [--cell CELL]
  python3 -B evals/pool/pool.py export TASK_ID            subject prompt + starter + answer contract
  python3 -B evals/pool/pool.py qualify [--cell CELL] [--task TASK_ID] [--record]

Qualification compiles every variant with the task's hidden oracle on the booted iOS/tvOS 26.5
simulators (or the macOS host) and checks each variant's expected status. It never boots or shuts
down simulators: boot them first. --record writes <cell>/scorecard.json (refused if present).
See README.md for the task format.
"""
import argparse
from hashlib import sha256
import json
from pathlib import Path
import sys

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT / "evals/rc1/grader"))
sys.path.insert(0, str(ROOT / "evals/protocol"))
import grade
from answer_contract import CONTRACT

CELLS = {"ios-uikit": ("ios", "UIKit"), "ios-swiftui": ("ios", "SwiftUI"), "macos-appkit": ("macos", "AppKit"),
         "macos-swiftui": ("macos", "SwiftUI"), "tvos-uikit": ("tvos", "UIKit"), "tvos-swiftui": ("tvos", "SwiftUI")}
STATUSES = {"pass", "contract-failure", "compile-failure"}
WORKSTREAMS = {f"W{i}" for i in range(1, 10)}


class Task:
    def __init__(self, folder):
        self.folder = folder
        meta = json.loads((folder / "task.json").read_bytes())
        self.meta, self.id = meta, meta["id"]
        assert folder.name == self.id and folder.parent.name == meta["cell"], folder
        self.platform, self.framework = CELLS[meta["cell"]]
        assert meta["workstream"] in WORKSTREAMS and meta["split"] in ("development", "transfer")
        assert meta["evidence"]["status"] in ("observed", "credible", "control")
        read = lambda name: (folder / name).read_text()
        self.prompt, self.starter, self.test = read("prompt.md").strip(), read("starter.swift"), read("test.swift")
        self.support = read("support.swift") if (folder / "support.swift").exists() else ""
        # The untouched starter must fail, except for no-change controls whose starter is already correct.
        starter_expect = meta.get("starterExpect", "contract-failure")
        assert starter_expect in STATUSES
        self.variants = [("reference", (folder / "reference.swift").read_bytes(), "pass"),
                         ("starter", (folder / "starter.swift").read_bytes(), starter_expect)]
        for v in meta["variants"]:
            assert v["expect"] in STATUSES and v.get("why"), (self.id, v)
            self.variants.append((Path(v["file"]).stem, (folder / v["file"]).read_bytes(), v["expect"]))
        kinds = [k for _, _, k in self.variants]
        assert sum(k == "pass" for n, _, k in self.variants if n != "starter") >= 2, \
            f"{self.id}: needs the reference plus at least one accepted alternative"
        assert any(k != "pass" for k in kinds), f"{self.id}: needs at least one mutant"
        # Oracle: hidden support declarations plus the check body, same markers as the rc.1 grader.
        self.oracle_source = (f"import {self.framework}\nimport Darwin\n{self.support}\n"
                              f"@main struct Oracle {{\n@MainActor static func check() -> Bool {{\n{self.test}\n}}\n"
                              f"static func main() {{ if check() {{ print(\"PASS:{self.id}\") }} "
                              f"else {{ print(\"FAIL:{self.id}\"); exit(42) }} }}\n}}\n")

    def export(self):
        return f"{self.prompt}\n\n{CONTRACT}\n\n```swift\n{self.starter}```\n"


_original_oracle = grade.oracle
grade.oracle = lambda t: t.oracle_source if hasattr(t, "oracle_source") else _original_oracle(t)


def load(cell=None, task=None):
    out = []
    for f in sorted(HERE.glob("*/*/task.json")):
        t = Task(f.parent)
        if (cell is None or t.meta["cell"] == cell) and (task is None or t.id == task):
            out.append(t)
    ids = [t.id for t in out]
    assert len(ids) == len(set(ids)), "duplicate task ids"
    return out


def qualify(tasks, record):
    expected = {(t.id, k): want for t in tasks for k, _, want in t.variants}
    report = grade.execute(tasks, lambda t: [(k, src) for k, src, _ in t.variants],
                           ROOT / "evals/results/pool", lambda r: expected[r["task"], r["variant"]])
    report["expected"] = {f"{a}/{b}": v for (a, b), v in expected.items()}
    report["taskSHA256"] = {t.id: sha256(b"".join((t.folder / n).read_bytes() for n in sorted(
        p.name for p in t.folder.iterdir() if p.is_file() and p.name != "scorecard.json"))).hexdigest() for t in tasks}
    wrong = [f"{r['task']}/{r['variant']}: got {r['status']}, expected {expected[r['task'], r['variant']]}"
             for r in report["rows"] if r["status"] != expected[r["task"], r["variant"]]]
    for w in wrong:
        print("MISMATCH", w)
    if record:
        cells = {t.meta["cell"] for t in tasks}
        assert len(cells) == 1, "record one cell at a time"
        grade.write_once(HERE / cells.pop() / "scorecard.json", report)
    print("ACCEPTED" if report["accepted"] else "NOT ACCEPTED", report["totals"], f"{len(tasks)} tasks")
    return 0 if report["accepted"] else 1


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("command", choices=["list", "export", "qualify"])
    p.add_argument("task_id", nargs="?")
    p.add_argument("--cell", choices=list(CELLS))
    p.add_argument("--task")
    p.add_argument("--record", action="store_true")
    a = p.parse_args()
    if a.command == "export":
        print(load(task=a.task_id)[0].export(), end="")
        return 0
    tasks = load(a.cell, a.task)
    if a.command == "list":
        for t in tasks:
            m = t.meta
            print(f"{m['cell']:14s} {t.id:34s} {m['workstream']} {m['split']:11s} {m['evidence']['status']:9s} {len(t.variants)} variants")
        return 0
    return qualify(tasks, a.record)


if __name__ == "__main__":
    sys.exit(main())

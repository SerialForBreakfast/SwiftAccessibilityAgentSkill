"""Stage a paired-run return for native grading with one arm-blind, mechanical selection rule.

  python3 -B evals/qualification-56/grade_run.py --calibrate
      Compare the mechanical rule with the hand selections used for the v4 return (no build).
  python3 -B evals/qualification-56/grade_run.py RETURN.zip SHA256
      Stage every cell under evals/results/persistent-replay/run-*/; then run
      research/evaluation/signal-panel-v4/replay/native.py <printed batch>.

  python3 -B evals/qualification-56/grade_run.py --collect BATCH
      After native.py: write BATCH/native.json for analyze.py. Only a compiled contract
      (unit-pass or unit-failure) gives a native primary verdict; every other outcome,
      including a selected subject that fails to compile, stays with the source grade.

Selection rule, identical for every arm and never a repair:
  S  no non-test Swift fence: the starter stands as the answer's recommendation
  N  no non-test Swift fence and no starter (source-only)
  n  the fence that declares every type the starter declares, or the only fence
  Cn the only fence redefines some starter types: splice those declarations into the starter
  G  a diff fence, or several fences with none complete (ambiguous; graded by source only)
"""
from common import *
import re, tempfile
from replay import selection as manual_q56
from prepare import modes as manual_v4

TEST = re.compile(r"\bfunc test\w*\s*\(|@Test\b|:\s*XCTestCase\b|\bimport XCTest\b")
TYPE = re.compile(r"\b(?:class|struct|enum|actor|protocol)\s+([A-Z]\w*)")


def select(answer, question):
    parts, starter = blocks(answer), blocks(question)
    if re.search(r"(?m)^`{3}diff\b", answer):
        return "G"
    code = [i for i, s in enumerate(parts) if not TEST.search(s)]
    if not code:
        return "S" if starter else "N"
    want = set(TYPE.findall(starter[0])) if starter else set()
    full = [i for i in code if want <= set(TYPE.findall(parts[i]))]
    if len(full) == 1:
        return str(full[0])
    if len(code) == 1 and not full and starter:
        names = set(TYPE.findall(parts[code[0]]))
        if names and names < want:
            return "C" + str(code[0])  # replace only the starter declarations this fence redefines
    return str(code[0]) if len(code) == 1 else "G"


def subject(mode, parts, starter):
    if mode == "S":
        return starter[0]
    if mode.startswith("C"):
        src, fence = starter[0], parts[int(mode[1:])]
        for name in TYPE.findall(fence):
            pat = r"\b(?:final\s+)?(?:class|struct|enum|actor|protocol)\s+" + name + r"\b"
            src = src.replace(declaration(src, pat), declaration(fence, pat))
        return src
    return parts[int(mode)]


def calibrate():
    agree, rows = 0, []
    with answers() as ret, questions() as qs:
        for c in json.loads(ret.read("return.json"))["cells"]:
            k, v4 = c["id"][2:6], c["arm"] == "signal-v4"
            hand = (manual_v4.get(k) or manual_q56[k])[v4]
            auto = select(ret.read(c["answer"]["path"]).decode(), qs.read("subjects/" + c["id"] + ".txt").decode())
            # Hand C/E/F codes name a declaration splice; the mechanical C code is the same kind of selection.
            same = auto == hand or (auto[:1] == "C" and hand[:1] in "CEF" and auto[1:] == re.sub(r"\D", "", hand))
            agree += same
            rows.append((c["id"], c["arm"], hand, auto, same))
    for r in rows:
        if not r[4]:
            print("differs", *r[:4])
    print(f"mechanical rule matches the hand selection in {agree}/{len(rows)} cells")


def stage(path, sha):
    batch = Path(tempfile.mkdtemp(prefix="run-", dir=BASE))
    counts = {}
    with packet(Path(path), sha) as ret, questions() as qs:
        for c in json.loads(ret.read("return.json"))["cells"]:
            r = next(x for x in PANEL if x["id"] == c["id"])
            q = qs.read("subjects/" + c["id"] + ".txt"); assert H(q) == r["questionSHA256"]
            a = ret.read(c["answer"]["path"]); assert H(a) == c["answer"]["sha256"]
            trial = c.get("trial", 1)
            cell = batch / f"{c['id']}.{c['arm']}.t{trial}"; cell.mkdir()
            (cell / "answer.txt").write_bytes(a); (cell / "question.txt").write_bytes(q)
            mode, parts = select(a.decode(), q.decode()), blocks(a.decode())
            counts[(c["arm"], mode if mode in ("N", "G", "S") else "selected")] = counts.get((c["arm"], mode if mode in ("N", "G", "S") else "selected"), 0) + 1
            if mode not in ("N", "G"):
                (cell / "Subject.swift").write_text(subject(mode, parts, blocks(q.decode())))
            proofs = [s for s in parts if TEST.search(s)]
            module = next((m[1] for s in proofs for m in re.finditer(r"@testable import (\w+)", s)), "YourAppModule")
            imports = "import XCTest\nimport SwiftUI\nimport AVFoundation\nimport " + ("AppKit" if r["platform"] == "macOS" else "UIKit") + "\n@testable import " + module + "\n"
            check, hashes = oracle(dict(r, criterion=r["originalCriterion"]))
            if check:
                (cell / "Contract.swift").write_text(imports + check)
            for n, s in enumerate(proofs):
                (cell / f"Proof{n}.swift").write_text(s if "import XCTest" in s else imports + s)
            meta = dict(id=c["id"], arm=c["arm"], trial=trial, platform=r["platform"], module=module, selection=mode,
                        oracle=hashes, inputs={p.name: H(p.read_bytes()) for p in cell.iterdir()})
            (cell / "input.json").write_text(json.dumps(meta, indent=2))
    for k in sorted(counts):
        print(*k, counts[k])
    print(batch.name)


def collect(name):
    batch, out = BASE / name, {}
    for cell in sorted(batch.glob("P-*")):
        meta, receipt = json.loads((cell / "input.json").read_text()), cell / "contract.json"
        status = json.loads(receipt.read_text())["status"] if receipt.exists() else None
        if status in ("unit-pass", "unit-failure"):
            out[f"{meta['id']}|{meta['arm']}|{meta['trial']}"] = {"primary": "pass" if status == "unit-pass" else "fail", "status": status}
    (batch / "native.json").write_text(json.dumps(out, indent=1, sort_keys=True) + "\n")
    print(f"{len(out)} native primary verdicts of {len(list(batch.glob('P-*')))} cells")


if __name__ == "__main__":
    if "--calibrate" in sys.argv:
        calibrate()
    elif "--collect" in sys.argv:
        collect(sys.argv[sys.argv.index("--collect") + 1])
    else:
        stage(sys.argv[1], sys.argv[2])

"""Offline zero-base experiment: emit reproducible arms and controller-only manifests."""
import argparse
import hashlib
import io
import json
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo

from rules import RULES

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
INV = "research/evaluation/failure-inventory/inventory.json"
SCORING = "research/evaluation/dev7-comparison/controller/scoring.json"
META = """---
name: swift-accessibility-agent
description: Review or implement accessibility in Swift interfaces for iOS, macOS and tvOS.
metadata:
  version: zero-base-v1
---

# Swift Accessibility Agent

On your first response using this skill, identify yourself as Swift Accessibility Agent (zero-base-v1).
When you consult a skill document, preface the answer with one short ROUTING: line naming the files actually read. Omit that line when none were read.
"""
UI = """interface:
  display_name: "Swift Accessibility Agent"
  short_description: "Accessibility for Swift interfaces on Apple platforms"
  default_prompt: "Use $swift-accessibility-agent to review this interface."
"""
CORE = {"restraint", "proof"}
# Primary decision per graded case; further controls and overlapping rules are retained below.
STREAM = {"W1":"ordinary","W2":"refresh","W3":"dismissal","W4":"layout","W5":"children",
          "W6":"ordinary","W7":"media","W8":"restraint","W9":"callbacks"}
SPECIAL = {"rc1/checkout-font":"font","mixed-macos-owner":"children",
           "macos-appkit-actions":"children","IOS-VALIDATION-OWNERSHIP-R1":"refresh",
           "rc1/motion-policy":"restraint","ios-missing-reference":"proof","tvos-version-boundary":"proof"}
def load(p):
    return json.loads((ROOT/p).read_bytes())


def digest(b):
    return hashlib.sha256(b).hexdigest()


def runtime(selected):
    entry = META
    files = {"agents/openai.yaml": UI}
    for r in selected:
        if r.id in CORE:
            entry += "\n" + r.guidance + "\n"
    if any(r.id not in CORE for r in selected):
        entry += "\nFor a matching implementation question, read only the relevant note:\n"
    for r in selected:
        if r.id not in CORE:
            path = "references/" + r.id + ".md"
            files[path] = "# " + r.label + "\n\n" + r.guidance + "\n"
            entry += f"- [{r.label}]({path})\n"
    files["SKILL.md"] = entry
    return {k:v.encode() for k,v in files.items()}


def archive(files):
    out = io.BytesIO()
    with ZipFile(out, "w") as z:
        for path, data in sorted(files.items()):
            info = ZipInfo("swift-accessibility-agent/" + path, (1980,1,1,0,0,0))
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            z.writestr(info,data,compress_type=ZIP_DEFLATED)
    return out.getvalue()


def board():
    inv = load(INV)
    by = {c["case"]: c for c in inv["cases"]}
    scores = {c["case"]:c for c in load(SCORING)}
    native_questions = {c["id"]:c["source"] for c in load("research/evaluation/native-activation-lift-v1/PROPOSAL.json")["cases"] if "source" in c}
    rows = []
    for case, c in by.items():
        if case in scores:
            question = f"research/evaluation/dev7-comparison/subjects/{case}/dev7.json#messages:last.content.request"
            rubric = SCORING + "#" + case
        elif case.startswith("GP26-"):
            question = ("evals/os26/" + ("expansion-1/" if int(case[-2:])>6 else "") + "prompts.json#" + case)
            rubric = question.replace("prompts.json", "acceptance.json")
        elif case.startswith("rc1/"):
            question = "evals/rc1-comparison/packet.json#subjectExports/" + case[4:]
            rubric = "evals/rc1/RUBRIC.md"
        elif case in native_questions:
            question = native_questions[case]
            rubric = "research/evaluation/native-activation-lift-v1/PROPOSAL.json"
        else:
            question = "research/evaluation/failure-driven/compact-candidate-a/BATCH.json#" + case
            rubric = "evals/reports/claude-haiku-20261105/README.md"
        primary = "proof" if case.startswith("EV") else SPECIAL.get(case, STREAM[c["workstream"]])
        related = {r.id for r in RULES if case in (r.target, r.control, r.neighbor)}
        related.add(primary)
        failed = sum(v.get("fail",0) for v in (c["targetUnaided"],c["targetWithSkill"],c["otherModels"]))
        passed = sum(v.get("pass",0) for v in (c["targetUnaided"],c["targetWithSkill"],c["otherModels"]))
        rows.append(dict(case=case, decision=c["title"], platform=c["platform"], framework=c["framework"],
                         disposition="mixed result" if failed and passed else "observed failure" if failed else "preserved success" if passed else "insufficient evidence",
                         priority=c["disposition"], evidenceSources=c["sources"], question=question,rubric=rubric,
                         rules=sorted(related), failedCriteria=c["failingCriteria"],
                         directContracts=[v for k in scores.get(case,{}).get("criteria",[]) for v in k["contracts"]]))
    for r in RULES:
        assert by[r.target]["modelsFailing"] and len({r.target,r.control,r.neighbor})==3
        assert (ROOT/r.evidence).is_file()
    for row in rows:
        for key in ("question","rubric"):
            assert (ROOT/row[key].split("#")[0]).is_file(), row[key]
    pool=[]
    for p in sorted((ROOT/"evals/pool").glob("*/*/task.json")):
        t=json.loads(p.read_bytes())
        pool.append(dict(id=t["id"], split=t["split"], cell=t["cell"], spec=str(p.relative_to(ROOT)),
                         historicalAnalogue=t["evidence"].get("inventoryCase"), outcome="not graded by this campaign"))
    base = ROOT/"code-examples"
    catalog = [str(p.relative_to(ROOT)) for p in sorted([
        *base.glob("*/*/evaluation/*.prompt.md"), *base.glob("*/*/evaluation/prompt.json")])]
    return dict(target="claude-haiku-5-5 low", evidenceInventory=INV, sourceRegistry=inv["sources"],
                observations=inv["totals"]["observations"], cases=rows, pool=pool, otherPackagePrompts=catalog,
                ungradedDevelopmentScenarios=[r["id"] for r in load("evals/scenarios.json") if r["split"]=="development"],
                rules=[dict(id=r.id,revision=digest(r.guidance.encode()),target=r.target,contrast=r.control,
                            neighbor=r.neighbor,contrastDecision=r.distinction,witness=r.evidence,
                            status="candidate hypothesis; marginal effect unmeasured") for r in RULES])


def outputs():
    matrix=board()
    arms={}
    products={}
    for row in matrix["cases"]:
        case=row["case"]
        path=row["question"].split("#")[0]
        if case.startswith("EV"):
            row["inputStatus"]="hash catalog only; retrieve exact subject bytes before use"
            continue
        if case.startswith("rc1/"):
            prompt=load(path)["subjectExports"][case[4:]]
        elif case.startswith("GP26-"):
            prompt=next(c["prompt"] for c in load(path)["cases"] if c["id"]==case)
        elif path.endswith("/dev7.json"):
            # Historical user turns include inline reference bodies. Only the developer request belongs in a native skill comparison.
            msg=load(path)["messages"][-1]
            assert msg["role"]=="user"
            prompt=json.loads(msg["content"])["request"]
        else:
            prompt=(ROOT/path).read_text()
        key="subjects/"+case.replace("/","-")+".txt"
        products[key]=prompt.encode()
        row.update(subjectPath=key,subjectSHA256=digest(products[key]),inputStatus="development export; grading admission separate")
    for name,chosen in [("shell",()),("full",RULES)]+[("minus-"+r.id,[s for s in RULES if s!=r]) for r in RULES]:
        files=runtime(chosen)
        blob=archive(files)
        arms[name]=dict(sha256=digest(blob),rules=[r.id for r in chosen],entryBytes=len(files["SKILL.md"]),
                        payloadBytes=sum(map(len,files.values())),files={k:digest(v) for k,v in files.items()})
        products["archives/"+name+".zip"]=blob
    as_json=lambda x:(json.dumps(x,indent=2,ensure_ascii=True)+"\n").encode()
    products["matrix.json"]=as_json(matrix)
    lines=["# Failure-to-rule board", "", "One row per graded case, including passes. Associations are hypotheses, not evidence of challenger lift.",
           "See matrix.json for inputs, rubric locators, source registry and scoped contracts.", "",
           "| Case | Framework / platform | Observed developer decision | Disposition | Candidate rules |",
           "|---|---|---|---|---|"]
    for row in matrix["cases"]:
        lines.append("| {case} | {platform} {framework} | {decision} | {disposition} | {rules} |".format(
            **{**row,"rules":", ".join(row["rules"])}))
    products["BOARD.md"]=("\n".join(lines)+"\n").encode()
    products["manifest.json"]=as_json(dict(arms=arms,matrixSHA256=digest(products["matrix.json"]),
                                         incumbent="evals/rc1/swift-accessibility-agent-0.3.0-rc.1.zip",
                                         incumbentSHA256="d691b3c29c933ac9305c2a84a73c952d44e7ebd66e4742578314a2f132de1b93",
                                         executionAuthorized=False))
    return products


if __name__ == "__main__":
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--check",action="store_true")
    args=ap.parse_args()
    for path,data in outputs().items():
        dest=HERE/path
        if args.check:
            if dest.read_bytes()!=data:
                raise SystemExit("Mismatch: "+path)
        else:
            dest.parent.mkdir(exist_ok=True)
            dest.write_bytes(data)
    print("Verified" if args.check else "Built", "matrix and eleven archive variants")

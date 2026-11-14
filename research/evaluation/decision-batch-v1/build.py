"""Build an isolated candidate and a separate controller board, entirely offline."""
import argparse
import csv
import hashlib
import io
import json
import re
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
DISC = ROOT / "evals/discovery-500"
BASE = HERE.parent / "signal-panel-v7-1/skill"
ROUTES = {
    "actions": "Reused controls, shortcuts, registration and edit authority",
    "lifecycle": "Dismissal, background exposure and focus restoration",
    "validation": "Form validation, late replies and restarted observers",
    "text": "Rotor search, text coordinates and scaling",
    "structure": "Containers, native controls, row semantics and visible names",
    "media": "Player item selection, metadata and asynchronous menus",
    "appearance": "Motion preferences and color contrast",
}
ALIASES = {
    "editable-wrapper": "editable-owner",
    "native-slider": "native-restraint",
    "automatic-vs-off": "media-off",
}
ENTRY = """---
name: swift-accessibility-agent
description: Review, implement or test accessible Swift interfaces on iOS, macOS and tvOS, including native controls, text navigation, presentation, media and adaptive display.
metadata:
  version: decision-batch-v1
---

# Swift Accessibility Agent

Identify yourself as Swift Accessibility Agent (decision-batch-v1) on first use.
Name only guidance actually opened in a concise ROUTING: line.

Start with the user's interaction and which framework owns its control.
Review the supplied path before proposing changes. Preserve working native
behavior and ordinary actions. If a fix is needed, connect it to the existing
control rather than returning a disconnected helper. On explanation requests,
answer the decision without imposing an implementation or test deliverable.

For a requested test, drive the installed input through the distinguishing
transition. Check both the effect that must change and the ordinary path that
must survive. A helper that prevents the triggering state does not test it.
Separate a focus request or configuration from what a person experiences.

Open only the relevant topic; consult a second topic only for a real boundary.

"""
def rows(path, delim=","):
    with path.open() as f:
        return list(csv.DictReader(f, delimiter=delim))

def digest(data):
    return hashlib.sha256(data).hexdigest()

def build():
    decisions = rows(HERE / "decisions.tsv", "\t")
    cases = json.loads((DISC / "controller.json").read_text())
    grades = {r["id"]: r for r in rows(DISC / "grade350/grades.csv")}
    proofs = {r["id"]: r for r in json.loads((ROOT / "evals/proof-repair-20/evidence.json").read_text())}
    scenarios = {r["family"]: r for r in rows(DISC / "scenarios.tsv", "\t")}
    assert len(decisions) == len({r["family"] for r in decisions}) == 51
    assert set(ROUTES) == {r["route"] for r in decisions}
    docs, board = {}, []
    docs["agents/openai.yaml"] = (BASE / "agents/openai.yaml").read_bytes()
    docs["references/apis.md"] = (BASE / "references/apis.md").read_bytes()
    docs["SKILL.md"] = (ENTRY + "".join(f"- [{v}](references/{k}.md)\n" for k,v in ROUTES.items()) +
                        "- [SDK member spellings, when implementation needs them](references/apis.md)\n").encode()
    for route,title in ROUTES.items():
        lines = ["# " + title, ""]
        for d in (d for d in decisions if d["route"] == route):
            key = d["family"]
            sc = scenarios.get(key)
            assert sc or key in ALIASES
            cases_for_rule = []
            for c in cases:
                grade = grades.get(c["id"], {})
                scoped_alias = (
                    key == "native-slider" and any(f.endswith("/GP26-11.txt") for f in c["families"])
                    or key == "editable-wrapper" and "interop-double-exposure" in c["families"]
                    or key == "automatic-vs-off" and grade.get("family") == "media-off"
                    and "automatic" in grade["reason"].lower()
                )
                if key not in c["families"] and not scoped_alias:
                    continue
                assert not grade or grade["promptSHA256"] == c["promptSHA256"]
                cases_for_rule.append(dict(id=c["id"], platform=c["platform"], framework=c["framework"],
                                           prompt=c["promptSHA256"], answer=grade.get("answerSHA256"),
                                           primary=grade.get("primary"), reason=grade.get("reason")))
            assert cases_for_rule, key
            refs = []
            for p in d["proof"].split(","):
                if p == "-":
                    continue
                rec = proofs[p]
                assert rec["outcomes"] == {"working":["passed"],"alternative":["passed"],"defect":["failed"]}
                assert (ROOT / rec["source"]).is_file()
                refs.append(dict(id=p,method=rec["method"],source=rec["source"],receipts=rec["firstReceipts"]))
            lines.extend(["- " + d["guidance"], ""])
            board.append(dict(family=key,route=route,cases=cases_for_rule,relatedQualifiedChecks=refs,
                              expectation=sc["expected"] if sc else d["guidance"],
                              decoy=sc["decoy"] if sc else {"editable-wrapper":"hide the entire wrapper",
                              "native-slider":"require a custom modifier","automatic-vs-off":"request automatic selection"}[key]))
        docs[f"references/{route}.md"] = ("\n".join(lines) + "\n").encode()
    assert all(path.decode() in docs for path in re.findall(rb"\]\(([^)]+)\)",docs["SKILL.md"]))
    assert not re.search(rb'Q-[a-f0-9]{16}|Q\d{3}\b|G-[a-f0-9]{14}', b'\n'.join(docs.values()))
    observed = {r["id"] for b in board for r in b["cases"] if r["primary"]=="fail"}
    assert observed == {qid for qid,r in grades.items() if r["primary"]=="fail"}
    buf = io.BytesIO()
    with ZipFile(buf,"w") as z:
        for path,data in sorted(docs.items()):
            info = ZipInfo("swift-accessibility-agent/"+path)
            info.compress_type = ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            z.writestr(info,data)
    # Sample passing cases only where a recorded failure gives the change headroom.
    # A source-supported answer need not have come from a working starter.
    index = {c["id"]: c for c in cases}
    panel = {qid: "failure" for qid in observed}
    controls = {}
    for b in board:
        if not any(c["id"] in observed for c in b["cases"]):
            continue
        passing = [c for c in b["cases"] if c["primary"] == "pass"]
        ranked = sorted(passing, key=lambda c: (not index[c["id"]]["workingControl"],
                                                len(index[c["id"]]["families"]), c["id"]))
        controls[b["family"]] = ranked[0]["id"] if ranked else None
        if ranked:
            panel[ranked[0]["id"]] = "preservation"
    selection = {"status":"offline proposal; not dispatched", "controlsByDecision":controls,
                 "questions":[dict(id=qid, role=role, promptSHA256=index[qid]["promptSHA256"],
                                   platform=index[qid]["platform"], framework=index[qid]["framework"],
                                   workingStarter=index[qid]["workingControl"])
                              for qid,role in sorted(panel.items())]}
    subject_files = {}
    with ZipFile(DISC / "subjects.zip") as originals:
        for row in selection["questions"]:
            path = index[row["id"]]["path"]
            data = originals.read(path)
            assert digest(data) == row["promptSHA256"]
            subject_files[path] = data
    additions = json.loads((HERE/"controls/rubrics.json").read_text())
    assert set(additions) == {k for k,v in controls.items() if v is None}
    for family, spec in additions.items():
        data = (HERE/"controls"/spec["file"]).read_bytes()
        qid = "Q-"+digest(data)[:16]
        assert qid not in index and qid not in controls.values()
        subject_files[f"questions/{qid}.md"] = data
        controls[family] = qid
        selection["questions"].append(dict(id=qid,role="new opposing control",
            promptSHA256=digest(data),platform=spec["platform"],framework=spec["framework"],
            workingStarter=True,unaidedGrade=None))
    selection["status"] = "frozen development inputs; execution not authorized"
    packet = io.BytesIO()
    with ZipFile(packet,"w") as z:
        for path,data in sorted(subject_files.items()):
            z.writestr(ZipInfo(path),data,compress_type=ZIP_DEFLATED)
    export = lambda obj: (json.dumps(obj,indent=2)+"\n").encode()
    outputs = {"candidate.zip":buf.getvalue(),"board.json":export(board),
               "panel.json":export(selection),"questions.zip":packet.getvalue()}
    seal = {name:digest(data) for name,data in outputs.items()}
    for path in [HERE/"controls/rubrics.json", DISC/"controller.json", DISC/"grade350/grades.csv"]:
        seal[str(path.relative_to(ROOT))] = digest(path.read_bytes())
    outputs["input-seal.json"] = export(seal)
    return outputs

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--check",action="store_true")
    args = parser.parse_args()
    for name,data in build().items():
        path = HERE/name
        if args.check:
            if path.read_bytes() != data:
                raise SystemExit("stale "+name)
        else:
            path.write_bytes(data)
        print(name,digest(data))

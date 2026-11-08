"""Offline integrity tests. Optional private evidence verification never extracts submissions."""
import argparse
import json
import re
from zipfile import ZipFile

from build import HERE, ROOT, RULES, META, UI, digest, load, outputs


def verify_public():
    for path, data in outputs().items():
        assert (HERE/path).read_bytes() == data, path
    matrix = json.loads((HERE/"matrix.json").read_bytes())
    manifest = json.loads((HERE/"manifest.json").read_bytes())
    assert digest((ROOT/manifest["incumbent"]).read_bytes()) == manifest["incumbentSHA256"]
    ids = {r["case"] for r in matrix["cases"]}
    assert len(ids)==len(matrix["cases"])
    assert {r["id"] for r in load("evals/os26/prompts.json")["cases"]} <= ids
    assert {r["id"] for r in load("evals/os26/expansion-1/prompts.json")["cases"]} <= ids
    assert all(set(row["rules"]) <= {r.id for r in RULES} for row in matrix["cases"])
    assert not manifest["executionAuthorized"]
    exports={HERE/r["subjectPath"] for r in matrix["cases"] if "subjectPath" in r}
    assert exports==set((HERE/"subjects").glob("*.txt"))
    for p in exports:
        assert b'"suppliedReferences"' not in p.read_bytes()
    baseline=ROOT/"evals/baselines/0.2.2"
    for f in json.loads((baseline/"manifest.json").read_bytes())["files"]:
        assert digest((baseline/"files"/f["path"]).read_bytes())==f["sha256"], f["path"]
    font=load("evals/headroom/checkout-font/scorecard.json")
    assert font["contractsSHA256"]==digest((ROOT/"evals/headroom/checkout-font/contracts.py").read_bytes())
    assert font["accepted"] and font["expected"]=={r["task"]+"/"+r["variant"]:r["status"] for r in font["rows"]}
    for name, info in manifest["arms"].items():
        with ZipFile(HERE/"archives"/(name+".zip")) as z:
            prefix = "swift-accessibility-agent/"
            files = {p.removeprefix(prefix):z.read(p) for p in z.namelist()}
            assert len(files)==len(z.namelist())
            entry = files["SKILL.md"].decode()
            assert entry.startswith(META) and files["agents/openai.yaml"]==UI.encode()
            assert name!="shell" or (entry==META and len(files)==2)
            assert set(re.findall(r'\]\((references/[^)]+)\)',entry)) == {p for p in files if p.startswith("references/")}
            text = b"\n".join(files.values()).decode()
            for r in RULES:
                present = name not in ("shell","minus-"+r.id)
                assert (r.guidance in text)==present and (r.id in info["rules"])==present
            assert not any(s in text for s in ("GP26-", "EV06","NegativeFixtures","evals/","research/"))
    print("PASS: reproducible archives, isolated development requests, disclosure parity, scoped removal, internal links, rc.1 and archived baseline pins, paired font scorecard")


def private_index():
    base = ROOT/"evals/results"
    records = []
    def record(case, bundle, key, prompt, answer, grade):
        records.append(dict(case=case, bundle=str(bundle.relative_to(ROOT)), key=key,
                            promptSHA256=digest(prompt), answerSHA256=digest(answer), grading=grade))
    p=base/"failure-inventory/bundles/dev7-flash-haiku-controller-return-r1.zip"
    with ZipFile(p) as z:
        for r in json.loads(z.read("answers-and-grades.json")):
            prompt=z.read("inputs/"+r["input_path"])
            answer=r["original_answer"].encode()
            assert digest(prompt)==r["input_sha256"] and digest(answer)==r["originalSha256"]
            record(r["case"],p,r["id"],prompt,answer,"answers-and-grades.json:grade")
    p=base/"rc1-failure-replay-20261107/bundles/rc1-failure-replay-seven-return.zip"
    with ZipFile(p) as z:
        for path,h in json.loads(z.read("checksums.json")).items():
            assert digest(z.read(path))==h
        for case in json.loads(z.read("grades.json")):
            record(case,p,case,z.read(case+"/prompt.txt"),z.read(case+"/answer.txt"),"grades.json:"+case)
    for p in sorted((base/"rc1-return-20261107/bundles").glob("rc1-release-native*zip")):
        with ZipFile(p) as z:
            for r in json.loads(z.read("index.json")):
                if r["state"]!="completed":
                    continue
                cell="cells/"+r["cell"]+"/"
                prompt=z.read(cell+"prompt.txt")
                assert digest(prompt)==r["promptSHA256"]
                record("rc1/"+r["task"],p,cell,prompt,z.read(cell+"answer.txt"),cell+"grade.json")
    folder=base/"zero-base-v1"
    folder.mkdir(exist_ok=True)
    data=(json.dumps(records,indent=2)+"\n").encode()
    out=folder/(digest(data)+"-answer-index.json")
    if out.exists():
        assert out.read_bytes()==data
    else:
        out.write_bytes(data)
    print("Verified",len(records),"private paired input/answer records;",out.name)


if __name__=="__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--private",action="store_true")
    args=parser.parse_args()
    verify_public()
    if args.private:
        private_index()

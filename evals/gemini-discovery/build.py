"""Build or verify held, controller-owned Gemini discovery inputs. Standard library only."""
import argparse
from collections import Counter
from hashlib import sha256
import json
from pathlib import Path
import re

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
ZERO = ROOT/"research/evaluation/zero-base-v1"
def sha(b): return sha256(b).hexdigest()
def read(p): return json.loads(p.read_bytes())
def dump(x): return (json.dumps(x,indent=2,ensure_ascii=False)+"\n").encode()
def rel(p): return str(p.relative_to(ROOT))
def code(text):
    # Only remove full comment lines and isolated on-line developer annotations.
    text=re.sub(r"(?m)^\s*//[^\n]*$", "", text)
    text=re.sub(r"/\*[^*\n]*\*/", "", text)
    return text.strip()

def labels():
    res={}
    for line in (HERE/"decisions.tsv").read_text().splitlines():
        if not line or line.startswith("#"): continue
        key,aliases,request=line.split("\t")
        for alias in aliases.split():
            assert alias not in res, alias
            res[alias]=(key,request)
    return res

def build():
    lookup=labels()
    rows=[]; inputs={}; seen={}; skipped=[]
    def add(prompt, **row):
        prompt=prompt.strip()+"\n"
        sig=sha(prompt.encode())
        if sig in seen:
            skipped.append(dict(source=row["source"],reason="identical subject bytes",alias=seen[sig]))
            return
        cid="G-"+sig[:14]
        seen[sig]=cid; inputs[cid]=prompt
        rows.append(dict(id=cid,inputSHA256=sig,**row))
    for path in sorted((ROOT/"code-examples").glob("*/*/manifest.json")):
        pkg=path.parent; d=read(path); os=d["platform"]
        if os not in ("iOS","macOS","tvOS"): continue
        fw="SwiftUI" if pkg.parent.name=="swiftui" else "AppKit" if os=="macOS" else "UIKit"
        pins={f["path"]:f["sha256"] for f in d["files"]}
        claims={c["id"]:c for c in d["claims"]}
        def pinned(key):
            data=(pkg/key).read_bytes()
            assert sha(data)==pins[key],(pkg.name,key)
            return data.decode()
        controls=set()
        for ch in d["checks"]:
            if ch.get("expected")!="failure" or not ch.get("replacement") or not ch.get("failureIds"): continue
            alias=ch["id"].removesuffix("-negative")
            if alias not in lookup: raise ValueError((pkg,alias))
            key,request=lookup[alias]
            if alias=="stale" and pkg.name.startswith("media-"): key,request=lookup["validation-generation"]; request="After reloading track choices, a late error from the previous load sometimes replaces a successful result. Is this handled?"
            if alias=="wrongnotification" and pkg.name=="uikit-lifecycle-v1": key,request="motion-notification","Does this observer refresh the motion setting when that setting actually changes?"
            if alias=="hiddencontrols" and pkg.name=="uikit-media-v1": key,request="player-controls","Can users still operate the player's built-in controls and keep automatic media selection?"
            if alias=="droppedaction": key,request="shortcut-dispatch","The named shortcut appears, but tapping it does not run the intended callback. What should change?"
            if alias=="row-selected":key,request="row-role","Can the table row describe its role and selection without swallowing its actionable children?"
            if alias=="stale-status":key,request="refresh-name","After a search result is selected, is its current status reported without the previous search label?"
            target=ch["replacement"]["target"]
            sources=[f for f in pins if f.startswith("Sources/") and f.endswith(".swift")]
            for ref in (False,True):
                if ref and target in controls:continue
                if ref:controls.add(target)
                parts={}
                # Resolve local type definitions referenced by the edited source, transitively.
                available={f:pinned(f) for f in sources}
                pending=[target]
                while pending:
                    f=pending.pop()
                    if f in parts:continue
                    body=code(available[f] if f!=target or ref else pinned(ch["replacement"]["source"]))
                    parts[f]=body
                    for dep,s in available.items():
                        if dep==f or dep in parts:continue
                        names=re.findall(r"(?m)^(?:(?:final|public|private|internal|indirect) )*(?:class|struct|protocol|enum|typealias|actor) (\w+)",s)
                        if any(re.search(r"\b"+n+r"\b",body) for n in names):pending.append(dep)
                prompt=(f"I'm reviewing a {fw} change for {os} {d['deploymentTarget']}. {request}\n\n"
                        "Review the supplied implementation against that requirement. If it already works, say why and leave it alone. "
                        "Otherwise provide the smallest integrated Swift change and a focused unit check. Preserve unrelated behavior.\n")
                for f,s in parts.items(): prompt+=f"\n{Path(f).name}:\n```swift\n{s}\n```\n"
                add(prompt,platform=os,framework=fw,lane="preservation" if ref else "repair",source=rel(path),
                    check=ch["id"],decision=key,sourceFile=target if ref else ch["replacement"]["source"],
                    assertions=ch["failureIds"],claims=[claims[i] for i in ch["claimIds"]],
                    limits=d["limitations"],grade="masked source review against linked behavior; units only if unchanged answer and original interface qualify")
        for p in sorted((pkg/"evaluation").glob("*")):
            if p.name.endswith(".prompt.md"):
                q=p.read_text(); rubric=p.with_name(p.name.replace(".prompt.md",".rubric.md"))
            elif p.name=="prompt.json":
                q=read(p)["prompt"];rubric=p.with_name("controller.md")
            else:continue
            if not rubric.is_file():
                skipped.append(dict(source=rel(p),reason="no paired rubric"));continue
            add(q,platform=os,framework=fw,lane="implementation",source=rel(p),rubric=rel(rubric),
                decision=None,grade="existing draft rubric; accept equivalent designs, assess integration separately")
    for r in read(ZERO/"matrix.json")["cases"]:
        if r["platform"] not in ("iOS","macOS","tvOS") or not r.get("subjectPath"):
            skipped.append(dict(source=r["case"],reason="outside three-platform scope or missing public neutral input"));continue
        p=ZERO/r["subjectPath"]
        assert sha(p.read_bytes())==r["subjectSHA256"]
        add(p.read_text(),platform=r["platform"],framework=r["framework"],lane="historical",source=rel(p),
            rubric=r["rubric"],decision=None,grade="original scoped rubric; no historical grade is an unaided result for this cohort")
    for p in sorted((ROOT/"evals/pool").glob("*/*/task.json")):
        t=read(p); ev=read(ZERO/"pool-receipts.json")[t["id"]]
        if not ev["status"].startswith("qualified") or t["split"]!="development":
            skipped.append(dict(source=rel(p),reason="quarantined or transfer-reserved"));continue
        os,fw=t["cell"].split("-")
        add((p.parent/"prompt.md").read_text()+"\nPaste the complete resulting Swift file in your reply.\n\n```swift\n"+(p.parent/"starter.swift").read_text()+"\n```",
            platform={"ios":"iOS","macos":"macOS","tvos":"tvOS"}[os],framework={"uikit":"UIKit","appkit":"AppKit","swiftui":"SwiftUI"}[fw],
            lane="integration",source=rel(p),rubric=rel(p.parent/"test.swift"),decision=None,grade="reviewed local native grader if eligible; validated task receipts, not model outcomes")
    for line in (HERE/"workflows.tsv").read_text().splitlines():
        if not line or line.startswith("#"):continue
        os,fw,key,ref,q,criterion=line.split("\t")
        guide,=list((ROOT/"references").glob("*/guidelines/"+ref+"-*.md"))
        add(f"{os}, {fw}. {q}",platform=os,framework=fw,decision=key,lane="workflow",source=rel(guide),
            criterion=criterion,grade="masked source review: judge the stated user outcome, accept equivalent paths")
    # Mix platform, framework and lane across the run so cutoffs do not exhaust only one cell.
    groups={}
    for r in rows: groups.setdefault((r["platform"],r["framework"],r["lane"]),[]).append(r)
    for v in groups.values():v.sort(key=lambda r:r["id"])
    ordered=[v[i] for i in range(max(map(len,groups.values()))) for v in groups.values() if i<len(v)]
    return inputs,ordered,skipped

def artifacts():
    inputs,rows,skip=build()
    # Freeze controller dependencies too; the subject digest alone cannot detect rubric drift.
    paths={r["source"] for r in rows}
    paths.update(r["rubric"].split("#")[0] for r in rows if r.get("rubric"))
    paths.update(rel(p) for p in (ROOT/"evals/pool").glob("*/*/task.json"))
    paths.update(rel(p) for p in (ROOT/"evals/rc1/grader").glob("*.py"))
    paths.add(rel(ZERO/"pool-receipts.json"))
    dependencies={path:sha((ROOT/path).read_bytes()) for path in sorted(paths)}
    sub=b"".join((json.dumps({"id":r["id"],"prompt":inputs[r["id"]]},ensure_ascii=False)+"\n").encode() for r in rows)
    controller=dump(rows)
    return {"subjects.jsonl":sub,"controller.json":controller,"excluded.json":dump(skip),
            "seal.json":dump(dict(model="gemini-3.8-flash-low",authorized=False,extraSpend=0,
                inputsSHA256=sha(sub),controllerSHA256=sha(controller),excludedSHA256=sha(dump(skip)),
                challengerSHA256=sha((ZERO/"archives/full.zip").read_bytes()),cases=len(rows),
                decisionKeys=len({r["decision"] for r in rows if r["lane"] in ("repair","workflow")}),
                platform=dict(Counter(r["platform"] for r in rows)),lanes=dict(Counter(r["lane"] for r in rows)),
                policyHashes={n:sha((HERE/n).read_bytes()) for n in ("HANDOFF.md","score.py")},
                gradingPins=dependencies,
                schedule=[r["id"] for r in rows]))}
if __name__=="__main__":
    ap=argparse.ArgumentParser()
    ap.add_argument("--check",action="store_true")
    a=ap.parse_args()
    for n,b in artifacts().items():
        if a.check:
            if (HERE/n).read_bytes()!=b:raise SystemExit("seal mismatch: "+n)
        else:(HERE/n).write_bytes(b)
    s=read(HERE/"seal.json")
    print(s["cases"],s["platform"],s["lanes"],s["decisionKeys"],"primary decision keys")

"""Render the generated sections of PROMPT-IMPROVEMENTS.md from items.json and the shards.

  python3 -B research/evaluation/prompt-improvements-v1/render.py
Hand-written sections stay as they are; text between <!-- name:begin --> and <!-- name:end --> markers
is replaced. verify.py checks the result.
"""
from collections import Counter, defaultdict
import json
from pathlib import Path
import re
import sys

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
LANES = ["repair", "preservation", "implementation", "historical", "integration", "workflow"]
DISP_ORDER = ["repair-oracle", "split-criteria", "specify-policy", "rewrite-neutral", "pair-variant", "raise-to-integration",
              "grade-components", "keep-control", "reserve-transfer", "retire-duplicate"]
SKILL_NAMES = {"S1": "Review: trace the path, leave working code", "S2": "Verify through the actual handler",
               "S3": "Callback capture and validation", "S4": "Focus destination and eligibility",
               "S5": "Precise platform facts", "S6": "Text-offset units", "S7": "Media selection and policy",
               "S8": "Restraint and pruning"}
esc = lambda s: (s or "").replace("|", "\\|").replace("\n", " ")


def generated(items, recs):
    rows = [(items[i], recs[i]) for i in items if i in recs]
    out = {}
    # Headroom by lane: verdicts and what the review proposes.
    L = ["| Lane | Items | Unaided pass / fail / inconclusive | Confirmed model gaps | Rewrite or pair for headroom | Oracle or criteria repairs | Keep as control |",
         "|---|---:|---|---:|---:|---:|---:|"]
    for lane in LANES:
        rs = [(i, r) for i, r in rows if i["lane"] == lane]
        v = Counter(i["verdict"] for i, _ in rs)
        d = Counter(r["disposition"] for _, r in rs)
        L.append(f"| {lane} | {len(rs)} | {v['pass']} / {v['fail']} / {v['inconclusive']} | "
                 f"{sum(r['problem'] == 'real-model-gap' for _, r in rs)} | {d['rewrite-neutral'] + d['pair-variant'] + d['raise-to-integration']} | "
                 f"{d['repair-oracle'] + d['split-criteria'] + d['specify-policy'] + d['grade-components']} | {d['keep-control']} |")
    out["lanes"] = "\n".join(L) + "\n"
    # Dispositions and problems.
    d, p = Counter(r["disposition"] for _, r in rows), Counter(r["problem"] for _, r in rows)
    L = ["| Disposition | Items |", "|---|---:|"] + [f"| `{k}` | {d[k]} |" for k in DISP_ORDER if d[k]]
    L += ["", "| Main problem | Items |", "|---|---:|"] + [f"| `{k}` | {v} |" for k, v in p.most_common()]
    out["dispositions"] = "\n".join(L) + "\n"
    # Skill links with reach and strongest evidence.
    reach, p0 = Counter(), Counter()
    for i, r in rows:
        for s in r["skill"]:
            reach[s] += 1
            p0[s] += r["priority"] == "P0"
    L = ["| Code | Skill content | Items linked | P0 items | Platforms |", "|---|---|---:|---:|---|"]
    for s in sorted(SKILL_NAMES, key=lambda s: -reach[s]):
        plats = Counter(i["platform"] for i, r in rows if s in r["skill"])
        L.append(f"| {s} | {SKILL_NAMES[s]} | {reach[s]} | {p0[s]} | " + ", ".join(f"{k} {v}" for k, v in sorted(plats.items())) + " |")
    out["skills"] = "\n".join(L) + "\n"
    # P0 list.
    L = ["| Item | Cell | Lane · decision | Problem | Disposition | Diagnosis |", "|---|---|---|---|---|---|"]
    for i, r in sorted(rows, key=lambda x: (x[1]["priority"], x[0]["platform"], x[0]["lane"], x[0]["id"])):
        if r["priority"] == "P0":
            L.append(f"| `{i['id']}` | {i['platform']} {i['framework']} | {i['lane']} · {i['decision'] or '—'} | "
                     f"{r['problem']} | {r['disposition']} | {esc(r['diagnosis'])} |")
    out["p0"] = "\n".join(L) + "\n"
    # Every item, grouped by platform and lane.
    L = []
    for plat in ("iOS", "macOS", "tvOS"):
        L += [f"### {plat}", ""]
        for lane in LANES:
            rs = sorted([(i, r) for i, r in rows if i["platform"] == plat and i["lane"] == lane], key=lambda x: x[0]["id"])
            if not rs:
                continue
            L += [f"#### {plat} · {lane} ({len(rs)})", ""]
            for i, r in rs:
                audit = f" Blind audit {i['audit']['mask']}: {i['audit']['blindWhole']}/{i['audit']['blindPrimary']}." if i["audit"] else ""
                pair = f" Pair: {i['pair']['outcome']}." if i["pair"] else ""
                L += [f"**`{i['id']}`** · {i['framework']} · {i['decision'] or 'open rubric'} · unaided **{i['verdict']}** "
                      f"(primary {i['primary']}).{audit}{pair} · **{r['priority']} {r['disposition']}** · {r['problem']}"
                      + (f" · {', '.join(r['skill'])}" if r["skill"] else ""), "",
                      f"> {esc(i['opening'])}", "",
                      f"- **Diagnosis:** {r['diagnosis']}",
                      f"- **Prompt:** {r['promptChange']}"]
                if r.get("proposedWording"):
                    L.append(f"- **Proposed wording:** {r['proposedWording']}")
                L += [f"- **Oracle:** {r['oracleChange']}",
                      f"- **Skill:** {r['skillWhy']}",
                      f"- **Transfer:** {r['transfer']}", ""]
    out["items"] = "\n".join(L)
    return out


def main():
    items = {i["id"]: i for i in json.loads((HERE / "items.json").read_bytes())["items"]}
    recs = {}
    for name in ("ios", "macos", "tvos"):
        for r in json.loads((HERE / "shards" / f"{name}.json").read_bytes()):
            recs[r["id"]] = r
    doc = HERE / "PROMPT-IMPROVEMENTS.md"
    text = doc.read_text()
    for marker, body in generated(items, recs).items():
        new, n = re.subn(rf"(<!-- {marker}:begin -->\n).*?(<!-- {marker}:end -->)", lambda m: m.group(1) + body + m.group(2), text, flags=re.S)
        assert n == 1, f"marker {marker} missing"
        text = new
    doc.write_text(text)
    print(f"rendered {len(recs)} items")


if __name__ == "__main__":
    main()

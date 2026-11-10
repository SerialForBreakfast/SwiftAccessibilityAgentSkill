"""Render the generated sections of SKILL-DEVELOPMENT-STRATEGY.md from items.json and the shards.

  python3 -B research/evaluation/skill-strategy-v1/render.py
Text between <!-- name:begin --> and <!-- name:end --> is replaced; everything else is hand-written.
verify.py checks that the document matches.
"""
from collections import Counter
import json
from pathlib import Path
import re
import sys

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
DOC = HERE / "SKILL-DEVELOPMENT-STRATEGY.md"
GAP_ORDER = ["harmful-instruction", "content-gap", "not-opened", "verification-gap", "rework", "question-defect",
             "oracle-defect", "variance", "unmeasured", "sound-control"]
# What the signal-v2 evidence implies for a discovery decision, by the skill code the earlier review linked.
V2_IMPLICATION = {
    "S3": "Apply the capture-at-install rule (return.md rewrite; actions.md AppKit and invocation-time checks).",
    "S4": "Apply the makeFirstResponder fallback and per-presentation dismissal rules; add focus trigger terms.",
    "S7": "Apply the concrete media path (item, asset group, select, read back) and request-scoped picker setter.",
    "S8": "Add native-control facts (Slider, Reduce Motion, selected trait) to stop rewrites of working code.",
    "S5": "Keep and extend facts.md; single named facts produced the clearest rescues.",
    "S2": "Use the check shapes: second configuration, real handler, independently named fixtures.",
    "S1": "Entry review sentence already helps; it only works when the skill is opened.",
    "S6": "No v2 evidence; leave text-offset guidance on demand.",
}
esc = lambda s: (s or "").replace("|", "\\|").replace("\n", " ")


def load():
    items = json.loads((HERE / "items.json").read_bytes())
    recs = {}
    for name in ("tier1", "tier2"):
        p = HERE / "shards" / f"{name}.json"
        if p.exists():
            for r in json.loads(p.read_bytes()):
                recs[r["id"]] = r
    return items, recs


def comp(g):
    if not g:
        return "unavailable"
    short = {"pass": "✓", "fail": "✗", "na": "–", "unknown": "?"}
    return " ".join(short.get(g[c], g[c]) for c in ("primary", "preservation", "verification", "integration", "rework", "whole")) + (" ⚠" if g["critical"] else "")


def entry(i, r, tier):
    L = []
    if tier == 1:
        cards = ", ".join(c.replace("references/", "") for c in i["cardsRead"]) or "nothing read"
        cross = "".join(f" Also {k}: `{i[v]}`." for k, v in (("gold-parity", "alsoGoldParity"), ("OS26", "alsoOS26")) if i.get(v))
        L.append(f"**`{i['id']}`** · {i['platform']} {i['framework']} · {i['family']} · axis {i['axis']} · "
                 f"whole **{i['transitions']['whole']}**, primary {i['transitions']['primary']} · read: {cards} · "
                 f"**{r['priority']} {r['gapType']}** · v3 {r['v3Covers']}.{cross}")
        L += ["", f"> {esc(i['opening'])}", "",
              f"- **Grades** (primary, preservation, verification, integration, rework, whole; ⚠ critical): "
              f"unaided {comp(i['unaided'])} · installed {comp(i['skill'])}"]
    else:
        ev = (f"gates: {', '.join(i['gates'])}" if i["set"] == "os26"
              else "criteria: " + ", ".join(f"{k} {v}" for k, v in sorted(i["coverage"].items())))
        prior = i.get("prior384") or {}
        L.append(f"**`{i['id']}`** · {i['set']} · {i['platform']} {i['framework']} · {i['family']} · "
                 f"384 unaided **{prior.get('verdict', 'not in 384')}** · {ev} · **{r['priority']} {r['gapType']}** · v3 {r['v3Covers']}")
        if i.get("opening"):
            L += ["", f"> {esc(i['opening'])}"]
        L.append("")
    L += [f"- **Diagnosis:** {r['diagnosis']}",
          f"- **Question:** {r['questionChange']}"]
    if r.get("proposedWording"):
        L.append(f"- **Proposed wording:** {r['proposedWording']}")
    L += [f"- **Oracle:** {r['oracleChange']}",
          f"- **Skill:** {r['skillChange']}",
          f"- **Routing:** {r['routingChange']}", ""]
    return L


def generated(items, recs):
    out = {}
    t1 = [(i, recs[i["id"]]) for i in items["tier1"] if i["id"] in recs]
    t2 = [(i, recs[i["id"]]) for i in items["tier2"] if i["id"] in recs]
    rows = t1 + t2
    # Gap types by tier.
    L = ["| Gap type | Tier 1 | Tier 2 | P0 |", "|---|---:|---:|---:|"]
    for g in GAP_ORDER:
        a, b = sum(r["gapType"] == g for _, r in t1), sum(r["gapType"] == g for _, r in t2)
        if a or b:
            L.append(f"| `{g}` | {a} | {b} | {sum(r['gapType'] == g and r['priority'] == 'P0' for _, r in rows)} |")
    out["gaps"] = "\n".join(L) + "\n"
    # Card-level read and outcome table from Tier 1.
    cards = Counter()
    outcome = {}
    for i, _ in t1:
        if not i["skill"]:
            continue
        reads = [c.replace("references/", "") for c in i["cardsRead"] if c.startswith("references/")] or (["SKILL.md only"] if i["cardsRead"] else ["nothing read"])
        for c in reads:
            o = outcome.setdefault(c, Counter())
            o["answers"] += 1
            o[i["transitions"]["whole"]] += 1
            o["pass"] += i["skill"]["whole"] == "pass"
            o["critical"] += bool(i["skill"]["critical"])
    L = ["| Card read by the installed answer | Answers | Installed whole pass | Gains | Both fail | Critical flags |", "|---|---:|---:|---:|---:|---:|"]
    for c, o in sorted(outcome.items(), key=lambda kv: -kv[1]["answers"]):
        L.append(f"| {c} | {o['answers']} | {o['pass']} | {o['gain']} | {o['both-fail']} | {o['critical']} |")
    out["cards"] = "\n".join(L) + "\n"
    # P0 list.
    L = ["| Item | Cell | Family | Gap | Skill change |", "|---|---|---|---|---|"]
    for i, r in sorted(rows, key=lambda x: (x[1]["gapType"], x[0]["id"])):
        if r["priority"] == "P0":
            L.append(f"| `{i['id']}` | {i['platform']} {i['framework']} | {i['family']} | {r['gapType']} | {esc(r['skillChange'])} |")
    out["p0"] = "\n".join(L) + "\n"
    # Per-item entries.
    L = []
    for fam in sorted({i["family"] for i, _ in t1}):
        L += [f"#### {fam}", ""]
        for i, r in sorted([x for x in t1 if x[0]["family"] == fam], key=lambda x: x[0]["id"]):
            L += entry(i, r, 1)
    out["tier1"] = "\n".join(L)
    L = []
    for s, title in (("os26", "OS26 gold prompts"), ("gold-parity", "Gold-parity scenarios")):
        L += [f"#### {title}", ""]
        for i, r in sorted([x for x in t2 if x[0]["set"] == s], key=lambda x: x[0]["id"]):
            L += entry(i, r, 2)
    out["tier2"] = "\n".join(L)
    # Tier 3 rollup.
    L = ["| Decision key | Items | Unaided pass / fail / inconclusive | Main dispositions | P0 / P1 | Skill codes | What v2 evidence implies |",
         "|---|---:|---|---|---|---|---|"]
    for t in items["tier3"]:
        v, d, p, s = t["verdict"], t["disposition"], t["priority"], t["skill"]
        top = ", ".join(f"{k} {n}" for k, n in sorted(d.items(), key=lambda kv: -kv[1])[:2])
        codes = sorted(s, key=lambda k: -s[k])
        imp = V2_IMPLICATION.get(codes[0], "") if codes else "Question or oracle work only."
        L.append(f"| {t['decision']} | {t['items']} | {v.get('pass', 0)} / {v.get('fail', 0)} / {v.get('inconclusive', 0)} | {top} | "
                 f"{p.get('P0', 0)} / {p.get('P1', 0)} | {', '.join(codes) or '—'} | {imp} |")
    out["tier3"] = "\n".join(L) + "\n"
    return out


def main():
    items, recs = load()
    text = DOC.read_text()
    for marker, body in generated(items, recs).items():
        text, n = re.subn(rf"(<!-- {marker}:begin -->\n).*?(<!-- {marker}:end -->)", lambda m: m.group(1) + body + m.group(2), text, flags=re.S)
        assert n == 1, f"marker {marker} missing"
    DOC.write_text(text)
    print(f"rendered {len(recs)} recommendations")


if __name__ == "__main__":
    main()

"""Build the case-level failure inventory from every preserved graded run. Offline; no model calls.

  python3 -B research/evaluation/failure-inventory/build.py           rebuild inventory.json + README.md
  python3 -B research/evaluation/failure-inventory/build.py --check   fail if either file differs

Public sources are read from the repo. Private returns are read with zipfile, never extracted, from
ignored evals/results/ copies. Without them the private sources are listed as unavailable and --check
requires the same evidence set. Raw answers are never copied into outputs; reasons are reviewer text.
"""
import argparse
from collections import Counter, defaultdict
from hashlib import sha256
import json
from pathlib import Path
import re
import sys
from zipfile import ZipFile

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
PRIV = ROOT / "evals/results"
OUT_JSON, OUT_MD = HERE / "inventory.json", HERE / "README.md"
sys.path.insert(0, str(HERE))
from cases import CASES, WORKSTREAMS, TARGET_MODEL, MODEL_TIER, EXCLUDED

obs, sources = [], []


def add(source, case, model, condition, verdict, grader, reason="", run=None, repeat=None, criteria=None):
    assert case in CASES, f"unclassified case {case} from {source}"
    if not isinstance(reason, str):
        reason = (reason.get("reason") or reason.get("summary") or json.dumps(reason, sort_keys=True)) if isinstance(reason, dict) else str(reason)
    v = {"material-gap": "fail", "contract-failure": "fail", "compile-failure": "fail",
         "meets": "pass", "pass": "pass", "not-assessable": "inconclusive", "inconclusive": "inconclusive"}[verdict]
    obs.append(dict(source=source, case=case, model=model, condition=condition, verdict=v, raw=verdict,
                    grader=grader, reason=reason.strip(), run=run, repeat=repeat,
                    failedCriteria=criteria or []))


def src(name, path, private, available, note):
    sources.append(dict(id=name, path=str(path), private=private, available=available, note=note))


def private_zip(rel):
    p = PRIV / rel
    return (ZipFile(p), p) if p.exists() else (None, p)


# S1. Nov 5 Haiku baseline: per-answer reviewer findings, C0 unaided vs C2 0.2.2 + supplied reference.
def s1():
    p = ROOT / "evals/reports/claude-haiku-20261105/README.md"
    case, n = None, 0
    for line in p.read_text().splitlines():
        if line.startswith("### "):
            case = line[4:].strip()
        m = re.match(r"^- \*\*(C0|C2) r(\d) · (meets|material-gap|not-assessable)\*\* — (.*)$", line)
        if m and case in CASES:
            cond = "unaided" if m.group(1) == "C0" else "context:0.2.2+reference"
            add("S1", case, "claude-haiku-5-5", cond, m.group(3), "source-unmasked", m.group(4),
                run="claude-haiku-baseline-20261105", repeat=int(m.group(2)))
            n += 1
    assert n == 84, n
    src("S1", p.relative_to(ROOT), False, True, "84 Haiku answers, 12 code cases x 3 repeats and 6 evidence cases x 1 repeat, each in C0 and C2")


# S2. Nov 5 Flash (AGY) baseline: per-case counts out of 3 with a short reviewer note.
def s2():
    p = ROOT / "evals/reports/agy-expanded-20261105/README.md"
    n = 0
    for line in p.read_text().splitlines():
        m = re.match(r"^\| (GP26-\d\d) · [^|]+\| (\d)/3 \| (\d)/3 \| ([^|]*)\|", line)
        if not m:
            continue
        for cond, k in (("unaided", int(m.group(2))), ("context:0.2.2+reference", int(m.group(3)))):
            for r in range(3):
                add("S2", m.group(1), "gemini-3.8-flash-low", cond, "meets" if r < k else "material-gap",
                    "source-unmasked", m.group(4), run="agy-expanded-20261105", repeat=None)
                n += 1
    assert n == 72, n
    src("S2", p.relative_to(ROOT), False, True, "Flash low, 12 code cases ×3, C0 vs C2; counts only, no per-answer mapping")


# S3. dev.5 vs dev.7 (supplied candidate context): private per-answer, per-criterion grades.
def s3():
    z, p = private_zip("failure-inventory/bundles/dev7-flash-haiku-controller-return-r1.zip")
    if not z:
        return src("S3", p.relative_to(ROOT), True, False, "private return not present")
    rows = json.loads(z.read("answers-and-grades.json"))
    for r in rows:
        g = r["grade"]
        model = {"gemini": "gemini-3.8-flash-low", "claude": "claude-haiku-5-5"}[r["provider"]]
        failed = [c["id"].split("/")[-1] + ": " + c["reason"] for c in g["criteria"] if c["verdict"] != "meets"]
        add("S3", r["case"], model, "context:" + r["arm"].replace("dev", "0.3.0-dev."), g["core"],
            "source-masked-besteffort", g.get("integration", ""), run="dev7-comparison-1e568ed", criteria=failed)
    assert len(rows) == 62
    src("S3", p.relative_to(ROOT), True, True, "62 answers: Flash 24 cases and Haiku 7 cases, dev.5 vs dev.7 context")


# S4. Argon high controlled run: generic vs supplied dev.5 context; task transitions only.
def s4():
    p = ROOT / "research/evaluation/gemini-controlled-run-20261107/summary.json"
    split = {"preserved-meets": ("meets", "meets"), "gap-to-meets": ("material-gap", "meets"),
             "meets-to-gap": ("meets", "material-gap"), "preserved-material-gap": ("material-gap", "material-gap"),
             "inconclusive-pair": ("inconclusive", "inconclusive")}
    for r in json.loads(p.read_bytes())["pair_rows"]:
        a, b = split[r["reviewer_task_transition"]]
        add("S4", r["case"], "gemini-4-argon-high", "unaided", a, "source-unmasked", run="gemini-controlled-20261107")
        add("S4", r["case"], "gemini-4-argon-high", "context:0.3.0-dev.5", b, "source-unmasked", run="gemini-controlled-20261107")
    src("S4", p.relative_to(ROOT), False, True, "Argon high, 24 cases, generic vs dev.5 context; transitions only")


# S5. dev.1 vs dev.2 (supplied context), Flash and Haiku, 7 GP26 cases each.
def s5():
    p1 = ROOT / "evals/reports/skill-0.3.0-dev.1-vs-0.3.0-dev.2-20261106/summary.json"
    for c in json.loads(p1.read_bytes())["cases"]:
        for v in ("0.3.0-dev.1", "0.3.0-dev.2"):
            add("S5", c["case"], "gemini-3.8-flash-low", "context:" + v, c[v]["core"], "source-unmasked", run="dev1-dev2-20261106")
    p2 = ROOT / "evals/reports/skill-0.3.0-dev.1-vs-0.3.0-dev.2-claude-20261106/summary.json"
    for case, by in json.loads(p2.read_bytes())["cases"].items():
        for v, verdict in by.items():
            add("S5", case, "claude-haiku-5-5", "context:" + v, verdict, "source-unmasked", run="dev1-dev2-claude-20261106")
    src("S5", p1.relative_to(ROOT), False, True, "Flash and Haiku, 7 cases, dev.1 vs dev.2 context (AGY native re-grades of the same answers not double counted)")


# S6. Native activation lift: Haiku, installed skill, automatic discovery (nothing invoked).
def s6():
    p = ROOT / "evals/reports/native-activation-lift-20261106/summary.json"
    for r in json.loads(p.read_bytes())["rows"]:
        if r["lane"] != "accessibility":
            continue
        cond = "unaided" if r["condition"] == "generic" else "installed-auto:" + r["condition"]
        invoked = r["successful_skill_loads"] > 0
        add("S6", r["case"], "claude-haiku-5-5", cond if invoked or cond == "unaided" else cond + " (not invoked)",
            r["source_quality"]["core"], "source-masked-besteffort", run="native-activation-lift-20261106")
    src("S6", p.relative_to(ROOT), False, True, "Haiku, 3 accessibility cases × generic, installed 0.2.2, installed dev.2; none invoked")


# S7. rc.1 vs 0.2.2: sealed source grades and diagnostic native grades (public summary).
def s7():
    p = ROOT / "evals/rc1-comparison/summary.json"
    s = json.loads(p.read_bytes())
    for r in s["sealed"]:
        if r["state"] == "completed":
            cond = ("installed-explicit:" if r["lane"] == "explicit" else "installed-auto:") + r["arm"]
            add("S7", "rc1/" + r["task"], "claude-haiku-5-5", cond + ("" if r["invoked"] else " (not invoked)"),
                r["source"], "source-masked-besteffort", run="rc1-sealed-v1")
    for r in s["diagnostic"]:
        cond = ("installed-explicit:" if r["lane"] == "explicit" else "installed-auto:") + r["arm"]
        add("S7", "rc1/" + r["task"], "claude-haiku-5-5", cond + ("" if r["invoked"] else " (not invoked)"),
            r["native"], "native-units",
            "" if r["native"] == "pass" else f"hidden unit contract failed natively; masked source review had said {r['source']}",
            run="rc1-diagnostic-v2")
    src("S7", p.relative_to(ROOT), False, True, "Haiku, 12 one-function tasks; sealed 9 source-graded, diagnostic 36 natively graded")


# S8. Explicit rc.1 replay of seven historical failures, plus its Haiku compact-candidate controls.
def s8():
    z, p = private_zip("rc1-failure-replay-20261107/bundles/rc1-failure-replay-seven-return.zip")
    if not z:
        return src("S8", p.relative_to(ROOT), True, False, "private return not present")
    grades = json.loads(z.read("grades.json"))
    for case, g in grades.items():
        add("S8", case, "claude-haiku-5-5", "installed-explicit:0.3.0-rc.1", g["verdict"], "source-unmasked",
            g["reason"], run="rc1-failure-replay-seven")
    for case, c in json.loads(z.read("controller.json"))["cases"].items():
        for ctl in c["controls"]:
            if ctl["run"].startswith("compact-a-development144"):
                add("S8", case, "claude-haiku-5-5", "context:compact-a", ctl["grade"], "source-unmasked",
                    run=ctl["run"])
    src("S8", p.relative_to(ROOT), True, True, "Haiku explicit rc.1 on 7 cases; plus compact-candidate-A controls")


# S9. GP26-03 first type-checks of preserved answers (model/condition mapping not opened).
def s9():
    z, p = private_zip("failure-inventory/bundles/swift-checkout-first-review-20261106-r1.zip")
    if not z:
        return src("S9", p.relative_to(ROOT), True, False, "private return not present")
    for c in json.loads(z.read("sanitized-results.json"))["cases"]:
        add("S9", "GP26-03", "unmapped", "unmapped", c["status"], "native-typecheck", run="checkout-first-review-20261106")
    src("S9", p.relative_to(ROOT), True, True, "8 GP26-03 answers type-checked natively; mapping to model/condition not opened")


def summarize():
    by = defaultdict(list)
    for o in obs:
        by[o["case"]].append(o)
    rows = []
    for case, os_ in by.items():
        meta = CASES[case]
        cnt = lambda pred: Counter(o["verdict"] for o in os_ if pred(o))
        target = lambda o: o["model"] == TARGET_MODEL
        # Skill content reached the model only if supplied in context or actually invoked.
        no_skill = lambda o: o["condition"] == "unaided" or o["condition"].endswith("(not invoked)")
        hu, hs = cnt(lambda o: target(o) and no_skill(o)), cnt(lambda o: target(o) and not no_skill(o))
        other = cnt(lambda o: o["model"] != TARGET_MODEL)
        native_fail = any(o["verdict"] == "fail" and o["grader"].startswith("native") for o in os_)
        models_failing = sorted({o["model"] for o in os_ if o["verdict"] == "fail"})
        reasons = [f"{o['model'].split('-')[1]} {o['condition']}: {o['reason'][:180]}" for o in os_
                   if o["verdict"] == "fail" and o["reason"]][:4]
        crit = Counter(c.split(":")[0] for o in os_ for c in o["failedCriteria"])
        if hs["fail"] and hu["pass"] and not hu["fail"]:
            disposition = "fix: possible regression (target passes without skill content, fails with it; attribution untested)"
        elif hs["fail"]:
            disposition = "fix: fails on the target model even with skill guidance"
        elif hu["fail"]:
            disposition = "fix-or-confirm: fails unaided on the target model; skill arm passed or untested"
        elif other["fail"]:
            disposition = "credible: fails on another model only; needs a target-model observation"
        elif not (hu["pass"] or hs["pass"] or other["pass"]):
            disposition = "insufficient evidence"
        else:
            disposition = "preserve: passing control"
        rank = (2 * hs["fail"] + 2 * hu["fail"] + other["fail"] + (3 if native_fail else 0)
                + (2 if len(models_failing) > 1 else 0))
        rows.append(dict(case=case, title=meta["title"], platform=meta["platform"], framework=meta["framework"],
                         workstream=meta["workstream"], tags=meta.get("tags", []), disposition=disposition,
                         targetUnaided=dict(hu), targetWithSkill=dict(hs), otherModels=dict(other),
                         nativeFailure=native_fail, modelsFailing=models_failing, rank=rank,
                         failingCriteria=dict(crit), exampleReasons=reasons,
                         observations=len(os_), sources=sorted({o["source"] for o in os_})))
    rows.sort(key=lambda r: (-r["rank"], r["case"]))
    return rows


def coverage(rows):
    cells = defaultdict(lambda: Counter())
    for r in rows:
        key = f"{r['platform']} {r['framework']}"
        d = r["disposition"].split(":")[0]
        cells[key][{"fix": "observed failure (target)", "fix-or-confirm": "observed failure (target)",
                    "credible": "other-model failure only", "preserve": "passing control",
                    "insufficient evidence": "insufficient"}[d]] += 1
    # Credible risks: qualified package prompts with hidden tests and negative fixtures, no model run yet.
    for m in sorted((ROOT / "code-examples").glob("*/*/manifest.json")):
        pkg = m.parent
        prompts = len(list((pkg / "evaluation").glob("*.prompt.md"))) if (pkg / "evaluation").exists() else 0
        if not prompts:
            continue
        man = json.loads(m.read_bytes())
        plat = man.get("platform", "iOS")
        fw = "SwiftUI" if pkg.parent.name == "swiftui" else "AppKit" if "appkit" in pkg.name or plat == "macOS" and "uikit" not in pkg.name else "UIKit"
        cells[f"{plat} {fw}"]["package prompt, not yet run (credible risk)"] += prompts
    return {k: dict(v) for k, v in sorted(cells.items())}


def render(inv):
    L = ["# Failure inventory", "",
         "Generated by `python3 -B research/evaluation/failure-inventory/build.py`; do not edit by hand. "
         "Raw answers stay private; reasons are reviewer text.", "",
         f"**Target model for development: `{TARGET_MODEL}`** (owner decision, November 7). "
         "Other models are supporting evidence. A deliberate mutant proves a test can detect a defect, "
         "not that a model makes it, so package prompts that haven't been run count as credible risks, not failures.", "",
         "## Counts", "",
         "| Measure | Count |", "|---|---:|"]
    t = inv["totals"]
    for k in ("cases", "observations", "targetFixCases", "targetUnaidedOnlyCases", "otherModelOnlyCases",
              "passingControls", "insufficient", "nativeConfirmedCases"):
        L.append(f"| {k} | {t[k]} |")
    L += ["", "## Ranked cases", "",
          "Rank weighs target-model failures (unaided and with skill) above other models, then native confirmation and failures on more than one model.", "",
          "Target columns count Haiku answers. *Without skill content* includes sessions where the skill was installed but never invoked. *With skill content* means the skill was supplied in context or actually invoked. `(n?)` counts inconclusive answers.", "",
          "| # | Case | Cell | Workstream | Target without skill content (pass/fail) | Target with skill content (pass/fail) | Other models (pass/fail) | Native fail | Disposition |",
          "|---:|---|---|---|---|---|---|---|---|"]
    pf = lambda d: f"{d.get('pass', 0)}/{d.get('fail', 0)}" + (f" ({d['inconclusive']}?)" if d.get("inconclusive") else "")
    for i, r in enumerate(inv["cases"], 1):
        L.append(f"| {i} | `{r['case']}` {r['title']} | {r['platform']} {r['framework']} | {r['workstream']} | "
                 f"{pf(r['targetUnaided'])} | {pf(r['targetWithSkill'])} | {pf(r['otherModels'])} | "
                 f"{'yes' if r['nativeFailure'] else ''} | {'regression' if 'regression' in r['disposition'] else r['disposition'].split(':')[0]} |")
    L += ["", "## By workstream", "", "| Workstream | Cases with target failures | Cases with any failure | Passing controls |", "|---|---:|---:|---:|"]
    for w, name in WORKSTREAMS.items():
        rs = [r for r in inv["cases"] if r["workstream"] == w]
        L.append(f"| {w} {name} | {sum(r['disposition'].startswith('fix') for r in rs)} | "
                 f"{sum(r['disposition'].split(':')[0] in ('fix', 'fix-or-confirm', 'credible') for r in rs)} | "
                 f"{sum(r['disposition'].startswith('preserve') for r in rs)} |")
    L += ["", "## Coverage by cell", "", "Observed cases plus qualified package prompts not yet run against a model.", "",
          "| Cell | Observed failure (target) | Other-model failure only | Passing control | Package prompts not yet run |", "|---|---:|---:|---:|---:|"]
    for cell, c in inv["coverage"].items():
        L.append(f"| {cell} | {c.get('observed failure (target)', 0)} | {c.get('other-model failure only', 0)} | "
                 f"{c.get('passing control', 0)} | {c.get('package prompt, not yet run (credible risk)', 0)} |")
    # rc1/* are one-function regression controls; they don't count as realistic coverage.
    target_cells = {f"{r['platform']} {r['framework']}" for r in inv["cases"] if not r["case"].startswith("rc1/")
                    and sum(r["targetUnaided"].values()) + sum(r["targetWithSkill"].values())}
    blind = [cell for cell in inv["coverage"] if cell not in target_cells and "any" not in cell]
    L += ["", f"**Cells with no realistic-task observation on the target model:** {', '.join(blind) or 'none'}. "
          "The one-function rc.1 regression controls are excluded. In these cells, no target failures means "
          "not yet tested, not passing."]
    L += ["", "## Failing reasons, top cases", ""]
    for r in inv["cases"][:25]:
        if r["exampleReasons"]:
            L.append(f"- **`{r['case']}`**: " + " · ".join(r["exampleReasons"][:2]))
    L += ["", "## Sources", "", "| ID | Source | Private | Available | Note |", "|---|---|---|---|---|"]
    for s in inv["sources"]:
        L.append(f"| {s['id']} | `{s['path']}` | {'yes' if s['private'] else ''} | {'yes' if s['available'] else 'no'} | {s['note']} |")
    L += ["", "**Excluded:** " + "; ".join(EXCLUDED), ""]
    return "\n".join(L)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    for f in (s1, s2, s3, s4, s5, s6, s7, s8, s9):
        f()
    rows = summarize()
    totals = dict(cases=len(rows), observations=len(obs),
                  targetFixCases=sum(r["disposition"].startswith("fix:") for r in rows),
                  targetUnaidedOnlyCases=sum(r["disposition"].startswith("fix-or-confirm") for r in rows),
                  otherModelOnlyCases=sum(r["disposition"].startswith("credible") for r in rows),
                  passingControls=sum(r["disposition"].startswith("preserve") for r in rows),
                  insufficient=sum(r["disposition"].startswith("insufficient") for r in rows),
                  nativeConfirmedCases=sum(r["nativeFailure"] for r in rows))
    inv = dict(schema=1, targetModel=TARGET_MODEL, modelTiers=MODEL_TIER, totals=totals, cases=rows,
               coverage=coverage(rows), sources=sources,
               observationsSHA256=sha256(json.dumps(obs, sort_keys=True).encode()).hexdigest())
    text, md = json.dumps(inv, indent=2) + "\n", render(inv)
    if args.check:
        ok = OUT_JSON.read_text() == text and OUT_MD.read_text() == md
        print("PASS: inventory matches sources" if ok else "FAIL: inventory differs from sources; rebuild")
        sys.exit(0 if ok else 1)
    OUT_JSON.write_text(text)
    OUT_MD.write_text(md)
    print(json.dumps(totals))


if __name__ == "__main__":
    main()

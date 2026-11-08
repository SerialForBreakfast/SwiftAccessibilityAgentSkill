"""Regenerate the Flash scorecard with Matplotlib using public result summaries."""
import json
import os
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
cache = ROOT / "evals/results/chart-cache"
cache.mkdir(parents=True, exist_ok=True)
os.environ.setdefault("MPLCONFIGDIR", str(cache))
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

baseline = json.loads((HERE / "baseline-metrics.json").read_text())
comparison = json.loads((ROOT / "research/evaluation/dev7-flash-haiku-results-20261107/summary.json").read_text())["outcomes"]["gemini"]
older, newer = (comparison["arms"][k] for k in ("dev5", "dev7"))
pairs = comparison["paired_outcomes"]
assert older["completed"] == newer["completed"] == sum(pairs.values())
n = sum(baseline["grades"].values())
paper, ink, muted = "#FAF9F5", "#172B3A", "#435766"
good, gap, uncertain, track = "#00726A", "#AF493B", "#677581", "#DFE5E3"
fig = plt.figure(figsize=(11, 8.3), facecolor=paper)
axes = fig.add_axes([0, 0, 1, 1], xlim=(0, 1), ylim=(0, 1))
axes.set_axis_off()

def label(x, y, value, size=12, color=ink, weight="normal"):
    axes.text(x, y, value, fontsize=size, color=color, fontweight=weight, va="center")

def bar(x, y, w, h, color):
    axes.add_patch(Rectangle((x, y), w, h, color=color, linewidth=0))

label(.045, .93, "Gemini Flash Low  /  Accessibility evaluation", 24, weight="bold")
label(.045, .865, "First-answer source review  ·  AGY subscription  ·  reported input and output tokens", 12, muted)
bar(.045, .823, .91, .002, track)
current = json.loads((HERE / "audit-revision-1/results.json").read_text())
label(.045, .784, "Matched content experiment   /   17 shared questions", 17, weight="bold")
for x, title in ((.045,"Supplied guidance"),(.315,"Task passes"),(.51,"Primary behavior"),(.71,"Tokens"),(.83,"Gain / loss*")):
    label(x, .729, title, 11, muted)
for i,(arm,name) in enumerate((("unaided","Unaided"),("review","Review sentence"),("text","UIKit text note"),("both","Both additions"))):
    stat = current["arms"][arm]
    y = .677 - .055*i
    label(.045,y,name,12,weight="bold" if arm=="unaided" else "normal")
    bar(.315,y-.009,.104,.018,track)
    bar(.315,y-.009,.104*stat["whole"].get("P",0)/17,.018,good)
    label(.432,y,f"{stat['whole'].get('P',0)}/17",11)
    label(.51,y,f"{stat['primary'].get('P',0)}/17",12)
    label(.71,y,f"{stat['tokens']['total_tokens']:,}",12)
    pairs_now = stat["pairedVsUnaided"]
    label(.83,y,"—" if arm=="unaided" else f"+{pairs_now.get('gain',0)} / −{pairs_now.get('regression',0)}",12)
label(.045,.452,"*Whole-answer gains / regressions against the concurrent unaided answer.",11,muted)
bar(.045,.422,.91,.002,track)
label(.045,.381,f"Discovery baseline   /   {n} unaided questions",15,weight="bold")
x=.045
for key,color in zip(("pass","fail","inconclusive"),(good,gap,uncertain)):
    width=.91*baseline["grades"][key]/n
    bar(x,.321,width,.028,color)
    x+=width
label(.045,.285,"   ·   ".join(f"{count} {key}" for key,count in baseline["grades"].items()),12)
label(.64,.285,f"{baseline['tokens']:,} tokens",12)
bar(.045,.24,.91,.002,track)
label(.045,.20,"Historical skill versions   /   24 shared questions",15,weight="bold")
label(.045,.141,f"Dev.5   {older['source_grades']['meets']}/24 passed   ·   {older['reported_tokens']:,} tokens",12)
label(.54,.141,f"Dev.7   {newer['source_grades']['meets']}/24 passed   ·   {newer['reported_tokens']:,} tokens",12)
label(.045,.071,f"Dev.7 gained {pairs['gain']} and regressed on {pairs['regression']}; the full 384-question skill effect remains unmeasured.",12,muted)
fig.savefig(ROOT / "docs/images/gemini-scorecard.png", dpi=160, facecolor=paper)

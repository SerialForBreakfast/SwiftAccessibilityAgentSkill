"""Analyze a signal-v6-run1 return: trial-majority verdicts, paired sign tests, self-agreement, exposure, tokens.

  python3 -B research/evaluation/signal-panel-v6/analyze.py HELD.zip SEAL RETURN.zip [NATIVE.json] [--out summary.json]

Validates the return with readiness/check_return.py first. NATIVE.json, optional, maps
"id|arm|trial" -> {"primary": "pass"|"fail"} from native grading; it is reported separately. A narrow native check cannot clear a broader source failure.
Outputs counts only, never answer text.
"""
from collections import Counter, defaultdict
from math import comb
import json, sys, zipfile
from pathlib import Path

sys.dont_write_bytecode = True
D = Path(__file__).resolve().parent
sys.path.insert(0, str(D / "readiness"))
from check_return import verify

COMPONENTS = ("primary", "preservation", "integration", "verification", "rework", "whole")
CANDIDATE, BASELINES = "signal-v6", ("signal-v2", "unaided")


def sign_test(gains, losses):
    """Two-sided exact binomial test on discordant pairs."""
    n = gains + losses
    if n == 0:
        return 1.0
    k = min(gains, losses)
    return min(1.0, 2 * sum(comb(n, i) for i in range(k + 1)) / 2 ** n)


def majority(verdicts):
    """Require two votes from the scheduled three; one observation is not a majority."""
    c = Counter(v for v in verdicts if v in ("pass", "fail"))
    if c["pass"] >= 2:
        return "pass"
    if c["fail"] >= 2:
        return "fail"
    return "na" if verdicts and all(v == "na" for v in verdicts) else "unknown"


def analyze(held, seal, ret_path, native=None):
    check = verify(held, seal, ret_path)
    z = zipfile.ZipFile(ret_path)
    cells = json.loads(z.read("return.json"))["cells"]
    native = native or {}
    verdict = defaultdict(lambda: defaultdict(list))  # (id, arm) -> component -> [trial verdicts]
    opened, tokens, critical = Counter(), defaultdict(list), Counter()
    critical_by_cell = {}
    native_agreement = Counter()
    for c in cells:
        if c["state"] != "answered" or not c.get("grade"):
            continue
        key = (c["id"], c["arm"])
        g = {k: c["grade"][k]["verdict"] for k in COMPONENTS}
        n = native.get(f"{c['id']}|{c['arm']}|{c['trial']}")
        if n and n.get("primary") in ("pass", "fail"):
            native_agreement[(c["arm"], g["primary"], n["primary"])] += 1
        critical_by_cell[(c["id"], c["trial"], c["arm"])] = bool(c["critical"])
        for k in COMPONENTS:
            verdict[key][k].append(g[k])
        critical[c["arm"]] += bool(c["critical"])
        reads = json.loads(z.read(c["trace"]["path"])).get("reads", []) if c["arm"] != "unaided" else []
        opened[key] += any("SKILL.md" in str(r.get("path") if isinstance(r, dict) else r) for r in reads)
        usage = (json.loads(z.read(c["usage"]["path"])).get("usage") or {}).get("total_tokens")
        if usage:
            tokens[c["arm"]].append(usage)
    ids = sorted({k[0] for k in verdict})
    arms = sorted({k[1] for k in verdict})
    maj = {(i, a): {k: majority(verdict[i, a][k]) for k in COMPONENTS} for i in ids for a in arms if (i, a) in verdict}
    out = {"check": check, "questions": len(ids), "arms": {}, "paired": {}, "selfAgreement": {}}
    for a in arms:
        rows = [maj[i, a] for i in ids if (i, a) in maj]
        out["arms"][a] = {k: sum(r[k] == "pass" for r in rows) for k in COMPONENTS}
        out["arms"][a]["decided"] = {k: sum(r[k] in ("pass", "fail") for r in rows) for k in COMPONENTS}
        out["arms"][a]["critical"] = critical[a]
        t = sorted(tokens[a])
        out["arms"][a]["medianTokens"] = t[len(t) // 2] if t else None
        # Fraction of questions where every graded trial agrees on whole and on primary.
        full = [i for i in ids if len(verdict[i, a]["whole"]) >= 2]
        out["selfAgreement"][a] = {k: f"{sum(len(set(verdict[i, a][k])) == 1 for i in full)}/{len(full)}" for k in ("whole", "primary")}
        if a != "unaided":
            out["arms"][a]["openedCells"] = sum(opened[i, a] for i in ids)
    for base in BASELINES:
        if CANDIDATE not in arms or base not in arms:
            continue
        res = {}
        for k in ("whole", "primary", "verification", "preservation"):
            gains = [i for i in ids if (maj.get((i, base)) or {}).get(k) == "fail" and (maj.get((i, CANDIDATE)) or {}).get(k) == "pass"]
            losses = [i for i in ids if (maj.get((i, base)) or {}).get(k) == "pass" and (maj.get((i, CANDIDATE)) or {}).get(k) == "fail"]
            res[k] = {"gains": len(gains), "losses": len(losses), "p": round(sign_test(len(gains), len(losses)), 4),
                      "gainIds": gains, "lossIds": losses}
        out["paired"][f"{CANDIDATE} vs {base}"] = res
    # Exposure split for v6 vs v2: did the skill open in a majority of v6 trials?
    if CANDIDATE in arms and "signal-v2" in arms:
        split = defaultdict(Counter)
        for i in ids:
            if any((i,a) not in maj or maj[i,a]["whole"] not in ("pass","fail") for a in (CANDIDATE,"signal-v2")):
                continue
            n6, n2 = len(verdict[i, CANDIDATE]["whole"]), len(verdict[i, "signal-v2"]["whole"])
            e = ("v6" if opened[i, CANDIDATE] * 2 > n6 else "") + ("v2" if opened[i, "signal-v2"] * 2 > n2 else "")
            b, c = maj[i, "signal-v2"]["whole"], maj[i, CANDIDATE]["whole"]
            split[e or "neither"][{("fail", "pass"): "gain", ("pass", "fail"): "loss"}.get((b, c), "same")] += 1
        out["exposureWhole"] = {k: dict(v) for k, v in split.items()}
    gate = out["paired"].get(f"{CANDIDATE} vs signal-v2", {}).get("whole", {})
    gate_u = out["paired"].get(f"{CANDIDATE} vs unaided", {}).get("whole", {})
    losses = sorted((i,t) for (i,t,a), flagged in critical_by_cell.items()
                    if a == CANDIDATE and flagged and critical_by_cell.get((i,t,"signal-v2")) is False)
    out["newCriticalVsV2"] = losses
    out["nativeByArmSourcePrimaryAndNative"] = {"|".join(k):v for k,v in sorted(native_agreement.items())}
    decided = all(maj.get((i,a),{}).get("whole") in ("pass","fail") for i in ids for a in (*BASELINES,CANDIDATE))
    out["panelGate"] = bool(check["status"]=="complete" and decided and not losses and gate and gate_u and gate["gains"] > gate["losses"] and gate["p"] < 0.05
                            and gate_u["gains"] > gate_u["losses"] and gate_u["p"] < 0.05
                            and critical[CANDIDATE] <= critical.get("signal-v2", 0))
    return out


if __name__ == "__main__":
    import argparse
    parser=argparse.ArgumentParser(description=__doc__)
    for key in ("held","seal","returned"): parser.add_argument(key)
    parser.add_argument("native",nargs="?",type=Path)
    parser.add_argument("--out",type=Path)
    args=parser.parse_args()
    result=analyze(args.held,args.seal,args.returned,json.loads(args.native.read_bytes()) if args.native else None)
    text=json.dumps(result,indent=1,sort_keys=True)
    if args.out: args.out.write_text(text+"\n")
    print(text)

"""Read-only check of BigDog's rc.1 returns against the sealed packet and RESULT.md.

Reads the private copies under evals/results/rc1-return-20261107/bundles/ with zipfile.
Never extracts or executes bundle content. Exits non-zero on any mismatch.
"""
from collections import Counter
from hashlib import sha256
import json
from pathlib import Path
import sys
from zipfile import ZipFile

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[2]
BUNDLES = ROOT / "evals/results/rc1-return-20261107/bundles"
PACKET = ROOT / "evals/rc1-comparison/packet.json"
SUMS = {
    "rc1-release-native-36-v1-return.zip": "77f942cd11071cef336e49ff0977777dd6f3f9bbf499014a171812769c3a80fa",
    "rc1-release-native-chat-36-v2-return.zip": "9f7d0cea62392c12d343efe9b698bb205a444374087fa01d9da40a7511ce4cad",
    "rc1-failure-replay-handoff-return.zip": "4f08fcc6f717140e1e76602f7ac743e6daa52333765a24927fbcf5c7577cbae8",
}
SEALED_PACKET = "496c51e084498d3eb164cc5a74b0c6398ec654d9acc686212b526f6e492f69c2"
V2_PACKET = "46d576c8e89cfe37236c74d387350b04a61130f2ac7fbf0c4839b32f0aae05ca"
ARMS = ("0.2.2", "0.3.0-rc.1")


def bundle(name):
    data = (BUNDLES / name).read_bytes()
    assert sha256(data).hexdigest() == SUMS[name], name + " hash"
    z = ZipFile(BUNDLES / name)
    sums = json.loads(z.read("checksums.json"))
    items = sums.items() if isinstance(sums, dict) else [(e["path"], e["sha256"]) for e in sums]
    for path, digest in items:
        assert sha256(z.read(path)).hexdigest() == digest, name + ": " + path
    return z


def pairs(index, lane="automatic"):
    rows = {}
    for r in index:
        if r["lane"] == lane:
            rows.setdefault(r["task"], {})[r["arm"]] = r
    out = Counter()
    for task, by in rows.items():
        if len(by) < 2 or any(by[a]["state"] != "completed" for a in ARMS):
            out["incomplete"] += 1
            continue
        a, b = (by[x]["source_grade"] for x in ARMS)
        out["both-pass" if a == b == "meets" else "both-fail" if a == b else "gain" if b == "meets" else "loss"] += 1
    return out


def lanes(index):
    out = {}
    for r in index:
        if r["state"] != "completed":
            continue
        k = r["lane"] + " " + r["arm"]
        o = out.setdefault(k, Counter())
        o["completed"] += 1
        o["meets"] += r["source_grade"] == "meets"
        o["invoked"] += bool(r.get("invoked"))
        o["announced"] += bool(r.get("announced"))
        o["routing"] += bool(r.get("routing_reported"))
    return {k: dict(v) for k, v in sorted(out.items())}


def main():
    sealed = json.loads(PACKET.read_bytes())
    assert sha256(PACKET.read_bytes()).hexdigest() == SEALED_PACKET
    sealed_prompts = {c["cell"]: c["promptSHA256"] for c in sealed["cells"]}
    v1, v2, replay = (bundle(n) for n in SUMS)
    for z in (v1, v2):
        assert sha256(z.read("evals/rc1-comparison/packet.json")).hexdigest() == SEALED_PACKET
    assert sha256(v2.read("controller/packet.json")).hexdigest() == V2_PACKET
    i1, i2 = (json.loads(z.read("index.json")) for z in (v1, v2))
    match = lambda idx: sum(r["promptSHA256"] == sealed_prompts[r["cell"]] for r in idx)

    # v1: the sealed run (first attempts).
    assert match(i1) == 36
    assert Counter(r["state"] for r in i1) == {"completed": 9, "attempt-error": 1, "unattempted": 26}
    assert pairs(i1) == {"both-pass": 4, "incomplete": 8}
    assert sum(bool(r.get("invoked")) for r in i1 if r["state"] == "completed") == 0

    # v2: a second job with rewritten prompts; every cell is a new session.
    assert match(i2) == 0
    assert Counter(r["state"] for r in i2) == {"completed": 36}
    by1 = {r["cell"]: r for r in i1}
    assert all(r["session_id"] != by1[r["cell"]].get("session_id") for r in i2)
    assert pairs(i2) == {"both-pass": 12}
    expected = {
        "automatic 0.2.2": dict(completed=12, meets=12, invoked=1, announced=0, routing=0),
        "automatic 0.3.0-rc.1": dict(completed=12, meets=12, invoked=1, announced=1, routing=1),
        "explicit 0.2.2": dict(completed=3, meets=3, invoked=3, announced=0, routing=0),
        "explicit 0.3.0-rc.1": dict(completed=3, meets=3, invoked=3, announced=3, routing=3),
        "repeat-automatic 0.2.2": dict(completed=6, meets=6, invoked=0, announced=0, routing=0),
    }
    assert lanes(i2) == expected, lanes(i2)
    s2 = json.loads(v2.read("summary.json"))
    refs = {k: v["references_read_sessions"] for k, v in s2["by_lane_and_version"].items()}
    assert refs == {"automatic 0.2.2": 0, "automatic 0.3.0-rc.1": 1, "explicit 0.2.2": 0,
                    "explicit 0.3.0-rc.1": 3, "repeat-automatic 0.2.2": 0}
    grades = [json.loads(v2.read(f"cells/{r['cell']}/grade.json")) for r in i2]
    assert sum(g["format_met"] for g in grades) == 0 and not any(g["critical"] for g in grades)
    first = {(r["task"], r["arm"]): r for r in i2 if r["lane"] == "automatic"}
    repeats = [r for r in i2 if r["lane"] == "repeat-automatic"]
    assert sum(r["source_grade"] == first[r["task"], r["arm"]]["source_grade"] for r in repeats) == 6
    assert s2["native_executions"] == 0

    # Checkout-font is the only task that ever auto-invoked; observations across both jobs.
    font = [(r["arm"], bool(r.get("invoked"))) for idx in (i1, i2) for r in idx
            if r["task"] == "checkout-font" and r["lane"] != "explicit" and r["state"] == "completed"]
    assert sorted(font) == [("0.2.2", False), ("0.2.2", False), ("0.2.2", True),
                            ("0.3.0-rc.1", False), ("0.3.0-rc.1", True)]

    assert "README.md" in replay.namelist() and "NEXT.md" in replay.namelist()
    print("PASS: 3 bundle hashes and internal checksums; v1 sealed 9/36 completed, 0 invoked;"
          " v2 rewritten-prompt 36/36, 12 both-pass, auto-invoked 1+1/24, explicit 6/6, repeats 6/6, 0 native.")


if __name__ == "__main__":
    main()

"""Usage: python3 check_return.py held.zip expected_packet_sha256 return.zip"""
import hashlib, json, sys
from pathlib import Path, PurePosixPath
from zipfile import ZipFile

H = lambda b: hashlib.sha256(b).hexdigest()


def need(ok, msg):
    if not ok:
        raise ValueError(msg)


def inventory(z):
    names = z.namelist()
    need(len(names) == len(set(names)) and all(not PurePosixPath(n).is_absolute() and ".." not in PurePosixPath(n).parts
                                               for n in names), "unsafe or duplicate members")


def verify(packet, seal, result):
    need(H(Path(packet).read_bytes()) == seal, "packet seal")
    with ZipFile(packet) as p, ZipFile(result) as z:
        inventory(p); inventory(z)
        hashes = json.loads(p.read("SHA256.json"))
        need(set(hashes) == set(p.namelist()) - {"SHA256.json"} and all(H(p.read(k)) == v for k, v in hashes.items()), "packet contents")
        expected = {(r["id"], r["arm"], r["trial"]): r for r in json.loads(p.read("schedule.json"))}
        m = json.loads(z.read("return.json"))
        need(m["packetSHA256"] == seal and m["job"] == "signal-v7-smoke1", "wrong job")

        def artifact(ref):
            b = z.read(ref["path"])
            need(b and H(b) == ref["sha256"], "missing or changed artifact")
            return b

        for k in ("report", "runLedger"):
            artifact(m[k])
        cells, answered, attempted, paths = {}, 0, 0, set()
        for c in m["cells"]:
            key = (c["id"], c["arm"], c["trial"])
            need(key in expected and key not in cells, "invalid or duplicate cell")
            cells[key] = c
            need(c["state"] in {"answered", "error", "unattempted"}, "state")
            need("grade" not in c or c["grade"] is None, "grades are not part of this job")
            if c["state"] == "unattempted":
                need(c["reason"] and c["attempts"] == 0, "unattempted")
                continue
            attempted += 1
            need(c["attempts"] == 1 and c["questionSHA256"] == expected[key]["questionSHA256"]
                 and c["skillSHA256"] == expected[key]["skillSHA256"], "attempt binding")
            for k in ("request", "receipt", "transport", "usage", "trace"):
                artifact(c[k])
            need(isinstance(json.loads(artifact(c["trace"])).get("reads"), list), "trace reads")
            if c["state"] == "error":
                artifact(c["error"])
                continue
            answered += 1
            artifact(c["answer"])
            need(c["answer"]["path"] not in paths, "reused answer path")
            paths.add(c["answer"]["path"])
        need(set(cells) == set(expected), "incomplete scheduled ledger")
        status = m["status"]
        need(status in {"complete", "partial", "blocked"}, "return status")
        if status == "complete":
            need(answered == len(expected), "incomplete complete return")
        else:
            need(m["stopReason"].strip(), "missing stop reason")
        if status == "blocked":
            need(not answered, "usable answers require partial return")
        return dict(status=status, planned=len(expected), attempted=attempted, answered=answered)


if __name__ == "__main__":
    print(json.dumps(verify(*sys.argv[1:]), indent=2))

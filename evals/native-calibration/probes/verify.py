"""Reconstruct the public index from private first receipts and actual XCTest lines."""
import argparse
import json
import re

from .run import BASE, HERE, METHODS, MODES, digest, subject


def check(value, message):
    if not value:
        raise ValueError(message)


def collect(batch, failed):
    first = BASE / failed / "macOS/positive"
    data = (first / "native.log").read_bytes()
    r = json.loads((first / "receipt.json").read_bytes())
    check(digest(data) == r["logSHA256"] and b'does not contain a scheme named "Probe"' in data
          and not r["tests"]["testAttachedRefusal"]["status"], "first harness outcome")
    out = []
    for platform, families in [("iOS", ["Field", "Sheet"]), ("tvOS", ["Field"]), ("macOS", ["Responder"])]:
        for family in families:
            method, marker = METHODS[family]
            runs = {}
            anchor = None
            for mode in MODES:
                cwd = BASE / batch / platform / mode
                receipt = (cwd / "receipt.json").read_bytes()
                row = json.loads(receipt)
                data = (cwd / "native.log").read_bytes()
                check(digest(data) == row["logSHA256"], "changed native log")
                for path, expected in row["inputs"].items():
                    check(digest((cwd / path).read_bytes()) == expected, path)
                env = {k:row[k] for k in ("platform","runtime","deployment","sdk","xcode")}
                env["destination"] = row["command"][row["command"].index("-destination")+1]
                check(anchor is None or anchor == env, "changed anchor")
                anchor = env
                check(row["platform"] == platform and row["variant"] == mode, "wrong variant")
                test = row["inputs"]["Tests/ProbeTests/"+family+".swift"]
                src = row["inputs"]["Sources/Probe/"+family+".swift"]
                check(src == digest(subject(platform,family,mode).encode()), "subject mismatch")
                check(test == digest((HERE/(family+".swift")).read_bytes()), "test mismatch")
                lines = data.decode(errors="replace").splitlines()
                statuses = [m[1] for line in lines if (m := re.search(r"Test Case '.* "+method+r"\]' (passed|failed)",line))]
                errors = [line for line in lines if ": error: " in line and " "+method+"]" in line]
                mutant = mode == "mutant"
                check(statuses == (["failed"] if mutant else ["passed"]), method)
                check(row["exit"] == (65 if mutant else 0), "unexpected exit")
                check(any(marker in line for line in errors) if mutant else not errors, "wrong diagnostic")
                runs[mode] = dict(status=statuses[0],subjectSHA256=src,receiptSHA256=digest(receipt))
            check(len({r["subjectSHA256"] for r in runs.values()}) == 3, "duplicate controls")
            out.append(dict(platform=platform, method=method, anchor=anchor, testSHA256=test,
                            diagnostic=marker, runs=runs))
    return dict(batch=batch, firstHarnessFailure=dict(batch=failed, logSHA256=r["logSHA256"],
                receiptSHA256=digest((first/"receipt.json").read_bytes())), probes=out)


def verified():
    saved = json.loads((HERE/"evidence.json").read_bytes())
    check(saved == collect(saved["batch"], saved["firstHarnessFailure"]["batch"]), "qualification index drift")
    return saved["probes"]


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--record", nargs=2, metavar=("BATCH", "FAILED_BATCH"))
    args = parser.parse_args()
    if args.record:
        result = collect(*args.record)
        with (HERE/"evidence.json").open("x") as f:
            f.write(json.dumps(result,indent=2)+"\n")
    else:
        print(len(verified()), "verified platform/probe controls")

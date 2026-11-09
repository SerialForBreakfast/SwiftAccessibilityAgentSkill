"""Recompute method outcomes from first native logs, not an aggregate failure count."""
import json
import re
import sys
from stage import BASE, D, H, PLATFORMS, VARIANTS, source

BATCH = "sheet-callback-d0p4j40r"


def collect():
    run = BASE / BATCH
    env = json.loads((run / "environment.json").read_bytes())
    rows = []
    for platform in PLATFORMS:
        for variant in VARIANTS:
            cell = run / f"P-{platform}-{variant}"
            meta = json.loads((cell / "input.json").read_bytes())
            inputs = meta["inputs"]
            assert inputs == {"Subject.swift": H(source(variant).encode()),
                              "Contract.swift": H((D / "CallbackTests.swift").read_bytes())}
            assert all(H((cell / p).read_bytes()) == h for p, h in inputs.items())
            receipt = json.loads((cell / "contract.json").read_bytes())
            intent = json.loads((cell / "contract-intent.json").read_bytes())
            assert (intent["source"], intent["checks"]) == (inputs["Subject.swift"], [inputs["Contract.swift"]])
            log = (cell / "contract.log").read_bytes()
            assert receipt["log"] == H(log)
            text = log.decode(errors="replace")
            methods = re.findall(r"Test Case '[^'\n]*testLateAThenBTwice\]' (\w+) \(", text)
            errs = [line for line in text.splitlines() if ": error:" in line]
            markers = ["late A must not consume B", "B must restore its own origin", "B may restore only once"] if variant == "shared" else []
            assert methods == (["failed"] if markers else ["passed"]), methods
            assert receipt["exit"] == (65 if markers else 0)
            assert len(errs) == len(markers) and all("late-A:row-B" in line and line.endswith(marker)
                                                     for line, marker in zip(errs, markers)), errs
            rows.append(dict(platform=platform, variant=variant, method=methods[0], markers=markers, inputs=inputs,
                             log=H(log), firstReceipt=H((cell / "contract.json").read_bytes())))
    return dict(batch=BATCH, anchors=env, results=rows)


if __name__ == "__main__":
    index = collect()
    path = D / "evidence.json"
    if sys.argv[1:] == ["--record"]:
        with path.open("x") as stream:
            stream.write(json.dumps(index, indent=2) + "\n")
    else:
        assert json.loads(path.read_bytes()) == index
    print("Verified three owned passes and three shared-ticket failures.")

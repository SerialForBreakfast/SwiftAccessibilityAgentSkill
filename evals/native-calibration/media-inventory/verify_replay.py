"""Rebuild the public answer index from immutable private inputs and method receipts."""
import json
import re
import sys

from replay_answers import BASE, D, H, PRIOR, contract

BATCH = "all-options-15f02kqe"
IDS = ("P-d4bd274c3a345669", "P-dc1e54ce99c97729")


def collect():
    index = []
    run = BASE / BATCH
    for batch, arms in [("tmp6xijam9k", ("unaided", "skill")),
                        ("v4-paired-jwlc74x4", ("signal-v2", "signal-v4"))]:
        for case in IDS:
            for arm in arms:
                name = f"{case}.{arm}"
                origin = BASE / batch / name
                original = json.loads((origin / "input.json").read_bytes())
                hashes = original["inputs"]
                for key in ("answer.txt", "question.txt", "Subject.swift"):
                    assert hashes[key] == H((origin / key).read_bytes())
                row = dict(origin=batch, case=case, arm=arm, platform=original["platform"],
                           answer=hashes["answer.txt"], question=hashes["question.txt"],
                           inventory="not exercised: no default native loader")
                if arm == "signal-v4":
                    cell = run / name
                    inputs = json.loads((cell / "input.json").read_bytes())["inputs"]
                    for key, digest in inputs.items():
                        assert digest == H((cell / key).read_bytes())
                    assert inputs["Subject.swift"] == H((PRIOR / name / "Subject.swift").read_bytes())
                    assert inputs["sample.mov"] == "c08c9e5d23f035221aedfd9004dde8873a1b9edeff1d21b45a73a4b5626f76f3"
                    assert (cell / "Contract.swift").read_text() == contract(row["platform"], cell / "sample.mov")
                    receipt = json.loads((cell / "contract.json").read_bytes())
                    log = (cell / "contract.log").read_bytes()
                    assert receipt["log"] == H(log) and receipt["exit"] == 65
                    methods = re.findall(rb"Test Case '-\[Checks.InventoryTests (\w+)\]' (passed|failed)", log)
                    assert methods == [(b"testLoadAndChooseEveryNativeOption", b"failed"),
                                       (b"testWritesWithPreloadedOptions", b"passed")]
                    assert len(receipt["diagnostics"]) == 1 and "inventory rejected: Duplicate track identifier" in receipt["diagnostics"][0]
                    row.update(inventory="native loader rejected duplicate keys", isolatedWriter="passed all options and audio readback",
                               inputs=inputs, log=H(log), receipt=H((cell / "contract.json").read_bytes()))
                index.append(row)
    return dict(batch=BATCH, environment=json.loads((run/"environment.json").read_bytes()), records=index)


if __name__ == "__main__":
    result = collect()
    dest = D / "answer-receipts.json"
    if sys.argv[1:] == ["--record"]:
        with dest.open("x") as stream:
            stream.write(json.dumps(result, indent=2) + "\n")
    else:
        assert result == json.loads(dest.read_bytes())
    print("Verified eight answer bindings and four executed method outcomes.")

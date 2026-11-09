"""Stage the unchanged answers and a setter-only ownership mutant per platform."""
import json
import re
import tempfile
from pathlib import Path
from replay_answers import BASE, D, PRIOR, QUALIFIED, H


def stage():
    batch = Path(tempfile.mkdtemp(prefix="picker-replacement-", dir=BASE))
    for old in sorted(PRIOR.glob("P-*.signal-v4")):
        row = json.loads((old / "input.json").read_bytes())
        source = (old / "Subject.swift").read_bytes()
        assert H(source) == row["inputs"]["Subject.swift"]
        asset = (QUALIFIED / row["platform"] / "ordinal/Tests/InventoryTests/sample.mov").read_bytes()
        assert H(asset) == "c08c9e5d23f035221aedfd9004dde8873a1b9edeff1d21b45a73a4b5626f76f3"
        for variant in ("original", "mutant"):
            cell = batch / (old.name + "." + variant)
            cell.mkdir()
            staged = source
            if variant == "mutant":
                staged, n = re.subn(rb'(set: \{ \[weak self\] \w+ in\s+guard let self), self\.generation == ticket,[^\n]+? else \{ return \}', rb'\1 else { return }', source)
                assert n == 1
            (cell / "Subject.swift").write_bytes(staged)
            (cell / "sample.mov").write_bytes(asset)
            (cell / "Contract.swift").write_text((D / "ReplacementTests.swift").read_text().replace("FIXTURE_PATH", str(cell / "sample.mov")))
            inputs = {p.name:H(p.read_bytes()) for p in cell.iterdir()}
            (cell / "input.json").write_text(json.dumps(dict(row, selection=variant, original=H(source), inputs=inputs), indent=2))
    return batch.name


if __name__ == "__main__":
    print(stage())

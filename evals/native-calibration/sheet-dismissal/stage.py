"""Use the candidate's exact compiled modifier and a separate shared-session control."""
import hashlib
import json
import tempfile
from pathlib import Path
from zipfile import ZipFile

D = Path(__file__).resolve().parent
ROOT = D.parents[2]
BASE = ROOT / "evals/results/persistent-replay"
H = lambda data: hashlib.sha256(data).hexdigest()
PLATFORMS = ("iOS", "macOS", "tvOS")
VARIANTS = ("owned", "shared")


def source(variant):
    src = (ROOT / "research/evaluation/signal-panel-v3/Presentation.swift").read_text()
    with ZipFile(ROOT / "research/evaluation/signal-panel-v5/candidate.zip") as archive:
        card = archive.read("swift-accessibility-agent/references/examples/return.md").decode()
    assert card.split("```swift\n", 1)[1].split("```", 1)[0] == src
    if variant == "owned":
        return src
    assert variant == "shared"
    return src.replace("private var active: UUID?", "private var active: UUID?\n    private var latest: (UUID, String)?").replace(
        "active = id", "active = id\n        latest = (id, origin)").replace(
        "guard let self, self.active == id", "guard let self, let (id, origin) = self.latest, self.active == id")


if __name__ == "__main__":
    batch = Path(tempfile.mkdtemp(prefix="sheet-callback-", dir=BASE))
    for platform in PLATFORMS:
        for variant in VARIANTS:
            cell = batch / f"P-{platform}-{variant}"
            cell.mkdir()
            (cell / "Subject.swift").write_text(source(variant))
            (cell / "Contract.swift").write_bytes((D / "CallbackTests.swift").read_bytes())
            inputs = {p.name:H(p.read_bytes()) for p in cell.iterdir()}
            (cell / "input.json").write_text(json.dumps(dict(platform=platform, module="Presentation", selection=variant, inputs=inputs), indent=2))
    print(batch.name)

"""Stage unchanged preserved implementations; adapt only the controller's public calls."""
import hashlib
import json
import tempfile
from pathlib import Path

D = Path(__file__).resolve().parent
BASE = D.parents[2] / "evals/results/persistent-replay"
PRIOR = BASE / "v4-binding-cpq3qelu"
QUALIFIED = D.parents[2] / "evals/results/media-inventory/batch-7l479_zv"
H = lambda data: hashlib.sha256(data).hexdigest()


def contract(platform, movie):
    ios = platform == "iOS"
    original = (D / "InventoryTests.swift").read_text()
    start = original.index("        let store =")
    end = original.index("        XCTAssertEqual(store.choices.count")
    prepare = """        let state = MediaState(player: AVPlayer(playerItem: item))
        LOAD
        var choices: [TrackChoice] = []
        for _ in 0..<500 {
            if case .loaded(let tracks) = state.loadState { choices = tracks; break }
            if case .failed(let reason) = state.loadState { XCTFail("inventory rejected: " + reason); return }
            try await Task.sleep(nanoseconds: 10_000_000)
        }
        guard !choices.isEmpty else { XCTFail("unresolved: loader did not return options"); return }
"""
    injected = """let rows = options.enumerated().map { idx, option in
            TrackChoice(id: String(idx), name: option.displayName, descriptive: false, option: option)
        }
        """ + ("state.loadOptions(for:item) { _,done in done(.success((rows,text))) }" if ios
               else "state.loadOptions { _ in (text,rows) }")
    head = original[:original.index("    func test")].replace("import Inventory", "import YourAppModule")
    method = original[len(original[:original.index("    func test")]):start] + prepare + original[end:original.rindex("}")]
    method = method.replace('URL(fileURLWithPath: #filePath).deletingLastPathComponent().appendingPathComponent("sample.mov")', f'URL(fileURLWithPath: "{movie}")')
    method = method.replace("store.choices", "choices").replace("store.selection.", "state." + ("selectionBinding." if ios else "pickerBinding."))
    return head + method.replace("LOAD", "" if ios else "state.loadOptions()") + method.replace("testLoadAndChooseEveryNativeOption", "testWritesWithPreloadedOptions").replace("LOAD", injected) + "}\n"


if __name__ == "__main__":
    batch = Path(tempfile.mkdtemp(prefix="all-options-", dir=BASE))
    for old in sorted(PRIOR.glob("P-*.signal-v4")):
        row = json.loads((old / "input.json").read_bytes())
        cell = batch / old.name
        cell.mkdir()
        source = (old / "Subject.swift").read_bytes()
        assert H(source) == row["inputs"]["Subject.swift"]
        movie = QUALIFIED / row["platform"] / "ordinal/Tests/InventoryTests/sample.mov"
        asset = movie.read_bytes()
        assert H(asset) == "c08c9e5d23f035221aedfd9004dde8873a1b9edeff1d21b45a73a4b5626f76f3"
        (cell / "sample.mov").write_bytes(asset)
        (cell / "Subject.swift").write_bytes(source)
        (cell / "Contract.swift").write_text(contract(row["platform"], cell / "sample.mov"))
        row.update(selection="native inventory and isolated all-option writes", inputs={p.name:H(p.read_bytes()) for p in cell.iterdir()})
        (cell / "input.json").write_text(json.dumps(row, indent=2))
    print(batch.name)

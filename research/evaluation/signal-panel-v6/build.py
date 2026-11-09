"""Signal-v6 research candidate: v5 with rewritten cards from cards/, examples unchanged.

  python3 -B research/evaluation/signal-panel-v6/build.py          # write candidate.zip
  python3 -B research/evaluation/signal-panel-v6/build.py --check  # rebuild in memory and compare
"""
import hashlib, io, posixpath, re, sys
from pathlib import Path
from zipfile import ZipFile, ZipInfo, ZIP_DEFLATED

sys.dont_write_bytecode = True
D = Path(__file__).resolve().parent
PARENT = D.parent / "signal-panel-v5/candidate.zip"
PARENT_SHA = "8ed8f947880fe18dd9bfaacd0baf2a26b1471400af3088addfcb8a93d6f95afd"
PREFIX = "swift-accessibility-agent/"
CARDS = {"SKILL.md": "SKILL.md", "return.md": "references/return.md", "media.md": "references/media.md",
         "validation.md": "references/validation.md", "actions.md": "references/actions.md",
         "facts.md": "references/facts.md"}
ENTRY_MAX, TOTAL_MAX = 2200, 15000


def build():
    assert hashlib.sha256(PARENT.read_bytes()).hexdigest() == PARENT_SHA, "v5 parent changed"
    with ZipFile(PARENT) as z:
        files = {n: z.read(n) for n in z.namelist()}
    for src, dst in CARDS.items():
        assert PREFIX + dst in files, dst
        files[PREFIX + dst] = (D / "cards" / src).read_bytes()
    out = io.BytesIO()
    with ZipFile(out, "w") as z:
        for n, b in sorted(files.items()):
            # No panel identifiers, test assertions or controller vocabulary in runtime context.
            assert not re.search(rb"\b[PG]-[0-9a-f]{12,}|GP26-|XCTAssert|Proof0\.swift|rubric|oracle", b, re.I), n
            for link in re.findall(rb"\]\(([^)]+)\)", b):
                if not link.startswith(b"https:"):
                    assert posixpath.normpath(posixpath.join(posixpath.dirname(n), link.decode())) in files, (n, link)
            z.writestr(ZipInfo(n, (2026, 1, 1, 0, 0, 0)), b, compress_type=ZIP_DEFLATED)
    entry, total = len(files[PREFIX + "SKILL.md"]), sum(map(len, files.values()))
    assert entry <= ENTRY_MAX and total <= TOTAL_MAX, (entry, total)
    return out.getvalue(), entry, total


if __name__ == "__main__":
    data, entry, total = build()
    target = D / "candidate.zip"
    if "--check" in sys.argv:
        assert target.read_bytes() == data, "candidate.zip differs from a rebuild"
    else:
        target.write_bytes(data)
    print(hashlib.sha256(data).hexdigest(), entry, total)

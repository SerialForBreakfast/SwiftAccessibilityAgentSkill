"""Signal-v7 research candidate, built fresh from skill/ (not patched from v6).

  python3 -B research/evaluation/signal-panel-v7/build.py          # write candidate.zip
  python3 -B research/evaluation/signal-panel-v7/build.py --check  # rebuild in memory and compare

Recipes contain XCTest code on purpose. Leaks of panel tests are screened separately by
screen.py (8-word overlap with questions, criteria, controller tests and run-1 answers).
"""
import hashlib, io, posixpath, re, sys
from pathlib import Path
from zipfile import ZipFile, ZipInfo, ZIP_DEFLATED

sys.dont_write_bytecode = True
D = Path(__file__).resolve().parent
SRC = D / "skill"
PREFIX = "swift-accessibility-agent/"
ENTRY_MAX, TOTAL_MAX = 3000, 40000
LEAK = rb"\b[PG]-[0-9a-f]{12,}|GP26-|Proof0\.swift|rubric|oracle|grader"


def build():
    files = {PREFIX + p.relative_to(SRC).as_posix(): p.read_bytes()
             for p in sorted(SRC.rglob("*")) if p.is_file() and p.name != ".DS_Store"}
    assert PREFIX + "SKILL.md" in files
    out = io.BytesIO()
    with ZipFile(out, "w") as z:
        for n, b in sorted(files.items()):
            assert not re.search(LEAK, b, re.I), (n, re.search(LEAK, b, re.I).group())
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

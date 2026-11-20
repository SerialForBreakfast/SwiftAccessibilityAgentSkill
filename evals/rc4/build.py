"""Reproduce rc.4 with a focused change to the proof checklist."""
from hashlib import sha256
from pathlib import Path
from zipfile import ZipFile

HERE = Path(__file__).resolve().parent
BASE = HERE.parent / "rc3/swift-accessibility-agent-0.3.0-rc.3.zip"
OUT = HERE / "swift-accessibility-agent-0.3.0-rc.4.zip"
ENTRY = "swift-accessibility-agent/SKILL.md"
OLD = """3. Assert a value that differs on the broken code, and use the fixed result as the expectation.
4. Show the ordinary path still succeeds."""
NEW = """3. Name the XCTest assertion that first fails on the defective implementation and passes on the working one. Give its actual value or callback count in each. Read the effect from the object the user operates. If both outcomes match, change the setup or assertion.
4. For stale or disabled actions, invoke the retained action after the transition, then invoke the current enabled action and check its recipient and count. For deferred effects, check immediately before and after completion. Preserve existing return values and cleanup."""


def build():
    assert sha256(BASE.read_bytes()).hexdigest() == "c5b857c20f6bb0be3ff304e5ebc9e0f53295e7942d4f5483bc887385ac02600e"
    with ZipFile(BASE) as previous, ZipFile(OUT, "w") as candidate:
        for entry in previous.infolist():
            body = previous.read(entry)
            if entry.filename == ENTRY:
                assert body.count(OLD.encode()) == 1 and body.count(b"0.3.0-rc.3") == 2
                body = body.replace(b"0.3.0-rc.3", b"0.3.0-rc.4").replace(OLD.encode(), NEW.encode())
            candidate.writestr(entry, body)


if __name__ == "__main__":
    build()

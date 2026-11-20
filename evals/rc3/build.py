"""Build rc.3 from the published rc.2 archive and the measured review instruction."""
from hashlib import sha256
from pathlib import Path
from zipfile import ZipFile

HERE = Path(__file__).resolve().parent
BASE = HERE.parent / "rc2/swift-accessibility-agent-0.3.0-rc.2.zip"
OUT = HERE / "swift-accessibility-agent-0.3.0-rc.3.zip"
ENTRY = "swift-accessibility-agent/SKILL.md"
INSTRUCTION = (
    "When reviewing an accessibility patch, trace the supplied input through the changed branch. "
    "Name the return value, state mutation, and user action that remains available. "
    "Base your verdict on that trace. If a concern depends on an unseen caller or a new fallback "
    "policy, state the assumption separately."
)


def build():
    assert sha256(BASE.read_bytes()).hexdigest() == "a1449f8863ee1c8724da8181d928cf8a58a963202da548b5fc1a1360e5b28aa5"
    with ZipFile(BASE) as previous, ZipFile(OUT, "w") as candidate:
        for entry in previous.infolist():
            body = previous.read(entry)
            if entry.filename == ENTRY:
                anchor = b"Make changed code fit"
                assert body.count(anchor) == 1 and body.count(b"0.3.0-rc.2") == 2
                body = body.replace(b"0.3.0-rc.2", b"0.3.0-rc.3")
                body = body.replace(anchor, INSTRUCTION.encode() + b"\n\n" + anchor)
            candidate.writestr(entry, body)


if __name__ == "__main__":
    build()

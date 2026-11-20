"""Build the single-change stale-validation candidate directly from rc.3."""
from pathlib import Path
from hashlib import sha256
from zipfile import ZipFile

HERE = Path(__file__).resolve().parent
BASE = HERE.parent / 'rc3/swift-accessibility-agent-0.3.0-rc.3.zip'
OUT = HERE / 'swift-accessibility-agent-0.3.0-rc.5.zip'
RULE = ("For a stale validation reply, keep the original request pending. In the test, "
        "submit A, assign B directly to the live field’s text, then deliver A’s captured "
        "reply. Calling an edit helper that cancels A tests cancellation instead. Assert "
        "that A’s result was rejected, B remains in the field, and the form can submit B.")

def build():
    assert sha256(BASE.read_bytes()).hexdigest() == 'c5b857c20f6bb0be3ff304e5ebc9e0f53295e7942d4f5483bc887385ac02600e'
    with ZipFile(BASE) as old, ZipFile(OUT, 'w') as new:
        for entry in old.infolist():
            data = old.read(entry)
            if entry.filename.endswith('/SKILL.md'):
                anchor = b'3. Assert a value'
                assert data.count(anchor) == 1 and data.count(b'0.3.0-rc.3') == 2
                data = data.replace(anchor, b'   ' + RULE.encode() + b'\n' + anchor)
                data = data.replace(b'0.3.0-rc.3', b'0.3.0-rc.5')
            new.writestr(entry, data)

if __name__ == '__main__':
    build()

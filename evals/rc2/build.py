"""Reproduce the opt-in RC from immutable, measured v6 bytes."""
import hashlib
import io
import json
import re
from pathlib import Path
from zipfile import ZipFile, ZipInfo, ZIP_DEFLATED

HERE = Path(__file__).resolve().parent
BASE = HERE.parents[1] / 'research/evaluation/signal-panel-v6/candidate.zip'
PIN = 'de259a352d5ec2217424df77d0829b0d4fec29e99079ae682cadb46720691862'
OUT = HERE / 'swift-accessibility-agent-0.3.0-rc.2.zip'
ROOT = 'swift-accessibility-agent/'
VERSION = '0.3.0-rc.2'

def package():
    data = BASE.read_bytes()
    assert hashlib.sha256(data).hexdigest() == PIN
    with ZipFile(io.BytesIO(data)) as z:
        files = {n.removeprefix(ROOT): z.read(n).decode() for n in z.namelist()}
    def replace(path, old, new):
        assert files[path].count(old) == 1, (path, old)
        files[path] = files[path].replace(old, new)
    replace('SKILL.md', 'version: signal-v6', 'version: ' + VERSION)
    desc = re.search(r'^description: (.+)$', files['SKILL.md'], re.M)[1]
    replace('SKILL.md', 'description: ' + desc, 'description: ' + json.dumps(desc))
    replace('SKILL.md', '(signal-v6)', '(' + VERSION + ')')
    replace('SKILL.md', 'reuse, children and wrapper callbacks.', 'reuse, editable children, ordinary taps and wrapper callbacks.')
    replace('SKILL.md', 'inspection, selection and overlapping requests.', 'inspector results, selection and overlapping requests.')
    replace('references/actions.md',
            'Removing duplicate wrapper semantics should leave the native editor available for editing.',
            'For a hosted Mac search field, remove the redundant label or element on the wrapper. Keep the NSSearchField and its field editor in charge of editing, selection and insertion. Hide decorative siblings if appropriate; hiding the representable or its ancestor, or replacing its accessibility representation with empty content, can hide the editor too. If the duplicate owner is unclear, identify it before suggesting a modifier.')
    replace('references/actions.md', 'Keep ordinary buttons connected.',
            'Keep ordinary buttons connected. On a custom player control, trace the ordinary single tap to the playback handler separately from drag-to-seek and accessibility activation. Adding an adjustable or named action does not install a touch handler. Preserve the existing tap on its surface; do not silently substitute a double tap or a separate button for that interaction.')
    replace('references/facts.md', 'Forwarding to it or a non-actionable wrapper are both fine.',
            'Strip duplicate wrapper semantics without hiding the editable subtree; see [Actions](actions.md).')
    replace('references/media.md', 'An unlisted selection is not Off.',
            'For an inspector, distinguish no item from a successfully inspected item without the requested group. Test the returned enum by matching its cases. An associated payload need not be Equatable: adding synthesized conformance just to compare two empty cases can break the build. When a loaded value matters, assert the relevant payload fields instead. An unlisted selection is not Off.')
    buf = io.BytesIO()
    with ZipFile(buf, 'w') as z:
        for name, body in sorted(files.items()):
            for link in re.findall(r'\]\(([^)]+)\)', body):
                if not link.startswith(('https:', 'http:', '#')):
                    assert (Path(name).parent / link).as_posix() in files, (name, link)
            entry = ZipInfo(ROOT + name, (2026, 1, 1, 0, 0, 0))
            entry.create_system = 3
            entry.external_attr = 0o100644 << 16
            z.writestr(entry, body, compress_type=ZIP_DEFLATED)
    return buf.getvalue()

if __name__ == '__main__':
    OUT.write_bytes(package())
    print(hashlib.sha256(OUT.read_bytes()).hexdigest(), OUT.name)

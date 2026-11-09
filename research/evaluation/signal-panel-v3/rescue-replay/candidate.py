"""Small additive successor; strategy and evidence remain controller-only."""
from io import BytesIO
from pathlib import Path
import hashlib,json,sys
from zipfile import ZipFile,ZipInfo,ZIP_DEFLATED
D=Path(__file__).resolve().parent
raw=(D.parent/'offline-pass/candidate.zip').read_bytes()
assert hashlib.sha256(raw).hexdigest()=='82a6d9eca61463637307bacd634fe0028e75c3442d5877920f7cef278705ba8e'
with ZipFile(BytesIO(raw)) as z:files={n:z.read(n) for n in z.namelist()}
p='swift-accessibility-agent/'
def sub(name,old,new):
    k=p+name;a=old.encode();assert files[k].count(a)==1
    files[k]=files[k].replace(a,new.encode())
entry=p+'SKILL.md';files[entry]=files[entry].replace(b'signal-v3-distilled.1',b'signal-v3-rescue.1')
sub('SKILL.md','Review or implement Swift accessibility on iOS, macOS and tvOS, including native-control wrappers, first-responder fallback, media picker bindings and asynchronous form validation.',
    'Use when reviewing or implementing accessible Swift UI on iOS, macOS or tvOS: VoiceOver actions after reuse, representable updates, sheet dismissal or first-responder refusal, caption selection, and forms that stay unavailable after edits.')
sub('SKILL.md','Separate configured behavior from delivered assistive interaction.',
    'Keep code fences compilable: put citations outside Swift declarations. Separate configured behavior from delivered assistive interaction.')
sub('references/return.md','Consume only the matching request before calling reentrant code.',
    'Compare the completed presentation with the current owner first. On mismatch leave the successor untouched; on match retire that request before a restoration callback can reopen the presentation.')
sub('references/facts.md','Preserve the uncategorized path when no category is requested.',
    'Exercise both explicit settings on the returned action. Preserve the caller\'s established default; an example factory with another default is not the contract.')
sub('references/actions.md','Direct dispatch alone does not establish attachment.',
    'For AppKit target-action wiring, exercise the configured button and observe its handler and document ID. A press return value alone cannot prove dispatch, nor can direct dispatch prove attachment.')
out=BytesIO()
with ZipFile(out,'w') as z:
    for n,data in sorted(files.items()):z.writestr(ZipInfo(n,(2026,1,1,0,0,0)),data,compress_type=ZIP_DEFLATED)
if '--check' in sys.argv:assert (D/'candidate.zip').read_bytes()==out.getvalue()
else:(D/'candidate.zip').write_bytes(out.getvalue())
fixtures=json.loads((D/'trigger-fixtures.json').read_text())
assert [r[0] for r in fixtures]==['use','near-miss']*5 and len({r[1] for r in fixtures})==10
print('candidate',hashlib.sha256(out.getvalue()).hexdigest(),'; entry',len(files[entry]),'bytes; 10 trigger fixtures (not evaluated)')

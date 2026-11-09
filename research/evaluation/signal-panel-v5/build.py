"""One research successor, no live subjects or controller material in runtime context."""
import hashlib,io,re,sys,posixpath
from pathlib import Path
from zipfile import ZipFile,ZipInfo,ZIP_DEFLATED
D=Path(__file__).resolve().parent
p=D.parent/'signal-panel-v4/candidate.zip'
assert hashlib.sha256(p.read_bytes()).hexdigest()=='8bb2d940dedf8aa8b4d6b416faad8751dc20faa8bcaaec9428884f50dca49e0d'
with ZipFile(p) as z:files={n:z.read(n) for n in z.namelist()}
prefix='swift-accessibility-agent/'
def edit(n,old,new):
    k=prefix+n;assert files[k].count(old.encode())==1
    files[k]=files[k].replace(old.encode(),new.encode())
files[prefix+'SKILL.md']=files[prefix+'SKILL.md'].replace(b'signal-v4',b'signal-v5')
edit('SKILL.md','Keep citations outside Swift code.', 'Use supplied types and fixtures; assert the fixed outcome. Keep citations outside Swift code.')
edit('SKILL.md','Read only the relevant note:', 'Start with the matching note. Open a second only for a separate decision:')
files[prefix+'references/media.md']=(D/'media.md').read_bytes()
edit('references/return.md','Bind the callback to that presentation or serialize presentations.',
     'Capture the owner when each presentation opens, not from shared state at dismissal. Exercise the installed closures: finish A late, then B twice; only B may restore, once. Serialize only if the product requires it.')
edit('references/return.md','Distinguish eligibility from the result of an attempted request. Apply the specified fallback policy; report the target requested, not delivered assistive focus.',
     'Where fallback is required, try it both when the origin is ineligible and when the eligible origin rejects the request. A detached-origin test covers neither attached case. Report requests, not delivered assistive focus.')
edit('references/actions.md',"For a collection, selected accessibility traits do not themselves change collection selection.",
     "Keep model state such as Saved distinct from a collection's transient selection. Changing native selection must not rewrite independent saved wording.")
edit('references/facts.md',"one correct property does not establish the others.",
     "one correct property does not establish the others. Clear optional AppKit help with nil; substituting an empty string changes the observable value.")
edit('references/facts.md',"distinguish the SDK's UIAccessibilityCustomAction.editCategory constant from an inferred enum case.",
     "for optional edit grouping assign `action.category = grouped ? UIAccessibilityCustomAction.editCategory : nil`. The category is a string, not an enum with a .edit case.")
out=io.BytesIO()
with ZipFile(out,'w') as z:
    for n,b in sorted(files.items()):
        assert not re.search(rb'\b[PG]-[0-9a-f]{12,}|XCTAssert|Proof0.swift',b)
        for link in re.findall(rb'\]\(([^)]+)\)',b):
            if not link.startswith(b'https:'):assert posixpath.normpath(posixpath.join(posixpath.dirname(n),link.decode())) in files
        z.writestr(ZipInfo(n,(2026,1,1,0,0,0)),b,compress_type=ZIP_DEFLATED)
target=D/'candidate.zip';data=out.getvalue()
if '--check' in sys.argv: assert target.read_bytes()==data
else:target.write_bytes(data)
print(hashlib.sha256(data).hexdigest(),len(files[prefix+'SKILL.md']),sum(map(len,files.values())))

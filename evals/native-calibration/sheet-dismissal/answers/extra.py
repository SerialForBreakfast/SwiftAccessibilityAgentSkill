import json,tempfile
from pathlib import Path
from zipfile import ZipFile
from prepare import D,BASE,ROOT,FENCES,H

batch=Path(tempfile.mkdtemp(prefix='sheet-extra-',dir=BASE/'persistent-replay'))
def add(name,platform,src,tests,ans):
    c=batch/('P-'+name);c.mkdir()
    (c/'Subject.swift').write_text(src+'\n'+(D/'Registration.swift').read_text())
    (c/'Contract.swift').write_bytes((D/tests).read_bytes())
    (c/'answer.txt').write_bytes(ans)
    (c/'input.json').write_text(json.dumps(dict(platform=platform,module='Presentation',selection=name,inputs={p.name:H(p.read_bytes()) for p in c.iterdir()}),indent=2))

with ZipFile(next(BASE.glob('signal-v4-review/*.zip'))) as z:
    ans=z.read('records/P-90629dd9d60ff906.signal-v4/answer.txt')
    add('9062-v4','iOS',FENCES.findall(ans.decode())[0],'IOS.swift',ans)
with ZipFile(next(BASE.glob('gemini-discovery*/bundles/*375*'))) as z:
    ans=z.read('G-16de77ef3240aa/answer.txt')
    code=(ROOT/'code-examples/swiftui/macos-v1/NegativeFixtures/lifecycle.swift').read_text()
    old='guard showing else { return }';new='guard showing, ticket == generation else { return }'
    assert '-        '+old in ans.decode() and '+        '+new in ans.decode() and code.count(old)==1
    add('G-16de77ef3240aa','macOS',code.replace(old,new),'Hosted.swift',ans)
code=(ROOT/'code-examples/swiftui/macos-v1/Sources/Lifecycle.swift').read_text()
assert code.count('onDismiss: {')==1
add('control-captured','macOS',code.replace('onDismiss: {','onDismiss: { [ticket] in'),'Hosted.swift',b'Controller positive, not a model answer.')
print(batch.name)

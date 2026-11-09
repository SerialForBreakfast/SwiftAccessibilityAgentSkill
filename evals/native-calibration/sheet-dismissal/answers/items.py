import json,tempfile
from pathlib import Path
from zipfile import ZipFile
from prepare import BASE,D,H,FENCES
batch=Path(tempfile.mkdtemp(prefix='sheet-items-',dir=BASE/'persistent-replay'))
for name,platform in [('G-fe05e95d638c25','macOS'),('b03-7','iOS')]:
    if platform=='macOS':
        with ZipFile(next(BASE.glob('gemini-discovery*/bundles/*375*'))) as z:
            ans=z.read(name+'/answer.txt')
    else:
        with ZipFile(next(BASE.glob('failure-inventory/bundles/dev7*'))) as z:
            row=next(x for x in json.loads(z.read('answers-and-grades.json')) if x['id']==name)
            ans=row['original_answer'].encode()
            assert H(ans)==row['originalSha256']
    src=FENCES.findall(ans.decode())[0]
    cell=batch/('P-'+name);cell.mkdir()
    (cell/'answer.txt').write_bytes(ans)
    (cell/'Subject.swift').write_text(src+'\n'+(D/'Items.swift').read_text())
    (cell/'Contract.swift').write_bytes((D/'ItemTests.swift').read_bytes())
    (cell/'input.json').write_text(json.dumps(dict(platform=platform,module='Presentation',selection='unchanged item fence',inputs={p.name:H(p.read_bytes()) for p in cell.iterdir()}),indent=2))
print(batch.name)

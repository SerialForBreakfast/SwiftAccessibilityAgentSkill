import json,re,tempfile
from pathlib import Path
from zipfile import ZipFile
from hashlib import sha256
D=Path(__file__).resolve().parent
ROOT=D.parents[3]
BASE=ROOT/'evals/results'
H=lambda b:sha256(b).hexdigest()
FENCES=re.compile(r'^```swift[^\n]*\n(.*?)^```',re.M|re.S)
def main():
    batch=Path(tempfile.mkdtemp(prefix='sheet-answers-',dir=BASE/'persistent-replay'))
    catalog=[]
    for path in sorted([*BASE.glob('*/bundles/*.zip'),*BASE.glob('signal-v*-review*/*.zip')]):
        with ZipFile(path) as z:
            for n in z.namelist():
                if not n.endswith('/answer.txt'):continue
                ans=z.read(n);a=ans.decode(); key=n.split('/')[-2]
                if not (re.search(r'\.sheet\s*\(|SheetExample|\.onDismiss\b',a) or key.startswith('dismiss-owner.')):continue
                if key[:8] in ('G-231795','G-2ef8d4'):continue
                blocks=FENCES.findall(a)
                row=dict(archive=path.name,member=n,answerSHA256=H(ans),proof='helper or source review; not an installed-callback receipt')
                candidates=[b for b in blocks if 'struct SheetExample: View' in b and 'final class PresentationState' in b]
                if candidates and 'sheetB' not in candidates[-1]:
                    code=candidates[-1]
                    reason='unchanged production fence'
                elif key in ('P-da7833399aac7f87.signal-v2','dismiss-owner.review','dismiss-owner.both','P-48400f490808a2cf.unaided'):
                    if key.endswith('.unaided'):
                        code=(BASE/'persistent-replay/tmp6xijam9k'/key/'Subject.swift').read_text()
                        reason='historical primary assembly; separate optional patch not applied'
                    else:
                        code=(ROOT/'code-examples/swiftui/macos-v1/Sources/Lifecycle.swift').read_text()
                        reason='no-change recommendation: unchanged starter'
                else:
                    row['selection']='different ownership or view interface; not exercised by hosted SheetExample contract'
                    catalog.append(row);continue
                cell=batch/('P-'+key);cell.mkdir()
                src=code+'\n'+(D/'Registration.swift').read_text()
                (cell/'Subject.swift').write_text(src)
                (cell/'Contract.swift').write_bytes((D/'Hosted.swift').read_bytes())
                (cell/'answer.txt').write_bytes(ans)
                (cell/'input.json').write_text(json.dumps(dict(platform='macOS',module='Presentation',selection=reason,inputs={p.name:H(p.read_bytes()) for p in cell.iterdir()}),indent=2))
                row.update(selection=reason,cell=cell.name,fence=H(code.encode()))
                catalog.append(row)
    (batch/'catalog.json').write_text(json.dumps(catalog,indent=2))
    print(batch.name,len(catalog),sum('cell'in x for x in catalog))
if __name__=='__main__':main()

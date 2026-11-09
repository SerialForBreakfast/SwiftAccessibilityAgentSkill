"""Build the guidance archive, and optionally regenerate its trace rationale offline."""
from pathlib import Path
from zipfile import ZipFile, ZipInfo, ZIP_DEFLATED
from hashlib import sha256
from io import BytesIO
import json,sys
D=Path(__file__).resolve().parent
V2=D.parent/'signal-panel-v2'
h=lambda b:sha256(b).hexdigest()
focus={'restore-only-owned-sheet':'return.md','restore-accessibility-background':'return.md','retained-native-target':'actions.md','write-actual-player-selection':'media.md'}

def traces():
    p=D.parents[2]/'evals/results/signal-v2-review-20261108/signal-panel-v2-return.zip'
    assert h(p.read_bytes())=='9929eb1bddb1eb850bdc6ff026bb0469852e8ecab19ef7100689595788990368'
    with ZipFile(p) as z:
        read=lambda n:json.loads(z.read(n))
        source=read('traces.json')
        rows=[]
        for r in read('transitions.json'):
            if r['family'] not in focus:continue
            t=source[r['id']+'.skill']
            paths={v['path'].split('/')[-1] for v in t['reads'] if v['status']==3 and v['returned_excerpt']}
            rows.append(dict(case=r['id'],family=r['family'],primary=r['transitions']['primary'],whole=r['transitions']['whole'],bodyRead='SKILL.md' in paths,
                        expectedCard=focus[r['family']],expectedCardRead=focus[r['family']] in paths,readFiles=sorted(paths)))
        return (json.dumps(rows,indent=2)+'\n').encode()

def build():
    raw=(V2/'candidate.zip').read_bytes()
    assert h(raw)=='c4b110e4ac596272e750eec91ef372e5e1ff49e37b3228206e920000b4c2176b'
    with ZipFile(BytesIO(raw)) as z:files={n:z.read(n) for n in z.namelist()}
    prefix='swift-accessibility-agent/'
    entry=prefix+'SKILL.md';files[entry]=files[entry].replace(b'signal-v2',b'signal-v3').replace(b'for reconfiguration, native children or bridged controls.',b'for retained UIKit actions, representable/coordinator rebinding, or independent children.').replace(b'Review or implement accessibility in Swift interfaces for iOS, macOS and tvOS.',b'Review or implement Swift accessibility on iOS, macOS and tvOS, including action callbacks in SwiftUI wrappers of native controls.')
    for name in ['actions','return','media']:
        key=prefix+'references/'+name+'.md'
        files[key]=files[key].rstrip()+b'\n\n'+(D/(name+'-delta.md')).read_bytes()
    # Source excerpts only, not prompts, tests, mutants or controller notes.
    examples=D.parents[2]/'code-examples'
    modal=(examples/'pilots/uikit-modal-v1/Sources/ModalUIKit.swift').read_text()
    surface=(examples/'swiftui/forwarding-ios-v1/Sources/NativeSurface.swift').read_text()
    media=(examples/'swiftui/media-ios-v2/Sources/MediaSelection.swift').read_text()
    def span(s,start,end):
        return s[s.index(start):s.index(end,s.index(start)+len(start))].rstrip()
    snippets={
        'return': [('Per-presentation SwiftUI modifier', (D/'Presentation.swift').read_text()),
                   ('UIKit teardown and snapshot release (methods on RestoringPanel)',modal[modal.index('    private func finish'):].rstrip().removesuffix('}'))],
        'actions':[('Installed shortcut (inside configure)',span(surface,'        let shortcut = action(view, secondary: true)\n        view.primary.accessibilityCustomActions','        #endif')),
                   ('Captured registration (method on SurfaceOwner)',span(surface,'    func action(_ view:', '    #if os(macOS)\n    @objc'))],
        'media':[('Binding captures the load (property on MediaSelectionStore)',span(media,'    var selection: Binding','    var status:')),
                 ('Write to the current player item (method on the same store)',span(media,'    @discardableResult\n    func choose','\n}\n'))]}
    for name, sections in snippets.items():
        files[prefix+'references/'+name+'.md']+=('\nFor implementation code, see the [tested source excerpts](examples/'+name+'.md).\n').encode()
        files[prefix+'references/examples/'+name+'.md']='\n\n'.join(
            title+'\n\n```swift\n'+code.rstrip()+'\n```' for title,code in sections).encode()+b'\n'
    out=BytesIO()
    with ZipFile(out,'w') as z:
        for n,v in sorted(files.items()):z.writestr(ZipInfo(n,(2026,1,1,0,0,0)),v,compress_type=ZIP_DEFLATED)
    return out.getvalue()

if __name__=='__main__':
    outputs={'candidate.zip':build()}
    if '--traces' in sys.argv:outputs['trace-review.json']=traces()
    for name,data in outputs.items():
        if '--check' in sys.argv:assert (D/name).read_bytes()==data,name
        else:(D/name).write_bytes(data)
        print(name,h(data))

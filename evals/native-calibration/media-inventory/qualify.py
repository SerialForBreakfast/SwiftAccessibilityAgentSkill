"""Compile isolated control variants. A qualifying negative must fail its registered assertion."""
import base64, hashlib, json, re, subprocess, sys, tempfile
from pathlib import Path
D=Path(__file__).resolve().parent
ROOT=D.parents[2]
BASE=ROOT/'evals/results/media-inventory'
BASE.mkdir(exist_ok=True)
H=lambda b:hashlib.sha256(b).hexdigest()
def cmd(*args):return subprocess.check_output(args,text=True).strip()
def replace(s,a,b):
    if s.count(a)!=1:raise ValueError('source drift: '+a)
    return s.replace(a,b)
MODES={'ordinal':None,'opaque':None,'language':'inventory must load despite language collision','local-only':'real caption write','audio-loss':'preserve audio'}
def subject(folder,mode):
    s=(folder/'Sources/MediaSelection.swift').read_text()
    start=s.index('            choices = loaded.options.enumerated().compactMap')
    end=s.index('            phase = .ready',start)
    # This case asks for ALL native options. Do not impose the separate full-caption-only policy.
    if mode=='opaque':
        inventory='''            choices = loaded.options.map { option in
                MediaOption(id: UUID().uuidString, name: option.displayName, option: option)
            }
'''
    else:
        key='option.extendedLanguageTag ?? option.displayName' if mode=='language' else r'"\(ticket):\(index)"'
        inventory='''            choices = loaded.options.enumerated().map { index, option in
                MediaOption(id: KEY, name: option.displayName, option: option)
            }
'''.replace('KEY',key)
    s=s[:start]+inventory+r'''            guard Set(choices.map(\.id)).count == choices.count else {
                choices = []; phase = .failed; return
            }
'''+s[end:]
    if mode=='local-only':s=replace(s,'item.select(choice.option, in: group)','_ = choice.option')
    if mode=='audio-loss':
        # Native AVFoundation group already loaded by the test; switch to the other audio option.
        s=replace(s,'item.select(choice.option, in: group)','''item.select(choice.option, in: group)
            if let audio = item.asset.mediaSelectionGroup(forMediaCharacteristic: .audible),
               let other = audio.options.first(where: { !$0.hasMediaCharacteristic(.describesVideoForAccessibility) }) {
                item.select(other, in: audio)
            }''')
    return s

def outcome(log,mode,rc):
    text=log.decode(errors='replace')
    statuses=re.findall(r"Test Case '[^'\n]* testLoadAndChooseEveryNativeOption\]' (passed|failed)",text)
    errors=[l.split(' : ',1)[-1] for l in text.splitlines() if ': error: -[' in l and ' testLoadAndChooseEveryNativeOption]' in l]
    marker=MODES[mode]
    ok=(rc==0 and statuses==['passed'] and not errors) if not marker else (rc==65 and statuses==['failed'] and any(marker in l for l in errors) and not any('fixture must' in l for l in errors))
    return dict(statuses=statuses,errors=errors,accepted=ok)

def run():
    batch=Path(tempfile.mkdtemp(prefix='batch-',dir=BASE))
    print(batch.name,flush=True)
    devices=json.loads(cmd('xcrun','simctl','list','devices','booted','-j'))['devices']
    for platform,sdk in [('iOS','iphonesimulator'),('tvOS','appletvsimulator')]:
        device,=[d for d in devices['com.apple.CoreSimulator.SimRuntime.'+platform+'-26-5'] if d['name']=='SwiftAccessibility-OS26-Unit-'+platform]
        folder=ROOT/f'code-examples/swiftui/media-{platform.lower()}-v2'
        asset=base64.b64decode(re.search(r'let positive = """(.*?)"""',(folder/'Tests/DescriptionFixture.swift').read_text(),re.S)[1])
        assert H(asset)=='c08c9e5d23f035221aedfd9004dde8873a1b9edeff1d21b45a73a4b5626f76f3'
        for mode in MODES:
            w=batch/platform/mode
            src=w/'Sources/Inventory'; src.mkdir(parents=True)
            test=w/'Tests/InventoryTests'; test.mkdir(parents=True)
            (src/'MediaSelection.swift').write_text(subject(folder,mode))
            (test/'InventoryTests.swift').write_bytes((D/'InventoryTests.swift').read_bytes())
            (test/'sample.mov').write_bytes(asset)
            (w/'Package.swift').write_text('// swift-tools-version: 6.0\nimport PackageDescription\nlet package=Package(name:"Inventory",platforms:[.iOS("26.0"),.tvOS("26.0")],products:[.library(name:"Inventory",targets:["Inventory"])],targets:[.target(name:"Inventory"),.testTarget(name:"InventoryTests",dependencies:["Inventory"],exclude:["sample.mov"])])\n')
            args=['xcodebuild','test','-scheme','Inventory','-destination','id='+device['udid'],'-derivedDataPath',str(w/'dd'),'-resultBundlePath',str(w/'result.xcresult'),'-parallel-testing-enabled','NO','-collect-test-diagnostics','never','CODE_SIGNING_ALLOWED=NO']
            intent=dict(platform=platform,mode=mode,xcode=cmd('xcodebuild','-version'),sdk=cmd('xcrun','--sdk',sdk,'--show-sdk-version'),runtime='26.5',deployment='26.0',command=args,inputs={str(p.relative_to(w)):H(p.read_bytes()) for p in w.rglob('*') if p.is_file()})
            (w/'intent.json').write_text(json.dumps(intent,indent=2))
            with (w/'native.log').open('xb') as f:rc=subprocess.run(args,cwd=w,stdout=f,stderr=subprocess.STDOUT,timeout=240).returncode
            data=(w/'native.log').read_bytes()
            result=dict(**outcome(data,mode,rc),exit=rc,logSHA256=H(data),intentSHA256=H((w/'intent.json').read_bytes()))
            (w/'receipt.json').write_text(json.dumps(result,indent=2))
            print(platform,mode,result['accepted'],flush=True)
            if not result['accepted']:raise SystemExit('Unexpected first result preserved.')
if __name__=='__main__':run()

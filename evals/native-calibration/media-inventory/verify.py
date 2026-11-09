"""Verify the staged bytes, unchanged oracle, environment and native method-level outcomes."""
import argparse,json
from qualify import D,ROOT,BASE,H,MODES,subject,outcome
def need(ok,msg):
    if not ok:raise ValueError(msg)
def collect(batch):
    out=[]
    for platform in ('iOS','tvOS'):
        folder=ROOT/f'code-examples/swiftui/media-{platform.lower()}-v2'
        env=None
        for mode in MODES:
            w=BASE/batch/platform/mode
            intent=(w/'intent.json').read_bytes(); i=json.loads(intent)
            receipt=(w/'receipt.json').read_bytes(); r=json.loads(receipt)
            log=(w/'native.log').read_bytes()
            need(H(log)==r['logSHA256'] and H(intent)==r['intentSHA256'], 'receipt chain')
            need(i['mode']==mode and i['platform']==platform,'fixture binding')
            anchor={k:i[k] for k in ('platform','xcode','sdk','runtime','deployment')}
            anchor['destination']=i['command'][i['command'].index('-destination')+1]
            need(env is None or anchor==env,'mixed anchors');env=anchor
            for path,h in i['inputs'].items():need(H((w/path).read_bytes())==h,path)
            inputs=i['inputs']
            need(inputs['Tests/InventoryTests/sample.mov']=='c08c9e5d23f035221aedfd9004dde8873a1b9edeff1d21b45a73a4b5626f76f3','changed media')
            need(inputs['Tests/InventoryTests/InventoryTests.swift']==H((D/'InventoryTests.swift').read_bytes()),'changed oracle')
            need(inputs['Sources/Inventory/MediaSelection.swift']==H(subject(folder,mode).encode()),'changed subject')
            verdict=outcome(log,mode,r['exit'])
            need(verdict['accepted'] and all(r[k]==v for k,v in verdict.items()),'method outcome')
            errors=verdict['errors']
            if mode=='language':
                need(errors[0].endswith(MODES[mode]),'fixture failed before the inventory assertion')
                need(all(any(token in e for token in (MODES[mode],'retain all requested options',
                         'independently addressable options','XCTUnwrap failed')) for e in errors),'unrelated inventory failure')
            elif MODES[mode]:
                need(all(e.endswith(MODES[mode]) for e in errors),'unrelated write failure')
            out.append(dict(anchor=anchor,mode=mode,status=verdict['statuses'][0],marker=MODES[mode],
                        inputs=inputs,receiptSHA256=H(receipt),logSHA256=H(log)))
    for key,n in [('Tests/InventoryTests/InventoryTests.swift',1),('Tests/InventoryTests/sample.mov',1),('Package.swift',1),('Sources/Inventory/MediaSelection.swift',len(MODES))]:
        need(len({r['inputs'][key] for r in out})==n,key)
    return dict(batch=batch,records=out)
if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--record',metavar='BATCH')
    args=parser.parse_args()
    path=D/'evidence.json'
    if args.record:
        value=collect(args.record)
        with path.open('x') as f:f.write(json.dumps(value,indent=2)+'\n')
    else:
        value=json.loads(path.read_bytes())
        need(value==collect(value['batch']),'index changed')
    print('Verified',len(value['records']),'platform/variant receipts')

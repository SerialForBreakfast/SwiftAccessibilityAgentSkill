"""Create a deterministic successor without changing subjects or scoring rules."""
from pathlib import Path
from io import BytesIO
import sys
import json
from zipfile import ZipFile
sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
PARENT = HERE.parent/'signal-panel-v1'
sys.path.insert(0,str(PARENT))
# This script also has the name build.py; import the pinned parent by path.
from importlib.util import spec_from_file_location, module_from_spec
spec=spec_from_file_location('panel_v1_builder', PARENT/'build.py')
base=module_from_spec(spec)
spec.loader.exec_module(base)

def unpack(data):
    with ZipFile(BytesIO(data)) as z:
        assert z.testzip() is None and len(z.namelist())==len(set(z.namelist()))
        return {k:z.read(k) for k in z.namelist()}

def outputs():
    data=(PARENT/'held.zip').read_bytes()
    assert base.h(data)=='82ea827e7a3907d6bc75b2edc6f546357bb4a5c3ffcc89e6b28d7553edc9b5d8'
    old=unpack(data)
    assert json.loads(old['seal.json'])=={k:base.h(v) for k,v in old.items() if k!='seal.json'}
    files=unpack(old['candidate.zip'])
    prefix='swift-accessibility-agent/'
    entry=files[prefix+'SKILL.md'].decode().replace('signal-v1','signal-v2')
    files[prefix+'SKILL.md']=(entry+'- [Pending form state](references/validation.md) for edits, overlapping submissions or delayed validation.\n').encode()
    for name in ('actions','validation','media','return'):
        files[prefix+'references/'+name+'.md']=(HERE/'cards'/f'{name}.md').read_bytes()
    candidate=base.pack(files)
    packet={**old,'candidate.zip':candidate,'HANDOFF.md':old['HANDOFF.md'].replace(b'signal-panel-v1',b'signal-panel-v2')}
    packet['seal.json']=base.dump({k:base.h(v) for k,v in sorted(packet.items()) if k!='seal.json'})
    sealed=base.pack(packet)
    assert {k for k in packet if old[k]!=packet[k]}=={'seal.json','candidate.zip','HANDOFF.md'}
    assert len([k for k in packet if k.startswith('subjects/')])==56
    for name in ('actions','validation','media','return','font','facts'):
        assert ('references/'+name+'.md').encode() in files[prefix+'SKILL.md'] and prefix+'references/'+name+'.md' in files
    return {'candidate.zip':candidate,'held.zip':sealed,'receipt.json':base.dump(dict(state='held-not-sent',cases=56,attemptsProposed=112,
            parentPacket=base.h(data),packetSHA256=base.h(sealed),candidateSHA256=base.h(candidate),
            addedEntryBytes=len(files[prefix+'SKILL.md'])-len(unpack(old['candidate.zip'])[prefix+'SKILL.md'])))}
if __name__=='__main__':
    for name,data in outputs().items():
        if '--check' in sys.argv: assert (HERE/name).read_bytes()==data,name
        else: (HERE/name).write_bytes(data)
        if name=='receipt.json': print(data.decode())

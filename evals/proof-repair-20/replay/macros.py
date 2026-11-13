"""Recheck first-pass macro loader gaps with the installed toolchain plugin."""
import json,subprocess
from stage import D,call
from pathlib import Path
rows=[]
for x in json.loads((D/'preflight.json').read_bytes()):
    if 'TestingMacros' not in (x.get('error') or ''):continue
    w=D/'preflight'/x['case']; sdk,dest={'iOS':('iphonesimulator','ios26.0-simulator'),'macOS':('macosx','macos26.0'),'tvOS':('appletvsimulator','tvos26.0-simulator')}[x['platform']]
    dev=Path(subprocess.check_output(['xcrun','--sdk',sdk,'--show-sdk-platform-path'],text=True).strip())/'Developer'
    compiler=Path(subprocess.check_output(['xcrun','-f','swiftc'],text=True).strip())
    plugin=compiler.parents[2]/'usr/lib/swift/host/plugins/testing/libTestingMacros.dylib'
    assert plugin.exists()
    prod='Prod'+x['case'];alias=x['alias']
    cmd=['xcrun','--sdk',sdk,'swiftc','-swift-version','5','-target','arm64-apple-'+dest,'-module-cache-path',str(D/'cache'),'-F',str(dev/'Library/Frameworks'),'-I',str(dev/'usr/lib'),'-I',str(w),'-load-plugin-library',str(plugin),'-typecheck']+(['-module-alias',alias+'='+prod] if alias!=prod else [])+[str(w/(x['hash']+'.swift'))]
    p=call(cmd);(w/(x['hash']+'.macro.log')).write_bytes(p.stderr)
    x.update(status='ready' if not p.returncode else 'compile gap',error=next((s.split('error: ',1)[-1] for s in p.stderr.decode().splitlines() if 'error:' in s),None));rows.append(x)
(D/'extra.json').write_text(json.dumps(rows,indent=1));print([(r['case'],r['status'],r.get('error')) for r in rows])

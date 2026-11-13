"""Require positive, alternative and specific native assertion-failure receipts."""
import csv,json,re,sys
from pathlib import Path
from prepare import D,H,J
base=Path(sys.argv[1]).resolve(); results=[]
for row in csv.DictReader((D/'witnesses.tsv').read_text().splitlines(),delimiter='\t'):
    i=row['id']; arms={}; directory=next((Path(path).resolve() for path in reversed(sys.argv[2:]) if (Path(path)/i/'working/result.json').exists()),base); a=json.loads((directory/i/'case.json').read_bytes())
    for v in ('working','alternative','defect'):
        w=directory/i/v;r=json.loads((w/'result.json').read_bytes());arms[v]=r
        assert all(H((w/f).read_bytes())==h for f,h in r['inputHashes'].items())
        assert H((w/'first.log').read_bytes())==r['logSHA256']
        assert r['inputHashes']['Tests/CurrentTests.swift']==a['proofSHA256']
    source=a['replacementTarget']
    assert len({r['inputHashes'][source] for r in arms.values()})==3
    for v in ('working','alternative'):
        assert arms[v]['exit']==0 and arms[v]['events']==['passed'],(i,v)
    d=arms['defect'];assert d['exit']==65 and d['events']==['failed'],i
    # Multiple XCTest expressions may share a source line. Check the actual reported failure,
    # not merely a nearby matching expression on that line.
    same_line_diagnostic={'Q024':'XCTAssertEqual failed', 'Q066':'("0") is not equal to ("1")',
                          'Q067':'"b"', 'Q072':'XCTAssertTrue failed','Q081':'XCTAssertTrue failed',
                          'Q083':'Ready','Q089':'("0") is not equal to ("1")','Q099':'XCTAssertFalse failed'}
    matched=[(line,diag) for line,diag in zip(d['witness'],d['diagnostics']) if row['assertionSubstring'] in line and same_line_diagnostic.get(i,'') in diag]
    assert matched,(i,d['witness'])
    results.append(dict(id=i,platform=d['platform'],observable=row['observable'],method=a['method'],anchor={k:d[k] for k in ('runtime','runtimeBuild','deployment','sdk','sdkBuild','xcode')}, outcomes={v:r['events'] for v,r in arms.items()},
                       source=a['assertionSource'],firstReceipts={v:H((directory/i/v/'result.json').read_bytes()) for v in arms},
                       witness=matched,proofSHA256=a['proofSHA256'],variants={v:r['inputHashes'][source] for v,r in arms.items()}))
assert len(results)==20
(D/'evidence.json').write_text(J(results))
print('20 working passes, 20 alternative passes, 20 assertion failures at specified witnesses.')

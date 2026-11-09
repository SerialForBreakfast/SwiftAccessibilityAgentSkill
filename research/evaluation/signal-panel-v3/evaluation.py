"""Export the original developer inputs, with no grades or routes. No inference."""
import argparse
from pathlib import Path
from zipfile import ZipFile
from hashlib import sha256
import sys

PACKET=Path(__file__).resolve().parent.parent/'signal-panel-v2/held.zip'
CASES={'panel':'P-34541ce79ee3d519','sheet':'P-90629dd9d60ff906','wrapper':'P-7d8c12fe30bd49a4',
       'media-ios':'P-d4bd274c3a345669','media-tvos':'P-dc1e54ce99c97729'}
if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('case',choices=CASES)
    key=CASES[p.parse_args().case]
    assert sha256(PACKET.read_bytes()).hexdigest()=='51bf28327715ad63929a107b9c8b3e3c364669916e3f2c0107f61b6300b45acd'
    with ZipFile(PACKET) as z:sys.stdout.buffer.write(z.read('subjects/'+key+'.txt'))

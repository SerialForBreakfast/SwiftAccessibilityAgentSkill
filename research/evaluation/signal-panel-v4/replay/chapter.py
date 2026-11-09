"""Append a test host after the verbatim answer fence to reach file-private decisions."""
from prepare import ROOT,H
from pathlib import Path
import json,sys,tempfile
base=ROOT/'evals/results/persistent-replay'
first=base/sys.argv[1]
out=Path(tempfile.mkdtemp(prefix='v4-chapter-',dir=base))
for old in sorted(first.glob('P-f93b*')):
    c=out/old.name;c.mkdir()
    meta=json.loads((old/'input.json').read_text());orig=(old/'Subject.swift').read_bytes()
    if old.name.endswith('v2'):
        adapter='''
extension PlaybackProgressView {
    @MainActor static func observe(_ from: Double, _ chapters: [Double], _ forward: Bool) -> Double {
        let v = Self(currentTime: .constant(from), duration: 160, chapterStarts: chapters, onTogglePlay: {})
        return forward ? v.nextPosition(from: from) : v.previousPosition(from: from)
    }
}
typealias Observed = PlaybackProgressView
'''
    else:
        adapter='''
extension ChapterScrubber {
    @MainActor static func observe(_ from: Double, _ chapters: [Double], _ forward: Bool) -> Double {
        var end = from
        let v = Self(currentTime: .constant(from), duration: 160, chapterStarts: chapters, isPlaying: false,
                     onTogglePlay: {}, onSeek: { end = $0 })
        if forward { v.stepForward() } else { v.stepBackward() }
        return end
    }
}
typealias Observed = ChapterScrubber
'''
    tests='''
import XCTest
@MainActor final class ChapterChecks: XCTestCase {
    func testInterior() {
        XCTAssertEqual(Observed.observe(35,[0,35,107],true),107)
        XCTAssertEqual(Observed.observe(35,[0,35,107],false),0)
    }
    func testOutward() {
        XCTAssertEqual(Observed.observe(107,[0,35,107],true),107)
        XCTAssertEqual(Observed.observe(0,[0,35,107],false),0)
    }
    func testEmptyPosition() {
        XCTAssertEqual(Observed.observe(35,[],true),35)
        XCTAssertEqual(Observed.observe(35,[],false),35)
    }
}
'''
    (c/'Subject.swift').write_text('// The unchanged source is hosted in the test target for private method access.\n')
    (c/'Contract.swift').write_bytes(orig+adapter.encode()+tests.encode())
    meta.update(selection='same-file controller probe',originalSubjectSHA256=H(orig),inputs={p.name:H(p.read_bytes()) for p in c.iterdir()})
    (c/'input.json').write_text(json.dumps(meta,indent=2))
print(out.name)

// Authoring utility only. Input is the documented local FFmpeg remux, not remote media.
import fs from 'node:fs';
import {createHash} from 'node:crypto';
const bytes = fs.readFileSync(process.argv[2]);
const root = new URL('./', import.meta.url);
const hash = b => createHash('sha256').update(b).digest('hex');
function atoms(b) {
  const out = [];
  for (let p = 0; p < b.length;) {
    if (p + 8 > b.length) throw Error('Truncated atom');
    const size = b.readUInt32BE(p);
    if (size < 8 || p + size > b.length) throw Error('Unsupported atom size');
    out.push({type: b.toString('ascii', p + 4, p + 8), bytes: b.subarray(p, p + size), body: b.subarray(p + 8, p + size)});
    p += size;
  }
  return out;
}
function box(type, body) {
  const header = Buffer.alloc(8); header.writeUInt32BE(body.length + 8); header.write(type, 4, 'ascii');
  return Buffer.concat([header, body]);
}
const top = atoms(bytes);
if (top.at(-1).type !== 'moov') throw Error('moov must be last to preserve media offsets');
let audioCount = 0;
const tag = box('tagc', Buffer.from('public.accessibility.describes-video', 'ascii'));
const tracks = atoms(top.at(-1).body).map(a => {
  if (a.type !== 'trak') return a.bytes;
  const children = atoms(a.body);
  const mdia = children.find(c => c.type === 'mdia');
  const handler = atoms(mdia.body).find(c => c.type === 'hdlr');
  if (handler.body.toString('ascii', 8, 12) !== 'soun' || ++audioCount !== 2) return a.bytes;
  const existing = children.find(c => c.type === 'udta');
  const body = children.map(c => c.type === 'udta' ? box('udta', Buffer.concat([c.body, tag])) : c.bytes);
  if (!existing) body.push(box('udta', tag));
  return box('trak', Buffer.concat(body));
});
if (audioCount !== 2) throw Error('Expected two audio tracks');
const tagged = Buffer.concat([...top.slice(0, -1).map(a => a.bytes), box('moov', Buffer.concat(tracks))]);
const encode = b => b.toString('base64').match(/.{1,96}/g).join('\n');
fs.writeFileSync(new URL('Tests/DescriptionFixture.swift', root), `import Foundation

// Silent synthetic media: validates metadata extraction, not narration quality.
enum DescriptionFixture {
    static func write(tagged: Bool) throws -> URL {
        let bytes = Data(base64Encoded: tagged ? positive : control, options: .ignoreUnknownCharacters)!
        let url = FileManager.default.temporaryDirectory.appendingPathComponent(UUID().uuidString).appendingPathExtension("mov")
        try bytes.write(to: url, options: .atomic)
        return url
    }
    private static let positive = """
${encode(tagged)}
"""
    private static let control = """
${encode(bytes)}
"""
}
`);
fs.writeFileSync(new URL('fixture-provenance.json', root), JSON.stringify({schema:1,kind:'synthetic-tagged-media',generator:'Existing FFmpeg8.0.1 remux plus this build-fixture.mjs; no installs',sourceFixture:'../uikit-media-v1/Tests/MediaFixture.swift',sourcePayloadHash:'eeb70b420ebc03ae18f82b7d799f1be4436a5abc2ffa56cddbfc381207406ec0',remuxCommand:'ffmpeg -nostdin -v error -i original.mp4 -map 0 -c copy -f mov untagged.mov',tagging:'Append documented tagc userdata to the second audio track; moov remains last, media offsets unchanged.',positive:{sha256:hash(tagged),bytes:tagged.length},control:{sha256:hash(bytes),bytes:bytes.length},limitations:'One second black video, silent en/es audio, synthetic captions. Tag is intentionally synthetic and does not establish audible description content or quality. Byte-identical remux across FFmpeg builds not promised.'},null,2)+'\n');

// Research companion only; does not modify released routing.
import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {hash} from './contracts.mjs';
const root = fileURLToPath(new URL('../../', import.meta.url));
const folders = {iOS: 'media-ios-v1', macOS: 'media-macos-v1', tvOS: 'media-tvos-v1'};
export function retrieve({platform, framework, topic, level = 'guidance'}, repository = root) {
  if (!['guidance', 'example', 'contract'].includes(level)) throw Error('Unknown disclosure level');
  if (framework !== 'SwiftUI' || !folders[platform] || !['selection', 'ownership', 'wiring'].includes(topic)) {
    return {status: 'unsupported', paths: [], trace: [], documents: [], loadedBytes: 0, tokens: null};
  }
  const base = 'code-examples/swiftui/' + folders[platform];
  const paths = [base + '/GUIDANCE.md'];
  if (level !== 'guidance') paths.push(base + '/Sources/MediaSelection.swift');
  if (level === 'contract') paths.push(base + '/manifest.json', base + '/Tests/MediaSelectionTests.swift', base + '/Tests/DescriptionFixture.swift');
  const resolved = fs.realpathSync(repository), trace = [], documents = [];
  for (const relative of paths) {
    const absolute = fs.realpathSync(path.join(resolved, relative));
    if (!absolute.startsWith(resolved + path.sep)) throw Error('Reference escapes repository');
    const bytes = fs.readFileSync(absolute);
    trace.push({path: relative, bytes: bytes.length, sha256: hash(bytes)});
    documents.push({path: relative, content: bytes.toString('utf8')});
  }
  return {status: 'selected', platform, framework, topic, level, paths, trace, documents,
    loadedBytes: trace.reduce((n, t) => n + t.bytes, 0), tokens: null};
}
if (process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url)) {
  const [platform, framework, topic, level, ...extra] = process.argv.slice(2);
  if (!platform || !framework || !topic || extra.length) throw Error('Usage: swiftui-media-retrieval.mjs PLATFORM SwiftUI TOPIC [guidance|example|contract]');
  console.log(JSON.stringify(retrieve({platform, framework, topic, level}), null, 2));
}

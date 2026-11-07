// Explicit metadata prototype, not an evaluated natural-language classifier.
import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {route as inherited} from '../0.3.0-dev.5/route.mjs';
import {hash} from '../../../../../code-examples/tools/contracts.mjs';
const root = fileURLToPath(new URL('../../../../../', import.meta.url));
const base = 'research/evaluation/failure-driven/candidates/0.3.0-dev.6/';
const platforms = {iOS: 'ios', macOS: 'macos', tvOS: 'tvos'};
const empty = status => ({status, paths: [], documents: [], trace: [], deliveredBytes: 0, tokens: null});
export function route(request, repository = root) {
  const {platform, framework, ownerFramework, topic, concern = 'overview', level = 'guidance',
    maxBytes = level === 'guidance' ? 12000 : 64000} = request;
  if (!['guidance', 'example', 'contract'].includes(level)) throw Error('Unknown disclosure level');
  if (!Number.isSafeInteger(maxBytes) || maxBytes < 1) throw Error('Positive integer byte budget required');
  if (framework === 'mixed' && !ownerFramework) return empty('needs-owner');
  const owner = framework === 'mixed' ? ownerFramework : framework;
  if (topic !== 'media' || owner !== 'SwiftUI') return {...inherited(request, repository), inheritedFrom: '0.3.0-dev.5'};
  const slug = platforms[platform];
  if (!slug || !['overview', 'selection', 'ownership', 'wiring'].includes(concern)) return empty('unsupported');
  const paths = [base + 'references/media-' + concern + '.md', base + 'references/sdk-' + slug + '.md'];
  const example = 'code-examples/swiftui/media-' + slug + '-v2/';
  if (level !== 'guidance') paths.push(example + 'Sources/MediaSelection.swift');
  if (level === 'contract') paths.push(example + 'manifest.json', example + 'Tests/MediaSelectionTests.swift',
    example + 'Tests/ReviewRegressionTests.swift', example + 'Tests/DescriptionFixture.swift');
  const repo = fs.realpathSync(repository);
  const files = paths.map(relative => {
    const absolute = fs.realpathSync(path.join(repo, relative));
    if (!absolute.startsWith(repo + path.sep) || !fs.statSync(absolute).isFile()) throw Error('Unsafe reference');
    return {path: relative, absolute, bytes: fs.statSync(absolute).size};
  });
  const plannedBytes = files.reduce((n, f) => n + f.bytes, 0);
  if (plannedBytes > maxBytes) return {...empty('budget-exceeded'), paths, plannedBytes};
  const trace = [], documents = [];
  for (const f of files) {
    const bytes = fs.readFileSync(f.absolute);
    trace.push({path: f.path, bytes: bytes.length, sha256: hash(bytes)});
    documents.push({path: f.path, content: bytes.toString('utf8')});
  }
  return {status: 'selected', platform, framework: owner, topic, concern, level, paths, trace, documents,
    deliveredBytes: trace.reduce((n, t) => n + t.bytes, 0), tokens: null,
    scope: 'Reviewed media-selection extension only; broader media APIs require additional target-specific sources.'};
}
if (process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url)) {
  const [platform, framework, topic, concern, level, ...extra] = process.argv.slice(2);
  if (!platform || !framework || !topic || extra.length) throw Error('Usage: route.mjs PLATFORM FRAMEWORK TOPIC [CONCERN] [LEVEL]');
  console.log(JSON.stringify(route({platform, framework, topic, concern, level}), null, 2));
}

// Additive candidate routes; the earlier platform router and its evidence stay pinned.
import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {retrieve as previous} from './platform-retrieval.mjs';
import {hash} from './contracts.mjs';
const root = fileURLToPath(new URL('../../', import.meta.url));
const routes = {
  'macOS:AppKit:table-selection': ['macos-navigation-v1','DesktopNavigation','macos/m-006-table-outline-list-semantics.md'],
  'macOS:AppKit:key-order': ['macos-navigation-v1','DesktopNavigation','macos/m-002-keyboard-focus-order.md'],
  'tvOS:UIKit:filtered-results': ['tvos-results-v1','TelevisionResults','tvos/t-006-search-filter-collection-semantics.md'],
  'tvOS:UIKit:motion-status': ['tvos-results-v1','TelevisionResults','tvos/t-008-reduce-motion-focus-animations.md']
};
export function retrieve(request, repository = root) {
  const {platform, framework, topic, level = 'guidance'} = request;
  if (!['guidance','example','contract'].includes(level)) throw Error('Choose guidance, example or contract');
  const route = routes[`${platform}:${framework}:${topic}`];
  if (!route) return previous(request, repository);
  const [folder, stem, guideline] = route, [family, name] = guideline.split('/');
  const paths = [`references/${family}/guidelines/${name}`], base = `code-examples/platforms/${folder}`;
  if (level !== 'guidance') paths.push(`${base}/Sources/${stem}.swift`);
  if (level === 'contract') paths.push(`${base}/manifest.json`,`${base}/Tests/${stem}Tests.swift`);
  const trace = [], documents = [], resolvedRoot = fs.realpathSync(repository);
  for (const relative of paths) {
    const absolute = fs.realpathSync(path.join(resolvedRoot,relative));
    if (!absolute.startsWith(resolvedRoot+path.sep)) throw Error('Reference escapes repository');
    const bytes = fs.readFileSync(absolute);
    trace.push({path:relative,bytes:bytes.length,sha256:hash(bytes)});
    documents.push({path:relative,content:bytes.toString('utf8')});
  }
  return {status:'selected',platform,framework,topic,level,paths,trace,documents,
    loadedBytes:trace.reduce((n,r)=>n+r.bytes,0),tokens:null};
}
if (process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url)) {
  const [platform,framework,topic,level,...extra] = process.argv.slice(2);
  if (!platform || !framework || !topic || extra.length) throw Error('Usage: navigation-retrieval.mjs PLATFORM FRAMEWORK TOPIC [guidance|example|contract]');
  console.log(JSON.stringify(retrieve({platform,framework,topic,level}),null,2));
}

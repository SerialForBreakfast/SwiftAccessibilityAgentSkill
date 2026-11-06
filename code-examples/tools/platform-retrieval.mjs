// Candidate retrieval only. This does not alter the released skill's routing.
import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {hash} from './contracts.mjs';
const root = fileURLToPath(new URL('../../', import.meta.url));
const routes = {
  'macOS:AppKit': {
    actions: ['m-001-nsaccessibility-roles-labels-values-actions.md', 'm-003-grouping-hierarchy-desktop-layouts.md'],
    notifications: ['m-004-announcements-state-change-notifications.md']
  },
  'tvOS:UIKit': {
    actions: ['t-005-custom-actions-remote-first.md', 't-003-labels-values-traits-focused-controls.md'],
    focus: ['t-001-focus-order-directional-navigation.md', 't-002-initial-focus-modal-restoration.md'],
    traits: ['t-003-labels-values-traits-focused-controls.md']
  }
};
const packages = {
  'macOS:AppKit': {folder:'macos-appkit-v1', stem:'DesktopActions', guidance:'macos'},
  'tvOS:UIKit': {folder:'tvos-uikit-v1', stem:'TelevisionActions', guidance:'tvos'}
};
export function select({platform, framework, topic, level = 'guidance'}) {
  if (!['guidance', 'example', 'contract'].includes(level)) throw Error('Choose guidance, example or contract');
  const key = `${platform}:${framework}`, item = packages[key];
  if (!item) return {status:'clarify', paths:[], reason:'Specify AppKit on macOS or UIKit on tvOS. Catalyst, SwiftUI and mixed boundaries require their own guidance; no platform fallback.'};
  const guidelines = routes[key][topic];
  if (!guidelines) return {status:'unsupported-topic', paths:[], reason:'No companion contract for this topic yet; do not substitute a different platform.'};
  const paths = guidelines.map(g=>`references/${item.guidance}/guidelines/${g}`);
  const base = `code-examples/platforms/${item.folder}`;
  if (level !== 'guidance') paths.push(`${base}/Sources/${item.stem}.swift`);
  if (level === 'contract') paths.push(`${base}/manifest.json`, `${base}/Tests/${item.stem}Tests.swift`);
  return {status:'selected', platform, framework, topic, level, paths};
}
export function retrieve(request, repository = root) {
  const selection = select(request), trace = [], documents = [];
  for (const relative of selection.paths) {
    const base = fs.realpathSync(repository), absolute = fs.realpathSync(path.join(base, relative));
    if (!absolute.startsWith(base + path.sep)) throw Error('Reference escapes repository');
    const bytes = fs.readFileSync(absolute);
    trace.push({path:relative, bytes:bytes.length, sha256:hash(bytes)});
    documents.push({path:relative, content:bytes.toString('utf8')});
  }
  return {...selection, trace, loadedBytes:trace.reduce((n,r)=>n+r.bytes,0), tokens:null, documents};
}
if (process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url)) {
  const [platform, framework, topic, level, ...extra] = process.argv.slice(2);
  if (!platform || !framework || !topic || extra.length) throw Error('Usage: platform-retrieval.mjs PLATFORM FRAMEWORK TOPIC [guidance|example|contract]');
  console.log(JSON.stringify(retrieve({platform, framework, topic, level}), null, 2));
}

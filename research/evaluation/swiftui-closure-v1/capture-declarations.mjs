import fs from 'node:fs';
import {spawnSync} from 'node:child_process';
import {hash} from '../../../code-examples/tools/contracts.mjs';
const records = [];
const queries = [
  ['AVPlayerItem.h', '- (void)selectMediaOption:', 'AVPlayerItem.select'],
  ['AVPlayerItem.h', '@property (readonly) AVMediaSelection *currentMediaSelection', 'AVPlayerItem.currentMediaSelection'],
  ['AVAsset.h', '- (void)loadMediaSelectionGroupForMediaCharacteristic:', 'AVAsset.loadMediaSelectionGroup'],
  ['AVMediaSelectionGroup.h', '@property (nonatomic, readonly) BOOL allowsEmptySelection;', 'AVMediaSelectionGroup.allowsEmptySelection'],
  ['AVMediaFormat.h', 'AVF_EXPORT AVMediaCharacteristic const AVMediaCharacteristicContainsOnlyForcedSubtitles API_AVAILABLE', 'forced-only characteristic']
];
for (const [platform, sdk] of [['macOS', 'macosx'], ['iOS', 'iphonesimulator'], ['tvOS', 'appletvsimulator']]) {
  const p = spawnSync('xcrun', ['--sdk', sdk, '--show-sdk-path'], {encoding: 'utf8', timeout: 10000});
  if (p.status !== 0) throw Error('Installed SDK path unavailable');
  for (const [header, selector, api] of queries) {
    const file = p.stdout.trim() + '/System/Library/Frameworks/AVFoundation.framework/Headers/' + header;
    const bytes = fs.readFileSync(file), lines = bytes.toString().split('\n');
    const i = lines.findIndex(line => line.startsWith(selector));
    if (i < 0) throw Error('Exact declaration unavailable: ' + platform + '/' + api);
    let end = i;
    while (!lines[end].includes(';') && end < i + 20) end++;
    const declaration = lines.slice(i, end + 1).join('\n');
    const annotations = [...declaration.matchAll(/API_(?:AVAILABLE|DEPRECATED|UNAVAILABLE)\([^;]+/g)].map(m => m[0]);
    records.push({platform, api, selector, file, fileSha256: hash(bytes), status: 'declaration-located',
      line: i + 1, declaration, excerpt: lines.slice(Math.max(0, i - 4), end + 1).join('\n'),
      annotations, introduction: annotations.length ? 'Exact declaration annotations retained; no nearby-comment inference.' :
        'No member-level annotation; enclosing declaration introduction not resolved in this capture.',
      deploymentTarget: '26.0', sdk: '27.0', evidenceScope: 'Header declaration and separate compile receipt; not runtime behavioral introduction.'});
  }
}
fs.writeFileSync('research/evaluation/swiftui-closure-v1/declarations.json',
  JSON.stringify({schema: 1, retrievedOn: '2026-11-07', records}, null, 2) + '\n');

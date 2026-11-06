import fs from 'node:fs';
import path from 'node:path';
import {spawnSync} from 'node:child_process';
import {fileURLToPath} from 'node:url';
import {hash} from '../../../../code-examples/tools/contracts.mjs';
import {selectedPackages} from '../../../../code-examples/tools/campaign-core.mjs';

const here = path.dirname(fileURLToPath(import.meta.url));
const sdkProbe = spawnSync('xcrun', ['--sdk','iphonesimulator','--show-sdk-path'], {encoding:'utf8'});
if (sdkProbe.status !== 0) throw Error('SDK unavailable');
const sdk = sdkProbe.stdout.trim(), names = new Map();
for (const pkg of [...selectedPackages(process.cwd()), 'research/evaluation/failure-driven/uikit-closure-v1/gap-contracts']) {
  const manifest = JSON.parse(fs.readFileSync(pkg + '/manifest.json'));
  for (const f of manifest.files.filter(f => f.path.startsWith('Sources/') && f.path.endsWith('.swift'))) {
    const source = fs.readFileSync(pkg + '/' + f.path, 'utf8');
    for (const name of source.match(/\b(?:UI|AV|NS|CG|CM|CA)[A-Z]\w*/g) ?? []) {
      if (['UIKit','AVKit','AVFoundation'].includes(name)) continue;
      const row = names.get(name) ?? {name, usages: []};
      if (!row.usages.some(u => u.path === pkg + '/' + f.path)) row.usages.push({path:pkg + '/' + f.path, sha256:f.sha256});
      names.set(name,row);
    }
  }
}
const rows = [];
for (const row of names.values()) {
  const pattern = `(@interface|@protocol)[[:space:]]+${row.name}([[:space:]:<]|$)|typedef[[:space:]]+(struct|enum)[[:space:]]+_?${row.name}([[:space:]{]|$)`;
  const found = spawnSync('rg', ['-n','--glob','*.h',pattern,path.join(sdk,'System/Library/Frameworks')], {encoding:'utf8',maxBuffer:8*1024*1024});
  if (![0,1].includes(found.status)) throw Error('Declaration search failed');
  const declarations = (found.stdout.trim() ? found.stdout.trim().split('\n') : []).map(line => {
    const m = line.match(/^(.*):(\d+):(.*)$/), bytes = fs.readFileSync(m[1]), lines = bytes.toString().split('\n'), at = Number(m[2]);
    return {path:m[1].slice(sdk.length+1), line:at, sha256:hash(bytes),
      context:lines.slice(Math.max(0,at-5),at+2),
      scope:'Type/protocol declaration context only; do not apply adjacent annotations to individual members.'};
  });
  rows.push({...row, declarations, status:declarations.length ? 'type-declaration-located' : 'explicit-unresolved-or-function-namespace',
    independentReview:'pending'});
}
fs.writeFileSync(path.join(here,'type-declarations.json'), JSON.stringify({schema:1,
  scope:'Lexical Apple-prefixed identifiers in production sources. Modules excluded; includes C functions/constants and namespaces explicitly when no type declaration exists. Member AST inventory is complementary.', rows},null,2)+'\n');
console.log(JSON.stringify({identifiers:rows.length,located:rows.filter(r=>r.declarations.length).length}));

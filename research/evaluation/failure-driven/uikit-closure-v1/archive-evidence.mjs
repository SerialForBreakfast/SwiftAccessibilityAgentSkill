import fs from 'node:fs';
import path from 'node:path';
import {spawnSync} from 'node:child_process';
import {hash} from '../../../../code-examples/tools/contracts.mjs';
const [root,output] = process.argv.slice(2);
if (!root || !output || !path.isAbsolute(root) || !path.isAbsolute(output)) throw Error('Pass completed private root and new private archive path');
if (fs.existsSync(output) || fs.existsSync(output+'.partial') || fs.existsSync(path.join(root,'execution.lock')))
  throw Error('Archive exists or campaign is running');
const plan=JSON.parse(fs.readFileSync(path.join(root,'plan.json'))), entries=['plan.json','plan.sha256','index.json','snapshot'];
for(const c of plan.checks) {
  const r=JSON.parse(fs.readFileSync(path.join(root,c.key,'result.json')));
  entries.push(c.key+'/result.json',...r.artifacts.map(a=>c.key+'/'+a.path));
  for(const extra of [c.key+'/tests.xcresult',c.key+'-adapter-process.json'])
    if(fs.existsSync(path.join(root,extra))) entries.push(extra);
}
const archived=spawnSync('tar',['-czf',output+'.partial','-C',root,...new Set(entries)],{encoding:'utf8',timeout:300000});
if(archived.status!==0 || archived.error || archived.signal) throw Error('Archive incomplete; partial retained');
fs.chmodSync(output+'.partial',0o600);
fs.linkSync(output+'.partial',output);fs.unlinkSync(output+'.partial');
console.log(JSON.stringify({bytes:fs.statSync(output).size,sha256:hash(fs.readFileSync(output)),
  scope:'Frozen inputs, adapters, raw diagnostics, receipts and xcresults; disposable build intermediates excluded.'}));

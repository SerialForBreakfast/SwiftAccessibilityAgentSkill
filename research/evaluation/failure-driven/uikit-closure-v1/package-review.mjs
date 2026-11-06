import fs from 'node:fs';
import path from 'node:path';
import {spawnSync} from 'node:child_process';
import {hash} from '../../../../code-examples/tools/contracts.mjs';
import {selectedPackages} from '../../../../code-examples/tools/campaign-core.mjs';
const [output] = process.argv.slice(2);
if (!output || !path.isAbsolute(output) || fs.existsSync(output)) throw Error('Pass a new private ZIP path');
const base='research/evaluation/failure-driven/uikit-closure-v1';
if (!fs.existsSync(base+'/execution.json')) throw Error('Execution report required before review submission');
const inputs=new Set();
function collect(file) {
  const stat=fs.lstatSync(file);
  if(stat.isSymbolicLink()) throw Error('Unexpected symlink in review packet');
  if(stat.isDirectory()) for(const name of fs.readdirSync(file).filter(n=>!n.startsWith('.'))) collect(file+'/'+name);
  else if(stat.isFile() && !file.endsWith('/packet-manifest.json') && !file.endsWith('/delivery.json')) inputs.add(file);
}
for(const file of [...selectedPackages(process.cwd()),base,'code-examples/tools',
  'code-examples/audits/requirements-v1/inventory.json','references/uikit/guidelines']) collect(file);
const files=[...inputs].sort();
const manifest={schema:1,scope:'Public/synthetic source and sanitized evidence; no original model answers, credentials or private onboarding files.',
  reviewStatus:'prepared-awaiting-submission',files:files.map(file=>({path:file,sha256:hash(fs.readFileSync(file))}))};
fs.writeFileSync(base+'/packet-manifest.json',JSON.stringify(manifest,null,2)+'\n',{flag:'wx'});
const zip=spawnSync('zip',['-q',output,...files,base+'/packet-manifest.json'],{encoding:'utf8',timeout:120000});
if(zip.status!==0 || zip.error || zip.signal) throw Error('Review ZIP incomplete; retain attempt');
console.log(JSON.stringify({files:files.length+1,bytes:fs.statSync(output).size,sha256:hash(fs.readFileSync(output))}));

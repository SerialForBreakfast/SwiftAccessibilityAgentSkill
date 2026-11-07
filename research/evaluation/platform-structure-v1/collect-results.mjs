// Collect existing native results; never launches tests or changes source inputs.
import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {hash, validateResult} from '../../../code-examples/tools/contracts.mjs';
const repository=fileURLToPath(new URL('../../../',import.meta.url));
const output=fileURLToPath(new URL('.',import.meta.url));
const base=process.argv[2];
if(!base || !path.isAbsolute(base))throw Error('Supply an absolute directory containing immutable platform attempts');
const attempts=[];
for(const name of fs.readdirSync(base).filter(n=>/^structure-(mac|tv)-[a-z-]+-r\d+$/.test(n)).sort()) {
  const dir=path.join(base,name);
  if(!fs.existsSync(path.join(dir,'result.json')))throw Error('Incomplete attempt: '+name);
  const raw=fs.readFileSync(path.join(dir,'result.json')),r=JSON.parse(raw);
  const manifestBytes=fs.readFileSync(path.join(dir,'manifest.json')),m=JSON.parse(manifestBytes);
  validateResult(m,hash(manifestBytes),r,dir);
  const summaryPath=path.join(dir,'summary.json');
  const failures=fs.existsSync(summaryPath)?(JSON.parse(fs.readFileSync(summaryPath)).testFailures??[]).map(f=>({test:f.testIdentifierString,diagnostic:f.failureText.replace(/0x[0-9a-f]+/gi,'<address>')})):[];
  attempts.push({attempt:name,originalResultHash:hash(raw),manifestHash:r.manifestHash,package:m.id,revision:m.revision,checkId:r.checkId,recordedAt:r.recordedAt,status:r.status,observed:r.observed,reason:r.reason??null,environment:r.environment??null,execution:r.execution??null,failures,artifacts:r.artifacts});
}
function walk(dir){return fs.readdirSync(dir,{withFileTypes:true}).filter(e=>!e.name.startsWith('.')).flatMap(e=>e.isDirectory()?walk(path.join(dir,e.name)):e.isFile()&&/\.(swift|md|json|mjs|txt)$/.test(e.name)?[path.join(dir,e.name)]:[]);}
const files=[...['macos-structure-v1','tvos-structure-v1'].flatMap(p=>walk(path.join(repository,'code-examples/platforms',p))), ...fs.readdirSync(path.join(repository,'code-examples/tools')).filter(n=>/^structure(-retrieval|\.test)\.mjs$/.test(n)&&n.endsWith('.mjs')).map(n=>path.join(repository,'code-examples/tools',n)),...walk(path.join(output,'incidents'))];
const pins=files.sort().map(p=>({path:path.relative(repository,p),sha256:hash(fs.readFileSync(p))}));
const index={schema:1,recordedAt:new Date().toISOString(),scope:'Native form recovery and collection configuration on AppKit/macOS and UIKit/tvOS; no released skill or frozen baseline changes',attempts,pins};
fs.writeFileSync(path.join(output,'results-index.json'),JSON.stringify(index,null,2)+'\n');
console.log(JSON.stringify({attempts:attempts.length,passed:attempts.filter(a=>a.status==='passed').length,failed:attempts.filter(a=>a.status==='failed').length,blocked:attempts.filter(a=>a.status==='blocked').length,pins:pins.length}));

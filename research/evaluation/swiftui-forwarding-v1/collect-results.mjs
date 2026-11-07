// Collect validated native receipts only; never starts execution or repairs.
import fs from 'node:fs';import path from 'node:path';import {hash,validateResult,artifact} from '../../../code-examples/tools/contracts.mjs';
const base='research/evaluation/swiftui-forwarding-v1/',roots=process.argv.slice(2);if(!roots.length||roots.some(r=>!path.isAbsolute(r)))throw Error('Supply absolute roots containing immutable swiftui attempts');
const attempts=[],seen=new Set();
for(const root of roots){for(const name of fs.readdirSync(root).filter(n=>/^sui-forward-(mac|ios|tv)-[a-z-]+-r\d+$/.test(n)).sort()){
 const dir=path.join(root,name);if(!fs.existsSync(dir+'/result.json'))throw Error('Incomplete attempt '+name);
 const bytes=fs.readFileSync(dir+'/manifest.json'),m=JSON.parse(bytes),raw=fs.readFileSync(dir+'/result.json'),r=JSON.parse(raw);validateResult(m,hash(bytes),r,dir);for(const a of r.artifacts??[])artifact(dir,a);if(seen.has(hash(raw)))continue;seen.add(hash(raw));
 const summary=fs.existsSync(dir+'/summary.json')?JSON.parse(fs.readFileSync(dir+'/summary.json')):null;
 attempts.push({attempt:name,originalResultHash:hash(raw),manifestHash:r.manifestHash,package:m.id,revision:m.revision,checkId:r.checkId,status:r.status,observed:r.observed,reason:r.reason??null,recordedAt:r.recordedAt,environment:r.environment??null,execution:r.execution??null,failures:(summary?.testFailures??[]).map(f=>({test:f.testIdentifierString,diagnostic:f.failureText.replace(/0x[0-9a-f]+/gi,'<address>')})),artifacts:r.artifacts});
 }}
function walk(root){return fs.readdirSync(root,{withFileTypes:true}).filter(e=>!e.name.startsWith('.')).flatMap(e=>e.isDirectory()?walk(root+'/'+e.name):[root+'/'+e.name]);}
const files=[...['forwarding-shared-v1','forwarding-macos-v1','forwarding-ios-v1','forwarding-tvos-v1'].flatMap(f=>walk('code-examples/swiftui/'+f)),...['swiftui-forwarding-campaign.mjs','swiftui-forwarding-retrieval.mjs'].map(n=>'code-examples/tools/'+n),...walk(base+'incidents')];
const pins=files.sort().map(path=>({path,sha256:hash(fs.readFileSync(path))}));fs.writeFileSync(base+'results-index.json',JSON.stringify({schema:1,recordedAt:new Date().toISOString(),scope:'SwiftUI native code contracts, not generated accessibility semantics or model qualification',attempts,pins},null,2)+'\n');console.log({attempts:attempts.length,passed:attempts.filter(r=>r.status==='passed').length,failed:attempts.filter(r=>r.status==='failed').length,pins:pins.length});

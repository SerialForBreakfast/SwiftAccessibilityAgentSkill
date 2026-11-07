// Archives verified receipt files and original result bundles, excluding build caches.
import fs from 'node:fs';import path from 'node:path';import {spawnSync} from 'node:child_process';import {hash,validateResult} from '../../../code-examples/tools/contracts.mjs';
const [destination,...roots]=process.argv.slice(2);if(!destination||!path.isAbsolute(destination)||!roots.length||roots.some(r=>!path.isAbsolute(r)))throw Error('Supply new private destination and absolute attempt roots');
fs.mkdirSync(destination,{mode:0o700});const stage=destination+'/contents';fs.mkdirSync(stage);const seen=new Set(),names=[];
for(const root of roots)for(const name of fs.readdirSync(root).filter(n=>/^sui-forward-(mac|ios|tv)-[a-z-]+-r\d+$/.test(n)).sort()){
 const from=root+'/'+name,raw=fs.readFileSync(from+'/result.json'),bytes=fs.readFileSync(from+'/manifest.json'),m=JSON.parse(bytes),r=JSON.parse(raw);validateResult(m,hash(bytes),r,from);if(seen.has(hash(raw)))continue;seen.add(hash(raw));names.push(name);const to=stage+'/'+name;fs.mkdirSync(to);
 for(const a of [...r.artifacts,{path:'result.json',sha256:hash(raw)}]){const target=to+'/'+a.path;fs.mkdirSync(path.dirname(target),{recursive:true});fs.copyFileSync(from+'/'+a.path,target);if(hash(fs.readFileSync(target))!==a.sha256)throw Error('Copy mismatch');}
 if(fs.existsSync(from+'/tests.xcresult'))fs.cpSync(from+'/tests.xcresult',to+'/tests.xcresult',{recursive:true,filter:p=>path.basename(p)!=='.DS_Store'});validateResult(m,hash(bytes),r,to);
}
const planRoot=roots.find(r=>fs.existsSync(r+'/plan.json'));if(planRoot){
 for(const name of ['plan.json','plan.sha256'])fs.copyFileSync(planRoot+'/'+name,stage+'/'+name);
 const plan=JSON.parse(fs.readFileSync(planRoot+'/plan.json'));
 for(const f of plan.inputs){const bytes=fs.readFileSync(planRoot+'/snapshot/'+f.path);if(hash(bytes)!==f.sha256)throw Error('Frozen snapshot mismatch');const target=stage+'/snapshot/'+f.path;fs.mkdirSync(path.dirname(target),{recursive:true});fs.writeFileSync(target,bytes,{flag:'wx'});}
}
for(const file of ['build-forwarding.mjs','build-forwarding-r2.mjs','build-forwarding-r3.mjs','build-forwarding-r4.mjs','forwarding-tests.mjs','forwarding-pairs.mjs','forward-heading-probe.swift','forward-heading-correct.swift'])if(fs.existsSync('/private/tmp/'+file))fs.copyFileSync('/private/tmp/'+file,stage+'/'+file);
const archive=destination+'/native-attempts-r1.tar.gz',r=spawnSync('tar',['-czf',archive,'-C',stage,'.'],{encoding:'utf8'});if(r.status!==0)throw Error(r.stderr);const bytes=fs.readFileSync(archive);const receipt={archive:archive.replace(process.env.HOME,'~'),sha256:hash(bytes),bytes:bytes.length,attempts:names.length,includes:'Verified original sources, commands, adapters, first failures, repaired attempts, XCTest bundles and frozen plan; regenerable build caches excluded.',private:true};fs.writeFileSync('research/evaluation/swiftui-forwarding-v1/archive-receipt.json',JSON.stringify(receipt,null,2)+'\n');console.log(receipt);

// Preserve complete receipt inputs and result bundles, not regenerable build caches.
import fs from 'node:fs';import path from 'node:path';import {spawnSync} from 'node:child_process';import {hash,validateResult} from '../../../code-examples/tools/contracts.mjs';
const [source,destination]=process.argv.slice(2);if(!source||!destination||!path.isAbsolute(source)||!path.isAbsolute(destination))throw Error('Supply absolute attempt source and new private archive directory');
fs.mkdirSync(destination,{mode:0o700});const stage=path.join(destination,'contents');fs.mkdirSync(stage,{mode:0o700});
const names=fs.readdirSync(source).filter(n=>/^closure-(mac|tv|ios|detail|recovery)-[a-z-]+-r\d+$/.test(n)).sort();
for(const name of names){const from=path.join(source,name),to=path.join(stage,name);const b=fs.readFileSync(path.join(from,'manifest.json')),m=JSON.parse(b),r=JSON.parse(fs.readFileSync(path.join(from,'result.json')));validateResult(m,hash(b),r,from);fs.mkdirSync(to);
 for(const f of [...r.artifacts,{path:'result.json',sha256:hash(fs.readFileSync(path.join(from,'result.json')))}]){const target=path.join(to,f.path);fs.mkdirSync(path.dirname(target),{recursive:true});fs.copyFileSync(path.join(from,f.path),target);if(hash(fs.readFileSync(target))!==f.sha256)throw Error('Archive copy mismatch');}
 if(fs.existsSync(path.join(from,'tests.xcresult')))fs.cpSync(path.join(from,'tests.xcresult'),path.join(to,'tests.xcresult'),{recursive:true,filter:p=>path.basename(p)!=='.DS_Store'});
 validateResult(m,hash(b),r,to);
}
fs.cpSync('/private/tmp/closure-apple-sources',path.join(stage,'sources'),{recursive:true});
for(const f of ['run-closure.mjs','run-closure-tail.mjs','repair-tv-state.mjs'])if(fs.existsSync('/private/tmp/'+f))fs.copyFileSync('/private/tmp/'+f,path.join(stage,f));
const archive=path.join(destination,'native-attempts-r1.tar.gz'),r=spawnSync('tar',['-czf',archive,'-C',stage,'.'],{encoding:'utf8'});if(r.status!==0)throw Error(r.stderr);
const b=fs.readFileSync(archive);const receipt={archive:archive.replace(process.env.HOME,'~'),sha256:hash(b),bytes:b.length,attempts:names.length,includes:'Verified source inputs, manifests, adapter snapshots, diagnostics, summaries, xcresults, Apple markdown and author runner scripts. Regenerable build caches excluded.',private:true};
fs.writeFileSync('research/evaluation/cross-platform-closure-v1/archive-receipt.json',JSON.stringify(receipt,null,2)+'\n');console.log(JSON.stringify(receipt));

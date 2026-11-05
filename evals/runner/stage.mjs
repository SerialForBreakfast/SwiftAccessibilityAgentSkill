import fs from 'node:fs';import path from 'node:path';
import {repo,verifyBaseline,hash,fingerprint} from './lib.mjs';
const [mode,destination]=process.argv.slice(2);
if(mode!=='knowledge'||!destination)throw Error('Usage: node stage.mjs knowledge NEW_DIRECTORY');
verifyBaseline();
const overlay=path.join(repo,'evals/candidates/knowledge'),manifest=JSON.parse(fs.readFileSync(path.join(overlay,'manifest.json')));
for(const f of manifest.files)if(hash(fs.readFileSync(path.join(overlay,'files',f.path)))!==f.sha256)throw Error('Overlay hash mismatch');
fs.mkdirSync(destination);
fs.cpSync(path.join(repo,'evals/baselines/0.2.2/files'),destination,{recursive:true});
for(const f of manifest.files){const out=path.join(destination,f.path);fs.mkdirSync(path.dirname(out),{recursive:true});fs.copyFileSync(path.join(overlay,'files',f.path),out);}
console.log(JSON.stringify({stage:'knowledge-only',skillHash:fingerprint(destination)},null,2));

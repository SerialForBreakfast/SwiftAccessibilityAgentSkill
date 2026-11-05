import fs from 'node:fs';import path from 'node:path';
import {repo} from './lib.mjs';
export function checkSources(){
 const registry=fs.readFileSync(path.join(repo,'references/core/sources/registry.md'),'utf8');
 const ids=[...registry.matchAll(/^\| ([A-Z][A-Z0-9-]+) \|/gm)].map(m=>m[1]);
 if(new Set(ids).size!==ids.length)throw Error('Duplicate source ID');
 const audit=JSON.parse(fs.readFileSync(path.join(repo,'evals/evidence/registry-audit.json')));
 const allowed=['reviewed-scoped','reviewed-report','discovery-only','historical-reference','access-limited','replaced-source'];
 for(const row of audit.sources){
  if(!allowed.includes(row.status)||!row.scope||!row.reviewedAt)throw Error('Incomplete audit disposition: '+row.id);
  if(!row.retrieval?.sha256||!/^[a-f0-9]{64}$/.test(row.retrieval.sha256))throw Error('Missing retrieval fingerprint: '+row.id);
  if(row.status==='reviewed-scoped'&&row.retrieval.httpStatus!==200)throw Error('Unsuccessful reviewed retrieval: '+row.id);
 }
 let mirrored=0;function walk(dir){for(const e of fs.readdirSync(dir,{withFileTypes:true})){const f=path.join(dir,e.name);if(e.isDirectory())walk(f);else if(e.isFile()&&f.endsWith('.md')){
 const s=fs.readFileSync(f,'utf8');for(const m of s.matchAll(/\[((?:APPLE|ASC|CVS|SWIFTLEE|HWS|MAJID|USEYOURLOAF|CASHAPP|ADA|AXE|A11YSIG|STACKOVERFLOW|COMMUNITY)[A-Z0-9-]+)\]/g))if(!ids.includes(m[1]))throw Error('Undefined source '+m[1]);
 const twin=path.join(repo,'docs',path.relative(path.join(repo,'references'),f));if(fs.existsSync(twin)){const normalized=x=>x.replaceAll('references/','docs/');if(normalized(s)!==normalized(fs.readFileSync(twin,'utf8')))throw Error('Doc mirror drift: '+f);mirrored++;}
 }}}walk(path.join(repo,'references'));
 return {auditedSources:audit.sources.length,registeredSources:ids.length,mirroredDocuments:mirrored,dispositions:Object.fromEntries(allowed.map(k=>[k,audit.sources.filter(r=>r.status===k).length]))};
}

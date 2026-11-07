import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {createHash} from 'node:crypto';
import {route} from '../failure-driven/candidates/0.3.0-dev.5/route.mjs';
import {median} from './compare.mjs';
const root=fileURLToPath(new URL('../../../',import.meta.url)),base='research/evaluation/failure-driven/candidates/0.3.0-dev.5/';
const read=p=>fs.readFileSync(path.join(root,p));const hash=b=>createHash('sha256').update(b).digest('hex');
export function context(){
 const m=JSON.parse(read(base+'candidate.json')),catalog=JSON.parse(read(base+'routes.json'));
 if(hash(read(m.subject.path))!==m.subject.sha256)throw Error('Candidate snapshot drift');
 const old='research/evaluation/failure-driven/candidates/0.3.0-dev.2/ENTRYPOINT.md';
 const prior=read(old).toString();const body=prior.includes('<!-- SUBJECT START -->')?prior.split('<!-- SUBJECT START -->')[1].split('<!-- SUBJECT END -->')[0].trim():null;
 if(body===null)throw Error('Expected marked prior subject body');
 const beforeBytes=Buffer.byteLength(body),rows=catalog.routes.map(r=>{
  const result=route(r);if(result.status!=='selected')return {platform:r.platform,framework:r.framework,topic:r.topic,status:result.status,tokens:null,trace:result.trace};
  const guide=result.trace.find(t=>t.path===r.guideline),before=beforeBytes+guide.bytes,after=m.subject.bytes+result.deliveredBytes;
  return {platform:r.platform,framework:r.framework,topic:r.topic,status:'selected',beforeBytes:before,afterBytes:after,byteChange:after/before-1,tokens:null,trace:result.trace};
 });
 return {schema:1,scope:'Static same-guideline byte comparison with actual offline reference reads; not autonomous model retrieval or provider tokens',candidate:base,prior:{path:old,sha256:hash(read(old)),bodyBytes:beforeBytes},candidateBodyBytes:m.subject.bytes,rows,medianByteChange:median(rows.filter(r=>r.status==='selected').map(r=>r.byteChange)),tokenTargetStatus:'unmeasured',modelCalls:0};
}
if(process.argv[1]&&path.resolve(process.argv[1])===fileURLToPath(import.meta.url))console.log(JSON.stringify(context(),null,2));

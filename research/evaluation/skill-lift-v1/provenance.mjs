import {createHash} from 'node:crypto';
const hash=b=>createHash('sha256').update(b).digest('hex');
export function auditAccess({claimedReads=[],claimedSupplied=[],supplied=[],events=[]}){
 const verifiedReads=[],offlineReads=[],invalidEvents=[];
 for(const event of events){
  if(!['instrumented-tool-read','offline-lookup'].includes(event.kind)||typeof event.path!=='string'||typeof event.content!=='string'||event.bytes!==Buffer.byteLength(event.content)||event.sha256!==hash(event.content)||event.success!==true){invalidEvents.push(event.path??'unknown');continue;}
  (event.kind==='instrumented-tool-read'?verifiedReads:offlineReads).push(event.path);
 }
 const suppliedPaths=supplied.filter(s=>typeof s.path==='string'&&typeof s.content==='string'&&s.sha256===hash(s.content)).map(s=>s.path);
 return {verifiedReads:[...new Set(verifiedReads)],offlineReads:[...new Set(offlineReads)],unverifiedReadClaims:claimedReads.filter(p=>!verifiedReads.includes(p)),unverifiedSuppliedClaims:claimedSupplied.filter(p=>!suppliedPaths.includes(p)),invalidEvents,semanticApplication:'requires-answer-review',scope:'Validates captured read records; does not authenticate their origin or prove the model used the guidance correctly.'};
}

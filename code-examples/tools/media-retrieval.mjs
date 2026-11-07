// Candidate companion retrieval; AVFoundation evidence is explicit, not a UI-framework substitute.
import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {retrieve as previous} from './lifecycle-retrieval.mjs';
import {hash} from './contracts.mjs';
const root=fileURLToPath(new URL('../../',import.meta.url));
const stems={'media-selection':'MediaChoice','media-metadata':'MediaMetadata','media-inspection':'MediaInspection'};
export function retrieve(request,repository=root){
 const {platform,framework,topic,level='guidance'}=request;
 if(!['guidance','example','contract'].includes(level))throw Error('Choose guidance, example or contract');
 const stem=stems[topic];
 const native=platform==='macOS'?'AppKit':platform==='tvOS'?'UIKit':null;
 if(!stem||!native||![native,'AVFoundation'].includes(framework))return previous(request,repository);
 const base=`code-examples/platforms/${platform==='macOS'?'macos':'tvos'}-media-v1`;
 const paths=[`${base}/GUIDANCE.md`];
 if(level!=='guidance')paths.push(`${base}/Sources/${stem}.swift`);
 if(level==='contract'){
  paths.push(`${base}/manifest.json`,`${base}/Tests/${stem}Tests.swift`);
  if(stem!=='MediaInspection')paths.push(`${base}/Tests/DescriptionFixture.swift`);
 }
 const trace=[],documents=[],resolved=fs.realpathSync(repository);
 for(const relative of paths){
  const absolute=fs.realpathSync(path.join(resolved,relative));
  if(!absolute.startsWith(resolved+path.sep))throw Error('Reference escapes repository');
  const bytes=fs.readFileSync(absolute);trace.push({path:relative,bytes:bytes.length,sha256:hash(bytes)});documents.push({path:relative,content:bytes.toString('utf8')});
 }
 return {status:'selected',platform,framework,evidenceFramework:'AVFoundation',topic,level,paths,trace,documents,loadedBytes:trace.reduce((n,r)=>n+r.bytes,0),tokens:null};
}
if(process.argv[1]&&path.resolve(process.argv[1])===fileURLToPath(import.meta.url)){
 const [platform,framework,topic,level,...extra]=process.argv.slice(2);
 if(!platform||!framework||!topic||extra.length)throw Error('Usage: media-retrieval.mjs PLATFORM FRAMEWORK TOPIC [guidance|example|contract]');
 console.log(JSON.stringify(retrieve({platform,framework,topic,level}),null,2));
}

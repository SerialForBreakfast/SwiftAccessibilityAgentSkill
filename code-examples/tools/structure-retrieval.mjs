// Additive candidate only; released skill routing and previous evidence stay unchanged.
import fs from 'node:fs';import path from 'node:path';import {fileURLToPath} from 'node:url';
import {hash} from './contracts.mjs';import {retrieve as previous} from './media-retrieval.mjs';
const root=fileURLToPath(new URL('../../',import.meta.url));
const routes={
 'macOS:AppKit:form-recovery':['macos-structure-v1','DesktopForm'],
 'macOS:AppKit:outline-structure':['macos-structure-v1','DesktopOutline'],
 'tvOS:UIKit:form-recovery':['tvos-structure-v1','TelevisionForm'],
 'tvOS:UIKit:shelf-structure':['tvos-structure-v1','TelevisionShelves']
};
export function retrieve(request,repository=root){
 const {platform,framework,topic,level='guidance'}=request;
 if(!['guidance','example','contract'].includes(level))throw Error('Choose guidance, example or contract');
 const route=routes[`${platform}:${framework}:${topic}`];if(!route)return previous(request,repository);
 const [folder,stem]=route,base='code-examples/platforms/'+folder,paths=[base+'/GUIDANCE.md'];
 if(level!=='guidance')paths.push(`${base}/Sources/${stem}.swift`);
 if(level==='contract')paths.push(`${base}/manifest.json`,`${base}/Tests/${stem}Tests.swift`);
 const trace=[],documents=[],resolved=fs.realpathSync(repository);
 for(const relative of paths){const absolute=fs.realpathSync(path.join(resolved,relative));if(!absolute.startsWith(resolved+path.sep))throw Error('Reference escapes repository');const bytes=fs.readFileSync(absolute);trace.push({path:relative,bytes:bytes.length,sha256:hash(bytes)});documents.push({path:relative,content:bytes.toString('utf8')});}
 return {status:'selected',platform,framework,topic,level,paths,trace,documents,loadedBytes:trace.reduce((n,t)=>n+t.bytes,0),tokens:null};
}
if(process.argv[1]&&path.resolve(process.argv[1])===fileURLToPath(import.meta.url)){
 const [platform,framework,topic,level,...extra]=process.argv.slice(2);if(!platform||!framework||!topic||extra.length)throw Error('Usage: structure-retrieval.mjs PLATFORM FRAMEWORK TOPIC [guidance|example|contract]');console.log(JSON.stringify(retrieve({platform,framework,topic,level}),null,2));
}

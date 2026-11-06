// Additive candidate only; released skill routing and previous evidence stay unchanged.
import fs from 'node:fs';import path from 'node:path';import {fileURLToPath} from 'node:url';
import {hash} from './contracts.mjs';import {retrieve as previous} from './structure-retrieval.mjs';
const root=fileURLToPath(new URL('../../',import.meta.url));
const routes={
 "tvOS:UIKit:state-recovery": ["tvos-state-recovery-v1", "StateContracts", "StateContract"],
 "macOS:AppKit:row-metadata": ["macos-closure-details-v1", "DesktopRow", "DesktopContract"],
 "macOS:AppKit:keyboard-action": ["macos-closure-details-v1", "StateContracts", "DesktopContract"],
  "iOS:UIKit:validation-ownership": [
    "ios-closure-v1",
    "AsyncOwnership",
    "AsyncOwnership"
  ],
  "iOS:UIKit:media-load-ownership": [
    "ios-closure-v1",
    "AsyncOwnership",
    "AsyncOwnership"
  ],
  "macOS:AppKit:validation-ownership": [
    "macos-closure-v1",
    "AsyncOwnership",
    "AsyncOwnership"
  ],
  "macOS:AppKit:media-load-ownership": [
    "macos-closure-v1",
    "AsyncOwnership",
    "AsyncOwnership"
  ],
  "macOS:AppKit:text-rotor": [
    "macos-closure-v1",
    "DesktopText",
    "DesktopText"
  ],
  "macOS:AppKit:native-state": [
    "macos-closure-v1",
    "StateContracts",
    "StateContract"
  ],
  "tvOS:UIKit:validation-ownership": [
    "tvos-closure-v1",
    "AsyncOwnership",
    "AsyncOwnership"
  ],
  "tvOS:UIKit:media-load-ownership": [
    "tvos-closure-v1",
    "AsyncOwnership",
    "AsyncOwnership"
  ],
  "tvOS:UIKit:text-rotor": [
    "tvos-closure-v1",
    "EditedRotorUIKit",
    "EditedRotorUIKit"
  ],
  "tvOS:UIKit:native-state": [
    "tvos-state-recovery-v1",
    "StateContracts",
    "StateContract"
  ]
};
export function retrieve(request,repository=root){
 const {platform,framework,topic,level='guidance'}=request;
 if(!['guidance','example','contract'].includes(level))throw Error('Choose guidance, example or contract');
 const route=routes[`${platform}:${framework}:${topic}`];if(!route)return previous(request,repository);
 const [folder,stem,testStem]=route,base='code-examples/platforms/'+folder,paths=[base+'/GUIDANCE.md'];
 if(level!=='guidance')paths.push(`${base}/Sources/${stem}.swift`);
 if(level==='contract')paths.push(`${base}/manifest.json`,`${base}/Tests/${testStem}Tests.swift`);
 const trace=[],documents=[],resolved=fs.realpathSync(repository);
 for(const relative of paths){const absolute=fs.realpathSync(path.join(resolved,relative));if(!absolute.startsWith(resolved+path.sep))throw Error('Reference escapes repository');const bytes=fs.readFileSync(absolute);trace.push({path:relative,bytes:bytes.length,sha256:hash(bytes)});documents.push({path:relative,content:bytes.toString('utf8')});}
 return {status:'selected',platform,framework,topic,level,paths,trace,documents,loadedBytes:trace.reduce((n,t)=>n+t.bytes,0),tokens:null};
}
if(process.argv[1]&&path.resolve(process.argv[1])===fileURLToPath(import.meta.url)){
 const [platform,framework,topic,level,...extra]=process.argv.slice(2);if(!platform||!framework||!topic||extra.length)throw Error('Usage: closure-retrieval.mjs PLATFORM FRAMEWORK TOPIC [guidance|example|contract]');console.log(JSON.stringify(retrieve({platform,framework,topic,level}),null,2));
}

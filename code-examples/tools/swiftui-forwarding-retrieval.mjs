// Candidate repository tool only. Released skill routing is unchanged.
import fs from 'node:fs';import path from 'node:path';import {fileURLToPath} from 'node:url';import {hash} from './contracts.mjs';
const root=fileURLToPath(new URL('../../',import.meta.url));
const folders={iOS:'forwarding-ios-v1',macOS:'forwarding-macos-v1',tvOS:'forwarding-tvos-v1'};
const stems={'native-metadata':'NativeSurface','native-actions':'NativeSurface','preference-forwarding':'PreferenceSurface'};
export function retrieve({platform,framework,topic,level='guidance'},repository=root){
 if(!['guidance','example','contract'].includes(level))throw Error('Unknown disclosure level');
 const folder=folders[platform],stem=stems[topic];if(framework!=='SwiftUI'||!folder||!stem)return {status:'unsupported',paths:[],trace:[],documents:[],loadedBytes:0,tokens:null};
 const base='code-examples/swiftui/'+folder,paths=[base+'/GUIDANCE.md'];
 if(level!=='guidance')paths.push(base+'/Sources/'+stem+'.swift');
 if(level==='contract')paths.push(base+'/manifest.json',base+'/Tests/'+'ForwardingTests'+'.swift');
 const trace=[],documents=[],resolved=fs.realpathSync(repository);
 for(const relative of paths){const absolute=fs.realpathSync(path.join(resolved,relative));if(!absolute.startsWith(resolved+path.sep))throw Error('Reference escapes repository');const bytes=fs.readFileSync(absolute);trace.push({path:relative,bytes:bytes.length,sha256:hash(bytes)});documents.push({path:relative,content:bytes.toString('utf8')});}
 return {status:'selected',platform,framework,topic,level,paths,trace,documents,loadedBytes:trace.reduce((n,t)=>n+t.bytes,0),tokens:null};
}
if(process.argv[1]&&path.resolve(process.argv[1])===fileURLToPath(import.meta.url)){const [platform,framework,topic,level,...extra]=process.argv.slice(2);if(!platform||!framework||!topic||extra.length)throw Error('Usage: swiftui-forwarding-retrieval.mjs PLATFORM SwiftUI TOPIC [guidance|example|contract]');console.log(JSON.stringify(retrieve({platform,framework,topic,level}),null,2));}

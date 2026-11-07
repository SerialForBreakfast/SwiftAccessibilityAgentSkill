// Explicit, bounded native campaign. No installs, model execution or automatic repairs.
import fs from 'node:fs';import path from 'node:path';import os from 'node:os';import {spawnSync} from 'node:child_process';import {fileURLToPath} from 'node:url';
import {hash,validateManifest,validateResult} from './contracts.mjs';
import {selectDestination as iosDestination} from './native-core.mjs';import {selectDestination as tvDestination} from './platform-core.mjs';
const root=fileURLToPath(new URL('../../',import.meta.url));
const packages=['media-macos-v2','media-ios-v2','media-tvos-v2'];
const adapters=['swiftui-media-review-campaign.mjs','swiftui-media-native.mjs','native-core.mjs','swiftui-media-platform-native.mjs','platform-core.mjs','contracts.mjs','swiftui-media-diagnostics.mjs'];
const [mode,output,ios,tv,...extra]=process.argv.slice(2);
if(!['freeze','run'].includes(mode)||!output||!path.isAbsolute(output)||!ios||!tv||extra.length)throw Error('Usage: swiftui-media-review-campaign.mjs freeze|run PRIVATE_ROOT IOS26_UUID TV26_UUID');
function probe(cmd,args){const r=spawnSync(cmd,args,{encoding:'utf8',timeout:120000});if(r.status!==0||r.error||r.signal)throw Error('Environment probe failed: '+cmd);return r.stdout.trim();}
function environment(){const devices=JSON.parse(probe('xcrun',['simctl','list','devices','available','--json'])),runtimes=JSON.parse(probe('xcrun',['simctl','list','runtimes','--json']));return {xcode:probe('xcodebuild',['-version']),compiler:probe('xcrun',['swiftc','--version']),architecture:os.arch(),host:{version:probe('sw_vers',['-productVersion']),build:probe('sw_vers',['-buildVersion'])},iOS:{...iosDestination(devices,runtimes,ios,26),uuid:ios},tvOS:{...tvDestination(devices,runtimes,tv,26),uuid:tv},sdks:Object.fromEntries(['macosx','iphonesimulator','appletvsimulator'].map(s=>[s,{version:probe('xcrun',['--sdk',s,'--show-sdk-version']),build:probe('xcrun',['--sdk',s,'--show-sdk-build-version'])}]))};}
function inputs(){return [...adapters.map(n=>'code-examples/tools/'+n),...packages.flatMap(p=>{const dir='code-examples/swiftui/'+p,m=JSON.parse(fs.readFileSync(root+dir+'/manifest.json'));validateManifest(m,root+dir);return [dir+'/manifest.json',...m.files.map(f=>dir+'/'+f.path)];})].map(p=>({path:p,sha256:hash(fs.readFileSync(root+p))}));}
function same(a,b,label){if(JSON.stringify(a)!==JSON.stringify(b))throw Error(label);}
if(mode==='freeze'){
 const plan={schema:1,createdAt:new Date().toISOString(),packages,inputs:inputs(),environment:environment()};fs.mkdirSync(output,{mode:0o700});
 for(const p of plan.inputs){const target=path.join(output,'snapshot',p.path);fs.mkdirSync(path.dirname(target),{recursive:true});fs.writeFileSync(target,fs.readFileSync(root+p.path),{flag:'wx',mode:0o400});}
 const bytes=JSON.stringify(plan,null,2)+'\n';fs.writeFileSync(path.join(output,'plan.json'),bytes,{flag:'wx',mode:0o400});fs.writeFileSync(path.join(output,'plan.sha256'),hash(bytes),{flag:'wx',mode:0o400});console.log('Frozen three-platform SwiftUI campaign; no native checks executed.');
}else{
 const bytes=fs.readFileSync(path.join(output,'plan.json'));if(hash(bytes)!==fs.readFileSync(path.join(output,'plan.sha256'),'utf8'))throw Error('Plan hash mismatch');const plan=JSON.parse(bytes);
 same(plan.packages,packages,'Package selection changed');same(plan.inputs,inputs(),'Input fingerprint changed');same(plan.environment,environment(),'Environment fingerprint changed');
 for(const f of plan.inputs)if(hash(fs.readFileSync(path.join(output,'snapshot',f.path)))!==f.sha256)throw Error('Snapshot changed');
 const lock=path.join(output,'execution.lock');fs.writeFileSync(lock,JSON.stringify({pid:process.pid}),{flag:'wx',mode:0o600});
 try{for(const p of packages){const manifest='code-examples/swiftui/'+p+'/manifest.json',b=fs.readFileSync(path.join(output,'snapshot',manifest)),m=JSON.parse(b);
  for(const c of m.checks){same(plan.inputs,inputs(),'Inputs changed during campaign');const lane=m.platform==='macOS'?'mac':m.platform==='tvOS'?'tv':'ios',prefix=p.includes('details')?'detail':p.includes('state-recovery')?'recovery':lane,dir=path.join(output,`sui-media-review-${prefix}-${c.id}-r${m.revision}`),result=path.join(dir,'result.json');
   if(fs.existsSync(dir)&&!fs.existsSync(result))throw Error('Incomplete immutable attempt: '+path.basename(dir));
   if(!fs.existsSync(result)){const adapter=m.platform==='iOS'?'swiftui-media-native.mjs':'swiftui-media-platform-native.mjs',uuid=m.platform==='iOS'?ios:m.platform==='tvOS'?tv:null;const r=spawnSync(process.execPath,[path.join(output,'snapshot/code-examples/tools',adapter),'execute',path.join(output,'snapshot',manifest),c.id,dir,...(uuid?[uuid]:[])],{encoding:'utf8',timeout:900000,maxBuffer:4*1024*1024});fs.writeFileSync(dir+'-process.json',JSON.stringify({exit:r.status,signal:r.signal,error:r.error?.code??null,stdout:r.stdout,stderr:r.stderr}),{flag:'wx',mode:0o600});if(r.signal||r.error||!fs.existsSync(result))throw Error('Infrastructure failure retained');}
   const r=JSON.parse(fs.readFileSync(result));validateResult(m,hash(b),r,dir);
   if(['blocked','error','skipped'].includes(r.status))throw Error('Native execution stopped: '+r.status);
   const env=r.environment,sdk=plan.environment.sdks[{iOS:'iphonesimulator',tvOS:'appletvsimulator',macOS:'macosx'}[m.platform]];
   for(const k of ['xcode','compiler','architecture'])same(env[k],plan.environment[k],'Recorded environment mismatch: '+k);
   same(env.sdkVersion,sdk.version,'SDK mismatch');same(env.sdkBuild,sdk.build,'SDK build mismatch');
   if(c.lane==='unit'){const runtime=m.platform==='macOS'?plan.environment.host:plan.environment[m.platform];same(env.runtimeVersion,runtime.version,'Runtime mismatch');same(env.runtimeBuild,runtime.build,'Runtime build mismatch');}
   console.log(JSON.stringify({package:p,check:c.id,status:r.status}));
   if(r.execution?.build==='failed')throw Error('Compilation defect retained; repair requires new revision and new campaign root');
  }
 }}finally{fs.unlinkSync(lock);}
}

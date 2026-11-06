// Explicit, serial native unit validation; no provider calls or UI-test targets.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {spawnSync} from 'node:child_process';
import {fileURLToPath} from 'node:url';
const source=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'../os26/fixtures');
const manifest=JSON.parse(fs.readFileSync(path.join(source,'manifest.json')));
const hash=b=>crypto.createHash('sha256').update(b).digest('hex');
const args=process.argv.slice(2);
if(args[0]!=='--execute') {
  console.log(JSON.stringify({execute:false,jobs:manifest.cases.flatMap(c=>['candidate','mutation-1','mutation-2'].map(variant=>({case:c.id,platform:c.platform,testId:c.testId,variant})))},null,2));
  process.exit(0);
}
const [output,ios,tvos]=args.slice(1);
if(args.length!==4 || !output || !path.isAbsolute(output) || fs.existsSync(output) || !ios || !tvos)throw Error('Use --execute NEW_ABSOLUTE_OUTPUT IOS26_UUID TVOS26_UUID');
function run(command,argv,options={}) {
  return spawnSync(command,argv,{encoding:'utf8',timeout:600000,killSignal:'SIGKILL',maxBuffer:32*1024*1024,...options});
}
const inventory=run('xcrun',['simctl','list','devices','available','--json']);
if(inventory.status!==0)throw Error('Cannot verify destinations');
const devices=JSON.parse(inventory.stdout).devices;
for(const [platform,id] of [['iOS',ios],['tvOS',tvos]]) {
  if(!Object.entries(devices).some(([runtime,list])=>runtime.includes(`.${platform}-26-`) && list.some(d=>d.udid===id)))throw Error('Destination is not installed OS26: '+platform);
}
fs.mkdirSync(output,{recursive:true,mode:0o700});
fs.writeFileSync(path.join(output,'devices.json'),inventory.stdout);
fs.writeFileSync(path.join(output,'xcode.txt'),run('xcodebuild',['-version']).stdout);
fs.writeFileSync(path.join(output,'swift.txt'),run('xcrun',['swift','--version']).stdout);
fs.copyFileSync(path.join(source,'manifest.json'),path.join(output,'fixture-manifest.json'));
fs.writeFileSync(path.join(output,'catalog-pins.json'),JSON.stringify({
  promptHash:hash(fs.readFileSync(path.join(source,'../prompts.json'))),
  acceptanceHash:hash(fs.readFileSync(path.join(source,'../acceptance.json')))
},null,2),{flag:'wx'});
const workspace=path.join(output,'workspace');fs.mkdirSync(workspace);
for(const name of ['Sources','Tests','Package.swift'])fs.cpSync(path.join(source,name),path.join(workspace,name),{recursive:true});
const testFiles=fs.readdirSync(path.join(source,'Tests/OS26FixturesTests')).sort();
const testSuiteHash=hash(testFiles.map(f=>f+'\n'+fs.readFileSync(path.join(source,'Tests/OS26FixturesTests',f),'utf8')).join('\n'));
const results=[];
for(const c of manifest.cases) {
  for(const variant of [c.candidate,...c.mutations]) {
    const id=variant.id??'candidate',stem=c.id+'-'+id;
    const bytes=fs.readFileSync(path.join(source,variant.path));
    if(hash(bytes)!==variant.sha256)throw Error('Fixture hash mismatch');
    fs.writeFileSync(path.join(workspace,c.candidate.path),bytes);
    const bundle=path.join(output,stem+'.xcresult');
    const command=['test','-scheme','OS26Fixtures','-destination',`platform=${c.platform} Simulator,id=${c.platform==='iOS'?ios:tvos}`,
      '-derivedDataPath',path.join(output,'DerivedData'),'-resultBundlePath',bundle,
      '-parallel-testing-enabled','NO','-collect-test-diagnostics','never',
      '-only-testing:OS26FixturesTests/'+c.testId,'CODE_SIGNING_ALLOWED=NO'];
    fs.writeFileSync(path.join(output,stem+'-intent.json'),JSON.stringify({case:c.id,variant:id,variantHash:variant.sha256,testSuiteHash,command,expectedFailureTestIds:id==='candidate'?[]:[c.testId]},null,2),{flag:'wx'});
    const result=run('xcodebuild',command,{cwd:workspace});
    const log=(result.stdout??'')+(result.stderr??'');
    fs.writeFileSync(path.join(output,stem+'.log'),log);
    const summaryResult=fs.existsSync(bundle)?run('xcrun',['xcresulttool','get','test-results','summary','--path',bundle,'--format','json']):null;
    let summary=null;try{if(summaryResult?.status===0)summary=JSON.parse(summaryResult.stdout);}catch{}
    if(summary)fs.writeFileSync(path.join(output,stem+'-summary.json'),JSON.stringify(summary,null,2));
    const match=[...log.matchAll(/Test Case '-\[OS26FixturesTests\.(\w+) (\w+)\]' (passed|failed)/g)];
    const executedTestIds=match.map(m=>m[1]+'/'+m[2]);
    const failedTestIds=match.filter(m=>m[3]==='failed').map(m=>m[1]+'/'+m[2]);
    const assertionFailure=log.includes('XCTAssert') && failedTestIds.length===1 && failedTestIds[0]===c.testId;
    const validCount=summary?.totalTestCount===1 && summary.skippedTests===0 && executedTestIds.length===1 && executedTestIds[0]===c.testId;
    const observed=validCount && result.status===0 && summary.failedTests===0?'pass':
      validCount && result.status===65 && summary.failedTests===1 && assertionFailure?'fail':'error';
    const record={case:c.id,variant:id,variantHash:variant.sha256,testSuiteHash,executedTestIds,failedTestIds,
      expectedFailureTestIds:id==='candidate'?[]:[c.testId],observed,expected:variant.expected,exitCode:result.status,
      signal:result.signal,error:result.error?.code??null,logHash:hash(log),summary};
    results.push(record);fs.writeFileSync(path.join(output,'results.json'),JSON.stringify(results,null,2));
    console.log(JSON.stringify({case:c.id,variant:id,observed,expected:variant.expected}));
    fs.copyFileSync(path.join(source,c.candidate.path),path.join(workspace,c.candidate.path));
    if(observed==='error')throw Error('Native infrastructure or unclassified failure; stopped: '+stem);
  }
}

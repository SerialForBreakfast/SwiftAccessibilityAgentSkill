// Assemble real native evidence only. Review gates intentionally remain pending.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {fileURLToPath, pathToFileURL} from 'node:url';
export function assemble(directory) {
const root=path.resolve(directory),base=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'../os26');
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
const prompts=fs.readFileSync(path.join(base,'prompts.json'));
const acceptanceBytes=fs.readFileSync(path.join(base,'acceptance.json'));
const acceptance=JSON.parse(acceptanceBytes);
const manifestBytes=fs.readFileSync(path.join(root,'fixture-manifest.json'));
const currentManifest=fs.readFileSync(path.join(base,'fixtures/manifest.json'));
if(!manifestBytes.equals(currentManifest))throw Error('Stale fixture manifest');
const tests=path.join(base,'fixtures/Tests/OS26FixturesTests');
const currentSuiteHash=sha(fs.readdirSync(tests).sort().map(f=>f+'\n'+fs.readFileSync(path.join(tests,f),'utf8')).join('\n'));
const manifest=JSON.parse(manifestBytes);
for(const fixture of manifest.cases)for(const variant of [fixture.candidate,...fixture.mutations]) {
  if(sha(fs.readFileSync(path.join(base,'fixtures',variant.path)))!==variant.sha256)throw Error('Current source differs from fixture manifest');
}
const records=JSON.parse(fs.readFileSync(path.join(root,'results.json')));
if(records.length!==manifest.cases.length*3 || new Set(records.map(r=>r.case+'/'+r.variant)).size!==records.length)throw Error('Incomplete or duplicate native matrix');
const xcode=fs.readFileSync(path.join(root,'xcode.txt'),'utf8').trim();
if(!/^Xcode .+\nBuild version .+$/m.test(xcode))throw Error('Missing Xcode identity');
const evidence={schema:1,promptHash:sha(prompts),acceptanceHash:sha(acceptanceBytes),cases:[]};
for(const fixture of manifest.cases) {
  const good=records.find(r=>r.case===fixture.id && r.variant==='candidate');
  if(!good || good.observed!=='pass')throw Error('Candidate did not pass');
  const candidateLog=fs.readFileSync(path.join(root,fixture.id+'-candidate.log'),'utf8');
  const sdk=candidateLog.match(/(?:iPhoneSimulator|AppleTVSimulator)[\d.]+\.sdk/)?.[0];
  if(!sdk)throw Error('Missing SDK identity');
  const caseRecord={id:fixture.id,fixtureAuthor:'BigDog-original/Sillycon-revision2',
    sdkBuild:xcode.replaceAll('\n','; ')+'; '+sdk,runtimeBuild:good.summary?.devicesAndConfigurations?.[0]?.device?.osBuildNumber??'',
    fixtureHash:sha(manifestBytes),checks:[]};
  for(const gate of acceptance.cases.find(c=>c.id===fixture.id).gates) {
    if(gate.kind==='review') {caseRecord.checks.push({id:gate.id,method:'review',observed:'not_run',artifacts:[]});continue;}
    const variant=gate.id.startsWith('mutation-')?gate.id:'candidate';
    const record=records.find(r=>r.case===fixture.id && r.variant===variant);
    if(!record || record.observed!==gate.expected)throw Error('Unexpected native outcome');
    const passing=record.observed==='pass';
    if(record.exitCode!==(passing?0:65) || record.signal!==null || record.error!==null ||
       record.summary?.passedTests!==(passing?1:0) || record.summary?.failedTests!==(passing?0:1) ||
       JSON.stringify(record.failedTestIds)!==JSON.stringify(passing?[]:[fixture.testId]) ||
       JSON.stringify(record.expectedFailureTestIds)!==JSON.stringify(passing?[]:[fixture.testId]))throw Error('Invalid native execution outcome');
    if(record.testSuiteHash!==currentSuiteHash)throw Error('Stale test suite');
    if(record.summary?.totalTestCount!==1 || record.summary?.skippedTests!==0 ||
       record.testSuiteHash!==good.testSuiteHash ||
       JSON.stringify(record.executedTestIds)!==JSON.stringify([fixture.testId]))throw Error('Native test selection mismatch');
    const definition=variant==='candidate'?fixture.candidate:fixture.mutations.find(m=>m.id===variant);
    if(record.variantHash!==definition.sha256)throw Error('Variant identity mismatch');
    const logName=fixture.id+'-'+variant+'.log',log=fs.readFileSync(path.join(root,logName));
    if(sha(log)!==record.logHash)throw Error('Native log mismatch');
    const intentName=fixture.id+'-'+variant+'-intent.json';
    const intentBytes=fs.readFileSync(path.join(root,intentName));
    const intent=JSON.parse(intentBytes);
    if(intent.variantHash!==record.variantHash || intent.testSuiteHash!==record.testSuiteHash ||
       JSON.stringify(intent.expectedFailureTestIds)!==JSON.stringify(record.expectedFailureTestIds))throw Error('Native intent mismatch');
    const check={id:gate.id,method:gate.kind==='oracle'?'unit':gate.kind,observed:record.observed,
      variantHash:record.variantHash,artifacts:[{path:logName,sha256:sha(log)},{path:intentName,sha256:sha(intentBytes)}]};
    if(check.method==='unit')check.execution={buildOutcome:'pass',testSuiteHash:record.testSuiteHash,
      executedTestIds:record.executedTestIds,failedTestIds:record.failedTestIds,
      expectedFailureTestIds:record.expectedFailureTestIds,outcome:record.observed==='pass'?'passed':'assertion_failed'};
    caseRecord.checks.push(check);
  }
  // No independentReviewer is invented: actual review must be supplied separately.
  evidence.cases.push(caseRecord);
}
return evidence;
}
if(process.argv[1] && import.meta.url===pathToFileURL(process.argv[1]).href) {
  const [directory]=process.argv.slice(2);
  if(!directory || process.argv.length!==3)throw Error('Usage: node os26-native-receipts.mjs PRIVATE_RUN_DIRECTORY');
  const evidence=assemble(directory);
  fs.writeFileSync(path.join(directory,'native-evidence-pending-review.json'),JSON.stringify(evidence,null,2),{flag:'wx'});
  console.log(JSON.stringify({cases:evidence.cases.length,review:'pending',promotion:false}));
}

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
if(!manifestBytes.equals(fs.readFileSync(path.join(base,'fixtures/manifest.json'))))throw Error('Stale fixture manifest');
const catalog=JSON.parse(fs.readFileSync(path.join(root,'catalog-pins.json')));
if(catalog.promptHash!==sha(prompts) || catalog.acceptanceHash!==sha(acceptanceBytes))throw Error('Stale prompt or acceptance catalog');
const suiteHash=directory=>{
  const names=fs.readdirSync(directory).sort();
  return sha(names.map(name=>name+'\n'+fs.readFileSync(path.join(directory,name),'utf8')).join('\n'));
};
const currentSuiteHash=suiteHash(path.join(base,'fixtures/Tests/OS26FixturesTests'));
if(suiteHash(path.join(root,'workspace/Tests/OS26FixturesTests'))!==currentSuiteHash)throw Error('Stale snapshotted test suite');
const manifest=JSON.parse(manifestBytes);
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
    if(record.summary?.totalTestCount!==1 || record.summary?.skippedTests!==0 ||
       record.testSuiteHash!==currentSuiteHash ||
       JSON.stringify(record.executedTestIds)!==JSON.stringify([fixture.testId]))throw Error('Native test selection mismatch');
    const failed=record.observed==='fail';
    if(record.signal!==null || record.error!==null || record.exitCode!==(failed?65:0) ||
       record.summary.passedTests!==(failed?0:1) || record.summary.failedTests!==(failed?1:0) ||
       JSON.stringify(record.failedTestIds)!==JSON.stringify(failed?[fixture.testId]:[]) ||
       JSON.stringify(record.expectedFailureTestIds)!==JSON.stringify(variant==='candidate'?[]:[fixture.testId]))throw Error('Native process/count mismatch');
    const definition=variant==='candidate'?fixture.candidate:fixture.mutations.find(m=>m.id===variant);
    if(record.variantHash!==definition.sha256)throw Error('Variant identity mismatch');
    if(sha(fs.readFileSync(path.join(base,'fixtures',definition.path)))!==definition.sha256)throw Error('Current source differs from fixture manifest');
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

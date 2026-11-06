import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {hash} from '../../../../code-examples/tools/contracts.mjs';
import {verifyInputs, verifyReceipt, classify} from '../../../../code-examples/tools/campaign-core.mjs';

const here = path.dirname(fileURLToPath(import.meta.url));
const roots = process.argv.slice(2);
if (!roots.length || roots.some(r => !path.isAbsolute(r))) throw Error('Pass completed private campaign roots');
const rows = [], campaigns = [];
for (const root of roots) {
  if (fs.existsSync(path.join(root, 'execution.lock'))) throw Error('Campaign still running');
  const bytes = fs.readFileSync(path.join(root, 'plan.json'));
  if (hash(bytes) !== fs.readFileSync(path.join(root, 'plan.sha256'), 'utf8')) throw Error('Plan drift');
  const plan = JSON.parse(bytes);
  verifyInputs(path.join(root, 'snapshot'), [...plan.inputs, ...plan.adapters]);
  const campaign = hash(bytes);
  const {uuid, ...environment} = plan.environment;
  campaigns.push({planHash: campaign, environment, inputs: plan.inputs, adapters: plan.adapters,
    checks: plan.checks.length, packages: plan.packages, parentPlanHash: plan.parentPlanHash ?? null});
  for (const c of plan.checks) {
    const pkg = plan.packages.find(p => p.key === c.package), output = path.join(root, c.key);
    const resultBytes = fs.readFileSync(path.join(output, 'result.json')), r = JSON.parse(resultBytes);
    const manifest = JSON.parse(fs.readFileSync(path.join(root, 'snapshot', pkg.path, 'manifest.json')));
    verifyReceipt(manifest, pkg.manifestHash, r, output, plan.environment);
    rows.push({campaign, package: pkg.path, key: c.key, check: c.check, manifestHash: pkg.manifestHash,
      lane: c.lane, expected: c.expected, status: r.status, observed: r.observed,
      classification: classify(r, c), recordedAt: r.recordedAt, environment: r.environment,
      execution: r.execution, originalRecordHash: hash(resultBytes), artifacts: r.artifacts,
      attempt: 1, repairs: 0});
  }
}
const positive = rows.filter(r => r.lane === 'unit' && r.expected === 'success');
const methods = new Set(positive.flatMap(r => (r.execution?.executedTestIds ?? []).map(id => r.package + ':' + id)));
const result = {schema: 1, status: 'executed-not-independent-acceptance',
  privacy: 'Private roots and simulator UUID omitted; original receipts and snapshots retained privately. Artifact paths are relative to each receipt root.',
  campaigns, counts: {packages: new Set(rows.map(r => r.package)).size, checks: rows.length,
    positiveUnitChecks: positive.length, uniquePositiveMethods: methods.size,
    negativeChecks: rows.filter(r => r.expected === 'failure').length,
    compileChecks: rows.filter(r => r.lane === 'compile').length,
    repeatedMethodExecutionsIncludingNegatives: rows.reduce((n,r) => n + (r.execution?.executedTestIds?.length ?? 0), 0),
    unexpectedOutcomes: rows.filter(r => !['positive-pass','intended-negative-rejection'].includes(r.classification)).length}, rows};
fs.writeFileSync(path.join(here, 'execution.json'), JSON.stringify(result, null, 2) + '\n', {flag:'wx'});
console.log(JSON.stringify(result.counts));

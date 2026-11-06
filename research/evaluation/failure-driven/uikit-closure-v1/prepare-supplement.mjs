import fs from 'node:fs';
import path from 'node:path';
import {hash} from '../../../../code-examples/tools/contracts.mjs';
import {inventory, verifyInputs} from '../../../../code-examples/tools/campaign-core.mjs';

const [parent, output] = process.argv.slice(2);
if (!parent || !output || !path.isAbsolute(parent) || !path.isAbsolute(output))
  throw Error('Usage: prepare-supplement.mjs COMPLETED_PRIVATE_CAMPAIGN NEW_PRIVATE_ROOT');
const bytes = fs.readFileSync(path.join(parent, 'plan.json'));
if (hash(bytes) !== fs.readFileSync(path.join(parent, 'plan.sha256'), 'utf8')) throw Error('Parent plan mismatch');
if (fs.existsSync(path.join(parent, 'execution.lock'))) throw Error('Parent still running');
const prior = JSON.parse(bytes), index = JSON.parse(fs.readFileSync(path.join(parent, 'index.json')));
if (index.remaining || index.rows.some(r => r.classification === 'infrastructure-or-unassessed'))
  throw Error('Parent infrastructure/incomplete execution requires adjudication');
verifyInputs(process.cwd(), prior.adapters);
const plan = {schema: 1, createdAt: new Date().toISOString(), parentPlanHash: hash(bytes),
  environment: prior.environment, ...inventory(process.cwd(),
    ['research/evaluation/failure-driven/uikit-closure-v1/gap-contracts']), adapters: prior.adapters};
fs.mkdirSync(output, {mode: 0o700});
for (const f of [...plan.inputs, ...plan.adapters]) {
  const to = path.join(output, 'snapshot', f.path);
  fs.mkdirSync(path.dirname(to), {recursive: true});
  fs.writeFileSync(to, fs.readFileSync(f.path), {flag: 'wx', mode: 0o600});
}
const serialized = JSON.stringify(plan, null, 2) + '\n';
fs.writeFileSync(path.join(output, 'plan.json'), serialized, {flag: 'wx', mode: 0o600});
fs.writeFileSync(path.join(output, 'plan.sha256'), hash(serialized), {flag: 'wx', mode: 0o600});
console.log('Supplement frozen; campaign run will recheck the actual environment before execution.');

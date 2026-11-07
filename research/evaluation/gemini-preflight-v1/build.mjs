// Freeze reviewed controller interpretation and export sealed subjects. Never execute a provider.
import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {hash} from '../../../code-examples/tools/contracts.mjs';
import {projectOutputPath} from '../../../evals/runner/workspace-paths.mjs';
const root = fileURLToPath(new URL('../../../', import.meta.url));
const base = 'research/evaluation/gemini-preflight-v1/';
const readBytes = p => fs.readFileSync(path.join(root, p));
const read = p => JSON.parse(readBytes(p));
const paths = {
  sealed: 'research/evaluation/milestone-package-v2/manifest.json',
  rubric: 'research/evaluation/rubric-closure-v1/rubrics.json',
  composite: 'research/evaluation/v2-controller-resolution-20261107/composite-controller.json',
  overlay: 'research/evaluation/v2-controller-resolution-20261107/controller-overlay.draft.json'
};
export function build() {
  const sealed = read(paths.sealed), rubric = read(paths.rubric), composite = read(paths.composite), overlay = read(paths.overlay);
  for (const pin of composite.components) if (hash(readBytes(pin.path)) !== pin.sha256) throw Error('Controller component drift: ' + pin.path);
  const exceptions = new Set(composite.provenance_correction.criteria);
  const applied = [], corrections = [], bindings = [], jobs = [];
  const rows = sealed.cases.map(c => {
    const original = rubric.rows.find(r => r.id === c.rubricCaseId);
    if (!original) throw Error('Missing original rubric');
    const row = structuredClone(original);
    row.criteria = row.criteria.map(criterion => {
      const override = overlay.action_criterion_overrides.find(o => o.criterion_id === criterion.id);
      if (override) {
        criterion.historicalInterpretation = {pass: criterion.pass, fail: criterion.fail, missing: criterion.missing};
        criterion.pass = override.clarified_pass; criterion.fail = override.clarified_fail; criterion.missing = override.missing;
        criterion.acceptedDesigns = override.calibration;
        applied.push(criterion.id);
      }
      const binding = overlay.source_bindings.find(b => b.criterion_id === criterion.id);
      if (binding) {
        criterion.sourceBinding = structuredClone(binding);
        bindings.push(criterion.id);
        if (exceptions.has(criterion.id)) {
          const note = criterion.sourceBinding.application_acceptance_sources.find(s => s.path.endsWith('/references/tasks/testing.md'));
          if (!note) throw Error('Missing provenance exception target');
          note.scope = 'Controller-side project testing policy, not supplied to this subject and not a subject read.';
          note.subjectCitationRequired = false;
          criterion.sourceBinding.provenanceCorrection = 'OR-01';
          corrections.push(criterion.id);
        }
      }
      criterion.appliesEquallyTo = ['generic-C0', 'candidate-controlled'];
      return criterion;
    });
    row.independentAcceptance = false;
    row.status = 'reviewed-interpretation-source-qualification-and-executed-calibration-pending';
    const arms = [...c.plans].sort((a, b) => hash(c.id + a.arm + 'gemini-v2-r1').localeCompare(hash(c.id + b.arm + 'gemini-v2-r1')));
    for (const plan of arms) {
      const relative = 'research/evaluation/milestone-package-v2/' + plan.path;
      const raw = readBytes(relative);
      if (hash(raw) !== plan.sha256) throw Error('Sealed payload drift');
      const payload = JSON.parse(raw);
      if (Object.keys(payload).join() !== 'messages' || payload.messages.length !== 2 ||
          payload.messages[0].role !== 'system' || payload.messages[1].role !== 'user' ||
          payload.messages.some(m => Object.keys(m).sort().join() !== 'content,role' || typeof m.content !== 'string')) throw Error('Unexpected subject envelope');
      jobs.push({cell: c.id + '/' + plan.arm, caseId: c.id, family: c.family, platform: c.platform,
        framework: c.framework, arm: plan.arm, condition: plan.condition,
        payloadPath: relative, payloadSha256: plan.sha256, messagesSha256: hash(JSON.stringify(payload.messages)),
        messageContentSha256: payload.messages.map(m => hash(m.content)),
        opaqueId: hash(c.id + '/' + plan.arm + '/gemini-v2-r1').slice(0, 24),
        messages: payload.messages});
    }
    return row;
  });
  if (rows.length !== 24 || jobs.length !== 48 || applied.length !== 3 || bindings.length !== 24 || corrections.length !== 5) throw Error('Unexpected reviewed matrix');
  const controller = {schema: 1, id: 'sealed-v2-reviewed-controller-gemini-r1', visibility: 'controller-only',
    inheritedComposite: {path: paths.composite, sha256: hash(readBytes(paths.composite))},
    rows, appliedActionOverrides: applied, reboundCriteria: bindings, correctedProvenance: corrections,
    executedCalibration: false, independentSourceQualificationComplete: false,
    releaseEligible: false, liveExecutionAuthorized: false};
  const pins = [...new Set([...Object.values(paths), ...composite.components.map(p => p.path), ...jobs.map(j => j.payloadPath)])]
    .map(p => ({path: p, sha256: hash(readBytes(p))}));
  const identity = {schema: 1, id: 'gemini-sealed-v2-reviewed-controller-r1', pins,
    controllerSha256: hash(JSON.stringify(controller, null, 2) + '\n'),
    cells: 48, pairedScenarios: 24, relatedFamilies: new Set(jobs.map(j => j.family)).size,
    subjectPayloadChanges: 0, candidateUnderTest: '0.3.0-dev.5 instructions with policy-and-target-sdk-v2 references',
    dev6Included: false, modelCallsAuthorized: 0, liveRunsAuthorized: false};
  return {controller, identity, jobs};
}

export function exportSubjects(output) {
  const out = projectOutputPath(output);
  if (fs.existsSync(out)) throw Error('New project-local output required');
  const built = build();
  fs.mkdirSync(path.join(out, 'subjects'), {recursive: true, mode: 0o700});
  fs.mkdirSync(path.join(out, 'operator'), {mode: 0o700});
  for (const j of built.jobs) fs.writeFileSync(path.join(out, 'subjects', j.opaqueId + '.json'), readBytes(j.payloadPath), {flag: 'wx', mode: 0o600});
  fs.writeFileSync(path.join(out, 'operator', 'controller.json'), JSON.stringify(built.controller, null, 2) + '\n', {flag: 'wx', mode: 0o600});
  fs.writeFileSync(path.join(out, 'operator', 'identity.json'), JSON.stringify(built.identity, null, 2) + '\n', {flag: 'wx', mode: 0o600});
  fs.writeFileSync(path.join(out, 'operator', 'jobs.json'), JSON.stringify(built.jobs.map(({messages, ...j}) => j), null, 2) + '\n', {flag: 'wx', mode: 0o600});
  return {output: path.relative(root, out), subjectFiles: 48, providerCalls: 0,
    isolationWarning: 'Folder layout is not runtime isolation; no transport or inference was invoked.'};
}
if (process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url)) {
  const [mode, output, ...extra] = process.argv.slice(2);
  if (extra.length) throw Error('Unexpected argument');
  if (mode === 'build' && !output) {
    const b = build();
    for (const [name, value] of [['controller.json', b.controller], ['comparison-identity.json', b.identity]]) {
      fs.writeFileSync(path.join(root, base, name), JSON.stringify(value, null, 2) + '\n', {flag: 'wx'});
    }
    console.log(JSON.stringify({cells: 48, payloadChanges: 0, controllerCriteria: b.controller.rows.reduce((n, r) => n + r.criteria.length, 0), modelCalls: 0}));
  } else if (mode === 'check' && !output) {
    const b = build();
    for (const [name, value] of [['controller.json', b.controller], ['comparison-identity.json', b.identity]])
      if (hash(readBytes(base + name)) !== hash(JSON.stringify(value, null, 2) + '\n')) throw Error('Frozen derived artifact drift: ' + name);
    console.log('Reviewed controller and all sealed payloads verified; live execution remains disabled.');
  } else if (mode === 'export' && output) console.log(JSON.stringify(exportSubjects(output), null, 2));
  else throw Error('Usage: build.mjs build|check|export NEW_PROJECT_OUTPUT (offline only)');
}

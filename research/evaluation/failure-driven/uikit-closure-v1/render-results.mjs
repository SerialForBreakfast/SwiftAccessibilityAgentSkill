import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
const here=path.dirname(fileURLToPath(import.meta.url));
const r=JSON.parse(fs.readFileSync(path.join(here,'execution.json')));
const ledger=JSON.parse(fs.readFileSync(path.join(here,'clause-ledger.json')));
const c=r.counts, environment=r.campaigns[0].environment;
const preservation=JSON.parse(fs.readFileSync(path.join(here,'preservation.json')));
const lines=['# Campaign Results','',
  `Status: ${c.unexpectedOutcomes ? 'executed-with-unresolved-outcomes' : 'executed-with-expected-outcomes'}; independent review pending. Not baseline promotion.`,'',
  '| Measure | Result |','| --- | ---: |',
  `| Packages | ${c.packages} |`, `| Native checks | ${c.checks} |`,
  `| Positive unit checks | ${c.positiveUnitChecks} |`,
  `| Unique selected positive unit methods | ${c.uniquePositiveMethods} |`,
  `| Negative controls, including compile negatives | ${c.negativeChecks} |`,
  `| Compile checks, including compile negatives | ${c.compileChecks} |`,
  `| All method executions, including negative reruns | ${c.repeatedMethodExecutionsIncludingNegatives} |`,
  `| Unexpected outcomes | ${c.unexpectedOutcomes} |`,'',
  'New development: three behavioral families, 17 positive methods and five deliberate mutants. Existing pilot and checkout methods are reruns, not newly discovered independent behaviors. Compile and negative categories overlap.','',
  `Anchor: SDK ${environment.sdkVersion} (${environment.sdkBuild}); runtime ${environment.runtimeVersion} (${environment.runtimeBuild}); ${environment.architecture}. Deployment target 26.0. Exact compiler/Xcode identifiers are retained in execution.json.`, '',
  '## Coverage','',
  ...Object.entries(ledger.counts).map(([status,count])=>`- ${status}: ${count} clauses.`),'',
  'All 15 guideline rules have partial dispositions with bounded assertions. This is accounting closure, not a claim that all accessibility behavior is unit-tested.','',
  '## First Attempts and Repairs','',
  'The original checkout oracle failure and correction remain in the checkout package. The new quantity pre-execution coverage defect and declaration-scanner scope defect retain first sources, findings and repair records. Neither authoring incident is a controlled model failure. Native first outcomes are in the table below; any later repair must use a separate revision/export.','',
  '## Per-Check Outcomes','',
  '| Package | Check | Lane | Outcome |','| --- | --- | --- | --- |',
  ...r.rows.map(row=>`| ${path.basename(row.package)} | ${row.check} | ${row.lane} | ${row.classification} |`),'',
  '## Preservation','',
  `${preservation.offline.passed} offline checks passed. All ${preservation.frozen.filesVerified} frozen files and ${preservation.historical.pinnedFiles} historical pins verified unchanged. Durable private archives preserve raw receipts, first failures, source snapshots and xcresults; hashes and recovery location are in preservation.json. Git publication was not performed.`,'',
  '## Remaining Review','',
  'Independent clause/oracle/rubric acceptance is pending. The availability matrix preserves unresolved introduction dates and overlay/type interpretation limits. No new development cases are baseline-eligible yet. No models, UI tests or mandatory manual checks were run; no skill or frozen-baseline updates were made.',''];
fs.writeFileSync(path.join(here,'RESULTS.md'),lines.join('\n'));

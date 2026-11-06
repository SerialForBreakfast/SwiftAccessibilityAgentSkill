import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
const here = path.dirname(fileURLToPath(import.meta.url));
const l = JSON.parse(fs.readFileSync(path.join(here, 'clause-ledger.json')));
const statuses = ['covered','partially-covered','missing-testable-coverage','documentation-supported/outside-unit-scope','swiftui-deferred'];
const escape = s => s.replaceAll('|','\\|').replaceAll('\n',' ');
let out = '# UIKit Coverage Ledger\n\nGenerated from `clause-ledger.json`; author review, independent acceptance pending.\n'
  + 'Coverage describes the bounded example assertions, not universal accessibility.\n\n'
  + '| Guideline | Covered | Partial | Testable gap | Outside unit scope | SwiftUI deferred |\n| --- | ---: | ---: | ---: | ---: | ---: |\n';
for (const rule of l.rules) {
  const id = rule.id.replace('-RULE',''), rows = l.clauses.filter(c => c.id.startsWith(id+'-'));
  out += `| [${id}](../../../../${rule.guidelinePath}) | ${statuses.map(s => rows.filter(c=>c.status===s).length).join(' | ')} |\n`;
}
out += '\n## Identified Implementation Gaps\n\n| Clause | Family | Disposition |\n| --- | --- | --- |\n';
for (const c of l.clauses.filter(c=>c.gapId)) out += `| ${c.id} | ${c.gapId} | ${c.gapDisposition} |\n`;
out += '\n## Clause Review\n\nBindings resolve to exact method IDs, body hashes, source claims and matching execution receipts in the JSON ledger and assertion catalog.\n';
for (const rule of l.rules) {
  const id = rule.id.replace('-RULE','');
  out += `\n### ${id}\n\nRule: ${rule.text}\n\nDisposition: ${rule.status}. ${rule.rationale}\n\n`;
  out += '| Clause | Requirement | Disposition | Assertion bindings |\n| --- | --- | --- | --- |\n';
  for (const c of l.clauses.filter(c=>c.id.startsWith(id+'-')))
    out += `| [${c.id}](../../../../${c.guidelinePath}#L${c.line}) | ${escape(c.text)} | ${c.status} | ${c.bindingIds.join(', ') || 'Documentation scope'} |\n`;
}
fs.writeFileSync(path.join(here, 'COVERAGE.md'), out);

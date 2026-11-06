import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import {hash} from './contracts.mjs';

const root = new URL('../../', import.meta.url);
test('requirements inventory preserves every selected clause in all fifteen guidelines', () => {
  const inventory = JSON.parse(fs.readFileSync(new URL('code-examples/audits/requirements-v1/inventory.json', root)));
  const names = fs.readdirSync(new URL('references/uikit/guidelines/', root)).filter(n => /^u-\d{3}-/.test(n)).sort();
  assert.equal(names.length, 15);
  assert.deepEqual(inventory.documents.map(d => d.path), names.map(n => 'references/uikit/guidelines/' + n));
  for (const d of inventory.documents) {
    const bytes = fs.readFileSync(new URL(d.path, root));
    assert.equal(hash(bytes), d.sha256);
    const lines = bytes.toString().split('\n');
    assert.equal(d.rule, lines.slice(lines.indexOf('## Rule') + 1, lines.indexOf('## Rationale')).join('\n').trim());
    let section = '', subsection = '';
    const clauses = [];
    lines.forEach((text, i) => {
      if (text.startsWith('## ')) { section = text.slice(3); subsection = ''; }
      if (text.startsWith('### ')) subsection = text.slice(4);
      if (text.startsWith('- ') && ['How To Implement', 'How To Test', "Do / Don't"].includes(section))
        clauses.push({id: d.guideline + '-L' + (i + 1), line: i + 1, section, subsection, text: text.slice(2), status: 'pending-clause-review'});
    });
    assert.deepEqual(d.clauses, clauses);
  }
});

test('partial media declaration matrix retains located declaration context', () => {
  const matrix = JSON.parse(fs.readFileSync(new URL('code-examples/audits/availability-v1/media-declarations.json', root)));
  assert.equal(matrix.status, 'partial-member-review');
  assert.equal(new Set(matrix.rows.map(r => r.id)).size, matrix.rows.length);
  for (const r of matrix.rows) {
    assert.match(r.headerHash, /^[0-9a-f]{64}$/);
    assert.equal(r.context.at(-1), r.declaration);
    assert.equal(r.contextStart + r.context.length - 1, r.line);
  }
  assert.ok(matrix.rows.find(r => r.id === 'legacy-locale').context.some(l => l.includes('@available(iOS, deprecated: 16')));
  assert.ok(matrix.rows.find(r => r.id === 'locale-language').context.some(l => l.includes('iOS 16')));
});

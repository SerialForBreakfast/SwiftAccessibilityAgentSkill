import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {spawnSync} from 'node:child_process';
import {hash} from '../../../../code-examples/tools/contracts.mjs';
import {enclosingObjCScope} from '../../../../code-examples/tools/declaration-scope.mjs';

const here = path.dirname(fileURLToPath(import.meta.url));
const sdkProbe = spawnSync('xcrun', ['--sdk','iphonesimulator','--show-sdk-path'], {encoding:'utf8'});
if (sdkProbe.status !== 0) throw Error('SDK unavailable');
const sdk = sdkProbe.stdout.trim();
const files = ['api-declarations.json', 'api-gap-declarations-r2.json'];
const entries = new Map();
for (const file of files) {
  const doc = JSON.parse(fs.readFileSync(path.join(here, file)));
  for (const row of doc.rows) {
    const entry = entries.get(row.symbol) ?? {...row, packages: [], inputRecords: []};
    entry.packages = [...new Set([...entry.packages, ...row.packages])];
    entry.inputRecords.push(file);
    entries.set(row.symbol, entry);
  }
}
const rows = [...entries.values()].map(row => {
  // Deliberately exclude preceding context: its annotations may name another API.
  const d = row.declaration;
  let enclosingDeclaration = null;
  if (d) {
    const bytes = fs.readFileSync(path.join(sdk,d.path));
    if (hash(bytes) !== d.sha256) throw Error('Header changed: ' + d.path);
    const source = bytes.toString().split('\n');
    enclosingDeclaration = enclosingObjCScope(source, d.line);
  }
  const lines = d ? d.context.slice(d.line - d.contextStart) : [];
  const own = lines.join('\n');
  const available = own.match(/API_AVAILABLE\((.*)\)/)?.[1];
  const deprecated = own.match(/API_DEPRECATED(?:_WITH_REPLACEMENT)?\((.*)\)/)?.[1];
  const introduction = available?.match(/\bios\(([\d.]+)\)/)?.[1] ?? null;
  const deprecation = deprecated?.match(/\bios\(([\d.]+),\s*([\d.]+)\)/);
  return {...row, enclosingDeclaration, enclosingScopeStatus:d?'header-scope-scanned-through-declaration':'unresolved-declaration-location', directDeclaration: own || null,
    introduction: introduction ?? deprecation?.[1] ?? null,
    deprecatedOnIOS: deprecation?.[2] ?? null,
    availabilityStatus: introduction || deprecation ? 'direct-iOS-annotation-extracted' : 'unresolved-explicitly',
    deprecationStatus: deprecation ? 'direct-iOS-deprecation-extracted' : 'no-direct-deprecation-extracted-not-a-guarantee',
    availabilityInterpretation: 'Enclosing declaration context remains separately recorded; overlays and inherited defaults are not inferred from nearby annotations.',
    sdkCompilation: 'SDK27.0 target26.0; see inputRecords for exact source/AST hashes',
    runtimeEvidence: 'Consult matching package receipts; compilation is not runtime evidence.',
    independentReview: 'pending'};
});
const result = {schema: 1, status: 'bounded-member-matrix-with-explicit-unresolved-items',
  scope: 'All compiler-resolved external member/override references in 19 production packages. Type-only/conformance inventory remains an explicit audit limitation, not silently counted as resolved.',
  inputs: files.map(file => ({file, sha256: hash(fs.readFileSync(path.join(here, file)))})), rows};
fs.writeFileSync(path.join(here, 'availability-matrix.json'), JSON.stringify(result, null, 2) + '\n');
console.log(JSON.stringify({members: rows.length, directIOSAnnotations: rows.filter(r => r.introduction).length,
  unresolved: rows.filter(r => !r.introduction).length}));

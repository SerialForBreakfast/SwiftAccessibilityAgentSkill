import fs from 'node:fs';
import path from 'node:path';
import {hash, validateManifest, validateResult, appendResult} from './contracts.mjs';

const [mode, manifestFile, recordFile, ledger, ...extra] = process.argv.slice(2);
if (!['plan', 'record'].includes(mode) || !manifestFile || extra.length ||
    (mode === 'plan' && (recordFile || ledger)) || (mode === 'record' && (!recordFile || !ledger))) {
  throw Error('Usage: node code-examples/tools/cli.mjs plan MANIFEST | record MANIFEST RESULT PRIVATE_LEDGER');
}
const bytes = fs.readFileSync(manifestFile);
const manifest = validateManifest(JSON.parse(bytes), path.dirname(path.resolve(manifestFile)));
if (mode === 'plan') {
  console.log(JSON.stringify({execution: false, manifestHash: hash(bytes), manifest}, null, 2));
} else {
  const record = validateResult(manifest, hash(bytes), JSON.parse(fs.readFileSync(recordFile)), path.dirname(path.resolve(recordFile)));
  console.log(JSON.stringify({execution: false, file: appendResult(ledger, record, path.dirname(path.resolve(recordFile))), status: record.status}));
}

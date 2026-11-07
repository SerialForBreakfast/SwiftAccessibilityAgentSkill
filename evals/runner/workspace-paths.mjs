import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';

export const projectRoot = fs.realpathSync(path.resolve(path.dirname(fileURLToPath(import.meta.url)), '../..'));

function inside(root, candidate) {
  const relative = path.relative(root, candidate);
  return relative !== '' && relative !== '..' && !relative.startsWith('..' + path.sep) && !path.isAbsolute(relative);
}

export function projectOutputPath(value, root = projectRoot) {
  if (typeof value !== 'string' || !value.trim()) throw Error('Project-local output path required');
  root = fs.realpathSync(root);
  const output = path.resolve(root, value);
  if (!inside(root, output)) throw Error('Output must stay inside the project directory');
  let current = root;
  for (const part of path.relative(root, output).split(path.sep)) {
    current = path.join(current, part);
    try { fs.lstatSync(current); }
    catch (e) { if (e.code === 'ENOENT') break; throw e; }
    const resolved = fs.realpathSync(current);
    if (!inside(root, resolved)) throw Error('Output symlink escapes the project directory');
  }
  return output;
}

export function runEnvironment(output) {
  output = projectOutputPath(output);
  const scratch = projectOutputPath(path.join(output, 'scratch'));
  const clang = projectOutputPath(path.join(output, 'cache', 'clang'));
  const swift = projectOutputPath(path.join(output, 'cache', 'swift'));
  for (const p of [scratch, clang, swift]) fs.mkdirSync(p, {recursive: true, mode: 0o700});
  return {...process.env, TMPDIR: scratch + path.sep, TMP: scratch, TEMP: scratch,
    CLANG_MODULE_CACHE_PATH: clang, SWIFT_MODULECACHE_PATH: swift};
}

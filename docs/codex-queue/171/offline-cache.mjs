// Keep CLI cache writes inside this ticket's evidence folder.
import fs from 'node:fs';
import path from 'node:path';
import { syncBuiltinESMExports } from 'node:module';
import { fileURLToPath } from 'node:url';
import { HashCache } from '../../../scripts/media/lib/hash.mjs';

const folder = path.dirname(fileURLToPath(import.meta.url));
const root = path.resolve(folder, '../../..');
const dryList = path.join(root, '.cache/media-push-dry-run.txt');
const redirect = (file) => typeof file === 'string' && (file === dryList || file.startsWith(`${dryList}.`))
  ? path.join(folder, path.basename(file)) : file;
const write = fs.writeFileSync;
const rename = fs.renameSync;
const mkdir = fs.mkdirSync;
fs.writeFileSync = (file, ...args) => write(redirect(file), ...args);
fs.renameSync = (from, to) => rename(redirect(from), redirect(to));
fs.mkdirSync = (file, ...args) => path.resolve(file) === path.join(root, '.cache') ? undefined : mkdir(file, ...args);
HashCache.prototype.save = function () { this.dirty = false; };
syncBuiltinESMExports();

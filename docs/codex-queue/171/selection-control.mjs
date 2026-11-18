// Compare old and new selectors on the same live disk, without Git writes.
import './offline-cache.mjs';
import assert from 'node:assert/strict';
import { execFileSync } from 'node:child_process';
import { writeFileSync } from 'node:fs';
import path from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';
import { createContext } from '../../../scripts/media/media.mjs';
import { hashEntries } from '../../../scripts/media/lib/hash.mjs';
import { scanSets, presentGames, withGame } from '../../../scripts/media/lib/sets.mjs';
const folder = path.dirname(fileURLToPath(import.meta.url));
const root = path.resolve(folder, '../../..');
const oldSource = execFileSync('git', ['show', 'HEAD:scripts/media/lib/sets.mjs'], { cwd: root, encoding: 'utf8' })
  .replace(/from '\.\/([^']+)'/g, (_, file) => `from '${pathToFileURL(path.join(root, 'scripts/media/lib', file)).href}'`);
const { scanSets: oldScan } = await import(`data:text/javascript;base64,${Buffer.from(oldSource).toString('base64')}`);
const ctx = createContext({ root, out: { write() {} } });
const result = {};
for (const game of [...presentGames(ctx), null]) {
  const gctx = withGame(ctx, game);
  const names = game ? ['originals', 'runtime'] : ['private'];
  const before = await oldScan(gctx, names);
  const after = await scanSets(gctx, names);
  const sets = {};
  for (const name of names) {
    await hashEntries([...before.sets[name], ...after.sets[name]], ctx.cache);
    const entries = (scan) => scan.sets[name].map(({ key, size, md5 }) => ({ key, size, md5 }));
    const old = entries(before);
    const current = entries(after);
    const known = new Set(old.map((entry) => entry.key));
    const added = current.filter((entry) => !known.has(entry.key));
    assert.deepEqual(current.filter((entry) => known.has(entry.key)), old, `${game?.id}/${name}: existing files changed`);
    if (name === 'runtime') for (const entry of added) assert.match(entry.key, /\.json$/i);
    else assert.deepEqual(added, [], `${game?.id}/${name}: selector changed`);
    sets[name] = { before: old.length, after: current.length, added };
  }
  result[game?.id ?? 'shared'] = sets;
}
writeFileSync(path.join(folder, 'selection-control.json'), JSON.stringify(result, null, 2) + '\n');
const json = Object.entries(result).flatMap(([id, sets]) => sets.runtime?.added.map((entry) => ({ game: id, ...entry })) ?? []);
assert.equal(json.length, 5);
writeFileSync(path.join(folder, 'new-json.tsv'), 'game\tstatus\tbytes\tmd5\tpath\n' + json.map(({ game, key, size, md5 }) => `${game}\tMới\t${size}\t${md5}\t${key}\n`).join(''));
process.stdout.write('Selectors agree on all originals/private and existing runtime files; exactly 5 runtime JSON added.\n');

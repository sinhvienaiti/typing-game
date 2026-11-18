// Capture local plans without changing media, locks or the hash cache.
import './offline-cache.mjs';
import { createHash } from 'node:crypto';
import { writeFileSync } from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { createContext } from '../../../scripts/media/media.mjs';
import { presentGames, withGame } from '../../../scripts/media/lib/sets.mjs';
import { loadState } from '../../../scripts/media/lib/state.mjs';

const folder = path.dirname(fileURLToPath(import.meta.url));
const root = path.resolve(folder, '../../..');
const ctx = createContext({ root, out: { write() {} } });
const snapshot = {};
for (const game of presentGames(ctx)) {
  const state = await loadState(withGame(ctx, game), ['originals', 'runtime']);
  snapshot[game.id] = Object.fromEntries(Object.entries(state.perSet).map(([name, value]) => [name, {
    plan: value.plan,
    local: [...value.local].map(([key, entry]) => ({ key, md5: entry.md5, size: entry.size })),
  }]));
}
const state = await loadState(withGame(ctx, null), ['private']);
snapshot.shared = { private: {
  plan: state.perSet.private.plan,
  local: [...state.perSet.private.local].map(([key, entry]) => ({ key, md5: entry.md5, size: entry.size })),
} };
const digest = (value) => createHash('sha256').update(JSON.stringify(value)).digest('hex');
for (const sets of Object.values(snapshot)) for (const [name, set] of Object.entries(sets)) {
  sets[name] = {
    count: set.local.length,
    bytes: set.local.reduce((sum, entry) => sum + entry.size, 0),
    localSha256: digest(set.local),
    planSha256: digest(set.plan),
    planCounts: Object.fromEntries(Object.entries(set.plan).map(([key, value]) => [key, value.length])),
    ...(name === 'runtime' ? { plan: set.plan, local: set.local } : {}),
  };
}
writeFileSync(path.join(folder, `snapshot-${process.argv[2]}.json`), `${JSON.stringify(snapshot, null, 2)}\n`);

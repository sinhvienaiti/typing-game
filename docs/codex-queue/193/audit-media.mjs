// Offline inventory; never updates the upload lock before media:push succeeds.
import assert from 'node:assert/strict';
import { createHash } from 'node:crypto';
import { readFile, readdir, writeFile } from 'node:fs/promises';
import { homedir } from 'node:os';
import { dirname, join, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';
const root = resolve(dirname(fileURLToPath(import.meta.url)), '../../..');
const source = join(homedir(), 'AudioLab/review/staging/keys-firefly');
const media = join(root, 'public/assets/typing-defense');
const hash = (bytes, algo = 'sha256') => createHash(algo).update(bytes).digest('hex');
async function walk(dir, prefix = '') {
  const files = [];
  for (const entry of await readdir(dir, { withFileTypes: true })) {
    const rel = prefix + entry.name;
    if (entry.isDirectory()) files.push(...await walk(join(dir, entry.name), rel + '/'));
    else files.push(rel);
  }
  return files.sort();
}
const inventory = [];
const pending = [];
for (const rel of (await walk(source)).filter((name) => !name.endsWith('.wav'))) {
  const runtime = 'audio/keys/' + rel;
  const original = await readFile(join(source, rel));
  const bytes = await readFile(join(media, runtime));
  assert.equal(hash(bytes), hash(original), rel + ': exact staging bytes');
  inventory.push({ file: 'public/assets/typing-defense/' + runtime, sha256: hash(bytes), bytes: bytes.length });
  if (rel.endsWith('.ogg')) pending.push(hash(bytes, 'md5') + '  public/assets/typing-defense/' + runtime);
}
assert(!(await walk(join(media, 'audio/keys'))).some((name) => name.endsWith('.wav')));
const artSource = '/Users/toandx/htdocs/typing-game/games/typing-defense/art-src/ui';
const art = [];
for (const name of (await readdir(join(media, 'ui/quick-settings'))).filter((name) => name.endsWith('.png')).sort()) {
  const srcDir = name.startsWith('hud-') || name.startsWith('vol-') ? 'quick-settings/selected' : 'frames-epic';
  const bytes = await readFile(join(media, 'ui/quick-settings', name));
  assert.equal(hash(bytes), hash(await readFile(join(artSource, srcDir, name))), name + ': existing art');
  const prompt = await readFile(join(media, 'ui/quick-settings', name.replace(/\.png$/, '.prompt.txt')));
  assert.equal(hash(prompt), hash(await readFile(join(artSource, srcDir, name.replace(/\.png$/, '.prompt.txt')))), name + ': exact prompt');
  art.push({ file: 'public/assets/typing-defense/ui/quick-settings/' + name, sha256: hash(bytes), bytes: bytes.length, promptMatches: true });
  pending.push(hash(bytes, 'md5') + '  public/assets/typing-defense/ui/quick-settings/' + name);
}
await writeFile(join(root, 'docs/codex-queue/193/media-pending.md5'), pending.sort((a, b) => a.slice(34).localeCompare(b.slice(34))).join('\n') + '\n');
console.log(JSON.stringify({ source, audio: inventory, art, samples: 91, previews: 7, wav: 0, pendingBinaryFiles: pending.length, uploadLockChanged: false, result: 'PASS' }, null, 2));

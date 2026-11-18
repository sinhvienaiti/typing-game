// Compare every set's file hashes and classification, not just displayed totals.
import assert from 'node:assert/strict';
import { readFileSync, writeFileSync } from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
const folder = path.dirname(fileURLToPath(import.meta.url));
const before = JSON.parse(readFileSync(path.join(folder, 'snapshot-before.json'), 'utf8'));
const after = JSON.parse(readFileSync(path.join(folder, 'snapshot-after.json'), 'utf8'));
const comparison = { unchanged: [], addedJson: {}, changedOtherFiles: [] };
for (const [id, sets] of Object.entries(after)) for (const [name, set] of Object.entries(sets)) {
  const old = before[id][name];
  if (name !== 'runtime') {
    assert.deepEqual(set, old, `${id}/${name} changed`);
    comparison.unchanged.push(`${id}/${name}`);
    continue;
  }
  const known = new Map(old.local.map((entry) => [entry.key, entry]));
  const added = set.local.filter((entry) => !known.has(entry.key));
  for (const entry of added) {
    assert.match(entry.key, /\.json$/i);
    assert.ok(set.plan.added.includes(entry.key), `${id}/${entry.key} is new`);
  }
  assert.deepEqual(set.local.filter((entry) => known.has(entry.key)), old.local, `${id}: non-JSON runtime changed`);
  assert.deepEqual({ ...set.plan, added: set.plan.added.filter((key) => known.has(key)) }, old.plan, `${id}: existing runtime plan changed`);
  comparison.addedJson[id] = added;
}
assert.equal(comparison.addedJson['dragon-hold'].length, 5);
writeFileSync(path.join(folder, 'comparison.json'), JSON.stringify(comparison, null, 2) + '\n');
const lines = Object.entries(comparison.addedJson).flatMap(([game, entries]) => entries.map((entry) => `${game}\tMới\t${entry.size}\t${entry.md5}\t${entry.key}`));
writeFileSync(path.join(folder, 'new-json.tsv'), `game\tstatus\tbytes\tmd5\tpath\n${lines.join('\n')}\n`);
process.stdout.write(`Unchanged: ${comparison.unchanged.length} originals/private sets; existing runtime unchanged. Added: ${lines.length} JSON.\n`);

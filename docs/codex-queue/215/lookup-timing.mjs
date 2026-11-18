import assert from 'node:assert/strict';
import { writeFile } from 'node:fs/promises';
import { performance } from 'node:perf_hooks';
import { applyLearningEvents } from '../../../shared/learning/core.mjs';
import { lookupLearningRecords } from '../../../shared/learning/query.mjs';

const now = '2026-10-30T06:00:00.000Z';
const ids = Array.from({ length: 5000 }, (_, i) => 'word-' + i);
const profile = applyLearningEvents(null, ids.map((entityId) => ({
  version: 1, entityType: 'vocabulary', entityId, gameId: 'recall-typing',
  activityType: 'meaning-recall', result: 'correct', occurredAt: now,
})));
const lookup = { entityType: 'vocabulary', entityIds: ids.filter((_, i) => i % 25 === 0) };
for (let i = 0; i < 5; i++) lookupLearningRecords(profile, lookup, now);
const durations = [];
for (let i = 0; i < 20; i++) {
  const started = performance.now();
  const result = lookupLearningRecords(profile, lookup, now);
  durations.push(performance.now() - started);
  assert.equal(result.items.length, 200);
}
const sorted = [...durations].sort((a, b) => a - b);
const result = {
  node: process.version, platform: process.platform, arch: process.arch,
  profileRecords: 5000, lookupIds: 200, warmups: 5, runs: 20,
  medianMs: (sorted[9] + sorted[10]) / 2, targetMs: 20,
  durationsMs: durations,
};
await writeFile(new URL('./lookup-timing.json', import.meta.url), JSON.stringify(result, null, 2) + '\n');
process.stdout.write(JSON.stringify(result) + '\n');

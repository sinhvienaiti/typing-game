// Runtime JSON coverage, tracked-file boundaries and offline push planning.
import assert from 'node:assert/strict';
import { readFileSync, rmSync } from 'node:fs';
import path from 'node:path';
import test from 'node:test';
import { createContext } from '../media.mjs';
import { planPush } from '../commands/push.mjs';
import { findGame, loadConfig, lockKeyProblem, scanSets, withGame } from '../lib/sets.mjs';
import { loadState } from '../lib/state.mjs';
import { addDragonHold, makeFixture, md5, REPO_ROOT, runMedia, write } from './fixture.mjs';

const JSON_BODY = '{"version":1,"tiles":["grass"]}\n';

function addJson(game, id) {
  const base = `public/assets/${id}`;
  write(game, '.gitignore', `${readFileSync(path.join(game, '.gitignore'), 'utf8')}\n${base}/\n`);
  const included = ['ground/manifest.json', 'decals/manifest.json', 'models/kit3/manifest.json', 'vfx/firefly/data.JSON'];
  const excluded = ['cache/data.json', '.cache/data.json', 'models/a-cache/data.json', 'tmp/data.json',
    'nested/temp/data.json', 'ground/manifest.tmp.json', 'ground/data.cache.json', 'ground/cache.json',
    'ground/manifest.json.tmp', 'ground/.#manifest.json', 'ground/manifest~.json'];
  for (const key of [...included, ...excluded]) write(game, `${base}/${key}`, JSON_BODY);
  for (const key of ['docs/data.json', 'src/data.json', 'public/data.json', `public/assets/${id}-other/data.json`]) write(game, key, JSON_BODY);
  return included.map((key) => `${base}/${key}`).sort();
}

test('runtime JSON: ignored assets are included for each game; tracked JSON and cache/temp are excluded', async (t) => {
  const fx = makeFixture();
  t.after(() => rmSync(fx.base, { recursive: true, force: true }));
  const dragon = addDragonHold(fx);
  const ctx = createContext({ root: fx.repo, out: { write() {} } });
  for (const [id, game] of [['space-typing', fx.game], ['dragon-hold', dragon]]) {
    const gctx = withGame(ctx, id);
    const before = await scanSets(gctx, ['originals', 'runtime', 'private']);
    const expected = addJson(game, id);
    const after = await scanSets(gctx, ['originals', 'runtime', 'private']);
    assert.deepEqual(after.sets.runtime.filter((entry) => /\.json$/i.test(entry.key)).map((entry) => entry.key), expected);
    assert.deepEqual(after.sets.runtime.filter((entry) => !/\.json$/i.test(entry.key)), before.sets.runtime);
    assert.deepEqual(after.sets.originals, before.sets.originals);
    assert.deepEqual(after.sets.private, before.sets.private);
  }
});

test('runtime JSON: lock validation allows only asset JSON outside cache/temp for every configured game', () => {
  const config = loadConfig(REPO_ROOT);
  assert.ok(!config.mediaExtensions.includes('json'), 'JSON is scoped to runtime assets');
  for (const game of config.games) {
    const base = `public/assets/${game.id}`;
    for (const key of [`${base}/ground/manifest.json`, `${base}/custom/deep/data.JSON`, `${base}/models/manifest.json`]) {
      assert.equal(lockKeyProblem(config, 'game', key, game), null, key);
    }
    for (const key of ['scripts/data.json', 'docs/data.json', 'public/data.json', `public/assets/${game.id}-other/data.json`,
      `${base}/cache/data.json`, `${base}/.cache/data.json`, `${base}/models/a-cache/data.json`,
      `${base}/nested/tmp/data.json`, `${base}/ground/data.tmp.json`, `${base}/ground/cache.json`,
      `${base}/ground/.#data.json`, `${base}/ground/data~.json`]) {
      assert.notEqual(lockKeyProblem(config, 'game', key, game), null, key);
    }
  }
  assert.notEqual(lockKeyProblem(config, 'game', 'public/local-assets/data.json', findGame(config, 'space-typing')), null);
});

test('runtime JSON: status, dry-run, md5 lock plan and missing-file validation work offline', async (t) => {
  const fx = makeFixture();
  t.after(() => rmSync(fx.base, { recursive: true, force: true }));
  const game = addDragonHold(fx);
  const expected = addJson(game, 'dragon-hold');
  const ctx = withGame(createContext({ root: fx.repo, out: { write() {} } }), 'dragon-hold');
  const state = await loadState(ctx, ['runtime']);
  assert.deepEqual(state.perSet.runtime.plan.added.filter((key) => /\.json$/i.test(key)), expected);
  const planned = planPush(ctx, state, ['runtime'], {});
  for (const key of expected) {
    assert.ok(planned.sets.runtime.upload.includes(key));
    assert.equal(planned.sets.runtime.newLock.get(key), md5(JSON_BODY));
  }
  const status = runMedia(fx, 'status', '--only', 'runtime');
  assert.equal(status.code, 0, status.out);
  assert.match(status.out, /runtime +5 file, .*Mới 5/);
  const dryRun = runMedia(fx, 'push', '--dry-run', '--only', 'runtime');
  assert.equal(dryRun.code, 0, dryRun.out);
  const list = readFileSync(path.join(fx.repo, '.cache/media-push-dry-run.txt'), 'utf8');
  for (const key of expected) assert.ok(list.includes(`games/dragon-hold/${key}`), key);
  write(game, 'media.md5', expected.map((key) => `${md5(JSON_BODY)}  ${key}\n`).join(''));
  for (const key of expected) rmSync(path.join(game, key));
  const missing = await loadState(ctx, ['runtime']);
  assert.deepEqual(missing.perSet.runtime.plan.missing, expected, 'a fresh machine accepts locked JSON before it exists');
  const missingPlan = planPush(ctx, missing, ['runtime'], {});
  assert.deepEqual(missingPlan.sets.runtime.autoForgotten, [], 'missing JSON under models still needs to be pulled');
  for (const key of expected) assert.equal(missingPlan.sets.runtime.newLock.get(key), md5(JSON_BODY));
});

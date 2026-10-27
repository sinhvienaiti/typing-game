// Unit tests: no network, no rclone. Run: pnpm media:test
import assert from 'node:assert/strict';
import { spawnSync } from 'node:child_process';
import { mkdirSync, mkdtempSync, readFileSync, rmSync, statSync, utimesSync, writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import path from 'node:path';
import test from 'node:test';
import { parseArgs, UsageError } from '../lib/args.mjs';
import { matchesGlob } from '../lib/glob.mjs';
import { isDetachedHead, lockHistory } from '../lib/git.mjs';
import { HashCache, hashEntries } from '../lib/hash.mjs';
import { formatLock, isSafeRelativePath, LockError, parseLock, parseLockHistory } from '../lib/lock.mjs';
import { classify, quotaCheck, runtimeReferences } from '../lib/plan.mjs';
import { assertAllowed, parseCombined, redact } from '../lib/rclone.mjs';
import { assertLockKeys, findGame, loadConfig, lockCopyName, lockKeyProblem, lostOriginalIds, presentGames, scanSets, setDefinitions, withGame } from '../lib/sets.mjs';
import { loadState } from '../lib/state.mjs';
import { nextStamp } from '../lib/ui.mjs';
import { askQuestions, compareDriveCopies, planPush } from '../commands/push.mjs';
import { createArgs, remoteSection } from '../commands/setup.mjs';
import { createContext } from '../media.mjs';
import { addDragonHold, CONTENT, DRAGON, git, makeFixture, md5, REPO_ROOT, runMedia, write } from './fixture.mjs';

const MD5_A = 'a'.repeat(32);
const MD5_B = 'b'.repeat(32);
const MD5_C = 'c'.repeat(32);

test('args: a leading -- from pnpm is dropped, everything else fails closed', () => {
  assert.deepEqual(parseArgs(['push', '--', '--dry-run']), { command: 'push', options: { 'dry-run': true } });
  assert.deepEqual(parseArgs(['push', '--dry-run']).options, { 'dry-run': true });
  assert.deepEqual(parseArgs(['pull', '--only=runtime,private', '--to', '/tmp/x']).options, { only: ['runtime', 'private'], to: '/tmp/x' });
  assert.deepEqual(parseArgs(['push', '--forget', 'a b.png', '--forget=c']).options, { forget: ['a b.png', 'c'] });
  assert.deepEqual(parseArgs(['push', '--readd', 'x.png', '--yes']).options, { readd: ['x.png'], yes: true });
  assert.deepEqual(parseArgs(['status', '--only', 'originals', '--only', 'originals']).options, { only: ['originals'] });
  assert.equal(parseArgs([]).command, 'help');
  for (const argv of [
    ['push', '--dryrun'], ['push', '--yes', '--', '--dry-run'], ['push', 'extra'], ['push', '--only'], ['push', '--only', 'music'],
    ['pull', '--to'], ['pull', '--to', 'a', '--to', 'b'], ['push', '--yes=1'], ['check', '--dry-run'], ['setup', '--client-id', '--reconnect'],
    ['sync'], ['push', '--forget', ''], ['pull', '--readd', 'x'],
  ]) {
    assert.throws(() => parseArgs(argv), UsageError, argv.join(' '));
  }
});

test('glob: ** spans zero or more folders, braces pick alternatives', () => {
  assert.ok(matchesGlob('models/enemies/a.glb', 'models/{enemies,bosses,items,skills,ships}/**/*.glb'));
  assert.ok(matchesGlob('models/ships/x/y/a.glb', 'models/{enemies,bosses,items,skills,ships}/**/*.glb'));
  assert.ok(!matchesGlob('models/heroes/a.glb', 'models/{enemies,bosses,items,skills,ships}/**/*.glb'));
  assert.ok(!matchesGlob('models/blend/ships/a.blend', 'models/{enemies,bosses,items,skills,ships}/**/*.glb'));
  assert.ok(matchesGlob('g01/_out/x.png', '**/_out/**'));
  assert.ok(matchesGlob('_out/x.png', '**/_out/**'));
  assert.ok(matchesGlob('fx/a b (1).zip', '**/*.zip'));
  assert.ok(matchesGlob('._thing', '._*'));
  assert.ok(!matchesGlob('a/._thing', '._*'));
  assert.ok(matchesGlob('src/node_modules', '**/node_modules'));
  assert.ok(matchesGlob('.wt-feature', '**/.wt-*'));
});

test('lock: md5sum format, sorted by path, LF only, strict parsing', () => {
  const entries = new Map([['b dir/x (1).png', MD5_B], ['a.glb', MD5_A]]);
  const text = formatLock(entries);
  assert.equal(text, `${MD5_A}  a.glb\n${MD5_B}  b dir/x (1).png\n`);
  assert.deepEqual(parseLock(text), new Map([['a.glb', MD5_A], ['b dir/x (1).png', MD5_B]]));
  assert.deepEqual(parseLock(`${MD5_A}  a.glb\r\n\r\n${MD5_B} *bin.glb\r\n`), new Map([['a.glb', MD5_A], ['bin.glb', MD5_B]]));
  assert.deepEqual(parseLock(`${MD5_A}  a.glb\n${MD5_A}  a.glb\n`).size, 1);
  assert.throws(() => parseLock(`${MD5_A}  a.glb\n${MD5_B}  a.glb\n`), LockError);
  assert.throws(() => parseLock(`<<<<<<< HEAD\n${MD5_A}  a.glb\n=======\n`), /xung đột merge/);
  assert.throws(() => parseLock(`${MD5_A}  art\\x.png\n`), LockError);
  assert.throws(() => parseLock(`${MD5_A}  ../x.png\n`), LockError);
  assert.throws(() => parseLock(`${MD5_A}  /abs.png\n`), LockError);
  assert.throws(() => parseLock('nothex  a.png\n'), LockError);
  assert.throws(() => formatLock(new Map([['a\\b', MD5_A]])), LockError);
  // Names Windows cannot hold (a WSL download's Zone.Identifier stream) never reach a lock.
  assert.throws(() => parseLock(`${MD5_A}  art-src/a.png:Zone.Identifier\n`), LockError);
  for (const bad of ['a:b.png', 'a?.png', 'a*.png', 'a"b.png', 'a<b>.png', 'a|b.png', 'a\tb.png']) assert.equal(isSafeRelativePath(bad), false, bad);
  assert.equal(isSafeRelativePath('art-src/fx (1)/a b,c+d.png'), true);
  // Code-unit order, independent of the machine's locale.
  assert.equal(formatLock(new Map([['b', MD5_A], ['B', MD5_A], ['a', MD5_A]])).split('\n')[0], `${MD5_A}  B`);
});

test('lock history: every md5 a path had in git log -p', () => {
  const patch = [
    'diff --git a/media.md5 b/media.md5', '--- a/media.md5', '+++ b/media.md5', '@@ -1,2 +1,2 @@',
    `-${MD5_A}  art-src/a.png`, `+${MD5_B}  art-src/a.png`, ` ${MD5_C}  art-src/c.png`,
  ].join('\n');
  const history = parseLockHistory(patch);
  assert.deepEqual([...history.get('art-src/a.png')].sort(), [MD5_A, MD5_B]);
  assert.deepEqual([...history.get('art-src/c.png')], [MD5_C]);
});

test('classify: a path the lock once had with these bytes is removedElsewhere, never added or a rename target', () => {
  // Machine A renamed old.png -> new.png; this machine pulled Git, still has old.png, lacks new.png.
  const local = new Map([['old.png', { md5: MD5_A }], ['forgotten.png', { md5: MD5_B }], ['readded-new.png', { md5: MD5_C }]]);
  const lock = new Map([['new.png', MD5_A]]);
  const history = new Map([['old.png', new Set([MD5_A])], ['new.png', new Set([MD5_A])], ['forgotten.png', new Set([MD5_B])],
    ['readded-new.png', new Set([MD5_A])]]);
  const result = classify({ local, lock, history });
  assert.deepEqual(result.removedElsewhere, ['forgotten.png', 'old.png']);
  assert.deepEqual(result.renames, [], 'old.png is not offered as new.png renamed back');
  assert.deepEqual(result.missing, ['new.png']);
  assert.deepEqual(result.added, ['readded-new.png'], 'same path with new bytes is a normal new file');
});

test('classify: new, edited, stale, missing and renames', () => {
  const local = new Map([
    ['same.png', { md5: MD5_A }],
    ['new.png', { md5: MD5_C }],
    ['edited.png', { md5: MD5_C }],
    ['stale.png', { md5: MD5_A }],
    ['renamed-to.png', { md5: MD5_B }],
    ['copy-1.png', { md5: 'd'.repeat(32) }],
    ['copy-2.png', { md5: 'd'.repeat(32) }],
  ]);
  const lock = new Map([
    ['same.png', MD5_A], ['edited.png', MD5_A], ['stale.png', MD5_B], ['renamed-from.png', MD5_B], ['gone.png', 'e'.repeat(32)],
    ['dup-from.png', 'd'.repeat(32)],
  ]);
  const history = new Map([['stale.png', new Set([MD5_A, MD5_B])], ['edited.png', new Set([MD5_A])]]);
  const result = classify({ local, lock, history });
  assert.deepEqual(result.unchanged, ['same.png']);
  assert.deepEqual(result.changed, ['edited.png']);
  assert.deepEqual(result.stale, ['stale.png']);
  assert.deepEqual(result.missing, ['gone.png']);
  assert.deepEqual(result.renames, [{ from: 'dup-from.png', to: 'copy-1.png' }, { from: 'renamed-from.png', to: 'renamed-to.png' }]);
  assert.deepEqual(result.added, ['copy-2.png', 'new.png']);
});

test('quota: refuse when free < upload + reserve; no limit reported is not a refusal', () => {
  assert.deepEqual(quotaCheck({ free: 10e9 }, 3.7e9, 2e9), { status: 'ok', free: 10e9, need: 5.7e9 });
  assert.deepEqual(quotaCheck({ free: 5e9 }, 3.7e9, 2e9), { status: 'low', free: 5e9, need: 5.7e9 });
  // No `free` but a total: free = total - used - other (Drive's `used` already holds the trash).
  assert.deepEqual(quotaCheck({ total: 15e9, used: 6e9, trashed: 1e9, other: 2e9 }, 1e9, 2e9), { status: 'ok', free: 7e9, need: 3e9 });
  assert.equal(quotaCheck({ total: 15e9, used: 12e9, other: 2e9 }, 1, 2e9).status, 'low');
  // Workspace pooled or unlimited storage: rclone about answers without total or free.
  assert.equal(quotaCheck({ used: 6e9, trashed: 0, other: 1e9 }, 1, 2e9).status, 'unlimited');
  assert.equal(quotaCheck({}, 1, 2e9).status, 'unlimited');
  assert.equal(quotaCheck(null, 1, 2e9).status, 'unknown', 'rclone about failed: refuse');
});

test('stamps: a new lock copy is always newer than every copy on Drive, even with a clock behind', () => {
  const now = new Date(Date.UTC(2026, 9, 22, 10, 0, 0));
  assert.deepEqual(nextStamp(now, null), { stamp: '2026-10-22_100000Z', clockBehind: false });
  assert.deepEqual(nextStamp(now, '2026-10-22_095959Z'), { stamp: '2026-10-22_100000Z', clockBehind: false });
  assert.deepEqual(nextStamp(now, '2026-10-22_100000Z'), { stamp: '2026-10-22_100001Z', clockBehind: false }, 'same second: next second');
  assert.deepEqual(nextStamp(now, '2026-10-22_235959Z'), { stamp: '2026-10-23_000000Z', clockBehind: true });
});

test('drift: newest Drive copies first, stop at the first copy this clone fully knows', () => {
  const lock = new Map([['art-src/a.png', MD5_A]]);
  const head = new Map([['art-src/a.png', new Set([MD5_A])]]);
  const all = new Map([['art-src/a.png', new Set([MD5_A])], ['art-src/feat.png', new Set([MD5_C])]]);
  const knownHere = (key, md5) => lock.get(key) === md5 || Boolean(head.get(key)?.has(md5));
  const rules = { knownHere, knownInClone: (key, md5) => knownHere(key, md5) || Boolean(all.get(key)?.has(md5)) };
  const copy = (stamp, entries) => ({ stamp, entries: new Map(entries) });

  // A version replaced twice before one commit (B never committed) sits in an older copy: superseded.
  const superseded = compareDriveCopies([copy('3', [['art-src/a.png', MD5_A]]), copy('2', [['art-src/a.png', MD5_B]])], rules);
  assert.deepEqual(superseded.drift, []);
  assert.equal(superseded.settled, true);

  // Another machine pushed after the copy this clone knows.
  const other = compareDriveCopies([copy('4', [['art-src/a.png', MD5_B]]), copy('3', [['art-src/a.png', MD5_A]])], rules);
  assert.deepEqual(other.drift, [{ key: 'art-src/a.png', stamp: '4' }]);

  // Pushed from another local branch: known to the clone, so no refusal, only a note.
  const branch = compareDriveCopies([copy('5', [['art-src/a.png', MD5_A], ['art-src/feat.png', MD5_C]])], rules);
  assert.deepEqual(branch.drift, []);
  assert.deepEqual(branch.otherBranch, ['art-src/feat.png']);

  // Lines of sets this push does not touch are ignored.
  const scoped = compareDriveCopies([copy('6', [['public/x.glb', MD5_B]])], { ...rules, relevant: (key) => key.startsWith('art-src/') });
  assert.deepEqual(scoped.drift, []);
  assert.equal(compareDriveCopies([], rules).settled, false);
});

test('rclone allowlist: copy-style commands only, dedupe only in skip mode', () => {
  for (const args of [
    ['version'], ['listremotes'], ['config', 'file'], ['config', 'dump'], ['config', 'create', 'tgmedia', 'drive', 'scope=drive', '--no-output'],
    ['config', 'reconnect', 'tgmedia:'], ['config', 'update', 'tgmedia', 'root_folder_id=x', 'config_refresh_token=false'],
    ['about', 'tgmedia:', '--json'], ['mkdir', 'tgmedia:typing-game-media'], ['lsjson', 'tgmedia:'], ['lsf', 'tgmedia:'], ['size', 'tgmedia:x'],
    ['copy', 'a', 'tgmedia:repo', '--files-from-raw', 'l', '--checksum', '--backup-dir', 'tgmedia:_replaced/s/repo'],
    ['copyto', 'README.txt', 'tgmedia:README.txt'], ['check', 'sum', 'tgmedia:repo', '--checkfile', 'md5', '--one-way'],
    ['dedupe', '--dedupe-mode', 'skip', 'tgmedia:repo'],
  ]) assert.equal(assertAllowed(args), true, args.join(' '));
  for (const args of [
    ['sync', 'a', 'tgmedia:'], ['bisync', 'a', 'tgmedia:'], ['move', 'a', 'tgmedia:'], ['moveto', 'a', 'tgmedia:b'], ['delete', 'tgmedia:x'],
    ['deletefile', 'tgmedia:x'], ['purge', 'tgmedia:x'], ['rmdir', 'tgmedia:x'], ['rmdirs', 'tgmedia:x'], ['cleanup', 'tgmedia:'],
    ['config', 'delete', 'tgmedia'], ['config', 'show'], ['config', 'password', 'tgmedia', 'x', 'y'],
    ['copy', 'a', 'tgmedia:', '--delete-excluded'], ['copy', 'a', 'tgmedia:', '--remove-source-files'],
    ['dedupe', 'tgmedia:repo'], ['dedupe', '--dedupe-mode', 'newest', 'tgmedia:repo'], ['dedupe', '--dedupe-mode', 'identical', 'tgmedia:repo'],
    ['dedupe', '--dedupe-mode', 'skip', 'rename', 'tgmedia:repo'], ['dedupe', '--dedupe-mode', 'skip', '--by-hash', 'tgmedia:repo'],
    ['dedupe', '--dedupe-mode=skip', '--dedupe-mode=first', 'tgmedia:repo'], [],
  ]) assert.throws(() => assertAllowed(args), Error, args.join(' '));
});

test('redact: tokens and secrets never reach the terminal', () => {
  // Built from parts so this file itself never looks like a leaked secret to the scan below.
  const google = ['GOCSPX', 'SECRETSECRET'].join('-');
  const refresh = ['"refresh', 'token":"1//0gSECRETSECRETSECRET"'].join('_');
  const samples = [
    `token = {"access_token":"ya29.a0AfB_byDEADBEEF","token_type":"Bearer",${refresh},"expiry":"2026"}`,
    '"token": "{\\"access_token\\":\\"ya29.SECRET\\",\\"refresh_token\\":\\"1//0SECRETSECRETSECRET\\"}"',
    `client_secret = ${google}`,
    `rclone config create tgmedia drive client_secret=${google}`,
    'Authorization: Bearer ya29.SECRETTOKEN',
  ];
  for (const sample of samples) {
    const output = redact(sample);
    assert.doesNotMatch(output, /SECRET|DEADBEEF/, output);
  }
  assert.equal(redact('Transferred: 12 MiB / 340 MiB, 3%'), 'Transferred: 12 MiB / 340 MiB, 3%');
});

test('rclone check --combined report parsing', () => {
  const report = parseCombined('= a.png\n+ missing dir/b (1).png\n* differ.glb\n! broken.bin\n- extra.png\nnoise\n');
  assert.deepEqual(report, {
    match: ['a.png'], missingOnRemote: ['missing dir/b (1).png'], differ: ['differ.glb'], error: ['broken.bin'], extraOnRemote: ['extra.png'],
  });
});

test('setup: the client secret is never an rclone argument', () => {
  const args = createArgs('tgmedia');
  assert.deepEqual(args, ['config', 'create', 'tgmedia', 'drive', 'scope=drive', '--no-output']);
  assert.ok(!args.some((arg) => /secret|token/i.test(arg)));
  assert.equal(remoteSection('tgmedia', 'id.apps.googleusercontent.com', 'GOCSPX-x'),
    '\n[tgmedia]\ntype = drive\nscope = drive\nclient_id = id.apps.googleusercontent.com\nclient_secret = GOCSPX-x\n');
  assert.throws(() => remoteSection('tgmedia', 'id', 'x\n[other]\ntype = local'));
});

test('hash cache: reused by size + mtime, refreshed when either changes', async () => {
  const dir = mkdtempSync(path.join(tmpdir(), 'media-hash-'));
  try {
    const file = write(dir, 'a.bin', 'one');
    const cacheFile = path.join(dir, 'cache.json');
    const entry = () => { const stats = statSync(file); return { abs: file, size: stats.size, mtimeMs: stats.mtimeMs, cacheKey: 'a.bin' }; };
    const first = entry();
    assert.equal(await hashEntries([first], new HashCache(cacheFile)), 1);
    assert.equal(first.md5, md5('one'));
    const second = entry();
    assert.equal(await hashEntries([second], new HashCache(cacheFile)), 0, 'cache hit');
    assert.equal(second.md5, md5('one'));
    writeFileSync(file, 'two!');
    const third = entry();
    assert.equal(await hashEntries([third], new HashCache(cacheFile)), 1);
    assert.equal(third.md5, md5('two!'));
    utimesSync(file, new Date(2020, 0, 1), new Date(2020, 0, 1));
    assert.equal(await hashEntries([entry()], new HashCache(cacheFile)), 1, 'mtime change re-hashes');
  } finally {
    rmSync(dir, { recursive: true, force: true });
  }
});

test('sets: walk the disk minus git ls-files, ignoring .gitignore', async (t) => {
  const fx = makeFixture();
  t.after(() => rmSync(fx.base, { recursive: true, force: true }));
  // WSL: a download from Windows leaves `name:Zone.Identifier` next to it. Junk, skipped quietly.
  write(fx.game, 'art-src/enemies/a.png:Zone.Identifier', '[ZoneTransfer]\nZoneId=3\n');
  write(fx.repo, 'shared/music/producer (1)/song a.m4a:Zone.Identifier', '[ZoneTransfer]\n');
  write(fx.game, 'art-src/enemies/what?.png', 'a name Windows cannot hold');
  const ctx = withGame(createContext({ root: fx.repo, out: { write() {} } }), 'space-typing');
  const { sets, notes } = await scanSets(ctx, ['originals', 'runtime', 'private']);
  const keys = (name) => sets[name].map((entry) => entry.key);
  assert.deepEqual(keys('originals'), [
    'art-src/3d/enemies/a.glb', 'art-src/enemies/a.png', 'art-src/models/blend/ships/v.blend', 'art-src/models/enemies/a.glb', 'art-src/models/raw/heroes/draconis.glb',
  ]);
  assert.deepEqual(notes.rawDuplicates.map((entry) => entry.rel), ['games/space-typing/art-src/models/raw/enemies/a.glb']);
  assert.deepEqual(keys('runtime'), [
    'docs/art-requests/map (1).png',
    'public/assets/space-typing/models/enemies/a/a.high.glb',
    'public/assets/space-typing/models/heroes/draconis/draconis.high.glb',
  ], 'ignored-but-untracked GLB and the tracked lost original are in; tracked webp, node_modules, dist, .visual are out');
  assert.deepEqual(notes.lostOriginals.map((entry) => entry.key), ['public/assets/space-typing/models/heroes/draconis/draconis.high.glb']);
  assert.deepEqual(keys('private'), [
    'games/space-typing/art-src/Dota-Sounds/Double Kill.wav',
    'games/space-typing/public/local-assets/announcer/a.ogg',
    'shared/music/producer (1)/song a.m4a',
  ]);
  assert.deepEqual(lostOriginalIds({ noOriginalOnThisMachine: { 'heroes/draconis, guides/draconis-v4': 'x', 'bosses/auriel-hero': 'y', 'not an id': 'z' } }),
    ['heroes/draconis', 'guides/draconis-v4', 'bosses/auriel-hero']);
  assert.deepEqual(notes.unsafe, ['games/space-typing/art-src/enemies/what?.png'], 'Zone.Identifier is junk; other Windows-forbidden names are reported');
});

test('sets: a models/raw file is dropped only when its art-src/3d twin is on this machine or in the lock', async (t) => {
  const fx = makeFixture();
  t.after(() => rmSync(fx.base, { recursive: true, force: true }));
  const ctx = withGame(createContext({ root: fx.repo, out: { write() {} } }), 'space-typing');
  const raw = 'art-src/models/raw/enemies/a.glb';
  // A machine whose art-src/3d is incomplete: SOURCES.json alone is not enough.
  rmSync(path.join(fx.game, 'art-src/3d/enemies/a.glb'));
  const incomplete = await scanSets(ctx, ['originals'], { gameLock: null });
  assert.ok(incomplete.sets.originals.some((entry) => entry.key === raw), 'kept and pushed');
  assert.ok(incomplete.notes.rawKept.some((entry) => entry.key === raw), 'listed in --dry-run');
  // The twin is already verified on Drive (in the lock): the raw copy is redundant.
  const locked = await scanSets(ctx, ['originals'], { gameLock: new Map([['art-src/3d/enemies/a.glb', md5(CONTENT.glbA)]]) });
  assert.ok(!locked.sets.originals.some((entry) => entry.key === raw));
  assert.deepEqual(locked.notes.rawDuplicates.map((entry) => entry.rel), [`games/space-typing/${raw}`]);
  // The lock lists another file under that md5 but outside art-src/3d: not a twin.
  const elsewhere = await scanSets(ctx, ['originals'], { gameLock: new Map([['art-src/enemies/a.glb', md5(CONTENT.glbA)]]) });
  assert.ok(elsewhere.sets.originals.some((entry) => entry.key === raw));
});

test('lock keys stay inside their set (locks come from a public repo and from Drive)', () => {
  const config = loadConfig(REPO_ROOT);
  const space = findGame(config, 'space-typing');
  for (const key of ['art-src/3d/enemies/a.glb', 'art-src/notes/prompt.txt', 'public/assets/space-typing/models/a/a.high.glb',
    'docs/art-requests/map (1).png', 'public/assets/space-typing/ships/3d/razor/height.bin']) {
    assert.equal(lockKeyProblem(config, 'game', key, space), null, key);
  }
  for (const key of ['.git/hooks/pre-push', 'scripts/x.mjs', 'public/a.js', 'node_modules/x/a.png', 'dist/a.png', '.visual/a.png',
    'art-src/Dota-Sounds/a.wav', 'public/local-assets/a.ogg', 'art-src/.git/config', 'src/.git/a.png']) {
    assert.notEqual(lockKeyProblem(config, 'game', key, space), null, key);
  }
  // Space's private folders are not private inside another game.
  const dragon = findGame(config, 'dragon-hold');
  assert.equal(lockKeyProblem(config, 'game', 'art-src/Dota-Sounds/a.wav', dragon), null);
  assert.equal(lockKeyProblem(config, 'game', 'public/assets/dragon-hold/models/units/a/a.high.glb', dragon), null);
  assert.notEqual(lockKeyProblem(config, 'game', 'scripts/x.mjs', dragon), null);
  assert.throws(() => lockKeyProblem(config, 'game', 'art-src/a.png'), /game nào/);
  assert.equal(lockKeyProblem(config, 'private', 'shared/music/a b/song.m4a'), null);
  assert.equal(lockKeyProblem(config, 'private', 'games/space-typing/public/local-assets/a.ogg'), null);
  for (const key of ['scripts/media/media.mjs', '.git/hooks/pre-push', 'shared/music/.git/x', 'shared/musicx/a.m4a']) {
    assert.notEqual(lockKeyProblem(config, 'private', key), null, key);
  }
  assert.throws(() => assertLockKeys(config, 'game', new Map([['scripts/x.mjs', MD5_A]]), 'media.md5', space), /ngoài nhóm/);
  assert.equal(assertLockKeys(config, 'game', null, 'media.md5', space), null);
});

test('runtime references: manifest URLs and ship textures with their ?v= hash', (t) => {
  const dir = mkdtempSync(path.join(tmpdir(), 'media-refs-'));
  t.after(() => rmSync(dir, { recursive: true, force: true }));
  write(dir, 'public/assets/space-typing/models/manifest.json', JSON.stringify({
    models: { 'enemies/a': { tiers: { high: { url: '/assets/space-typing/models/enemies/a/a.high.glb?v=abc123' } } } },
  }));
  write(dir, 'public/assets/space-typing/ships/3d/razor/model.json', JSON.stringify({ color: 'color.webp?v=def456', height: 'height.bin?v=0011' }));
  const refs = runtimeReferences(dir, {
    modelsManifest: 'public/assets/space-typing/models/manifest.json', ships3dDir: 'public/assets/space-typing/ships/3d',
  });
  assert.deepEqual(refs.map(({ key, version }) => [key, version]), [
    ['public/assets/space-typing/models/enemies/a/a.high.glb', 'abc123'],
    ['public/assets/space-typing/ships/3d/razor/color.webp', 'def456'],
    ['public/assets/space-typing/ships/3d/razor/height.bin', '0011'],
  ]);
});

test('push plan: --forget, auto-forget of unreferenced models, missing files need an answer', async (t) => {
  const fx = makeFixture();
  t.after(() => rmSync(fx.base, { recursive: true, force: true }));
  const ctx = withGame(createContext({ root: fx.repo, out: { write() {} } }), 'space-typing');
  const lock = [
    [md5(CONTENT.glbA), 'art-src/3d/enemies/a.glb'],
    [MD5_A, 'public/assets/space-typing/models/enemies/old/old.high.glb'],
    [md5(CONTENT.runtimeGlb), 'public/assets/space-typing/models/enemies/a/a.high.glb'],
    [MD5_C, 'docs/art-requests/gone.png'],
    [MD5_C, 'docs/art-requests/forgotten.png'],
  ].map(([hash, file]) => `${hash}  ${file}`).sort((a, b) => (a.slice(34) < b.slice(34) ? -1 : 1)).join('\n');
  writeFileSync(path.join(fx.game, 'media.md5'), `${lock}\n`);
  rmSync(path.join(fx.game, 'public/assets/space-typing/models/enemies/a/a.high.glb'));
  const state = await loadState(ctx, ['originals', 'runtime']);
  const planned = planPush(ctx, state, ['originals', 'runtime'], { forget: ['games/space-typing/docs/art-requests/forgotten.png'] });
  const runtime = planned.sets.runtime;
  assert.deepEqual(runtime.autoForgotten, ['public/assets/space-typing/models/enemies/old/old.high.glb'], 'not in the manifest any more');
  assert.deepEqual(runtime.forgotten, ['docs/art-requests/forgotten.png']);
  assert.deepEqual(runtime.missing, ['docs/art-requests/gone.png', 'public/assets/space-typing/models/enemies/a/a.high.glb'],
    'a missing file the manifest still uses, or one outside the manifest folders, needs an answer');
  assert.ok(runtime.questions.some((question) => question.kind === 'missing'));
  assert.equal(planned.problems.length, 0);
  assert.ok(!runtime.newLock.has('public/assets/space-typing/models/enemies/old/old.high.glb'));

  const unknown = planPush(ctx, state, ['runtime'], { forget: ['games/space-typing/docs/nope.png'] });
  assert.match(unknown.problems[0].title, /không khớp file nào/);

  const additive = planPush(ctx, state, ['runtime'], { 'new-only': true });
  assert.deepEqual(additive.sets.runtime.questions, []);
  assert.ok(additive.sets.runtime.newLock.has('docs/art-requests/gone.png'), '--new-only keeps every lock line');
  assert.deepEqual(additive.sets.runtime.autoForgotten, [], '--new-only never auto-forgets: that machine may just not have pulled');
  assert.ok(additive.sets.runtime.newLock.has('public/assets/space-typing/models/enemies/old/old.high.glb'));
});

test('push plan: --yes never accepts a rename; --forget <old name> does; --readd brings back a dropped path', async (t) => {
  const fx = makeFixture();
  t.after(() => rmSync(fx.base, { recursive: true, force: true }));
  const ctx = withGame(createContext({ root: fx.repo, out: { write() {} }, stdin: { isTTY: false } }), 'space-typing');
  // Lock v1 lists art-src/enemies/a.png; v2 renamed it to placeholder.png and dropped forgotten.png.
  writeFileSync(path.join(fx.game, 'media.md5'), `${md5(CONTENT.pngV1)}  art-src/enemies/a.png\n${MD5_B}  art-src/enemies/forgotten.png\n`);
  git(fx.game, 'add', '-f', 'media.md5');
  git(fx.game, 'commit', '-q', '-m', 'v1');
  writeFileSync(path.join(fx.game, 'media.md5'), `${md5(CONTENT.pngV1)}  art-src/enemies/old-name.png\n`);
  git(fx.game, 'commit', '-q', '-am', 'v2');
  write(fx.game, 'art-src/enemies/forgotten-again.png', 'x');
  rmSync(path.join(fx.game, 'art-src/enemies/a.png'));
  write(fx.game, 'art-src/enemies/new-name.png', CONTENT.pngV1);
  const state = await loadState(ctx, ['originals']);
  assert.deepEqual(state.perSet.originals.plan.renames, [{ from: 'art-src/enemies/old-name.png', to: 'art-src/enemies/new-name.png' }]);

  const planned = planPush(ctx, state, ['originals'], {});
  assert.deepEqual(planned.sets.originals.questions.map((question) => question.kind), ['rename']);
  await assert.rejects(askQuestions(ctx, planned, { yes: true }), /Cần xác nhận.*--forget <đường dẫn cũ>/s);

  const confirmed = planPush(ctx, state, ['originals'], { forget: ['games/space-typing/art-src/enemies/old-name.png'] });
  assert.deepEqual(confirmed.sets.originals.questions, []);
  assert.equal(confirmed.problems.length, 0);
  assert.ok(confirmed.sets.originals.newLock.has('art-src/enemies/new-name.png'));
  assert.ok(!confirmed.sets.originals.newLock.has('art-src/enemies/old-name.png'));

  // a.png with the v1 bytes would have been "added" before; now it is removedElsewhere.
  write(fx.game, 'art-src/enemies/a.png', CONTENT.pngV1);
  const again = await loadState(ctx, ['originals']);
  assert.deepEqual(again.perSet.originals.plan.removedElsewhere, ['art-src/enemies/a.png']);
  const skipped = planPush(ctx, again, ['originals'], { forget: ['games/space-typing/art-src/enemies/old-name.png'] });
  assert.ok(!skipped.sets.originals.upload.includes('art-src/enemies/a.png'));
  assert.ok(skipped.warnings.some((warning) => /--readd/.test(warning)));
  const readded = planPush(ctx, again, ['originals'], { forget: ['games/space-typing/art-src/enemies/old-name.png'], readd: ['games/space-typing/art-src/enemies/a.png'] });
  assert.ok(readded.sets.originals.upload.includes('art-src/enemies/a.png'));
  assert.equal(readded.sets.originals.newLock.get('art-src/enemies/a.png'), md5(CONTENT.pngV1));
  const unused = planPush(ctx, again, ['originals'], { readd: ['games/space-typing/art-src/nothing.png'] });
  assert.ok(unused.problems.some((problem) => /--readd .*không khớp/.test(problem.title)));
});

test('git helpers: lock history and detached HEAD', (t) => {
  const dir = mkdtempSync(path.join(tmpdir(), 'media-git-'));
  t.after(() => rmSync(dir, { recursive: true, force: true }));
  git(dir, 'init', '-q');
  writeFileSync(path.join(dir, 'media.md5'), `${MD5_A}  art-src/a.png\n`);
  git(dir, 'add', 'media.md5');
  git(dir, 'commit', '-q', '-m', 'v1');
  writeFileSync(path.join(dir, 'media.md5'), `${MD5_B}  art-src/a.png\n`);
  git(dir, 'commit', '-q', '-am', 'v2');
  assert.deepEqual([...lockHistory(dir, 'media.md5').get('art-src/a.png')].sort(), [MD5_A, MD5_B]);
  // A lock committed on another branch: in the --all history only.
  git(dir, 'checkout', '-q', '-b', 'feat-x');
  writeFileSync(path.join(dir, 'media.md5'), `${MD5_B}  art-src/a.png\n${MD5_C}  art-src/feat.png\n`);
  git(dir, 'commit', '-q', '-am', 'feat');
  git(dir, 'checkout', '-q', 'main');
  assert.equal(lockHistory(dir, 'media.md5').has('art-src/feat.png'), false);
  assert.deepEqual([...lockHistory(dir, 'media.md5', { all: true }).get('art-src/feat.png')], [MD5_C]);
  assert.equal(isDetachedHead(dir), false);
  git(dir, 'checkout', '-q', '--detach');
  assert.equal(isDetachedHead(dir), true);
});

test('no OAuth token or client secret is committed in the parent repo', () => {
  const listed = spawnSync('git', ['ls-files', '-co', '--exclude-standard', '-z'], { cwd: REPO_ROOT, encoding: 'utf8', maxBuffer: 64 * 1024 * 1024 });
  assert.equal(listed.status, 0);
  const files = listed.stdout.split('\0').filter(Boolean);
  assert.ok(!files.some((file) => /(^|\/)(rclone\.conf|[^/]*\.rclone\.conf)$/.test(file)), 'rclone.conf is never in the repo');
  assert.ok(!files.includes('media/private.md5'), 'the private lock stays out of Git');
  const secret = /GOCSPX-[\w-]{10,}|\bya29\.[\w-]{20,}|\b1\/\/0[\w-]{30,}|"refresh_token"\s*:\s*"[^"*]{10,}"|^\s*token\s*=\s*\{/m;
  const offenders = [];
  for (const file of files) {
    let text;
    try {
      const stats = statSync(path.join(REPO_ROOT, file));
      if (!stats.isFile() || stats.size > 8 * 1024 * 1024) continue;
      text = readFileSync(path.join(REPO_ROOT, file), 'utf8');
    } catch {
      continue;
    }
    if (secret.test(text)) offenders.push(file);
  }
  assert.deepEqual(offenders, []);
});

test('config: games[] keeps Space first with the exact lock, Drive folder and lock copy it had', () => {
  const config = loadConfig(REPO_ROOT);
  assert.deepEqual(config.games.map((game) => game.id), ['space-typing', 'dragon-hold', 'typing-defense', 'typing-survival', 'immortality-cultivation']);
  assert.equal(config.game, undefined, 'the old single block is gone after loading');
  const space = config.games[0];
  // The values the single `game` block had: Drive paths must not move, or everything uploads again.
  assert.deepEqual({ ...space, id: undefined, title: undefined }, {
    id: undefined, title: undefined, dir: 'games/space-typing', lock: 'media.md5', pulledStamp: '.media-pulled', sources: 'art-src/3d/SOURCES.json',
    indexSourcesScript: 'games/space-typing/scripts/models/index-3d-sources.mjs', modelsDir: 'public/assets/space-typing/models',
    modelsManifest: 'public/assets/space-typing/models/manifest.json', ships3dDir: 'public/assets/space-typing/ships/3d',
  });
  const strip = ({ game, ...rest }) => rest;
  const definitions = setDefinitions(config, space);
  assert.deepEqual(strip(definitions.originals), { name: 'originals', lockFile: 'games/space-typing/media.md5', lockBase: 'games/space-typing', remoteBase: 'repo/games/space-typing', backup: true, confirmReplace: true, inGameLock: true });
  assert.deepEqual(strip(definitions.runtime), { name: 'runtime', lockFile: 'games/space-typing/media.md5', lockBase: 'games/space-typing', remoteBase: 'repo/games/space-typing', backup: false, confirmReplace: false, inGameLock: true });
  assert.deepEqual(strip(definitions.private), { name: 'private', lockFile: 'media/private.md5', lockBase: '', remoteBase: 'private', backup: true, confirmReplace: true, inGameLock: false });
  assert.equal(lockCopyName(space), 'space-typing.media.md5');
  for (const id of ['dragon-hold', 'typing-defense', 'typing-survival', 'immortality-cultivation']) {
    const game = findGame(config, id);
    assert.equal(game.dir, `games/${id}`);
    assert.equal(game.modelsManifest, `public/assets/${id}/models/manifest.json`);
    assert.equal(setDefinitions(config, game).originals.remoteBase, `repo/games/${id}`);
    assert.equal(setDefinitions(config, game).runtime.lockFile, `games/${id}/media.md5`);
    assert.equal(lockCopyName(game), `${id}.media.md5`);
  }
  assert.deepEqual(Object.keys(setDefinitions(config, null)), ['private'], 'no game: the private set only');
});

test('config: an older single game block still loads; bad or duplicate games are refused', (t) => {
  const dir = mkdtempSync(path.join(tmpdir(), 'media-config-'));
  t.after(() => rmSync(dir, { recursive: true, force: true }));
  const base = JSON.parse(readFileSync(path.join(REPO_ROOT, 'media/media.config.json'), 'utf8'));
  const space = base.games[0];
  const save = (value) => {
    mkdirSync(path.join(dir, 'media'), { recursive: true });
    writeFileSync(path.join(dir, 'media/media.config.json'), JSON.stringify(value));
  };
  const { games, ...rest } = base;
  const { id, title, ...legacyBlock } = space;
  save({ ...rest, game: legacyBlock });
  const legacy = loadConfig(dir);
  assert.deepEqual(legacy.games.map((game) => [game.id, game.dir]), [['space-typing', 'games/space-typing']]);
  save({ ...rest, games: [space, { ...space }] });
  assert.throws(() => loadConfig(dir), /trùng/);
  save({ ...rest, games: [space, { ...space, id: 'Bad Id', dir: 'games/x' }] });
  assert.throws(() => loadConfig(dir), /id không hợp lệ/);
  save({ ...rest, games: [space, { ...space, id: 'x', dir: '../outside' }] });
  assert.throws(() => loadConfig(dir), /dir không hợp lệ/);
  save({ ...rest, games: [] });
  assert.throws(() => loadConfig(dir), /games\[\]/);
});

test('games: a game whose folder is missing is skipped with one notice, never an error', async (t) => {
  const fx = makeFixture();
  t.after(() => rmSync(fx.base, { recursive: true, force: true }));
  let printed = '';
  const ctx = createContext({ root: fx.repo, out: { write(text) { printed += text; } } });
  assert.deepEqual(presentGames(withGame(ctx, 'space-typing')).map((game) => game.id), ['space-typing']);
  assert.deepEqual(presentGames(ctx).map((game) => game.id), ['space-typing'], 'cached across withGame copies');
  assert.equal(printed.match(/Bỏ qua games\/dragon-hold/g)?.length, 1);
  assert.match(printed, /Bỏ qua games\/typing-defense/);
  assert.match(printed, /Bỏ qua games\/typing-survival/);
  // The private set needs no game; it still reads Space's Git list for its folders.
  const { sets } = await scanSets(withGame(ctx, null), ['private']);
  assert.deepEqual(sets.private.map((entry) => entry.key), [
    'games/space-typing/art-src/Dota-Sounds/Double Kill.wav', 'games/space-typing/public/local-assets/announcer/a.ogg', 'shared/music/producer (1)/song a.m4a',
  ]);
  await assert.rejects(scanSets(withGame(ctx, null), ['originals']), /game nào/);

  const status = runMedia(fx, 'status');
  assert.equal(status.code, 0, status.out);
  assert.match(status.stdout, /Bỏ qua games\/dragon-hold: chưa có thư mục/);
  assert.match(status.stdout, /games\/space-typing \(Space Typing\):\n {2}Chưa có games\/space-typing\/media\.md5/);
  const check = runMedia(fx, 'check', '--only', 'runtime');
  assert.match(check.stdout, /Bỏ qua games\/typing-survival/);
  assert.doesNotMatch(check.out, /Error|at file:/);

  // Even Space missing is a notice: the private set still works.
  rmSync(fx.game, { recursive: true, force: true });
  const privateOnly = runMedia(fx, 'status');
  assert.equal(privateOnly.code, 0, privateOnly.out);
  assert.match(privateOnly.stdout, /Bỏ qua games\/space-typing/);
  assert.match(privateOnly.stdout, /private {4}1 file/);
});

test('sets: a second game has its own originals, runtime, lock base and Drive folder', async (t) => {
  const fx = makeFixture();
  t.after(() => rmSync(fx.base, { recursive: true, force: true }));
  addDragonHold(fx);
  const ctx = createContext({ root: fx.repo, out: { write() {} } });
  assert.deepEqual(presentGames(ctx).map((game) => game.id), ['space-typing', 'dragon-hold']);
  const dragon = withGame(ctx, 'dragon-hold');
  const { sets, notes } = await scanSets(dragon, ['originals', 'runtime']);
  assert.deepEqual(sets.originals.map((entry) => [entry.key, entry.rel]), [
    ['art-src/3d/units/warden.glb', 'games/dragon-hold/art-src/3d/units/warden.glb'],
    ['art-src/units/warden.png', 'games/dragon-hold/art-src/units/warden.png'],
  ]);
  assert.deepEqual(sets.runtime.map((entry) => entry.key), ['public/assets/dragon-hold/models/units/warden/warden.high.glb']);
  assert.deepEqual(notes.unsafe, []);
  // Space's sets do not change when another game appears.
  const space = await scanSets(withGame(ctx, 'space-typing'), ['originals', 'runtime']);
  assert.ok(space.sets.originals.every((entry) => entry.rel.startsWith('games/space-typing/')));
  assert.ok(space.sets.runtime.every((entry) => entry.rel.startsWith('games/space-typing/')));
  assert.equal(space.sets.runtime.length, 3);

  const state = await loadState(dragon, ['originals', 'runtime']);
  assert.equal(state.perSet.originals.definition.remoteBase, 'repo/games/dragon-hold');
  assert.equal(state.gameLockExists, false);
  assert.deepEqual(state.perSet.runtime.plan.added, ['public/assets/dragon-hold/models/units/warden/warden.high.glb']);
  assert.equal(md5(DRAGON.glb), state.perSet.originals.local.get('art-src/3d/units/warden.glb').md5);
  const planned = planPush(dragon, state, ['originals', 'runtime'], {});
  assert.equal(planned.problems.length, 0, JSON.stringify(planned.problems));
  // A --forget meant for Space is not refused inside Dragonhold's plan when the caller checks all games.
  const scoped = planPush(dragon, state, ['runtime'], { forget: ['games/space-typing/docs/x.png'] }, { reportUnused: false });
  assert.equal(scoped.problems.length, 0);
  assert.equal(scoped.usedForget.size, 0);
});

// Runs the REAL rclone against a local folder standing in for Drive:
// push -> check --remote -> pull --to -> md5, plus replace, stale, rename,
// forget, pull back into the repo, and the two-machine and two-branch cases.
// Skipped when rclone is not installed.
import assert from 'node:assert/strict';
import { chmodSync, existsSync, mkdirSync, readdirSync, readFileSync, renameSync, rmSync, writeFileSync } from 'node:fs';
import path from 'node:path';
import test from 'node:test';
import { addDragonHold, CONTENT, DRAGON, git, hasRclone, makeFixture, md5, runMedia, write } from './fixture.mjs';

const GAME_REMOTE = 'repo/games/space-typing';

function listFiles(root) {
  const files = [];
  const walk = (dir, prefix) => {
    if (!existsSync(dir)) return;
    for (const entry of readdirSync(dir, { withFileTypes: true })) {
      const rel = prefix ? `${prefix}/${entry.name}` : entry.name;
      if (entry.isDirectory()) walk(path.join(dir, entry.name), rel);
      else files.push(rel);
    }
  };
  walk(root, '');
  return files.sort();
}

const read = (root, rel) => readFileSync(path.join(root, rel), 'utf8');

/** Newest _locks/<stamp>/ that holds the game lock copy, and its text. */
function newestGameCopy(drive) {
  const locks = path.join(drive, '_locks');
  const stamps = readdirSync(locks).filter((stamp) => existsSync(path.join(locks, stamp, 'space-typing.media.md5'))).sort();
  const stamp = stamps.at(-1);
  return { stamp, text: readFileSync(path.join(locks, stamp, 'space-typing.media.md5'), 'utf8') };
}

function commitLock(game, message) {
  if (git(game, 'status', '--porcelain', '--', 'media.md5').trim()) {
    git(game, 'add', 'media.md5');
    git(game, 'commit', '-q', '-m', message);
  }
}

test('media store round trip with the real rclone on a local remote', { skip: !hasRclone() && 'rclone is not installed' }, async (t) => {
  const fx = makeFixture();
  t.after(() => rmSync(fx.base, { recursive: true, force: true }));
  const lockFile = path.join(fx.game, 'media.md5');

  await t.test('pnpm-style "push -- --dry-run" changes nothing', () => {
    const result = runMedia(fx, 'push', '--', '--dry-run');
    assert.equal(result.code, 0, result.out);
    assert.match(result.stdout, /Đẩy thử/);
    assert.match(result.stdout, /art-src\/models\/raw\/heroes\/draconis\.glb/, 'a raw model with no twin in SOURCES.json is listed');
    assert.match(result.stdout, /art-src\/models\/blend\/ships\/v\.blend/);
    assert.match(result.stdout, /art-src\/models\/raw: 1 file trùng md5/);
    assert.deepEqual(listFiles(fx.drive), []);
    assert.equal(existsSync(lockFile), false);
    const plan = read(fx.repo, '.cache/media-push-dry-run.txt');
    assert.doesNotMatch(plan, /\.zip|_out|node_modules|\/dist\/|\.visual|\.DS_Store|models\/raw\/enemies|campaign3d-model-cache|notes\.txt|index\.local\.json/);
  });

  await t.test('unknown flags fail closed before anything runs', () => {
    const result = runMedia(fx, 'push', '--dryrun');
    assert.equal(result.code, 2);
    assert.deepEqual(listFiles(fx.drive), []);
  });

  await t.test('first push uploads the three sets and writes the locks', () => {
    const result = runMedia(fx, 'push', '--yes');
    assert.equal(result.code, 0, result.out);
    const drive = listFiles(fx.drive);
    for (const expected of [
      `${GAME_REMOTE}/art-src/3d/enemies/a.glb`,
      `${GAME_REMOTE}/art-src/enemies/a.png`,
      `${GAME_REMOTE}/art-src/models/raw/heroes/draconis.glb`,
      `${GAME_REMOTE}/art-src/models/blend/ships/v.blend`,
      `${GAME_REMOTE}/art-src/models/enemies/a.glb`,
      `${GAME_REMOTE}/public/assets/space-typing/models/enemies/a/a.high.glb`,
      `${GAME_REMOTE}/public/assets/space-typing/models/heroes/draconis/draconis.high.glb`,
      `${GAME_REMOTE}/docs/art-requests/map (1).png`,
      'private/shared/music/producer (1)/song a.m4a',
      'private/games/space-typing/art-src/Dota-Sounds/Double Kill.wav',
      'private/games/space-typing/public/local-assets/announcer/a.ogg',
    ]) assert.ok(drive.includes(expected), `${expected} is on Drive:\n${drive.join('\n')}`);
    for (const pattern of [/\.zip$/, /_out\//, /node_modules/, /\/dist\//, /\.visual/, /\.DS_Store/, /models\/raw\/enemies/,
      /model-cache/, /index\.local\.json/, /shared\/music\/README\.md/, /background\.webp/, /notes\.txt/,
      new RegExp(`^${GAME_REMOTE}/art-src/Dota-Sounds`), new RegExp(`^${GAME_REMOTE}/public/local-assets`)]) {
      assert.equal(drive.filter((file) => pattern.test(file)).length, 0, `${pattern} must not be on Drive`);
    }
    const lock = readFileSync(lockFile, 'utf8');
    assert.ok(lock.endsWith('\n') && !lock.includes('\r'));
    const lines = lock.trim().split('\n');
    const paths = lines.map((line) => line.slice(34));
    assert.deepEqual(paths, [...paths].sort(), 'sorted by path');
    assert.ok(lines.includes(`${md5(CONTENT.glbA)}  art-src/3d/enemies/a.glb`));
    assert.doesNotMatch(lock, /Dota-Sounds|local-assets|shared\/music/, 'private paths never reach the tracked lock');
    const privateLock = read(fx.repo, 'media/private.md5');
    assert.match(privateLock, /shared\/music\/producer \(1\)\/song a\.m4a/);
    const lockCopies = drive.filter((file) => file.startsWith('_locks/'));
    assert.ok(lockCopies.some((file) => file.endsWith('/space-typing.media.md5')));
    assert.ok(lockCopies.some((file) => file.endsWith('/private.md5')));
    assert.match(result.stdout, /git -C games\/space-typing add media\.md5/);
    assert.equal(git(fx.game, 'status', '--porcelain', '--', 'media.md5').trim(), '?? media.md5', 'the script never stages or commits');
  });

  await t.test('check --remote is clean', () => {
    const result = runMedia(fx, 'check', '--remote');
    assert.equal(result.code, 0, result.out);
    assert.match(result.stdout, /art-src\/3d: 1\/1 khớp/);
    assert.match(result.stdout, /✓ Khớp/);
  });

  await t.test('pull --to restores every file with matching md5', () => {
    const restore = path.join(fx.base, 'restore');
    const result = runMedia(fx, 'pull', '--to', restore);
    assert.equal(result.code, 0, result.out);
    assert.match(result.stdout, /Đang tải \d+ file/);
    const restored = listFiles(restore);
    const lockLines = readFileSync(lockFile, 'utf8').trim().split('\n').length + read(fx.repo, 'media/private.md5').trim().split('\n').length;
    assert.equal(restored.length, lockLines);
    assert.match(result.stdout, new RegExp(`Khớp ${lockLines}/${lockLines}`));
    assert.equal(read(restore, 'games/space-typing/art-src/3d/enemies/a.glb'), CONTENT.glbA);
    assert.equal(read(restore, 'shared/music/producer (1)/song a.m4a'), CONTENT.song);
    assert.equal(existsSync(path.join(fx.game, '.media-pulled')), false, '--to never touches the repo');
  });

  await t.test('a file lost on Drive is reported by check --remote and uploaded again by push', () => {
    rmSync(path.join(fx.drive, GAME_REMOTE, 'art-src/3d/enemies/a.glb'));
    const checked = runMedia(fx, 'check', '--remote', '--only', 'originals');
    assert.equal(checked.code, 1, checked.out);
    assert.match(checked.stdout, /Thiếu trên Drive/);
    const result = runMedia(fx, 'push');
    assert.equal(result.code, 0, result.out);
    assert.match(result.stdout, /đẩy lại/);
    assert.match(result.stdout, /Không có gì mới để đẩy/);
    assert.equal(read(fx.drive, `${GAME_REMOTE}/art-src/3d/enemies/a.glb`), CONTENT.glbA);
  });

  git(fx.game, 'add', 'media.md5');
  git(fx.game, 'commit', '-q', '-m', 'lock v1');

  await t.test('replacing an original asks first and keeps the old copy in _replaced/', () => {
    writeFileSync(path.join(fx.game, 'art-src/enemies/a.png'), CONTENT.pngV2);
    const refused = runMedia(fx, 'push');
    assert.equal(refused.code, 1, refused.out);
    assert.match(refused.out, /Cần xác nhận/);
    assert.equal(read(fx.drive, `${GAME_REMOTE}/art-src/enemies/a.png`), CONTENT.pngV1);

    const result = runMedia(fx, 'push', '--yes');
    assert.equal(result.code, 0, result.out);
    assert.equal(read(fx.drive, `${GAME_REMOTE}/art-src/enemies/a.png`), CONTENT.pngV2);
    const backups = listFiles(fx.drive).filter((file) => file.startsWith('_replaced/') && file.endsWith(`${GAME_REMOTE}/art-src/enemies/a.png`));
    assert.equal(backups.length, 1);
    assert.equal(read(fx.drive, backups[0]), CONTENT.pngV1);
  });

  git(fx.game, 'add', 'media.md5');
  git(fx.game, 'commit', '-q', '-m', 'lock v2');

  await t.test('a stale copy (an older lock version) is refused by push and replaced by pull --update-stale', () => {
    writeFileSync(path.join(fx.game, 'art-src/enemies/a.png'), CONTENT.pngV1);
    const status = runMedia(fx, 'status');
    assert.match(status.stdout, /cũ hơn bản trên Drive \(1\)/);
    const refused = runMedia(fx, 'push', '--yes');
    assert.equal(refused.code, 1, refused.out);
    assert.match(refused.out, /cũ hơn bản trên Drive/);
    assert.equal(read(fx.drive, `${GAME_REMOTE}/art-src/enemies/a.png`), CONTENT.pngV2, 'Drive was not rolled back');

    const plain = runMedia(fx, 'pull', '--only', 'originals');
    assert.equal(plain.code, 0, plain.out);
    assert.equal(read(fx.game, 'art-src/enemies/a.png'), CONTENT.pngV1, 'plain pull never overwrites');

    const pulled = runMedia(fx, 'pull', '--update-stale', '--only', 'originals');
    assert.equal(pulled.code, 0, pulled.out);
    assert.equal(read(fx.game, 'art-src/enemies/a.png'), CONTENT.pngV2);
    const old = listFiles(path.join(fx.repo, '.media-old'));
    assert.equal(old.length, 1);
    assert.match(old[0], /games\/space-typing\/art-src\/enemies\/a\.png$/);
    assert.ok(existsSync(path.join(fx.game, '.media-pulled')));
  });

  await t.test('runtime files are replaced without a prompt or a backup', () => {
    writeFileSync(path.join(fx.game, 'public/assets/space-typing/models/enemies/a/a.high.glb'), `${CONTENT.runtimeGlb} rebuilt`);
    const result = runMedia(fx, 'push', '--only', 'runtime');
    assert.equal(result.code, 0, result.out);
    assert.equal(listFiles(fx.drive).filter((file) => file.startsWith('_replaced/') && file.includes('/public/')).length, 0);
  });

  await t.test('a rename is detected by md5, never accepted by --yes alone, and recorded under the new name', () => {
    renameSync(path.join(fx.game, 'art-src/enemies/a.png'), path.join(fx.game, 'art-src/enemies/a-renamed.png'));
    const status = runMedia(fx, 'status', '--only', 'originals');
    assert.match(status.stdout, /Đổi tên \(1\)/);
    const before = readFileSync(lockFile, 'utf8');
    const refused = runMedia(fx, 'push', '--yes', '--only', 'originals');
    assert.equal(refused.code, 1, refused.out);
    assert.match(refused.out, /Cần xác nhận.*--forget <đường dẫn cũ>/s);
    assert.equal(readFileSync(lockFile, 'utf8'), before);
    const result = runMedia(fx, 'push', '--only', 'originals', '--forget', 'games/space-typing/art-src/enemies/a.png');
    assert.equal(result.code, 0, result.out);
    const lock = readFileSync(lockFile, 'utf8');
    assert.match(lock, /art-src\/enemies\/a-renamed\.png/);
    assert.doesNotMatch(lock, /art-src\/enemies\/a\.png/);
    assert.ok(existsSync(path.join(fx.drive, GAME_REMOTE, 'art-src/enemies/a.png')), 'Drive keeps the old name');
  });

  await t.test('a deleted file blocks push until --forget, and Drive keeps it', () => {
    rmSync(path.join(fx.game, 'docs/art-requests/map (1).png'));
    const refused = runMedia(fx, 'push', '--only', 'runtime');
    assert.equal(refused.code, 1, refused.out);
    assert.match(refused.out, /pnpm media:pull|--forget/);
    const wrong = runMedia(fx, 'push', '--only', 'runtime', '--forget', 'games/space-typing/docs/nothing.png');
    assert.equal(wrong.code, 1);
    const result = runMedia(fx, 'push', '--only', 'runtime', '--forget', 'games/space-typing/docs/art-requests/map (1).png');
    assert.equal(result.code, 0, result.out);
    assert.doesNotMatch(readFileSync(lockFile, 'utf8'), /map \(1\)\.png/);
    assert.ok(existsSync(path.join(fx.drive, GAME_REMOTE, 'docs/art-requests/map (1).png')));
  });

  await t.test('pull brings a missing runtime file back and stamps .media-pulled', () => {
    const file = path.join(fx.game, 'public/assets/space-typing/models/enemies/a/a.high.glb');
    rmSync(path.join(fx.game, '.media-pulled'), { force: true });
    rmSync(file);
    const result = runMedia(fx, 'pull', '--only', 'runtime');
    assert.equal(result.code, 0, result.out);
    assert.equal(readFileSync(file, 'utf8'), `${CONTENT.runtimeGlb} rebuilt`);
    assert.ok(existsSync(path.join(fx.game, '.media-pulled')));
    assert.match(result.stdout, /play\.sh sẽ build lại/);
  });

  commitLock(fx.game, 'lock v3');

  await t.test('a download whose md5 differs from the lock is never put in place, so it never reaches the lock', () => {
    const rel = 'public/assets/space-typing/models/enemies/a/a.high.glb';
    const file = path.join(fx.game, rel);
    const driveFile = path.join(fx.drive, GAME_REMOTE, rel);
    const good = readFileSync(driveFile);
    writeFileSync(driveFile, 'changed on Drive by hand');
    rmSync(path.join(fx.game, '.media-pulled'), { force: true });
    rmSync(file);
    const pulled = runMedia(fx, 'pull', '--only', 'runtime');
    assert.equal(pulled.code, 1, pulled.out);
    assert.match(pulled.out, /khác md5/);
    assert.equal(existsSync(file), false, 'the unverified copy is not in the repo');
    assert.equal(existsSync(path.join(fx.game, '.media-pulled')), false, 'play.sh is not told to rebuild with it');
    assert.equal(existsSync(path.join(fx.repo, '.media-tmp')), false, 'staging folder removed');
    const parked = listFiles(path.join(fx.repo, '.media-old')).filter((item) => item.includes('/mismatch/'));
    assert.deepEqual(parked.map((item) => item.split('/mismatch/')[1]), [`games/space-typing/${rel}`]);

    const lockBefore = readFileSync(lockFile, 'utf8');
    const pushed = runMedia(fx, 'push', '--only', 'runtime');
    assert.equal(pushed.code, 1, pushed.out);
    assert.equal(readFileSync(lockFile, 'utf8'), lockBefore, 'no unverified md5 enters media.md5');

    writeFileSync(driveFile, good);
    const again = runMedia(fx, 'pull', '--only', 'runtime');
    assert.equal(again.code, 0, again.out);
    assert.equal(readFileSync(file, 'utf8'), `${CONTENT.runtimeGlb} rebuilt`);
    assert.ok(existsSync(path.join(fx.game, '.media-pulled')));
  });

  await t.test('a lock copy that cannot reach _locks/ leaves media.md5 unchanged; the next push copies it', { skip: process.getuid?.() === 0 && 'root ignores chmod' }, () => {
    write(fx.game, 'art-src/enemies/b.png', 'b art');
    const locks = path.join(fx.drive, '_locks');
    const before = readFileSync(lockFile, 'utf8');
    const copiesBefore = readdirSync(locks).length;
    chmodSync(locks, 0o555);
    let refused;
    try {
      refused = runMedia(fx, 'push', '--only', 'originals');
    } finally {
      chmodSync(locks, 0o755);
    }
    assert.equal(refused.code, 1, refused.out);
    assert.match(refused.out, /chưa chép được danh sách md5/);
    assert.equal(readFileSync(lockFile, 'utf8'), before, 'media.md5 unchanged');
    assert.equal(readdirSync(locks).length, copiesBefore);

    const result = runMedia(fx, 'push', '--only', 'originals');
    assert.equal(result.code, 0, result.out);
    const lock = readFileSync(lockFile, 'utf8');
    assert.match(lock, /art-src\/enemies\/b\.png/);
    assert.equal(newestGameCopy(fx.drive).text, lock);

    // A copy missing on Drive is copied again even when nothing is new.
    rmSync(path.join(locks, newestGameCopy(fx.drive).stamp), { recursive: true });
    assert.notEqual(newestGameCopy(fx.drive).text, lock);
    const healed = runMedia(fx, 'push', '--only', 'originals');
    assert.equal(healed.code, 0, healed.out);
    assert.match(healed.stdout, /đã chép lại vào _locks/);
    assert.match(healed.stdout, /Không có gì mới để đẩy/);
    assert.equal(newestGameCopy(fx.drive).text, lock);
  });

  commitLock(fx.game, 'lock v4');

  await t.test('a rename made on another machine is not undone here, even with --yes', () => {
    const oldName = path.join(fx.game, 'art-src/enemies/a-renamed.png');
    const newName = path.join(fx.game, 'art-src/enemies/a3.png');
    // Machine A renames and confirms with --forget <old name>, then commits.
    renameSync(oldName, newName);
    const renamed = runMedia(fx, 'push', '--only', 'originals', '--forget', 'games/space-typing/art-src/enemies/a-renamed.png');
    assert.equal(renamed.code, 0, renamed.out);
    commitLock(fx.game, 'A: rename');
    const lockA = readFileSync(lockFile, 'utf8');
    assert.match(lockA, /a3\.png/);

    // Machine B pulled Git, not the media yet: the old name on disk, the new one missing.
    renameSync(newName, oldName);
    const status = runMedia(fx, 'status', '--only', 'originals');
    assert.match(status.stdout, /Đã bị bỏ khỏi danh sách[^\n]*\(1\)/);
    assert.match(status.stdout, /Thiếu \(1\)/);
    assert.doesNotMatch(status.stdout, /Đổi tên \(1\)/);
    const refused = runMedia(fx, 'push', '--yes', '--only', 'originals');
    assert.equal(refused.code, 1, refused.out);
    assert.match(refused.out, /thiếu 1 file/);
    assert.doesNotMatch(refused.out, /có vẻ đã đổi tên/);
    assert.equal(readFileSync(lockFile, 'utf8'), lockA, 'the rename is not reversed');

    const pulled = runMedia(fx, 'pull', '--only', 'originals');
    assert.equal(pulled.code, 0, pulled.out);
    assert.equal(read(fx.game, 'art-src/enemies/a3.png'), CONTENT.pngV2);
    const again = runMedia(fx, 'push', '--yes', '--only', 'originals');
    assert.equal(again.code, 0, again.out);
    assert.match(again.stdout, /không đẩy lại/);
    assert.equal(readFileSync(lockFile, 'utf8'), lockA);
    rmSync(oldName);
  });

  await t.test('a file forgotten on another machine is not added back unless --readd', () => {
    const file = path.join(fx.game, 'art-src/enemies/b.png');
    rmSync(file);
    const forgotten = runMedia(fx, 'push', '--only', 'originals', '--forget', 'games/space-typing/art-src/enemies/b.png');
    assert.equal(forgotten.code, 0, forgotten.out);
    commitLock(fx.game, 'A: forget b.png');
    const lockA = readFileSync(lockFile, 'utf8');
    assert.doesNotMatch(lockA, /b\.png/);

    // Machine B still has b.png.
    writeFileSync(file, 'b art');
    const result = runMedia(fx, 'push', '--yes', '--only', 'originals');
    assert.equal(result.code, 0, result.out);
    assert.equal(readFileSync(lockFile, 'utf8'), lockA, 'b.png stays out');
    const unknown = runMedia(fx, 'push', '--only', 'originals', '--readd', 'games/space-typing/art-src/enemies/nothing.png');
    assert.equal(unknown.code, 1, unknown.out);
    const readded = runMedia(fx, 'push', '--only', 'originals', '--readd', 'games/space-typing/art-src/enemies/b.png');
    assert.equal(readded.code, 0, readded.out);
    assert.match(readFileSync(lockFile, 'utf8'), /art-src\/enemies\/b\.png/);
    commitLock(fx.game, 'B: readd b.png');
  });

  await t.test('a lock pushed from another branch of this clone is not taken for another machine', () => {
    git(fx.game, 'checkout', '-q', '-b', 'feat-x');
    const feature = write(fx.game, 'art-src/enemies/feat.png', 'feature art');
    const onFeature = runMedia(fx, 'push', '--only', 'originals');
    assert.equal(onFeature.code, 0, onFeature.out);
    commitLock(fx.game, 'feat-x: feat.png');
    git(fx.game, 'checkout', '-q', 'main');
    rmSync(feature);
    write(fx.game, 'art-src/enemies/main.png', 'main art');
    const onMain = runMedia(fx, 'push', '--only', 'originals');
    assert.equal(onMain.code, 0, onMain.out);
    assert.doesNotMatch(onMain.out, /máy khác/);
    assert.match(onMain.out, /nhánh khác/);
    const lock = readFileSync(lockFile, 'utf8');
    assert.match(lock, /main\.png/);
    assert.doesNotMatch(lock, /feat\.png/);
    commitLock(fx.game, 'main: main.png');
  });

  await t.test('a second machine without media.md5 and media/private.md5 still pulls from the Drive copies', () => {
    rmSync(path.join(fx.repo, 'media/private.md5'));
    rmSync(path.join(fx.repo, 'shared/music/producer (1)/song a.m4a'));
    const result = runMedia(fx, 'pull', '--only', 'private');
    assert.equal(result.code, 0, result.out);
    assert.equal(read(fx.repo, 'shared/music/producer (1)/song a.m4a'), CONTENT.song);
    assert.ok(existsSync(path.join(fx.repo, 'media/private.md5')));
  });

  await t.test('another machine pushed a newer lock: push refuses until git pull', () => {
    const latestText = newestGameCopy(fx.drive).text;
    const lines = `${latestText}${md5('elsewhere')}  art-src/enemies/zz-from-other-machine.png\n`.split('\n').filter(Boolean).sort();
    const newer = path.join(fx.drive, '_locks', '2999-01-01_000000Z');
    mkdirSync(newer, { recursive: true });
    writeFileSync(path.join(newer, 'space-typing.media.md5'), `${lines.join('\n')}\n`);
    writeFileSync(path.join(fx.game, 'art-src/enemies/new.png'), 'new art');
    const result = runMedia(fx, 'push', '--yes', '--only', 'originals');
    assert.equal(result.code, 1, result.out);
    assert.match(result.out, /máy khác/);
    assert.equal(existsSync(path.join(fx.drive, GAME_REMOTE, 'art-src/enemies/new.png')), false);
  });

  await t.test('the whole flow only ever ran allowlisted, non-destructive rclone subcommands', () => {
    const calls = readFileSync(fx.rcloneLog, 'utf8').trim().split('\n');
    const used = new Set(calls.map((line) => line.split(' ')[0]));
    for (const command of used) assert.ok(['version', 'config', 'lsf', 'lsjson', 'mkdir', 'copy', 'check', 'about', 'size'].includes(command), command);
    assert.ok(used.has('copy') && used.has('check'));
    for (const line of calls) {
      assert.doesNotMatch(line, /^(sync|bisync|move|moveto|delete|deletefile|purge|rmdirs?|cleanup|dedupe)\b/);
      if (line.startsWith('check ')) assert.match(line, /--one-way/);
      if (line.startsWith('copy ') && line.includes(' tgmedia:')) {
        assert.match(line, /--contimeout 10s --timeout 60s --retries 3 --low-level-retries 5 --tpslimit 8/);
        assert.match(line, /--transfers 4/);
      }
    }
  });
});

test('two games: each has its own lock, Drive folder and _locks copy; Space stays where it was', { skip: !hasRclone() && 'rclone is not installed' }, async (t) => {
  const fx = makeFixture();
  t.after(() => rmSync(fx.base, { recursive: true, force: true }));
  const dragon = addDragonHold(fx);
  const DRAGON_REMOTE = 'repo/games/dragon-hold';
  const spaceLock = path.join(fx.game, 'media.md5');
  const dragonLock = path.join(dragon, 'media.md5');

  await t.test('dry run lists both games and skips the missing ones', () => {
    const result = runMedia(fx, 'push', '--dry-run');
    assert.equal(result.code, 0, result.out);
    assert.match(result.stdout, /Bỏ qua games\/typing-defense/);
    assert.match(result.stdout, /originals → Drive repo\/games\/dragon-hold\//);
    const plan = read(fx.repo, '.cache/media-push-dry-run.txt');
    assert.match(plan, /games\/space-typing\/art-src\/3d\/enemies\/a\.glb/);
    assert.match(plan, /games\/dragon-hold\/art-src\/3d\/units\/warden\.glb/);
    assert.match(plan, /games\/dragon-hold\/public\/assets\/dragon-hold\/models\/units\/warden\/warden\.high\.glb/);
  });

  await t.test('one push uploads both games and writes one lock per game', () => {
    const result = runMedia(fx, 'push', '--yes');
    assert.equal(result.code, 0, result.out);
    const drive = listFiles(fx.drive);
    for (const expected of [
      `${GAME_REMOTE}/art-src/3d/enemies/a.glb`,
      `${GAME_REMOTE}/public/assets/space-typing/models/enemies/a/a.high.glb`,
      `${DRAGON_REMOTE}/art-src/3d/units/warden.glb`,
      `${DRAGON_REMOTE}/art-src/units/warden.png`,
      `${DRAGON_REMOTE}/public/assets/dragon-hold/models/units/warden/warden.high.glb`,
    ]) assert.ok(drive.includes(expected), `${expected} is on Drive:\n${drive.join('\n')}`);
    const copies = drive.filter((file) => file.startsWith('_locks/'));
    const stamps = new Set(copies.map((file) => file.split('/')[1]));
    assert.equal(stamps.size, 1, 'one stamp for the whole push');
    for (const name of ['space-typing.media.md5', 'dragon-hold.media.md5', 'private.md5']) assert.ok(copies.some((file) => file.endsWith(`/${name}`)), name);
    const space = readFileSync(spaceLock, 'utf8');
    const own = readFileSync(dragonLock, 'utf8');
    assert.doesNotMatch(space, /dragon-hold|warden/);
    assert.equal(own, [
      `${md5(DRAGON.glb)}  art-src/3d/units/warden.glb`,
      `${md5(DRAGON.png)}  art-src/units/warden.png`,
      `${md5(DRAGON.runtime)}  public/assets/dragon-hold/models/units/warden/warden.high.glb`,
    ].join('\n') + '\n');
    assert.equal(read(fx.drive, `_locks/${[...stamps][0]}/dragon-hold.media.md5`), own);
    assert.match(result.stdout, /git -C games\/space-typing add media\.md5/);
    assert.match(result.stdout, /git -C games\/dragon-hold add media\.md5/);
  });

  await t.test('check --remote and pull --to cover both games', () => {
    const checked = runMedia(fx, 'check', '--remote');
    assert.equal(checked.code, 0, checked.out);
    assert.match(checked.stdout, /games\/dragon-hold \(Rồng Giữ Ải\):/);
    assert.match(checked.stdout, new RegExp(`${DRAGON_REMOTE}/: khớp 3/3`));
    const restore = path.join(fx.base, 'restore-two');
    const result = runMedia(fx, 'pull', '--to', restore);
    assert.equal(result.code, 0, result.out);
    const total = [spaceLock, dragonLock, path.join(fx.repo, 'media/private.md5')]
      .reduce((sum, file) => sum + readFileSync(file, 'utf8').trim().split('\n').length, 0);
    assert.match(result.stdout, new RegExp(`Khớp ${total}/${total}`));
    assert.equal(read(restore, 'games/dragon-hold/art-src/3d/units/warden.glb'), DRAGON.glb);
    assert.equal(read(restore, 'games/space-typing/art-src/3d/enemies/a.glb'), CONTENT.glbA);
  });

  git(fx.game, 'add', 'media.md5');
  git(fx.game, 'commit', '-q', '-m', 'space lock');
  git(dragon, 'add', 'media.md5');
  git(dragon, 'commit', '-q', '-m', 'dragon lock');

  await t.test('pull restores a missing file of the second game and stamps only that game', () => {
    const file = path.join(dragon, 'public/assets/dragon-hold/models/units/warden/warden.high.glb');
    rmSync(file);
    const result = runMedia(fx, 'pull', '--only', 'runtime');
    assert.equal(result.code, 0, result.out);
    assert.equal(readFileSync(file, 'utf8'), DRAGON.runtime);
    assert.ok(existsSync(path.join(dragon, '.media-pulled')));
    assert.equal(existsSync(path.join(fx.game, '.media-pulled')), false);
    assert.match(result.stdout, /play\.sh sẽ build lại Rồng Giữ Ải/);
  });

  await t.test('--forget works across games; a pattern no game uses is refused', () => {
    rmSync(path.join(dragon, 'art-src/units/warden.png'));
    const before = readFileSync(spaceLock, 'utf8');
    const wrong = runMedia(fx, 'push', '--only', 'originals', '--forget', 'games/dragon-hold/art-src/units/warden.png', '--forget', 'games/dragon-hold/nothing.png');
    assert.equal(wrong.code, 1, wrong.out);
    assert.match(wrong.out, /--forget games\/dragon-hold\/nothing\.png: không khớp/);
    const result = runMedia(fx, 'push', '--only', 'originals', '--forget', 'games/dragon-hold/art-src/units/warden.png');
    assert.equal(result.code, 0, result.out);
    assert.doesNotMatch(readFileSync(dragonLock, 'utf8'), /warden\.png/);
    assert.equal(readFileSync(spaceLock, 'utf8'), before, 'Space lock untouched');
    assert.ok(existsSync(path.join(fx.drive, DRAGON_REMOTE, 'art-src/units/warden.png')), 'Drive keeps it');
  });
});

test('setup refuses an encrypted rclone.conf and a tgmedia remote that is not Google Drive (no network)', { skip: !hasRclone() && 'rclone is not installed' }, (t) => {
  const fx = makeFixture();
  t.after(() => rmSync(fx.base, { recursive: true, force: true }));
  const aliasConfig = readFileSync(fx.env.RCLONE_CONFIG, 'utf8');
  const notDrive = runMedia(fx, 'setup');
  assert.equal(notDrive.code, 1, notDrive.out);
  assert.match(notDrive.out, /không phải Google Drive/);
  assert.equal(readFileSync(fx.env.RCLONE_CONFIG, 'utf8'), aliasConfig, 'setup changed nothing');

  writeFileSync(fx.env.RCLONE_CONFIG, '# Encrypted rclone configuration File\n\nRCLONE_ENCRYPT_V0:\nabc\n');
  const encrypted = runMedia(fx, 'setup');
  assert.equal(encrypted.code, 1, encrypted.out);
  assert.match(encrypted.out, /mã hoá/);

  const withSecretFlag = runMedia(fx, 'setup', '--client-secret', 'x');
  assert.equal(withSecretFlag.code, 2, 'a secret is never accepted as a command-line flag');
  assert.deepEqual(listFiles(fx.drive), []);
});

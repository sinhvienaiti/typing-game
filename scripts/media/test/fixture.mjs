// A throwaway parent repo + game repo with every kind of media file the sets
// must include or skip, and an rclone "tgmedia" remote that is a local folder.
import { createHash } from 'node:crypto';
import { spawnSync } from 'node:child_process';
import { chmodSync, copyFileSync, mkdirSync, mkdtempSync, writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

export const REPO_ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '../../..');
export const SCRIPT = path.join(REPO_ROOT, 'scripts/media/media.mjs');

export const md5 = (content) => createHash('md5').update(content).digest('hex');
export const sha256 = (content) => createHash('sha256').update(content).digest('hex');

export function hasRclone() {
  const result = spawnSync(process.env.RCLONE_BIN || 'rclone', ['version'], { encoding: 'utf8' });
  return result.status === 0;
}

const GIT_ENV = {
  GIT_AUTHOR_NAME: 'media test', GIT_AUTHOR_EMAIL: 'media@test.invalid',
  GIT_COMMITTER_NAME: 'media test', GIT_COMMITTER_EMAIL: 'media@test.invalid',
  GIT_CONFIG_NOSYSTEM: '1',
};

export function git(cwd, ...args) {
  const result = spawnSync('git', ['-c', 'commit.gpgsign=false', '-c', 'core.hooksPath=/dev/null', '-c', 'init.defaultBranch=main', ...args],
    { cwd, encoding: 'utf8', env: { ...process.env, ...GIT_ENV } });
  if (result.status !== 0) throw new Error(`git ${args.join(' ')}: ${result.stderr}`);
  return result.stdout;
}

export function write(root, rel, content) {
  const file = path.join(root, rel);
  mkdirSync(path.dirname(file), { recursive: true });
  writeFileSync(file, content);
  return file;
}

export const CONTENT = {
  glbA: 'GLB-A original from Meshy',
  pngV1: 'PNG-A v1',
  pngV2: 'PNG-A version two',
  draconisOriginal: 'DRACONIS original only on this machine',
  blenderOut: 'normalized by Blender',
  blend: 'BLEND file',
  runtimeGlb: 'runtime enemy a high',
  lostGlb: 'draconis runtime, original lost',
  docPng: 'defense map layout',
  song: 'm4a song bytes',
  wav: 'double kill wav',
  ogg: 'announcer ogg',
};

/** Builds the fixture. Returns paths plus an env that points the CLI and rclone at it. */
export function makeFixture() {
  const base = mkdtempSync(path.join(tmpdir(), 'media-fixture-'));
  const repo = path.join(base, 'repo');
  const drive = path.join(base, 'drive');
  mkdirSync(drive, { recursive: true });
  mkdirSync(path.join(repo, 'media'), { recursive: true });
  copyFileSync(path.join(REPO_ROOT, 'media/media.config.json'), path.join(repo, 'media/media.config.json'));

  // Parent repo: tracked README and music index, untracked music.
  write(repo, 'README.md', 'parent\n');
  write(repo, 'shared/music/README.md', 'music\n');
  write(repo, 'shared/music/index.json', '{"version":1,"tracks":[]}\n');
  git(repo, 'init', '-q');
  git(repo, 'add', 'README.md', 'shared/music/README.md', 'shared/music/index.json', 'media/media.config.json');
  git(repo, 'commit', '-q', '-m', 'parent');
  write(repo, 'shared/music/index.local.json', '{"tracks":[1]}\n');
  write(repo, 'shared/music/producer (1)/song a.m4a', CONTENT.song);
  write(repo, 'shared/music/.DS_Store', 'junk');

  // Game repo (its own Git repo, like the submodule).
  const game = path.join(repo, 'games/space-typing');
  const runtimeUrl = '/assets/space-typing/models/enemies/a/a.high.glb';
  const lostUrl = '/assets/space-typing/models/heroes/draconis/draconis.high.glb';
  write(game, 'art-src/README.md', 'art\n');
  write(game, 'art-src/3d/SOURCES.json', `${JSON.stringify({
    version: 1,
    files: { 'enemies/a.glb': { md5: md5(CONTENT.glbA), bytes: CONTENT.glbA.length } },
    noOriginalOnThisMachine: { 'heroes/draconis': 'Only the runtime copy remains.' },
  }, null, 1)}\n`);
  write(game, 'public/assets/space-typing/models/manifest.json', `${JSON.stringify({
    version: 1,
    models: {
      'enemies/a': { tiers: { high: { url: `${runtimeUrl}?v=${sha256(CONTENT.runtimeGlb).slice(0, 10)}` } } },
      'heroes/draconis': { tiers: { high: { url: `${lostUrl}?v=${sha256(CONTENT.lostGlb).slice(0, 10)}` } } },
    },
  }, null, 1)}\n`);
  write(game, 'public/assets/space-typing/models/heroes/draconis/draconis.high.glb', CONTENT.lostGlb);
  write(game, 'public/assets/space-typing/background.webp', 'tracked webp');
  // Ignored by .gitignore, still untracked media: must be in the runtime set.
  write(game, '.gitignore', 'public/assets/space-typing/models/enemies/\nnode_modules/\ndist/\nart-src/*\n!art-src/README.md\n!art-src/3d/\nart-src/3d/*\n!art-src/3d/SOURCES.json\npublic/local-assets/\n');
  git(game, 'init', '-q');
  git(game, 'add', '-A');
  git(game, 'commit', '-q', '-m', 'game');

  write(game, 'art-src/3d/enemies/a.glb', CONTENT.glbA);
  write(game, 'art-src/enemies/a.png', CONTENT.pngV1);
  write(game, 'art-src/g01/_out/preview.png', 'generated preview');
  write(game, 'art-src/g01/pack.zip', 'zip bundle');
  write(game, 'art-src/models/raw/enemies/a.glb', CONTENT.glbA);
  write(game, 'art-src/models/raw/heroes/draconis.glb', CONTENT.draconisOriginal);
  write(game, 'art-src/models/enemies/a.glb', CONTENT.blenderOut);
  write(game, 'art-src/models/.campaign3d-model-cache/a.json', '{"source":"/abs/path"}');
  write(game, 'art-src/models/blend/ships/v.blend', CONTENT.blend);
  write(game, 'art-src/.DS_Store', 'junk');
  write(game, 'art-src/Dota-Sounds/Double Kill.wav', CONTENT.wav);
  write(game, 'public/local-assets/announcer/a.ogg', CONTENT.ogg);
  write(game, 'public/assets/space-typing/models/enemies/a/a.high.glb', CONTENT.runtimeGlb);
  write(game, 'docs/art-requests/map (1).png', CONTENT.docPng);
  write(game, 'node_modules/pkg/icon.png', 'dependency');
  write(game, 'dist/assets/x.png', 'build output');
  write(game, '.visual/shot.png', 'screenshot');
  write(game, 'src/notes.txt', 'not media');

  const rcloneConfig = write(base, 'rclone.conf', `[tgmedia]\ntype = alias\nremote = ${drive}\n`);
  // Shim that logs every rclone call the scripts make, then runs the real binary.
  const rcloneLog = path.join(base, 'rclone-calls.log');
  const shim = write(base, 'bin/rclone-shim', `#!/bin/sh\nprintf '%s\\n' "$*" >> '${rcloneLog}'\nexec ${process.env.RCLONE_BIN || 'rclone'} "$@"\n`);
  chmodSync(shim, 0o755);
  const env = { ...process.env, RCLONE_CONFIG: rcloneConfig, TGMEDIA_ROOT: repo, RCLONE_BIN: shim };
  return { base, repo, game, drive, env, rcloneLog };
}

export function runMedia(fixture, ...args) {
  const result = spawnSync(process.execPath, [SCRIPT, ...args], { env: fixture.env, encoding: 'utf8', cwd: fixture.repo });
  return { code: result.status, out: `${result.stdout}${result.stderr}`, stdout: result.stdout, stderr: result.stderr };
}

// Read-only Git helpers. The media scripts never commit, stage or check out.
import { spawnSync } from 'node:child_process';
import { parseLockHistory } from './lock.mjs';

function git(cwd, args, { allowFailure = false } = {}) {
  const result = spawnSync('git', args, { cwd, encoding: 'utf8', maxBuffer: 512 * 1024 * 1024 });
  if (result.error) throw new Error(`không chạy được git: ${result.error.message}`);
  if (result.status !== 0 && !allowFailure) {
    throw new Error(`git ${args.join(' ')} lỗi trong ${cwd}: ${(result.stderr || '').trim()}`);
  }
  return result;
}

/** Tracked files (index), POSIX paths relative to dir. .gitignore plays no part. */
export function trackedFiles(dir) {
  return git(dir, ['ls-files', '-z']).stdout.split('\0').filter(Boolean);
}

/**
 * Every md5 each path ever had in the committed lock (path relative to the lock).
 * Default: the history of HEAD (stale copies are judged against this branch).
 * all: every branch and ref in this clone, so a lock pushed from another local
 * branch is not mistaken for another machine's push.
 */
export function lockHistory(repoDir, lockFile, { all = false } = {}) {
  const args = ['log', ...(all ? ['--all'] : []), '-p', '--no-color', '--no-ext-diff', '--format=', '--', lockFile];
  const result = git(repoDir, args, { allowFailure: true });
  if (result.status !== 0) return new Map();
  return parseLockHistory(result.stdout);
}

export function isDetachedHead(repoDir) {
  const result = git(repoDir, ['symbolic-ref', '-q', 'HEAD'], { allowFailure: true });
  return result.status !== 0;
}

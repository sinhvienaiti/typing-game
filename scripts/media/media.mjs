#!/usr/bin/env node
// Media store on Google Drive: pnpm media:setup | status | push | pull | check.
// Node built-ins only; rclone runs through lib/rclone.mjs (argument arrays,
// allowlist, redacted output). Guide: docs/MEDIA_STORAGE.md.
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { parseArgs, USAGE, UsageError } from './lib/args.mjs';
import { HashCache } from './lib/hash.mjs';
import { LockError } from './lib/lock.mjs';
import { RcloneError, redact } from './lib/rclone.mjs';
import { loadConfig } from './lib/sets.mjs';
import { fmtBytes, MediaError } from './lib/ui.mjs';
import { check } from './commands/check.mjs';
import { pull } from './commands/pull.mjs';
import { push } from './commands/push.mjs';
import { setup } from './commands/setup.mjs';
import { status } from './commands/status.mjs';

const COMMANDS = { setup, status, push, pull, check };
const DEFAULT_ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '../..');

export function createContext({ root = DEFAULT_ROOT, env = process.env, out = process.stdout, err = process.stderr, stdin = process.stdin, now } = {}) {
  const config = loadConfig(root);
  const ctx = { root, env, out, err, stdin, now, config, game: null, present: {} };
  ctx.cache = new HashCache(path.join(root, config.hashCache));
  let warned = false;
  ctx.onSlowHash = (count, bytes) => {
    if (warned) return;
    warned = true;
    out.write(`Đang tính md5 ${count} file (${fmtBytes(bytes)}). Lần đầu mất 1–3 phút; các lần sau dùng cache.\n`);
  };
  return ctx;
}

export async function main(argv, options = {}) {
  const err = options.err ?? process.stderr;
  const out = options.out ?? process.stdout;
  let parsed;
  try {
    parsed = parseArgs(argv);
  } catch (error) {
    if (error instanceof UsageError) {
      err.write(`✗ ${error.message}\nCách dùng: node scripts/media/media.mjs --help (hoặc docs/MEDIA_STORAGE.md). Chưa làm gì.\n`);
      return 2;
    }
    throw error;
  }
  if (parsed.command === 'help' || parsed.options.help) {
    out.write(`${USAGE}\n`);
    return 0;
  }
  try {
    const ctx = createContext(options);
    return await COMMANDS[parsed.command](ctx, parsed.options);
  } catch (error) {
    if (error instanceof MediaError || error instanceof LockError || error instanceof RcloneError) {
      err.write(`✗ ${redact(error.message)}\n`);
      return 1;
    }
    err.write(`✗ ${redact(error?.stack ?? String(error))}\n`);
    return 1;
  }
}

if (process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url)) {
  const root = process.env.TGMEDIA_ROOT ? path.resolve(process.env.TGMEDIA_ROOT) : DEFAULT_ROOT;
  process.exitCode = await main(process.argv.slice(2), { root });
}

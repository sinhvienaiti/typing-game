// Output helpers: Vietnamese number format, prompts, run stamps.
import { createInterface } from 'node:readline/promises';

/** A refusal or a problem the owner can fix: printed without a stack trace, exit code 1. */
export class MediaError extends Error {}

export function fmtBytes(bytes) {
  const units = [['GB', 1e9], ['MB', 1e6], ['KB', 1e3]];
  for (const [unit, size] of units) {
    if (bytes >= size) return `${(bytes / size).toFixed(bytes >= size * 100 ? 0 : 1).replace('.', ',')} ${unit}`;
  }
  return `${bytes} B`;
}

export function fmtCount(count) {
  return String(count).replace(/\B(?=(\d{3})+(?!\d))/g, '.');
}

export function sumBytes(entries) {
  return entries.reduce((sum, entry) => sum + (entry?.size ?? 0), 0);
}

/** UTC stamp, so stamps sort the same on every machine: 2026-10-21_164500Z. */
export function runStamp(date = new Date()) {
  const pad = (value) => String(value).padStart(2, '0');
  return `${date.getUTCFullYear()}-${pad(date.getUTCMonth() + 1)}-${pad(date.getUTCDate())}_`
    + `${pad(date.getUTCHours())}${pad(date.getUTCMinutes())}${pad(date.getUTCSeconds())}Z`;
}

export function parseStamp(stamp) {
  const match = /^(\d{4})-(\d{2})-(\d{2})_(\d{2})(\d{2})(\d{2})Z$/.exec(stamp ?? '');
  if (!match) return null;
  const [, year, month, day, hours, minutes, seconds] = match.map(Number);
  return new Date(Date.UTC(year, month - 1, day, hours, minutes, seconds));
}

/**
 * Stamp for a push: later than every stamp already in _locks/, so the newest
 * copy on Drive is always the newest push even when this machine's clock is
 * behind (WSL after sleep). clockBehind: the clock gave an earlier stamp.
 */
export function nextStamp(date, maxStamp) {
  const stamp = runStamp(date);
  const newest = parseStamp(maxStamp);
  if (!newest || stamp > maxStamp) return { stamp, clockBehind: false };
  return { stamp: runStamp(new Date(newest.getTime() + 1000)), clockBehind: stamp < maxStamp };
}

export function printList(ctx, title, items, { limit = 12, indent = '    ' } = {}) {
  if (!items.length) return;
  ctx.out.write(`${title}\n`);
  for (const item of items.slice(0, limit)) ctx.out.write(`${indent}${item}\n`);
  if (items.length > limit) ctx.out.write(`${indent}… và ${fmtCount(items.length - limit)} file khác\n`);
}

/** y/N question. Returns null when there is no terminal to ask. */
export async function confirm(ctx, question) {
  if (!ctx.stdin?.isTTY) return null;
  const rl = createInterface({ input: ctx.stdin, output: ctx.out });
  try {
    const answer = await rl.question(`${question} [y/N] `);
    return /^(y|yes|c|có)$/i.test(answer.trim());
  } finally {
    rl.close();
  }
}

/** Reads one line without echoing it (client secret). */
export function readHidden(ctx, prompt) {
  const input = ctx.stdin;
  if (!input?.isTTY) return Promise.resolve(null);
  return new Promise((resolve) => {
    ctx.out.write(prompt);
    let value = '';
    input.setRawMode(true);
    input.resume();
    input.setEncoding('utf8');
    const done = (result) => {
      input.setRawMode(false);
      input.pause();
      input.removeListener('data', onData);
      ctx.out.write('\n');
      resolve(result);
    };
    const onData = (chunk) => {
      for (const char of chunk) {
        if (char === '\r' || char === '\n') return done(value);
        if (char === '\u0003') return done(null);
        if (char === '\u007f' || char === '\b') value = value.slice(0, -1);
        else if (char >= ' ') value += char;
      }
      return undefined;
    };
    input.on('data', onData);
  });
}

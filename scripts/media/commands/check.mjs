// pnpm media:check: local files against the locks, art-src/3d against
// SOURCES.json, runtime manifests against the files they name; --remote also
// checks Drive's md5s, duplicates and the size of _replaced/.
import { existsSync, statSync } from 'node:fs';
import path from 'node:path';
import { hashEntries } from '../lib/hash.mjs';
import { runtimeReferences } from '../lib/plan.mjs';
import { rcloneOk, runRclone } from '../lib/rclone.mjs';
import { driveAbout, ensureRemote, fetchLockCopies, listingFlags, PRIVATE_LOCK_COPY, remoteHas } from '../lib/remote.mjs';
import { presentGames, readSources, withGame } from '../lib/sets.mjs';
import { gameSetNames, lockForSet, loadState, selectedSets } from '../lib/state.mjs';
import { fmtBytes, fmtCount, printList } from '../lib/ui.mjs';
import { verifyOnDrive } from './push.mjs';
import { printSetDetails, setLine } from './status.mjs';

function sourcesReport(ctx, perSet) {
  const sources = readSources(ctx.root, ctx.game);
  const prefix = `${ctx.config.sets.originals.root}/3d/`;
  const problems = [];
  let matched = 0;
  for (const [file, item] of Object.entries(sources.files)) {
    const entry = perSet.local.get(`${prefix}${file}`);
    if (!entry) problems.push(`thiếu ${prefix}${file}`);
    else if (entry.md5 !== item.md5) problems.push(`khác md5: ${prefix}${file}`);
    else matched += 1;
  }
  for (const key of perSet.local.keys()) {
    if (key.startsWith(prefix) && key.endsWith('.glb') && !sources.files[key.slice(prefix.length)]) problems.push(`chưa có trong SOURCES.json: ${key}`);
  }
  return { total: Object.keys(sources.files).length, matched, problems };
}

async function manifestReport(ctx) {
  const gameRoot = path.join(ctx.root, ctx.game.dir);
  const references = runtimeReferences(gameRoot, ctx.game);
  const missing = [];
  const present = [];
  for (const reference of references) {
    const rel = `${ctx.game.dir}/${reference.key}`;
    const abs = path.join(ctx.root, rel);
    if (!existsSync(abs)) { missing.push(reference.key); continue; }
    const stats = statSync(abs);
    present.push({ ...reference, rel, abs, size: stats.size, mtimeMs: stats.mtimeMs, cacheKey: rel });
  }
  await hashEntries(present, ctx.cache, { onSlow: ctx.onSlowHash });
  const wrongVersion = present.filter((item) => item.version && !item.sha256.startsWith(item.version)).map((item) => `${item.key} (?v=${item.version})`);
  return { total: references.length, missing, wrongVersion };
}

/** states: [{ state, names }] for each game, then the private set. */
async function remoteReport(ctx, info, states, options) {
  let problems = 0;
  const hasPrivate = states.some(({ names }) => names.includes('private'));
  const copies = hasPrivate ? await fetchLockCopies(ctx, info, { latest: [PRIVATE_LOCK_COPY] }) : {};
  const groups = new Map();
  for (const { state, names } of states) {
    const privateLock = copies[PRIVATE_LOCK_COPY]?.at(-1)?.entries ?? state.privateLock;
    for (const name of names) {
      const definition = state.definitions[name];
      const lock = lockForSet(ctx.config, definition, state.gameLock, privateLock);
      const group = groups.get(definition.remoteBase) ?? new Map();
      for (const [key, md5] of lock) group.set(key, md5);
      groups.set(definition.remoteBase, group);
    }
  }
  ctx.out.write('\nTrên Google Drive:\n');
  for (const [remoteBase, entries] of groups) {
    if (!entries.size) { ctx.out.write(`  ${remoteBase}/: danh sách trống, bỏ qua.\n`); continue; }
    const report = await verifyOnDrive(ctx, info, remoteBase, entries);
    const bad = report.missingOnRemote.length + report.differ.length + report.error.length;
    problems += bad;
    ctx.out.write(`  ${remoteBase}/: khớp ${fmtCount(report.match.length)}/${fmtCount(entries.size)} · thiếu ${report.missingOnRemote.length} · khác ${report.differ.length} · lỗi ${report.error.length}\n`);
    printList(ctx, '    Thiếu trên Drive:', report.missingOnRemote, { indent: '      ' });
    printList(ctx, '    Khác md5:', report.differ, { indent: '      ' });
    printList(ctx, '    Lỗi đọc:', report.error, { indent: '      ' });

    if (!(await remoteHas(ctx, info, remoteBase))) continue;
    const listing = await runRclone(ctx, ['lsjson', '-R', '--files-only', '--no-mimetype', `${info.remote}:${remoteBase}`, ...listingFlags(info)]);
    if (listing.code !== 0) continue;
    const files = JSON.parse(listing.stdout || '[]');
    const counts = new Map();
    for (const file of files) counts.set(file.Path, (counts.get(file.Path) ?? 0) + 1);
    const duplicates = [...counts].filter(([, count]) => count > 1).map(([file, count]) => `${file} ×${count}`);
    const extras = [...counts.keys()].filter((file) => !entries.has(file));
    if (extras.length) ctx.out.write(`    Có ${fmtCount(extras.length)} file trên Drive không còn trong danh sách (đã bỏ hoặc đổi tên; giữ lại, không sao).\n`);
    if (duplicates.length) {
      problems += duplicates.length;
      printList(ctx, `    Trùng tên trên Drive (${duplicates.length}) → pnpm media:check --remote --fix-duplicates`, duplicates, { indent: '      ' });
      if (options['fix-duplicates']) {
        await rcloneOk(ctx, ['dedupe', '--dedupe-mode', 'skip', `${info.remote}:${remoteBase}`], { capture: false });
        ctx.out.write('    Đã xoá các bản trùng giống hệt (cùng md5). Bản khác nhau giữ nguyên; chạy lại để xem còn gì.\n');
      }
    }
  }
  if ((await remoteHas(ctx, info, '_replaced'))) {
    const size = await runRclone(ctx, ['size', `${info.remote}:_replaced`, '--json', ...listingFlags(info)]);
    if (size.code === 0) {
      const { count, bytes } = JSON.parse(size.stdout);
      ctx.out.write(`  _replaced/: ${fmtCount(count)} bản cũ, ${fmtBytes(bytes)} (không tự xoá; dọn tay trên Drive khi cần).\n`);
    }
  }
  const about = await driveAbout(ctx, info);
  if (about?.free !== undefined) ctx.out.write(`  Drive còn trống ${fmtBytes(about.free)}${about.total ? ` / ${fmtBytes(about.total)}` : ''}.\n`);
  return problems;
}

export async function check(ctx, options) {
  const names = selectedSets(options);
  const gameNames = gameSetNames(names);
  const states = [];
  let problems = 0;
  ctx.out.write('Kiểm tra trên máy này (so với danh sách md5):\n');
  for (const game of gameNames.length ? presentGames(ctx) : []) {
    const gctx = withGame(ctx, game);
    const state = await loadState(gctx, gameNames);
    states.push({ state, names: gameNames });
    ctx.out.write(`${game.dir} (${game.title ?? game.id}):\n`);
    for (const name of gameNames) {
      const perSet = state.perSet[name];
      ctx.out.write(`${setLine(name, perSet)}\n`);
      printSetDetails(ctx, perSet);
      problems += perSet.plan.missing.length + perSet.plan.changed.length + perSet.plan.stale.length;
    }
    if (gameNames.includes('originals')) {
      const report = sourcesReport(gctx, state.perSet.originals);
      ctx.out.write(`art-src/3d: ${report.matched}/${report.total} khớp md5 trong SOURCES.json.\n`);
      printList(ctx, '  Lệch SOURCES.json:', report.problems, { indent: '    ' });
      problems += report.problems.length;
    }
    if (gameNames.includes('runtime')) {
      const report = await manifestReport(gctx);
      ctx.out.write(`Manifest runtime: ${report.total} file được game gọi tới · thiếu ${report.missing.length} · sai ?v= ${report.wrongVersion.length}\n`);
      printList(ctx, '  Thiếu (game sẽ báo 404) → pnpm media:pull:', report.missing, { indent: '    ' });
      printList(ctx, '  Sai ?v= (file khác bản manifest ghi):', report.wrongVersion, { indent: '    ' });
      problems += report.missing.length + report.wrongVersion.length;
    }
  }
  if (names.includes('private')) {
    const state = await loadState(withGame(ctx, null), ['private']);
    states.push({ state, names: ['private'] });
    if (gameNames.length) ctx.out.write('Dùng chung:\n');
    const perSet = state.perSet.private;
    ctx.out.write(`${setLine('private', perSet)}\n`);
    printSetDetails(ctx, perSet);
    problems += perSet.plan.missing.length + perSet.plan.changed.length + perSet.plan.stale.length;
  }
  if (options.remote || options['fix-duplicates']) {
    const info = await ensureRemote(ctx);
    problems += await remoteReport(ctx, info, states, options);
  }
  ctx.out.write(problems ? `\n✗ Còn ${fmtCount(problems)} vấn đề.\n` : '\n✓ Khớp.\n');
  return problems ? 1 : 0;
}

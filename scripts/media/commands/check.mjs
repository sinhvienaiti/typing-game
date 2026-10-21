// pnpm media:check: local files against the locks, art-src/3d against
// SOURCES.json, runtime manifests against the files they name; --remote also
// checks Drive's md5s, duplicates and the size of _replaced/.
import { existsSync, statSync } from 'node:fs';
import path from 'node:path';
import { hashEntries } from '../lib/hash.mjs';
import { runtimeReferences } from '../lib/plan.mjs';
import { rcloneOk, runRclone } from '../lib/rclone.mjs';
import { driveAbout, ensureRemote, fetchLockCopies, listingFlags, LOCK_COPY_NAMES, remoteHas } from '../lib/remote.mjs';
import { readSources } from '../lib/sets.mjs';
import { lockForSet, loadState, selectedSets } from '../lib/state.mjs';
import { fmtBytes, fmtCount, printList } from '../lib/ui.mjs';
import { verifyOnDrive } from './push.mjs';
import { printSetDetails, setLine } from './status.mjs';

function sourcesReport(ctx, perSet) {
  const sources = readSources(ctx.root, ctx.config);
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
  const gameRoot = path.join(ctx.root, ctx.config.game.dir);
  const references = runtimeReferences(gameRoot, ctx.config.game);
  const missing = [];
  const present = [];
  for (const reference of references) {
    const rel = `${ctx.config.game.dir}/${reference.key}`;
    const abs = path.join(ctx.root, rel);
    if (!existsSync(abs)) { missing.push(reference.key); continue; }
    const stats = statSync(abs);
    present.push({ ...reference, rel, abs, size: stats.size, mtimeMs: stats.mtimeMs, cacheKey: rel });
  }
  await hashEntries(present, ctx.cache, { onSlow: ctx.onSlowHash });
  const wrongVersion = present.filter((item) => item.version && !item.sha256.startsWith(item.version)).map((item) => `${item.key} (?v=${item.version})`);
  return { total: references.length, missing, wrongVersion };
}

async function remoteReport(ctx, info, state, names, options) {
  let problems = 0;
  const copies = names.includes('private') ? await fetchLockCopies(ctx, info, { latest: [LOCK_COPY_NAMES.private] }) : {};
  const privateLock = copies[LOCK_COPY_NAMES.private]?.at(-1)?.entries ?? state.privateLock;
  const groups = new Map();
  for (const name of names) {
    const definition = state.definitions[name];
    const lock = lockForSet(ctx.config, definition, state.gameLock, privateLock);
    const group = groups.get(definition.remoteBase) ?? new Map();
    for (const [key, md5] of lock) group.set(key, md5);
    groups.set(definition.remoteBase, group);
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
  const state = await loadState(ctx, names);
  let problems = 0;
  ctx.out.write('Kiểm tra trên máy này (so với danh sách md5):\n');
  for (const name of names) {
    const perSet = state.perSet[name];
    ctx.out.write(`${setLine(name, perSet)}\n`);
    printSetDetails(ctx, perSet);
    problems += perSet.plan.missing.length + perSet.plan.changed.length + perSet.plan.stale.length;
  }
  if (names.includes('originals')) {
    const report = sourcesReport(ctx, state.perSet.originals);
    ctx.out.write(`art-src/3d: ${report.matched}/${report.total} khớp md5 trong SOURCES.json.\n`);
    printList(ctx, '  Lệch SOURCES.json:', report.problems, { indent: '    ' });
    problems += report.problems.length;
  }
  if (names.includes('runtime')) {
    const report = await manifestReport(ctx);
    ctx.out.write(`Manifest runtime: ${report.total} file được game gọi tới · thiếu ${report.missing.length} · sai ?v= ${report.wrongVersion.length}\n`);
    printList(ctx, '  Thiếu (game sẽ báo 404) → pnpm media:pull:', report.missing, { indent: '    ' });
    printList(ctx, '  Sai ?v= (file khác bản manifest ghi):', report.wrongVersion, { indent: '    ' });
    problems += report.missing.length + report.wrongVersion.length;
  }
  if (options.remote || options['fix-duplicates']) {
    const info = await ensureRemote(ctx);
    problems += await remoteReport(ctx, info, state, names, options);
  }
  ctx.out.write(problems ? `\n✗ Còn ${fmtCount(problems)} vấn đề.\n` : '\n✓ Khớp.\n');
  return problems ? 1 : 0;
}

// pnpm media:status: offline, per set: Thiếu / Mới / Khác against the locks.
import { hashEntries } from '../lib/hash.mjs';
import { readSources, scanSets } from '../lib/sets.mjs';
import { loadState, selectedSets } from '../lib/state.mjs';
import { fmtBytes, fmtCount, printList, sumBytes } from '../lib/ui.mjs';

const LABELS = { originals: 'originals', runtime: 'runtime  ', private: 'private  ' };

export function setLine(name, perSet) {
  const { local, plan } = perSet;
  const entries = [...local.values()];
  const differ = plan.changed.length + plan.stale.length;
  return `  ${LABELS[name]}  ${fmtCount(entries.length)} file, ${fmtBytes(sumBytes(entries))} · `
    + `Thiếu ${fmtCount(plan.missing.length)} · Mới ${fmtCount(plan.added.length + plan.renames.length)} · Khác ${fmtCount(differ)}`;
}

export function printSetDetails(ctx, perSet, { limit = 5 } = {}) {
  const { plan, definition } = perSet;
  const rel = (key) => (definition.lockBase ? `${definition.lockBase}/${key}` : key);
  printList(ctx, `    Khác, cũ hơn bản trên Drive (${plan.stale.length}) → pnpm media:pull --update-stale`, plan.stale.map(rel), { limit, indent: '      ' });
  printList(ctx, `    Khác, sửa ở máy này (${plan.changed.length}) → pnpm media:push`, plan.changed.map(rel), { limit, indent: '      ' });
  printList(ctx, `    Đổi tên (${plan.renames.length})`, plan.renames.map(({ from, to }) => `${rel(from)} → ${rel(to)}`), { limit, indent: '      ' });
  printList(ctx, `    Thiếu (${plan.missing.length}) → pnpm media:pull`, plan.missing.map(rel), { limit, indent: '      ' });
  printList(ctx, `    Đã bị bỏ khỏi danh sách (đổi tên hoặc --forget, có thể ở máy khác) (${plan.removedElsewhere.length}): không đẩy lại. `
    + `Không cần thì chuyển vào ${ctx.config.oldDir}/; cần thì pnpm media:push --readd <đường dẫn>`, plan.removedElsewhere.map(rel), { limit, indent: '      ' });
}

/**
 * 3D files under art-src outside art-src/3d whose md5 is not in SOURCES.json
 * and that are not Blender outputs: possible lost originals (old Windows machine).
 */
export async function findUnknownModels(ctx) {
  const { config } = ctx;
  const { sets } = await scanSets(ctx, ['originals']);
  const sources = readSources(ctx.root, config);
  const known = new Set(Object.values(sources.files).map((item) => item.md5));
  const candidates = sets.originals.filter((entry) => /\.(glb|gltf|blend|fbx|obj)$/i.test(entry.key)
    && !entry.key.startsWith(`${config.sets.originals.root}/3d/`));
  await hashEntries(candidates, ctx.cache, { onSlow: ctx.onSlowHash });
  return candidates.filter((entry) => !known.has(entry.md5));
}

export async function status(ctx, options) {
  const names = selectedSets(options);
  const state = await loadState(ctx, names);
  ctx.out.write('Kho media trên máy này (không cần mạng, so với danh sách md5)\n');
  if (!state.gameLockExists && names.some((name) => state.definitions[name].inGameLock)) {
    ctx.out.write(`  Chưa có ${ctx.config.game.dir}/${ctx.config.game.lock}: lần pnpm media:push đầu tiên sẽ tạo.\n`);
  }
  if (!state.privateLockExists && names.includes('private')) {
    ctx.out.write(`  Chưa có ${ctx.config.privateLock} trên máy này (danh sách riêng không vào Git, chỉ nằm ở đây và trên Drive). Lần đẩy đầu sẽ tạo; máy khác lấy bằng pnpm media:pull --only private.\n`);
  }
  let toPush = 0;
  let toPull = 0;
  let stale = 0;
  for (const name of names) {
    const perSet = state.perSet[name];
    ctx.out.write(`${setLine(name, perSet)}\n`);
    printSetDetails(ctx, perSet);
    toPush += perSet.plan.added.length + perSet.plan.changed.length + perSet.plan.renames.length;
    toPull += perSet.plan.missing.length;
    stale += perSet.plan.stale.length;
  }
  if (state.notes.rawKept.length) {
    printList(ctx, `  art-src/models/raw: ${state.notes.rawKept.length} file không trùng art-src/3d, được sao lưu cùng originals:`, state.notes.rawKept.map((entry) => entry.rel));
  }
  if (state.notes.unsafe.length) {
    printList(ctx, '  Bỏ qua tên file không dùng được trên Windows/Drive:', state.notes.unsafe);
  }
  if (toPush) ctx.out.write(`→ ${fmtCount(toPush)} file chưa lên Drive: pnpm media:push (xem trước: pnpm media:push --dry-run)\n`);
  if (toPull) ctx.out.write(`→ ${fmtCount(toPull)} file còn thiếu: pnpm media:pull\n`);
  if (stale) ctx.out.write(`→ ${fmtCount(stale)} file cũ hơn bản trên Drive: pnpm media:pull --update-stale\n`);
  if (!toPush && !toPull && !stale) ctx.out.write('→ Khớp danh sách md5.\n');

  if (options['find-unknown']) {
    const unknown = await findUnknownModels(ctx);
    if (!unknown.length) ctx.out.write('Mô hình 3D lạ ngoài art-src/3d: không có.\n');
    else {
      printList(ctx, `Mô hình 3D ngoài art-src/3d mà SOURCES.json không biết (${unknown.length}). Có thể là bản gốc duy nhất: chép vào art-src/3d rồi chạy node ${ctx.config.game.indexSourcesScript}.`,
        unknown.map((entry) => `${entry.rel}  (${fmtBytes(entry.size)})`), { limit: 50 });
    }
  }
  return 0;
}

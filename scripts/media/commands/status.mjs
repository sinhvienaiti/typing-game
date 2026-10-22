// pnpm media:status: offline, per game and set: Thiếu / Mới / Khác against the locks.
import { hashEntries } from '../lib/hash.mjs';
import { presentGames, readSources, scanSets, withGame } from '../lib/sets.mjs';
import { gameSetNames, loadState, selectedSets } from '../lib/state.mjs';
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
 * ctx.game: the game to look in.
 */
export async function findUnknownModels(ctx) {
  const { config } = ctx;
  const { sets } = await scanSets(ctx, ['originals']);
  const sources = readSources(ctx.root, ctx.game);
  const known = new Set(Object.values(sources.files).map((item) => item.md5));
  const candidates = sets.originals.filter((entry) => /\.(glb|gltf|blend|fbx|obj)$/i.test(entry.key)
    && !entry.key.startsWith(`${config.sets.originals.root}/3d/`));
  await hashEntries(candidates, ctx.cache, { onSlow: ctx.onSlowHash });
  return candidates.filter((entry) => !known.has(entry.md5));
}

function printNotes(ctx, notes) {
  if (notes.rawKept.length) {
    printList(ctx, `  art-src/models/raw: ${notes.rawKept.length} file không trùng art-src/3d, được sao lưu cùng originals:`, notes.rawKept.map((entry) => entry.rel));
  }
  if (notes.unsafe.length) {
    printList(ctx, '  Bỏ qua tên file không dùng được trên Windows/Drive:', notes.unsafe);
  }
}

export async function status(ctx, options) {
  const names = selectedSets(options);
  const gameNames = gameSetNames(names);
  ctx.out.write('Kho media trên máy này (không cần mạng, so với danh sách md5)\n');
  const games = gameNames.length || options['find-unknown'] ? presentGames(ctx) : [];
  let toPush = 0;
  let toPull = 0;
  let stale = 0;
  const count = (perSet) => {
    toPush += perSet.plan.added.length + perSet.plan.changed.length + perSet.plan.renames.length;
    toPull += perSet.plan.missing.length;
    stale += perSet.plan.stale.length;
  };
  if (gameNames.length) {
    for (const game of games) {
      const state = await loadState(withGame(ctx, game), gameNames);
      ctx.out.write(`${game.dir} (${game.title ?? game.id}):\n`);
      if (!state.gameLockExists) ctx.out.write(`  Chưa có ${game.dir}/${game.lock}: lần pnpm media:push đầu tiên sẽ tạo.\n`);
      for (const name of gameNames) {
        ctx.out.write(`${setLine(name, state.perSet[name])}\n`);
        printSetDetails(ctx, state.perSet[name]);
        count(state.perSet[name]);
      }
      printNotes(ctx, state.notes);
    }
  }
  if (names.includes('private')) {
    const state = await loadState(withGame(ctx, null), ['private']);
    if (gameNames.length) ctx.out.write('Dùng chung:\n');
    if (!state.privateLockExists) {
      ctx.out.write(`  Chưa có ${ctx.config.privateLock} trên máy này (danh sách riêng không vào Git, chỉ nằm ở đây và trên Drive). Lần đẩy đầu sẽ tạo; máy khác lấy bằng pnpm media:pull --only private.\n`);
    }
    ctx.out.write(`${setLine('private', state.perSet.private)}\n`);
    printSetDetails(ctx, state.perSet.private);
    count(state.perSet.private);
    printNotes(ctx, state.notes);
  }
  if (toPush) ctx.out.write(`→ ${fmtCount(toPush)} file chưa lên Drive: pnpm media:push (xem trước: pnpm media:push --dry-run)\n`);
  if (toPull) ctx.out.write(`→ ${fmtCount(toPull)} file còn thiếu: pnpm media:pull\n`);
  if (stale) ctx.out.write(`→ ${fmtCount(stale)} file cũ hơn bản trên Drive: pnpm media:pull --update-stale\n`);
  if (!toPush && !toPull && !stale) ctx.out.write('→ Khớp danh sách md5.\n');

  if (options['find-unknown']) {
    for (const game of games) {
      const unknown = await findUnknownModels(withGame(ctx, game));
      if (!unknown.length) ctx.out.write(`Mô hình 3D lạ ngoài art-src/3d (${game.dir}): không có.\n`);
      else {
        printList(ctx, `Mô hình 3D ngoài art-src/3d mà SOURCES.json không biết (${game.dir}, ${unknown.length}). Có thể là bản gốc duy nhất: chép vào art-src/3d rồi chạy node ${game.indexSourcesScript}.`,
          unknown.map((entry) => `${entry.rel}  (${fmtBytes(entry.size)})`), { limit: 50 });
      }
    }
  }
  return 0;
}

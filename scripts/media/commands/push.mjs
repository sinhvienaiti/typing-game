// pnpm media:push: copy new and changed files to Drive (rclone copy only),
// verify Drive's md5 against the new lock, and only then rewrite the locks.
import { rmSync, writeFileSync } from 'node:fs';
import path from 'node:path';
import { isDetachedHead, lockHistory } from '../lib/git.mjs';
import { formatLock, mergeHistory, sameEntries, writeFileAtomic, writeLockFile } from '../lib/lock.mjs';
import { isManifestOwned, quotaCheck, runtimeReferences } from '../lib/plan.mjs';
import { parseCombined, RcloneError, rcloneOk, runRclone, TRANSFER_FLAGS } from '../lib/rclone.mjs';
import {
  downloadLockCopies, driveAbout, driveFlags, ensureRemote, fetchLockCopies, listingFlags, listLockCopies, LOCK_COPY_NAMES,
  tempDir, uploadLockCopies,
} from '../lib/remote.mjs';
import { folderSummary, gameLockSetOf, readSources, toRel } from '../lib/sets.mjs';
import { loadState, readLocks, selectedSets } from '../lib/state.mjs';
import { confirm, fmtBytes, fmtCount, MediaError, nextStamp, printList, sumBytes } from '../lib/ui.mjs';

const SUMMARY_DEPTH = { originals: 2, runtime: 5, private: 4 };

function normalizePattern(value, flag) {
  const clean = value.replace(/\\/g, '/').replace(/^\.\//, '').replace(/\/+$/, '');
  if (!clean || clean.startsWith('/') || clean.split('/').includes('..')) throw new MediaError(`${flag}: đường dẫn không hợp lệ: ${value}`);
  return clean;
}

function patternMatches(pattern, rel, key) {
  return [rel, key].some((candidate) => candidate === pattern || candidate.startsWith(`${pattern}/`));
}

/** Local files under art-src/3d must be indexed in SOURCES.json with the same md5. */
function sourcesProblems(ctx, perSet) {
  const sources = readSources(ctx.root, ctx.config);
  const prefix = `${ctx.config.sets.originals.root}/3d/`;
  const problems = [];
  for (const [key, entry] of perSet.local) {
    if (!key.startsWith(prefix) || !key.endsWith('.glb')) continue;
    const listed = sources.files[key.slice(prefix.length)];
    if (!listed) problems.push(`${key}: chưa có trong SOURCES.json`);
    else if (listed.md5 !== entry.md5) problems.push(`${key}: md5 khác SOURCES.json`);
  }
  return problems;
}

/**
 * Compares Drive's game lock copies (newest first) with what this clone knows.
 * The walk stops at the first copy whose relevant lines are all known: older
 * copies are superseded, so a file replaced twice before one commit never
 * blocks. Stamps are never older than the copies a push saw (nextStamp), so
 * "newest" is the latest push even when a clock is behind.
 * - drift: lines no branch of this clone ever had and this machine's files do
 *   not match: another machine pushed and this clone has not pulled it.
 * - otherBranch: lines of the newest copy known only from another branch here.
 * - settled: a fully known copy was found (no need to read older copies).
 */
export function compareDriveCopies(copies, { knownHere, knownInClone, relevant = () => true }) {
  const drift = new Map();
  let settled = false;
  for (const { stamp, entries } of copies) {
    const unknown = [...entries].filter(([key, md5]) => relevant(key) && !knownInClone(key, md5));
    if (!unknown.length) { settled = true; break; }
    for (const [key] of unknown) if (!drift.has(key)) drift.set(key, stamp);
  }
  const newest = copies[0] ?? null;
  const otherBranch = newest
    ? [...newest.entries].filter(([key, md5]) => relevant(key) && knownInClone(key, md5) && !knownHere(key, md5)).map(([key]) => key)
    : [];
  return { drift: [...drift].map(([key, stamp]) => ({ key, stamp })), otherBranch, newest, settled };
}

/** Reads the game lock copies newest first, in growing batches, until compareDriveCopies settles. */
async function checkDriveLocks(ctx, info, listing, state, gameSets) {
  const name = LOCK_COPY_NAMES.game;
  const stamps = [...(listing.byName[name] ?? [])].reverse();
  const headHistory = state.perSet[gameSets[0]].history;
  const allHistory = lockHistory(path.join(ctx.root, ctx.config.game.dir), ctx.config.game.lock, { all: true });
  const setOf = (key) => gameLockSetOf(ctx.config, key);
  const knownHere = (key, md5) => state.gameLock.get(key) === md5 || Boolean(headHistory.get(key)?.has(md5))
    || state.perSet[setOf(key)]?.local.get(key)?.md5 === md5;
  const rules = {
    knownHere,
    knownInClone: (key, md5) => knownHere(key, md5) || Boolean(allHistory.get(key)?.has(md5)),
    relevant: (key) => gameSets.includes(setOf(key)),
  };
  const copies = [];
  let report = compareDriveCopies(copies, rules);
  for (let index = 0, batch = 1; index < stamps.length && !report.settled; batch *= 8) {
    const take = stamps.slice(index, index + batch);
    index += take.length;
    const downloaded = await downloadLockCopies(ctx, info, take.map((stamp) => ({ stamp, name })));
    for (const stamp of take) {
      const entries = downloaded.get(`${stamp}/${name}`);
      if (entries) copies.push({ stamp, entries });
    }
    report = compareDriveCopies(copies, rules);
  }
  return report;
}

function referencedRuntimeKeys(ctx) {
  return new Set(runtimeReferences(path.join(ctx.root, ctx.config.game.dir), ctx.config.game).map((ref) => ref.key));
}

/**
 * Decides, per set, what to upload and what the new lock is. Collects
 * problems (refusals) and questions (need y, or --yes for "replace") instead of acting.
 */
export function planPush(ctx, state, names, options) {
  const forget = (options.forget ?? []).map((value) => normalizePattern(value, '--forget'));
  const readd = (options.readd ?? []).map((value) => normalizePattern(value, '--readd'));
  const usedForget = new Set();
  const usedReadd = new Set();
  const newOnly = Boolean(options['new-only']);
  const referenced = names.includes('runtime') ? referencedRuntimeKeys(ctx) : new Set();
  const problems = [];
  const warnings = [];
  const sets = {};
  for (const name of names) {
    const perSet = state.perSet[name];
    const { plan, local, lock, definition } = perSet;
    const rel = (key) => toRel(definition, key);
    const forgetPattern = (key) => {
      const pattern = forget.find((item) => patternMatches(item, rel(key), key));
      if (pattern) usedForget.add(pattern);
      return Boolean(pattern);
    };
    const forgotten = [];
    const autoForgotten = [];
    const missing = [];
    for (const key of plan.missing) {
      if (forgetPattern(key)) forgotten.push(key);
      // --new-only never drops a line by itself: the other machine may simply not have pulled it.
      else if (!newOnly && name === 'runtime' && isManifestOwned(key, ctx.config.game) && !referenced.has(key)) autoForgotten.push(key);
      else missing.push(key);
    }
    const readded = [];
    const removedElsewhere = [];
    for (const key of plan.removedElsewhere) {
      const pattern = readd.find((item) => patternMatches(item, rel(key), key));
      if (pattern) { usedReadd.add(pattern); readded.push(key); }
      else removedElsewhere.push(key);
    }
    const set = {
      name, definition, lock, local,
      upload: [], replace: [], renames: [], forgotten, autoForgotten, missing, stale: plan.stale, readded, removedElsewhere,
      newLock: new Map(lock), questions: [],
    };
    sets[name] = set;
    for (const key of [...forgotten, ...autoForgotten]) set.newLock.delete(key);
    for (const key of [...plan.added, ...readded]) set.upload.push(key);
    if (removedElsewhere.length) {
      warnings.push(`${name}: ${removedElsewhere.length} file ở máy này đã bị bỏ khỏi danh sách (đổi tên hoặc --forget, có thể ở máy khác): không đẩy lại. `
        + `Không cần thì chuyển vào ${ctx.config.oldDir}/; cần thì --readd <đường dẫn>.`);
    }

    if (newOnly) {
      // Additive mode for a second machine: only files the lock has never seen.
      for (const { from, to } of plan.renames) {
        set.upload.push(to);
        if (forgetPattern(from)) { forgotten.push(from); set.newLock.delete(from); }
      }
      if (plan.changed.length || plan.stale.length) {
        warnings.push(`${name}: bỏ qua ${plan.changed.length + plan.stale.length} file khác danh sách (--new-only không thay file nào).`);
      }
      if (missing.length || plan.renames.length) {
        warnings.push(`${name}: ${missing.length + plan.renames.length} file trong danh sách không có ở máy này; danh sách giữ nguyên.`);
      }
      set.missing = [];
    } else {
      for (const key of plan.changed) {
        set.upload.push(key);
        set.replace.push(key);
      }
      const asked = [];
      for (const rename of plan.renames) {
        set.renames.push(rename);
        set.upload.push(rename.to);
        // --forget <old name> is the explicit, non-interactive yes for a rename.
        if (!forgetPattern(rename.from)) asked.push(rename);
      }
      if (plan.stale.length) {
        problems.push({
          title: `${name}: ${plan.stale.length} file ở máy này cũ hơn bản trên Drive (md5 trùng một bản cũ trong danh sách). Đẩy sẽ làm Drive quay về bản cũ.\n  Chạy pnpm media:pull --update-stale (bản ở máy này chuyển vào ${ctx.config.oldDir}/), rồi đẩy lại.`,
          items: plan.stale.map(rel),
        });
      }
      if (set.replace.length && definition.confirmReplace) {
        set.questions.push({
          kind: 'replace',
          title: `${name}: thay ${set.replace.length} file gốc trên Drive. Bản cũ chuyển vào _replaced/, không bị xoá.`,
          items: set.replace.map(rel),
        });
      }
      if (asked.length) {
        set.questions.push({
          kind: 'rename',
          title: `${name}: ${asked.length} file có vẻ đã đổi tên (cùng md5). Danh sách sẽ ghi tên mới, bỏ tên cũ; bản tên cũ trên Drive vẫn giữ.\n`
            + '  Nếu tên cũ chỉ là chưa tải về (máy khác vừa thêm): trả lời N, chạy pnpm media:pull.',
          items: asked.map(({ from, to }) => `${rel(from)} → ${rel(to)}`),
        });
      }
      if (missing.length) {
        set.questions.push({
          kind: 'missing',
          title: `${name}: máy này thiếu ${missing.length} file có trong danh sách.\n  Nếu chưa tải về: chạy pnpm media:pull trước.\n  Nếu đã xoá có chủ ý: y = bỏ khỏi danh sách (bản trên Drive vẫn giữ), hoặc dùng --forget <đường dẫn>.`,
          items: missing.map(rel),
        });
      }
    }
    for (const key of set.upload) set.newLock.set(key, local.get(key).md5);
    for (const { from } of set.renames) set.newLock.delete(from);
    if (name === 'originals') {
      const sourceProblems = sourcesProblems(ctx, perSet);
      if (sourceProblems.length) {
        problems.push({
          title: `originals: art-src/3d chưa khớp SOURCES.json. Chạy node ${ctx.config.game.indexSourcesScript} trước, rồi commit SOURCES.json.`,
          items: sourceProblems,
        });
      }
    }
  }
  for (const pattern of forget) {
    if (!usedForget.has(pattern)) problems.push({ title: `--forget ${pattern}: không khớp file nào đang thiếu, hay tên cũ của file đổi tên (file còn trên máy thì không bỏ được).`, items: [] });
  }
  for (const pattern of readd) {
    if (!usedReadd.has(pattern)) problems.push({ title: `--readd ${pattern}: không khớp file nào đã bị bỏ khỏi danh sách.`, items: [] });
  }
  return { sets, problems, warnings, newOnly };
}

function printProblems(ctx, problems) {
  for (const problem of problems) {
    ctx.err.write(`✗ ${problem.title}\n`);
    for (const item of problem.items.slice(0, 15)) ctx.err.write(`    ${item}\n`);
    if (problem.items.length > 15) ctx.err.write(`    … và ${problem.items.length - 15} file khác\n`);
  }
}

function printPlan(ctx, planned, state) {
  for (const set of Object.values(planned.sets)) {
    const uploadEntries = set.upload.map((key) => set.local.get(key));
    const backup = set.definition.backup ? 'bản bị thay vào _replaced/' : 'thay thẳng, không giữ bản cũ';
    ctx.out.write(`\n${set.name} → Drive ${set.definition.remoteBase}/ (${backup})\n`);
    ctx.out.write(`  Đẩy ${fmtCount(set.upload.length)} file (${fmtBytes(sumBytes(uploadEntries))}): mới ${set.upload.length - set.replace.length - set.renames.length}, `
      + `thay ${set.replace.length}, đổi tên ${set.renames.length}. Bỏ khỏi danh sách: ${set.forgotten.length + set.autoForgotten.length}.\n`);
    if (uploadEntries.length) {
      ctx.out.write('  Theo thư mục:\n');
      for (const group of folderSummary(uploadEntries, SUMMARY_DEPTH[set.name])) {
        ctx.out.write(`    ${group.folder.padEnd(48)} ${String(group.count).padStart(5)} file  ${fmtBytes(group.bytes).padStart(9)}\n`);
      }
    }
    if (set.autoForgotten.length) printList(ctx, '  Tự bỏ khỏi danh sách (manifest không còn dùng):', set.autoForgotten, { indent: '    ' });
    if (set.forgotten.length) printList(ctx, '  Bỏ khỏi danh sách (--forget):', set.forgotten, { indent: '    ' });
    if (set.readded.length) printList(ctx, '  Thêm lại vào danh sách (--readd):', set.readded, { indent: '    ' });
    if (set.removedElsewhere.length) {
      printList(ctx, '  Không đẩy: đã bị bỏ khỏi danh sách (đổi tên hoặc --forget):', set.removedElsewhere.map((key) => toRel(set.definition, key)), { indent: '    ', limit: 10 });
    }
    if (set.name === 'originals') {
      const kept = state.notes.modelsKept;
      ctx.out.write(`  art-src/models: ${kept.length} file được giữ (không phải bản Blender tạo lại được)${kept.length ? ':' : '.'}\n`);
      for (const entry of kept) ctx.out.write(`    ${entry.key}  (${fmtBytes(entry.size)})\n`);
      if (state.notes.rawDuplicates.length) {
        ctx.out.write(`  art-src/models/raw: ${state.notes.rawDuplicates.length} file trùng md5 với một file art-src/3d (có trong SOURCES.json, và có ở máy này hoặc trong danh sách), bỏ qua (${fmtBytes(sumBytes(state.notes.rawDuplicates))}).\n`);
      }
    }
    if (set.name === 'runtime' && state.notes.lostOriginals.length) {
      ctx.out.write(`  Kèm ${state.notes.lostOriginals.length} mô hình runtime đã mất bản gốc (vẫn có trong Git, ${fmtBytes(sumBytes(state.notes.lostOriginals))}).\n`);
    }
    for (const question of set.questions) {
      ctx.out.write(`  ? ${question.title}\n`);
      for (const item of question.items.slice(0, 10)) ctx.out.write(`      ${item}\n`);
      if (question.items.length > 10) ctx.out.write(`      … và ${question.items.length - 10} file khác\n`);
    }
  }
  for (const warning of planned.warnings) ctx.out.write(`! ${warning}\n`);
}

function writeDryRunList(ctx, planned) {
  const file = path.join(ctx.root, '.cache', 'media-push-dry-run.txt');
  const lines = [];
  for (const set of Object.values(planned.sets)) {
    const replace = new Set(set.replace);
    for (const key of set.upload) {
      const entry = set.local.get(key);
      lines.push(`${set.name}\t${replace.has(key) ? 'thay' : 'mới'}\t${entry.size}\t${entry.rel}`);
    }
  }
  writeFileAtomic(file, `${lines.join('\n')}\n`);
  return path.relative(ctx.root, file);
}

const NO_TTY_HINTS = {
  missing: 'chạy pnpm media:pull, hoặc --forget <đường dẫn>',
  rename: 'chạy trong terminal để trả lời y, hoặc --forget <đường dẫn cũ> nếu đúng là đổi tên (chưa tải về thì pnpm media:pull)',
  replace: 'chạy lại với --yes, hoặc trong terminal để trả lời',
};

/**
 * --yes only answers "replace an original" (Drive keeps the old copy in _replaced/).
 * A missing file or a rename drops a lock line, so it always needs a y or --forget.
 */
export async function askQuestions(ctx, planned, options) {
  for (const set of Object.values(planned.sets)) {
    for (const question of set.questions) {
      if (options.yes && question.kind === 'replace') continue;
      ctx.out.write(`\n? ${question.title}\n`);
      for (const item of question.items.slice(0, 20)) ctx.out.write(`    ${item}\n`);
      if (question.items.length > 20) ctx.out.write(`    … và ${question.items.length - 20} file khác\n`);
      const answer = await confirm(ctx, question.kind === 'missing' ? 'Bỏ các file này khỏi danh sách?' : 'Tiếp tục?');
      if (answer === null) {
        const hint = NO_TTY_HINTS[question.kind];
        throw new MediaError(`Cần xác nhận nhưng không có terminal để hỏi: ${hint}. Chưa đẩy gì.`);
      }
      if (!answer) throw new MediaError('Đã dừng theo lựa chọn của bạn. Chưa đẩy gì.');
      if (question.kind === 'missing') {
        for (const key of set.missing) { set.newLock.delete(key); set.forgotten.push(key); }
        set.missing = [];
      }
    }
  }
}

async function copyUp(ctx, info, set, keys, stamp) {
  const listDir = tempDir('media-push-');
  try {
    const listFile = path.join(listDir, 'files.txt');
    writeFileSync(listFile, `${keys.join('\n')}\n`);
    const localBase = path.join(ctx.root, set.definition.lockBase);
    // With --fast-list, Drive refuses to copy into a folder that does not exist yet.
    await rcloneOk(ctx, ['mkdir', `${info.remote}:${set.definition.remoteBase}`]);
    const args = ['copy', localBase, `${info.remote}:${set.definition.remoteBase}`, '--files-from-raw', listFile, '--checksum',
      ...TRANSFER_FLAGS, ...driveFlags(info)];
    if (set.definition.backup) args.push('--backup-dir', `${info.remote}:_replaced/${stamp}/${set.definition.remoteBase}`);
    const result = await runRclone(ctx, args, { capture: false });
    if (result.code !== 0) {
      throw new MediaError(`Đẩy ${set.name} chưa xong (rclone mã ${result.code}). Danh sách md5 chưa đổi. Chạy lại pnpm media:push: file đã lên được bỏ qua theo md5.`);
    }
  } finally {
    rmSync(listDir, { recursive: true, force: true });
  }
}

/** rclone check --one-way of a lock against Drive (Drive's own md5, no download). */
export async function verifyOnDrive(ctx, info, remoteBase, entries) {
  const dir = tempDir('media-check-');
  try {
    const sumFile = path.join(dir, 'lock.md5');
    writeFileSync(sumFile, formatLock(entries));
    const result = await runRclone(ctx, ['check', sumFile, `${info.remote}:${remoteBase}`, '--checkfile', 'md5', '--one-way',
      '--combined', '-', '--checkers', '8', ...listingFlags(info)]);
    const report = parseCombined(result.stdout);
    if (result.code !== 0 && !report.missingOnRemote.length && !report.differ.length && !report.error.length) {
      // The folder itself is missing: every entry is missing on Drive.
      if (result.code === 3) report.missingOnRemote.push(...entries.keys());
      else report.error.push(`(rclone check mã ${result.code})`);
    }
    return report;
  } finally {
    rmSync(dir, { recursive: true, force: true });
  }
}

/** Lock copies go to _locks/<stamp>/ before any local lock changes, so a failed copy changes nothing here. */
async function uploadCopies(ctx, info, stamp, copies) {
  try {
    await uploadLockCopies(ctx, info, stamp, copies);
  } catch (error) {
    if (!(error instanceof RcloneError)) throw error;
    throw new MediaError(`File đã lên Drive và khớp md5, nhưng chưa chép được danh sách md5 vào _locks/${stamp}/.\n${error.message}\n`
      + 'Danh sách md5 trên máy này chưa đổi. Chạy lại pnpm media:push: file đã lên được bỏ qua theo md5.');
  }
}

function newGameLock(ctx, state, planned) {
  const next = new Map();
  for (const [key, md5] of state.gameLock) {
    if (!planned.sets[gameLockSetOf(ctx.config, key)]) next.set(key, md5);
  }
  for (const set of Object.values(planned.sets)) {
    if (set.definition.inGameLock) for (const [key, md5] of set.newLock) next.set(key, md5);
  }
  return next;
}

export async function push(ctx, options) {
  const names = selectedSets(options);
  const dryRun = Boolean(options['dry-run']);
  const gameSets = names.filter((name) => name !== 'private');
  let info = null;
  let listing = null;
  let privateVersions = [];
  if (!dryRun) {
    info = await ensureRemote(ctx);
    listing = await listLockCopies(ctx, info);
    if (names.includes('private')) {
      privateVersions = (await fetchLockCopies(ctx, info, { all: [LOCK_COPY_NAMES.private] }, listing))[LOCK_COPY_NAMES.private];
    }
  }
  const privateHistory = new Map();
  for (const version of privateVersions) mergeHistory(privateHistory, version.entries);
  const state = await loadState(ctx, names, {
    privateLock: privateVersions.at(-1)?.entries,
    privateHistory,
  });
  if (names.includes('private')) mergeHistory(privateHistory, state.privateLock);

  const planned = planPush(ctx, state, names, options);
  let driveGameLock = null;
  if (!dryRun && gameSets.length) {
    const report = await checkDriveLocks(ctx, info, listing, state, gameSets);
    driveGameLock = report.newest?.entries ?? null;
    if (report.drift.length) {
      const stamps = [...new Set(report.drift.map((item) => item.stamp))];
      planned.problems.unshift({
        title: `Drive có danh sách md5 mới hơn từ máy khác (${report.drift.length} file, _locks/${stamps.at(0)}${stamps.length > 1 ? ` và ${stamps.length - 1} bản sao khác` : ''}).\n`
          + `  Chạy git pull trong ${ctx.config.game.dir} (và git submodule update ở repo cha), rồi pnpm media:pull, sau đó đẩy lại.\n`
          + '  Máy kia mất commit media.md5: xem docs/MEDIA_STORAGE.md, mục Khi gặp lỗi.',
        items: report.drift.map((item) => item.key),
      });
    }
    if (report.otherBranch.length) {
      planned.warnings.unshift(`Danh sách trên Drive có ${report.otherBranch.length} dòng chỉ có ở nhánh khác trong repo ${ctx.config.game.dir} của máy này, `
        + 'chưa có ở nhánh hiện tại. Vẫn đẩy tiếp; nhớ merge nhánh đó (không phải git pull) để media.md5 đủ dòng.');
    }
  }

  if (dryRun) {
    ctx.out.write('Đẩy thử (--dry-run): không kết nối Drive, không ghi gì lên Drive hay vào danh sách md5.\n');
    printPlan(ctx, planned, state);
    const all = Object.values(planned.sets).flatMap((set) => set.upload.map((key) => set.local.get(key)));
    const listFile = writeDryRunList(ctx, planned);
    ctx.out.write(`\nTổng: ${fmtCount(all.length)} file, ${fmtBytes(sumBytes(all))}. Danh sách đầy đủ: ${listFile}\n`);
    if (planned.problems.length) {
      ctx.out.write('\nKhi đẩy thật sẽ bị từ chối vì:\n');
      printProblems(ctx, planned.problems);
      return 1;
    }
    return 0;
  }

  if (planned.problems.length) {
    printProblems(ctx, planned.problems);
    ctx.err.write('Chưa đẩy gì.\n');
    return 1;
  }
  await askQuestions(ctx, planned, options);
  for (const warning of planned.warnings) ctx.out.write(`! ${warning}\n`);

  const sets = Object.values(planned.sets);
  const uploads = sets.flatMap((set) => set.upload.map((key) => set.local.get(key)));
  const nextGameLock = gameSets.length ? newGameLock(ctx, state, planned) : state.gameLock;
  const gameLockChanged = gameSets.length > 0 && (!state.gameLockExists ? nextGameLock.size > 0 : !sameEntries(nextGameLock, state.gameLock));
  const nextPrivateLock = names.includes('private') ? planned.sets.private.newLock : null;
  const privateChanged = Boolean(nextPrivateLock) && !sameEntries(nextPrivateLock, state.privateLock);
  const localPrivateStale = Boolean(nextPrivateLock) && !sameEntries(nextPrivateLock, readLocks(ctx).privateLock ?? new Map());
  const nothingNew = !uploads.length && !gameLockChanged && !privateChanged;
  if (gameLockChanged && isDetachedHead(path.join(ctx.root, ctx.config.game.dir))) {
    throw new MediaError(`${ctx.config.game.dir} đang ở detached HEAD: commit media.md5 sẽ dễ mất.\n  Chạy: git -C ${ctx.config.game.dir} switch <nhánh đang làm>  (hoặc switch -c <nhánh mới>), rồi đẩy lại. Chưa đẩy gì.`);
  }

  const uploadBytes = sumBytes(uploads);
  if (uploads.length) {
    const quota = quotaCheck(await driveAbout(ctx, info), uploadBytes, ctx.config.reserveBytes);
    if (quota.status === 'unknown') throw new MediaError('Không đọc được dung lượng trống của Drive (rclone about). Chưa đẩy gì.');
    if (quota.status === 'low') {
      throw new MediaError(`Drive còn trống ${fmtBytes(quota.free)}, cần ${fmtBytes(uploadBytes)} + ${fmtBytes(ctx.config.reserveBytes)} dự phòng `
        + '(Drive đầy thì Gmail ngừng nhận thư). Dọn _replaced/ hoặc thùng rác trên Drive, hay nâng gói, rồi đẩy lại. Chưa đẩy gì.');
    }
    if (quota.status === 'unlimited') {
      ctx.out.write('! Drive không báo hạn mức (tài khoản Workspace dùng chung dung lượng, hoặc không giới hạn): bỏ qua kiểm tra chỗ trống.\n');
    }
    ctx.out.write(`Đang đẩy ${fmtCount(uploads.length)} file (${fmtBytes(uploadBytes)}) lên Google Drive…\n`);
  }

  const { stamp, clockBehind } = nextStamp(ctx.now?.() ?? new Date(), listing.maxStamp);
  if (clockBehind) {
    ctx.out.write(`! Giờ máy này sớm hơn bản sao mới nhất trên Drive (_locks/${listing.maxStamp}): một trong hai máy lệch giờ. `
      + `Lần đẩy này dùng ${stamp}. WSL lệch giờ sau khi ngủ: chạy wsl --shutdown trong PowerShell rồi mở lại.\n`);
  }
  for (const set of sets) {
    if (set.upload.length) await copyUp(ctx, info, set, set.upload, stamp);
  }
  info.topFolders = null;

  // Verify every line of the new locks on Drive, per Drive folder. This also
  // runs when nothing is new, so a file lost on Drive is uploaded again.
  const groups = new Map();
  for (const set of sets) {
    const group = groups.get(set.definition.remoteBase) ?? { sets: [], entries: new Map() };
    group.sets.push(set);
    for (const [key, md5] of set.newLock) group.entries.set(key, md5);
    groups.set(set.definition.remoteBase, group);
  }
  let verified = 0;
  for (const [remoteBase, group] of groups) {
    if (!group.entries.size) continue;
    let report = await verifyOnDrive(ctx, info, remoteBase, group.entries);
    // Self-heal: a locked file missing on Drive is uploaded again when this machine has the same bytes.
    const healable = new Map();
    for (const key of report.missingOnRemote) {
      const set = group.sets.find((candidate) => candidate.local.get(key)?.md5 === group.entries.get(key));
      if (set) healable.set(set, [...(healable.get(set) ?? []), key]);
    }
    if (healable.size) {
      ctx.out.write(`Drive thiếu ${report.missingOnRemote.length} file đã có trong danh sách; đẩy lại…\n`);
      for (const [set, keys] of healable) await copyUp(ctx, info, set, keys, stamp);
      report = await verifyOnDrive(ctx, info, remoteBase, group.entries);
    }
    const bad = [...report.missingOnRemote.map((key) => `thiếu trên Drive: ${key}`), ...report.differ.map((key) => `Drive khác md5: ${key}`),
      ...report.error.map((key) => `lỗi đọc: ${key}`)];
    if (bad.length) {
      printProblems(ctx, [{ title: `Kiểm tra md5 trên Drive (${remoteBase}) chưa khớp. Danh sách md5 chưa đổi.`, items: bad }]);
      if (report.differ.length) ctx.err.write('  "Drive khác md5" thường là do máy khác vừa đẩy bản mới: git pull, pnpm media:pull, rồi đẩy lại.\n');
      return 1;
    }
    verified += report.match.length;
  }

  if (nothingNew) {
    if (localPrivateStale) writeLockFile(state.privateLockFile, nextPrivateLock);
    // The newest Drive copy must describe this lock: a copy that failed to upload
    // earlier, or a lock merged in Git, is copied now (every line was just verified).
    if (gameSets.length && state.gameLock.size && !sameEntries(state.gameLock, driveGameLock)) {
      await uploadCopies(ctx, info, stamp, { [LOCK_COPY_NAMES.game]: state.gameLock });
      ctx.out.write(`Bản sao danh sách mới nhất trên Drive khác ${ctx.config.game.dir}/${ctx.config.game.lock}: đã chép lại vào _locks/${stamp}/.\n`);
    }
    ctx.out.write(`Không có gì mới để đẩy. Drive khớp md5: ${fmtCount(verified)}/${fmtCount(verified)}.\n`);
    return 0;
  }

  await uploadCopies(ctx, info, stamp, {
    [LOCK_COPY_NAMES.game]: gameSets.length && nextGameLock.size ? nextGameLock : null,
    [LOCK_COPY_NAMES.private]: nextPrivateLock?.size ? nextPrivateLock : null,
  });
  if (gameLockChanged) writeLockFile(state.gameLockFile, nextGameLock);
  if (privateChanged || localPrivateStale) writeLockFile(state.privateLockFile, nextPrivateLock);

  ctx.out.write(`\n✓ Đã đẩy ${fmtCount(uploads.length)} file (${fmtBytes(uploadBytes)}). Drive khớp md5: ${fmtCount(verified)}/${fmtCount(verified)}. Bản sao danh sách: _locks/${stamp}/\n`);
  if (gameLockChanged) {
    const game = ctx.config.game.dir;
    ctx.out.write(`\nĐã cập nhật ${game}/${ctx.config.game.lock}. Commit cùng code (script không tự commit):\n`
      + `  git -C ${game} add ${ctx.config.game.lock}\n`
      + `  git -C ${game} commit -m "chore(media): cập nhật ${ctx.config.game.lock}"\n`
      + `  git add ${game}\n`
      + `  git commit -m "chore: cập nhật con trỏ ${path.posix.basename(game)} (${ctx.config.game.lock})"\n`);
  }
  if (privateChanged) ctx.out.write(`Danh sách riêng ${ctx.config.privateLock} chỉ nằm trên máy này và trên Drive (_locks/), không vào Git.\n`);
  return 0;
}


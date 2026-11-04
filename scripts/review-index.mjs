#!/usr/bin/env node
// Rebuilds INDEX.md of the owner's review folder (owner, 04/11/2026: one folder beside the source, so he can see what
// captures and review videos exist and when they may go). It lists every topic folder under captures/<game>/ and
// owner-review/<date>/<game>/ with its size, file count, newest file and the notes from its ABOUT.md.
//
//   node scripts/review-index.mjs [root]      (root defaults to the folder beside this repo: ../typing-game-review)
//
// ABOUT.md is a few "key: value" lines: purpose, made-by, doc, delete-when (values in Vietnamese).
import { existsSync, readdirSync, readFileSync, statSync, writeFileSync } from "node:fs";
import { dirname, join, relative, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const repo = resolve(dirname(fileURLToPath(import.meta.url)), "..");
const root = resolve(process.argv[2] ?? join(repo, "..", "typing-game-review"));
if (!existsSync(root)) {
  console.error(`review folder not found: ${root}`);
  process.exit(2);
}

/** Size in bytes, file count and newest mtime under `dir` (symlinks are not followed). */
function walk(dir) {
  let bytes = 0;
  let files = 0;
  let newest = 0;
  for (const e of readdirSync(dir, { withFileTypes: true })) {
    if (e.name === ".DS_Store" || e.name === "ABOUT.md") continue;
    const p = join(dir, e.name);
    if (e.isDirectory()) {
      const s = walk(p);
      bytes += s.bytes;
      files += s.files;
      newest = Math.max(newest, s.newest);
    } else if (e.isFile()) {
      const st = statSync(p);
      bytes += st.size;
      files += 1;
      newest = Math.max(newest, st.mtimeMs);
    }
  }
  return { bytes, files, newest };
}

function about(dir) {
  const p = join(dir, "ABOUT.md");
  const out = {};
  if (!existsSync(p)) return out;
  for (const line of readFileSync(p, "utf8").split("\n")) {
    const m = /^([a-z-]+):\s*(.+)$/.exec(line.trim());
    if (m) out[m[1]] = m[2].replace(/\|/g, "\\|");
  }
  return out;
}

const size = (b) => (b >= 1e9 ? `${(b / 1e9).toFixed(1)} GB` : b >= 1e6 ? `${(b / 1e6).toFixed(0)} MB` : `${Math.ceil(b / 1e3)} KB`);
const day = (ms) => (ms ? new Date(ms).toLocaleString("vi-VN", { dateStyle: "short", timeStyle: "short" }) : "");
const subdirs = (d) => (existsSync(d) ? readdirSync(d, { withFileTypes: true }).filter((e) => e.isDirectory()).map((e) => e.name).sort() : []);

function table(rows) {
  const head = "| Thư mục | Dung lượng | Số file | File mới nhất | Để làm gì | Ai tạo | Tài liệu | Xoá được khi |\n|---|---:|---:|---|---|---|---|---|";
  return [head, ...rows.map((r) => `| \`${r.path}\` | ${size(r.bytes)} | ${r.files} | ${day(r.newest)} | ${r.purpose ?? "_chưa ghi_"} | ${r["made-by"] ?? ""} | ${r.doc ?? ""} | ${r["delete-when"] ?? "_chưa ghi_"} |`)].join("\n");
}

function topics(base, depthDirs) {
  // depthDirs: how many levels sit between base and a topic (captures/<game>/<topic>: 1; owner-review/<date>/<game>/<topic>: 2)
  const rows = [];
  const visit = (dir, left) => {
    for (const name of subdirs(dir)) {
      const p = join(dir, name);
      if (left > 0) visit(p, left - 1);
      else rows.push({ path: relative(root, p), ...walk(p), ...about(p) });
    }
  };
  visit(base, depthDirs);
  return rows;
}

const reviewRows = topics(join(root, "owner-review"), 2).sort((a, b) => b.path.localeCompare(a.path));
const captureRows = topics(join(root, "captures"), 1);
const sum = (rows) => rows.reduce((s, r) => s + r.bytes, 0);

// Folders still inside the source tree's tmp/ (not moved here), one row per game with its biggest parts, so nothing is
// hidden from the owner. A tmp/shots that is a link into this folder is already counted above and is skipped.
const leftovers = [];
for (const g of subdirs(join(repo, "games"))) {
  const t = join(repo, "games", g, "tmp");
  if (!existsSync(t) || g.startsWith(".wt-")) continue;
  const parts = subdirs(t).map((name) => ({ name, ...walk(join(t, name)) })).sort((a, b) => b.bytes - a.bytes);
  const total = parts.reduce((s, p) => ({ bytes: s.bytes + p.bytes, files: s.files + p.files, newest: Math.max(s.newest, p.newest) }), { bytes: 0, files: 0, newest: 0 });
  if (total.bytes === 0) continue;
  const top = parts.slice(0, 4).map((p) => `${p.name} ${size(p.bytes)}`).join(", ");
  leftovers.push({ path: relative(repo, t), top, ...total });
}
leftovers.sort((a, b) => b.bytes - a.bytes);

const md = `# Mục lục thư mục review (tự sinh)

Sinh bởi \`node scripts/review-index.mjs\` (repo \`typing-game\`) lúc ${day(Date.now())}. Đừng sửa tay file này: sửa \`ABOUT.md\` trong từng thư mục rồi chạy lại lệnh.

**Tổng:** video và ảnh gửi anh ${size(sum(reviewRows))}; ảnh chụp làm việc ${size(sum(captureRows))}.

## 1. Gửi anh xem (\`owner-review/<ngày>/<game>/<việc>/\`)

${reviewRows.length ? table(reviewRows) : "_Chưa có._"}

## 2. Ảnh chụp, khung kiểm, clip làm việc của agent (\`captures/<game>/<việc>/\`)

${captureRows.length ? table(captureRows) : "_Chưa có._"}

## 3. Còn nằm trong \`tmp/\` của các game, chưa chuyển về đây

Các thư mục này không phải ảnh chụp đã gom (mã thử, máy chủ xem cố định, bot đo) hoặc do phiên khác tạo. Chưa chuyển để không làm hỏng việc đang chạy.

| Thư mục (tính từ repo) | Dung lượng | Số file | File mới nhất | Phần lớn nhất |
|---|---:|---:|---|---|
${leftovers.map((r) => `| \`${r.path}\` | ${size(r.bytes)} | ${r.files} | ${day(r.newest)} | ${r.top} |`).join("\n")}
`;

writeFileSync(join(root, "INDEX.md"), md);
console.log(`INDEX.md: ${reviewRows.length} review folders, ${captureRows.length} capture folders, ${leftovers.length} leftovers -> ${join(root, "INDEX.md")}`);

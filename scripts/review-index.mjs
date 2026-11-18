#!/usr/bin/env node
// Rebuilds INDEX.md of a project's review folder: one folder beside the source that holds every capture and every
// file sent to the owner, so he can see what exists and when it may go (owner, 04/11/2026). It lists each topic folder
// under captures/<area>/ and owner-review/<date>/<area>/ with its size, file count, newest file, the notes from its
// ABOUT.md and how many of the project's Markdown docs still name it, plus what still sits in the source's tmp folders.
//
//   node review-index.mjs [review-root]
//
// review-root defaults to "<source>-review" beside the source repo this script lives in (scripts/ or a skill folder:
// then pass the root). Settings come from <review-root>/review.config.json:
//   { "source": "/abs/path/to/repo",
//     "areas": { "<area>": ["<dir in repo>", "<old prefix in docs, e.g. tmp/shots/>"] },
//     "docDirs": ["docs", ".agents/skills"],          (each area's <dir>/docs is added)
//     "tmpParents": ["games"] }                        (scans <source>/tmp and <source>/<parent>/*/tmp)
// ABOUT.md is a few "key: value" lines: purpose, made-by, doc, delete-when.
// The same file lives in the user's skill ~/.claude/skills/review-folder/scripts/; keep the two identical.
import { existsSync, lstatSync, readdirSync, readFileSync, statSync, writeFileSync } from "node:fs";
import { basename, dirname, join, relative, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const here = dirname(fileURLToPath(import.meta.url));
const guessRepo = resolve(here, "..");
const root = resolve(process.argv[2] ?? join(guessRepo, "..", `${basename(guessRepo)}-review`));
if (!existsSync(root)) {
  console.error(`review folder not found: ${root} (pass it as the first argument)`);
  process.exit(2);
}
const cfgPath = join(root, "review.config.json");
const cfg = existsSync(cfgPath) ? JSON.parse(readFileSync(cfgPath, "utf8")) : {};
const repo = resolve(cfg.source ?? guessRepo);
const AREAS = cfg.areas ?? {};

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

/** Every Markdown doc of the project, read once, to count which capture folders docs still name. */
const docTexts = [];
function readDocs(dir, depth) {
  if (!existsSync(dir) || depth < 0) return;
  for (const e of readdirSync(dir, { withFileTypes: true })) {
    if (e.name === "node_modules" || e.name.startsWith(".wt-")) continue;
    const p = join(dir, e.name);
    if (e.isDirectory()) readDocs(p, depth - 1);
    else if (e.isFile() && e.name.endsWith(".md")) docTexts.push(readFileSync(p, "utf8"));
  }
}
for (const d of cfg.docDirs ?? ["docs"]) readDocs(join(repo, d), 6);
for (const [dir] of Object.values(AREAS)) readDocs(join(repo, dir, "docs"), 6);
const escape = (s) => s.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
/** Number of docs that name this capture folder, by its path here or its old path in the source. */
function linkedDocs(relPath) {
  const parts = relPath.split("/");
  if (parts[0] !== "captures" || parts.length < 3 || parts[2].startsWith("(")) return 0;
  const rest = parts.slice(2).join("/");
  const needles = [`captures/${parts[1]}/${rest}`];
  if (AREAS[parts[1]]) needles.push(`${AREAS[parts[1]][1]}${rest}`);
  const res = needles.map((n) => new RegExp(`${escape(n)}(?![\\w-])`));
  return docTexts.filter((t) => res.some((re) => re.test(t))).length;
}

const size = (b) => (b >= 1e9 ? `${(b / 1e9).toFixed(1)} GB` : b >= 1e6 ? `${(b / 1e6).toFixed(0)} MB` : `${Math.ceil(b / 1e3)} KB`);
const day = (ms) => (ms ? new Date(ms).toLocaleString("vi-VN", { dateStyle: "short", timeStyle: "short" }) : "");
const subdirs = (d) => (existsSync(d) ? readdirSync(d, { withFileTypes: true }).filter((e) => e.isDirectory()).map((e) => e.name).sort() : []);

function table(rows, withLinks) {
  const head = withLinks
    ? "| Thư mục | Dung lượng | Số file | File mới nhất | Để làm gì | Ai tạo | Tài liệu | Số tài liệu đang trỏ tới | Xoá được khi |\n|---|---:|---:|---|---|---|---|---:|---|"
    : "| Thư mục | Dung lượng | Số file | File mới nhất | Để làm gì | Ai tạo | Tài liệu | Xoá được khi |\n|---|---:|---:|---|---|---|---|---|";
  const cell = (r) => (withLinks ? ` ${linkedDocs(r.path)} |` : "");
  return [head, ...rows.map((r) => `| \`${r.path}\` | ${size(r.bytes)} | ${r.files} | ${day(r.newest)} | ${r.purpose ?? "_chưa ghi_"} | ${r["made-by"] ?? ""} | ${r.doc ?? ""} |${cell(r)} ${r["delete-when"] ?? "_chưa ghi_"} |`)].join("\n");
}

function topics(base, depthDirs) {
  // depthDirs: levels between base and a topic (captures/<area>/<topic>: 1; owner-review/<date>/<area>/<topic>: 2)
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
// Loose files straight inside captures/<area>/ (old one-off scripts and notes), one row per area.
for (const g of subdirs(join(root, "captures"))) {
  const dir = join(root, "captures", g);
  let bytes = 0;
  let files = 0;
  let newest = 0;
  for (const e of readdirSync(dir, { withFileTypes: true })) {
    if (!e.isFile() || [".DS_Store", "ABOUT.md", "README.md"].includes(e.name)) continue;
    const st = statSync(join(dir, e.name));
    bytes += st.size;
    files += 1;
    newest = Math.max(newest, st.mtimeMs);
  }
  if (files) captureRows.push({ path: `captures/${g}/(file lẻ)`, bytes, files, newest, purpose: "File lẻ ngay trong thư mục: script thử, ghi chú cũ", "delete-when": "xem từng file" });
}
const sum = (rows) => rows.reduce((s, r) => s + r.bytes, 0);
const areas = subdirs(join(root, "captures"));

// tmp folders still inside the source (not moved here), one row per folder with its biggest parts, so nothing is
// hidden from the owner. A tmp that is a link into this folder is already counted above and is skipped.
const tmpDirs = [join(repo, "tmp"), ...(cfg.tmpParents ?? []).flatMap((p) => subdirs(join(repo, p)).filter((g) => !g.startsWith(".wt-")).map((g) => join(repo, p, g, "tmp")))];
const leftovers = [];
for (const t of tmpDirs) {
  if (!existsSync(t) || lstatSync(t).isSymbolicLink()) continue;
  const parts = subdirs(t).map((name) => ({ name, ...walk(join(t, name)) })).sort((a, b) => b.bytes - a.bytes);
  const total = parts.reduce((s, p) => ({ bytes: s.bytes + p.bytes, files: s.files + p.files, newest: Math.max(s.newest, p.newest) }), { bytes: 0, files: 0, newest: 0 });
  if (total.bytes === 0) continue;
  leftovers.push({ path: relative(repo, t), top: parts.slice(0, 4).map((p) => `${p.name} ${size(p.bytes)}`).join(", "), ...total });
}
leftovers.sort((a, b) => b.bytes - a.bytes);

const md = `# Mục lục thư mục review (tự sinh)

Sinh bởi \`review-index.mjs\` lúc ${day(Date.now())}, cho source \`${repo}\`. Đừng sửa tay file này: sửa \`ABOUT.md\` trong từng thư mục rồi chạy lại.

**Tổng:** video và ảnh gửi anh ${size(sum(reviewRows))}; ảnh chụp làm việc ${size(sum(captureRows))}.

## 1. Gửi anh xem (\`owner-review/<ngày>/<khu>/<việc>/\`)

${reviewRows.length ? table(reviewRows, false) : "_Chưa có._"}

## 2. Ảnh chụp, khung kiểm, clip làm việc của agent (\`captures/<khu>/<việc>/\`)

Theo từng khu: ${areas.map((g) => `${g} ${size(sum(captureRows.filter((r) => r.path.startsWith(`captures/${g}/`))))}`).join(", ") || "chưa có"}. Cột "Số tài liệu đang trỏ tới" đếm các file \`.md\` của dự án còn nhắc tới thư mục đó. Nếu là 0, xoá thư mục không làm hỏng tài liệu nào.

${captureRows.length ? table(captureRows, true) : "_Chưa có._"}

## 3. Còn nằm trong \`tmp/\` của source, chưa chuyển về đây

${leftovers.length ? `Thường là mã thử, máy chủ xem cố định hay bot đo đang dùng, nên chưa chuyển.

| Thư mục (tính từ source) | Dung lượng | Số file | File mới nhất | Phần lớn nhất |
|---|---:|---:|---|---|
${leftovers.map((r) => `| \`${r.path}\` | ${size(r.bytes)} | ${r.files} | ${day(r.newest)} | ${r.top} |`).join("\n")}` : "_Không còn gì._"}
`;

writeFileSync(join(root, "INDEX.md"), md);
console.log(`INDEX.md: ${reviewRows.length} review folders, ${captureRows.length} capture rows, ${leftovers.length} tmp leftovers -> ${join(root, "INDEX.md")}`);

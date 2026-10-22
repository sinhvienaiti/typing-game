#!/usr/bin/env node
// Copies shared/game-kit modules into a game's src/kit with a sha256 manifest (docs/games/SPLIT_PLAN.md §4.2).
//   node scripts/sync-game-kit.mjs --target games/<id> [--allow-missing]
//   node scripts/sync-game-kit.mjs --check     every games/<id> with kit.config.json is current and untouched
//   node scripts/sync-game-kit.mjs --drift     kit vs its Space originals (informational, exit 0)
// --root <dir> runs against another checkout (tests).
import { execFileSync } from "node:child_process";
import { createHash } from "node:crypto";
import { existsSync, lstatSync, mkdirSync, readFileSync, readdirSync, realpathSync, rmdirSync, rmSync, writeFileSync } from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

export const KIT_DIR = "shared/game-kit";
export const MANIFEST_FILE = "kit-manifest.json";
export const VERIFY_FILE = "verify-kit.mjs";
export const README_FILE = "README.md";
const DEFAULT_ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");

// Never copied into a game: tests and their helpers stay in the kit.
const TEST_FILE = /(\.test|\.spec)\.[cm]?[jt]sx?$|\.test-helper\.[cm]?[jt]sx?$/;
const TEST_DIR = new Set(["__tests__", "__fixtures__", "test-fixtures", "node_modules"]);
const IGNORED = new Set([".DS_Store", "Thumbs.db"]);
// No media in Git, ever: the kit is code only.
const MEDIA = /\.(png|jpe?g|webp|avif|gif|bmp|ico|glb|gltf|bin|ktx2|hdr|exr|mp3|ogg|wav|m4a|flac|aac|mp4|mov|webm|mkv|ttf|otf|woff2?)$/i;
const CODE = /\.(ts|tsx|mts|cts|js|mjs|cjs)$/;

const toPosix = (value) => value.split(path.sep).join("/");
const sha256 = (bytes) => createHash("sha256").update(bytes).digest("hex");

export function isKitSourceFile(relative) {
  const parts = relative.split("/");
  if (parts.some((part) => TEST_DIR.has(part))) return false;
  const name = parts[parts.length - 1] ?? "";
  return !IGNORED.has(name) && !TEST_FILE.test(name);
}

function git(root, args) {
  try {
    return execFileSync("git", ["-C", root, ...args], { encoding: "buffer", stdio: ["ignore", "pipe", "ignore"] });
  } catch {
    return null;
  }
}

function listTree(dir, base = dir) {
  const out = [];
  if (!existsSync(dir)) return out;
  for (const entry of readdirSync(dir, { withFileTypes: true })) {
    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) {
      if (entry.name === "node_modules") continue;
      out.push(...listTree(full, base));
    } else if (entry.isFile()) {
      out.push(toPosix(path.relative(base, full)));
    }
  }
  return out.sort();
}

/** Reads kit files from the working tree, or from a parent commit when the game pins one. */
function kitSource(root, commit) {
  if (commit === undefined) {
    const kitRoot = path.join(root, KIT_DIR);
    return {
      label: "working tree",
      hasModule: (name) => existsSync(path.join(kitRoot, name, "index.ts")),
      list: (name) => listTree(path.join(kitRoot, name)).map((file) => name + "/" + file),
      read: (relative) => readFileSync(path.join(kitRoot, relative)),
      packageJson: () => JSON.parse(readFileSync(path.join(kitRoot, "package.json"), "utf8")),
    };
  }
  const listing = git(root, ["ls-tree", "-r", "--name-only", commit, "--", KIT_DIR + "/"]);
  if (listing === null) throw new Error(`pinned commit ${commit} is not in this repository`);
  const files = listing.toString("utf8").split("\n").filter(Boolean).map((file) => file.slice(KIT_DIR.length + 1));
  const read = (relative) => {
    const bytes = git(root, ["show", `${commit}:${KIT_DIR}/${relative}`]);
    if (bytes === null) throw new Error(`cannot read ${KIT_DIR}/${relative} at ${commit}`);
    return bytes;
  };
  return {
    label: "commit " + commit,
    hasModule: (name) => files.includes(name + "/index.ts"),
    list: (name) => files.filter((file) => file.startsWith(name + "/") && !file.includes("/node_modules/")).sort(),
    read,
    packageJson: () => JSON.parse(read("package.json").toString("utf8")),
  };
}

export function readKitConfig(gameDir) {
  const file = path.join(gameDir, "kit.config.json");
  if (!existsSync(file)) throw new Error(`${file} is missing`);
  const config = JSON.parse(readFileSync(file, "utf8"));
  const modules = config?.modules;
  if (!Array.isArray(modules) || modules.length === 0 || !modules.every((name) => typeof name === "string" && /^[a-z0-9][a-z0-9-]*$/.test(name))) {
    throw new Error(`${file}: "modules" must be a non-empty list of kit folder names`);
  }
  if (new Set(modules).size !== modules.length) throw new Error(`${file}: a module is listed twice`);
  let pinned = null;
  if (config.pinned !== undefined && config.pinned !== null) {
    const { commit, reason } = config.pinned;
    if (typeof commit !== "string" || !/^[0-9a-f]{7,40}$/.test(commit)) throw new Error(`${file}: pinned.commit must be a commit sha`);
    if (typeof reason !== "string" || reason.trim() === "") throw new Error(`${file}: pinned.reason is required`);
    pinned = { commit, reason: reason.trim() };
  }
  return { modules: [...modules], pinned };
}

// Relative import specifiers of a code file.
function relativeImports(text) {
  const found = new Set();
  // Comments may show example imports; drop them first.
  const code = text.replace(/\/\*[\s\S]*?\*\//g, "").replace(/^\s*\/\/.*$/gm, "");
  const pattern = /(?:\bfrom\s*|\bimport\s*\(?\s*)["'](\.{1,2}\/[^"']+)["']/g;
  for (const match of code.matchAll(pattern)) found.add(match[1]);
  return [...found];
}

function resolvesTo(files, fromFile, specifier) {
  const target = path.posix.normalize(path.posix.join(path.posix.dirname(fromFile), specifier));
  if (target.startsWith("..")) return { target, file: null };
  const candidates = [target, ...[".ts", ".tsx", ".mts", ".js", ".mjs"].map((ext) => target + ext), target + "/index.ts", target.replace(/\.js$/, ".ts")];
  return { target, file: candidates.find((candidate) => files.has(candidate)) ?? null };
}

const README_TEXT = `# src/kit — chép từ \`shared/game-kit\`

Thư mục này do \`node scripts/sync-game-kit.mjs --target games/<id>\` ở repo cha tạo ra.

- **Không sửa tay.** Mọi file được kiểm sha256 theo \`${MANIFEST_FILE}\`.
- \`node src/kit/${VERIFY_FILE}\` báo lỗi khi một file khác bản kê. Lệnh \`check\` của game chạy nó.
- Muốn đổi kit: sửa ở \`shared/game-kit\`, chạy \`pnpm kit:test\`, rồi \`pnpm kit:sync --target games/<id>\`.
- Chọn module trong \`kit.config.json\` của game.
`;

export const VERIFY_SOURCE = `#!/usr/bin/env node
// Generated by typing-game scripts/sync-game-kit.mjs; never edit. Fails when a src/kit file differs from ${MANIFEST_FILE}.
// Standalone on purpose: it works in a game repository cloned without its parent.
import { createHash } from "node:crypto";
import { readFileSync, readdirSync, realpathSync } from "node:fs";
import { dirname, join, relative, sep } from "node:path";
import { fileURLToPath } from "node:url";

const MANIFEST = "${MANIFEST_FILE}";
const IGNORED = new Set([".DS_Store", "Thumbs.db"]);

function listFiles(dir, base = dir) {
  const out = [];
  for (const entry of readdirSync(dir, { withFileTypes: true })) {
    const full = join(dir, entry.name);
    if (entry.isDirectory()) out.push(...listFiles(full, base));
    else if (!IGNORED.has(entry.name)) out.push(relative(base, full).split(sep).join("/"));
  }
  return out;
}

/** Problems found in a src/kit folder; empty when every file matches the manifest. */
export function verifyKit(kitDir = dirname(fileURLToPath(import.meta.url))) {
  let manifest;
  try {
    manifest = JSON.parse(readFileSync(join(kitDir, MANIFEST), "utf8"));
  } catch (error) {
    return ["cannot read " + MANIFEST + ": " + (error instanceof Error ? error.message : String(error))];
  }
  const expected = manifest !== null && typeof manifest.files === "object" ? manifest.files : {};
  const actual = new Set(listFiles(kitDir).filter((file) => file !== MANIFEST));
  const problems = [];
  for (const [file, hash] of Object.entries(expected)) {
    if (!actual.has(file)) problems.push("missing: " + file);
    else if (createHash("sha256").update(readFileSync(join(kitDir, file))).digest("hex") !== hash) problems.push("changed: " + file);
  }
  for (const file of actual) if (!Object.hasOwn(expected, file)) problems.push("not in manifest: " + file);
  return problems.sort();
}

function runAsScript() {
  try {
    return process.argv[1] !== undefined && realpathSync(process.argv[1]) === realpathSync(fileURLToPath(import.meta.url));
  } catch {
    return false;
  }
}

if (runAsScript()) {
  const kitDir = dirname(fileURLToPath(import.meta.url));
  const problems = verifyKit(kitDir);
  if (problems.length > 0) {
    console.error("src/kit differs from " + MANIFEST + " (never edit src/kit by hand; re-sync from the parent repo):");
    for (const problem of problems) console.error("  " + problem);
    process.exit(1);
  }
  const manifest = JSON.parse(readFileSync(join(kitDir, MANIFEST), "utf8"));
  console.log("src/kit OK: " + Object.keys(manifest.files).length + " files match " + MANIFEST + " (kit " + manifest.kitVersion + ", modules " + manifest.modules.join(", ") + ")");
}
`;

function parentState(root, pinned) {
  if (pinned !== null) {
    const full = git(root, ["rev-parse", "--verify", pinned.commit + "^{commit}"]);
    return { parentCommit: full === null ? pinned.commit : full.toString("utf8").trim(), parentDirty: false };
  }
  const last = git(root, ["log", "-1", "--format=%H", "--", KIT_DIR]);
  const status = git(root, ["status", "--porcelain", "--", KIT_DIR]);
  return {
    parentCommit: last === null || last.toString("utf8").trim() === "" ? null : last.toString("utf8").trim(),
    parentDirty: status === null ? null : status.toString("utf8").trim() !== "",
  };
}

/**
 * Everything src/kit should hold for a game: file bytes by path, and the manifest.
 * Throws on a missing module (unless allowMissing), a cross-module import the
 * config leaves out, or a media file in the kit.
 */
export function planKit({ root = DEFAULT_ROOT, gameDir, allowMissing = false }) {
  const config = readKitConfig(gameDir);
  const source = kitSource(root, config.pinned?.commit);
  const missing = config.modules.filter((name) => !source.hasModule(name));
  if (missing.length > 0 && !allowMissing) {
    throw new Error(`kit module(s) not found in ${KIT_DIR} (${source.label}): ${missing.join(", ")} (a module needs index.ts; --allow-missing syncs the rest)`);
  }
  const modules = config.modules.filter((name) => !missing.includes(name));
  const files = new Map();
  for (const name of modules) {
    for (const relative of source.list(name)) {
      if (!isKitSourceFile(relative)) continue;
      if (MEDIA.test(relative)) throw new Error(`${KIT_DIR}/${relative}: media never goes in the kit`);
      files.set(relative, source.read(relative));
    }
  }

  const problems = [];
  for (const [file, bytes] of files) {
    if (!CODE.test(file)) continue;
    for (const specifier of relativeImports(bytes.toString("utf8"))) {
      const { target, file: resolved } = resolvesTo(files, file, specifier);
      if (resolved !== null) continue;
      const needed = target.split("/")[0];
      if (target.startsWith("..")) problems.push(`${file} imports ${specifier}, outside the kit`);
      else if (missing.includes(needed)) console.warn(`warning: ${file} imports ${specifier}; module ${needed} is not in the kit yet`);
      else if (!config.modules.includes(needed)) problems.push(`${file} imports ${specifier}: add "${needed}" to kit.config.json modules`);
      else problems.push(`${file} imports ${specifier}, which does not exist`);
    }
  }
  if (problems.length > 0) throw new Error("kit imports do not resolve:\n  " + problems.join("\n  "));

  files.set(README_FILE, Buffer.from(README_TEXT));
  files.set(VERIFY_FILE, Buffer.from(VERIFY_SOURCE));
  const sorted = new Map([...files].sort(([a], [b]) => (a < b ? -1 : a > b ? 1 : 0)));
  const pkg = source.packageJson();
  const manifest = {
    schema: 1,
    kit: pkg.name ?? "@typing-game/game-kit",
    kitVersion: pkg.version ?? "0.0.0",
    ...parentState(root, config.pinned),
    pinned: config.pinned,
    modules,
    ...(missing.length > 0 ? { missingModules: missing } : {}),
    files: Object.fromEntries([...sorted].map(([file, bytes]) => [file, sha256(bytes)])),
  };
  return { config, files: sorted, manifest, missing };
}

function removeEmptyDirs(dir, keep) {
  if (!existsSync(dir)) return;
  for (const entry of readdirSync(dir, { withFileTypes: true })) {
    if (entry.isDirectory()) removeEmptyDirs(path.join(dir, entry.name), false);
  }
  if (!keep && readdirSync(dir).length === 0) rmdirSync(dir);
}

/** Writes src/kit for one game; returns what changed. */
export function syncGame({ root = DEFAULT_ROOT, target, allowMissing = false }) {
  const gameDir = path.resolve(root, target);
  const plan = planKit({ root, gameDir, allowMissing });
  const kitDir = path.join(gameDir, "src", "kit");
  if (existsSync(kitDir) && lstatSync(kitDir).isSymbolicLink()) throw new Error(`${kitDir} is a symlink; refusing to write`);
  mkdirSync(kitDir, { recursive: true });
  const written = [];
  const removed = [];
  for (const file of listTree(kitDir)) {
    if (file !== MANIFEST_FILE && !plan.files.has(file)) {
      rmSync(path.join(kitDir, file));
      removed.push(file);
    }
  }
  removeEmptyDirs(kitDir, true);
  for (const [file, bytes] of plan.files) {
    const out = path.join(kitDir, file);
    if (existsSync(out) && readFileSync(out).equals(bytes)) continue;
    mkdirSync(path.dirname(out), { recursive: true });
    writeFileSync(out, bytes);
    written.push(file);
  }
  const manifestText = JSON.stringify(plan.manifest, null, 2) + "\n";
  const manifestPath = path.join(kitDir, MANIFEST_FILE);
  if (!existsSync(manifestPath) || readFileSync(manifestPath, "utf8") !== manifestText) {
    writeFileSync(manifestPath, manifestText);
    written.push(MANIFEST_FILE);
  }
  return { gameDir, kitDir, written, removed, missing: plan.missing, manifest: plan.manifest };
}

/** Problems of one game's src/kit against the kit (or its pinned commit). */
export function checkGame({ root = DEFAULT_ROOT, gameDir }) {
  const problems = [];
  const kitDir = path.join(gameDir, "src", "kit");
  const manifestPath = path.join(kitDir, MANIFEST_FILE);
  if (!existsSync(manifestPath)) return [`src/kit/${MANIFEST_FILE} is missing; run pnpm kit:sync --target ${toPosix(path.relative(root, gameDir))}`];
  let manifest;
  try {
    manifest = JSON.parse(readFileSync(manifestPath, "utf8"));
  } catch (error) {
    return [`src/kit/${MANIFEST_FILE} is not JSON: ${error.message}`];
  }
  const recorded = manifest?.files ?? {};
  const actual = new Set(listTree(kitDir).filter((file) => file !== MANIFEST_FILE && !IGNORED.has(path.posix.basename(file))));
  // Hand edits: files against the game's own manifest.
  for (const [file, hash] of Object.entries(recorded)) {
    if (!actual.has(file)) problems.push(`missing: ${file}`);
    else if (sha256(readFileSync(path.join(kitDir, file))) !== hash) problems.push(`edited by hand: ${file}`);
  }
  for (const file of actual) if (!Object.hasOwn(recorded, file)) problems.push(`not in manifest: ${file}`);

  // Freshness: the manifest against the kit as it is now (or at the pinned commit).
  let plan;
  try {
    plan = planKit({ root, gameDir });
  } catch (error) {
    problems.push(`cannot plan the kit: ${error.message.split("\n")[0]}`);
    return problems;
  }
  const label = plan.config.pinned === null ? "the current kit" : `pinned commit ${plan.config.pinned.commit}`;
  if (JSON.stringify(manifest.modules) !== JSON.stringify(plan.manifest.modules)) {
    problems.push(`modules ${JSON.stringify(manifest.modules)} differ from kit.config.json ${JSON.stringify(plan.manifest.modules)}`);
  }
  if (JSON.stringify(manifest.pinned ?? null) !== JSON.stringify(plan.config.pinned)) problems.push("pinned setting differs from kit.config.json");
  const expected = plan.manifest.files;
  const stale = [];
  for (const [file, hash] of Object.entries(expected)) if (recorded[file] !== hash) stale.push(file);
  for (const file of Object.keys(recorded)) if (!Object.hasOwn(expected, file)) stale.push(file);
  if (stale.length > 0) problems.push(`out of date with ${label}: ${stale.slice(0, 8).join(", ")}${stale.length > 8 ? ` and ${stale.length - 8} more` : ""}`);
  return problems;
}

/** Game folders that use the kit (worktrees and other dot-folders are skipped). */
export function kitGames(root = DEFAULT_ROOT) {
  const gamesDir = path.join(root, "games");
  if (!existsSync(gamesDir)) return [];
  return readdirSync(gamesDir, { withFileTypes: true })
    .filter((entry) => entry.isDirectory() && !entry.name.startsWith(".") && existsSync(path.join(gamesDir, entry.name, "kit.config.json")))
    .map((entry) => path.join(gamesDir, entry.name))
    .sort();
}

export function checkAll(root = DEFAULT_ROOT) {
  return kitGames(root).map((gameDir) => ({ game: toPosix(path.relative(root, gameDir)), problems: checkGame({ root, gameDir }) }));
}

// ---- drift: kit files against the Space files they came from ----

/** The sources a kit file's "// Source:" header names: [{ repo, ref, path }] or "new". */
export function parseSourceHeader(text) {
  const line = text.split("\n").slice(0, 3).find((candidate) => candidate.startsWith("// Source:"));
  if (line === undefined) return null;
  const body = line.slice("// Source:".length).trim();
  if (/^new\b/i.test(body)) return "new";
  const head = body.replace(/\s*\([^)]*\)/g, "").split(";")[0].trim();
  const sources = [];
  let repo = null;
  let ref = null;
  for (const token of head.split(/\s*\+\s*|\s*,\s*/)) {
    const pinned = /^(games\/[a-z0-9-]+)@(\S+)\s+(\S+)/.exec(token);
    const direct = /^((?:games\/[a-z0-9-]+)|shared)\/(\S+)/.exec(token);
    if (pinned !== null) {
      [, repo, ref] = pinned;
      sources.push({ repo, ref, path: pinned[3] });
    } else if (direct !== null) {
      repo = direct[1];
      ref = null;
      sources.push({ repo, ref, path: direct[2] });
    } else if (repo !== null && /^\S+\.\w+$/.test(token)) {
      sources.push({ repo, ref, path: token });
    }
  }
  return sources;
}

function readOriginal(root, source) {
  const repoDir = path.join(root, source.repo);
  if (source.ref === null) {
    const file = path.join(repoDir, source.path);
    return existsSync(file) ? readFileSync(file, "utf8") : null;
  }
  for (const ref of [source.ref, "origin/" + source.ref]) {
    const bytes = git(repoDir, ["show", `${ref}:${source.path}`]);
    if (bytes !== null) return bytes.toString("utf8");
  }
  return null;
}

const lines = (text) => text.replace(/\r\n/g, "\n").split("\n").filter((line) => !line.startsWith("// Source:"));

/** Length of the longest common subsequence of two line lists. */
export function commonLines(a, b) {
  let previous = new Uint32Array(b.length + 1);
  let current = new Uint32Array(b.length + 1);
  for (let i = 1; i <= a.length; i += 1) {
    for (let j = 1; j <= b.length; j += 1) {
      current[j] = a[i - 1] === b[j - 1] ? previous[j - 1] + 1 : Math.max(previous[j], current[j - 1]);
    }
    [previous, current] = [current, previous];
  }
  return previous[b.length];
}

export function driftReport(root = DEFAULT_ROOT) {
  const kitRoot = path.join(root, KIT_DIR);
  const rows = [];
  const modules = existsSync(kitRoot)
    ? readdirSync(kitRoot, { withFileTypes: true }).filter((entry) => entry.isDirectory() && entry.name !== "node_modules" && !entry.name.startsWith(".")).map((entry) => entry.name).sort()
    : [];
  for (const name of modules) {
    for (const file of listTree(path.join(kitRoot, name))) {
      const relative = name + "/" + file;
      if (!isKitSourceFile(relative) || !CODE.test(relative)) continue;
      const text = readFileSync(path.join(kitRoot, relative), "utf8");
      const sources = parseSourceHeader(text);
      if (sources === null) {
        rows.push({ module: name, file: relative, source: "-", status: "kit only" });
        continue;
      }
      if (sources === "new") {
        rows.push({ module: name, file: relative, source: "-", status: "new" });
        continue;
      }
      for (const source of sources) {
        const label = source.ref === null ? source.repo + "/" + source.path : `${source.repo}@${source.ref} ${source.path}`;
        const original = readOriginal(root, source);
        if (original === null) {
          rows.push({ module: name, file: relative, source: label, status: "source missing" });
          continue;
        }
        const kitLines = lines(text);
        const sourceLines = lines(original);
        const common = commonLines(kitLines, sourceLines);
        const added = kitLines.length - common;
        const removed = sourceLines.length - common;
        const status = added === 0 && removed === 0 ? "same" : `changed +${added} -${removed}${sources.length > 1 ? " (one of " + sources.length + " sources)" : ""}`;
        rows.push({ module: name, file: relative, source: label, status });
      }
    }
  }
  return rows;
}

function printDrift(root) {
  const rows = driftReport(root);
  console.log("Kit drift against the Space originals (informational; log fixes in shared/game-kit/DRIFT.md)\n");
  const width = Math.max(4, ...rows.map((row) => row.file.length));
  for (const row of rows) console.log(`${row.file.padEnd(width)}  ${row.status.padEnd(18)}  ${row.source}`);
  const byModule = new Map();
  for (const row of rows) {
    const counts = byModule.get(row.module) ?? { same: 0, changed: 0, new: 0, missing: 0, unknown: 0 };
    if (row.status === "same") counts.same += 1;
    else if (row.status.startsWith("changed")) counts.changed += 1;
    else if (row.status === "new") counts.new += 1;
    else if (row.status === "source missing") counts.missing += 1;
    else counts.unknown += 1;
    byModule.set(row.module, counts);
  }
  console.log("\nSummary:");
  for (const [name, counts] of byModule) {
    console.log(`  ${name.padEnd(10)} same ${counts.same}, changed ${counts.changed}, new ${counts.new + counts.unknown}, source missing ${counts.missing}`);
  }
  const driftLog = path.join(root, KIT_DIR, "DRIFT.md");
  if (existsSync(driftLog)) {
    const entries = readFileSync(driftLog, "utf8").split("\n").filter((line) => /^\|\s*\d{1,4}[-/.]\d/.test(line)).length;
    console.log(`\nDRIFT.md: ${entries} logged fix(es).`);
  }
}

function usage() {
  return "Usage: node scripts/sync-game-kit.mjs (--target games/<id> [--allow-missing] | --check | --drift) [--root <dir>]";
}

export function main(argv) {
  let root = DEFAULT_ROOT;
  let target = null;
  let mode = null;
  let allowMissing = false;
  for (let index = 0; index < argv.length; index += 1) {
    const arg = argv[index];
    if (arg === "--target" || arg === "--root") {
      const value = argv[index + 1];
      if (value === undefined || value.startsWith("--")) throw new Error(usage());
      index += 1;
      if (arg === "--target") {
        target = value;
        mode = mode ?? "sync";
      } else root = path.resolve(value);
    } else if (arg === "--check" || arg === "--drift") {
      if (mode !== null && mode !== "sync") throw new Error(usage());
      mode = arg.slice(2);
    } else if (arg === "--allow-missing") allowMissing = true;
    else if (arg === "--") continue;
    else throw new Error(usage());
  }
  if (mode === "sync" && target !== null) {
    const result = syncGame({ root, target, allowMissing });
    const where = toPosix(path.relative(root, result.kitDir));
    console.log(`${where}: ${Object.keys(result.manifest.files).length} files from modules ${result.manifest.modules.join(", ")} (kit ${result.manifest.kitVersion}, parent commit ${result.manifest.parentCommit ?? "none"}${result.manifest.parentDirty ? ", uncommitted kit changes" : ""})`);
    console.log(`  written ${result.written.length}, removed ${result.removed.length}`);
    if (result.missing.length > 0) {
      console.warn(`  not synced (missing in the kit): ${result.missing.join(", ")}; kit:check fails until they are`);
    }
    return 0;
  }
  if (mode === "check") {
    const results = checkAll(root);
    if (results.length === 0) console.log("No game has kit.config.json.");
    let failed = 0;
    for (const { game, problems } of results) {
      if (problems.length === 0) {
        console.log(`${game}: OK`);
        continue;
      }
      failed += 1;
      console.error(`${game}: ${problems.length} problem(s)`);
      for (const problem of problems) console.error(`  ${problem}`);
    }
    return failed === 0 ? 0 : 1;
  }
  if (mode === "drift") {
    printDrift(root);
    return 0;
  }
  throw new Error(usage());
}

function runAsScript() {
  try {
    return process.argv[1] !== undefined && realpathSync(process.argv[1]) === realpathSync(fileURLToPath(import.meta.url));
  } catch {
    return false;
  }
}

if (runAsScript()) {
  try {
    process.exitCode = main(process.argv.slice(2));
  } catch (error) {
    console.error(error instanceof Error ? error.message : String(error));
    process.exitCode = 1;
  }
}

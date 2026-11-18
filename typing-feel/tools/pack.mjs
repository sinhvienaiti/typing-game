#!/usr/bin/env node
// feel:pack, phase G4 / step B6 of docs/games/TYPING_FEEL_SERVICE.md (§6.5, §8.1).
// Zips public/v1 (catalogue, health.json, every set folder) as
// typing-feel-v1-<revision>.zip for a machine without the feel host: the
// company Mac downloads it from Drive and Monkeytype's `pnpm feel:mirror`
// unpacks it into frontend/static/typing-feel/. Entries are "v1/...", so the
// mirror reads the Typing Feel URLs under /typing-feel/v1/.
//
// Refuses (exit 1, nothing written) when the §8.1 data rules that apply
// without Cloudflare fail:
//   - the catalogue lists no set;
//   - a catalogue row does not resolve (the kit's required fields, the
//     contract's path rules, a duplicate id), points at a missing file, or
//     its manifest is not a set manifest of that id (keys/sets/…/
//     keys-manifest.json) or its preview not an OGG;
//   - a file a set manifest names (files[].file, preview) is missing;
//   - a JSON does not parse, an OGG is empty or does not start with "OggS";
//   - "typing-game.local" appears anywhere in the pack (a path or any bytes,
//     in any case, or a JSON string with escapes);
//   - health.json is missing or names another revision than the catalogue.
// The sha256 against each folder's fp12 is the importer's rule, not repeated
// here. Decode, true peak, file budgets and _headers wait for the Cloudflare
// pack (§6.4). Dot files and *.tmp (an importer's leftovers) are left out;
// any other file type, and a symbolic link, is refused.
//
// The zip is deterministic (sorted entries, one fixed timestamp from the
// catalogue's publishedAt): JSON is deflated, OGG stored. Written to a temp
// name and renamed, so a half-written zip never carries the final name.
// Node built-ins only.
//
//   node tools/pack.mjs [--public <publicDir>] [--out <outDir>]
// Default out: <parent repo>/tmp/typing-feel-pack/ (Git ignores /tmp/).
import { createHash } from "node:crypto";
import { lstat, mkdir, readdir, readFile, rename, rm, writeFile } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { crc32, deflateRawSync } from "node:zlib";
import { CATALOGUE_FILE, DEFAULT_PUBLIC_DIR, loadContract, pathProblem, PACKAGE_ROOT } from "./import-staging.mjs";

export const DEFAULT_OUT_DIR = path.resolve(PACKAGE_ROOT, "..", "tmp", "typing-feel-pack");
export const LOCAL_HOST = "typing-game.local";
/** Host names ignore case (as check-pack's local-host rule does). */
const LOCAL_HOST_RE = /typing-game\.local/i;
const REVISION = /^[A-Za-z0-9][A-Za-z0-9._-]{0,63}$/;
const KINDS = new Set([".json", ".ogg"]);
const OGG_MAGIC = Buffer.from("OggS");

export class PackError extends Error {
  constructor(problems) {
    super(problems.join("\n"));
    this.problems = problems;
  }
}

/** Every file under `dir` as "a/b/c" (sorted), skipping dot entries and *.tmp; links are reported. */
async function listFiles(dir, problems) {
  const files = [];
  const skipped = [];
  const walk = async (rel) => {
    const entries = await readdir(path.join(dir, rel), { withFileTypes: true });
    for (const entry of entries) {
      const child = rel ? `${rel}/${entry.name}` : entry.name;
      if (entry.name.startsWith(".") || entry.name.endsWith(".tmp")) {
        skipped.push(child);
        continue;
      }
      if (entry.isSymbolicLink()) problems.push(`${child}: a symbolic link`);
      else if (entry.isDirectory()) await walk(child);
      else if (entry.isFile()) files.push(child);
      else problems.push(`${child}: not a regular file`);
    }
  };
  await walk("");
  files.sort((a, b) => (a < b ? -1 : a > b ? 1 : 0));
  return { files, skipped };
}

function parseJson(bytes, name, problems) {
  try {
    return JSON.parse(bytes.toString("utf8"));
  } catch {
    problems.push(`${name}: not JSON`);
    return undefined;
  }
}

const isObject = (value) => value !== null && typeof value === "object" && !Array.isArray(value);

/** "a/b/../c" never happens (pathProblem refuses it), so a plain join is the URL resolution. */
const joinRel = (folder, relative) => (folder ? `${folder}/${relative}` : relative);

/**
 * Reads and checks public/v1. Returns { revision, publishedAt, sets, files: [{ name, bytes }] }
 * or throws PackError with every problem found.
 */
export async function collect(publicDir = DEFAULT_PUBLIC_DIR, contract = loadContract()) {
  const v1 = path.join(publicDir, "v1");
  const problems = [];
  const info = await lstat(v1).catch(() => null);
  if (!info?.isDirectory()) throw new PackError([`${v1}: no v1 folder`]);
  const { files: names, skipped } = await listFiles(v1, problems);
  const bytes = new Map();
  for (const name of names) bytes.set(name, await readFile(path.join(v1, name)));
  const has = (name) => bytes.has(name);
  const idPattern = new RegExp(contract.id.pattern);
  const reserved = new Set(contract.id.reserved);

  const localHost = new Set();
  const flagLocalHost = (name) => {
    if (localHost.has(name)) return;
    localHost.add(name);
    problems.push(`${name}: contains "${LOCAL_HOST}"`);
  };
  for (const [name, data] of bytes) {
    const ext = path.extname(name).toLowerCase();
    if (!KINDS.has(ext)) problems.push(`${name}: not a .json or .ogg file`);
    // latin1 maps each byte to one character, so any byte string matches.
    if (LOCAL_HOST_RE.test(name) || LOCAL_HOST_RE.test(data.toString("latin1"))) flagLocalHost(name);
    if (ext === ".ogg") {
      if (data.length === 0) problems.push(`${name}: empty OGG`);
      else if (!data.subarray(0, 4).equals(OGG_MAGIC)) problems.push(`${name}: not an OGG stream (no "OggS")`);
    }
  }
  const json = new Map();
  for (const [name, data] of bytes) {
    if (!name.toLowerCase().endsWith(".json")) continue;
    const parsed = parseJson(data, name, problems);
    json.set(name, parsed);
    // A JSON string may spell the host with escapes ("\u0074yping-game.local").
    if (parsed !== undefined && LOCAL_HOST_RE.test(JSON.stringify(parsed))) flagLocalHost(name);
  }

  const catalogueName = `keys/${CATALOGUE_FILE}`;
  const catalogue = json.get(catalogueName);
  let revision;
  let sets = 0;
  if (!has(catalogueName)) problems.push(`${catalogueName}: missing`);
  else if (catalogue !== undefined && (!isObject(catalogue) || !Array.isArray(catalogue.profiles))) problems.push(`${catalogueName}: no profiles list`);
  else if (catalogue !== undefined) {
    if (catalogue.contract !== contract.contract) problems.push(`${catalogueName}: contract ${JSON.stringify(catalogue.contract)}, not ${contract.contract}`);
    if (typeof catalogue.revision !== "string" || !REVISION.test(catalogue.revision)) problems.push(`${catalogueName}: revision ${JSON.stringify(catalogue.revision)} is not a short file-name-safe id`);
    else revision = catalogue.revision;
    sets = catalogue.profiles.length;
    if (sets === 0) problems.push(`${catalogueName}: lists no set`);
    const ids = new Set();
    catalogue.profiles.forEach((row, index) => {
      const where = `${catalogueName} profiles[${index}]${isObject(row) && typeof row.id === "string" ? ` (${row.id})` : ""}`;
      if (!isObject(row)) {
        problems.push(`${where}: not an object`);
        return;
      }
      // The kit's required fields (audio.ts loadKeyboardCatalog): a row without them is silently dropped in game.
      if (typeof row.id !== "string" || !idPattern.test(row.id) || reserved.has(row.id)) problems.push(`${where}: id is not a valid set id`);
      else if (ids.has(row.id)) problems.push(`${where}: duplicate id`);
      else ids.add(row.id);
      if (typeof row.name !== "string" || !row.name.trim()) problems.push(`${where}: no name`);
      if (typeof row.order !== "number" || !Number.isFinite(row.order)) problems.push(`${where}: order is not a number`);
      for (const field of ["manifest", "preview"]) {
        const relative = row[field];
        const problem = typeof relative === "string" ? pathProblem(relative, contract) : "not a string";
        const target = problem ? undefined : joinRel("keys", relative);
        if (problem) problems.push(`${where}: ${field} does not resolve (${problem})`);
        else if (!has(target)) problems.push(`${where}: ${field} ${target} is missing`);
        else if (field === "preview" && path.extname(target).toLowerCase() !== ".ogg") problems.push(`${where}: preview ${target} is not an OGG`);
        else if (field === "manifest") {
          // The kit loads the set from this file: it must be a set manifest (its
          // files list is checked below with every other set manifest).
          const manifest = json.get(target);
          if (!target.startsWith("keys/sets/") || path.posix.basename(target) !== CATALOGUE_FILE) problems.push(`${where}: manifest ${target} is not a set manifest (keys/sets/…/${CATALOGUE_FILE})`);
          else if (isObject(manifest) && manifest.id !== undefined && manifest.id !== row.id) problems.push(`${where}: manifest ${target} is the set ${JSON.stringify(manifest.id)}`);
        }
      }
    });
  }

  // Every set manifest in the pack, listed in the catalogue or not (older fp12 folders).
  for (const [name, manifest] of json) {
    if (!name.startsWith("keys/sets/") || path.posix.basename(name) !== CATALOGUE_FILE || manifest === undefined) continue;
    const folder = path.posix.dirname(name);
    if (!isObject(manifest) || !Array.isArray(manifest.files)) {
      problems.push(`${name}: no files list`);
      continue;
    }
    let samples = 0;
    manifest.files.forEach((entry, index) => {
      const file = typeof entry === "string" ? entry : isObject(entry) ? entry.file : undefined;
      const problem = typeof file === "string" ? pathProblem(file, contract) : "not a string";
      if (problem) problems.push(`${name} files[${index}]: does not resolve (${problem})`);
      else if (!has(joinRel(folder, file))) problems.push(`${name} files[${index}]: ${folder}/${file} is missing`);
      else if (/^(key|space)-\d+\.ogg$/.test(file)) samples += 1;
    });
    if (samples === 0) problems.push(`${name}: names no key or space sample`);
    if (manifest.preview !== undefined) {
      const problem = typeof manifest.preview === "string" ? pathProblem(manifest.preview, contract) : "not a string";
      if (problem) problems.push(`${name} preview: does not resolve (${problem})`);
      else if (!has(joinRel(folder, manifest.preview))) problems.push(`${name} preview: ${folder}/${manifest.preview} is missing`);
    }
  }

  const health = json.get("health.json");
  if (!has("health.json")) problems.push("health.json: missing");
  else if (health !== undefined && (!isObject(health) || health.revision !== catalogue?.revision)) problems.push(`health.json: revision ${JSON.stringify(health?.revision)} is not the catalogue's ${JSON.stringify(catalogue?.revision)}`);

  if (problems.length > 0) throw new PackError(problems);
  const files = names.map((name) => ({ name: `v1/${name}`, bytes: bytes.get(name) }));
  return { revision, publishedAt: catalogue.publishedAt, sets, files, skipped };
}

/** MS-DOS date and time (UTC fields) of an ISO timestamp; 1980-01-01 when it is missing or earlier. */
function dosTime(iso) {
  const date = new Date(typeof iso === "string" ? iso : NaN);
  if (Number.isNaN(date.getTime()) || date.getUTCFullYear() < 1980) return { time: 0, day: (1 << 5) | 1 };
  return {
    time: (date.getUTCHours() << 11) | (date.getUTCMinutes() << 5) | Math.floor(date.getUTCSeconds() / 2),
    day: ((date.getUTCFullYear() - 1980) << 9) | ((date.getUTCMonth() + 1) << 5) | date.getUTCDate(),
  };
}

/** A plain zip (no zip64): UTF-8 names, Unix 0644 files, deflate for JSON, store for OGG. */
export function zipFiles(files, timestamp) {
  if (files.length > 0xfffe) throw new PackError([`${files.length} files: too many for a plain zip`]);
  const { time, day } = dosTime(timestamp);
  const locals = [];
  const central = [];
  let offset = 0;
  for (const { name, bytes } of files) {
    const nameBytes = Buffer.from(name, "utf8");
    const deflate = !name.toLowerCase().endsWith(".ogg");
    const body = deflate ? deflateRawSync(bytes, { level: 9 }) : bytes;
    const method = deflate ? 8 : 0;
    const crc = crc32(bytes);
    if (bytes.length >= 0xffffffff || offset >= 0xffffffff) throw new PackError([`${name}: too large for a plain zip`]);
    const local = Buffer.alloc(30);
    local.writeUInt32LE(0x04034b50, 0);
    local.writeUInt16LE(20, 4);
    local.writeUInt16LE(0x800, 6);
    local.writeUInt16LE(method, 8);
    local.writeUInt16LE(time, 10);
    local.writeUInt16LE(day, 12);
    local.writeUInt32LE(crc, 14);
    local.writeUInt32LE(body.length, 18);
    local.writeUInt32LE(bytes.length, 22);
    local.writeUInt16LE(nameBytes.length, 26);
    locals.push(local, nameBytes, body);
    const entry = Buffer.alloc(46);
    entry.writeUInt32LE(0x02014b50, 0);
    entry.writeUInt16LE((3 << 8) | 20, 4);
    entry.writeUInt16LE(20, 6);
    entry.writeUInt16LE(0x800, 8);
    entry.writeUInt16LE(method, 10);
    entry.writeUInt16LE(time, 12);
    entry.writeUInt16LE(day, 14);
    entry.writeUInt32LE(crc, 16);
    entry.writeUInt32LE(body.length, 20);
    entry.writeUInt32LE(bytes.length, 24);
    entry.writeUInt16LE(nameBytes.length, 28);
    entry.writeUInt32LE((0o100644 << 16) >>> 0, 38);
    entry.writeUInt32LE(offset, 42);
    central.push(entry, nameBytes);
    offset += 30 + nameBytes.length + body.length;
  }
  const centralBytes = Buffer.concat(central);
  if (offset + centralBytes.length >= 0xffffffff) throw new PackError(["the pack is too large for a plain zip"]);
  const end = Buffer.alloc(22);
  end.writeUInt32LE(0x06054b50, 0);
  end.writeUInt16LE(files.length, 8);
  end.writeUInt16LE(files.length, 10);
  end.writeUInt32LE(centralBytes.length, 12);
  end.writeUInt32LE(offset, 16);
  return Buffer.concat([...locals, centralBytes, end]);
}

/** Checks public/v1, then writes <outDir>/typing-feel-v1-<revision>.zip. */
export async function pack({ publicDir = DEFAULT_PUBLIC_DIR, outDir = DEFAULT_OUT_DIR } = {}) {
  const contract = loadContract();
  const found = await collect(path.resolve(publicDir), contract);
  const zip = zipFiles(found.files, found.publishedAt);
  const out = path.resolve(outDir);
  const file = path.join(out, `typing-feel-v${contract.contract}-${found.revision}.zip`);
  await mkdir(out, { recursive: true });
  const temp = `${file}.${process.pid}.tmp`;
  try {
    await writeFile(temp, zip);
    await rename(temp, file);
  } catch (error) {
    await rm(temp, { force: true });
    throw error;
  }
  const audio = found.files.filter(({ name }) => name.toLowerCase().endsWith(".ogg")).length;
  return {
    file,
    revision: found.revision,
    sets: found.sets,
    files: found.files.length,
    audio,
    bytes: found.files.reduce((sum, { bytes }) => sum + bytes.length, 0),
    zipBytes: zip.length,
    sha256: createHash("sha256").update(zip).digest("hex"),
    skipped: found.skipped,
  };
}

const USAGE = "Usage: pnpm feel:pack [--public <publicDir>] [--out <outDir>]";

export function parseArgs(argv) {
  const args = [...argv];
  if (args[0] === "--") args.shift();
  const options = {};
  const flags = { "--public": "publicDir", "--out": "outDir" };
  for (let index = 0; index < args.length; index += 1) {
    const arg = args[index];
    if (arg === "-h" || arg === "--help") return { help: true };
    if (!Object.hasOwn(flags, arg)) throw new PackError([`Unknown argument ${arg}. ${USAGE}`]);
    const value = args[index + 1];
    if (value === undefined || value.startsWith("--")) throw new PackError([`${arg} needs a value. ${USAGE}`]);
    if (Object.hasOwn(options, flags[arg])) throw new PackError([`${arg} given twice. ${USAGE}`]);
    options[flags[arg]] = value;
    index += 1;
  }
  return options;
}

export async function main(argv = process.argv.slice(2), { out = process.stdout, err = process.stderr } = {}) {
  let options;
  try {
    options = parseArgs(argv);
  } catch (error) {
    err.write(`${error.message}\n`);
    return 2;
  }
  if (options.help) {
    out.write(`${USAGE}\n`);
    return 0;
  }
  try {
    const result = await pack(options);
    out.write(`Typing Feel ${result.revision}: ${result.sets} sets, ${result.files} files (${result.audio} OGG, ${result.bytes} bytes) -> ${result.file}\n`);
    out.write(`  zip ${result.zipBytes} bytes, sha256 ${result.sha256}\n`);
    if (result.skipped.length > 0) out.write(`  left out: ${result.skipped.join(", ")}\n`);
    out.write("  company Mac: in games/monkeytype/frontend run `pnpm feel:mirror <zip>`, then start Monkeytype with TYPING_FEEL_URL=/typing-feel\n");
    return 0;
  } catch (error) {
    if (error instanceof PackError) {
      const shown = error.problems.slice(0, 40);
      err.write(`feel:pack refused (${error.problems.length} problem${error.problems.length === 1 ? "" : "s"}):\n${shown.map((line) => `  - ${line}`).join("\n")}\n`);
      if (error.problems.length > shown.length) err.write(`  … and ${error.problems.length - shown.length} more\n`);
      err.write("Nothing was written.\n");
      return 1;
    }
    throw error;
  }
}

if (process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url)) {
  process.exitCode = await main();
}

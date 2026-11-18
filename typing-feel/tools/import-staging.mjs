#!/usr/bin/env node
// Seed import, phase G1 / step B1 of docs/games/TYPING_FEEL_SERVICE.md (§3.5, §4).
// Reads the Audio Lab staging catalogue (typing-keys-firefly/catalogue-2) and
// writes public/v1/keys/: one immutable folder per set, sets/<id>/<fp12>/, with
// the OGG bytes copied unchanged (§3.9: never re-encode) and a trimmed set-1
// manifest, then the catalogue-3 and public/v1/health.json.
//
// Never overwrites: an existing set folder must match byte for byte (its set
// manifest apart from the name, which the fp12 leaves out so a rename keeps the
// URL), a published revision is never rewritten with other content, and a
// rerun on the same staging writes nothing. Node built-ins only.
//
//   node tools/import-staging.mjs <stagingDir> [--out <publicDir>] [--revision r1] [--default bright-clack]
import { createHash } from "node:crypto";
import { constants, readFileSync } from "node:fs";
import { copyFile, lstat, mkdir, readdir, readFile, rename, rm, writeFile } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

const HERE = path.dirname(fileURLToPath(import.meta.url));
export const PACKAGE_ROOT = path.resolve(HERE, "..");
export const CONTRACT_FILE = path.join(PACKAGE_ROOT, "contract/typing-feel.v1.json");
export const DEFAULT_PUBLIC_DIR = path.join(PACKAGE_ROOT, "public");

export const STAGING_CATALOGUE_SCHEMA = "typing-keys-firefly/catalogue-2";
export const STAGING_SET_SCHEMA = "typing-keys-firefly/2";
export const CATALOGUE_FILE = "keys-manifest.json";
export const SET_MANIFEST_FILE = "keys-manifest.json";
export const DEFAULT_REVISION = "r1";
export const DEFAULT_SET = "bright-clack";
export const LEGACY_LABEL = "legacy-218";

const REVISION = /^r[0-9]{1,6}$/;
const revisionNumber = (revision) => Number(revision.slice(1));
const INCOMING_PREFIX = ".incoming-";

export class ImportError extends Error {}

export function loadContract(file = CONTRACT_FILE) {
  return JSON.parse(readFileSync(file, "utf8"));
}

/** Same serialization as admin/media-assets-v2.mjs hashJson: sorted keys, 2-space indent, newline. */
export function canonicalJson(value) {
  const sort = (item) => {
    if (Array.isArray(item)) return item.map(sort);
    if (item !== null && typeof item === "object") return Object.fromEntries(Object.keys(item).sort().map((key) => [key, sort(item[key])]));
    return item;
  };
  return `${JSON.stringify(sort(value), null, 2)}\n`;
}

export function sha256(bytes) {
  return createHash("sha256").update(bytes).digest("hex");
}

/**
 * The seed fp12 (contract fingerprint.seed): the set-1 manifest without its
 * name, plus every audio file's name, size and sha256. A rename alone keeps the
 * folder; any other change (bytes, durations, licence, recipe) gets a new one.
 */
export function seedFingerprint(manifest, files) {
  const content = { ...manifest };
  delete content.name;
  const audio = files.map(({ file, bytes, sha256: hash }) => ({ bytes, file, sha256: hash })).sort((a, b) => (a.file < b.file ? -1 : a.file > b.file ? 1 : 0));
  return sha256(canonicalJson({ ...content, audio })).slice(0, 12);
}

/** Why a relative path breaks the kit resolver or the exporter's stricter segment rule, or null. */
export function pathProblem(relative, contract = loadContract()) {
  const rules = contract.paths;
  if (typeof relative !== "string" || relative === "") return "empty path";
  if (relative.startsWith("/")) return "leading /";
  for (const character of rules.forbiddenCharacters) if (relative.includes(character)) return `contains "${character}"`;
  const segment = new RegExp(rules.segmentPattern);
  for (const part of relative.split("/")) {
    if (rules.forbiddenSegments.includes(part)) return `"${part}" segment`;
    if (part === "") return "empty segment";
    if (!segment.test(part)) return `segment "${part}" does not match ${rules.segmentPattern}`;
  }
  return null;
}

function assertPath(relative, contract, where) {
  const problem = pathProblem(relative, contract);
  if (problem !== null) throw new ImportError(`${where}: path ${JSON.stringify(relative)} is refused (${problem}).`);
  return relative;
}

function assertId(id, contract, where, { set = false } = {}) {
  if (typeof id !== "string" || !new RegExp(contract.id.pattern).test(id)) {
    throw new ImportError(`${where}: id ${JSON.stringify(id)} does not match ${contract.id.pattern}.`);
  }
  // "off" is the kit's silent choice: a set with that id would never show in a game.
  if (set && (contract.id.reserved ?? []).includes(id)) {
    throw new ImportError(`${where}: id ${JSON.stringify(id)} is reserved (${(contract.id.reserved ?? []).join(", ")}); no set may use it.`);
  }
  return id;
}

/** "Bright Clack" -> "bright-clack". */
export function familyId(name) {
  return name.trim().toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/^-+|-+$/g, "");
}

function isoSeconds(now) {
  const date = now instanceof Date ? now : new Date(now ?? Date.now());
  if (Number.isNaN(date.getTime())) throw new ImportError(`Invalid time: ${String(now)}.`);
  return date.toISOString().replace(/\.\d{3}Z$/, "Z");
}

async function readJson(file, label) {
  let text;
  try { text = await readFile(file, "utf8"); } catch (error) {
    throw new ImportError(`${label}: ${error.code === "ENOENT" ? "not found" : error.message} (${file}).`);
  }
  try { return JSON.parse(text); } catch (error) {
    throw new ImportError(`${label}: not valid JSON (${error.message}).`);
  }
}

async function readOptional(file) {
  try { return await readFile(file); } catch (error) {
    if (error.code === "ENOENT") return null;
    throw error;
  }
}

async function regularFile(file, where) {
  let stats;
  try { stats = await lstat(file); } catch (error) {
    throw new ImportError(`${where}: ${error.code === "ENOENT" ? "file not found" : error.message} (${file}).`);
  }
  if (stats.isSymbolicLink() || !stats.isFile()) throw new ImportError(`${where}: not a regular file (${file}).`);
  return stats;
}

function inside(root, relative) {
  const full = path.resolve(root, ...relative.split("/"));
  const rel = path.relative(root, full);
  if (rel === "" || rel.startsWith("..") || path.isAbsolute(rel)) throw new ImportError(`Path leaves the staging folder: ${relative}.`);
  return full;
}

const SET_FILE = /^(key|space)-([0-9]{2,3})\.ogg$/;

function fileDuration(entry) {
  if (Number.isFinite(entry.durationMs)) return entry.durationMs;
  if (Number.isFinite(entry.metrics?.duration_ms)) return entry.metrics.duration_ms;
  return undefined;
}

/** Reads one staging set: its manifest, every audio file it lists (hashed), and its recipe. */
async function readStagingSet(stagingDir, row, contract, warnings) {
  const where = `set ${row.id}`;
  const manifestRel = assertPath(row.manifest, contract, `${where} manifest`);
  const previewRel = assertPath(row.preview, contract, `${where} preview`);
  if (path.posix.basename(manifestRel) !== SET_MANIFEST_FILE) throw new ImportError(`${where}: manifest must be named ${SET_MANIFEST_FILE} (${manifestRel}).`);
  const folderRel = path.posix.dirname(manifestRel);
  if (folderRel === "." || path.posix.dirname(previewRel) !== folderRel) {
    throw new ImportError(`${where}: manifest and preview must share one set folder (${manifestRel}, ${previewRel}).`);
  }
  const folder = inside(stagingDir, folderRel);
  const manifest = await readJson(inside(stagingDir, manifestRel), `${where} ${manifestRel}`);
  if (manifest?.schema !== STAGING_SET_SCHEMA) throw new ImportError(`${where}: ${manifestRel} schema is ${JSON.stringify(manifest?.schema)}, expected ${STAGING_SET_SCHEMA}.`);
  if (manifest.id !== undefined && manifest.id !== row.id) throw new ImportError(`${where}: ${manifestRel} names id ${JSON.stringify(manifest.id)}.`);
  if (typeof manifest.licence !== "string" || !manifest.licence.trim()) throw new ImportError(`${where}: ${manifestRel} has no licence.`);
  if (!Array.isArray(manifest.files)) throw new ImportError(`${where}: ${manifestRel} has no files list.`);

  const previewName = path.posix.basename(previewRel);
  if (!new RegExp(contract.set.previewPattern).test(previewName)) throw new ImportError(`${where}: preview ${previewRel} must match ${contract.set.previewPattern}.`);
  if (manifest.preview !== undefined && manifest.preview !== previewName) throw new ImportError(`${where}: ${manifestRel} preview ${JSON.stringify(manifest.preview)} differs from the catalogue (${previewName}).`);

  const seen = new Set([previewName]);
  const entries = [];
  for (const [index, entry] of manifest.files.entries()) {
    const at = `${where} ${manifestRel} files[${index}]`;
    if (entry === null || typeof entry !== "object") throw new ImportError(`${at}: not an object.`);
    assertPath(entry.file, contract, at);
    const match = SET_FILE.exec(entry.file);
    if (match === null) throw new ImportError(`${at}: file ${JSON.stringify(entry.file)} must match ${contract.set.file.filePattern}.`);
    if (entry.set !== match[1]) throw new ImportError(`${at}: set ${JSON.stringify(entry.set)} does not match ${entry.file}.`);
    if (seen.has(entry.file)) throw new ImportError(`${at}: ${entry.file} is listed twice.`);
    seen.add(entry.file);
    const duration = fileDuration(entry);
    if (duration === undefined || duration <= 0) throw new ImportError(`${at}: ${entry.file} has no positive duration (durationMs or metrics.duration_ms).`);
    entries.push({ file: entry.file, set: entry.set, number: Number(match[2]), durationMs: Math.max(1, Math.round(duration)) });
  }
  entries.sort((a, b) => (a.set === b.set ? a.number - b.number : a.set === "key" ? -1 : 1));
  const keys = entries.filter((entry) => entry.set === "key").length;
  const spaces = entries.length - keys;
  const minimum = contract.set.minimum;
  if (keys < minimum.key || spaces < minimum.space) {
    throw new ImportError(`${where}: ${keys} keys and ${spaces} spaces; at least ${minimum.key} keys and ${minimum.space} spaces are needed.`);
  }

  const audio = [];
  for (const name of [...entries.map((entry) => entry.file), previewName]) {
    const source = path.join(folder, name);
    const stats = await regularFile(source, `${where} ${folderRel}/${name}`);
    const bytes = await readFile(source);
    audio.push({ file: name, source, bytes: stats.size, sha256: sha256(bytes) });
  }
  // Audio on disk that the manifest does not list is reported, never copied.
  for (const name of (await readdir(folder)).sort()) {
    if (/\.(ogg|opus|mp3|wav|m4a|flac|webm|aac)$/i.test(name) && !seen.has(name)) warnings.push(`${where}: ${folderRel}/${name} is not listed in ${manifestRel}; not copied.`);
  }

  const ownerPick = row.ownerPick === true;
  const score = typeof row.score === "number" && Number.isFinite(row.score) ? row.score : null;
  // Seed rule: the owner's picks were made with natural processing; every other
  // staging row carries the ticket 218 machine score and is legacy-218.
  if (!ownerPick && score === null) throw new ImportError(`${where}: neither an owner pick nor a ticket 218 score; its recipe is unknown.`);
  return {
    folderRel,
    previewName,
    licence: manifest.licence.trim(),
    recipe: ownerPick ? "natural-v1" : "firefly-218",
    legacy: !ownerPick,
    ownerPick,
    score,
    files: entries.map(({ file, set, durationMs }) => ({ file, set, durationMs })),
    keys,
    spaces,
    audio,
  };
}

/** The set-1 text: one file per line, so the tracked copy stays readable. */
export function setManifestText(manifest) {
  const head = ["schema", "id", "name", "licence", "recipe"].map((key) => `  ${JSON.stringify(key)}: ${JSON.stringify(manifest[key])},`);
  const files = manifest.files.map((entry) => `    ${JSON.stringify({ file: entry.file, set: entry.set, durationMs: entry.durationMs })}`);
  return `{\n${head.join("\n")}\n  "files": [\n${files.join(",\n")}\n  ],\n  "preview": ${JSON.stringify(manifest.preview)}\n}\n`;
}

/** Lists a folder's files (names) or null when it does not exist. */
async function listFolder(folder) {
  try {
    const entries = await readdir(folder, { withFileTypes: true });
    return entries.map((entry) => ({ name: entry.name, file: entry.isFile() && !entry.isSymbolicLink() }));
  } catch (error) {
    if (error.code === "ENOENT") return null;
    throw error;
  }
}

/**
 * Differences between an existing set folder and what the import would write.
 * Audio must match byte for byte; the set manifest too, apart from the name it
 * was written with (the fp12 leaves the name out, so a rename keeps the folder).
 * Returns { problems, heldName }.
 */
async function folderDifferences(folder, set) {
  const listed = await listFolder(folder);
  const problems = [];
  const regular = new Set();
  const audio = new Map(set.audio.map((item) => [item.file, item.sha256]));
  for (const entry of listed) {
    if (entry.name !== SET_MANIFEST_FILE && !audio.has(entry.name)) problems.push(`${entry.name} is not part of this set`);
    else if (!entry.file) problems.push(`${entry.name} is not a regular file`);
    else regular.add(entry.name);
  }
  for (const [name, hash] of audio) {
    if (!regular.has(name)) {
      if (!listed.some((entry) => entry.name === name)) problems.push(`${name} is missing`);
      continue;
    }
    const bytes = await readFile(path.join(folder, name));
    if (sha256(bytes) !== hash) problems.push(`${name} differs (sha256 ${sha256(bytes).slice(0, 12)}…, expected ${hash.slice(0, 12)}…)`);
  }
  let heldName = null;
  if (!regular.has(SET_MANIFEST_FILE)) {
    if (!listed.some((entry) => entry.name === SET_MANIFEST_FILE)) problems.push(`${SET_MANIFEST_FILE} is missing`);
  } else {
    const bytes = await readFile(path.join(folder, SET_MANIFEST_FILE));
    let held = null;
    try { held = JSON.parse(bytes.toString("utf8")); } catch { /* Not JSON: reported as a difference below. */ }
    if (typeof held?.name === "string") heldName = held.name;
    const expected = heldName === null ? null : Buffer.from(setManifestText({ ...set.manifest, name: heldName }));
    if (expected === null || !bytes.equals(expected)) {
      problems.push(`${SET_MANIFEST_FILE} differs (sha256 ${sha256(bytes).slice(0, 12)}…, expected ${sha256(set.manifestText).slice(0, 12)}…)`);
      heldName = null;
    }
  }
  return { problems, heldName };
}

async function writeAtomic(file, text) {
  const temporary = `${file}.${process.pid}.tmp`;
  await writeFile(temporary, text, { flag: "wx" });
  try { await rename(temporary, file); } catch (error) {
    await rm(temporary, { force: true });
    throw error;
  }
}

/** Copies one set into sets/<id>/<fp12>/ through a hidden folder, so a crash never leaves a half set at its URL. */
async function writeSetFolder(setsDir, set, manifestText) {
  const parent = path.join(setsDir, set.id);
  await mkdir(parent, { recursive: true });
  const incoming = path.join(parent, `${INCOMING_PREFIX}${set.fp12}-${process.pid}`);
  await rm(incoming, { recursive: true, force: true });
  await mkdir(incoming);
  try {
    for (const item of set.audio) {
      const target = path.join(incoming, item.file);
      await copyFile(item.source, target, constants.COPYFILE_EXCL);
      const copied = await readFile(target);
      if (copied.length !== item.bytes || sha256(copied) !== item.sha256) throw new ImportError(`set ${set.id}: copy of ${item.file} does not match its staging bytes.`);
    }
    await writeFile(path.join(incoming, SET_MANIFEST_FILE), manifestText, { flag: "wx" });
    await rename(incoming, path.join(parent, set.fp12));
  } catch (error) {
    await rm(incoming, { recursive: true, force: true });
    throw error;
  }
}

function catalogueBody(catalogue) {
  const { publishedAt, ...rest } = catalogue;
  return canonicalJson(rest);
}

/**
 * Imports `stagingDir` into `publicDir` (default typing-feel/public).
 * Returns a summary; throws ImportError (nothing written) on any problem found before writing.
 */
export async function importStaging({
  stagingDir,
  publicDir = DEFAULT_PUBLIC_DIR,
  revision = DEFAULT_REVISION,
  defaultSet = DEFAULT_SET,
  now = Date.now(),
  contract = loadContract(),
} = {}) {
  if (typeof stagingDir !== "string" || !stagingDir) throw new ImportError("A staging folder is required.");
  const staging = path.resolve(stagingDir);
  const out = path.resolve(publicDir);
  if (!REVISION.test(revision)) throw new ImportError(`Revision ${JSON.stringify(revision)} must look like r1, r2, …`);
  const stamp = isoSeconds(now);
  const warnings = [];

  // 1. Read and check the whole staging catalogue before touching anything.
  const source = await readJson(path.join(staging, CATALOGUE_FILE), `staging ${CATALOGUE_FILE}`);
  if (source?.schema !== STAGING_CATALOGUE_SCHEMA) throw new ImportError(`staging ${CATALOGUE_FILE}: schema is ${JSON.stringify(source?.schema)}, expected ${STAGING_CATALOGUE_SCHEMA}.`);
  if (!Array.isArray(source.profiles) || source.profiles.length === 0) throw new ImportError(`staging ${CATALOGUE_FILE}: no profiles.`);
  const rows = source.profiles.map((row, index) => {
    if (row === null || typeof row !== "object") throw new ImportError(`staging profiles[${index}]: not an object.`);
    const where = `staging profiles[${index}]`;
    assertId(row.id, contract, where, { set: true });
    if (typeof row.name !== "string" || !row.name.trim()) throw new ImportError(`${where} (${row.id}): no name.`);
    if (typeof row.family !== "string" || !row.family.trim()) throw new ImportError(`${where} (${row.id}): no family.`);
    if (!Number.isFinite(row.order)) throw new ImportError(`${where} (${row.id}): order must be a number.`);
    return { ...row, index };
  });
  const ids = new Set();
  for (const row of rows) {
    if (ids.has(row.id)) throw new ImportError(`staging ${CATALOGUE_FILE}: id ${row.id} is listed twice.`);
    ids.add(row.id);
  }
  rows.sort((a, b) => a.order - b.order || a.index - b.index);

  // Families in order of first appearance; each name gets one id.
  const families = [];
  const familyByName = new Map();
  for (const row of rows) {
    const name = row.family;
    if (familyByName.has(name)) continue;
    const id = assertId(familyId(name), contract, `family ${JSON.stringify(name)}`);
    if (families.some((family) => family.id === id)) throw new ImportError(`Families ${JSON.stringify(name)} and another name both become id ${id}.`);
    const family = { id, name, order: families.length };
    families.push(family);
    familyByName.set(name, family);
  }

  assertId(defaultSet, contract, "default set", { set: true });
  const sets = [];
  for (const row of rows) {
    const staged = await readStagingSet(staging, row, contract, warnings);
    // Names and notes are kept exactly as staging has them (§3.5: same ids, names, families, order).
    const manifest = { schema: contract.set.schema, id: row.id, name: row.name, licence: staged.licence, recipe: staged.recipe, files: staged.files, preview: staged.previewName };
    const fp12 = seedFingerprint(manifest, staged.audio);
    sets.push({ ...staged, id: row.id, name: row.name, family: familyByName.get(row.family), order: row.order, index: row.index, note: typeof row.note === "string" && row.note.trim() ? row.note : undefined, manifest, manifestText: setManifestText(manifest), fp12 });
  }
  sets.sort((a, b) => a.family.order - b.family.order || a.order - b.order || a.index - b.index);
  if (!sets.some((set) => set.id === defaultSet)) throw new ImportError(`Default set ${JSON.stringify(defaultSet)} is not in the staging catalogue.`);

  // 2. Plan every set folder; an existing one must already hold exactly these
  // bytes (its set manifest may carry an older name: a rename keeps the folder).
  const keysDir = path.join(out, "v1", "keys");
  const setsDir = path.join(keysDir, "sets");
  const problems = [];
  for (const set of sets) {
    set.dir = `sets/${set.id}/${set.fp12}`;
    assertPath(`${set.dir}/${SET_MANIFEST_FILE}`, contract, `set ${set.id}`);
    const folder = path.join(setsDir, set.id, set.fp12);
    if ((await listFolder(folder)) === null) { set.create = true; continue; }
    set.create = false;
    const { problems: differences, heldName } = await folderDifferences(folder, set);
    if (differences.length) problems.push(`${set.dir}/ already exists with other content (set folders are never overwritten):\n    ${differences.join("\n    ")}`);
    else if (heldName !== set.name) warnings.push(`set ${set.id}: ${set.dir}/ keeps its set manifest name ${JSON.stringify(heldName)}; the catalogue carries ${JSON.stringify(set.name)}.`);
  }
  if (problems.length) throw new ImportError(problems.join("\n"));

  // 3. The catalogue: a published revision is never rewritten with other content.
  const profiles = sets.map((set, order) => ({
    id: set.id,
    name: set.name,
    family: set.family.name,
    familyId: set.family.id,
    order,
    score: set.score,
    ownerPick: set.ownerPick,
    status: "published",
    keys: set.keys,
    spaces: set.spaces,
    manifest: assertPath(`${set.dir}/${SET_MANIFEST_FILE}`, contract, `set ${set.id}`),
    preview: assertPath(`${set.dir}/${set.previewName}`, contract, `set ${set.id}`),
    ...(set.legacy ? { labels: [LEGACY_LABEL] } : {}),
    ...(set.note !== undefined ? { note: set.note } : {}),
  }));
  const effects = { ...contract.effects.defaults };
  const catalogue = { schema: contract.catalogue.schema, contract: contract.contract, revision, publishedAt: stamp, default: defaultSet, effects, families, profiles };
  const catalogueFile = path.join(keysDir, CATALOGUE_FILE);
  const existingText = await readOptional(catalogueFile);
  if (existingText !== null) {
    let existing;
    try { existing = JSON.parse(existingText.toString("utf8")); } catch {
      throw new ImportError(`${catalogueFile} is not valid JSON; fix or remove it by hand.`);
    }
    const held = typeof existing?.revision === "string" ? existing.revision : "";
    if (held === revision) {
      if (catalogueBody(existing) !== catalogueBody(catalogue)) {
        throw new ImportError(`${CATALOGUE_FILE} already holds revision ${revision} with other content; a published revision is never rewritten. Rerun with --revision r${revisionNumber(revision) + 1} to publish a new one.`);
      }
      if (typeof existing.publishedAt === "string") catalogue.publishedAt = existing.publishedAt;
    } else if (!REVISION.test(held) || revisionNumber(held) >= revisionNumber(revision)) {
      // Never step back over a newer revision, or over one another tool (the Admin) published.
      throw new ImportError(`${CATALOGUE_FILE} holds revision ${JSON.stringify(held)}; this import would replace it with ${revision}. ${REVISION.test(held) ? `Pass --revision r${revisionNumber(held) + 1} to publish a newer one.` : "The seed import does not replace a catalogue it did not write."}`);
    }
  }
  const catalogueText = `${JSON.stringify(catalogue, null, 2)}\n`;
  const healthFile = path.join(out, "v1", "health.json");
  const build = `data-${sha256(catalogueText).slice(0, 12)}`;
  const health = { contract: contract.contract, revision, build, builtAt: stamp };
  const healthText = await readOptional(healthFile);
  if (healthText !== null) {
    try {
      const existing = JSON.parse(healthText.toString("utf8"));
      if (existing?.contract === health.contract && existing.revision === revision && existing.build === build && typeof existing.builtAt === "string") health.builtAt = existing.builtAt;
    } catch { /* A broken health file is simply replaced. */ }
  }
  const nextHealth = `${JSON.stringify(health, null, 2)}\n`;

  // 4. Write: new set folders first, then the catalogue, then health. A set
  // folder written before a later error stays: it is content-addressed and
  // nothing points at it until the catalogue is written.
  const catalogueWritten = existingText === null || existingText.toString("utf8") !== catalogueText;
  const healthWritten = healthText === null || healthText.toString("utf8") !== nextHealth;
  try {
    for (const set of sets) if (set.create) await writeSetFolder(setsDir, set, set.manifestText);
    await mkdir(keysDir, { recursive: true });
    if (catalogueWritten) await writeAtomic(catalogueFile, catalogueText);
    if (healthWritten) await writeAtomic(healthFile, nextHealth);
  } catch (error) {
    if (error && typeof error === "object") error.duringWrite = true;
    throw error;
  }

  return {
    revision,
    publishedAt: catalogue.publishedAt,
    profiles: profiles.length,
    families: families.length,
    created: sets.filter((set) => set.create).map((set) => set.dir),
    reused: sets.filter((set) => !set.create).map((set) => set.dir),
    audioFiles: sets.reduce((sum, set) => sum + set.audio.length, 0),
    audioBytes: sets.reduce((sum, set) => sum + set.audio.reduce((total, item) => total + item.bytes, 0), 0),
    legacy: sets.filter((set) => set.legacy).length,
    catalogueWritten,
    healthWritten,
    warnings,
  };
}

const USAGE = "Usage: pnpm feel:import <stagingDir> [--out <publicDir>] [--revision r1] [--default bright-clack]";

export function parseArgs(argv) {
  const args = [...argv];
  if (args[0] === "--") args.shift();
  const options = {};
  const positional = [];
  const flags = { "--out": "publicDir", "--revision": "revision", "--default": "defaultSet" };
  for (let index = 0; index < args.length; index += 1) {
    const arg = args[index];
    if (arg === "-h" || arg === "--help") return { help: true };
    if (Object.hasOwn(flags, arg)) {
      const value = args[index + 1];
      if (value === undefined || value.startsWith("--")) throw new ImportError(`${arg} needs a value. ${USAGE}`);
      if (Object.hasOwn(options, flags[arg])) throw new ImportError(`${arg} given twice. ${USAGE}`);
      options[flags[arg]] = value;
      index += 1;
    } else if (arg.startsWith("-")) {
      throw new ImportError(`Unknown option ${arg}. ${USAGE}`);
    } else {
      positional.push(arg);
    }
  }
  if (positional.length !== 1) throw new ImportError(`Give exactly one staging folder. ${USAGE}`);
  return { ...options, stagingDir: positional[0] };
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
    const result = await importStaging(options);
    out.write(`Typing Feel ${result.revision}: ${result.profiles} sets in ${result.families} families, ${result.audioFiles} audio files (${result.audioBytes} bytes), ${result.legacy} labelled ${LEGACY_LABEL}.\n`);
    out.write(`  set folders: ${result.created.length} new, ${result.reused.length} unchanged\n`);
    out.write(`  keys-manifest.json: ${result.catalogueWritten ? "written" : "unchanged"} (publishedAt ${result.publishedAt}); health.json: ${result.healthWritten ? "written" : "unchanged"}\n`);
    for (const warning of result.warnings) out.write(`  warning: ${warning}\n`);
    return 0;
  } catch (error) {
    if (error instanceof ImportError) {
      err.write(`feel:import refused: ${error.message}\n${error.duringWrite ? "Stopped while writing; fix the cause and rerun (a rerun never overwrites)." : "Nothing was changed."}\n`);
      return 1;
    }
    throw error;
  }
}

if (process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url)) {
  process.exitCode = await main();
}

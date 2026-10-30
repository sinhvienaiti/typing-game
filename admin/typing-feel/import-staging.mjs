#!/usr/bin/env node
// One-off Typing Feel seed for the Admin (docs/games/TYPING_FEEL_SERVICE.md §3.5,
// §4.2 G1 note, §6.3 step 4).
//
//   node admin/typing-feel/import-staging.mjs <stagingDir> --public <typing-feel/public>
//   node admin/typing-feel/import-staging.mjs --restore --public <typing-feel/public>
//
// Registers every set of the published catalogue (today r1, 34 sets) as a Media V2
// reference version that keeps its G1 folder sets/<id>/<fp12>/ (the components'
// runtimeUrl carries it), so the first Publish moves no URL, then writes the
// first Typing Feel revision: seed-v1 (with a staging folder) or
// restored-<catalogue revision> (--restore, a fresh clone or a lost .local).
// Families, order, default and effects are the catalogue's; its export must
// equal the catalogue byte for byte before anything is written. A set folder
// with no catalogue row (a set hidden or retired before .local was lost) keeps
// its id: a hidden row when it has one complete folder, retiredIds otherwise.
// Reruns are no-ops and read before they write. The Media V2 registry is shared
// with a running Admin service through its lock file, so the Admin may stay up.
// The staging folder is only read, to cross-check names, families,
// order and audio bytes. Locations: --data / --shared or the env
// (TYPING_GAME_ADMIN_DATA_DIR, TYPING_GAME_ADMIN_SHARED_DIR), all three with
// --public overridden together or none (see locations.mjs).
import { lstat, readdir, readFile } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { LEGACY_LABEL, canonicalJson, loadContract, sha256 } from "../../typing-feel/tools/import-staging.mjs";
import { MediaAssetStore } from "../media-assets-v2.mjs";
import {
  CATALOGUE_FILE,
  KEYS_URL_PREFIX,
  PREVIEW_FILE,
  SET_MANIFEST_FILE,
  SET_TAGS,
  buildCatalogue,
  catalogueFile,
  catalogueProblems,
  ensureSetFolders,
  healthFile,
  healthText,
  keysDir,
  readTextOrNull,
} from "./export.mjs";
import { resolveTypingFeelLocations } from "./locations.mjs";
import { SET_NAME_MAX, TYPING_FEEL_CONFIG_SCHEMA, configProblems } from "./policy.mjs";
import { RESTORE_COMMAND, TypingFeelService } from "./service.mjs";
import { TypingFeelRevisionStore } from "./store.mjs";

const HERE = path.dirname(fileURLToPath(import.meta.url));
const REPO_ROOT = path.resolve(HERE, "../..");
export const SEED_REVISION = "seed-v1";
export const STAGING_CATALOGUE_SCHEMA = "typing-keys-firefly/catalogue-2";
export const LEGACY_NOTE = "legacy-218, owner-kept 30/10";
const LEGACY_GENERATOR = "keys-firefly/218 builder (tools/audio-lab keys/firefly_v2), Audio Lab staging, imported 30/10/2026";
const PICK_GENERATOR = "natural-v1, owner pick 30/10/2026 (tools/audio-lab, keys-firefly staging)";
const HIDDEN_GENERATOR = "Typing Feel restore: a published set folder with no catalogue row";
/** The recipe of the ticket 218 batch: every such set was imported as published with the legacy-218 label. */
const LEGACY_RECIPE = "firefly-218";
const SET_FOLDER_NAME = /^[0-9a-f]{12}$/;
export const RESTORED_FAMILY_ID = "restored";
export const RESTORED_FAMILY_NAME = "Restored";

export class SeedImportError extends Error {}

export function setAssetId(setId) {
  return `typing-feel.keyboard-set.${setId}`;
}

async function readJsonFile(file, label) {
  let text;
  try {
    text = await readFile(file, "utf8");
  } catch (error) {
    throw new SeedImportError(`${label}: ${error.code === "ENOENT" ? "not found" : error.message} (${file}).`);
  }
  try {
    return { text, value: JSON.parse(text) };
  } catch (error) {
    throw new SeedImportError(`${label}: not valid JSON (${error.message}).`);
  }
}

/**
 * One published set folder, read and hashed: the plan for its Media V2 reference
 * version. `hidden` marks a folder with no catalogue row (see findUnlistedSets):
 * its only facts are the set manifest's, and a firefly-218 recipe means the 218 batch.
 */
async function readPublishedSet(publicDir, profile, contract, { hidden = false } = {}) {
  const folder = profile.manifest.split("/").slice(0, 3).join("/");
  const root = path.join(keysDir(publicDir), ...folder.split("/"));
  const { text, value: manifest } = await readJsonFile(path.join(root, SET_MANIFEST_FILE), `set ${profile.id} ${folder}/${SET_MANIFEST_FILE}`);
  if (manifest?.schema !== contract.set.schema || manifest.id !== profile.id) throw new SeedImportError(`set ${profile.id}: ${folder}/${SET_MANIFEST_FILE} is not the ${contract.set.schema} manifest of this set.`);
  if (manifest.preview !== PREVIEW_FILE || !Array.isArray(manifest.files)) throw new SeedImportError(`set ${profile.id}: ${folder}/${SET_MANIFEST_FILE} has no files or preview.`);
  const filePattern = new RegExp(contract.set.file.filePattern);
  if (!manifest.files.every((entry) => typeof entry?.file === "string" && filePattern.test(entry.file))) throw new SeedImportError(`set ${profile.id}: ${folder}/${SET_MANIFEST_FILE} lists a file that is not key-NN.ogg or space-NN.ogg.`);
  if (hidden && !Object.hasOwn(contract.recipes, manifest.recipe)) throw new SeedImportError(`set ${profile.id}: ${folder}/${SET_MANIFEST_FILE} names the unknown recipe ${JSON.stringify(manifest.recipe)}.`);
  const manifestBytes = Buffer.from(text);
  const components = [{
    role: "manifest", mimeType: "application/json", format: "json", storageClass: "runtime-reference",
    runtimeUrl: `${KEYS_URL_PREFIX}${folder}/${SET_MANIFEST_FILE}`, sha256: sha256(manifestBytes), byteSize: manifestBytes.length,
  }];
  const files = [{ name: SET_MANIFEST_FILE, role: "manifest", sha256: components[0].sha256, byteSize: manifestBytes.length, source: path.join(root, SET_MANIFEST_FILE), storageClass: "runtime-reference" }];
  const entries = [...manifest.files.map((entry) => ({ name: entry.file, role: entry.file.replace(/\.ogg$/, ""), durationMs: entry.durationMs })), { name: PREVIEW_FILE, role: "preview" }];
  let keys = 0;
  let spaces = 0;
  for (const entry of entries) {
    const file = path.join(root, entry.name);
    let stats;
    try {
      stats = await lstat(file);
    } catch (error) {
      throw new SeedImportError(`set ${profile.id}: ${folder}/${entry.name} ${error.code === "ENOENT" ? "is missing (run pnpm media:pull)" : `cannot be read (${error.message})`}.`);
    }
    if (!stats.isFile()) throw new SeedImportError(`set ${profile.id}: ${folder}/${entry.name} is not a regular file.`);
    const bytes = await readFile(file);
    const hash = sha256(bytes);
    if (entry.role.startsWith("key-")) keys += 1;
    if (entry.role.startsWith("space-")) spaces += 1;
    components.push({
      role: entry.role, mimeType: "audio/ogg", format: "ogg", storageClass: "runtime-reference",
      runtimeUrl: `${KEYS_URL_PREFIX}${folder}/${entry.name}`, sha256: hash, byteSize: bytes.length,
      ...(Number.isInteger(entry.durationMs) && entry.durationMs > 0 ? { durationSeconds: entry.durationMs / 1000 } : {}),
    });
    files.push({ name: entry.name, role: entry.role, sha256: hash, byteSize: bytes.length, source: file, storageClass: "runtime-reference" });
  }
  const legacy = hidden ? manifest.recipe === LEGACY_RECIPE : (profile.labels ?? []).includes(LEGACY_LABEL);
  const source = {
    owner: "typing-feel",
    generator: legacy ? LEGACY_GENERATOR : hidden ? HIDDEN_GENERATOR : profile.ownerPick ? PICK_GENERATOR : "Typing Feel seed",
    sourcePath: `typing-feel/public${KEYS_URL_PREFIX}${folder}/`,
    license: manifest.licence,
    ...(legacy ? { note: LEGACY_NOTE } : typeof profile.note === "string" ? { note: profile.note.slice(0, 500) } : {}),
  };
  return { profile, folder, manifest, components, files, keys, spaces, source, legacy, hidden };
}

function validSetName(value) {
  return typeof value === "string" && value.trim() === value && value !== "" && value.length <= SET_NAME_MAX && !/[\u0000-\u001f\u007f]/.test(value);
}

/**
 * Ids that have a set folder under v1/keys/sets/ but no catalogue row. The
 * catalogue leaves hidden and retired sets out (§4.3) and set folders are never
 * deleted, so after a lost .local these folders are the only record that the ids
 * were used. An id with exactly one complete folder comes back as a hidden row
 * (same sound, so old saves keep pointing at it); any other id is retired, so it
 * can never be given another sound (§3.4, §3.13).
 * Returns { hidden: [planned set], retired: [{ id, reason }] }, sorted by id.
 */
async function findUnlistedSets(publicDir, catalogue, contract) {
  const setsDir = path.join(keysDir(publicDir), "sets");
  const listed = new Set(catalogue.profiles.map((profile) => profile.id));
  const idPattern = new RegExp(contract.id.pattern);
  const reserved = new Set(contract.id.reserved ?? []);
  let entries;
  try {
    entries = await readdir(setsDir, { withFileTypes: true });
  } catch (error) {
    if (error.code === "ENOENT") return { hidden: [], retired: [] };
    throw error;
  }
  const hidden = [];
  const retired = [];
  for (const entry of entries.sort((a, b) => a.name.localeCompare(b.name))) {
    if (!entry.isDirectory() || listed.has(entry.name) || !idPattern.test(entry.name) || reserved.has(entry.name)) continue;
    const id = entry.name;
    const folders = (await readdir(path.join(setsDir, id), { withFileTypes: true }))
      .filter((child) => child.isDirectory() && SET_FOLDER_NAME.test(child.name))
      .map((child) => child.name)
      .sort();
    if (folders.length !== 1) {
      retired.push({ id, reason: folders.length === 0 ? "it has no set folder" : `it has ${folders.length} set folders (${folders.join(", ")}), so its last sound is not known` });
      continue;
    }
    const folder = `sets/${id}/${folders[0]}`;
    try {
      const set = await readPublishedSet(publicDir, { id, manifest: `${folder}/${SET_MANIFEST_FILE}`, ownerPick: false }, contract, { hidden: true });
      // The same checks a revision's sets pass later, so a bad folder is retired here and never fails after the writes.
      const missing = contract.set.required.filter((field) => !Object.hasOwn(set.manifest, field));
      if (missing.length) throw new SeedImportError(`its set manifest has no ${missing.join(", ")}`);
      if (set.manifest.files.some((entry) => !Number.isInteger(entry.durationMs) || entry.durationMs <= 0 || !entry.file.startsWith(`${entry.set}-`))) throw new SeedImportError("its set manifest has a malformed file entry");
      if (set.keys < contract.set.minimum.key || set.spaces < contract.set.minimum.space) throw new SeedImportError(`it holds ${set.keys} keys and ${set.spaces} spaces, fewer than the ${contract.set.minimum.key} and ${contract.set.minimum.space} a set needs`);
      hidden.push(set);
    } catch (error) {
      if (!(error instanceof SeedImportError)) throw error;
      retired.push({ id, reason: `${folder}/ cannot be registered: ${error.message.replace(/^set \S+: /, "")}` });
    }
  }
  return { hidden, retired };
}

/** A family id and name for the restored hidden rows that no catalogue family uses. */
function restoredFamily(families) {
  for (let index = 1; ; index += 1) {
    const id = index === 1 ? RESTORED_FAMILY_ID : `${RESTORED_FAMILY_ID}-${index}`;
    const name = index === 1 ? RESTORED_FAMILY_NAME : `${RESTORED_FAMILY_NAME} ${index}`;
    if (!families.some((family) => family.id === id || family.name === name)) {
      return { id, name, order: Math.max(-1, ...families.map((family) => family.order)) + 1 };
    }
  }
}

/** Staging differences are reported, never fatal: the published folder is what the seed registers. */
async function compareStaging(stagingDir, catalogue, sets) {
  const warnings = [];
  const { value: staging } = await readJsonFile(path.join(stagingDir, CATALOGUE_FILE), `staging ${CATALOGUE_FILE}`);
  if (staging?.schema !== STAGING_CATALOGUE_SCHEMA || !Array.isArray(staging.profiles)) {
    throw new SeedImportError(`staging ${CATALOGUE_FILE}: schema is ${JSON.stringify(staging?.schema)}, expected ${STAGING_CATALOGUE_SCHEMA}.`);
  }
  const rows = staging.profiles.map((row, index) => ({ ...row, index })).sort((a, b) => a.order - b.order || a.index - b.index);
  // The G1 import grouped staging by family (first appearance), keeping staging order inside each family.
  const familyFirst = [];
  for (const row of rows) if (!familyFirst.includes(row.family)) familyFirst.push(row.family);
  const grouped = [...rows].sort((a, b) => familyFirst.indexOf(a.family) - familyFirst.indexOf(b.family));
  const rank = new Map(grouped.map((row, index) => [row.id, index]));
  const byId = new Map(rows.map((row) => [row.id, row]));
  for (const profile of catalogue.profiles) {
    const row = byId.get(profile.id);
    if (!row) {
      warnings.push(`set ${profile.id} is published but not in the staging catalogue.`);
      continue;
    }
    if (row.name !== profile.name) warnings.push(`set ${profile.id}: staging name ${JSON.stringify(row.name)}, published ${JSON.stringify(profile.name)}.`);
    if (row.family !== profile.family) warnings.push(`set ${profile.id}: staging family ${JSON.stringify(row.family)}, published ${JSON.stringify(profile.family)}.`);
    if (rank.get(profile.id) !== profile.order) warnings.push(`set ${profile.id}: staging position ${rank.get(profile.id)}, published order ${profile.order}.`);
    const set = sets.find((entry) => entry.profile.id === profile.id);
    const stagingFolder = path.join(stagingDir, ...String(row.manifest).split("/").slice(0, -1));
    let differ = 0;
    for (const file of set.files.filter((entry) => entry.role !== "manifest")) {
      try {
        if (sha256(await readFile(path.join(stagingFolder, file.name))) !== file.sha256) differ += 1;
      } catch {
        differ += 1;
      }
    }
    if (differ) warnings.push(`set ${profile.id}: ${differ} audio file(s) in staging differ from the published copy; the published bytes are registered.`);
  }
  for (const row of rows) if (!catalogue.profiles.some((profile) => profile.id === row.id)) warnings.push(`staging set ${row.id} is not published; add it through the Admin.`);
  return warnings;
}

/**
 * Imports (or restores) the seed. Throws SeedImportError with nothing changed
 * on any problem found before writing. Returns a summary.
 */
export async function importTypingFeelSeed({ publicDir, stagingDir = null, restore = false, mediaStore, store, contract = loadContract(), repoRoot = REPO_ROOT }) {
  if (!restore && !stagingDir) throw new SeedImportError("Give the staging folder, or --restore to rebuild from the published catalogue alone.");
  const { text: catalogueText, value: catalogue } = await readJsonFile(catalogueFile(publicDir), `published ${CATALOGUE_FILE}`);
  const shapeProblems = catalogueProblems(catalogue, contract);
  if (shapeProblems.length) throw new SeedImportError(`published ${CATALOGUE_FILE} breaks the v1 contract: ${shapeProblems.join(" ")}`);
  const healthTextOnDisk = await readTextOrNull(healthFile(publicDir));
  let builtAt = catalogue.publishedAt;
  try {
    const health = healthTextOnDisk === null ? null : JSON.parse(healthTextOnDisk);
    if (health?.revision === catalogue.revision && typeof health.builtAt === "string") builtAt = health.builtAt;
  } catch { /* A broken health file is rewritten by the server's start-up check. */ }

  const sets = [];
  for (const profile of catalogue.profiles) sets.push(await readPublishedSet(publicDir, profile, contract));
  const warnings = stagingDir ? await compareStaging(path.resolve(stagingDir), catalogue, sets) : [];
  const unlisted = await findUnlistedSets(publicDir, catalogue, contract);

  // The seed config: the catalogue's families, order, default and effects.
  const familyOrder = new Map();
  const planned = sets.map(({ profile, manifest }) => {
    const order = familyOrder.get(profile.familyId) ?? 0;
    familyOrder.set(profile.familyId, order + 1);
    return {
      id: profile.id,
      name: profile.name,
      family: profile.familyId,
      order,
      enabled: true,
      status: profile.status,
      assetVersionId: "media-version.planned",
      ownerPick: profile.ownerPick,
      ownerScore: null,
      recipe: manifest.recipe,
      score: profile.score,
      ...(profile.labels ? { labels: [...profile.labels] } : {}),
      ...(profile.note !== undefined ? { note: profile.note } : {}),
    };
  });
  const families = catalogue.families.map(({ id, name, order }) => ({ id, name, order }));
  // Folders with no catalogue row: hidden rows in their own family, which the export leaves
  // out with them. A 218-batch set was published; any other set's status was not recorded.
  if (unlisted.hidden.length) {
    const family = restoredFamily(families);
    families.push(family);
    unlisted.hidden.forEach(({ profile, manifest, folder, legacy }, order) => {
      planned.push({
        id: profile.id,
        name: validSetName(manifest.name) ? manifest.name : profile.id,
        family: family.id,
        order,
        enabled: false,
        status: legacy ? "published" : "provisional",
        assetVersionId: "media-version.planned",
        ownerPick: false,
        ownerScore: null,
        recipe: manifest.recipe,
        score: null,
        ...(legacy ? { labels: [LEGACY_LABEL] } : { note: `Restored hidden from ${folder}/, which catalogue ${catalogue.revision} does not list; its status before was not recorded.` }),
      });
    });
  }
  const allSets = [...sets, ...unlisted.hidden];
  const config = {
    schema: TYPING_FEEL_CONFIG_SCHEMA,
    contract: contract.contract,
    keyboard: {
      defaultSet: catalogue.default,
      families,
      sets: planned,
      retiredIds: unlisted.retired.map((entry) => entry.id),
    },
    effects: { defaults: { ...catalogue.effects } },
  };
  const configIssues = configProblems(config, contract);
  if (configIssues.length) throw new SeedImportError(`The seed config would be invalid: ${configIssues.join(" ")}`);

  // Before any write: the seed's export must be the published catalogue, byte for byte,
  // and every set folder must hold exactly the files it lists.
  const described = new Map(allSets.map((set) => [set.profile.id, { folder: set.folder, keys: set.keys, spaces: set.spaces, files: set.files, provenance: "generated-runtime" }]));
  const exported = buildCatalogue({ config, described, catalogueRevision: catalogue.revision, publishedAt: catalogue.publishedAt, contract });
  if (exported.text !== catalogueText) {
    throw new SeedImportError(`The seed's export would differ from the published ${CATALOGUE_FILE} (revision ${catalogue.revision}); nothing was changed. Check the catalogue for fields the Admin does not keep.`);
  }
  const expectedHealth = healthText({ catalogueText, catalogueRevision: catalogue.revision, builtAt, contract });
  if (healthTextOnDisk !== expectedHealth) warnings.push("health.json differs from the catalogue; the Admin server rewrites it at start-up.");
  await ensureSetFolders({ config, described, publicDir, dryRun: true });

  const seedRevision = restore ? `restored-${catalogue.revision}` : SEED_REVISION;
  const unlistedNote = unlisted.hidden.length || unlisted.retired.length
    ? ` Set folders with no catalogue row: ${unlisted.hidden.length} kept as hidden rows, ${unlisted.retired.length} retired.`
    : "";
  const message = restore
    ? `Restored from the published Typing Feel catalogue ${catalogue.revision} (${sets.length} sets); drafts that were never published are not recoverable.${unlistedNote}`
    : `Typing Feel seed: catalogue ${catalogue.revision} (${sets.length} sets) from the Audio Lab staging; 32 legacy-218 sets and the owner picks Raindrop Tile and Hail Stone as published.${unlistedNote}`;
  const registration = (set) => ({
    assetId: setAssetId(set.profile.id),
    kind: "audio",
    title: config.keyboard.sets.find((row) => row.id === set.profile.id).name,
    provenance: "generated-runtime",
    components: set.components,
    actorId: "typing-feel-seed",
    tags: [...SET_TAGS, ...(set.legacy ? [LEGACY_LABEL] : [])],
    source: set.source,
  });

  return store.exclusive(async () => {
    const initialized = await store.isInitialized();
    if (initialized && !(await store.hasRevision(seedRevision))) {
      const state = await store.getState();
      throw new SeedImportError(`The Typing Feel store already holds revisions (active ${state.activeRevision}) and no ${seedRevision}; the seed only runs on an empty store. Nothing was changed.`);
    }
    return mediaStore.withWriteLock(async () => {
      let versionsCreated = 0;
      let revisionWritten = false;
      if (initialized) {
        // A rerun reads first and writes only what an interrupted run left out (the
        // publication record, references): Media V2 must already hold every version
        // the stored revision names, with the same content.
        const existing = await store.getRevision(seedRevision);
        const named = new Map((existing.config?.keyboard?.sets ?? []).map((row) => [row.id, row.assetVersionId]));
        const lost = [];
        for (const [index, set] of allSets.entries()) {
          const found = await mediaStore.findReferenceVersion(registration(set));
          if (found) {
            config.keyboard.sets[index].assetVersionId = found.assetVersionId;
            described.get(set.profile.id).assetId = found.assetId;
            continue;
          }
          const versionId = named.get(set.profile.id);
          if (versionId && !(await mediaStore.getVersion(versionId).then(() => true, () => false))) lost.push(`${set.profile.id} → ${versionId}`);
        }
        if (lost.length) {
          throw new SeedImportError(`Media V2 (${mediaStore.registryPath}) does not hold ${lost.length} of the versions ${seedRevision} names (for example ${lost[0]}): the Media registry was reset or lost while the Typing Feel store (${store.rootDir}) was kept. Nothing was changed. To recover, move the Typing Feel store folder aside, run ${RESTORE_COMMAND} and restart the Admin service: the restore rebuilds the live catalogue and keeps every id that has a set folder; drafts that were never published and the revision history stay in the moved folder only.`);
        }
        if (canonicalJson(existing.config) !== canonicalJson(config)) {
          throw new SeedImportError(`Revision ${seedRevision} already exists with other content (the published catalogue or its set folders changed since); nothing was changed.`);
        }
      } else {
        for (const [index, set] of allSets.entries()) {
          const result = await mediaStore.registerReferenceAsset(registration(set));
          if (result.created) versionsCreated += 1;
          config.keyboard.sets[index].assetVersionId = result.version.assetVersionId;
          described.get(set.profile.id).assetId = result.version.assetId;
        }
        await store.initialize(config, { revision: seedRevision, message, author: "typing-feel-seed" });
        revisionWritten = true;
      }
      const publicationWritten = await store.writePublication({ revision: seedRevision, catalogueRevision: catalogue.revision, publishedAt: catalogue.publishedAt, builtAt });
      const service = new TypingFeelService({ store, mediaStore, publicDir, repoRoot, contract });
      const referencesCreated = await service.addReferences(seedRevision, config, described, "typing-feel-seed");
      // The stored seed passes the same checks every later revision does.
      const { problems } = await service.checkConfig(config);
      if (problems.length) throw new SeedImportError(`The imported seed fails its own checks: ${problems.join(" ")}`);
      return {
        revision: seedRevision,
        catalogueRevision: catalogue.revision,
        sets: sets.length,
        families: catalogue.families.length,
        legacy: sets.filter((set) => set.legacy).length,
        ownerPicks: sets.filter((set) => set.profile.ownerPick).length,
        versionsCreated,
        versionsReused: allSets.length - versionsCreated,
        hidden: unlisted.hidden.map((set) => set.profile.id),
        retired: unlisted.retired,
        revisionWritten,
        publicationWritten,
        referencesCreated,
        changed: versionsCreated > 0 || revisionWritten || publicationWritten || referencesCreated > 0,
        warnings,
      };
    });
  });
}

const USAGE = "Usage: node admin/typing-feel/import-staging.mjs <stagingDir> --public <typing-feel/public> [--data <dir> --shared <dir>]\n       node admin/typing-feel/import-staging.mjs --restore --public <typing-feel/public> [--data <dir> --shared <dir>]";

export function parseArgs(argv) {
  const options = { restore: false };
  const positional = [];
  const flags = { "--public": "publicDir", "--data": "dataDir", "--shared": "sharedDir" };
  for (let index = 0; index < argv.length; index += 1) {
    const arg = argv[index];
    if (arg === "-h" || arg === "--help") return { help: true };
    if (arg === "--restore") options.restore = true;
    else if (Object.hasOwn(flags, arg)) {
      const value = argv[index + 1];
      if (value === undefined || value.startsWith("--")) throw new SeedImportError(`${arg} needs a value.\n${USAGE}`);
      options[flags[arg]] = value;
      index += 1;
    } else if (arg.startsWith("-")) throw new SeedImportError(`Unknown option ${arg}.\n${USAGE}`);
    else positional.push(arg);
  }
  if (!options.publicDir) throw new SeedImportError(`--public is required.\n${USAGE}`);
  if (options.restore ? positional.length !== 0 : positional.length !== 1) throw new SeedImportError(`${options.restore ? "--restore takes no staging folder" : "Give exactly one staging folder"}.\n${USAGE}`);
  return { ...options, stagingDir: positional[0] ?? null };
}

export async function main(argv = process.argv.slice(2), { out = process.stdout, err = process.stderr, env = process.env, root = REPO_ROOT } = {}) {
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
  const locations = resolveTypingFeelLocations({ root, env, values: { dataDir: options.dataDir, sharedDir: options.sharedDir, publicDir: options.publicDir } });
  if (!locations.available) {
    err.write(`${locations.reason}\n`);
    return 2;
  }
  try {
    const mediaStore = new MediaAssetStore({ rootDir: locations.dataDir });
    await mediaStore.initialize();
    const store = new TypingFeelRevisionStore({ rootDir: locations.sharedDir });
    const result = await importTypingFeelSeed({ publicDir: locations.publicDir, stagingDir: options.stagingDir, restore: options.restore, mediaStore, store, repoRoot: root });
    out.write(`Typing Feel ${result.revision} (catalogue ${result.catalogueRevision}): ${result.sets} sets in ${result.families} families, ${result.legacy} legacy-218, ${result.ownerPicks} owner picks.\n`);
    out.write(`  Media V2 versions: ${result.versionsCreated} new, ${result.versionsReused} unchanged; references: ${result.referencesCreated} new\n`);
    out.write(`  revision: ${result.revisionWritten ? "written" : "unchanged"}; publication record: ${result.publicationWritten ? "written" : "unchanged"}${result.changed ? "" : " (nothing changed)"}\n`);
    if (result.hidden.length) {
      out.write(`  set folders with no catalogue row, kept as hidden rows in family ${RESTORED_FAMILY_NAME}: ${result.hidden.join(", ")}\n`);
      out.write("    Each was hidden or retired before. Retire again in Keyboard Sounds any that were retired.\n");
    }
    for (const entry of result.retired) out.write(`  retired (the id is never used again): ${entry.id}, because ${entry.reason}\n`);
    for (const warning of result.warnings) out.write(`  warning: ${warning}\n`);
    return 0;
  } catch (error) {
    if (error instanceof SeedImportError) {
      err.write(`Typing Feel seed refused: ${error.message}\n`);
      return 1;
    }
    throw error;
  }
}

if (process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url)) {
  process.exitCode = await main();
}

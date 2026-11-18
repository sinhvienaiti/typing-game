// Typing Feel export (docs/games/TYPING_FEEL_SERVICE.md §3.12, §4.2–4.4).
// Turns one typing-feel-admin/1 revision plus its Media V2 versions into the
// static files every game reads under <public>/v1/keys/:
//   sets/<id>/<fp12>/  immutable set folders (written once, never overwritten),
//   keys-manifest.json the catalogue (typing-feel/catalogue-3, atomic temp + rename),
//   ../health.json     { contract, revision, build, builtAt }.
// Seed sets are Media V2 reference versions that keep their G1 folder (their
// runtimeUrl carries it); Admin-upload bundles get sets/<id>/<first 12 hex of
// the version contentFingerprint>/.
import { randomUUID } from "node:crypto";
import { constants } from "node:fs";
import { copyFile, lstat, mkdir, readdir, readFile, rename, rm, writeFile } from "node:fs/promises";
import { join } from "node:path";
import { pathProblem, sha256 } from "../../typing-feel/tools/import-staging.mjs";

export const CATALOGUE_FILE = "keys-manifest.json";
export const SET_MANIFEST_FILE = "keys-manifest.json";
export const PREVIEW_FILE = "preview.ogg";
export const KEYS_URL_PREFIX = "/v1/keys/";
export const SET_TAGS = Object.freeze(["typing-feel", "keyboard-set"]);
const KEY_ROLE = /^(key|space)-([0-9]{2,3})$/;
const FOLDER = /^sets\/([a-z0-9][a-z0-9-]{0,31})\/([0-9a-f]{12})$/;
const ISO_SECONDS = /^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$/;
const INCOMING_PREFIX = ".incoming-";

export class TypingFeelExportError extends Error {
  constructor(problems) {
    const list = [problems].flat().filter(Boolean);
    super(list.length === 1 ? list[0] : `${list.length} problems: ${list.join(" ")}`);
    this.name = "TypingFeelExportError";
    this.problems = list;
  }
}

export function isoSeconds(value) {
  const date = value instanceof Date ? value : new Date(value);
  if (Number.isNaN(date.getTime())) throw new TypeError(`Invalid time: ${String(value)}.`);
  return date.toISOString().replace(/\.\d{3}Z$/, "Z");
}

export function keysDir(publicDir) {
  return join(publicDir, "v1", "keys");
}

export function catalogueFile(publicDir) {
  return join(keysDir(publicDir), CATALOGUE_FILE);
}

export function healthFile(publicDir) {
  return join(publicDir, "v1", "health.json");
}

/** The file a component is published as, or null for roles that stay in the Admin (report, A/B takes, source). */
export function publishedFileName(role) {
  if (role === "manifest") return SET_MANIFEST_FILE;
  if (role === "preview") return PREVIEW_FILE;
  if (KEY_ROLE.test(role)) return `${role}.ogg`;
  return null;
}

function folderFromReference(component, problems, label) {
  const url = component.runtimeUrl;
  const name = publishedFileName(component.role);
  if (typeof url !== "string" || !url.startsWith(KEYS_URL_PREFIX) || !url.endsWith(`/${name}`)) {
    problems.push(`${label}: reference component ${component.role} must carry its published URL ${KEYS_URL_PREFIX}sets/<id>/<fp12>/${name}.`);
    return null;
  }
  return url.slice(KEYS_URL_PREFIX.length, -(name.length + 1));
}

/**
 * Reads one Media V2 version as a keyboard set: where it is published, its files
 * (name, sha256, size, where the bytes are), its parsed set-1 manifest and counts.
 * Returns { description, problems }: problems are owner-readable sentences.
 */
export async function describeSetVersion({ mediaStore, publicDir, assetVersionId, setId, contract, readAccept = false }) {
  const label = `Set ${setId}`;
  const problems = [];
  let version;
  let asset;
  try {
    version = await mediaStore.getVersion(assetVersionId);
    asset = await mediaStore.getAsset(version.assetId);
  } catch (error) {
    return { description: null, problems: [`${label}: Media V2 version ${assetVersionId} is unknown (${error.message})`] };
  }
  for (const tag of SET_TAGS) if (!asset.tags.includes(tag)) problems.push(`${label}: Media asset ${asset.assetId} must carry the tag ${tag}.`);

  const files = [];
  let folder = null;
  let keys = 0;
  let spaces = 0;
  for (const component of version.components) {
    const name = publishedFileName(component.role);
    if (name === null) continue;
    const match = KEY_ROLE.exec(component.role);
    if (match?.[1] === "key") keys += 1;
    if (match?.[1] === "space") spaces += 1;
    const expectedFormat = component.role === "manifest" ? "json" : "ogg";
    if (component.format !== undefined && component.format !== expectedFormat) problems.push(`${label}: component ${component.role} must be ${expectedFormat}, not ${component.format}.`);
    if (typeof component.sha256 !== "string" || !Number.isInteger(component.byteSize)) {
      problems.push(`${label}: component ${component.role} has no sha256 and size, so its published copy cannot be checked.`);
      continue;
    }
    let source;
    if (component.storageClass === "admin-blob") {
      source = join(mediaStore.mediaRoot, component.storageKey);
    } else if (component.storageClass === "runtime-reference") {
      const held = folderFromReference(component, problems, label);
      if (held === null) continue;
      if (folder !== null && folder !== held) problems.push(`${label}: components point at two folders (${folder}, ${held}).`);
      folder ??= held;
      source = join(keysDir(publicDir), ...held.split("/"), name);
    } else {
      problems.push(`${label}: component ${component.role} is ${component.storageClass}; only Admin blobs and published references can be exported.`);
      continue;
    }
    files.push({ name, role: component.role, sha256: component.sha256, byteSize: component.byteSize, source, storageClass: component.storageClass });
  }
  if (version.provenance === "admin-upload") folder = `sets/${setId}/${version.contentFingerprint.slice(0, 12)}`;
  const minimum = contract.set.minimum;
  if (!files.some((file) => file.role === "manifest")) problems.push(`${label}: the Media version has no manifest component.`);
  if (!files.some((file) => file.role === "preview")) problems.push(`${label}: the Media version has no preview component.`);
  if (keys < minimum.key || spaces < minimum.space) problems.push(`${label}: ${keys} keys and ${spaces} spaces; at least ${minimum.key} keys and ${minimum.space} spaces are needed.`);
  if (folder === null) problems.push(`${label}: the Media version does not say where it is published.`);
  else {
    const match = FOLDER.exec(folder);
    if (!match) problems.push(`${label}: folder ${folder} is not sets/<id>/<fp12>.`);
    else if (match[1] !== setId) problems.push(`${label}: its Media version is published as set ${match[1]}.`);
    const pathIssue = pathProblem(`${folder}/${SET_MANIFEST_FILE}`, contract);
    if (pathIssue) problems.push(`${label}: path ${folder} is refused (${pathIssue}).`);
  }

  // The set-1 manifest: read once, checked against its own sha256 and against the components.
  let manifest = null;
  const manifestFile = files.find((file) => file.role === "manifest");
  if (manifestFile && problems.length === 0) {
    try {
      const bytes = await readFile(manifestFile.source);
      if (sha256(bytes) !== manifestFile.sha256) problems.push(`${label}: ${folder}/${SET_MANIFEST_FILE} does not match its Media V2 sha256.`);
      else manifest = JSON.parse(bytes.toString("utf8"));
    } catch (error) {
      problems.push(`${label}: cannot read its set manifest (${error.code === "ENOENT" ? "file missing; run pnpm media:pull" : error.message}).`);
    }
  }
  if (manifest !== null) {
    const audio = new Set(files.filter((file) => file.role !== "manifest" && file.role !== "preview").map((file) => file.name));
    const listed = Array.isArray(manifest.files) ? manifest.files : [];
    const filePattern = new RegExp(contract.set.file.filePattern);
    if (manifest.schema !== contract.set.schema) problems.push(`${label}: set manifest schema is ${JSON.stringify(manifest.schema)}, not ${contract.set.schema}.`);
    if (manifest.id !== setId) problems.push(`${label}: set manifest names id ${JSON.stringify(manifest.id)}.`);
    for (const field of contract.set.required) if (!Object.hasOwn(manifest, field)) problems.push(`${label}: set manifest has no ${field}.`);
    if (!Object.hasOwn(contract.recipes, manifest.recipe)) problems.push(`${label}: set manifest recipe ${JSON.stringify(manifest.recipe)} is unknown.`);
    if (manifest.preview !== PREVIEW_FILE) problems.push(`${label}: set manifest preview must be ${PREVIEW_FILE}.`);
    const names = new Set();
    for (const entry of listed) {
      if (!entry || !filePattern.test(entry.file) || !entry.file.startsWith(`${entry.set}-`) || !Number.isInteger(entry.durationMs) || entry.durationMs <= 0) {
        problems.push(`${label}: set manifest file entry ${JSON.stringify(entry)} is malformed.`);
      } else names.add(entry.file);
    }
    for (const name of audio) if (!names.has(name)) problems.push(`${label}: ${name} is in Media V2 but not in the set manifest.`);
    for (const name of names) if (!audio.has(name)) problems.push(`${label}: the set manifest lists ${name}, which Media V2 does not hold.`);
  }
  if (problems.length) return { description: null, problems };
  // Decision 5: an Admin-upload set carries the owner's Accept record (score and status) in its report component.
  const accept = readAccept && version.provenance === "admin-upload" ? await acceptRecord(mediaStore, version) : null;
  // An Admin-upload set names the Media version of its source WAV (§3.6: source.sourcePath).
  let sourceAssetVersionId = null;
  if (typeof version.source?.sourcePath === "string" && /^media-version\.[a-z0-9._:-]+$/.test(version.source.sourcePath)) {
    sourceAssetVersionId = version.source.sourcePath;
  }
  return {
    description: {
      setId,
      assetId: asset.assetId,
      sourceAssetVersionId,
      assetVersionId: version.assetVersionId,
      provenance: version.provenance,
      archived: asset.lifecycle === "archived",
      folder,
      keys,
      spaces,
      recipe: manifest.recipe,
      manifestName: manifest.name,
      files: files.sort((a, b) => a.name.localeCompare(b.name)),
      ...(accept ? { accept } : {}),
    },
    problems,
  };
}

/**
 * The Accept record of an Admin-upload set version: report.json's `accept` block,
 * written server-side by jobs.accept (§3.8 step 4), the only code that makes
 * Admin-upload set bundles. Returns { ownerScore, status, reason }, null when the
 * version has no record (a bundle not made by Accept: the client rules of
 * baseProblems still apply), or { missing: why } when a report is there but
 * cannot be trusted (never throws).
 */
async function acceptRecord(mediaStore, version) {
  if (!version.components.some((component) => component.role === "report")) return null;
  try {
    const component = await mediaStore.resolveComponent(version.assetVersionId, "report");
    if (!component.absolutePath) return null;
    const bytes = await readFile(component.absolutePath);
    if (sha256(bytes) !== component.sha256) return { missing: "its report does not match its Media V2 sha256" };
    const block = JSON.parse(bytes.toString("utf8"))?.accept;
    if (block === undefined || block === null) return null;
    if (typeof block.ownerScore !== "number" || typeof block.status !== "string") return { missing: "its Accept record has no owner score or status" };
    return { ownerScore: block.ownerScore, status: block.status, reason: typeof block.reason === "string" ? block.reason : null };
  } catch (error) {
    return { missing: `its report cannot be read (${error.code === "ENOENT" ? "file missing; run pnpm media:pull" : error.message})` };
  }
}

const STATUS_WORD = Object.freeze({ published: "Published", provisional: "Provisional" });

/**
 * Decision 5 (§8.3) against what the owner did, not what a client sent: a draft row
 * of an Admin-upload set keeps the status and owner score recorded at Accept. Save
 * draft cannot turn a Provisional set (scored under 9) into a Published one; a new
 * score needs a new Format and Accept.
 */
function acceptProblem(set, accept) {
  if (!accept) return null;
  if (accept.missing) return `Set ${set.id}: its Media version cannot show the owner's Accept (${accept.missing}); accept the set again from Add sound set.`;
  if (set.status === accept.status && set.ownerScore === accept.ownerScore) return null;
  return `Set ${set.id}: the owner accepted this sound as ${STATUS_WORD[accept.status] ?? accept.status}, owner score ${accept.ownerScore}; the draft says ${STATUS_WORD[set.status] ?? set.status}, owner score ${set.ownerScore ?? "none"}. The status and score come from Accept: Format and accept the take again to change them.`;
}

/** Describes every set of `config`; returns { described: Map<setId, description>, problems }. */
export async function describeConfigSets({ config, mediaStore, publicDir, contract, baseConfig = null }) {
  const described = new Map();
  const problems = [];
  const baseVersions = new Map((baseConfig?.keyboard?.sets ?? []).map((set) => [set.id, set.assetVersionId]));
  const seen = new Map();
  for (const set of config.keyboard.sets) {
    // A draft (baseConfig given) is checked against the owner's Accept records too.
    const { description, problems: found } = await describeSetVersion({ mediaStore, publicDir, assetVersionId: set.assetVersionId, setId: set.id, contract, readAccept: baseConfig !== null });
    problems.push(...found);
    if (!description) continue;
    const decided = acceptProblem(set, description.accept);
    if (decided) problems.push(decided);
    if (seen.has(description.assetVersionId)) problems.push(`Sets ${seen.get(description.assetVersionId)} and ${set.id} use the same Media version.`);
    seen.set(description.assetVersionId, set.id);
    // §3.4: a sound newly chosen in a draft never comes from an archived asset (a rollback or re-export may still use one).
    if (baseConfig && description.archived && baseVersions.get(set.id) !== set.assetVersionId) problems.push(`Set ${set.id}: Media asset ${description.assetId} is archived; restore it before using it.`);
    if (description.recipe !== set.recipe) problems.push(`Set ${set.id}: recipe ${set.recipe} differs from its set manifest (${description.recipe}).`);
    described.set(set.id, description);
  }
  return { described, problems };
}

/** The catalogue-3 object and its exact text for one revision. Hidden sets are left out; orders are contiguous. */
export function buildCatalogue({ config, described, catalogueRevision, publishedAt, contract }) {
  const keyboard = config.keyboard;
  const shown = keyboard.sets.filter((set) => set.enabled);
  const familyById = new Map(keyboard.families.map((family) => [family.id, family]));
  const usedFamilies = keyboard.families
    .filter((family) => shown.some((set) => set.family === family.id))
    .sort((a, b) => a.order - b.order || a.id.localeCompare(b.id));
  const familyRank = new Map(usedFamilies.map((family, index) => [family.id, index]));
  const ordered = [...shown].sort((a, b) => familyRank.get(a.family) - familyRank.get(b.family) || a.order - b.order || a.id.localeCompare(b.id));
  const families = usedFamilies.map((family, order) => ({ id: family.id, name: family.name, order }));
  const profiles = ordered.map((set, order) => {
    const description = described.get(set.id);
    if (!description) throw new TypingFeelExportError(`Set ${set.id} has no checked Media version.`);
    const family = familyById.get(set.family);
    return {
      id: set.id,
      name: set.name,
      family: family.name,
      familyId: family.id,
      order,
      score: typeof set.score === "number" ? set.score : null,
      ownerPick: set.ownerPick,
      status: set.status,
      keys: description.keys,
      spaces: description.spaces,
      manifest: `${description.folder}/${SET_MANIFEST_FILE}`,
      preview: `${description.folder}/${PREVIEW_FILE}`,
      ...(Array.isArray(set.labels) && set.labels.length ? { labels: [...set.labels] } : {}),
      ...(typeof set.note === "string" ? { note: set.note } : {}),
    };
  });
  const defaults = config.effects.defaults;
  const catalogue = {
    schema: contract.catalogue.schema,
    contract: contract.contract,
    revision: catalogueRevision,
    publishedAt,
    default: keyboard.defaultSet,
    effects: { style: defaults.style, intensity: defaults.intensity, size: defaults.size, volume: defaults.volume },
    families,
    profiles,
  };
  return { catalogue, text: `${JSON.stringify(catalogue, null, 2)}\n` };
}

/**
 * Every rule a published catalogue must meet: the contract (required fields,
 * ids, paths, statuses, labels, contiguous orders, one run per family) and the
 * kit's loadKeyboardCatalog reader (manifest, preview and order on every row,
 * a resolvable relative path, a non-empty list). Returns [] when it passes.
 */
export function catalogueProblems(catalogue, contract) {
  const problems = [];
  const add = (message) => problems.push(message);
  const idPattern = new RegExp(contract.id.pattern);
  const reserved = new Set(contract.id.reserved ?? []);
  const fpPattern = new RegExp(contract.fingerprint.pattern);
  const exactKeys = (value, path, required, optional = []) => {
    if (value === null || typeof value !== "object" || Array.isArray(value)) return add(`${path} must be an object.`);
    for (const key of required) if (!Object.hasOwn(value, key)) add(`${path}.${key} is required.`);
    for (const key of Object.keys(value)) if (!required.includes(key) && !optional.includes(key)) add(`${path}.${key} is not in the v1 contract.`);
  };
  exactKeys(catalogue, "catalogue", contract.catalogue.required, contract.catalogue.optional);
  if (problems.length) return problems;
  if (catalogue.schema !== contract.catalogue.schema) add(`catalogue.schema must be ${contract.catalogue.schema}.`);
  if (catalogue.contract !== contract.contract) add(`catalogue.contract must be ${contract.contract}.`);
  const revision = catalogue.revision;
  if (typeof revision !== "string" || revision.trim() !== revision || revision === "" || revision.length > 128 || /[\u0000-\u001f\u007f]/.test(revision)) add("catalogue.revision must be a short printable id.");
  if (typeof catalogue.publishedAt !== "string" || !ISO_SECONDS.test(catalogue.publishedAt)) add("catalogue.publishedAt must be ISO 8601 UTC without milliseconds.");
  const effects = catalogue.effects;
  exactKeys(effects, "catalogue.effects", ["style", "intensity", "size", "volume"]);
  if (effects && typeof effects === "object") {
    if (!contract.effects.styles.includes(effects.style)) add("catalogue.effects.style is not a known style.");
    if (!contract.effects.intensities.includes(effects.intensity)) add("catalogue.effects.intensity is not a known intensity.");
    if (!contract.effects.sizes.includes(effects.size)) add("catalogue.effects.size is not a known size.");
    if (typeof effects.volume !== "number" || effects.volume < contract.effects.volume.min || effects.volume > contract.effects.volume.max) add("catalogue.effects.volume is out of range.");
  }

  const families = Array.isArray(catalogue.families) ? catalogue.families : [];
  if (!Array.isArray(catalogue.families) || families.length === 0) add("catalogue.families must list at least one family.");
  const familyById = new Map();
  families.forEach((family, index) => {
    exactKeys(family, `families[${index}]`, contract.catalogue.family.required, contract.catalogue.family.optional);
    if (!idPattern.test(family?.id ?? "")) add(`families[${index}].id is invalid.`);
    if (familyById.has(family?.id)) add(`Family ${family?.id} is listed twice.`);
    if (family?.order !== index) add(`families[${index}].order must be ${index} (contiguous from 0).`);
    familyById.set(family?.id, family);
  });

  const profiles = Array.isArray(catalogue.profiles) ? catalogue.profiles : [];
  if (!Array.isArray(catalogue.profiles) || profiles.length === 0) add("catalogue.profiles must list at least one set (an empty list is invalid in every game).");
  const ids = new Set();
  const finishedFamilies = new Set();
  let currentFamily = null;
  let lastFamilyOrder = -1;
  profiles.forEach((profile, index) => {
    const at = `profiles[${index}]`;
    exactKeys(profile, at, contract.catalogue.profile.required, contract.catalogue.profile.optional);
    if (!profile || typeof profile !== "object") return;
    if (typeof profile.id !== "string" || !idPattern.test(profile.id) || reserved.has(profile.id)) add(`${at}.id ${JSON.stringify(profile.id)} is invalid or reserved.`);
    if (ids.has(profile.id)) add(`Set ${profile.id} is listed twice.`);
    ids.add(profile.id);
    if (typeof profile.name !== "string" || profile.name.trim() === "") add(`${at}.name must not be empty.`);
    if (profile.order !== index) add(`${at}.order must be ${index} (contiguous from 0, in list order).`);
    const family = familyById.get(profile.familyId);
    if (!family) add(`${at}.familyId ${JSON.stringify(profile.familyId)} is not in families.`);
    else {
      if (profile.family !== family.name) add(`${at}.family must be the family name ${JSON.stringify(family.name)}.`);
      if (profile.familyId !== currentFamily) {
        if (finishedFamilies.has(profile.familyId)) add(`Family ${profile.familyId} is split into two runs; each family must be one run.`);
        if (currentFamily !== null) finishedFamilies.add(currentFamily);
        if (family.order < lastFamilyOrder) add(`Family ${profile.familyId} comes after a family with a higher order.`);
        currentFamily = profile.familyId;
        lastFamilyOrder = family.order;
      }
    }
    if (profile.score !== null && (typeof profile.score !== "number" || !Number.isFinite(profile.score))) add(`${at}.score must be a number or null.`);
    if (typeof profile.ownerPick !== "boolean") add(`${at}.ownerPick must be true or false.`);
    if (!contract.statuses.includes(profile.status)) add(`${at}.status must be one of ${contract.statuses.join(", ")}.`);
    if (!Number.isInteger(profile.keys) || profile.keys < contract.set.minimum.key) add(`${at}.keys must be at least ${contract.set.minimum.key}.`);
    if (!Number.isInteger(profile.spaces) || profile.spaces < contract.set.minimum.space) add(`${at}.spaces must be at least ${contract.set.minimum.space}.`);
    for (const [field, file] of [["manifest", SET_MANIFEST_FILE], ["preview", PREVIEW_FILE]]) {
      const value = profile[field];
      const issue = pathProblem(value, contract);
      if (issue) {
        add(`${at}.${field} ${JSON.stringify(value)} is refused (${issue}).`);
        continue;
      }
      const parts = value.split("/");
      if (parts.length !== 4 || parts[0] !== "sets" || parts[1] !== profile.id || !fpPattern.test(parts[2]) || parts[3] !== file) {
        add(`${at}.${field} must be sets/${profile.id}/<fp12>/${file}.`);
      }
    }
    if (typeof profile.manifest === "string" && typeof profile.preview === "string" && profile.manifest.split("/").slice(0, 3).join("/") !== profile.preview.split("/").slice(0, 3).join("/")) {
      add(`${at}: manifest and preview must share one set folder.`);
    }
    if (profile.labels !== undefined && (!Array.isArray(profile.labels) || profile.labels.length === 0 || profile.labels.some((value) => !Object.hasOwn(contract.labels, value)))) add(`${at}.labels must list known labels.`);
    if (profile.note !== undefined && (typeof profile.note !== "string" || profile.note.trim() === "")) add(`${at}.note must be text.`);
  });
  const chosen = profiles.find((profile) => profile?.id === catalogue.default);
  if (!chosen) add(`Default ${JSON.stringify(catalogue.default)} is not a listed set.`);
  else if (chosen.status !== "published") add(`Default ${catalogue.default} must be published, not ${chosen.status}.`);
  return problems;
}

/** health.json text for a catalogue (contract health: build is data-<12 hex of the catalogue bytes>). */
export function healthText({ catalogueText, catalogueRevision, builtAt, contract }) {
  const health = { contract: contract.contract, revision: catalogueRevision, build: `data-${sha256(catalogueText).slice(0, 12)}`, builtAt };
  return `${JSON.stringify(health, null, 2)}\n`;
}

async function listFolder(folder) {
  try {
    return await readdir(folder, { withFileTypes: true });
  } catch (error) {
    if (error.code === "ENOENT") return null;
    throw error;
  }
}

/** Why an existing set folder differs from the files it must hold (byte for byte), or []. */
async function folderDifferences(folder, files) {
  const problems = [];
  const entries = await listFolder(folder);
  const expected = new Map(files.map((file) => [file.name, file]));
  for (const entry of entries) {
    if (entry.name.startsWith(".")) continue;
    if (!expected.has(entry.name)) problems.push(`${entry.name} is not part of this set`);
    else if (!entry.isFile() || entry.isSymbolicLink()) problems.push(`${entry.name} is not a regular file`);
  }
  for (const file of files) {
    let bytes;
    try {
      const stats = await lstat(join(folder, file.name));
      if (!stats.isFile()) continue;
      bytes = await readFile(join(folder, file.name));
    } catch (error) {
      if (error.code === "ENOENT") {
        problems.push(`${file.name} is missing`);
        continue;
      }
      throw error;
    }
    if (bytes.length !== file.byteSize || sha256(bytes) !== file.sha256) problems.push(`${file.name} differs from its Media V2 bytes (sha256 ${sha256(bytes).slice(0, 12)}…, expected ${file.sha256.slice(0, 12)}…)`);
  }
  return problems;
}

/** Copies one Admin-upload set into its folder through a hidden folder, so a crash never leaves half a set at its URL. */
async function writeSetFolder(publicDir, description) {
  const [, setId, fp12] = FOLDER.exec(description.folder);
  const parent = join(keysDir(publicDir), "sets", setId);
  await mkdir(parent, { recursive: true });
  const incoming = join(parent, `${INCOMING_PREFIX}${fp12}-${process.pid}-${randomUUID().slice(0, 8)}`);
  await mkdir(incoming);
  try {
    for (const file of description.files) {
      const target = join(incoming, file.name);
      await copyFile(file.source, target, constants.COPYFILE_EXCL);
      const copied = await readFile(target);
      if (copied.length !== file.byteSize || sha256(copied) !== file.sha256) throw new TypingFeelExportError(`Set ${setId}: the copy of ${file.name} does not match its Media V2 bytes.`);
    }
    await rename(incoming, join(parent, fp12));
  } catch (error) {
    await rm(incoming, { recursive: true, force: true });
    if (error?.code === "ENOTEMPTY" || error?.code === "EEXIST") {
      throw new TypingFeelExportError(`Set ${setId}: ${description.folder} appeared while it was being written; publish again to check it.`);
    }
    throw error;
  }
}

/**
 * Makes sure every shown set of `config` has its folder: an existing folder is
 * checked byte for byte (never rewritten; any difference is an error), a missing
 * Admin-upload folder is written from its blobs, a missing reference folder is an
 * error (its files come from Git and Drive: pnpm media:pull).
 * Returns { created, reused } folder lists. With `dryRun` nothing is written.
 */
export async function ensureSetFolders({ config, described, publicDir, dryRun = false }) {
  const created = [];
  const reused = [];
  const problems = [];
  const toWrite = [];
  for (const set of config.keyboard.sets.filter((entry) => entry.enabled)) {
    const description = described.get(set.id);
    const folder = join(keysDir(publicDir), ...description.folder.split("/"));
    if ((await listFolder(folder)) === null) {
      if (description.provenance !== "admin-upload") {
        problems.push(`Set ${set.id}: ${description.folder}/ is missing from the published folder; restore it with pnpm media:pull.`);
        continue;
      }
      toWrite.push(description);
      continue;
    }
    const differences = await folderDifferences(folder, description.files);
    if (differences.length) problems.push(`Set ${set.id}: ${description.folder}/ already exists with other content (set folders are never overwritten): ${differences.join("; ")}.`);
    else reused.push(description.folder);
  }
  if (problems.length) throw new TypingFeelExportError(problems);
  for (const description of toWrite) {
    if (!dryRun) await writeSetFolder(publicDir, description);
    created.push(description.folder);
  }
  return { created, reused };
}

const LEFTOVER_FILE = /^(?:keys-manifest|health)\.json\.\d+\.[0-9a-f-]{36}\.tmp$/;
const LEFTOVER_FOLDER = /^\.incoming-[0-9a-f]{12}-\d+-[0-9a-f]{8}$/;

/**
 * Removes what an export stopped half-way leaves behind: its own temporary
 * catalogue or health files and hidden .incoming- set folders (names only this
 * module writes). Runs at start-up, in the write queue, before any export.
 * Returns the removed paths, relative to the published folder.
 */
export async function removeExportLeftovers(publicDir) {
  const removed = [];
  for (const [dir, relative] of [[keysDir(publicDir), "v1/keys"], [join(publicDir, "v1"), "v1"]]) {
    for (const entry of (await listFolder(dir)) ?? []) {
      if (entry.isFile() && LEFTOVER_FILE.test(entry.name)) {
        await rm(join(dir, entry.name), { force: true });
        removed.push(`${relative}/${entry.name}`);
      }
    }
  }
  const setsDir = join(keysDir(publicDir), "sets");
  for (const set of (await listFolder(setsDir)) ?? []) {
    if (!set.isDirectory()) continue;
    for (const entry of (await listFolder(join(setsDir, set.name))) ?? []) {
      if (entry.isDirectory() && LEFTOVER_FOLDER.test(entry.name)) {
        await rm(join(setsDir, set.name, entry.name), { recursive: true, force: true });
        removed.push(`v1/keys/sets/${set.name}/${entry.name}`);
      }
    }
  }
  return removed;
}

/** Writes `text` to a new temporary file beside `file` and returns its path (the caller renames or removes it). */
export async function writeTemporary(file, text) {
  const temporary = `${file}.${process.pid}.${randomUUID()}.tmp`;
  await writeFile(temporary, text, { encoding: "utf8", flag: "wx" });
  return temporary;
}

export async function writeFileAtomic(file, text) {
  const temporary = await writeTemporary(file, text);
  try {
    await rename(temporary, file);
  } catch (error) {
    await rm(temporary, { force: true });
    throw error;
  }
}

export async function readTextOrNull(file) {
  try {
    return await readFile(file, "utf8");
  } catch (error) {
    if (error.code === "ENOENT") return null;
    throw error;
  }
}

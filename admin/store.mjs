import { createHash, randomUUID } from "node:crypto";
import { mkdir, readFile, readdir, rename, writeFile } from "node:fs/promises";
import { join } from "node:path";

export class AdminConflictError extends Error {}
export class AdminValidationError extends Error {}

function canonicalize(value) {
  if (Array.isArray(value)) return value.map(canonicalize);
  if (value !== null && typeof value === "object") {
    return Object.fromEntries(
      Object.keys(value)
        .sort()
        .map((key) => [key, canonicalize(value[key])]),
    );
  }
  return value;
}

function serialize(value) {
  return `${JSON.stringify(canonicalize(value), null, 2)}\n`;
}

async function readJson(path) {
  return JSON.parse(await readFile(path, "utf8"));
}

async function writeJsonAtomic(path, value) {
  const temporary = `${path}.${process.pid}.${randomUUID()}.tmp`;
  await writeFile(temporary, serialize(value), "utf8");
  await rename(temporary, path);
}

function object(value, path) {
  if (value === null || typeof value !== "object" || Array.isArray(value)) {
    throw new AdminValidationError(`${path} must be an object.`);
  }
  return value;
}

function string(value, path, { min = 1, max = 200, pattern } = {}) {
  if (typeof value !== "string" || value.length < min || value.length > max) {
    throw new AdminValidationError(`${path} must be a string between ${min} and ${max} characters.`);
  }
  if (pattern && !pattern.test(value)) {
    throw new AdminValidationError(`${path} has an invalid format.`);
  }
  return value;
}

function boolean(value, path) {
  if (typeof value !== "boolean") throw new AdminValidationError(`${path} must be boolean.`);
  return value;
}

function number(value, path, { min = Number.NEGATIVE_INFINITY, max = Number.POSITIVE_INFINITY } = {}) {
  if (typeof value !== "number" || !Number.isFinite(value) || value < min || value > max) {
    throw new AdminValidationError(`${path} must be a finite number between ${min} and ${max}.`);
  }
  return value;
}

function enumValue(value, path, allowed) {
  if (!allowed.includes(value)) {
    throw new AdminValidationError(`${path} must be one of: ${allowed.join(", ")}.`);
  }
  return value;
}

function rejectUnknownKeys(value, path, allowed) {
  for (const key of Object.keys(value)) {
    if (!allowed.includes(key)) throw new AdminValidationError(path + "." + key + " is not supported by the current canonical schema.");
  }
}

function validateTrackIds(value, path, { allowEmpty = true } = {}) {
  if (!Array.isArray(value)) throw new AdminValidationError(path + " must be an array.");
  if (!allowEmpty && value.length === 0) throw new AdminValidationError(path + " must contain at least one track id.");
  const seen = new Set();
  for (const [index, id] of value.entries()) {
    string(id, path + "[" + index + "]", { max: 160, pattern: /^[a-z0-9][a-z0-9._-]*$/ });
    if (seen.has(id)) throw new AdminValidationError(path + " contains duplicate track id " + id + ".");
    seen.add(id);
  }
}

function validatePlaylistAssignment(value, path) {
  object(value, path);
  rejectUnknownKeys(value, path, ["kind", "trackIds", "selectionMode"]);
  enumValue(value.kind, path + ".kind", ["inherit", "replace"]);
  if (value.kind === "inherit") {
    if (value.trackIds !== undefined || value.selectionMode !== undefined) {
      throw new AdminValidationError(path + " inherit assignments cannot include trackIds/selectionMode.");
    }
    return;
  }
  validateTrackIds(value.trackIds, path + ".trackIds", { allowEmpty: false });
  if (value.selectionMode !== undefined) {
    enumValue(value.selectionMode, path + ".selectionMode", ["shuffle-bag", "ordered"]);
  }
}

function validateWorldMusicEntry(value, path) {
  object(value, path);
  rejectUnknownKeys(value, path, ["normal", "boss"]);
  if (value.normal !== undefined) validatePlaylistAssignment(value.normal, path + ".normal");
  if (value.boss !== undefined) {
    const boss = object(value.boss, path + ".boss");
    rejectUnknownKeys(boss, path + ".boss", ["common", "mini", "world", "major"]);
    for (const key of ["common", "mini", "world", "major"]) {
      if (boss[key] !== undefined) validatePlaylistAssignment(boss[key], path + ".boss." + key);
    }
  }
}

function validateWorldMusic(worldMusic) {
  object(worldMusic, "worldMusic");
  string(worldMusic.policyRevision, "worldMusic.policyRevision", { max: 120, pattern: /^[a-z0-9][a-z0-9._-]*$/ });
  object(worldMusic.assignments, "worldMusic.assignments");
  if (worldMusic.publishedPolicy === undefined) return;
  const policy = object(worldMusic.publishedPolicy, "worldMusic.publishedPolicy");
  rejectUnknownKeys(policy, "worldMusic.publishedPolicy", ["configRevision", "disabledTrackIds", "worlds", "global"]);
  string(policy.configRevision, "worldMusic.publishedPolicy.configRevision", { max: 160, pattern: /^[a-zA-Z0-9][a-zA-Z0-9._-]*$/ });
  if (policy.disabledTrackIds !== undefined) validateTrackIds(policy.disabledTrackIds, "worldMusic.publishedPolicy.disabledTrackIds");
  if (policy.global !== undefined) validateWorldMusicEntry(policy.global, "worldMusic.publishedPolicy.global");
  if (policy.worlds !== undefined) {
    const worlds = object(policy.worlds, "worldMusic.publishedPolicy.worlds");
    for (const [worldId, entry] of Object.entries(worlds)) {
      string(worldId, "worldMusic world id", { max: 8, pattern: /^world-(?:0[1-9]|[1-4]\d|50)$/ });
      validateWorldMusicEntry(entry, "worldMusic.publishedPolicy.worlds." + worldId);
    }
  }
}

function validateAudio(audio) {
  object(audio, "audio");
  string(audio.profileId, "audio.profileId", { max: 80, pattern: /^[a-z0-9][a-z0-9-]*$/ });
  const defaults = object(audio.defaults, "audio.defaults");
  for (const key of ["master", "pronunciation", "music", "ambient", "sfx", "announcer"]) {
    number(defaults[key], `audio.defaults.${key}`, { min: 0, max: 1 });
  }
  if (defaults.credit !== undefined) number(defaults.credit, "audio.defaults.credit", { min: 0, max: 2 });
  if (defaults.categories !== undefined) {
    const categories = object(defaults.categories, "audio.defaults.categories");
    for (const key of ["typing", "combat", "warnings", "ui", "rewards"]) {
      number(categories[key], `audio.defaults.categories.${key}`, { min: 0, max: 1 });
    }
  }
}

function validateSystem(system) {
  object(system, "system");
  const gameDefaults = object(system.gameDefaults, "system.gameDefaults");
  enumValue(gameDefaults.defaultMode, "system.gameDefaults.defaultMode", ["campaign", "recall", "expedition"]);
  string(gameDefaults.defaultShip, "system.gameDefaults.defaultShip", { max: 80, pattern: /^[a-z0-9][a-z0-9-]*$/ });
  enumValue(gameDefaults.difficulty, "system.gameDefaults.difficulty", ["easy", "normal", "hard"]);
  boolean(gameDefaults.tutorialEnabled, "system.gameDefaults.tutorialEnabled");
  boolean(gameDefaults.pronunciationDefault, "system.gameDefaults.pronunciationDefault");
  boolean(gameDefaults.autoSave, "system.gameDefaults.autoSave");

  const network = object(system.network, "system.network");
  string(network.minimumVersion, "system.network.minimumVersion", { max: 40, pattern: /^\d+\.\d+\.\d+(?:[-+][0-9A-Za-z.-]+)?$/ });
  number(network.autoSaveIntervalSeconds, "system.network.autoSaveIntervalSeconds", { min: 5, max: 3600 });
  number(network.reconnectWindowSeconds, "system.network.reconnectWindowSeconds", { min: 1, max: 600 });
  boolean(network.offlinePlay, "system.network.offlinePlay");
  boolean(network.telemetry, "system.network.telemetry");

  const maintenance = object(system.maintenance, "system.maintenance");
  boolean(maintenance.enabled, "system.maintenance.enabled");
  string(maintenance.message, "system.maintenance.message", { min: 0, max: 500 });
}

function validateFeatureFlags(featureFlags) {
  object(featureFlags, "featureFlags");
  const scopes = ["all", "new-players", "cohort", "environment", "accounts"];
  const risks = ["normal", "economy", "competitive", "save"];
  for (const [id, flag] of Object.entries(featureFlags)) {
    string(id, "featureFlags id", { max: 100, pattern: /^[a-z0-9][a-z0-9-]*$/ });
    object(flag, `featureFlags.${id}`);
    boolean(flag.enabled, `featureFlags.${id}.enabled`);
    number(flag.rolloutPercent, `featureFlags.${id}.rolloutPercent`, { min: 0, max: 100 });
    enumValue(flag.scope, `featureFlags.${id}.scope`, scopes);
    enumValue(flag.risk, `featureFlags.${id}.risk`, risks);
  }
}

export class RevisionStore {
  constructor({ rootDir, contract, now = () => new Date() }) {
    this.rootDir = rootDir;
    this.contract = contract;
    this.now = now;
    this.revisionsDir = join(rootDir, "revisions");
    this.statePath = join(rootDir, "state.json");
  }

  validateConfig(config) {
    if (config === null || typeof config !== "object" || Array.isArray(config)) {
      throw new AdminValidationError("Config must be an object.");
    }
    const required = [
      ["contractRevision", this.contract.contractRevision],
      ["configSchemaVersion", this.contract.configSchemaVersion],
      ["worldMusicCatalogSchemaVersion", this.contract.worldMusicCatalogSchemaVersion],
    ];
    for (const [key, expected] of required) {
      if (config[key] !== expected) {
        throw new AdminValidationError(`${key} must equal ${JSON.stringify(expected)}.`);
      }
    }
    validateAudio(config.audio);
    validateWorldMusic(config.worldMusic);

    // Phase B namespaces are additive to v1 so existing local revisions remain readable.
    // Once present, they are strictly validated before a revision can be written/published.
    if (config.system !== undefined) validateSystem(config.system);
    if (config.featureFlags !== undefined) validateFeatureFlags(config.featureFlags);
    return config;
  }

  async initialize(seedConfig) {
    this.validateConfig(seedConfig);
    await mkdir(this.revisionsDir, { recursive: true });
    try {
      return await this.getState();
    } catch (error) {
      if (error?.code !== "ENOENT") throw error;
    }

    const revision = {
      revision: "seed-v1",
      parentRevision: null,
      createdAt: this.now().toISOString(),
      author: "system",
      message: "Initial Space Typing Admin seed",
      config: structuredClone(seedConfig),
    };
    const revisionPath = this.revisionPath(revision.revision);
    try {
      await writeFile(revisionPath, serialize(revision), { encoding: "utf8", flag: "wx" });
    } catch (error) {
      if (error?.code !== "EEXIST") throw error;
    }

    const state = {
      version: 1,
      activeRevision: revision.revision,
      generation: 1,
      updatedAt: this.now().toISOString(),
    };
    await writeJsonAtomic(this.statePath, state);
    return state;
  }

  revisionPath(revision) {
    if (!/^[a-zA-Z0-9._-]+$/.test(revision)) {
      throw new AdminValidationError("Invalid revision id.");
    }
    return join(this.revisionsDir, `${revision}.json`);
  }

  async getState() {
    return readJson(this.statePath);
  }

  async getRevision(revision) {
    return readJson(this.revisionPath(revision));
  }

  async getActiveRevision() {
    const state = await this.getState();
    return this.getRevision(state.activeRevision);
  }

  async getRuntimeConfig() {
    const active = await this.getActiveRevision();
    return structuredClone(active.config);
  }

  async listRevisions() {
    const state = await this.getState();
    const names = (await readdir(this.revisionsDir)).filter((name) => name.endsWith(".json"));
    const revisions = await Promise.all(
      names.map((name) => readJson(join(this.revisionsDir, name))),
    );
    return revisions
      .sort((a, b) => b.createdAt.localeCompare(a.createdAt))
      .map((revision) => ({
        ...revision,
        active: revision.revision === state.activeRevision,
      }));
  }

  async createRevision({ baseRevision, config, author = "local-admin", message = "Admin draft" }) {
    this.validateConfig(config);
    await this.getRevision(baseRevision);
    const createdAt = this.now().toISOString();
    const digest = createHash("sha256")
      .update(`${baseRevision}\n${createdAt}\n${randomUUID()}\n${serialize(config)}`)
      .digest("hex")
      .slice(0, 12);
    const revision = {
      revision: `r-${createdAt.replace(/[-:.TZ]/g, "").slice(0, 14)}-${digest}`,
      parentRevision: baseRevision,
      createdAt,
      author,
      message,
      config: structuredClone(config),
    };
    await writeFile(this.revisionPath(revision.revision), serialize(revision), {
      encoding: "utf8",
      flag: "wx",
    });
    return revision;
  }

  async publish({ revision, expectedActiveRevision }) {
    const state = await this.getState();
    if (state.activeRevision !== expectedActiveRevision) {
      throw new AdminConflictError(
        `Active revision changed from ${expectedActiveRevision} to ${state.activeRevision}.`,
      );
    }
    const target = await this.getRevision(revision);
    this.validateConfig(target.config);
    const nextState = {
      version: 1,
      activeRevision: revision,
      generation: state.generation + 1,
      updatedAt: this.now().toISOString(),
    };
    await writeJsonAtomic(this.statePath, nextState);
    return nextState;
  }

  async rollback({ targetRevision, expectedActiveRevision }) {
    return this.publish({ revision: targetRevision, expectedActiveRevision });
  }
}

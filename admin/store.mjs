import { createHash, randomUUID } from "node:crypto";
import { mkdir, readFile, readdir, rename, writeFile } from "node:fs/promises";
import { join } from "node:path";

export class AdminConflictError extends Error {}
export class AdminValidationError extends Error {}

const AUDIO_VOLUME_KEYS = ["master", "pronunciation", "music", "ambient", "sfx", "announcer"];
const WORLD_ID_PATTERN = /^world-(0[1-9]|[1-4][0-9]|50)$/;
const PLAYLIST_SELECTION_MODES = new Set(["shuffle-bag", "ordered"]);

function isObject(value) {
  return value !== null && typeof value === "object" && !Array.isArray(value);
}

function validateAssignment(value, label) {
  if (value === undefined) return;
  if (!isObject(value)) throw new AdminValidationError(`${label} must be an object.`);
  if (value.kind === "inherit") return;
  if (value.kind !== "replace") {
    throw new AdminValidationError(`${label}.kind must be inherit or replace.`);
  }
  if (!Array.isArray(value.trackIds) || value.trackIds.length === 0) {
    throw new AdminValidationError(`${label}.trackIds must contain at least one track id.`);
  }
  if (value.trackIds.some((id) => typeof id !== "string" || id.trim().length === 0)) {
    throw new AdminValidationError(`${label}.trackIds must contain non-empty strings.`);
  }
  if (new Set(value.trackIds).size !== value.trackIds.length) {
    throw new AdminValidationError(`${label}.trackIds must not contain duplicates.`);
  }
  if (value.selectionMode !== undefined && !PLAYLIST_SELECTION_MODES.has(value.selectionMode)) {
    throw new AdminValidationError(`${label}.selectionMode must be shuffle-bag or ordered.`);
  }
}

function validatePolicyEntry(entry, label) {
  if (!isObject(entry)) throw new AdminValidationError(`${label} must be an object.`);
  validateAssignment(entry.normal, `${label}.normal`);
  if (entry.boss !== undefined) {
    if (!isObject(entry.boss)) throw new AdminValidationError(`${label}.boss must be an object.`);
    validateAssignment(entry.boss.common, `${label}.boss.common`);
    validateAssignment(entry.boss.mini, `${label}.boss.mini`);
    validateAssignment(entry.boss.world, `${label}.boss.world`);
    validateAssignment(entry.boss.major, `${label}.boss.major`);
  }
}

function validateWorldMusicPolicy(policy) {
  if (!isObject(policy)) throw new AdminValidationError("worldMusic.publishedPolicy must be an object.");
  if (typeof policy.configRevision !== "string" || policy.configRevision.trim().length === 0) {
    throw new AdminValidationError("worldMusic.publishedPolicy.configRevision is required.");
  }
  if (policy.disabledTrackIds !== undefined) {
    if (!Array.isArray(policy.disabledTrackIds) || policy.disabledTrackIds.some((id) => typeof id !== "string" || id.trim().length === 0)) {
      throw new AdminValidationError("worldMusic.publishedPolicy.disabledTrackIds must contain non-empty strings.");
    }
    if (new Set(policy.disabledTrackIds).size !== policy.disabledTrackIds.length) {
      throw new AdminValidationError("worldMusic.publishedPolicy.disabledTrackIds must not contain duplicates.");
    }
  }
  if (policy.worlds !== undefined) {
    if (!isObject(policy.worlds)) throw new AdminValidationError("worldMusic.publishedPolicy.worlds must be an object.");
    for (const [worldId, entry] of Object.entries(policy.worlds)) {
      if (!WORLD_ID_PATTERN.test(worldId)) {
        throw new AdminValidationError(`Unknown World id in published policy: ${worldId}.`);
      }
      validatePolicyEntry(entry, `worldMusic.publishedPolicy.worlds.${worldId}`);
    }
  }
  if (policy.global !== undefined) validatePolicyEntry(policy.global, "worldMusic.publishedPolicy.global");
}

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
    if (!isObject(config.audio)) {
      throw new AdminValidationError("audio config is required.");
    }
    if (typeof config.audio.profileId !== "string" || config.audio.profileId.trim().length === 0) {
      throw new AdminValidationError("audio.profileId is required.");
    }
    if (!isObject(config.audio.defaults)) {
      throw new AdminValidationError("audio.defaults is required.");
    }
    for (const key of AUDIO_VOLUME_KEYS) {
      const value = config.audio.defaults[key];
      if (typeof value !== "number" || !Number.isFinite(value) || value < 0 || value > 1) {
        throw new AdminValidationError(`audio.defaults.${key} must be between 0 and 1.`);
      }
    }
    if (!isObject(config.worldMusic)) {
      throw new AdminValidationError("worldMusic config is required.");
    }
    if (typeof config.worldMusic.policyRevision !== "string" || config.worldMusic.policyRevision.trim().length === 0) {
      throw new AdminValidationError("worldMusic.policyRevision is required.");
    }
    if (config.worldMusic.assignments !== undefined && !isObject(config.worldMusic.assignments)) {
      throw new AdminValidationError("worldMusic.assignments must be an object when present.");
    }
    if (config.worldMusic.publishedPolicy !== undefined) {
      validateWorldMusicPolicy(config.worldMusic.publishedPolicy);
      if (config.worldMusic.policyRevision !== config.worldMusic.publishedPolicy.configRevision) {
        throw new AdminValidationError("worldMusic.policyRevision must match publishedPolicy.configRevision.");
      }
    }
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

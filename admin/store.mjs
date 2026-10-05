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
    if (config.audio === null || typeof config.audio !== "object") {
      throw new AdminValidationError("audio config is required.");
    }
    if (config.worldMusic === null || typeof config.worldMusic !== "object") {
      throw new AdminValidationError("worldMusic config is required.");
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

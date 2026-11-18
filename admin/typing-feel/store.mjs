// Typing Feel revision store (docs/games/TYPING_FEEL_SERVICE.md §3.3).
// Own revisions, state and publication records under TYPING_GAME_ADMIN_SHARED_DIR
// (default .local/admin/shared/typing-feel/), apart from the Space Typing config,
// so a Space draft never blocks a Typing Feel Publish and a Space Rollback never
// rolls back every game's keyboard sounds.
import { AsyncLocalStorage } from "node:async_hooks";
import { randomUUID } from "node:crypto";
import { link, mkdir, readdir, readFile, rm, writeFile } from "node:fs/promises";
import { basename, join, resolve } from "node:path";
import { loadContract } from "../../typing-feel/tools/import-staging.mjs";
import { AdminValidationError, RevisionStore } from "../store.mjs";
import { validateTypingFeelConfig } from "./policy.mjs";

export const TYPING_FEEL_SEED_MESSAGE = "Typing Feel seed";
export const PUBLICATION_SCHEMA = "typing-feel-publication/1";

// One write queue per store folder for the whole process: Save draft, Accept,
// Publish, Rollback and the start-up re-export all run one at a time, so two
// Publishes can never both pass the expectedActiveRevision check. Re-entrant
// inside one async call chain.
const queueTails = new Map();
const heldQueues = new AsyncLocalStorage();

export function runTypingFeelExclusive(rootDir, operation) {
  const key = resolve(rootDir);
  const held = heldQueues.getStore();
  if (held?.has(key)) return Promise.resolve().then(operation);
  const run = () => heldQueues.run(new Set([...(held ?? []), key]), operation);
  const next = (queueTails.get(key) ?? Promise.resolve()).then(run, run);
  const settled = next.then(() => undefined, () => undefined);
  queueTails.set(key, settled);
  settled.then(() => {
    if (queueTails.get(key) === settled) queueTails.delete(key);
  });
  return next;
}

function serialize(value) {
  return `${JSON.stringify(value, null, 2)}\n`;
}

export class TypingFeelRevisionStore extends RevisionStore {
  constructor({ rootDir, contract = loadContract(), now = () => new Date(), seedMessage = TYPING_FEEL_SEED_MESSAGE } = {}) {
    if (!rootDir) throw new TypeError("TypingFeelRevisionStore requires rootDir.");
    super({ rootDir, contract, now, seedMessage });
    this.publicationsDir = join(rootDir, "publications");
  }

  /** typing-feel-admin/1 only; the Space Typing checks never run here. */
  validateConfig(config) {
    return validateTypingFeelConfig(config, this.contract);
  }

  /** Runs `operation` in this store's write queue (every Typing Feel write goes through it). */
  exclusive(operation) {
    return runTypingFeelExclusive(this.rootDir, operation);
  }

  /** True once a seed (import or restore) has written state.json. Reads only. */
  async isInitialized() {
    try {
      await this.getState();
      return true;
    } catch (error) {
      if (error?.code === "ENOENT") return false;
      throw error;
    }
  }

  async hasRevision(revision) {
    try {
      await this.getRevision(revision);
      return true;
    } catch (error) {
      if (error?.code === "ENOENT") return false;
      throw error;
    }
  }

  publicationPath(revision) {
    return join(this.publicationsDir, basename(this.revisionPath(revision)));
  }

  /**
   * The catalogue identity of a revision once it has been published:
   * { revision, catalogueRevision, publishedAt, builtAt }. The seed keeps the
   * G1 catalogue's "r1" and its times, so exporting it again gives the same bytes.
   */
  async getPublication(revision) {
    try {
      return JSON.parse(await readFile(this.publicationPath(revision), "utf8"));
    } catch (error) {
      if (error?.code === "ENOENT") return null;
      throw error;
    }
  }

  /**
   * Writes a publication record once. Returns true when written, false when an
   * equal record already exists. The record appears whole or not at all (a temp
   * file hard-linked into place, which also refuses an existing record), so a
   * stop mid-write never leaves a torn record that listPublications cannot read.
   */
  async writePublication({ revision, catalogueRevision, publishedAt, builtAt }) {
    const record = { schema: PUBLICATION_SCHEMA, revision, catalogueRevision, publishedAt, builtAt };
    const target = this.publicationPath(revision);
    await mkdir(this.publicationsDir, { recursive: true });
    const temporary = `${target}.${process.pid}.${randomUUID()}.tmp`;
    await writeFile(temporary, serialize(record), { encoding: "utf8", flag: "wx" });
    try {
      await link(temporary, target);
      return true;
    } catch (error) {
      if (error?.code !== "EEXIST") throw error;
      const existing = await this.getPublication(revision);
      if (JSON.stringify(existing) !== JSON.stringify(record)) {
        throw new AdminValidationError(`Revision ${revision} was already published as ${existing?.catalogueRevision} at ${existing?.publishedAt}.`);
      }
      return false;
    } finally {
      await rm(temporary, { force: true });
    }
  }

  async removePublication(revision) {
    await rm(this.publicationPath(revision), { force: true });
  }

  async listPublications() {
    let names;
    try {
      names = (await readdir(this.publicationsDir)).filter((name) => name.endsWith(".json"));
    } catch (error) {
      if (error?.code === "ENOENT") return [];
      throw error;
    }
    return Promise.all(names.map(async (name) => JSON.parse(await readFile(join(this.publicationsDir, name), "utf8"))));
  }

  /** Every id retired in any revision that was ever published: reserved forever (§3.4). */
  async reservedRetiredIds() {
    const reserved = new Set();
    for (const publication of await this.listPublications()) {
      try {
        const revision = await this.getRevision(publication.revision);
        for (const id of revision.config?.keyboard?.retiredIds ?? []) reserved.add(id);
      } catch (error) {
        if (error?.code !== "ENOENT") throw error;
      }
    }
    return [...reserved].sort();
  }

  /**
   * Every set id of every revision that was ever published, with the Media versions
   * it was published with (§3.13: ids are fixed). A Rollback can take an id out of the
   * live catalogue, but players who picked it keep it in their saves, so the id never
   * names a different sound later. Returns Map<setId, Set<assetVersionId>>.
   */
  async publishedSetVersions() {
    const published = new Map();
    for (const publication of await this.listPublications()) {
      try {
        const revision = await this.getRevision(publication.revision);
        for (const set of revision.config?.keyboard?.sets ?? []) {
          if (typeof set?.id !== "string") continue;
          if (!published.has(set.id)) published.set(set.id, new Set());
          if (typeof set.assetVersionId === "string") published.get(set.id).add(set.assetVersionId);
        }
      } catch (error) {
        if (error?.code !== "ENOENT") throw error;
      }
    }
    return published;
  }
}

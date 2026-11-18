// Typing Feel Admin service: Draft → Validate → Publish → Rollback for every
// game's keyboard sounds and typing defaults (docs/games/TYPING_FEEL_SERVICE.md
// §3.3, §3.11, §3.12). Every write runs in the store's single queue; Media V2
// writes take the shared registry lock inside it (queue first, lock second).
import { execFile } from "node:child_process";
import { lstat, mkdir, readFile, realpath, rename, rm } from "node:fs/promises";
import { dirname, isAbsolute, join, relative, sep } from "node:path";
import { sha256 } from "../../typing-feel/tools/import-staging.mjs";
import { AdminConflictError, AdminValidationError } from "../store.mjs";
import { describeTypingFeelChangeScope } from "./change-scope.mjs";
import {
  TypingFeelExportError,
  buildCatalogue,
  catalogueFile,
  catalogueProblems,
  describeConfigSets,
  ensureSetFolders,
  healthFile,
  healthText,
  isoSeconds,
  keysDir,
  readTextOrNull,
  removeExportLeftovers,
  SET_TAGS,
  writeFileAtomic,
  writeTemporary,
} from "./export.mjs";
import { TypingFeelValidationError, baseProblems, configProblems } from "./policy.mjs";

export const REFERENCE_DOMAIN = "typing-feel.keyboard";
export const SOURCE_REFERENCE_DOMAIN = "typing-feel.source";
export const IMPORT_COMMAND = "node admin/typing-feel/import-staging.mjs ~/AudioLab/review/staging/keys-firefly --public typing-feel/public";
export const RESTORE_COMMAND = "node admin/typing-feel/import-staging.mjs --restore --public typing-feel/public";
export const DEPLOY_COMMAND = "pnpm feel:deploy";
export const BACKUP_COMMAND = "pnpm media:push";

export class TypingFeelNotReadyError extends Error {
  constructor(message = `Typing Feel is not imported yet. Run ${IMPORT_COMMAND} once (or ${RESTORE_COMMAND} on a fresh clone).`) {
    super(message);
    this.name = "TypingFeelNotReadyError";
  }
}

export class TypingFeelNotFoundError extends Error {
  constructor(message) {
    super(message);
    this.name = "TypingFeelNotFoundError";
  }
}

const PREVIEW_CACHE_MS = 5000;

function mimeFor(name) {
  if (name.endsWith(".json")) return "application/json; charset=utf-8";
  if (name.endsWith(".ogg")) return "audio/ogg";
  return "application/octet-stream";
}

export class TypingFeelService {
  constructor({ store, mediaStore, publicDir, repoRoot = null, contract = store.contract, now = () => new Date() }) {
    if (!store || !mediaStore || !publicDir) throw new TypeError("TypingFeelService requires store, mediaStore and publicDir.");
    this.store = store;
    this.mediaStore = mediaStore;
    this.publicDir = publicDir;
    this.repoRoot = repoRoot;
    this.contract = contract;
    this.now = now;
    this.previewCache = new Map();
  }

  get catalogueFile() {
    return catalogueFile(this.publicDir);
  }

  get healthFile() {
    return healthFile(this.publicDir);
  }

  async requireInitialized() {
    if (!(await this.store.isInitialized())) throw new TypingFeelNotReadyError();
  }

  async revision(revisionId) {
    if (typeof revisionId !== "string" || !revisionId) throw new AdminValidationError("A revision id is required.");
    try {
      return await this.store.getRevision(revisionId);
    } catch (error) {
      if (error?.code === "ENOENT") throw new TypingFeelNotFoundError(`Revision ${revisionId} does not exist.`);
      throw error;
    }
  }

  /**
   * Schema, draft-against-base and Media checks of one config.
   * Returns { problems, described } (described: Map setId → set version description).
   */
  async checkConfig(config, { baseConfig = null } = {}) {
    const problems = configProblems(config, this.contract);
    if (problems.length) return { problems, described: new Map() };
    if (baseConfig) problems.push(...baseProblems(config, baseConfig, { reservedIds: await this.store.reservedRetiredIds(), publishedVersions: await this.store.publishedSetVersions() }));
    const { described, problems: media } = await describeConfigSets({ config, mediaStore: this.mediaStore, publicDir: this.publicDir, contract: this.contract, baseConfig });
    problems.push(...media);
    return { problems, described };
  }

  /** The catalogue and health text of `config` under `publication`; throws when the result breaks the contract. */
  buildExport(config, described, publication) {
    const { catalogue, text } = buildCatalogue({ config, described, catalogueRevision: publication.catalogueRevision, publishedAt: publication.publishedAt, contract: this.contract });
    const problems = catalogueProblems(catalogue, this.contract);
    if (problems.length) throw new TypingFeelExportError(problems);
    return { catalogue, text, health: healthText({ catalogueText: text, catalogueRevision: publication.catalogueRevision, builtAt: publication.builtAt, contract: this.contract }) };
  }

  newPublication(revisionId) {
    const stamp = isoSeconds(this.now());
    return { revision: revisionId, catalogueRevision: revisionId, publishedAt: stamp, builtAt: stamp };
  }

  /**
   * Media V2 references of one published revision (§3.6): every set's version,
   * and the source WAV of an Admin-made set, so neither can be hard-deleted and
   * the Media Library shows where they are used. Idempotent.
   */
  async addReferences(revisionId, config, described, actorId = "local-admin") {
    const inputs = [];
    for (const set of config.keyboard.sets) {
      const description = described.get(set.id);
      inputs.push({ assetId: description.assetId, assetVersionId: set.assetVersionId, domain: REFERENCE_DOMAIN, entityType: "keyboard-set", entityId: set.id, field: "assetVersionId", revisionId });
      if (description.sourceAssetVersionId) {
        try {
          const source = await this.mediaStore.getVersion(description.sourceAssetVersionId);
          inputs.push({ assetId: source.assetId, assetVersionId: source.assetVersionId, domain: SOURCE_REFERENCE_DOMAIN, entityType: "keyboard-set", entityId: set.id, field: "sourceAssetVersionId", revisionId });
        } catch {
          // A source that is not in Media V2 (a restored machine) has nothing to protect.
        }
      }
    }
    const { created } = await this.mediaStore.addReferences(inputs, { actorId });
    return created;
  }

  /**
   * Accept (§3.8, G7): stores one formatted set as an immutable Media V2 bundle
   * version, in the Typing Feel write queue. Changes no revision and nothing the
   * games read; a draft then points a set at the returned version.
   */
  acceptSetBundle({ assetId = null, title, components, source = {}, actorId = "local-admin" }) {
    return this.store.exclusive(() => (assetId
      ? this.mediaStore.createUploadBundleVersion({ assetId, components, source, actorId })
      : this.mediaStore.createUploadBundleAsset({ kind: "audio", title, tags: [...SET_TAGS], components, source, actorId })));
  }

  async ancestors(revisionId) {
    const chain = [];
    let cursor = await this.revision(revisionId);
    while (cursor.parentRevision) {
      chain.push(cursor.parentRevision);
      cursor = await this.revision(cursor.parentRevision);
    }
    return chain;
  }

  /**
   * Writes the export of an already checked revision, switching the store pointer
   * with `activate` between temp and rename (§3.12). The publication record is
   * written only after the switch: a stop before it leaves no record for a
   * revision that never went live (a record reserves its retired ids for ever),
   * and a stop after it is repaired at start-up, which writes the missing record
   * and exports again.
   */
  async #exportAndActivate({ revisionId, config, described, activate, actorId }) {
    const existing = await this.store.getPublication(revisionId);
    const publication = existing ?? this.newPublication(revisionId);
    const exported = this.buildExport(config, described, publication);
    const folders = await ensureSetFolders({ config, described, publicDir: this.publicDir });
    await mkdir(keysDir(this.publicDir), { recursive: true });
    const temporary = await writeTemporary(this.catalogueFile, exported.text);
    let state;
    try {
      state = await activate();
      if (!existing) await this.store.writePublication(publication);
    } catch (error) {
      await rm(temporary, { force: true });
      throw error;
    }
    await rename(temporary, this.catalogueFile);
    await writeFileAtomic(this.healthFile, exported.health);
    const references = await this.addReferences(revisionId, config, described, actorId);
    this.previewCache.clear();
    return {
      state,
      catalogue: { revision: publication.catalogueRevision, publishedAt: publication.publishedAt, sets: exported.catalogue.profiles.length, families: exported.catalogue.families.length, default: exported.catalogue.default, sha256: sha256(exported.text) },
      folders,
      referencesCreated: references,
    };
  }

  saveDraft({ baseRevision, config, message = "Typing Feel draft", author = "local-admin" }) {
    return this.store.exclusive(async () => {
      await this.requireInitialized();
      const base = await this.revision(baseRevision);
      const { problems } = await this.checkConfig(config, { baseConfig: base.config });
      if (problems.length) throw new TypingFeelValidationError(problems);
      return this.store.createRevision({ baseRevision, config, author, message: typeof message === "string" && message.trim() ? message.trim().slice(0, 200) : "Typing Feel draft" });
    });
  }

  async changeScope(revisionId) {
    const target = await this.revision(revisionId);
    const base = target.parentRevision ? await this.revision(target.parentRevision) : null;
    return describeTypingFeelChangeScope({ baseRevision: base?.revision ?? null, targetRevision: target.revision, baseConfig: base?.config ?? {}, targetConfig: target.config });
  }

  async rollbackChangeScope(targetRevision) {
    const state = await this.store.getState();
    const active = await this.revision(state.activeRevision);
    const target = await this.revision(targetRevision);
    return describeTypingFeelChangeScope({ baseRevision: active.revision, targetRevision: target.revision, baseConfig: active.config, targetConfig: target.config });
  }

  /** Validate and Review (read only): problems, change scope, the catalogue it would publish and the folders it would write. */
  async validate(revisionId) {
    await this.requireInitialized();
    const target = await this.revision(revisionId);
    const history = await this.store.listRevisions();
    const entry = history.find((candidate) => candidate.revision === revisionId);
    const state = await this.store.getState();
    const base = target.parentRevision ? await this.revision(target.parentRevision) : null;
    const isDraft = entry.relation === "draft";
    const { problems, described } = await this.checkConfig(target.config, { baseConfig: isDraft ? base?.config ?? null : null });
    let catalogue = null;
    let plan = null;
    if (problems.length === 0) {
      const publication = (await this.store.getPublication(revisionId)) ?? { catalogueRevision: revisionId, publishedAt: isoSeconds(target.createdAt), builtAt: isoSeconds(target.createdAt) };
      try {
        const exported = this.buildExport(target.config, described, publication);
        catalogue = { revision: exported.catalogue.revision, default: exported.catalogue.default, families: exported.catalogue.families.length, sets: exported.catalogue.profiles.length, hidden: target.config.keyboard.sets.filter((set) => !set.enabled).map((set) => set.id) };
        plan = await ensureSetFolders({ config: target.config, described, publicDir: this.publicDir, dryRun: true });
      } catch (error) {
        if (!(error instanceof TypingFeelExportError)) throw error;
        problems.push(...error.problems);
      }
    }
    const valid = problems.length === 0;
    return {
      revision: revisionId,
      valid,
      problems,
      activeRevision: state.activeRevision,
      parentRevision: target.parentRevision,
      relation: entry.relation,
      publishable: valid && entry.publishable,
      rollbackEligible: valid && entry.rollbackEligible,
      changeScope: await this.changeScope(revisionId),
      catalogue,
      plan,
      previewBase: `/api/runtime/typing-feel/preview/${encodeURIComponent(revisionId)}/keys/`,
    };
  }

  publish({ revision, expectedActiveRevision, actorId = "local-admin" }) {
    return this.store.exclusive(async () => {
      await this.requireInitialized();
      const state = await this.store.getState();
      if (state.activeRevision !== expectedActiveRevision) {
        throw new AdminConflictError(`Active revision changed from ${expectedActiveRevision} to ${state.activeRevision}.`);
      }
      const target = await this.revision(revision);
      if (target.parentRevision !== state.activeRevision) {
        throw new AdminConflictError(`Revision ${revision} was based on ${target.parentRevision ?? "no parent"}; active revision is ${state.activeRevision}. Create a fresh draft before publishing.`);
      }
      const base = await this.revision(target.parentRevision);
      const { problems, described } = await this.checkConfig(target.config, { baseConfig: base.config });
      if (problems.length) throw new TypingFeelValidationError(problems);
      return this.#exportAndActivate({
        revisionId: revision,
        config: target.config,
        described,
        actorId,
        activate: () => this.store.publish({ revision, expectedActiveRevision }),
      });
    });
  }

  rollback({ targetRevision, expectedActiveRevision, actorId = "local-admin" }) {
    return this.store.exclusive(async () => {
      await this.requireInitialized();
      const state = await this.store.getState();
      if (state.activeRevision !== expectedActiveRevision) {
        throw new AdminConflictError(`Active revision changed from ${expectedActiveRevision} to ${state.activeRevision}.`);
      }
      if (!(await this.ancestors(state.activeRevision)).includes(targetRevision)) {
        throw new AdminValidationError(`Rollback target ${targetRevision} must be a published ancestor of active revision ${state.activeRevision}.`);
      }
      const target = await this.revision(targetRevision);
      // A rollback restores a revision that was live before: only its files and Media are checked again.
      const { problems, described } = await this.checkConfig(target.config);
      if (problems.length) throw new TypingFeelValidationError(problems);
      return this.#exportAndActivate({
        revisionId: targetRevision,
        config: target.config,
        described,
        actorId,
        activate: () => this.store.rollback({ targetRevision, expectedActiveRevision }),
      });
    });
  }

  /**
   * Start-up (§3.12): when the catalogue on disk is not the active revision's
   * export, export it again; re-add Media V2 references a stop between rename
   * and references left out. Never runs before a seed exists.
   */
  async syncOnStartup() {
    if (!(await this.store.isInitialized())) return { status: "not-initialized" };
    return this.store.exclusive(async () => {
      const leftovers = await removeExportLeftovers(this.publicDir);
      const state = await this.store.getState();
      const active = await this.revision(state.activeRevision);
      const { problems, described } = await this.checkConfig(active.config);
      if (problems.length) {
        if (problems.some((problem) => /Media V2 version \S+ is unknown/.test(problem))) {
          problems.push(`If the Media V2 registry (${this.mediaStore.registryPath}) was reset or lost, move the Typing Feel store folder (${this.store.rootDir}) aside, run ${RESTORE_COMMAND} and restart the Admin service (docs/games/TYPING_FEEL_SERVICE.md §6.3).`);
        }
        return { status: "error", activeRevision: active.revision, problems, leftovers };
      }
      let publication = await this.store.getPublication(active.revision);
      let recordWritten = false;
      if (!publication) {
        publication = this.newPublication(active.revision);
        recordWritten = await this.store.writePublication(publication);
      }
      let exported;
      try {
        exported = this.buildExport(active.config, described, publication);
      } catch (error) {
        if (error instanceof TypingFeelExportError) return { status: "error", activeRevision: active.revision, problems: error.problems };
        throw error;
      }
      const onDisk = await readTextOrNull(this.catalogueFile);
      const healthOnDisk = await readTextOrNull(this.healthFile);
      if (onDisk === exported.text) {
        const healthWritten = healthOnDisk !== exported.health;
        if (healthWritten) await writeFileAtomic(this.healthFile, exported.health);
        const referencesCreated = await this.addReferences(active.revision, active.config, described, "system");
        return { status: "in-sync", activeRevision: active.revision, catalogueRevision: publication.catalogueRevision, healthWritten, referencesCreated, recordWritten, leftovers };
      }
      let previous = null;
      try {
        previous = onDisk === null ? null : JSON.parse(onDisk).revision ?? null;
      } catch {
        previous = "unreadable";
      }
      let folders;
      try {
        folders = await ensureSetFolders({ config: active.config, described, publicDir: this.publicDir });
      } catch (error) {
        if (error instanceof TypingFeelExportError) return { status: "error", activeRevision: active.revision, problems: error.problems };
        throw error;
      }
      await mkdir(keysDir(this.publicDir), { recursive: true });
      await writeFileAtomic(this.catalogueFile, exported.text);
      await writeFileAtomic(this.healthFile, exported.health);
      const referencesCreated = await this.addReferences(active.revision, active.config, described, "system");
      this.previewCache.clear();
      return { status: "re-exported", activeRevision: active.revision, catalogueRevision: publication.catalogueRevision, previousCatalogueRevision: previous, folders, referencesCreated, recordWritten, leftovers };
    });
  }

  /** Sets of one revision with their Media facts, for the Keyboard Sounds library. */
  async library(revisionId) {
    const target = await this.revision(revisionId);
    const { described, problems } = await describeConfigSets({ config: target.config, mediaStore: this.mediaStore, publicDir: this.publicDir, contract: this.contract });
    const previewBase = `/api/runtime/typing-feel/preview/${encodeURIComponent(revisionId)}/keys/`;
    return {
      revision: revisionId,
      problems,
      sets: target.config.keyboard.sets.map((set) => {
        const description = described.get(set.id);
        return {
          ...set,
          media: description ? {
            assetId: description.assetId,
            provenance: description.provenance,
            folder: description.folder,
            keys: description.keys,
            spaces: description.spaces,
            legacy218: (set.labels ?? []).includes("legacy-218"),
            preview: `${previewBase}${description.folder}/preview.ogg`,
          } : null,
        };
      }),
    };
  }

  async state() {
    if (!(await this.store.isInitialized())) {
      return { initialized: false, setup: { importCommand: IMPORT_COMMAND, restoreCommand: RESTORE_COMMAND } };
    }
    const state = await this.store.getState();
    const publications = new Map((await this.store.listPublications()).map((record) => [record.revision, record]));
    const revisions = (await this.store.listRevisions()).map((entry) => ({
      ...entry,
      publication: publications.get(entry.revision) ?? null,
    }));
    const active = revisions.find((entry) => entry.revision === state.activeRevision);
    // The draft waiting: the newest never-published draft on top of the live revision,
    // saved after the live revision went live. Drafts left from before a Publish or a
    // Rollback stay in History and are only used when someone picks one.
    const draft = revisions.find((entry) => entry.relation === "draft" && entry.publishable && !entry.publication && entry.createdAt >= state.updatedAt) ?? null;
    // History rows carry no config (each is ~11 KB and the list grows with every draft);
    // GET revisions/:id reads one. The live revision and the draft come whole.
    const history = revisions.map(({ config, ...entry }) => entry);
    let onDisk = null;
    const text = await readTextOrNull(this.catalogueFile);
    if (text !== null) {
      try {
        const parsed = JSON.parse(text);
        onDisk = { revision: parsed.revision ?? null, publishedAt: parsed.publishedAt ?? null, sets: Array.isArray(parsed.profiles) ? parsed.profiles.length : null };
      } catch {
        onDisk = { revision: null, unreadable: true };
      }
    }
    return {
      initialized: true,
      state,
      active,
      draft,
      history,
      reservedIds: await this.store.reservedRetiredIds(),
      local: { catalogue: onDisk, matchesActive: onDisk?.revision === active?.publication?.catalogueRevision },
    };
  }

  /** Release & History deployment rows (§3.11), read only: local, Git, Drive, online. */
  async exportStatus() {
    const text = await readTextOrNull(this.catalogueFile);
    let catalogue = null;
    try {
      catalogue = text === null ? null : JSON.parse(text);
    } catch {
      catalogue = null;
    }
    const local = catalogue ? { revision: catalogue.revision ?? null, publishedAt: catalogue.publishedAt ?? null, sets: catalogue.profiles?.length ?? 0 } : null;

    let git = { status: "unknown" };
    const inside = this.repoRoot ? relative(this.repoRoot, this.publicDir) : null;
    if (inside === null || inside.startsWith("..") || isAbsolute(inside)) {
      git = { status: "outside-repository", message: "The published folder is not inside this Git checkout." };
    } else {
      git = await new Promise((done) => {
        // --no-optional-locks: a status read never refreshes the index under .git/index.lock,
        // so it cannot make a git add or commit running at the same time fail.
        const env = { ...process.env, GIT_OPTIONAL_LOCKS: "0" };
        execFile("git", ["--no-optional-locks", "-C", this.repoRoot, "status", "--porcelain", "--untracked-files=all", "--", inside], { timeout: 5000, maxBuffer: 1024 * 1024, env }, (error, stdout) => {
          if (error) return done({ status: "unknown", message: "git status failed." });
          const changes = stdout.split("\n").filter(Boolean).filter((line) => /\.json$/.test(line.trim()));
          done({ status: changes.length ? "uncommitted" : "committed", changedFiles: changes.length, message: changes.length ? "The catalogue or set manifests have changes Git has not recorded; ask for a commit." : "The published JSON matches Git." });
        });
      });
    }

    let drive;
    const lockFile = join(dirname(this.publicDir), "media.md5");
    try {
      const lines = (await readFile(lockFile, "utf8")).split("\n");
      const tracked = new Set(lines.map((line) => line.replace(/^[0-9a-f]{32}\s+/, "").trim()).filter(Boolean));
      const audio = [];
      for (const profile of catalogue?.profiles ?? []) {
        const folder = profile.manifest.split("/").slice(0, 3).join("/");
        audio.push(`public/v1/keys/${folder}/preview.ogg`);
      }
      const missing = audio.filter((path) => !tracked.has(path));
      drive = { status: missing.length ? "not-backed-up" : "listed", lockFile: "typing-feel/media.md5", previewsListed: audio.length - missing.length, previews: audio.length, backupCommand: BACKUP_COMMAND };
    } catch (error) {
      drive = { status: error.code === "ENOENT" ? "no-lock-file" : "unknown", message: "typing-feel/media.md5 does not exist yet: the sound files are not tracked for Drive.", backupCommand: BACKUP_COMMAND };
    }
    return {
      local,
      git,
      drive,
      online: { status: "not-configured", message: "No online Typing Feel host yet. After Cloudflare is set up, the owner runs the deploy by hand.", deployCommand: DEPLOY_COMMAND },
    };
  }

  async #previewDescription(revisionId) {
    const cached = this.previewCache.get(revisionId);
    if (cached && cached.until > Date.now()) return cached.value;
    const target = await this.revision(revisionId);
    const { problems, described } = await this.checkConfig(target.config);
    if (problems.length) throw new TypingFeelValidationError(problems);
    const publication = (await this.store.getPublication(revisionId)) ?? { catalogueRevision: revisionId, publishedAt: isoSeconds(target.createdAt), builtAt: isoSeconds(target.createdAt) };
    const exported = this.buildExport(target.config, described, publication);
    const files = new Map();
    for (const set of target.config.keyboard.sets) {
      const description = described.get(set.id);
      for (const file of description.files) files.set(`${description.folder}/${file.name}`, file);
    }
    const value = { text: exported.text, files };
    this.previewCache.set(revisionId, { value, until: Date.now() + PREVIEW_CACHE_MS });
    return value;
  }

  /**
   * One file of a published set folder, as the games read it (`path` is
   * sets/<id>/<fp12>/<file>, already checked by the route). Only a regular file
   * inside the published keys folder; returns { body, contentType } or null.
   */
  async publishedFile(path) {
    const base = await realpath(keysDir(this.publicDir)).catch(() => null);
    if (base === null) return null;
    let file;
    try {
      file = await realpath(join(base, ...path.split("/")));
    } catch (error) {
      if (error?.code === "ENOENT" || error?.code === "ENOTDIR") return null;
      throw error;
    }
    if (!file.startsWith(`${base}${sep}`) || !(await lstat(file)).isFile()) return null;
    return { body: await readFile(file), contentType: mimeFor(file) };
  }

  /**
   * One file of a checked revision's export, for the Admin's own players and
   * previews (no token: <audio> and the kit's fetch cannot send one, §3.12).
   * `path` is relative to /v1/keys/. Returns { body, contentType } or null.
   */
  async previewFile(revisionId, path) {
    const preview = await this.#previewDescription(revisionId);
    if (path === "keys-manifest.json") return { body: Buffer.from(preview.text), contentType: mimeFor(path) };
    const file = preview.files.get(path);
    if (!file) return null;
    const body = await readFile(file.source);
    if (sha256(body) !== file.sha256) throw new TypingFeelExportError(`${path} does not match its Media V2 bytes.`);
    return { body, contentType: mimeFor(file.name) };
  }
}

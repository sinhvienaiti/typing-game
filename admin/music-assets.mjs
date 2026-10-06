import { randomUUID } from "node:crypto";
import {
  mkdir,
  readFile,
  rename,
  rm,
  writeFile,
} from "node:fs/promises";
import { basename, extname, join, relative, resolve, sep } from "node:path";
import { spawn } from "node:child_process";

export class MusicAssetError extends Error {
  constructor(message, status = 400) {
    super(message);
    this.status = status;
  }
}

const MAX_UPLOAD_BYTES = 96 * 1024 * 1024;
const WORLD_ID = /^world-(0[1-9]|[1-4][0-9]|50)$/;
const TRACK_ID = /^[a-z0-9](?:[a-z0-9-]{0,78}[a-z0-9])?$/;
const ALLOWED_EXTENSIONS = new Map([
  [".mp3", "audio/mpeg"],
  [".ogg", "audio/ogg"],
  [".wav", "audio/wav"],
  [".m4a", "audio/mp4"],
]);

function text(value, label, max = 160) {
  if (typeof value !== "string" || value.trim().length === 0 || value.trim().length > max) {
    throw new MusicAssetError(`${label} is required and must be at most ${max} characters.`);
  }
  return value.trim();
}

function finitePositive(value, label) {
  const number = Number(value);
  if (!Number.isFinite(number) || number <= 0) {
    throw new MusicAssetError(`${label} must be a positive finite number.`);
  }
  return number;
}

function optionalFinitePositive(value, label, upperBound) {
  if (value === undefined || value === null || value === "") return undefined;
  const number = finitePositive(value, label);
  if (upperBound !== undefined && number >= upperBound) {
    throw new MusicAssetError(`${label} must be lower than durationSeconds.`);
  }
  return number;
}

function safeRelative(root, target) {
  const value = relative(root, target);
  if (value === "" || value.startsWith(`..${sep}`) || value === "..") {
    if (value !== "") throw new MusicAssetError("Asset path escaped the authored music root.");
  }
  return value.split(sep).join("/");
}

function codecFor(extension, requested) {
  const canonical = ALLOWED_EXTENSIONS.get(extension);
  if (canonical === undefined) {
    throw new MusicAssetError(
      `Unsupported audio extension ${extension || "(none)"}. Use mp3, ogg, wav, or m4a.`,
    );
  }
  if (requested === undefined || requested === null || requested === "") return canonical;
  const normalized = String(requested).split(";")[0].trim().toLowerCase();
  const compatible =
    normalized === canonical ||
    (extension === ".m4a" && (normalized === "audio/x-m4a" || normalized === "audio/mp4"));
  if (!compatible) {
    throw new MusicAssetError(`Content type ${requested} does not match ${extension}.`);
  }
  return canonical;
}

function sourceUrl(relativeAssetPath) {
  return `/assets/audio/music/${relativeAssetPath.replace(/^public\/assets\/audio\/music\//, "")}`;
}

async function run(rootDir, command, args, timeoutMs = 30_000) {
  const child = spawn(command, args, {
    cwd: rootDir,
    env: process.env,
    shell: false,
    stdio: ["ignore", "pipe", "pipe"],
  });
  const stdout = [];
  const stderr = [];
  return new Promise((resolvePromise, reject) => {
    const timer = setTimeout(() => {
      child.kill("SIGKILL");
      reject(new MusicAssetError("World Music catalog rebuild timed out.", 500));
    }, timeoutMs);
    child.stdout.on("data", (chunk) => stdout.push(chunk));
    child.stderr.on("data", (chunk) => stderr.push(chunk));
    child.on("error", (error) => {
      clearTimeout(timer);
      reject(new MusicAssetError(`Could not rebuild World Music catalog: ${error.message}`, 500));
    });
    child.on("close", (code) => {
      clearTimeout(timer);
      if (code !== 0) {
        reject(
          new MusicAssetError(
            `World Music catalog rebuild failed (${code ?? "signal"}): ${Buffer.concat(stderr).toString("utf8").trim()}`,
            500,
          ),
        );
        return;
      }
      resolvePromise(Buffer.concat(stdout).toString("utf8"));
    });
  });
}

export class MusicAssetService {
  constructor({ rootDir }) {
    this.rootDir = rootDir;
    this.childDir = resolve(rootDir, "games/space-typing");
    this.musicRoot = resolve(this.childDir, "public/assets/audio/music");
    this.catalogPath = resolve(this.childDir, "src/audio/world-music-catalog.json");
  }

  async readCatalog() {
    try {
      return JSON.parse(await readFile(this.catalogPath, "utf8"));
    } catch (error) {
      throw new MusicAssetError(`Could not read World Music catalog: ${error.message}`, 500);
    }
  }

  async list() {
    const catalog = await this.readCatalog();
    return {
      schemaVersion: catalog.schemaVersion,
      manifestRevision: catalog.manifestRevision,
      tracks: (catalog.tracks ?? []).map((track) => ({
        ...track,
        uploadedByAdmin: track.metadata?.provenance === "local-admin-upload",
      })),
    };
  }

  async upload({
    bytes,
    fileName,
    contentType,
    trackId,
    title,
    worldId,
    durationSeconds,
    mixOutSeconds,
    mood,
  }) {
    if (!Buffer.isBuffer(bytes) || bytes.length === 0) {
      throw new MusicAssetError("Audio upload is empty.");
    }
    if (bytes.length > MAX_UPLOAD_BYTES) {
      throw new MusicAssetError(`Audio upload exceeds ${MAX_UPLOAD_BYTES / 1024 / 1024} MiB.` , 413);
    }
    const safeTrackId = text(trackId, "trackId", 80).toLowerCase();
    if (!TRACK_ID.test(safeTrackId)) {
      throw new MusicAssetError("trackId must use lowercase letters, digits, and hyphens only.");
    }
    const safeTitle = text(title, "title");
    const safeWorldId = text(worldId, "worldId", 8).toLowerCase();
    if (!WORLD_ID.test(safeWorldId)) {
      throw new MusicAssetError("worldId must be world-01 through world-50.");
    }
    const duration = finitePositive(durationSeconds, "durationSeconds");
    const mixOut = optionalFinitePositive(mixOutSeconds, "mixOutSeconds", duration);
    const originalName = basename(text(fileName, "fileName", 200));
    const extension = extname(originalName).toLowerCase();
    const codec = codecFor(extension, contentType);

    const trackDir = resolve(
      this.musicRoot,
      "worlds",
      safeWorldId,
      "uploads",
      safeTrackId,
    );
    safeRelative(this.musicRoot, trackDir);
    await mkdir(trackDir, { recursive: true });

    const audioPath = join(trackDir, `audio${extension}`);
    const manifestPath = join(trackDir, "track.json");
    try {
      await readFile(manifestPath);
      throw new MusicAssetError(`Track ${safeTrackId} already exists. Delete it before uploading a replacement.`, 409);
    } catch (error) {
      if (error instanceof MusicAssetError) throw error;
      if (error?.code !== "ENOENT") throw error;
    }

    const temporary = `${audioPath}.${process.pid}.${randomUUID()}.tmp`;
    await writeFile(temporary, bytes, { flag: "wx" });
    await rename(temporary, audioPath);

    const relativeAudio = safeRelative(this.musicRoot, audioPath);
    const manifest = {
      id: safeTrackId,
      title: safeTitle,
      playback: {
        kind: "single",
        sources: [{ src: sourceUrl(relativeAudio), codec }],
      },
      durationSeconds: duration,
      ...(mixOut === undefined ? {} : { mixOutSeconds: mixOut }),
      loop: true,
      metadata: {
        ...(typeof mood === "string" && mood.trim() ? { mood: mood.trim().slice(0, 80) } : {}),
        provenance: "local-admin-upload",
        originalFileName: originalName,
      },
    };

    try {
      await writeFile(manifestPath, `${JSON.stringify(manifest, null, 2)}\n`, { flag: "wx" });
      await this.rebuildCatalog();
    } catch (error) {
      await rm(trackDir, { recursive: true, force: true });
      throw error;
    }

    return {
      track: manifest,
      catalog: await this.list(),
    };
  }

  async remove(trackId) {
    const safeTrackId = text(trackId, "trackId", 80).toLowerCase();
    if (!TRACK_ID.test(safeTrackId)) throw new MusicAssetError("Invalid trackId.");
    const catalog = await this.readCatalog();
    const track = (catalog.tracks ?? []).find((entry) => entry.id === safeTrackId);
    if (track === undefined) throw new MusicAssetError(`Unknown track ${safeTrackId}.`, 404);
    if (track.metadata?.provenance !== "local-admin-upload") {
      throw new MusicAssetError("Only tracks uploaded through Local Admin may be deleted here.", 409);
    }

    const manifests = [
      ...Array.from({ length: 50 }, (_, index) =>
        resolve(
          this.musicRoot,
          "worlds",
          `world-${String(index + 1).padStart(2, "0")}`,
          "uploads",
          safeTrackId,
        ),
      ),
      resolve(this.musicRoot, "special", "uploads", safeTrackId),
    ];
    let removed = false;
    for (const directory of manifests) {
      safeRelative(this.musicRoot, directory);
      try {
        const manifest = JSON.parse(await readFile(join(directory, "track.json"), "utf8"));
        if (manifest.id !== safeTrackId || manifest.metadata?.provenance !== "local-admin-upload") continue;
        await rm(directory, { recursive: true, force: true });
        removed = true;
      } catch (error) {
        if (error?.code !== "ENOENT" && !(error instanceof SyntaxError)) throw error;
      }
    }
    if (!removed) throw new MusicAssetError(`Uploaded source for ${safeTrackId} was not found.`, 404);
    await this.rebuildCatalog();
    return this.list();
  }

  async rebuildCatalog() {
    await run(this.rootDir, "pnpm", ["--dir", this.childDir, "music:catalog"]);
    return this.readCatalog();
  }
}

export { MAX_UPLOAD_BYTES };

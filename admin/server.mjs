import { createServer } from "node:http";
import { readFile } from "node:fs/promises";
import { resolve } from "node:path";
import { fileURLToPath } from "node:url";
import { AdminConflictError, AdminValidationError } from "./store.mjs";
import { SpaceTypingRevisionStore } from "./space-typing-store.mjs";
import { createDefaultSpaceTypingConfig } from "./default-config.mjs";
import { runWorldMusicPreview, WorldMusicPreviewError } from "./world-music-preview.mjs";
import { runShipRegistryPreview, ShipRegistryPreviewError } from "./ship-registry-preview.mjs";
import { runEquipmentRegistryPreview, EquipmentRegistryPreviewError } from "./equipment-registry-preview.mjs";
import { runSkillRegistryPreview, SkillRegistryPreviewError } from "./skill-registry-preview.mjs";
import { runEnemyRegistryPreview, EnemyRegistryPreviewError } from "./enemy-registry-preview.mjs";
import { createShipRuntimeEnvelope } from "./ship-runtime.mjs";
import { createEquipmentRuntimeEnvelope } from "./equipment-runtime.mjs";
import { createSkillRuntimeEnvelope } from "./skill-runtime.mjs";
import { createEnemyRuntimeEnvelope } from "./enemy-runtime.mjs";
import { MAX_UPLOAD_BYTES, MusicAssetError, MusicAssetService } from "./music-assets.mjs";

const root = resolve(fileURLToPath(new URL("..", import.meta.url)));
const contractPath = resolve(root, "games/space-typing/contracts/space-typing-admin.v1.json");
const contract = JSON.parse(await readFile(contractPath, "utf8"));
const store = new SpaceTypingRevisionStore({
  rootDir: process.env.TYPING_GAME_ADMIN_DATA_DIR || resolve(root, ".local/admin/space-typing"),
  contract,
});
const musicAssets = new MusicAssetService({ rootDir: root });
await store.initialize(createDefaultSpaceTypingConfig(contract));

const host = "127.0.0.1";
const port = Number.parseInt(process.env.TYPING_GAME_ADMIN_PORT || "3199", 10);
const token = process.env.TYPING_GAME_ADMIN_TOKEN || "local-dev";

function json(response, status, body) {
  const data = JSON.stringify(body);
  response.writeHead(status, {
    "content-type": "application/json; charset=utf-8",
    "cache-control": "no-store",
    "content-length": Buffer.byteLength(data),
  });
  response.end(data);
}

async function readBody(request, maxBytes) {
  const chunks = [];
  let size = 0;
  for await (const chunk of request) {
    size += chunk.length;
    if (size > maxBytes) throw new AdminValidationError("Request body too large.");
    chunks.push(chunk);
  }
  return Buffer.concat(chunks);
}

async function body(request) {
  const buffer = await readBody(request, 1024 * 1024);
  if (buffer.length === 0) return {};
  try {
    return JSON.parse(buffer.toString("utf8"));
  } catch {
    throw new AdminValidationError("Request body must be valid JSON.");
  }
}

function header(request, name, required = false) {
  const value = request.headers[name];
  const text = Array.isArray(value) ? value[0] : value;
  if (required && (typeof text !== "string" || text.trim().length === 0)) {
    throw new AdminValidationError(`Missing ${name} header.`);
  }
  return typeof text === "string" ? text : undefined;
}

function authorized(request) {
  return request.headers["x-typing-game-admin-token"] === token;
}

const server = createServer(async (request, response) => {
  try {
    const url = new URL(request.url || "/", `http://${host}:${port}`);

    if (request.method === "GET" && url.pathname === "/api/runtime/space-typing/ships") {
      const state = await store.getState();
      const config = await store.getRuntimeConfig();
      json(response, 200, createShipRuntimeEnvelope(state, config));
      return;
    }
    if (request.method === "GET" && url.pathname === "/api/runtime/space-typing/equipment") {
      const state = await store.getState();
      const config = await store.getRuntimeConfig();
      json(response, 200, createEquipmentRuntimeEnvelope(state, config));
      return;
    }
    if (request.method === "GET" && url.pathname === "/api/runtime/space-typing/skills") {
      const state = await store.getState();
      const config = await store.getRuntimeConfig();
      json(response, 200, createSkillRuntimeEnvelope(state, config, contract));
      return;
    }
    if (request.method === "GET" && url.pathname === "/api/runtime/space-typing/enemies") {
      const state = await store.getState();
      const config = await store.getRuntimeConfig();
      json(response, 200, createEnemyRuntimeEnvelope(state, config, contract));
      return;
    }

    if (!url.pathname.startsWith("/api/admin/")) {
      json(response, 404, { error: "not-found" });
      return;
    }
    if (!authorized(request)) {
      json(response, 401, { error: "unauthorized" });
      return;
    }

    if (request.method === "GET" && url.pathname === "/api/admin/space-typing/contract") {
      json(response, 200, contract);
      return;
    }
    if (request.method === "GET" && url.pathname === "/api/admin/space-typing/state") {
      const state = await store.getState();
      const active = await store.getActiveRevision();
      const history = await store.listRevisions();
      json(response, 200, { state, active, history });
      return;
    }
    if (request.method === "GET" && url.pathname === "/api/admin/space-typing/runtime") {
      json(response, 200, {
        activeRevision: (await store.getState()).activeRevision,
        config: await store.getRuntimeConfig(),
      });
      return;
    }
    if (request.method === "GET" && url.pathname === "/api/admin/space-typing/music/library") {
      json(response, 200, await musicAssets.list());
      return;
    }
    if (request.method === "POST" && url.pathname === "/api/admin/space-typing/music/upload") {
      const bytes = await readBody(request, MAX_UPLOAD_BYTES + 1);
      const result = await musicAssets.upload({
        bytes,
        fileName: header(request, "x-music-file-name", true),
        contentType: header(request, "content-type"),
        trackId: header(request, "x-music-track-id", true),
        title: header(request, "x-music-title", true),
        worldId: header(request, "x-music-world-id", true),
        durationSeconds: header(request, "x-music-duration-seconds", true),
        mixOutSeconds: header(request, "x-music-mix-out-seconds"),
        mood: header(request, "x-music-mood"),
      });
      json(response, 201, result);
      return;
    }
    if (request.method === "DELETE" && url.pathname.startsWith("/api/admin/space-typing/music/tracks/")) {
      const trackId = decodeURIComponent(url.pathname.slice("/api/admin/space-typing/music/tracks/".length));
      json(response, 200, await musicAssets.remove(trackId));
      return;
    }
    if (request.method === "POST" && url.pathname === "/api/admin/space-typing/world-music/preview") {
      const input = await body(request);
      const activeConfig = await store.getRuntimeConfig();
      const publishedPolicy = input.publishedPolicy ?? activeConfig.worldMusic?.publishedPolicy;
      const preview = await runWorldMusicPreview({
        rootDir: root,
        contract,
        publishedPolicy,
        musicMode: input.musicMode ?? "map",
        stageNumber: input.stageNumber,
      });
      json(response, 200, preview);
      return;
    }
    if (request.method === "POST" && url.pathname === "/api/admin/space-typing/ships/preview") {
      const input = await body(request);
      const activeConfig = await store.getRuntimeConfig();
      const policy = input.policy ?? activeConfig.content?.ships;
      const preview = await runShipRegistryPreview({ rootDir: root, contract, policy });
      json(response, 200, preview);
      return;
    }
    if (request.method === "POST" && url.pathname === "/api/admin/space-typing/equipment/preview") {
      const input = await body(request);
      const activeConfig = await store.getRuntimeConfig();
      const policy = input.policy ?? activeConfig.content?.equipment;
      const preview = await runEquipmentRegistryPreview({ rootDir: root, contract, policy });
      json(response, 200, preview);
      return;
    }
    if (request.method === "POST" && url.pathname === "/api/admin/space-typing/skills/preview") {
      const input = await body(request);
      const activeConfig = await store.getRuntimeConfig();
      const policy = input.policy ?? activeConfig.content?.skills;
      const preview = await runSkillRegistryPreview({ rootDir: root, contract, policy });
      json(response, 200, preview);
      return;
    }
    if (request.method === "POST" && url.pathname === "/api/admin/space-typing/enemies/preview") {
      const input = await body(request);
      const activeConfig = await store.getRuntimeConfig();
      const policy = input.policy ?? activeConfig.content?.enemies;
      const preview = await runEnemyRegistryPreview({ rootDir: root, contract, policy });
      json(response, 200, preview);
      return;
    }
    if (request.method === "POST" && url.pathname === "/api/admin/space-typing/validate-revision") {
      const input = await body(request);
      json(response, 200, await store.validateRevision(input.revision));
      return;
    }
    if (request.method === "POST" && url.pathname === "/api/admin/space-typing/revisions") {
      const input = await body(request);
      const revision = await store.createRevision(input);
      json(response, 201, revision);
      return;
    }
    if (request.method === "POST" && url.pathname === "/api/admin/space-typing/publish") {
      const input = await body(request);
      const state = await store.publish(input);
      json(response, 200, state);
      return;
    }
    if (request.method === "POST" && url.pathname === "/api/admin/space-typing/rollback") {
      const input = await body(request);
      const state = await store.rollback(input);
      json(response, 200, state);
      return;
    }

    json(response, 404, { error: "not-found" });
  } catch (error) {
    if (error instanceof AdminConflictError) {
      json(response, 409, { error: "conflict", message: error.message });
      return;
    }
    if (error instanceof AdminValidationError) {
      json(response, 400, { error: "validation", message: error.message });
      return;
    }
    if (error instanceof MusicAssetError) {
      json(response, error.status, { error: "music-asset", message: error.message });
      return;
    }
    if (error instanceof WorldMusicPreviewError) {
      json(response, 502, { error: "preview-error", message: error.message });
      return;
    }
    if (error instanceof ShipRegistryPreviewError) {
      json(response, 502, { error: "ships-preview-error", message: error.message });
      return;
    }
    if (error instanceof EquipmentRegistryPreviewError) {
      json(response, 502, { error: "equipment-preview-error", message: error.message });
      return;
    }
    if (error instanceof SkillRegistryPreviewError) {
      json(response, 502, { error: "skills-preview-error", message: error.message });
      return;
    }
    if (error instanceof EnemyRegistryPreviewError) {
      json(response, 502, { error: "enemies-preview-error", message: error.message });
      return;
    }
    console.error(error);
    json(response, 500, { error: "internal-error" });
  }
});

server.listen(port, host, () => {
  console.log(`Space Typing Admin service: http://${host}:${port}`);
  if (token === "local-dev") {
    console.log("Admin auth token: local-dev (local development default)");
  }
});

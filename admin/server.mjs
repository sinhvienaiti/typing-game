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
import { runBossRegistryPreview, BossRegistryPreviewError } from "./boss-registry-preview.mjs";
import { runWorldRegistryPreview, WorldRegistryPreviewError } from "./world-registry-preview.mjs";
import { runStageConfigPreview, StageConfigPreviewError } from "./stage-config-preview.mjs";
import { createShipRuntimeEnvelope } from "./ship-runtime.mjs";
import { createEquipmentRuntimeEnvelope } from "./equipment-runtime.mjs";
import { createSkillRuntimeEnvelope } from "./skill-runtime.mjs";
import { createEnemyRuntimeEnvelope } from "./enemy-runtime.mjs";
import { createBossRuntimeEnvelope } from "./boss-runtime.mjs";
import { createWorldRuntimeEnvelope } from "./world-runtime.mjs";
import { createStageRuntimeEnvelope } from "./stage-runtime.mjs";
import { queryTypingContentCatalog } from "./typing-content-catalog.mjs";
import { createShopCapabilityManifest } from "./shop-capability.mjs";
import { createCurrencyCapabilityManifest } from "./currency-capability.mjs";
import { createDeveloperToolsManifest } from "./developer-tools.mjs";
import { MAX_UPLOAD_BYTES, MusicAssetError, MusicAssetService } from "./music-assets.mjs";
import { MediaAssetStore } from "./media-assets-v2.mjs";
import { bootstrapMediaReferences } from "./media-bootstrap.mjs";
import { createMediaV2HttpHandler } from "./media-http.mjs";
import {
  ADMIN_PERMISSIONS,
  AdminAuthorizationError,
  LocalAdminAuditLog,
  createLocalAdminActorFromRequest,
  describeConfigChangeScope,
  requireAdminPermission,
  runAuthorizedAdminMutation,
} from "./admin-security.mjs";

const root = resolve(fileURLToPath(new URL("..", import.meta.url)));
const contract = JSON.parse(await readFile(resolve(root, "games/space-typing/contracts/space-typing-admin.v1.json"), "utf8"));
const eventsContract = JSON.parse(await readFile(resolve(root, "games/space-typing/contracts/space-typing-admin-events.v1.json"), "utf8"));
const duelContract = JSON.parse(await readFile(resolve(root, "games/space-typing/contracts/space-typing-admin-duel.v1.json"), "utf8"));
const rankedContract = JSON.parse(await readFile(resolve(root, "games/space-typing/contracts/space-typing-admin-ranked.v1.json"), "utf8"));
const alternativeModesContract = JSON.parse(await readFile(resolve(root, "games/space-typing/contracts/space-typing-admin-alternative-modes.v1.json"), "utf8"));
const backgroundsContract = JSON.parse(await readFile(resolve(root, "games/space-typing/contracts/space-typing-admin-backgrounds.v1.json"), "utf8"));
const vfxContract = JSON.parse(await readFile(resolve(root, "games/space-typing/contracts/space-typing-admin-vfx.v1.json"), "utf8"));
const uiAssetsContract = JSON.parse(await readFile(resolve(root, "games/space-typing/contracts/space-typing-admin-ui-assets.v1.json"), "utf8"));
const qaContract = JSON.parse(await readFile(resolve(root, "games/space-typing/contracts/space-typing-admin-qa.v1.json"), "utf8"));
const telemetryContract = JSON.parse(await readFile(resolve(root, "games/space-typing/contracts/space-typing-admin-telemetry.v1.json"), "utf8"));
const expeditionContract = JSON.parse(await readFile(resolve(root, "games/space-typing/contracts/space-typing-admin-expedition.v1.json"), "utf8"));
const dailyWeeklyContract = JSON.parse(await readFile(resolve(root, "games/space-typing/contracts/space-typing-admin-daily-weekly.v1.json"), "utf8"));
const adminDataDir = process.env.TYPING_GAME_ADMIN_DATA_DIR || resolve(root, ".local/admin/space-typing");
const store = new SpaceTypingRevisionStore({ rootDir: adminDataDir, contract });
const musicAssets = new MusicAssetService({ rootDir: root });
const mediaAssetsV2 = new MediaAssetStore({ rootDir: adminDataDir });
const auditLog = new LocalAdminAuditLog({ rootDir: adminDataDir });
await store.initialize(createDefaultSpaceTypingConfig(contract));
await mediaAssetsV2.initialize();
await bootstrapMediaReferences({ store: mediaAssetsV2, childRoot: resolve(root, "games/space-typing") });
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
  if (!buffer.length) return {};
  try {
    return JSON.parse(buffer.toString("utf8"));
  } catch {
    throw new AdminValidationError("Request body must be valid JSON.");
  }
}

function header(request, name, required = false) {
  const value = request.headers[name];
  const text = Array.isArray(value) ? value[0] : value;
  if (required && (typeof text !== "string" || !text.trim())) {
    throw new AdminValidationError(`Missing ${name} header.`);
  }
  return typeof text === "string" ? text : undefined;
}

function authorized(request) {
  return request.headers["x-typing-game-admin-token"] === token;
}

function reportAuditDegradation(error) {
  console.error("Space Typing Admin audit append degraded after mutation:", error);
}

const mutationAuditBase = {
  auditLog,
  onAuditError: reportAuditDegradation,
};
const handleMediaV2Request = createMediaV2HttpHandler({
  store: mediaAssetsV2,
  auditLog,
  onAuditError: reportAuditDegradation,
});

async function revisionChangeScope(revisionId) {
  const target = await store.getRevision(revisionId);
  const base = target.parentRevision ? await store.getRevision(target.parentRevision) : null;
  return describeConfigChangeScope({
    baseRevision: base?.revision ?? null,
    targetRevision: target.revision,
    baseConfig: base?.config ?? {},
    targetConfig: target.config,
  });
}

async function rollbackChangeScope(targetRevision) {
  const state = await store.getState();
  const active = await store.getRevision(state.activeRevision);
  const target = await store.getRevision(targetRevision);
  return describeConfigChangeScope({
    baseRevision: active.revision,
    targetRevision: target.revision,
    baseConfig: active.config,
    targetConfig: target.config,
  });
}

const server = createServer(async (request, response) => {
  try {
    const url = new URL(request.url || "/", `http://${host}:${port}`);
    const runtimeHandlers = {
      "/api/runtime/space-typing/ships": (s, c) => createShipRuntimeEnvelope(s, c),
      "/api/runtime/space-typing/equipment": (s, c) => createEquipmentRuntimeEnvelope(s, c),
      "/api/runtime/space-typing/skills": (s, c) => createSkillRuntimeEnvelope(s, c, contract),
      "/api/runtime/space-typing/enemies": (s, c) => createEnemyRuntimeEnvelope(s, c, contract),
      "/api/runtime/space-typing/bosses": (s, c) => createBossRuntimeEnvelope(s, c, contract),
      "/api/runtime/space-typing/worlds": (s, c) => createWorldRuntimeEnvelope(s, c, contract),
      "/api/runtime/space-typing/stages": (s, c) => createStageRuntimeEnvelope(s, c, contract),
    };

    if(request.method==="GET"&&runtimeHandlers[url.pathname]) {
      const state = await store.getState();
      const config = await store.getRuntimeConfig();
      json(response, 200, runtimeHandlers[url.pathname](state, config));
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

    const actor = createLocalAdminActorFromRequest(request);
    if (await handleMediaV2Request({ request, response, url, actor })) return;

    if(request.method==="GET"&&url.pathname==="/api/admin/space-typing/actor") {
      json(response, 200, actor);
      return;
    }
    if(request.method==="GET"&&url.pathname==="/api/admin/space-typing/audit") {
      requireAdminPermission(actor, ADMIN_PERMISSIONS.AUDIT_READ);
      const parsedLimit = Number.parseInt(url.searchParams.get("limit") || "100", 10);
      const limit = Number.isFinite(parsedLimit) ? parsedLimit : 100;
      json(response, 200, { events: await auditLog.list({ limit }) });
      return;
    }
    if(request.method==="GET"&&url.pathname==="/api/admin/space-typing/developer-tools/manifest") {
      requireAdminPermission(actor, ADMIN_PERMISSIONS.DEVELOPER_INSPECT);
      json(response, 200, createDeveloperToolsManifest());
      return;
    }
    if(request.method==="GET"&&url.pathname==="/api/admin/space-typing/contract") {
      json(response, 200, contract);
      return;
    }
    if(request.method==="GET"&&url.pathname==="/api/admin/space-typing/events/contract") {
      json(response, 200, eventsContract);
      return;
    }
    if(request.method==="GET"&&url.pathname==="/api/admin/space-typing/duel/contract") {
      json(response, 200, duelContract);
      return;
    }
    if(request.method==="GET"&&url.pathname==="/api/admin/space-typing/ranked/contract") {
      json(response, 200, rankedContract);
      return;
    }
    if(request.method==="GET"&&url.pathname==="/api/admin/space-typing/alternative-modes/contract") {
      json(response, 200, alternativeModesContract);
      return;
    }
    if(request.method==="GET"&&url.pathname==="/api/admin/space-typing/backgrounds/contract") {
      json(response, 200, backgroundsContract);
      return;
    }
    if(request.method==="GET"&&url.pathname==="/api/admin/space-typing/vfx/contract") {
      json(response, 200, vfxContract);
      return;
    }
    if(request.method==="GET"&&url.pathname==="/api/admin/space-typing/ui-assets/contract") {
      json(response, 200, uiAssetsContract);
      return;
    }
    if(request.method==="GET"&&url.pathname==="/api/admin/space-typing/qa/contract") {
      json(response, 200, qaContract);
      return;
    }
    if(request.method==="GET"&&url.pathname==="/api/admin/space-typing/telemetry/contract") {
      json(response, 200, telemetryContract);
      return;
    }
    if(request.method==="GET"&&url.pathname==="/api/admin/space-typing/expedition/contract") {
      json(response, 200, expeditionContract);
      return;
    }
    if(request.method==="GET"&&url.pathname==="/api/admin/space-typing/daily-weekly/contract") {
      json(response, 200, dailyWeeklyContract);
      return;
    }
    if(request.method==="GET"&&url.pathname==="/api/admin/space-typing/state") {
      json(response, 200, {
        state: await store.getState(),
        active: await store.getActiveRevision(),
        history: await store.listRevisions(),
      });
      return;
    }
    if(request.method==="GET"&&url.pathname==="/api/admin/space-typing/runtime") {
      json(response, 200, {
        activeRevision: (await store.getState()).activeRevision,
        config: await store.getRuntimeConfig(),
      });
      return;
    }
    if(request.method==="GET"&&url.pathname==="/api/admin/space-typing/typing-content/catalog") {
      json(response, 200, await queryTypingContentCatalog({ rootDir: root, searchParams: url.searchParams }));
      return;
    }
    if(request.method==="GET"&&url.pathname==="/api/admin/space-typing/shop/capabilities") {
      json(response, 200, createShopCapabilityManifest());
      return;
    }
    if(request.method==="GET"&&url.pathname==="/api/admin/space-typing/currencies/capabilities") {
      json(response, 200, createCurrencyCapabilityManifest());
      return;
    }
    if(request.method==="GET"&&url.pathname==="/api/admin/space-typing/music/library") {
      json(response, 200, await musicAssets.list());
      return;
    }
    if(request.method==="POST"&&url.pathname==="/api/admin/space-typing/change-scope") {
      requireAdminPermission(actor, ADMIN_PERMISSIONS.CONFIG_DRAFT);
      const input = await body(request);
      json(response, 200, await revisionChangeScope(input.revision));
      return;
    }

    if(request.method==="POST"&&url.pathname==="/api/admin/space-typing/music/upload") {
      const trackId = header(request, "x-music-track-id");
      const result = await runAuthorizedAdminMutation({
        ...mutationAuditBase,
        actor,
        permission: ADMIN_PERMISSIONS.MEDIA_UPLOAD,
        action: "media.music.upload",
        domain: "media.music",
        entityType: "music-track",
        entityId: trackId ?? null,
        changeScope: { model: "asset-mutation", operation: "upload", assetType: "music", assetId: trackId ?? null },
        operation: async () => {
          const bytes = await readBody(request, MAX_UPLOAD_BYTES + 1);
          return musicAssets.upload({
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
        },
      });
      json(response, 201, result);
      return;
    }

    if(request.method==="DELETE"&&url.pathname.startsWith("/api/admin/space-typing/music/tracks/")) {
      const trackId = decodeURIComponent(url.pathname.slice("/api/admin/space-typing/music/tracks/".length));
      const result = await runAuthorizedAdminMutation({
        ...mutationAuditBase,
        actor,
        permission: ADMIN_PERMISSIONS.MEDIA_DELETE,
        auditLog,
        action: "media.music.delete",
        domain: "media.music",
        entityType: "music-track",
        entityId: trackId,
        changeScope: { model: "asset-mutation", operation: "delete", assetType: "music", assetId: trackId },
        operation: () => musicAssets.remove(trackId),
      });
      json(response, 200, result);
      return;
    }

    if(request.method==="POST"&&url.pathname==="/api/admin/space-typing/world-music/preview") {
      const input = await body(request);
      const active = await store.getRuntimeConfig();
      json(response, 200, await runWorldMusicPreview({
        rootDir: root,
        contract,
        publishedPolicy: input.publishedPolicy ?? active.worldMusic?.publishedPolicy,
        musicMode: input.musicMode ?? "map",
        stageNumber: input.stageNumber,
      }));
      return;
    }

    const previewHandlers = {
      "/api/admin/space-typing/ships/preview": [runShipRegistryPreview, "ships"],
      "/api/admin/space-typing/equipment/preview": [runEquipmentRegistryPreview, "equipment"],
      "/api/admin/space-typing/skills/preview": [runSkillRegistryPreview, "skills"],
      "/api/admin/space-typing/enemies/preview": [runEnemyRegistryPreview, "enemies"],
      "/api/admin/space-typing/bosses/preview": [runBossRegistryPreview, "bosses"],
      "/api/admin/space-typing/worlds/preview": [runWorldRegistryPreview, "worlds"],
      "/api/admin/space-typing/stages/preview": [runStageConfigPreview, "stages"],
    };
    if(request.method==="POST"&&previewHandlers[url.pathname]) {
      const input = await body(request);
      const active = await store.getRuntimeConfig();
      const [run, key] = previewHandlers[url.pathname];
      json(response, 200, await run({ rootDir: root, contract, policy: input.policy ?? active.content?.[key] }));
      return;
    }

    if(request.method==="POST"&&url.pathname==="/api/admin/space-typing/validate-revision") {
      const input = await body(request);
      const validation = await store.validateRevision(input.revision);
      json(response, 200, { ...validation, changeScope: await revisionChangeScope(input.revision) });
      return;
    }

    if(request.method==="POST"&&url.pathname==="/api/admin/space-typing/revisions") {
      const input = await body(request);
      const baseRevision = await store.getRevision(input.baseRevision);
      const draftScope = describeConfigChangeScope({
        baseRevision: baseRevision.revision,
        targetRevision: null,
        baseConfig: baseRevision.config,
        targetConfig: input.config,
      });
      const revision = await runAuthorizedAdminMutation({
        ...mutationAuditBase,
        actor,
        permission: ADMIN_PERMISSIONS.CONFIG_DRAFT,
        auditLog,
        action: "revision.create",
        domain: "config",
        entityType: "revision",
        changeScope: draftScope,
        resolveEntityId: (created) => created.revision,
        resolveChangeScope: (created) => ({ ...draftScope, targetRevision: created.revision }),
        operation: () => store.createRevision({ ...input, author: actor.actorId }),
      });
      json(response, 201, revision);
      return;
    }

    if(request.method==="POST"&&url.pathname==="/api/admin/space-typing/publish") {
      const input = await body(request);
      const changeScope = await revisionChangeScope(input.revision);
      const state = await runAuthorizedAdminMutation({
        ...mutationAuditBase,
        actor,
        permission: ADMIN_PERMISSIONS.CONFIG_PUBLISH,
        auditLog,
        action: "revision.publish",
        domain: "config",
        entityType: "revision",
        entityId: input.revision,
        changeScope,
        operation: () => store.publish(input),
      });
      json(response, 200, state);
      return;
    }

    if(request.method==="POST"&&url.pathname==="/api/admin/space-typing/rollback") {
      const input = await body(request);
      const changeScope = await rollbackChangeScope(input.targetRevision);
      const state = await runAuthorizedAdminMutation({
        ...mutationAuditBase,
        actor,
        permission: ADMIN_PERMISSIONS.CONFIG_ROLLBACK,
        auditLog,
        action: "revision.rollback",
        domain: "config",
        entityType: "revision",
        entityId: input.targetRevision,
        changeScope,
        operation: () => store.rollback(input),
      });
      json(response, 200, state);
      return;
    }

    json(response, 404, { error: "not-found" });
  } catch (error) {
    if (error instanceof AdminAuthorizationError) {
      json(response, 403, { error: "forbidden", message: error.message, permission: error.permission });
      return;
    }
    if (error instanceof AdminConflictError) {
      json(response, 409, { error: "conflict", message: error.message });
      return;
    }
    if (error instanceof AdminValidationError) {
      json(response, 400, { error: "validation", message: error.message });
      return;
    }
    if (error instanceof TypeError && String(error.message).startsWith("Unsupported typing-content kind:")) {
      json(response, 400, { error: "validation", message: error.message });
      return;
    }
    if (error instanceof MusicAssetError) {
      json(response, error.status, { error: "music-asset", message: error.message });
      return;
    }
    const previews = [
      [WorldMusicPreviewError, "preview-error"],
      [ShipRegistryPreviewError, "ships-preview-error"],
      [EquipmentRegistryPreviewError, "equipment-preview-error"],
      [SkillRegistryPreviewError, "skills-preview-error"],
      [EnemyRegistryPreviewError, "enemies-preview-error"],
      [BossRegistryPreviewError, "bosses-preview-error"],
      [WorldRegistryPreviewError, "worlds-preview-error"],
      [StageConfigPreviewError, "stages-preview-error"],
    ];
    for (const [Type, code] of previews) {
      if (error instanceof Type) {
        json(response, 502, { error: code, message: error.message });
        return;
      }
    }
    console.error(error);
    json(response, 500, { error: "internal-error" });
  }
});

server.listen(port, host, () => {
  console.log(`Space Typing Admin service: http://${host}:${port}`);
  if (token === "local-dev") console.log("Admin auth token: local-dev (local development default)");
});
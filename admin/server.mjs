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
import { MAX_UPLOAD_BYTES, MusicAssetError, MusicAssetService } from "./music-assets.mjs";

const root = resolve(fileURLToPath(new URL("..", import.meta.url)));
const contract = JSON.parse(await readFile(resolve(root, "games/space-typing/contracts/space-typing-admin.v1.json"), "utf8"));
const store = new SpaceTypingRevisionStore({ rootDir: process.env.TYPING_GAME_ADMIN_DATA_DIR || resolve(root, ".local/admin/space-typing"), contract });
const musicAssets = new MusicAssetService({ rootDir: root });
await store.initialize(createDefaultSpaceTypingConfig(contract));
const host = "127.0.0.1";
const port = Number.parseInt(process.env.TYPING_GAME_ADMIN_PORT || "3199", 10);
const token = process.env.TYPING_GAME_ADMIN_TOKEN || "local-dev";

function json(response, status, body) { const data = JSON.stringify(body); response.writeHead(status, { "content-type":"application/json; charset=utf-8", "cache-control":"no-store", "content-length":Buffer.byteLength(data) }); response.end(data); }
async function readBody(request, maxBytes) { const chunks=[]; let size=0; for await (const chunk of request) { size+=chunk.length; if(size>maxBytes) throw new AdminValidationError("Request body too large."); chunks.push(chunk); } return Buffer.concat(chunks); }
async function body(request) { const buffer=await readBody(request,1024*1024); if(!buffer.length)return {}; try{return JSON.parse(buffer.toString("utf8"));}catch{throw new AdminValidationError("Request body must be valid JSON.");} }
function header(request,name,required=false){const value=request.headers[name];const text=Array.isArray(value)?value[0]:value;if(required&&(typeof text!=="string"||!text.trim()))throw new AdminValidationError(`Missing ${name} header.`);return typeof text==="string"?text:undefined;}
function authorized(request){return request.headers["x-typing-game-admin-token"]===token;}

const server=createServer(async(request,response)=>{try{
  const url=new URL(request.url||"/",`http://${host}:${port}`);
  const runtimeHandlers={
    "/api/runtime/space-typing/ships":(s,c)=>createShipRuntimeEnvelope(s,c),
    "/api/runtime/space-typing/equipment":(s,c)=>createEquipmentRuntimeEnvelope(s,c),
    "/api/runtime/space-typing/skills":(s,c)=>createSkillRuntimeEnvelope(s,c,contract),
    "/api/runtime/space-typing/enemies":(s,c)=>createEnemyRuntimeEnvelope(s,c,contract),
    "/api/runtime/space-typing/bosses":(s,c)=>createBossRuntimeEnvelope(s,c,contract),
    "/api/runtime/space-typing/worlds":(s,c)=>createWorldRuntimeEnvelope(s,c,contract),
    "/api/runtime/space-typing/stages":(s,c)=>createStageRuntimeEnvelope(s,c,contract),
  };
  if(request.method==="GET"&&runtimeHandlers[url.pathname]){const state=await store.getState();const config=await store.getRuntimeConfig();json(response,200,runtimeHandlers[url.pathname](state,config));return;}
  if(!url.pathname.startsWith("/api/admin/")){json(response,404,{error:"not-found"});return;}
  if(!authorized(request)){json(response,401,{error:"unauthorized"});return;}
  if(request.method==="GET"&&url.pathname==="/api/admin/space-typing/contract"){json(response,200,contract);return;}
  if(request.method==="GET"&&url.pathname==="/api/admin/space-typing/state"){json(response,200,{state:await store.getState(),active:await store.getActiveRevision(),history:await store.listRevisions()});return;}
  if(request.method==="GET"&&url.pathname==="/api/admin/space-typing/runtime"){json(response,200,{activeRevision:(await store.getState()).activeRevision,config:await store.getRuntimeConfig()});return;}
  if(request.method==="GET"&&url.pathname==="/api/admin/space-typing/typing-content/catalog"){json(response,200,await queryTypingContentCatalog({rootDir:root,searchParams:url.searchParams}));return;}
  if(request.method==="GET"&&url.pathname==="/api/admin/space-typing/shop/capabilities"){json(response,200,createShopCapabilityManifest());return;}
  if(request.method==="GET"&&url.pathname==="/api/admin/space-typing/currencies/capabilities"){json(response,200,createCurrencyCapabilityManifest());return;}
  if(request.method==="GET"&&url.pathname==="/api/admin/space-typing/music/library"){json(response,200,await musicAssets.list());return;}
  if(request.method==="POST"&&url.pathname==="/api/admin/space-typing/music/upload"){const bytes=await readBody(request,MAX_UPLOAD_BYTES+1);json(response,201,await musicAssets.upload({bytes,fileName:header(request,"x-music-file-name",true),contentType:header(request,"content-type"),trackId:header(request,"x-music-track-id",true),title:header(request,"x-music-title",true),worldId:header(request,"x-music-world-id",true),durationSeconds:header(request,"x-music-duration-seconds",true),mixOutSeconds:header(request,"x-music-mix-out-seconds"),mood:header(request,"x-music-mood")}));return;}
  if(request.method==="DELETE"&&url.pathname.startsWith("/api/admin/space-typing/music/tracks/")){json(response,200,await musicAssets.remove(decodeURIComponent(url.pathname.slice("/api/admin/space-typing/music/tracks/".length))));return;}
  if(request.method==="POST"&&url.pathname==="/api/admin/space-typing/world-music/preview"){const input=await body(request);const active=await store.getRuntimeConfig();json(response,200,await runWorldMusicPreview({rootDir:root,contract,publishedPolicy:input.publishedPolicy??active.worldMusic?.publishedPolicy,musicMode:input.musicMode??"map",stageNumber:input.stageNumber}));return;}
  const previewHandlers={
    "/api/admin/space-typing/ships/preview":[runShipRegistryPreview,"ships"],
    "/api/admin/space-typing/equipment/preview":[runEquipmentRegistryPreview,"equipment"],
    "/api/admin/space-typing/skills/preview":[runSkillRegistryPreview,"skills"],
    "/api/admin/space-typing/enemies/preview":[runEnemyRegistryPreview,"enemies"],
    "/api/admin/space-typing/bosses/preview":[runBossRegistryPreview,"bosses"],
    "/api/admin/space-typing/worlds/preview":[runWorldRegistryPreview,"worlds"],
    "/api/admin/space-typing/stages/preview":[runStageConfigPreview,"stages"],
  };
  if(request.method==="POST"&&previewHandlers[url.pathname]){const input=await body(request);const active=await store.getRuntimeConfig();const [run,key]=previewHandlers[url.pathname];json(response,200,await run({rootDir:root,contract,policy:input.policy??active.content?.[key]}));return;}
  if(request.method==="POST"&&url.pathname==="/api/admin/space-typing/validate-revision"){const input=await body(request);json(response,200,await store.validateRevision(input.revision));return;}
  if(request.method==="POST"&&url.pathname==="/api/admin/space-typing/revisions"){json(response,201,await store.createRevision(await body(request)));return;}
  if(request.method==="POST"&&url.pathname==="/api/admin/space-typing/publish"){json(response,200,await store.publish(await body(request)));return;}
  if(request.method==="POST"&&url.pathname==="/api/admin/space-typing/rollback"){json(response,200,await store.rollback(await body(request)));return;}
  json(response,404,{error:"not-found"});
}catch(error){
  if(error instanceof AdminConflictError){json(response,409,{error:"conflict",message:error.message});return;}
  if(error instanceof AdminValidationError){json(response,400,{error:"validation",message:error.message});return;}
  if(error instanceof TypeError&&String(error.message).startsWith("Unsupported typing-content kind:")){json(response,400,{error:"validation",message:error.message});return;}
  if(error instanceof MusicAssetError){json(response,error.status,{error:"music-asset",message:error.message});return;}
  const previews=[[WorldMusicPreviewError,"preview-error"],[ShipRegistryPreviewError,"ships-preview-error"],[EquipmentRegistryPreviewError,"equipment-preview-error"],[SkillRegistryPreviewError,"skills-preview-error"],[EnemyRegistryPreviewError,"enemies-preview-error"],[BossRegistryPreviewError,"bosses-preview-error"],[WorldRegistryPreviewError,"worlds-preview-error"],[StageConfigPreviewError,"stages-preview-error"]];
  for(const [Type,code] of previews){if(error instanceof Type){json(response,502,{error:code,message:error.message});return;}}
  console.error(error);json(response,500,{error:"internal-error"});
}});
server.listen(port,host,()=>{console.log(`Space Typing Admin service: http://${host}:${port}`);if(token==="local-dev")console.log("Admin auth token: local-dev (local development default)");});

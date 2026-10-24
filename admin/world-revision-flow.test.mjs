import assert from "node:assert/strict";
import { mkdtemp, rm } from "node:fs/promises";
import { tmpdir } from "node:os";
import { join } from "node:path";
import test from "node:test";
import { createDefaultSpaceTypingConfig } from "./default-config.mjs";
import { createWorldRuntimeEnvelope } from "./world-runtime.mjs";
import { SpaceTypingRevisionStore } from "./space-typing-store.mjs";

const contract={contractRevision:"space-typing-admin-v1",configSchemaVersion:1,worldMusicCatalogSchemaVersion:1,worlds:{count:50,authorableFields:["enemyRoster"],constraints:{enemyRoster:{minItems:1,maxItems:64,unique:true}}},enemies:{ids:["rainbow-dart"]},applyBoundaries:{worldPolicy:"new-session"}};

async function fixture(){const rootDir=await mkdtemp(join(tmpdir(),"typing-game-world-flow-"));const store=new SpaceTypingRevisionStore({rootDir,contract});const seed=createDefaultSpaceTypingConfig(contract);seed.content={worlds:seed.content.worlds};await store.initialize(seed);return{store,rootDir};}

test("B06.6 World Draft -> Publish -> Runtime -> Rollback is revision isolated",async(t)=>{const{store,rootDir}=await fixture();t.after(()=>rm(rootDir,{recursive:true,force:true}));const seed=await store.getActiveRevision();const config=structuredClone(seed.config);config.content.worlds={configRevision:"worlds-test-v2",worlds:{"world-01":{enemyRoster:["rainbow-dart"]}}};const draft=await store.createRevision({baseRevision:seed.revision,config,message:"World roster override"});let runtime=createWorldRuntimeEnvelope(await store.getState(),await store.getRuntimeConfig(),contract);assert.deepEqual(runtime.policy.worlds,{});await store.publish({revision:draft.revision,expectedActiveRevision:seed.revision});runtime=createWorldRuntimeEnvelope(await store.getState(),await store.getRuntimeConfig(),contract);assert.deepEqual(runtime.policy.worlds["world-01"].enemyRoster,["rainbow-dart"]);await store.rollback({targetRevision:seed.revision,expectedActiveRevision:draft.revision});runtime=createWorldRuntimeEnvelope(await store.getState(),await store.getRuntimeConfig(),contract);assert.deepEqual(runtime.policy.worlds,{});});
